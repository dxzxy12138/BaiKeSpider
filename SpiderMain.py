from DataOutput import DataOutput
from HtmlParser import HtmlParser
from HtmlDownloader import HtmlDownloader
from URLManager import URLManager
from bs4 import BeautifulSoup

class SpiderMain(object):
    def __init__(self):
        self.manager=URLManager()
        self.downloader=HtmlDownloader()
        self.parser=HtmlParser()
        self.output=DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        seen = set()
        new_url=self.manager.get_new_url()
        html=self.downloader.download(new_url)
        new_urls,data=self.parser.parser(new_url, html)
        self.output.store_data(data)
        self.output.output_html()
        self.manager.add_new_urls(new_urls)
        size = len(self.manager.new_urls)
        #size = 30
        #print(size)
        while len(seen) < size:
            n_url = self.manager.get_new_url()
            if n_url not in seen:
                seen.add(n_url)
            else:
                continue
            html = self.downloader.download(n_url)
            new_urls, data=self.parser.parser(n_url, html)
            self.output.store_data(data)
            self.output.output_html()
            #print()
            #self.manager.new_urls.remove(n_url)
        seenn = set()
        urls = set()
        for item in list(seen):
            count = 0
            print(item)
            html=self.downloader.download(item)
            urls,data=self.parser.parser(item, html)
            if urls is None or data is None:
                continue
            self.output.store_data(data)
            self.output.output_html()
            sizee = len(urls)
            print(sizee)
            while count < sizee:
                if len(urls) <= 0:
                    break
                else: 
                    n_url = urls.pop()
                count += 1
                if n_url not in seenn and n_url not in seen:
                    seenn.add(n_url)
                else:
                    continue
                html = self.downloader.download(n_url)
                new_urls,data=self.parser.parser(n_url, html)
                if urls is None or data is None:
                    break
                self.output.store_data(data)
                self.output.output_html()
            urls.clear()

if __name__ == '__main__':
    spider_man=SpiderMain()
    spider_man.crawl("https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%90%88%E5%90%8C%E6%B3%95/61754#viewPageContent")