import re
from urllib import parse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont, 'html.parser')
        if soup is None:
            return None, None
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data


    def _get_new_urls(self,page_url,soup):
        if soup is None:
            return None
        new_urls=set()
        #links=soup.find_all('a',href=re.compile(r'/item/*'))
        links = []
        for item in soup.find_all('a'):
            if '/item/' in str(item.get("href")):
                links.append(str(item.get("href")))
        for link in links:
            #new_url=link['href']
            new_full_url=parse.urljoin(page_url,link)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        if soup is None:
            return None
        data={}
        data['url']=page_url
        if soup.find('dd',class_='lemmaWgt-lemmaTitle-title') is None:
            return None
        if soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1') is None:
            return None
        if soup.find('h1') is None:
            return None
        title=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        #if '百度' in str(title.get_text()) or '秒懂' in str(title.get_text()):
        #    return None
        data['title']=title.get_text()
        #if soup.find('div',class_='lemma-summary') is None:
        #    return None
        #summary=soup.find('div',class_='lemma-summary')
        #data['summary']=summary.get_text()
        return data