from bs4 import BeautifulSoup as BS
from lxml.html.formfill import fill_form
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import requests as rt
import pandas as pd

form_url = "https://forms.gle/DbVivvdT5yvEPziN9"
listing_url = "https://www.zillow.com/san-francisco-ca/rentals/2_p/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-123.8466398985262%2C%22east%22%3A-121.6878264219637%2C%22south%22%3A37.223081771144585%2C%22north%22%3A38.463667991536795%7D%2C%22mapZoom%22%3A9%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D"

class House_listings:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def fill_form(self,link,address,price):
        self.driver.get(form_url)
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i1 i4"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i6 i9"]').send_keys(price)
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i11 i14"]').send_keys(link,Keys.ENTER)



    def get_data(self,houses):
        for i in houses:
            link = i.select_one("a")["href"]
            address = i.select_one("a").text
            price = i.select_one("span.srp-bueOgM").replace("/mo","")
            fill_form(link,address,price)

    def main(self):
        with open("data.html","r",encoding="utf-8") as f:
            data=f.read()
            result = BS(data,"html.parser")
            listings = result.select('div[data-testid="property-card-data"]')
            self.get_data(listings)


if __name__ == "__main__":
    obj = House_listings()
    obj.main()

