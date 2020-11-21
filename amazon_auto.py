from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


item_url ="https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452"
#item_url = "https://www.amazon.co.uk/dp/B07WDF13WC"
options = Options()
#options.page_load_strategy = 'eager'
#options.add_argument('--no-sandbox')
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)


driver.get(item_url)


while not driver.find_elements_by_xpath('//*[@id="buy-now-button"]'):
    driver.refresh()

driver.find_element_by_xpath(
    '//*[@id="buy-now-button"]').click()

print("found the buy now button!")
