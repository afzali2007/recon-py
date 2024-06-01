import requests

# Replace "https://www.example.com" with the URL of the webpage you want to check the status of
url = "https://visa.com"

# Send a GET request to the URL and store the response in a variable
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

