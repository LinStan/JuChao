# JuChao
一个基于scrapy框架的巨潮网pdf下载爬虫
# 使用说明
运行pachong文件夹下的entrypoint.py文件，将自动获取巨潮网上从2017-2-28号起向后推算365天的年度报告pdf。<br>
并且保存在D：\juchao\test1文件夹下，文件名为巨潮网上的文档编号<br>
如果想要下载其他类型的pdf文件可以自定更换Test1.py中的noticeType=010301中的010301换成你想要的报告类型就好，具体代码如下<br>

新添加一个批量转换txt文件的py类，可以批量转换一个文件夹下所有pdf文件为txt文件，并且尽量保持原有格式。（无法保持表格数据格式）
如果有人对于提取pdf中的表格数据有想法和实践过的好方法，请留言，万分感谢。
# 环境要求
Python 3.5.2<br>
scrapy 1.3.3
win10系统可以选择通过anaconda来安装会方便很多
# 引用包
scrapy、
urllib、
time
