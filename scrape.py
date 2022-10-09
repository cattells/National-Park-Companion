import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

data = {}
baseurl = "https://www.recreation.gov/camping/"
location = input("Enter national park: ")
start_date = input("Enter start date (MM/DD/YYYY)")
end_date = input("Enter end date (MM/DD/YYYY)")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.recreation.gov/")

search_bar = driver.find_element(by=By.ID, value="hero-search-input")
search_button = driver.find_element(by=By.ID, value="gtm-explore-all-hero-search")
search_bar.send_keys(location)
search_button.click()

time.sleep(2)

selections = driver.find_elements(by=By.CSS_SELECTOR, value="#search-results-list .search-outer-wrap .flex-col-12")
selections[0].click()

time.sleep(10)

campsites = driver.find_elements(by=By.CSS_SELECTOR, value="[data-component='CarouselItem']")
print(len(campsites))
for i in range(0, len(campsites)):

    campsites[i].click()

    '''campsite_start_date_bar = driver.find_element(by=By.ID, value="campground-start-date-calendar")
    campsite_end_date_bar = driver.find_eleemnt(by=By.ID, value="campground-end-date-calendar")
    campsite_start_date_bar.send_keys(start_date)
    campsite_end_date_bar.send_keys(end_date)'''

time.sleep(10)

print(data)
