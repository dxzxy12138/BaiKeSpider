import codecs
import json

class DataOutput(object):
    def __init__(self):
        self.datas=[]
        
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        json_str = json.dumps(self.datas, ensure_ascii=False, indent=4)
        with open('test_data.json', 'w', encoding = 'utf-8') as json_file:
            json_file.write(json_str)