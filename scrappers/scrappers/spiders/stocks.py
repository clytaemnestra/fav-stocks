import scrapy


class Stocks(scrapy.Spider):
    name = "stocks"
    start_urls = ["https://swingtradebot.com/equities"]

    def parse(self, response):
        for i in response.xpath('//*[@class="table table-striped table-bordered"]//tbody'):
            table = response.xpath('//*[@class="table table-striped table-bordered"]//tbody')
            rows = table.xpath('//tr')

            yield {
                'id': i,
                'symbol': rows.xpath('td/a/text()')[0].extract(),
                'price': rows.xpath('td[7]/text()')[0].extract()
            }

        next_page = response.css('a.next.btn.btn-primary').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

