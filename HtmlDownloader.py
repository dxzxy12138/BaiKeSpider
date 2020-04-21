import requests
import time
class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        user_agent='Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
        headers={'User-Agent':user_agent,'Connection':'close',}
        requests.packages.urllib3.disable_warnings()
        requests.adapters.DEFAULT_RETRIES = 5  
        try:
            r=requests.get(url,headers=headers,verify=False)
            if r.status_code==200:
                r.encoding='utf-8'
                return r.text
            return None
        except:
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            return None