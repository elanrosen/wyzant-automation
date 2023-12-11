from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
from openai_client import create_openai_client
from job_logic import JobProcessor

# Configure your OpenAI API key
OPENAI_API_KEY = config('OPENAI_API_KEY')

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
current_url = driver.current_url
next_page_string = "https://www.wyzant.com/tutor/jobs?action=index&controller=tutor_facing%2Fjobs&page="

last_page_element = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/form/div[2]/div[4]/div[2]/div/a[4]')
num_pages = int(last_page_element.text)
openai_client = create_openai_client()
mode = "single-page" ## "single-page" or "multi-page"
# Create an instance of JobProcessor
job_processor = JobProcessor(driver, openai_client, mode)

while True:
    if not job_processor.process_job(current_url, next_page_string, num_pages):
        break

# Close the browser
driver.quit()
