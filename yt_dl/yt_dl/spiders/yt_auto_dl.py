import scrapy


class YtAutoDlSpider(scrapy.Spider): # scrapy.Spider is sa required argument for this class
    name = 'yt_auto_dl'
    allowed_domains = ['youtube.com']
    start_urls = ['https://www.youtube.com/c/ClearedHotPodcast', 'https://www.youtube.com/c/AndrewHubermanLab', 'https://www.youtube.com/c/lexfridman',  ]

    def parse(self, response):
        pass
