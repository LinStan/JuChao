# JuChao
一个基于scrapy框架的巨潮网pdf下载爬虫
# 使用说明
运行pachong文件夹下的entrypoint.py文件，将自动获取巨潮网上从2017-2-28号起向后推算365天的年度报告pdf。
并且保存在D：\juchao\test1文件夹下，文件名为巨潮网上的文档编号。
如果想要下载其他类型的pdf文件可以自定更换Test1.py中的noticeType=010301中的010301换成你想要的报告类型就好，具体代码如下
                  <option value="" >请选择公告类型</option>
                  <option value="010301" >年度报告</option>
                  <option value="010303" >半年度报告</option>
                  <option value="010305" >一季度报告</option>
                  <option value="010307" >三季度报告</option>
                  <option value="010116" >拟上市公司公告</option>
                  <option value="0102" >首次公开发行及上市</option>
                  <option value="0105" >配股</option>
                  <option value="0107" >增发</option>
                  <option value="0109" >可转换债券</option>
                  <option value="0110" >权证相关公告</option>
                  <option value="0111" >其它融资</option>
                  <option value="0113"  title="权益分派及限制出售股份上市">权益及限制出售股份</option>
                  <option value="0115" >股权变动</option>
                  <option value="0117" >交易</option>
                  <option value="0119" >股东大会</option>
                  <option value="0121"  title="澄清、风险提示、业绩预告事项">澄清、风险、业绩预告</option>
                  <option value="0125" >特别处理和退市</option>
                  <option value="0127" >补充及更正</option>
                  <option value="0129" >中介机构报告</option>
                  <option value="0131" >上市公司制度</option>
                  <option value="0123" >其它重大事项</option>
# 环境要求
Python 3.5.2
scrapy 1.3.3
win10系统可以选择通过anaconda来安装会方便很多
# 引用包
scrapy、
urllib、
time
