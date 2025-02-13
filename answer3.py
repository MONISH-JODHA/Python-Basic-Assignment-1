import time
import requests
def url_checker(urls):
    for url in urls:
        status=requests.get(url).status_code
        if 400<=status<500:
            print(f'URL:{url} Status-code:{status} client-side error')
        elif 500<=status<600:
            print(f'URL:{url} Status-code:{status} Server-side error')
        else:
            print(f'URL:{url} Status-code:{status} Success')

urlscontainer = [
        "http://www.example.com/nonexistentpage",
        "http://httpstat.us/404",
        "http://httpstat.us/500",
        "https://www.google.com/"
    ]

while True:   
    url_checker(urlscontainer)
    time.sleep(10)