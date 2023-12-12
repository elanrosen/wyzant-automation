# Automated Tutoring Applications on Wyzant

## Overview
This Python project automates the process of applying for tutoring jobs on the Wyzant platform. It leverages the Selenium library for web scraping and browser automation, and the OpenAI API for generating personalized job application messages. The program's primary functionality includes browsing job listings, evaluating each job based on predefined criteria, and automatically submitting applications where suitable.

## Requirements
- Python 3.x
- Selenium WebDriver
- Python-decouple for configuration management
- OpenAI API Key for generating personalized messages

## Configuration
Before running the script, set up the following configurations in your environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key.
- `USER_PROFILE_DIR`: The path to your Chrome user data directory.

## Installation
1. Install the required Python packages:
   ```bash
   pip install selenium python-decouple openai
   ```
2. Download the appropriate ChromeDriver based on your Chrome version and add it to your PATH.

## Usage
1. Set your OpenAI API key and Chrome user profile directory in environment variables.
2. Run the script to start the job application process.
3. The script navigates through the job listings on Wyzant, evaluates them, and applies based on the set criteria.

## How Job Processing Works
The `JobProcessor` class in `job_logic.py` is responsible for processing job listings. Here's how it works:

1. **Browser Initialization**: The script initializes a Chrome WebDriver instance with custom options to interact with the Wyzant website.

2. **Job Processing**: The script navigates to the Wyzant job listings page and processes each job one by one.

3. **Job Evaluation**: Jobs are evaluated based on various criteria, including the recommended rate, subject, and other factors. The evaluation criteria include:

    - **Recommended Rate**: The script checks the recommended rate for the job, and if available, passess it through a rate calculator function to decide my specified rate for the job.
    
    - **Student Grade Level**: It considers the student's grade level to determine whether the job is suitable.

    - **Job Description and Subject**: The script also analyzes the job description and subject to decide whether the job is suitable.

4. **Application Submission**: If a job meets the criteria, the script uses OpenAI's API to generate a personalized application message. It also allows for inputting a rate for the application. Once the message and rate are set, the script submits the application.

5. **Error Handling**: The script includes robust error handling for web scraping and network issues. It accounts for cases where no jobs are found on a page, and it can handle exceptions gracefully.

## Additional Details
- The script employs a click index to determine which job listing to click on. It changes the click index periodically to avoid a repetitive pattern.

- The script handles both single-page and multi-page modes. In single-page mode, it refreshes the page if no jobs are found. In multi-page mode, it navigates to the next page if available or exits if there are no more pages.

- Depending on various factors like recommended rate, job description, and subject, the script decides whether to submit the application or skip the job.

- For skipped jobs, it updates the click index to proceed to the next job listing.


## Classes and Functions
- `JobProcessor`: Main class that handles job processing, evaluation, and application submission.
- `generate_openai_message`: Function to generate personalized messages using OpenAI's API.
- `approximate_function`, `print_separator`, `print_job_info`: Helper functions for various tasks.

## Limitations
- The script is specifically tailored for the Wyzant platform and may not work with other websites.
- Requires constant internet connection and depends on the structure of the Wyzant website, which may change.

## Contribution
Contributions are welcome. Please fork the repository and submit a pull request for any enhancements.

## License
This project is open-source and available under the MIT License.