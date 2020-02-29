# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from festalist.models import FestaList


class FestascraperPipeline(object):
    def process_item(self, item, spider):
        festalist = FestaList()
        festalist.title = item['title']
        festalist.organizer = item['organizer']
        festalist.date = item['date']
        festalist.price = item['price']
        festalist.image = item['image']
        festalist.save()
        return item
