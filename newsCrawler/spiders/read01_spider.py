import scrapy


class Read01Spider(scrapy.Spider):
    name = "read01_spider"
    start_urls = [

        'https://read01.com/c710/',
    ]
    # scrapy.Request("https://read01.com/c710/",
    #                callback=self.parse2,
    #                dont_filter=True)
    def parse(self, response):
        # return scrapy.Request("https://read01.com/c710/",
        #                       callback=self.parse,
        #                       dont_filter=True)
        print str(response.css('div.title').extract(),'utf-8')

        # for title in response.css('div.title'):


