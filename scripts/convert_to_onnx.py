from pathlib import Path

import torch

from ml.liveness.model_lib.MiniFASNet import MiniFASNetV2


def main() -> None:
    pth_path = Path("ml/models/2.7_80x80_MiniFASNetV2.pth")
    onnx_path = Path("ml/models/MiniFASNetV2.onnx")

    model = MiniFASNetV2(
        embedding_size=128,
        conv6_kernel=(5, 5),
        drop_p=0.2,
        num_classes=3,
        img_channel=3,
    )

    state_dict = torch.load(pth_path, map_location="cpu")

    cleaned = {}
    for key, value in state_dict.items():
        if key.startswith("module."):
            key = key[len("module.") :]
        cleaned[key] = value

    model.load_state_dict(cleaned)
    model.eval()

    dummy = torch.randn(1, 3, 80, 80, dtype=torch.float32)

    torch.onnx.export(
        model,
        dummy,
        onnx_path.as_posix(),
        export_params=True,
        opset_version=11,
        do_constant_folding=True,
        input_names=["input"],
        output_names=["logits"],
        dynamic_axes={
            "input": {0: "batch_size"},
            "logits": {0: "batch_size"},
        },
    )

    print(f"Exported to {onnx_path}")


if __name__ == "__main__":
    main()
