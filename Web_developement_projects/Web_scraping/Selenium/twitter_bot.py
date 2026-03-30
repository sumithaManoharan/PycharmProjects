from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
import random

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "Web_developement_projects/Web_scraping/Selenium/chrome_profile"
twitter_email = "sumithamanoharan76@gmail.com"
twitter_password = "$Umitha762"

class TwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument(f"user-data-dir={CHROME_DRIVER_PATH}")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.options = uc.ChromeOptions()
        self.uc_driver = uc.Chrome(options=self.options)
    #
    # def human_type(element, text):
    #     """Types like a human with random delays."""
    #     for char in text:
    #         element.send_keys(char)
    #         sleep(random.uniform(0.1, 0.3))

    def twitter_post(self):
        self.driver.get("https://x.com/home")
        sleep(5)



    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.js-start-test")))
        self.driver.find_element(By.CSS_SELECTOR,"a.js-start-test").click()
        WebDriverWait(self.driver,200).until(EC.url_contains("https://www.speedtest.net/result/"))
        download = self.driver.find_element(By.CSS_SELECTOR,"span.download-speed").text
        upload = self.driver.find_element(By.CSS_SELECTOR,"span.upload-speed").text
        if download != "" and upload != "":
            self.twitter_post()


    def main(self):
        self.get_internet_speed()

if __name__ == "__main__":
    twitter = TwitterBot()
    twitter.main()