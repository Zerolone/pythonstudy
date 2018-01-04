#!/usr/bin/python
# coding=utf-8

# 连接mysql

import MySQLdb

config = {
  'host': '127.0.0.1',
  'port': 3306,
  'user': 'root',
  'passwd': 'root',
  'db': 'test',
  'charset': 'utf8'
}
conn = MySQLdb.connect(**config);

cursor = conn.cursor();

DB_NAME = 'test_py';
TABLE_NAME = 'user';

try:
  # 创建数据库
  '''
    sql = 'DROP DATABASE IF EXISTS ' + DB_NAME;
    print  '24---' + sql;
    cursor.execute(sql);

    sql = 'CREATE DATABASE ' + DB_NAME;
    print  '28---' + sql;

    cursor.execute(sql);
    '''

  # 创建表
  conn.select_db(DB_NAME);
  '''
    sql = 'CREATE TABLE ' + TABLE_NAME + ' (id int primary key,name varchar(30))';
    sql = 'CREATE TABLE %s (id int primary key,name varchar(30))' % (TABLE_NAME) ;
    cursor.execute(sql);
    '''

  # 插入单条数据
  '''
    sql = 'INSERT INTO user values("%d","%s")' % (1, "jack");
    cursor.execute(sql);
    '''

  # 不建议直接拼接sql，占位符方面可能会出问题，execute提供了直接传值
  '''
    value = [2,'John']
    cursor.execute('INSERT INTO user values(%s,%s)', value);
    '''

  # 批量插入数据
  '''
    values = []
    for i in range(3, 20):
        values.append((i,'kk'+str(i)))
    cursor.executemany('INSERT INTO user values(%s,%s)',values)
    '''

  '''
    # 查询数据条目
    count = cursor.execute('SELECT * FROM %s' %TABLE_NAME)
    print 'total records: %d' %count
    print 'total records:', cursor.rowcount

    # 获取表名信息
    desc = cursor.description
    print "%s %3s" % (desc[0][0], desc[1][0])

    # 查询一条记录
    print 'fetch one record:'
    result = cursor.fetchone()
    print result
    print 'id: %s,name: %s' %(result[0],result[1])

    # 查询多条记录
    print 'fetch five record:'
    results = cursor.fetchmany(5)
    for r in results:
        print r

    # 查询所有记录
    # 重置游标位置，偏移量:大于0向后移动;小于0向前移动，mode默认是relative
    # relative:表示从当前所在的行开始移动; absolute:表示从第一行开始移动
    cursor.scroll(0, mode='absolute')
    results = cursor.fetchall()
    for r in results:
      print r

    cursor.scroll(-2)
    results = cursor.fetchall()
    for r in results:
      print r
      
    '''

  # 更新记录
  # cursor.execute('UPDATE %s SET name = "%s" WHERE id = %s' % (TABLE_NAME, 'Jack-jak', 1))

  # 删除记录
  # cursor.execute('DELETE FROM %s WHERE id = %s' %(TABLE_NAME,2))

  # 休眠执行
  '''
    import time

    i = 1;
    while i <= 3 :
      print 'sleep %i second' %i;
      i+=1;
      time.sleep(1);
    '''

  # 时间戳
  '''
  import time

  # 获取当前时间
  time_now = time.time();
  print time_now;

  int_time = int(time_now);
  print int_time;

  # 转换成localtime
  time_local = time.localtime(time_now)
  print time_local

  # 转换成新的时间格式(2016-05-09 18:59:20)
  dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

  print dt
  '''

  #curl 访问接口
  import pycurl, StringIO

  #print '142-------------';
  #print pycurl.version_info();
  #print '142-------------';
  url = 'http://api.mingyihui.net:8082/common/info';
  url = 'http://api.mingyihui.net:8082/services/hospital/info';


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

  #post_data_dic = [{"name": "value"}]


  postData = '[{"hid":"2","hid"=2}]'

  postData = 'hid=2';

  c.setopt(c.POSTFIELDS, postData);

  # 设置代理
  # c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)
  # c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)
  # 不明确作用
  # c.setopt(pycurl.HTTPPROXYTUNNEL,1) #隧道代理
  # c.setopt(pycurl.NOSIGNAL, 1)
  # 设置post请求， 上传文件的字段名 上传的文件
  # post_file = "/home/ubuntu/avatar.jpg"
  #c.setopt(c.HTTPPOST, [("textname", (c.FORM_FILE, post_file))])
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
  #print(html)
  b.close()
  c.close()

  #解析json数据 http://www.runoob.com/python/python-json.html
  '''
  import json

  arr = json.loads(html);
  print arr['data']['phone'];
  '''

  '''读写文本数据'''
  #http://www.runoob.com/python/python-files-io.html
  try:
    fname = '018.txt';
    fobj  = open(fname, 'r+');
  except:
    print 'open error!';
  else:
    str = fobj.read();
    print str;

    if str != '':
      fobj = open(fname, 'a+');

    fobj.write("zerolone\n");

    fobj.close();




except:
  print 'some thing error!';

  import traceback;

  traceback.print_exc();

finally:
  cursor.close();

  conn.close();
