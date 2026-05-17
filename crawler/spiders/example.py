"""Example spider — copy this file to add a new source."""

from crawler.spiders.base import BaseSpider


class ExampleSpider(BaseSpider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/gallery"]

    def parse(self, response):
        for img_url in response.css("img::attr(src)").getall():
            yield self.make_image_item(
                url=response.urljoin(img_url),
                source_page=response.url,
            )
