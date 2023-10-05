import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    def parse(self, response):
        lis = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in lis:
            name = li.xpath('./div[1]/div[2]/div[1]/a/span[1]/text()').extract_first()
            score = li.xpath('./div[1]/div[2]/div[2]/div[1]/span[2]/text()').extract_first()
            people = li.xpath('./div[1]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
            desc = li.xpath('./div[1]/div[2]/div[2]/p/span/text()').extract_first()
            print(name,score,people,desc)
            yield {
                "name":name,
                "score":score,
                "people":people,
                "desc":desc
            }

        next_page_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        if next_page_url != None:
            url = response.urljoin(next_page_url)
        yield scrapy.Request(url=url,callback=self.parse)
