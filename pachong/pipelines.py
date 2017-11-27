# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
import pachong.items,pachong.settings
import urllib

class PachongPipeline(object):
    #def process_item(self, item, spider):
    #    return item
    '''
    def process_item(self, item, spider):
        dir_path = '%s/%s'%(pachong.settings.PDF_STORE,spider.name)#存储路径
        print ('dir_path',dir_path)
        #url_head = 'www.cninfo.com.cn'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for pdf_url in item['pdf_link']:
            list_name = pdf_url.split('/')
            file_name = list_name[len(list_name)-1]#文件名
            # print 'filename',file_name
            file_path = '%s/%s'%(dir_path,file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue
            with open(file_path,'wb') as file_writer:
                conn = urllib.request.urlopen('http://www.cninfo.com.cn'+pdf_url)#下载
                file_writer.write(conn.read())
            file_writer.close()
        return item
        '''
    def process_item(self, item, spider):
        dir_path = '%s/%s' % (pachong.settings.PDF_STORE, spider.name)
        # 存储路径为PDF_STORE/spider_name
        # 目前为当前目录下的output下的pachong文件夹下
        print('dir_path', dir_path)
        # url_head = 'www.cninfo.com.cn'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for pdf_url in item['pdf_link']:
            list_name = pdf_url.split('/')
            file_name = list_name[len(list_name) - 1]# 文件名为 网址最后的一串文件编码
            #file_name = list
            # print 'filename',file_name
            file_path = '%s/%s' % (dir_path, file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue
            with open(file_path, 'wb') as file_writer:
                conn = urllib.request.urlopen('http://www.cninfo.com.cn' + pdf_url)  # 下载pdf
                file_writer.write(conn.read())
            file_writer.close()
        return item

