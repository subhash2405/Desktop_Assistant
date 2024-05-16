from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os

class Info():
    def __init__(self):
        chrome_driver_path = os.getenv('chrome_path')
        chrome_service = ChromeService(executable_path=chrome_driver_path, args=["--no-close"])
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search_input = self.driver.find_element(By.XPATH,"//input[@id='searchInput']")
        search_input.send_keys(query)
        search_input.submit()



# input("Press Enter to close the Chrome tab...")
# info.driver.quit()  # Close the Chrome tab when Enter is pressed
