import requests
from bs4 import BeautifulSoup

URL = "https://www.flashscore.ru/hockey/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(page.content)



