import time,datetime
import csv,os
'''
生成需要的网址列表

最开始不会使用start_request方法于是打算生成所有需要爬取的网址再进行批量爬取，现在已经无用了

'''
csvFile = open("./urls.csv", "w",newline='')
writer = csv.writer(csvFile)
writer.writerow(('num','url'))

seDate = int(time.time())

a = "2017-2-27"

aa = time.strptime(a, "%Y-%m-%d")

seDate = int(time.mktime(aa))




for i in range(1,365):

    seDate1 = time.strftime("%Y-%m-%d", time.localtime(seDate))

    seDate2 = str(seDate1)
    #seDate3 = seDate2.decode()

    writer.writerow((seDate2, 'http://www.cninfo.com.cn/search/search.jsp?noticeType=010301&startTime='
                     +seDate2+'&endTime='+seDate2+'&pageNo='))

    seDate = seDate + 86400

