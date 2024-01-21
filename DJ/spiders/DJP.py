import scrapy

base_url = 'https://www.dj4e.com'


def parse_page(response):

    for links in response.css('.tsugi-lessons-module-slide-link'):
        link = links.css('a ::attr(href)').get()
        title = links.css('span a ::text').get()
        yield {
            'Title': title,
            'file_urls': [link]
        }


class DjpSpider(scrapy.Spider):
    name = "DJP"
    start_urls = ["https://www.dj4e.com/lessons"]

    def parse(self, response):
        url_list = response.css('i+a ::attr(href)').getall()
        for remaining_url in url_list:
            url = base_url + remaining_url
            yield scrapy.Request(url, callback=parse_page)
        # yield from self.parse_page(self, response)

