import requests
from itertools import cycle

list_proxy = ['82.114.82.90:56068',
              '103.216.82.207:6667',
              '83.142.197.99:52247',
               '137.74.157.159:1080',
              ]

proxy_cycle = cycle(list_proxy)
# Prime the pump
proxy = next(proxy_cycle)
num = input("How many times you want to try : ")
url = input("put in the URL of your site : ")
for i in range(1, 10):
    proxy = next(proxy_cycle)
    print(proxy)
    proxies = {
      "http": proxy,
      "https":proxy
    }
    try:


        r = requests.get(url=url, proxies=proxies)
        print("Success", url)
        print(r.json())
    except:  

        print("Skipping. Connnection error", url)
