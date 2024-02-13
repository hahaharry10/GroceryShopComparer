import scrapy


class AsdaspiderSpider(scrapy.Spider):
    name = "asdaSpider"
    allowed_domains = ["groceries.asda.com"]
    asda_search_url = "https://groceries.asda.com/search/"
    start_urls = []

    def __init__(self, items):
        for item in items:
            self.start_urls.append(self.asda_search_url + str(item))
    #ENDINIT

    # USED FOR TESTING: Output the start urls.
    def printStart_urls(self):
        for url in self.start_urls:
            print(url)

    def parse(self, response):
        pass
#ENDCLASS

# Test init:
spider = AsdaspiderSpider(["apples", "oranges", "bananas"])
spider.printStart_urls()
