#!/usr/bin/env python
#coding:utf-8

import urllib
import re

def getHtml(url):
    html = urllib.urlopen(url)
    sorce = html.read()
    return sorce

def getRange(content):
    start0 = content.find(r'<div class="entry">')
    start = content.find(r'<ol>',start0)
    end = content.find(r'<div id="ad1">',start)
    content2 = content[start:end]
    return content2

def getLink(content2):
    reg = re.compile(r'<a href="(.*?[.html|.pdf]?)" target=')
    result = reg.findall(content2)
    return result

def getName(content2):
    reg = re.compile(r'<a href=".*?[.html|.pdf]?" target="_blank">(.*?)</a>')
    result2 = reg.findall(content2)
    return result2

if __name__ == '__main__':
    content = getHtml(r'http://blog.jobbole.com/29281/')
    content2 = getRange(content)
    link = getLink(content2)
    name = getName(content2)
    i = 1
    f = open('content.txt','w+')
    for x, y in zip(name, link):
        print >>f, str(i),": ",x,
        print >>f
        print >>f,y
        i = i + 1