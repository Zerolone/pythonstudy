# -*- coding: utf-8 -*-
import scrapy
import json
import re
import sys;

from ..items import Z018Item;

from scrapy.http import Request

urlFix = 'http://www.j.com/scrapy/';
urlFix = 'http://192.168.99.101/scrapy/';
#urlFix = 'http://www.zerolone.com/scrapy/';

class Z1Spider(scrapy.Spider):
    name = 'z1'
    ddid = 0;

    allowed_domains = ['jx.com','192.168.99.101']
    start_urls = []

    def __init__(self, ddid=0, *args, **kwargs):
      super(Z1Spider, self).__init__(*args, **kwargs)
      self.ddid = ddid
      print '-----------'
      print ddid;
      self.start_urls.append(urlFix + str(ddid) + '.html');

      print '----------------------------';
      print(self.start_urls);
      print '----------------------------';

    def parse(self, response):
        myItems = re.findall('<a href="(.+?)">(.+?)</a>', response.body, re.I | re.M);

        for i in myItems:
            url = urlFix + i[0];
            print url;

            yield Request(url, callback=self.parse_url)
          #print items;

        #return items;

    def parse_url(self, response):

        print '=================================='
        myItems = re.findall('{title([\s\S]+?)}[\s\S]+?{body([\s\S]+?)}', response.body, re.I | re.M);
        print myItems;

        for i in myItems:
            item = Z018Item();
            item['title']   = i[0];
            item['content'] = i[1];
            item['ddid']    = self.ddid;

            print item;
            yield item;

        #exit();
