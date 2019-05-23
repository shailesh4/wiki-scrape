import requests
from bs4 import BeautifulSoup
import re

web_link = "https://en.wikipedia.org/wiki/Black_hole"

open("raw_data","w+", encoding='utf-8').write(requests.get(web_link, verify=False).text);
for p in BeautifulSoup(open("raw_data", "r", encoding='utf-8').read(), 'html.parser').findAll("div", { "class": 'mw-parser-output' })[0].find_all('p'): web_link += p.get_text() 
open("raw_data","w+", encoding='utf-8').write(re.sub(r'\[+\d+\]', '', str(web_link)))
