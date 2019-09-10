# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from kafka import KafkaProducer
import  re
class LianjiaPipeline(object):
    def open_spider(self,spider):
        self.kafka=KafkaProducer(bootstrap_servers='192.168.40.132:9092')
    def close_spider(self,spider):
        self.kafka.close()
    def process_item(self, item, spider):
        data= re.sub(r'\n','',str(item))

        self.kafka.send("lianjiaershou",data.encode(encoding="utf-8"))
        return item
