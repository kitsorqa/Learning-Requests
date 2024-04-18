import requests
from bs4 import BeautifulSoup
import jwt

epl_games = 'https://soccer365.ru/competitions/12/'
html_games = requests.get(epl_games)

some_site = BeautifulSoup(html_games.text, "html.parser")
home_match = some_site.find_all(class_="ht")
guest_match = some_site.find_all(class_="at")

print(home_match[0].find(class_='name').text)
print(guest_match[0].find(class_='name').text)