# Import necessary modules and packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
from openai_client import create_openai_client
from job_logic import JobProcessor

# Configure your OpenAI API key from environment variables
OPENAI_API_KEY = config('OPENAI_API_KEY')

# Load other configuration settings, such as the user profile directory
USER_PROFILE_DIR = config('USER_PROFILE_DIR')

# Create a ChromeOptions object and set the user data directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={USER_PROFILE_DIR}')

# Create a new Chrome driver instance with specified options
driver = webdriver.Chrome(options=chrome_options)

# Set an implicit wait time for the driver to wait for elements to appear
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

# Navigate to the website
driver.get("https://www.wyzant.com/tutor/jobs")

# Get the current URL for reference
current_url = driver.current_url

# Define the base URL string for navigating to the next page
next_page_string = "https://www.wyzant.com/tutor/jobs?action=index&controller=tutor_facing%2Fjobs&page="

# Find the element that contains the last page number and extract it
last_page_element = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/form/div[2]/div[4]/div[2]/div/a[4]')
num_pages = int(last_page_element.text)

# Create an instance of the OpenAI client
openai_client = create_openai_client()

# Define the mode of operation ('single-page' or 'multi-page')
mode = "multi-page"  # Change this to 'multi-page' if needed

# Create an instance of the JobProcessor
job_processor = JobProcessor(driver, openai_client, mode)

# Start processing job listings
while True:
    # Process a job listing from the current page and check if more jobs are available
    if not job_processor.process_job(current_url, next_page_string, num_pages):
        break

# Close the browser
driver.quit()
