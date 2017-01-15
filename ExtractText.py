# -*- coding: utf-8 -*-
import re
from scrapy.selector import Selector

#file = open(r'/home/chaycao/Desktop/刘德华（中国香港男演员、歌手、词作人）_百度百科.html','r')
#file = open(r'/home/chaycao/Desktop/史蒂夫·乔布斯（美国苹果公司联合创始人）_百度百科.html','r')
file = open(r'/home/chaycao/Desktop/刘恺威_百度百科.html','r')

fileread = file.read()
#用Xpath提取出<div class="para"></div>中的所有内容
data = Selector(text=fileread).xpath('//div[@class="para"]').extract();
data = ''.join(data)#把list合并成一个字符串
data = data.encode("utf8")
#去掉所有的标签
dr = re.compile(r'<div class=\"description.*?</div>',re.S)#去除description
text = dr.sub('',data)
dr = re.compile(r'<sup.*?</sup>',re.S)#去除sup
text = dr.sub('',text)
dr = re.compile(r'<[^>]+>',re.S)
text = dr.sub('',text).replace("\n","")
print text

output = open('output.txt','w')
output.write(text)
output.close()