# Wyzant Job Application Bot

The Wyzant Job Application Bot is a sophisticated Python-based tool designed to streamline the process of applying for tutoring positions on the Wyzant platform. It leverages Selenium for efficient web scraping and automation, incorporates the cutting-edge capabilities of OpenAI's GPT-4 for crafting personalized application messages, and utilizes MySQL for robust database management.

## Key Features

- **Automated Navigation**: Effortlessly traverses through Wyzant's job listings.
- **Advanced Filtering**: Selectively applies to jobs based on user-defined criteria such as rate, student grade level, and subject area.
- **Personalized Messaging**: Utilizes OpenAI's GPT-4 to generate unique and engaging application messages for each job.
- **Efficient Application Submission**: Automatically applies to jobs that meet the specified criteria.

## System Requirements

- Python version 3.6 or higher
- Selenium WebDriver
- OpenAI GPT-4 API
- python-decouple for environment management
- MySQL Connector Python for database interactions

## Installation and Setup

1. **Repository Cloning**:
   ```
   git clone [repository-url]
   ```
2. **Dependency Installation**:
   Execute the following command to install the required Python packages:
   ```bash
   pip install selenium openai python-decouple mysql-connector-python
   ```
3. **Environment Configuration**:
   Set up your `.env` file with the necessary credentials:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   USER_PROFILE_DIR=your_chrome_user_data_directory
   ```
4. **Execution**:
   Run the script using Python:
   ```bash
   python wyzant_bot.py
   ```

## Ethical Use Reminder

This script is developed solely for educational purposes. Users must adhere to Wyzant's terms of service and OpenAI's use case policy. Responsible and ethical usage is strongly encouraged.

## Script Overview

The script primarily consists of the following components:

- **Selenium WebDriver Configuration**: Sets up the Chrome browser for automation.
- **Job Application Logic**: Navigates through job listings, applies filters, and selects jobs based on predefined criteria.
- **Message Generation with OpenAI GPT-4**: Crafts personalized application messages using OpenAI's advanced language model.
- **Application Submission Process**: Automates the filling and submission of application forms.
- **Exception Handling**: Includes robust error and exception management to ensure smooth operation.
- **Database Integration**: Utilizes MySQL for storing and retrieving application data.

## Script Highlights

- `approximate_function(x)`: Calculates an appropriate rate based on various factors.
- `print_separator(char, length)`: Prints a separator line for better readability in console output.
- `print_job_info(title, info)`: Displays job details in a structured format.

## Usage Statistics

At the end of the script, it outputs the total number of jobs submitted and skipped, providing insights into the script's activity and efficiency.