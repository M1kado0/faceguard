# frontend/CLAUDE.md — Web Apps (Public Site + Admin Panel)

> Read the root [`CLAUDE.md`](../CLAUDE.md) first for project-wide rules.

This directory contains **two separate FastAPI web applications** that render server-side HTML. They share templates and static assets via `frontend/shared/`.

**Both apps are pure Python.** The only JavaScript in the whole project is ~50 lines in `shared/static/js/webcam.js` for liveness capture.

---

## Why This Stack?

This is a beginner-friendly stack chosen to minimize cognitive load:

- **FastAPI** — the developer already knows it
- **Jinja2** — Python-like template syntax, integrates natively with FastAPI
- **HTMX** — interactivity via HTML attributes, no JavaScript required for most things
- **Tailwind CSS via CDN** — styling without a build step
- **DaisyUI** — pre-built styled components on top of Tailwind

**No build step. No Node.js. No npm. No TypeScript. No React.**

If you find yourself reaching for a JS library, **stop and ask if HTMX can do it first** (it probably can).

---

## Layout

```
frontend/
├── public-site/                # End-user-facing app (port 8000)
│   ├── main.py                 # FastAPI app entry point
│   ├── routers/
│   │   ├── auth.py             # /login, /register, /verify
│   │   ├── enroll.py           # /enroll (with liveness)
│   │   ├── search.py           # /search (with liveness)
│   │   ├── matches.py          # /matches
│   │   ├── takedowns.py        # /takedowns
│   │   ├── settings.py         # /settings, GDPR controls
│   │   └── billing.py          # /billing (Stripe)
│   ├── templates/
│   │   ├── pages/              # Full pages (extend base.html)
│   │   └── partials/           # HTMX response fragments
│   ├── services/
│   │   └── api_client.py       # Calls backend JSON API
│   └── tests/
├── admin-panel/                # Admin-only app (port 8001)
│   ├── main.py
│   ├── routers/
│   │   ├── auth.py             # Admin login
│   │   ├── users.py            # /admin/users
│   │   ├── audit.py            # /admin/audit
│   │   ├── crawler.py          # /admin/crawler
│   │   ├── models.py           # /admin/models
│   │   ├── clusters.py         # /admin/clusters
│   │   ├── takedowns.py        # /admin/takedowns
│   │   └── analytics.py        # /admin/analytics
│   ├── templates/
│   ├── services/
│   └── tests/
└── shared/                     # Shared across both apps
    ├── templates/
    │   ├── base.html           # Base layout (Tailwind, HTMX, DaisyUI imports)
    │   ├── partials/
    │   │   ├── navbar.html
    │   │   ├── flash_messages.html
    │   │   └── ...
    │   └── macros/             # Reusable Jinja2 macros
    │       ├── forms.html      # Form field macros
    │       └── ...
    ├── static/
    │   ├── css/
    │   │   └── custom.css      # App-specific styles
    │   ├── js/
    │   │   └── webcam.js       # THE ONLY JS FILE
    │   └── img/
    ├── api_client/             # Shared backend API client (Python)
    │   ├── client.py
    │   └── models.py
    └── auth/                   # Shared auth helpers
        └── session.py
```

---

## Running the Apps

```bash
# Public site
uv run uvicorn frontend.public-site.main:app --reload --port 8000

# Admin panel
uv run uvicorn frontend.admin-panel.main:app --reload --port 8001
```

Both apps:
- Talk to the **backend API** (port 8002) via HTTP for data
- Share session storage (Redis) for SSO across the two apps if needed
- Run in separate processes — they can be deployed and scaled independently

---

## Base Template

`shared/templates/base.html` is the foundation:

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}FaceGuard{% endblock %}</title>

    <!-- Tailwind via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- DaisyUI components -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@4.x/dist/full.min.css" rel="stylesheet">

    <!-- HTMX -->
    <script src="https://unpkg.com/htmx.org@2.0.0"></script>

    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', path='/css/custom.css') }}">

    {% block head %}{% endblock %}
</head>
<body class="min-h-screen bg-base-200">
    {% include "partials/navbar.html" %}

    <main class="container mx-auto p-4">
        {% include "partials/flash_messages.html" %}
        {% block content %}{% endblock %}
    </main>

    {% block scripts %}{% endblock %}
</body>
</html>
```

In production, switch from CDN Tailwind to a built CSS file. Keep this for development.

---

## HTMX Patterns

### Form submission with inline result swap

```html
<form hx-post="/search"
      hx-target="#results"
      hx-swap="innerHTML"
      hx-encoding="multipart/form-data"
      hx-indicator="#loading">
    <input type="file" name="photo" accept="image/*" required class="file-input">
    <button class="btn btn-primary">Search</button>
    <span id="loading" class="htmx-indicator loading loading-spinner"></span>
</form>

<div id="results"></div>
```

Backend handler returns an HTML fragment (a `partials/` template), not JSON:

```python
@router.post("/search", response_class=HTMLResponse)
async def search(
    request: Request,
    photo: UploadFile,
    user: User = Depends(get_current_user),
):
    # Liveness check FIRST
    if not await liveness_check(photo):
        return templates.TemplateResponse(
            "partials/liveness_failed.html",
            {"request": request},
            status_code=403,
        )

    matches = await api_client.search(photo, user.token)
    return templates.TemplateResponse(
        "partials/search_results.html",
        {"request": request, "matches": matches},
    )
```

### Polling for async results

```html
<div hx-get="/matches/status"
     hx-trigger="every 3s"
     hx-target="this"
     hx-swap="outerHTML">
    Scanning...
</div>
```

### Confirm before destructive actions

```html
<button hx-delete="/enrollments/{{ enrollment.id }}"
        hx-confirm="Delete this enrollment? This removes your face from monitoring."
        hx-target="#enrollment-{{ enrollment.id }}"
        hx-swap="outerHTML"
        class="btn btn-error btn-sm">
    Delete
</button>
```

### Modal dialogs

Use DaisyUI's `<dialog>` modal pattern — server returns the modal content, HTMX swaps it in, dialog opens via `showModal()`:

```html
<button hx-get="/takedowns/new?match_id={{ match.id }}"
        hx-target="#modal-content"
        onclick="document.getElementById('takedown-modal').showModal()"
        class="btn btn-warning">
    Request Takedown
</button>

<dialog id="takedown-modal" class="modal">
    <div class="modal-box" id="modal-content"></div>
</dialog>
```

---

## Forms

Use **WTForms** with **starlette-wtf** integration. Define forms once in Python, render via Jinja2 macros.

```python
# forms.py
from starlette_wtf import StarletteForm
from wtforms import StringField, PasswordField, validators

class LoginForm(StarletteForm):
    email = StringField("Email", [validators.Email()])
    password = PasswordField("Password", [validators.Length(min=8)])
```

Template macro in `shared/templates/macros/forms.html`:

```html
{% macro render_field(field) %}
<div class="form-control">
    <label class="label" for="{{ field.id }}">
        <span class="label-text">{{ field.label.text }}</span>
    </label>
    {{ field(class="input input-bordered") }}
    {% if field.errors %}
        {% for error in field.errors %}
        <span class="text-error text-sm">{{ error }}</span>
        {% endfor %}
    {% endif %}
</div>
{% endmacro %}
```

---

## Liveness Capture (The Only JavaScript)

`shared/static/js/webcam.js` — the only JavaScript file in the project. Keep it small, well-commented, vanilla JS (no libraries).

Responsibilities:
1. Request webcam access (`getUserMedia`)
2. Show a face-positioning oval overlay
3. Record ~1 second of video
4. Stop the stream immediately after capture
5. Submit the blob to the backend via HTMX (programmatic trigger)

Sketch:

```javascript
// shared/static/js/webcam.js
async function startLivenessCapture(targetUrl, onComplete) {
    const video = document.getElementById('webcam-preview');
    const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'user', width: 640, height: 480 },
        audio: false,
    });
    video.srcObject = stream;

    // Record 1 second
    const recorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
    const chunks = [];
    recorder.ondataavailable = (e) => chunks.push(e.data);
    recorder.onstop = async () => {
        // IMPORTANT: stop the stream the moment we're done
        stream.getTracks().forEach(t => t.stop());

        const blob = new Blob(chunks, { type: 'video/webm' });
        const formData = new FormData();
        formData.append('liveness_blob', blob, 'capture.webm');

        // Send via fetch, then trigger HTMX swap with response
        const response = await fetch(targetUrl, { method: 'POST', body: formData });
        const html = await response.text();
        document.getElementById('liveness-result').innerHTML = html;
        // Triggers HTMX to process the new content
        htmx.process(document.getElementById('liveness-result'));
    };

    recorder.start();
    setTimeout(() => recorder.stop(), 1000);
}
```

This is the **only** place to add JavaScript. If you need more interactivity elsewhere, use HTMX. If HTMX can't do it, **propose an ADR before adding more JS**.

---

## Backend API Client

`shared/api_client/client.py` wraps the backend JSON API. Both web apps use it.

```python
import httpx
from typing import Any

class BackendClient:
    def __init__(self, base_url: str):
        self._client = httpx.AsyncClient(base_url=base_url, timeout=30.0)

    async def login(self, email: str, password: str) -> dict[str, Any]:
        r = await self._client.post("/v1/auth/login", json={"email": email, "password": password})
        r.raise_for_status()
        return r.json()

    async def search(self, photo_bytes: bytes, token: str) -> list[dict]:
        r = await self._client.post(
            "/v1/search",
            files={"photo": photo_bytes},
            headers={"Authorization": f"Bearer {token}"},
        )
        r.raise_for_status()
        return r.json()["matches"]

    # ... etc
```

**Never** call the backend with raw `httpx` from a route handler — always go through this client.

---

## Authentication

Use **fastapi-users** in the backend for auth state. The web apps just hold a session cookie containing the JWT.

```python
# shared/auth/session.py
from fastapi import Cookie, Depends, HTTPException

async def get_current_user(session_token: str = Cookie(None)) -> User:
    if not session_token:
        raise HTTPException(401, "not_authenticated")
    user = await api_client.get_me(token=session_token)
    return user
```

Public-site routes that require auth use `Depends(get_current_user)`. Admin panel routes additionally check `user.role in ["admin", "moderator"]`.

The admin panel runs on a **separate domain** in production (`admin.faceguard.io`) to isolate blast radius if either app is compromised.

---

## Public Site Pages

| Route | Purpose |
|---|---|
| `/` | Landing page (logged out) or dashboard (logged in) |
| `/register` | Account creation |
| `/login` | Login |
| `/verify` | Email verification |
| `/enroll` | Add a face to be monitored (with liveness) |
| `/search` | Search for matches (with liveness) |
| `/matches` | Match dashboard |
| `/matches/{id}` | Match detail page |
| `/takedowns` | Takedown requests list |
| `/takedowns/{id}` | Takedown detail page |
| `/settings` | Account settings, GDPR controls |
| `/settings/export` | Download my data (GDPR portability) |
| `/settings/delete` | Delete my account (GDPR erasure) |
| `/billing` | Plan management (if SaaS) |

---

## Admin Panel Pages

| Route | Purpose |
|---|---|
| `/login` | Admin login |
| `/users` | User management |
| `/users/{id}` | User detail (read-only biometric data — never expose embeddings) |
| `/audit` | Audit log viewer (filterable, exportable) |
| `/crawler` | Spider health, throughput |
| `/crawler/blocklist` | Manage blocked domains |
| `/models` | Current model versions, trigger re-embedding |
| `/clusters` | Face cluster review (merge/split) |
| `/takedowns` | Review pending takedown requests |
| `/analytics` | Dashboards |

---

## Design Tokens

Pick a theme in `data-theme` on `<html>`. DaisyUI ships with themes; `light` and `dark` are good defaults.

- **Primary action**: blue (`btn-primary`) — for safe, expected actions
- **Warning**: yellow (`btn-warning`) — for takedown requests, role changes
- **Destructive**: red (`btn-error`) — for delete actions only
- **Never use red as a primary action color**

---

## Accessibility

- Every form input has a `<label>`
- HTMX swaps include focus management (`hx-on::after-swap`)
- Color contrast meets WCAG 2.1 AA
- Webcam UI has audio prompts for visually impaired users
- Don't ship a face-handling component without an accessibility review

---

## Internationalization (Later)

Use **babel** with **fastapi-babel** for translations. Start English-only; add `de`, `fr`, `es` for GDPR jurisdictions in a later phase.

---

## Testing

```bash
# Unit tests
uv run pytest frontend/public-site/tests/
uv run pytest frontend/admin-panel/tests/

# Integration tests (requires backend running)
uv run pytest frontend/tests/integration/
```

Use FastAPI's `TestClient`. For HTMX flows, test that the right HTML fragment comes back, not just status codes:

```python
def test_search_returns_results_fragment(client, logged_in_user):
    response = client.post("/search", files={"photo": ("face.jpg", FAKE_FACE_BYTES)})
    assert response.status_code == 200
    assert 'id="search-results"' in response.text
    assert "match-card" in response.text
```

---

## Common Tasks

### Add a new page
1. Add route in the appropriate `routers/*.py`
2. Create template in `templates/pages/`
3. Extend `base.html`: `{% extends "base.html" %}`
4. Add to navbar if it's a top-level page
5. Test that it renders with `pytest`

### Add an HTMX interaction
1. Add an `hx-*` attribute to a button or form
2. Create the route handler that returns an HTML fragment
3. Create the partial template in `templates/partials/`
4. Test the swap behavior

### Add a new form
1. Define WTForm in `forms.py`
2. Use `render_field` macro in template
3. Handle validation in the route handler
4. On error, re-render the form with messages; on success, redirect or HTMX swap

### Share a template between the two apps
1. Put it in `shared/templates/`
2. Both apps' Jinja2 environments include `shared/templates/` in their search path

---

## What NOT to Do (Frontend-Specific)

- ❌ Do **not** add JavaScript outside `shared/static/js/webcam.js` without an ADR
- ❌ Do **not** install npm packages or set up a build step
- ❌ Do **not** introduce React, Vue, Alpine, or any other JS framework
- ❌ Do **not** return JSON from route handlers — return HTML (these are web apps, not APIs)
- ❌ Do **not** call the database or vector DB directly from route handlers — go through the backend API
- ❌ Do **not** persist raw face/liveness blobs in localStorage or IndexedDB
- ❌ Do **not** keep the webcam stream alive after capture completes — call `getTracks().forEach(t => t.stop())`
- ❌ Do **not** ship enrollment/search flows without explicit consent UI
- ❌ Do **not** put the admin panel on the same domain as the public site in production
- ❌ Do **not** use `{{ user_input | safe }}` in templates — Jinja2 autoescape protects against XSS, don't bypass it

---

## Beginner Tips

- **HTMX docs are short and excellent**: https://htmx.org/docs/
- **DaisyUI components**: https://daisyui.com/components/ — copy-paste-ready
- **Tailwind cheat sheet**: https://nerdcave.com/tailwind-cheat-sheet
- **FastAPI templates**: https://fastapi.tiangolo.com/advanced/templates/
- **Read the HTMX hypermedia essays** (`hypermedia.systems`) once you have the basics — they explain the philosophy and will save you from over-engineering
- **When in doubt, render server-side.** That's the whole point of this stack.