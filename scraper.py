from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ChromeDriver setup
chrome_driver_path = "./chromedriver"
service = Service(executable_path=chrome_driver_path)

# Chrome options to avoid detection
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=options)

def get_itu_data():
    url = "https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx"
    driver.get(url)
    time.sleep(3)

    # Assuming there is a table with data on the page
    table = driver.find_element(By.CSS_SELECTOR, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        data.append([cell.text for cell in cells])

    for row_data in data:
        print(row_data)

get_itu_data()
driver.quit()
