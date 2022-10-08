from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.nps.gov/index.htm")

driver.implicitly_wait(3)

state_dropdown = driver.find_element(by=By.CSS_SELECTOR, value="[data-toggle='dropdown']")
state_dropdown.click()

state_options = driver.find_elements(by=By.CSS_SELECTOR, value="[role='menuitem']")

for state_option in state_options:

    print(state_option.text)

