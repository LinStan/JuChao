# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PachongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_id = scrapy.Field()

    pdf_link = scrapy.Field()

    pdf_title = scrapy.Field()

    pdf_id = scrapy.Field()

    pdf_count = scrapy.Field()
    pass
