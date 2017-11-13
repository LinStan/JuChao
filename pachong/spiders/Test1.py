# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup,BeautifulStoneSoup
from pachong.items import PachongItem
import time,datetime
import urllib

class PCSpider(CrawlSpider):
    name = "pachong"
    #爬取网址的主域名
    allowed_domains = ["cninfo.com.cn"]
    #start_urls = ['http://www.cninfo.com.cn/search/search.jsp?noticeType=010301&#startTime=2017-02-01&endTime=2017-02-28&pageNo=']
    # 010301是年度报告的类型代码，如果需要爬取其他类型可以自行替换即可
    bash_url = 'http://www.cninfo.com.cn/search/search.jsp?noticeType=010301&startTime='

    #自定义爬取网址规则
    def start_requests(self):
        #向后遍历天数
        n=365
        #起始爬取日期
        a = "2017-02-28"
        #转化为对应格式
        aa = time.strptime(a, "%Y-%m-%d")
        #转化时间戳
        seDate = int(time.mktime(aa))

        while n > 0:
            seDate1 = time.strftime("%Y-%m-%d", time.localtime(seDate))
            seDate2 = str(seDate1)
            # print(seDate2)

            '''
            for i in range(1,5):

                url = self.bash_url + str(seDate2) + '&endTime=' + str(seDate2) + '&pageNo=' + str(i)
                yield Request(url, self.parse)
            '''
            url = self.bash_url + str(seDate2) + '&endTime=' + str(seDate2) + '&pageNo='
            yield Request(url, self.parse)
            seDate = seDate + 86400

            n = n - 1
            #返回url


    def parse(self, response):
        #print(response.xpath('//div[@class="g_width"]/span[@class="count"]/text()'))
        items =[]
        item = PachongItem()
        #xpath匹配式
        id = response.xpath('//table/tbody/tr/td[@class="dm"]/text()').extract()
        link=response.xpath('//table/tbody/tr/td[@class="qsgg"]/a/@href').extract()
        title = response.xpath('//table/tbody/tr/td[@class="qsgg"]/a/text()').extract()
        count = response.xpath('//div[@class="g_width"]/span[@class="count"]/text()').extract()

        item['pdf_id']=id
        '''
        html =[]
        if link:
            for i in (0, len(link)+1):
                html[i]='http://www.cninfo.com.cn/'+str(link[i])
        item['pdf_link']=html
        '''
        item['pdf_link']=link
        item['pdf_title']=title
        zip1 = zip(item['pdf_id'],item['pdf_link'],item['pdf_title'])
        print(zip1)


        yield item

        max_page =response.xpath('//*[@id="nright"]/div[2]/span[1]/span/a/text()').extract()
        p = response.url[-1]
        print(p)
        if max_page:
            if p=='=':
                for i in range(2,int(max_page[-1])+1):
                    url = response.url+str(i)
                    print(url)
                    yield Request(url,callback=self.parse)

            #print(max_page[-1])