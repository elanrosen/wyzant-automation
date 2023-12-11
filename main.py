from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from decouple import config
from openai import OpenAI
import os
import math
from selenium.common.exceptions import NoSuchElementException

def approximate_function(x):
    if x <= 25:
        # Linear ceil from 10 to 25
        return 25
    elif 25 < x <= 40:
        # Slow increase / plateau from 25 to 40
        return math.ceil(25 + 0.7 * (x - 25))
    else:
        # Faster increase from 40 to 70
        temp = math.ceil(27 + 0.9 * (x - 40))
        return min(temp, 40)

def print_separator(char, length):
    print(char * length)

def print_job_info(title, info):
    print(f"{title}: {info}")
# Configure your OpenAI API key
OPENAI_API_KEY = config('OPENAI_API_KEY')
client = OpenAI(api_key=config("OPENAI_API_KEY"))

# Your other configuration settings
USER_PROFILE_DIR = config('USER_PROFILE_DIR')

##stats
jobs_submitted = 0
jobs_skipped = 0


# Create a ChromeOptions object and set the user data directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={USER_PROFILE_DIR}')
# Create a new Chrome driver instance
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

# Navigate to the website
driver.get("https://www.wyzant.com/tutor/jobs")
current_url = driver.current_url
click_index = 0 ## on jobs page, account for jobs not submitted for
page_index = 1
next_page_string = "https://www.wyzant.com/tutor/jobs?action=index&controller=tutor_facing%2Fjobs&page="

last_page_element = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/form/div[2]/div[4]/div[2]/div/a[4]')
num_pages = int(last_page_element.text)

while True:
    try:
        rate_found = True
        job_links = driver.find_elements(By.CLASS_NAME, "job-details-link")
        # print("found " + str(len(job_links)) + " jobs")

        if len(job_links) == 0:
            # No more job links found, break out of the loop
            break

        job_links[click_index].click()

        poster_name_element = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/div[1]/h4')
        job_description_element = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/div[2]/div/div[6]/p')
        job_subject_element = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/div[1]/h1')
        
        try:
            recommended_rate_element = driver.find_element(By.XPATH, '//*[@id="job_application_form"]/div[4]/div[2]/p')
            recommended_rate_text = recommended_rate_element.text.strip()

            # Check if the text matches the expected format
            if recommended_rate_text.startswith("$ "):
                recommended_rate_text = recommended_rate_text[2:]  # Remove the "$ " prefix
                recommended_rate = int(recommended_rate_text)
            else:
                raise ValueError("Recommended rate text is not provided")
        except NoSuchElementException:
            rate_found = False
            recommended_rate = 40
        except ValueError as e:
            rate_found = False
            recommended_rate = 40

        job_details_element = driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/div[1]/div/div/div/div[5]')

        # Find all the <p> elements within the div
        p_elements = job_details_element.find_elements(By.TAG_NAME, 'p')

        student_grade_level = ""

        # Iterate through the <p> elements
        for i, p_element in enumerate(p_elements):
            if p_element.text == "Student grade level: ":
                # Check if there's a next <p> element and store its text
                if i + 1 < len(p_elements):
                    student_grade_level = p_elements[i + 1].text
                break  # Exit the loop since we found what we needed
        poster_name = poster_name_element.text
        job_description = job_description_element.text
        job_subject = job_subject_element.text
        
        print_separator("=", 40)
        print("\nFound Job:")
        print_separator("-", 40)
        print(f"Poster Name: {poster_name}")
        if rate_found:
            print(f"Recommended Rate: {recommended_rate}")
        else:
            print("Recommended Rate: n/a")
        print(f"Student Grade Level: {student_grade_level}")
        print(f"Job Subject: {job_subject}")
        print(f"Job Description: {job_description}")
        print_separator("-", 40)

        inputted_rate = int(approximate_function(recommended_rate))

        # if 'SAT' in job_subject or 'SAT' in job_description:
        #     inputted_rate = recommended_rate - 10

        planning_to_submit = True
        if student_grade_level == "High School":
            continue
        elif recommended_rate > 55:
            if student_grade_level == "Adult" or student_grade_level == "Graduate":
                planning_to_submit = False
            else:
                keywords_to_check = ["SAT", "React", "MySQL", "Flask", "Data Structures", "Algorithms", "C++", "Son", "Selenium", "Intro", "College", "Openai","Open-ai", "student"]
                if all(keyword.lower() not in job_description.lower() for keyword in keywords_to_check):
                    planning_to_submit = False
        elif recommended_rate > 35 and rate_found == True:
            if "Excel" in job_subject or "Excel" in job_description:
                planning_to_submit = False
        elif "Excel" == job_subject and "vba" in job_description.lower() or "unity" in job_description.lower():
            planning_to_submit = False

        if ("excel" in job_subject.lower() or "excel" in job_description.lower()) and not rate_found:
            inputted_rate = 29
        
        if planning_to_submit:
            print("Proceeding with Job")
            print_separator("-", 40)
            prompt = f"Job Posting: \n Name: {poster_name}\n Subject: {job_subject}\n Description: {job_description}"
            system_message = """
            You are to help me draft intro messages to potential tutoring clients. I will provide you with a job posting description and client name, and you should generate a message greeting them, and mention the fact I have plenty of experience.

            Here's a template to use:

            1) 'Hi ___! I saw that you're looking for help with ___. I have plenty of experience with ____, and would love to help. Hope to hear from you!'

            (keep it short and sweet). If they use an acronym keep it in acronym form (don't restate the full word). 
            Also, if they are a college student looking for help on a project, mention you are confident 
            you'll be able to help them finish their project as soon as possible (mention you have experience 
            with CS projects as a recent student). Don't mention projects otherwise.

            Sometimes the job posting will be for a parent looking for help for their child. In this case, recognize that in your response.
            Sometimes the job posting will mention an introductory meeting. In this case, mention you're available for an introductory meeting.
            Sometimes the job posting will have additional information in the description. In this case, make sure to mention you're familiarity with any additional technologies mentioned.

            """

            # Generate a personal message using the OpenAI API
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt},
                ]
            )
            generated_message = response.choices[0].message.content.strip("'")
            print("Generated Message:\n")
            print(generated_message)
            print(f"\nChosen Rate: {inputted_rate}")
            # Input the generated personal message into the form field
            personal_message_element = driver.find_element(By.ID, "personal_message")
            personal_message_element.clear()
            personal_message_element.send_keys(generated_message)

            hourly_rate_input = driver.find_element(By.ID, "hourly_rate")
            hourly_rate_input.clear()
            hourly_rate_input.send_keys(inputted_rate)

            submit_application_button = driver.find_element(By.XPATH, '//*[@id="job_application_form"]/input[5]')
            submit_application_button.click()
            click_index += 1
            print_separator("-", 40)
            print("Submitted!")
            jobs_submitted += 1

        else:
            print("SKIPPING JOB")
            click_index += 1
            print("Click Index: " + str(click_index))
            driver.get(current_url)
            jobs_skipped += 1

    except Exception as e:
        page_index += 1
        if page_index > num_pages:
            break
        print("Exception: " + str(e))
        print("Going to page: " + str(page_index))
        driver.get(next_page_string + str(page_index))
        current_url = driver.current_url
        click_index = 0

# Close the browser
driver.quit()

print_separator("=", 40)
print("Jobs Submitted: " + str(jobs_submitted))
print("Jobs Skipped: " + str(jobs_skipped))