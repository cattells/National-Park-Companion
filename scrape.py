import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

data = {}

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.nps.gov/index.htm")

driver.implicitly_wait(3)

state_dropdown = driver.find_element(by=By.CSS_SELECTOR, value="[data-toggle='dropdown']")
state_dropdown.click()

state_options = driver.find_elements(by=By.CSS_SELECTOR, value="[role='menuitem']")
for i in range(0, len(state_options) - 55):

    state_name = state_options[i].text
    data.update({state_name: {}})
    state_options[i].click()

    national_parks = driver.find_elements(by=By.CSS_SELECTOR, value="#list_parks > li")
    for j in range(0, len(national_parks)):

        national_park_link = national_parks[j].find_element(by=By.CSS_SELECTOR, value="h3 > a")
        national_park_name = national_park_link.text
        data[state_name].update({national_park_name: {}})

        partial_href = national_park_link.get_attribute("href")[-6:]

        national_park_link.click()

        try:
            driver.find_element(by=By.CSS_SELECTOR, value="[href='" + partial_href + "planyourvisit/eatingsleeping.htm']")
            print("Found")
        except:
            print("Not found")

        driver.back()
        national_parks = driver.find_elements(by=By.CSS_SELECTOR, value="#list_parks > li")

print(data)
