
BOT_NAME = "DJ"

SPIDER_MODULES = ["DJ.spiders"]
NEWSPIDER_MODULE = "DJ.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# ITEM_PIPELINES = {"scrapy.pipelines.files.FilesPipeline": 1}
ITEM_PIPELINES = {"DJ.pipelines.CustomFilesPipelines": 1}


FILES_STORE = 'downloaded_files'


# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
