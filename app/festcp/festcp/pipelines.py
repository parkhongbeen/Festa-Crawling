# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from festalist.models import FestaList


class FestcpPipeline(object):
    def process_item(self, item, spider):
        festa = FestaList()
        festa.title = item['title']
        festa.image = item['image']
        festa.host = item['host']
        festa.date = item['date']
        festa.content = item['content']
        festa.apply = item['apply']
        festa.tickets = item['tickets']
        festa.link = item['link']
        festa.save()
        return item
