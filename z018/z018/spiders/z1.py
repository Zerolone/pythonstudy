# -*- coding: utf-8 -*-
import scrapy
import json
import re
import sys;


# 获取数据
def getData(paramsArr=''):
    try:
        ddid  = paramsArr['ddid'];
        limit = paramsArr['limit'];

        sql = '''
        select 
            hdd.ddid, hdd.`name`, hdd.url 
        FROM monolithpro_hospital_department_doctor             hdd
        LEFT JOIN monolithpro_kuaiyi_hospital_department_doctor khdd on hdd.ddid = khdd.ddid and hdd.`name` = khdd.ddname
        where 1
        and url like 'http://www.haodf.com/doctor/%'
        and ddid > %d
        order by hdd.ddid
        limit %d;
        ''' % (ddid, limit) ;


        print paramsArr['DB_NAME'];
        return 1;



    except:
        print 'get datas error, please Check database is exist!';
        print '';

        # import traceback;
        # traceback.print_exc();
        sys.exit(0);
    pass

class Z1Spider(scrapy.Spider):
    name = 'z1'
    allowed_domains = ['jx.com']
    start_urls = []

    import MySQLdb

    #初始化变量
    fobj = open('config.json', 'w+');
    config = fobj.read();

    try:
        config = json.loads(config)
    except:
        pass;

    #print type(config);
    #DB_NAME = config['DB_NAME']

    ddid  = 0;
    limit = 10;
    try:
        ddid  = config['ddid'];
        limit = config['limit'];
    except:
        pass;

    config = {};
    config['ddid']  = ddid;
    config['limit'] = limit;

    try:
        encode_json = json.dumps(config)
        fobj.write(encode_json);
        fobj.close();
    except:
        print 'config write error. please check permission';

    #连接数据库
    try:
        config_db = open('config_db.json');
        config_db = config_db.read();
        config_db = json.loads(config_db)
        conn = MySQLdb.connect(**config_db); #将dict扩展为关键字参数
        cursor = conn.cursor();
    except:
        print 'db connect error, please Check db_config.json';

        #import traceback;
        #traceback.print_exc();
        sys.exit(0);




    #开始
    print 'begin snatch with ddid = %d' % (ddid)

    #获取数据
    #a = getData(config);
    #print a;

    urlFix = 'http://www.j.com/scrapy/';
    urlFix = 'http://192.168.99.101/scrapy/';

    for i in range(0,10):
        start_urls.append(urlFix + str(i) + '.html');

    #sys.exit(0);

    print '----------------------------';
    print(start_urls);
    print '----------------------------';

    def parse(self, response):
        filename = response.url;
        print filename;
        print '-----' * 10;

        items=[];
        myItems = re.findall('{title([\s\S]+?)}[\s\S]+?{body([\s\S]+?)}', response.body, re.I | re.M);
        for i in myItems:
          items.append({
            'title'   : i[0].strip(),
            'content' : i[1],
          });

        print items;
        #exit();

        return items;

