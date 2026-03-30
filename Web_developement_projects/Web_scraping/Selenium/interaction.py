from time import time,sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")


timer = time() +300
timeout = time() + 10
driver.implicitly_wait(15)
driver.find_element(By.CSS_SELECTOR,"div#langSelect-EN").click()
sleep(5)

while True:
    if time() > timeout:
        driver.find_element(By.CSS_SELECTOR,"button#bigCookie").click()

    # 2. Every 5 seconds, find the most expensive available upgrade
    # Select all product prices that are NOT "grayed out" (enabled)
    all_prices = driver.find_elements(By.CSS_SELECTOR, "div.enabled div span.price")
    item_prices = []
    for price in all_prices:
        element_text = price.text.replace(",", "")
        if element_text != "":
            item_prices.append(int(element_text))


    # 3. Buy the highest value one
    if item_prices:
        highest_price = max(item_prices)
        # Find the index of the highest price to click the correct product
        highest_price_index = item_prices.index(highest_price)

        # Select all enabled product containers
        driver.find_element(By.ID, f"product{highest_price_index}").click()
        print(f"Bought upgrade worth: {highest_price}")
print("time's up")
# driver.find_element(By.CSS_SELECTOR,'input[name="fName"]').send_keys("sumitha")
# driver.find_element(By.CSS_SELECTOR,'input[name="lName"]').send_keys("Manoharan")
# driver.find_element(By.CSS_SELECTOR,'input[name="email"]').send_keys("sumithamanoharan76@gmail.com")
# driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
#
# driver.quit()