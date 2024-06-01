import requests
from bs4 import BeautifulSoup
import dns.resolver
import socket
import re
import whois
import argparse
import csv

def step8():
   
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('--text', type=str, help='process some text')

    args = parser.parse_args()

    if args.text is not None:
        print(f"Processing text: {args.text}")
    return args.text    

vorodi = step8()
print('site map:')
def site_map(url):
    # darkhast be site
    response = requests.get(url)
    
    # if darkhast true!
    if response.status_code == 200:
        # gereftan mohtavaye site ba bs4
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # find all a tags
        links = soup.find_all('a')
        
        # estekhraj url az har a
        urls = [link.get('href') for link in links if link.get('href')]
        
        return urls
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
        return []

url = 'https://'+vorodi
links = site_map(url)
for link in links:
    print(link)


def sub_domain():
    domain = vorodi


    ns = dns.resolver.query(domain, 'NS')


    subdomains = ["api", "www", "mail", "ftp", "blog", "test", "dev", "staging", "docs", "shop",
                "support", "help", "forum", "status", "beta", "demo", "app", "secure", "static", "cdn"]


    for server in ns:
        server = str(server)
        for subdomain in subdomains:
            try:
                answers = dns.resolver.query(subdomain + "." + domain, "A")
                for ip in answers:
                    print(subdomain + "." + domain + " - " + str(ip))
            except:
                pass

sub_domain()

print("title:")
def title(vorodi):
    url = "https://" + vorodi

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    title_tag = soup.title

    if title_tag:
        title = title_tag.string
    else:
        title = "no title"

    print(title)

title(vorodi)

print("status:")
def status():
    url = "https://"+vorodi
#darkhast  zadan be site
    response = requests.get(url)

    # Check the HTTP status code of the response
    if response.status_code == 200:
        print("Success!")
        print("the request was successful and the response contains the requested data.")
    elif response.status_code == 301:
        print("301:Moved Permanently")
        print("the request was successful and the response contains the requested data.")
    elif response.status_code == 302:
        print("302:found")
        print("the requested page has been temporarily moved to a new location.")
    elif response.status_code == 400:
        print("400:bad requests")
        print("the server could not understand the request.")
    elif response.status_code == 401:
        print("401:Unauthorized")
        print("the user is not authorized to access the requested resource.")
    elif response.status_code == 403:
        print("403:Forbidden")
        print("the user is authenticated but doesn't have permission to access the requested resource.")
    elif response.status_code == 404:
        print("404:Not found")
        print("the user is authenticated but doesn't have permission to access the requested resource.")
    elif response.status_code == 500:
        print("500:Internal Server Error")
        print("the server encountered an error while processing the request.")

status()

print("ip:")
def ip():
    domain = vorodi

    ip_address = socket.gethostbyname(domain)

    print(f"The IP address of {domain} is {ip_address}")

ip()

print("port:")
def port():
    domain = vorodi
    ip = ip_address = socket.gethostbyname(domain)

    # List of commonly used ports to scan
    common_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]

    for port in common_ports:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))
        sock.close()

port()


def regex(url):
    
    def extract_contacts_from_website(url):
        try:
            # peyda kardan mohtava
            response = requests.get(url)
            response.raise_for_status()  #barresi vojod error
        except requests.RequestException as e:
            print(f"Failed to retrieve the website content: {e}")
            return [], []

        emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', response.text)
       
       
        phone_numbers = re.findall(r"\d{3}-\d{8}", response.text)
        
        return emails, phone_numbers

    # dar avardan email va shomare
    emails, phone_numbers = extract_contacts_from_website(url)

   
    print("emails:")
    for email in emails:
        print(email)

    print("\nphone numbers:")
    for number in phone_numbers:
        print("phone number:", number)


website_url = "https://"+ vorodi
regex(website_url)


def hoois():
    domain = vorodi

    w = whois.whois(domain)

    print(w)

    # Safely print each field if it exists
    print("Domain registrar:", w.registrar if hasattr(w, 'registrar') else "N/A")
    print("WHOIS server:", w.whois_server if hasattr(w, 'whois_server') else "N/A")
    print("Domain creation date:", w.creation_date if hasattr(w, 'creation_date') else "N/A")
    print("Domain expiration date:", w.expiration_date if hasattr(w, 'expiration_date') else "N/A")
    print("Domain last updated:", w.last_updated if hasattr(w, 'last_updated') else "N/A")
    print("Name servers:", w.name_servers if hasattr(w, 'name_servers') else "N/A")
    print("Registrant name:", w.name if hasattr(w, 'name') else "N/A")
    print("Registrant organization:", w.org if hasattr(w, 'org') else "N/A")
    print("Registrant email:", w.email if hasattr(w, 'email') else "N/A")
    print("Registrant phone:", w.phone if hasattr(w, 'phone') else "N/A")

hoois()

def report (site_map):
    
    filename = "data.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(site_map)
report(links )      