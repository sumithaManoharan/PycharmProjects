from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

time = driver.find_elements(By.XPATH,"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li/time")
events = driver.find_elements(By.XPATH,"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li/a")
upcoming_events = {}
for i in range(0,len(time)):
    # print(i)
    upcoming_events[i] = {"time":time[i].text,"name": events[i].text}
print(upcoming_events)
driver.quit()
