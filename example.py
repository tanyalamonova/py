import requests
import re 
from bs4 import BeautifulSoup, SoupStrainer
            
sitePage = requests.get('http://www.csd.tsu.ru/')
reobj = re.compile(r"\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,6}\b", re.IGNORECASE)
emails = list(set(re.findall(reobj, sitePage.text)))   
print(emails)
soup = BeautifulSoup(sitePage.content, 'html.parser', parse_only=SoupStrainer('a'))
links = []
links.append([link['href'] for link in soup if link.has_attr('href') and len(links)<10])
print(links)
