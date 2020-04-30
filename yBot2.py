import requests
from bs4 import BeautifulSoup
from random import choice

def proxy_generator():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, 
	   soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
    return proxy

def data_scraper(request_method, url, **kwargs):
    timeout = int(input('enter timeout : '))
    while True:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))

            response = requests.request(request_method, url, proxies=proxy, timeout=timeout, **kwargs)
            break
            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass
    return response

def main():
    url = input('enter your url : ')
    response = data_scraper('get', url)

if __name__ =="__main__":

    main()