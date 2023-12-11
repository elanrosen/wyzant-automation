from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from helpers import approximate_function, print_separator, print_job_info
from openai_client import generate_openai_message

class JobProcessor:
    def __init__(self, driver, openai_client, mode):
        """
        Initialize the JobProcessor instance.

        Args:
            driver: Selenium WebDriver for web automation.
            openai_client: Client for interacting with the OpenAI API.
            mode (str): The mode of operation (e.g., "single-page" or "multi-page").
        """
        self.driver = driver
        self.openai_client = openai_client
        self.click_index = 0
        self.page_index = 1
        self.jobs_processed = 0
        self.jobs_skipped = 0
        self.jobs_submitted = 0
        self.mode = mode

    def process_job(self, current_url, next_page_string, num_pages):
        """
        Process a job listing from a web page.

        Args:
            current_url (str): The URL of the current job listing page.
            next_page_string (str): The base URL string for navigating to the next page.
            num_pages (int): The total number of pages to process.

        Returns:
            bool: True if the job was processed, False if no jobs are found or an error occurred.
        """
        try:
            rate_found = True
            job_links = self.driver.find_elements(By.CLASS_NAME, "job-details-link")

            if len(job_links) == 0:
                print("No jobs found: exiting")
                return False

            job_links[self.click_index].click()

            # Extract job details
            poster_name_element = self.driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/div[1]/h4')
            job_description_element = self.driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/div[2]/div/div[6]/p')
            job_subject_element = self.driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/div[1]/h1')

            try:
                recommended_rate_element = self.driver.find_element(By.XPATH, '//*[@id="job_application_form"]/div[4]/div[2]/p')
                recommended_rate_text = recommended_rate_element.text.strip()
                if recommended_rate_text.startswith("$ "):
                    recommended_rate_text = recommended_rate_text[2:]
                    recommended_rate = int(recommended_rate_text)
                else:
                    raise ValueError("Recommended rate text is not provided")
            except NoSuchElementException:
                rate_found = False
                recommended_rate = 40
            except ValueError as e:
                rate_found = False
                recommended_rate = 40

            job_details_element = self.driver.find_element(By.XPATH, '//*[@id="wyzantResponsiveColumns"]/div[1]/div/div/div/div[5]')
            p_elements = job_details_element.find_elements(By.TAG_NAME, 'p')
            student_grade_level = ""

            for i, p_element in enumerate(p_elements):
                if p_element.text == "Student grade level: ":
                    if i + 1 < len(p_elements):
                        student_grade_level = p_elements[i + 1].text
                    break

            poster_name = poster_name_element.text
            job_description = job_description_element.text
            job_subject = job_subject_element.text

            print_separator("=", 40)
            print("\nFound Job:")
            print_separator("-", 40)
            print_job_info("Poster Name", poster_name)
            if rate_found:
                print_job_info("Recommended Rate", recommended_rate)
            else:
                print_job_info("Recommended Rate", "n/a")
            print_job_info("Student Grade Level", student_grade_level)
            print_job_info("Job Subject", job_subject)
            print_job_info("Job Description", job_description)
            print_separator("-", 40)

            inputted_rate = int(approximate_function(recommended_rate))

            planning_to_submit = True
            if student_grade_level == "High School":
                planning_to_submit = True
            elif recommended_rate > 55:
                if student_grade_level == "Adult" or student_grade_level == "Graduate":
                    planning_to_submit = False
                else:
                    keywords_to_check = ["SAT", "React", "MySQL", "Flask", "Data Structures", "Algorithms", "C++", "Son", "Selenium", "Intro", "College", "Openai", "Open-ai", "student"]
                    if all(keyword.lower() not in job_description.lower() for keyword in keywords_to_check):
                        planning_to_submit = False
            elif recommended_rate > 35 and rate_found == True:
                if "Excel" in job_subject or "Excel" in job_description:
                    planning_to_submit = False
            elif "Excel" == job_subject and "vba" in job_description.lower() or "unity" in job_description.lower():
                planning_to_submit = False

            if ("excel" in job_subject.lower() or "excel" in job_description.lower()) and not rate_found:
                inputted_rate = 29
            self.jobs_processed += 1
            if planning_to_submit:
                self.jobs_submitted += 1
                return self.submit_job(poster_name, job_subject, job_description, inputted_rate, current_url)
            else:
                self.jobs_skipped += 1
                return self.skip_job(current_url)

        except Exception as e:
            self.page_index += 1
            if self.page_index > num_pages:
                print("No more pages: exiting")
                return False
            print("Exception: " + str(e))
            if self.mode == "multi-page":
                print("Going to page: " + str(self.page_index))
                self.driver.get(next_page_string + str(self.page_index))
            elif self.mode == "single-page":
                print("Refreshing page")
                self.driver.get(current_url)
            current_url = self.driver.current_url
            self.click_index = 0
            return True

    def submit_job(self, poster_name, job_subject, job_description, inputted_rate, current_url):
        """
        Submit a job application with generated content.

        Args:
            poster_name (str): Name of the job poster.
            job_subject (str): Subject of the job listing.
            job_description (str): Description of the job listing.
            inputted_rate (int): The rate to input in the job application.
            current_url (str): The URL of the current job listing page.

        Returns:
            bool: True if the job was successfully submitted, False otherwise.
        """
        try:
            print("Proceeding with Job")
            print_separator("-", 40)

            generated_message = generate_openai_message(self.openai_client, poster_name, job_subject, job_description)
            print("Generated Message:\n")
            print(generated_message)
            print_job_info("Chosen Rate", inputted_rate)

            personal_message_element = self.driver.find_element(By.ID, "personal_message")
            personal_message_element.clear()
            personal_message_element.send_keys(generated_message)

            hourly_rate_input = self.driver.find_element(By.ID, "hourly_rate")
            hourly_rate_input.clear()
            hourly_rate_input.send_keys(inputted_rate)

            submit_application_button = self.driver.find_element(By.XPATH, '//*[@id="job_application_form"]/input[5]')
            submit_application_button.click()
            # self.driver.get(current_url)
            # self.click_index += 1
            print_separator("-", 40)
            print("Submitted!")
            return True

        except Exception as e:
            print("Exception while submitting job: " + str(e))

    def skip_job(self, current_url):
        """
        Skip processing the current job listing and go to the next one.

        Args:
            current_url (str): The URL of the current job listing page.

        Returns:
            bool: True if the job was skipped successfully, False otherwise.
        """
        try:
            print("SKIPPING JOB")
            self.click_index += 1
            print("Click Index: " + str(self.click_index))
            self.driver.get(current_url)
            return True

        except Exception as e:
            print("Exception while skipping job: " + str(e))
