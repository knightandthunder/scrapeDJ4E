# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()

