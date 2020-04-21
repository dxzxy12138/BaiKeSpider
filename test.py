import re
from urllib import parse
from bs4 import BeautifulSoup

content = '<li class="item">▪<a title="法律出版社出版法律学专著" href=/item/%E6%89%BF%E5%8A%9E%E4%BA%BA>法律出版社出版法律学专著</a></li>'

regex = re.compile(r'/item/*')
x = regex.findall(content)
print(x)