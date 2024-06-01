import requests
from bs4 import BeautifulSoup


a=input("")
url = "https://"+a

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.title.string

print(title)