import requests
from bs4 import BeautifulSoup

link = 'http://books.toscrape.com'

requisicao = requests.get(link)
print(requisicao)

site = BeautifulSoup(requisicao.text, 'html.parser')

print(site)



