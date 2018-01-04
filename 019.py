import scrapy


def parse_page1():
  print 1
  return scrapy.Request("http://192.168.99.101/scrapy/0_11.html",
                        callback=parse_page2)


def parse_page2(response):
  print 2
  # this would log http://www.example.com/some_page.html
  self.logger.info("Visited %s", response.url)



parse_page1();
