from bs4 import BeautifulSoup as bs
import requests as rt

params = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
response = rt.get("https://www.billboard.com/charts/hot-100/",headers=params)
soup = bs(response.text, "html.parser")
print(soup)
