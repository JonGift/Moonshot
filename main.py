from bs4 import BeautifulSoup
import requests

home = requests.get('https://www.reddit.com/r/wallstreetbets/')


soup = BeautifulSoup(home.content, 'lxml')
print(soup.prettify())