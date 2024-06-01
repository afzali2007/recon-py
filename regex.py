import re
import requests

def extract_contacts_from_website(url):
    # دریافت محتوای صفحه وب
    response = requests.get(url)
    if response.status_code == 200:
        # استخراج ایمیل‌ها با استفاده از regex
        emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', response.text)
        # الگوی regex برای شماره‌های تلفن با فرمت 021- و 8 رقم عددی
        phone_numbers = re.findall(r"[021-]\d{8}", response.text)
        return emails, phone_numbers
    else:
        print("Failed to retrieve the website content.")
        return [], []

# آدرس وب‌سایت مورد نظر
website_url = "https://cafebazaar.ir/contact"
# استخراج ایمیل‌ها و شماره‌های تلفن
emails, phone_numbers = extract_contacts_from_website(website_url)

# چاپ ایمیل‌ها
print("ایمیل‌ها:")
for email in emails:
    print(email)

# چاپ شماره‌های تلفن
print("\nشماره‌های تلفن:")
for number in phone_numbers:
    print("شماره تلفن:", number)