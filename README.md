# About
Simple script that scrape for http proxies from [Free Proxy List Website](https://free-proxy-list.net/),
and stored it inside a text file.
This script make use of [requests](https://pypi.org/project/requests/) and [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/).

# Running this script
1. git clone the script
2. cd into the folder
```
jun@b:~$ cd proxy_list_scrapper
```
3. create new virtual environment
```
jun@b:~$ python3 -m venv .venv
```
4. get into the environment
```
jun@b:~$ source .venv/bin/activate
```
5. install dependencies
```
(.venv) jun@b:~$ pip install -r requirements.txt
```
6. run the script.
```
(.venv) jun@b:~$ python app.py
```
7. get our of virtual environment
```
(.venv) jun@b:~$ deactivate
```