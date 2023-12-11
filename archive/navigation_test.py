from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from decouple import config
from openai import OpenAI
import os
import math
from selenium.common.exceptions import NoSuchElementException



# Your other configuration settings
USER_PROFILE_DIR = config('USER_PROFILE_DIR')

# Create a ChromeOptions object and set the user data directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={USER_PROFILE_DIR}')
# Create a new Chrome driver instance
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

# Navigate to the website
driver.get("https://www.wyzant.com/tutor/jobs")

next_page_button = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/form/div[2]/div[4]/div[2]/div/a[5]')
next_page_button.click()
time.sleep(2)
next_page_button.click()
next_page_button = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/form/div[2]/div[4]/div[2]/div/a[5]')
next_page_button.click()