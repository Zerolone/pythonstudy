# -*- coding: utf-8 -*-
import scrapy

import re

from sss.items import SssItem

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['news.fjsen.com']
    #start_urls = ['http://news.fjsen.com/e_news.htm', 'http://news.fjsen.com/W_Comments.htm']
    start_urls = ['http://news.fjsen.com/e_news.htm']

    def parse(self, response):
        filename  = response.url.split('/')[-2];
        filename  = 'test_' + response.url.split('/')[-1];

        print '-' * 40;
        print filename;
        print '-' * 40;

        f = open(filename, 'wb');
        f.write(response.body);

        items=[];


        '''xpath''
        sel = scrapy.selector.Selector(response);
        sites = sel.xpath('/html/body/div[2]/div/div[1]/ul/li/a');
        sites = sel.xpath('/html/body/div[2]/div/div[1]/ul/li');

        for site in sites:
          #print site;
          title = site.xpath('a/text()').extract();

          url   = site.xpath('a/@href').extract();
          uptime = site.xpath('span/text()').extract();
          print title, url, uptime;

          item = SssItem();
          item['title'] = title;
          item['url']   = url;
          item['uptime'] = uptime;

          items.append(item);
        '''

        '''
        regex
        re.I	使匹配对大小写不敏感
        re.L	做本地化识别（locale-aware）匹配
        re.M	多行匹配，影响 ^ 和 $
        re.S	使 . 匹配包括换行在内的所有字符
        re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
        re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。        
        '''

        #print '----' * 10;        print myItems;        print '----' * 10;
        myItems = re.findall('<li><span>(.+?)</span><a href="(.+?)">(.+?)</a></li>', response.body, re.I);
        for i in myItems:
          items.append({
            'uptime': i[0], 'url' : i[1], 'title' : i[2]
          });







        ''''''
        


        return items;






