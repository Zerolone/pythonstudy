# -*- coding: utf-8 -*-

'''
scrapy crawl example

输出json格式
scrapy crawl z1 -o sss_z1.json -t json

'''

import scrapy
import json
import re


class Z1Spider(scrapy.Spider):
    name = 'z1'
    allowed_domains = ['news.fjsen.com']
    start_urls = []

    urlFix = 'http://news.fjsen.com/';
    urls = open('sss_re.json');
    urlsArr = json.load(urls)
    #print  urlsArr;

    for url in urlsArr:
      #print url;       print '-----' * 10;
      tmpUrl = urlFix + url['url'];

      #print tmpUrl; print '-----' * 10;


      start_urls.append(tmpUrl);
      #break;

    print start_urls;
    #exit();



    def parse(self, response):
        filename  = response.url.split('/')[-2];
        filename  = 'html/' + response.url.split('/')[-1];


        print filename;        print '-----' * 10;

        #save
        #f = open(filename, 'wb'); f.write(response.body);

        items=[];
        myItems = re.findall('<h1>([\s\S]+?)</h1>[\s\S]+?<span id="pubtime_baidu">(.+?)</span>[\s\S]+?<span id="editor_baidu">责任编辑：(.+?)</span>[\s\S]+?<td id="new_message_id">([\s\S]+?)</td>', response.body, re.I | re.M);
        for i in myItems:
          items.append({
            'title'   : i[0].strip(),
            'uptime'  : i[1],
            'author'  : i[2],
            'content' : i[3],
          });

        print items;
        #exit();

        return items;
