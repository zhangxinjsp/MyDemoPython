#coding=utf-8

import urllib2
import HTMLParser
import re

urlArray = ["http://www.baidu.com"]
urlAlready = []

def getHTML(url) :
    try :
        response = urllib2.urlopen(url)
        return response.read()
    except IOError:
        print("========================== get html IOError", url)
    except UnicodeDecodeError:
        print("========================== get html UnicodeDecodeError", url)
    return ""

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag ==  'a' :
            for name,value in attrs:
                try :
                    if value != None and "http" in value and value not in urlArray and value not in urlAlready :
                        print("tag : %s === %s : %s" % (tag, name, value))
                        urlArray.append(value)
                except IOError:
                    print("========================== handle_starttag IOError")
                except UnicodeDecodeError:
                    print("========================== handle_starttag UnicodeDecodeError")
    def handle_endtag(self, tag):
        print('end', tag)
    
    def handle_data(self, data):
        print('data')

my = MyParser()
# 传入要分析的数据，是html的。
while len(urlArray) > 0:
    url = urlArray[0]
    if url in urlAlready:
        print('<<<<<<<<<<<<<<<<<<<,already load url', len(urlAlready))
        urlArray.remove(url)
        continue
    try :
        print("++++++++++++++++++++++++++", url)
        html = getHTML(url)
        if 'html' in html :
            print("feed start")
            my.feed(html)
            print("feed end")
    except IOError:
        print("========================== IOError", url)
    except UnicodeDecodeError:
        print("========================== UnicodeDecodeError", url)
    urlArray.remove(url)
    urlAlready.append(url)


