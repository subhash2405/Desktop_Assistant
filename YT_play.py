from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os

class entertainment():
    def __init__(self):
        chrome_driver_path = os.getenv('chrome_path')
        chrome_service = ChromeService(executable_path=chrome_driver_path, args=["--no-close"])
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string/span')
        video.click()

# assist = entertainment()
# assist.play("funmoji")
