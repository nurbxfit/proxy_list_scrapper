import requests
from bs4 import BeautifulSoup

# TODO read proxy_list.txt and populate into tuple
# then test the address by sending request with proxies = {'http':'addres:port'}
# res = request.get('https://httpbin.org/ip',proxies=proxies)
# check if res['origin'] == proxy[0][0]
# below funct is to check if in valid add format
# def valid_address(addr):
#     return isinstance(addr,(list,tuple)) and len(addr) == 2 and isinstance(addr[0],str) and isinstance(addr[1],int)

def write_list_to_file(list):
    with open("proxy_list.txt","w") as file:
        for item in list:
            file.write(f"{item}\n")
        print("Done")

def get_html(proxy_site):
    res = requests.get(proxy_site)
    page_html = res.text
    return page_html

def scrape_list(page_html):
    soup = BeautifulSoup(page_html,'html.parser')
    list_div = soup.find(class_="table-responsive fpl-list")
    list_tr = list_div.select("tr")
    proxy_list = []

    for tr in list_tr:
        td = tr.select("td")
        if not td:
            pass
        else:
            ip = td[0].get_text()
            port = td[1].get_text()
            protocol = "http" if td[6].get_text() == "no" else "https"
            proxy_list.append(f"{ip}:{port},{protocol}")
    
    return proxy_list


def main():
    proxy_site = "https://free-proxy-list.net/"
    page = get_html(proxy_site)
    if page:
        proxy_list = scrape_list(page)
        if proxy_list:
            write_list_to_file(proxy_list)

if __name__ == "__main__":
    main()