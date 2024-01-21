from scrapy.pipelines.files import FilesPipeline


class CustomFilesPipelines(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return item.get("Title")
