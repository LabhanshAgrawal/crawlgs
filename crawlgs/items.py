# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlgsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    URL = scrapy.Field()
    Year = scrapy.Field()
    Citations = scrapy.Field()
    Versions = scrapy.Field()
    Cluster_ID= scrapy.Field()
    Citations_list = scrapy.Field()
    Versions_list = scrapy.Field()
    Excerpt = scrapy.Field()
