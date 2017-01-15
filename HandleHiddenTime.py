# -*- coding: utf-8 -*-
import re
file = open(r'output.txt','r')
fileread = file.read()
oldSentences = re.findall('(.+?(?:。”|。|！|？|……|；|，))' ,fileread)#将句子进行划分，注意标点是中文标点
flagTime = ""
newSentences = []
for s in oldSentences:
    fullTime = re.search(r'\d+年',s)#检测年
    sameYear = re.search(r'同年',s)#检测同年
    noYear = re.search(r'(?<!年\d)(?<!年)\d+月[0-9]*(日)*', s)
    p = s
    if fullTime is not None:
        flagTime = fullTime.group()
    if sameYear is not None:
        p = s.replace('同年',flagTime)
    if noYear is not None:
        p = s.replace(noYear.group(),flagTime+noYear.group())
    print "O:"+s
    print "N:"+p+"\n"
    newSentences.append(p)
para = ''.join(newSentences)#把list合并成一个字符串
print para
output = open('output_replaceTime.txt','w')
output.write(para)
output.close()
