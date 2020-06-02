#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        # 这里重新定义了处理开始标签的函数
        self.CurrentData = tag
        print(tag)
        # if tag == "movie":
        #     print("*****Movie*****")
        #     title = attributes["title"]
        #     print("Title:", title)

    def endElement(self, tag):
        print(tag)
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    def characters(self, data):
        print(data)
        if self.CurrentData == "type":
            self.type = data
        elif self.CurrentData == "format":
            self.format = data
        elif self.CurrentData == "year":
            self.year = data
        elif self.CurrentData == "rating":
            self.rating = data
        elif self.CurrentData == "stars":
            self.stars = data
        elif self.CurrentData == "description":
            self.description = data


# 创建一个 XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# 重写 ContextHandler
Handler = MovieHandler()
parser.setContentHandler(Handler)

parser.parse("xml_movies.xml")
