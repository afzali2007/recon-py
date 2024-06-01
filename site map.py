import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    # درخواست به سایت
    response = requests.get(url)
    
    # اگر درخواست موفقیت آمیز بود
    if response.status_code == 200:
        # پارس کردن محتوای HTML با استفاده از BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # پیدا کردن تمامی تگ‌های <a>
        links = soup.find_all('a')
        
        # استخراج URL از هر تگ <a>
        urls = [link.get('href') for link in links if link.get('href')]
        
        return urls
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
        return []

# مثال از استفاده
url = 'https://myket.ir'
links = get_all_links(url)
for link in links:
    print(link)

