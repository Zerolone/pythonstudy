# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Z018Pipeline(object):
    def process_item(self, item, spider):
      #print 'ZZZZZZZZZZZZZZZZZZZZZZZZ';

      ddid = item['ddid']

      # curl 访问接口
      import pycurl, StringIO

      # print '142-------------';
      # print pycurl.version_info();
      # print '142-------------';
      url = 'http://api.mingyihui.net:8082/common/info';
      url = 'http://api.mingyihui.net:8082/services/hospital/info';
      url = 'http://api.mingyihui.net:8082/services/feedback/add_scrapy'

      c = pycurl.Curl()
      # c.setopt(c.POST, 1)
      c.setopt(pycurl.URL, url)  # 设置要访问的网址 url = "http://www.cnn.com"
      c.setopt(pycurl.FOLLOWLOCATION, 1)  # 参数有1、2
      c.setopt(pycurl.MAXREDIRS, 5)  # 最大重定向次数,可以预防重定向陷阱

      # 连接超时设置
      c.setopt(pycurl.CONNECTTIMEOUT, 60)  # 链接超时
      # c.setopt(pycurl.TIMEOUT, 300) #下载超时
      # c.setopt(pycurl.HEADER, True)
      # c.setopt(c.HTTPHEADER, ["Content-Type: application/x-www-form-urlencoded","X-Requested-With:XMLHttpRequest","Cookie:"+set_cookie[0]])
      # 模拟浏览器
      c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
      # c.setopt(pycurl.AUTOREFERER,1)
      # c.setopt(c.REFERER, url)
      # cookie设置
      # Option -b/--cookie <name=string/file> Cookie string or file to read cookies from
      # Note: must be a string, not a file object.
      # c.setopt(pycurl.COOKIEFILE, "cookie_file_name")
      # Option -c/--cookie-jar Write cookies to this file after operation
      # Note: must be a string, not a file object.
      # c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
      # Option -d/--data HTTP POST data

      # post_data_dic = [{"name": "value"}]

      postData = 'ddid=%s&content=%s' % (ddid, item['content']);

      c.setopt(c.POSTFIELDS, postData);

      # 设置代理
      # c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)
      # c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)
      # 不明确作用
      # c.setopt(pycurl.HTTPPROXYTUNNEL,1) #隧道代理
      # c.setopt(pycurl.NOSIGNAL, 1)
      # 设置post请求， 上传文件的字段名 上传的文件
      # post_file = "/home/ubuntu/avatar.jpg"
      # c.setopt(c.HTTPPOST, [("textname", (c.FORM_FILE, post_file))])
      # 调试回调.调试信息类型是一个调试信 息的整数标示类型.在这个回调被调用时VERBOSE选项必须可用
      # c.setopt(c.VERBOSE, 1) #verbose 详细
      # c.setopt(c.DEBUGFUNCTION, test)
      # f = open("body", "wb")
      # c.setopt(c.WRITEDATA, f)
      # h = open("header", "wb")
      # c.setopt(c.WRITEHEADER, h)
      # print "Header is in file 'header', body is in file 'body'"
      # f.close()
      # h.close()
      # c.setopt(c.NOPROGRESS, 0)
      # c.setopt(c.PROGRESSFUNCTION, progress)
      # c.setopt(c.OPT_FILETIME, 1)
      # 访问,阻塞到访问结束

      b = StringIO.StringIO()
      c.setopt(c.WRITEFUNCTION, b.write)
      c.perform()  # 执行上述访问网址的操作

      '''
      print "HTTP-code:", c.getinfo(c.HTTP_CODE)  # 打印出 200(HTTP状态码)
      print "Total-time:", c.getinfo(c.TOTAL_TIME)
      print "Download speed: %.2f bytes/second" % c.getinfo(c.SPEED_DOWNLOAD)
      print "Document size: %d bytes" % c.getinfo(c.SIZE_DOWNLOAD)
      print "Effective URL:", c.getinfo(c.EFFECTIVE_URL)
      print "Content-type:", c.getinfo(c.CONTENT_TYPE)
      print "Namelookup-time:", c.getinfo(c.NAMELOOKUP_TIME)
      print "Redirect-time:", c.getinfo(c.REDIRECT_TIME)
      print "Redirect-count:", c.getinfo(c.REDIRECT_COUNT)
      # epoch = c.getinfo(c.INFO_FILETIME)
      # print "Filetime: %d (%s)" % (epoch, time.ctime(epoch))
      '''

      html = b.getvalue()
      # print(html)
      b.close()
      c.close()

      # 解析json数据 http://www.runoob.com/python/python-json.html
      import json

      arr = json.loads(html);
      errcode = arr['errcode'];
      theStr = 'fail'
      if errcode == 0:
        theStr = 'succ';

      theStr = 'ddid=%s is update %s' % (ddid, theStr);

      try:
        fname = '../018.txt';
        fobj = open(fname, 'r+');
      except:
        print 'open error!';
      else:
        str = fobj.read();
        #print str;
        print theStr;

        if str != '':
          fobj = open(fname, 'a+');

        fobj.write(theStr + "\n");

        fobj.close();

        return item
