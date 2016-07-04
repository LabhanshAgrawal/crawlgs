import scrapy
import re

from crawlgs.items import CrawlgsItem

class crawlgsSpider(scrapy.Spider):
    name = "crawlgs"
    allowed_domains = ["https://scholar.google.co.in"]
    start_urls = [
        "https://scholar.google.com/scholar?as_sdt=1,5&q=einstein&hl=en&as_vis=1"
    ]
    def parse(self, response):
        item = CrawlgsItem()
        for x in range(2,12):
            item['Title'] = "".join(response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/h3/a/text() | //div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/h3/a/b/text()').extract()).encode('utf8')
            item['URL'] = response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/h3/a/@href').extract()[0].encode('utf8')
            item['Year'] = re.findall(r'\b\d{4}\b', response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/div[@class="gs_a"]').extract()[0])[0]
            item['Citations'] = re.split('</a>', re.split('Cited by ', response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/div[@class="gs_fl"]').extract()[0])[1])[0]
            item['Versions'] = re.split('All ', re.split(' version', response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/div[@class="gs_fl"]').extract()[0])[0])[1]
            item['Cluster_ID'] = re.split('&', re.split('cites=', response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/div[@class="gs_fl"]').extract()[0])[1])[0]
            item['Citations_list'] = 'https://scholar.google.co.in' + response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/div[@class="gs_fl"]/a[1]/@href').extract()[0]
            item['Versions_list'] = 'https://scholar.google.co.in' + response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/div[@class="gs_fl"]/a[@class="gs_nph"][1]/@href').extract()[0]
            item['Excerpt'] = ''.join(response.xpath('//div[@id="gs_ccl"]/div[' + str(x) + ']/div[@class="gs_ri"]/div[@class="gs_rs"]/text()').extract())
            yield item
