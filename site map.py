import requests
from bs4 import BeautifulSoup

def get_all_links(url):

    response = requests.get(url)
    

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        

        links = soup.find_all('a')
        

        urls = [link.get('href') for link in links if link.get('href')]
        
        return urls
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
        return []


url = 'https://myket.ir'
links = get_all_links(url)
for link in links:
    print(link)

