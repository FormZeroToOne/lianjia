# -*- coding: utf-8 -*-
import scrapy
import  json

from  lianjia.items import LianjiaItem


class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    #allowed_domains = ['https://bj.lianjia.com/ershoufang/pg1/']
    start_urls = ['https://bj.lianjia.com/ershoufang/pg1/']

    def parse(self, response):
        jsonstr =response.css("div.page-box.house-lst-page-box::attr('page-data')").extract_first()
        datadict = json.loads(jsonstr)
        print("共有",datadict['totalPage'],"页")
        for i in range(1,datadict['totalPage']+1):
            # print("https://bj.lianjia.com/ershoufang/pg{page}/".format(page=i))
            url = "https://bj.lianjia.com/ershoufang/pg{page}/".format(page=i)
            yield  response.follow(url,self.list)

    def list(self,response):
        urls = response.css('div.title>a::attr("href")').extract()
        print(urls)
        print(len(urls))
        for url in urls:
            yield response.follow(url, self.detail)

    def detail(self,response):
        #print(response.css('span.total::text').extract_first())
        item = LianjiaItem()
        item["name"] = response.css('a.info::text').extract_first()
        item["zongjia"] = response.css('span.total::text').extract_first()
        item["danjia"] = response.css('span.unitPriceValue::text').extract_first()
        item["qu"] = "".join(response.css('div.areaName span.info a::text').extract())
        item["jianzhunian"] = response.css('div.area div.subInfo::text').extract_first()
        item["huxing"] = response.css('div.base div.content li:nth-child(1)::text').extract_first()

        item["louceng"] = response.css('div.base div.content li:nth-child(2)::text').extract_first()
        item["mianji"] = response.css('div.base div.content li:nth-child(3)::text').extract_first()
        item["huxingjiegou"] = response.css('div.base div.content li:nth-child(4)::text').extract_first()
        item["huxingleixing"] = response.css('div.base div.content li:nth-child(6)::text').extract_first()
        item["fangxiang"] = response.css('div.base div.content li:nth-child(7)::text').extract_first()
        item["zhuangxiu"] = response.css('div.base div.content li:nth-child(9)::text').extract_first()
        item["tihu"] = response.css('div.base div.content li:nth-child(10)::text').extract_first()
        item["gongnuan"] = response.css('div.base div.content li:nth-child(11)::text').extract_first()
        #print(item)
        item["dianti"] = response.css('div.base div.content li:nth-child(12)::text').extract_first()
        item["chanquan"] = response.css('div.base div.content li:nth-child(13)::text').extract_first()
        item["guapai"] = response.css('div.transaction div.content li:nth-child(1) span:nth-child(2)::text').extract_first()
        item["jiaoyiquanshu"] = response.css('div.transaction div.content li:nth-child(2) span:nth-child(2)::text').extract_first()
        item["shangcijiaoyi"] = response.css('div.transaction div.content li:nth-child(3) span:nth-child(2)::text').extract_first()
        item["fanghuyongtu"] = response.css('div.transaction div.content li:nth-child(4) span:nth-child(2)::text').extract_first()
        item["fangwunianxian"] = response.css('div.transaction div.content li:nth-child(5) span:nth-child(2)::text').extract_first()
        item["chanquansuoshu"] = response.css('div.transaction div.content li:nth-child(6) span:nth-child(2)::text').extract_first()
        item["diyaxinxi"] = str.strip(response.css('div.transaction div.content li:nth-child(7) span:nth-child(2)::text').extract_first())
        item["fangben"] = response.css('div.transaction div.content li:nth-child(8) span:nth-child(2)::text').extract_first()
        # 全部验证
        yield  item
