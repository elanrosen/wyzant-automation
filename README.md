# Project README: Automated Tutor Job Application Processor

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

## How it Works
1. **Browser Initialization**: Creates a Chrome WebDriver instance with custom options.
2. **Job Processing**: Navigates to the Wyzant job listings page and processes each job.
3. **Job Evaluation**: Jobs are evaluated based on the rate, subject, and other criteria.
4. **Application Submission**: If a job meets the criteria, the script uses OpenAI's API to generate a personalized application message and submits the application.
5. **Error Handling**: Includes robust error handling for web scraping and network issues.

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