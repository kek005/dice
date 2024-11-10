# Dice Job Application Automation
This Python script automates the process of searching and applying for jobs on Dice, using Selenium WebDriver to navigate the website and interact with the pages. This automation is particularly useful for job seekers looking to save time by applying to multiple job postings quickly.

Features
Automated Job Searching and Application: Searches for jobs based on specific keywords, navigates through job listings, and applies to positions on Dice.
Dynamic Form Filling: Interacts with form elements like text inputs, checkboxes, radio buttons, and dropdowns to automatically complete job application forms.
Shadow DOM Handling: Accesses elements within nested shadow DOMs, making it compatible with complex web components.
GPT Integration: Uses OpenAI's GPT API to provide answers to form questions (customizable for responses).
Logging System: Logs successfully applied jobs, incomplete applications, and already applied jobs for tracking purposes.
Prerequisites
Python 3.x: Ensure Python is installed on your system.

Selenium: Install Selenium for browser automation.
pip install selenium

ChromeDriver: Download ChromeDriver compatible with your Chrome browser version.

Webdriver Manager: Simplifies ChromeDriver setup.
pip install webdriver-manager

OpenAI API Key: Sign up for an API key if you intend to use GPT for responses.

Additional Libraries: Install other dependencies if needed.
pip install requests

Setup

Clone the Repository:
git clone https://github.com/kek005/dice.git

cd dice-job-automation

Configure the Script:
Update options.add_argument() in the __init__ function of the Dice class with your Chrome profile path or any other configurations required for the Chrome browser setup.
Add your OpenAI API key in the ask_gpt function by replacing 'your_api_key' with your actual OpenAI API key.

Environment Variables (Optional):
Use a .env file to store sensitive information like the OpenAI API key and load it securely.

Usage

Run the Script:
python dice_job_automation.py

How It Works:
The script navigates to Dice’s job search page, inputs a specified job keyword (e.g., "QA"), and sets job preferences.
It retrieves job postings, navigates to each job link, clicks the apply button, and interacts with any required form fields (text inputs, checkboxes, etc.).
Logs application status (completed, incomplete, or already applied) into respective log files.

File Logging:
The script logs all application attempts in text files for tracking.
Files created include:
completed_jobs.log: Logs successfully applied jobs.
incomplete_jobs.log: Logs jobs where the form completion failed.
alreadycomplete_jobs.log: Logs jobs that were already applied for.

Important Notes
Shadow DOM Elements: This script accesses elements within nested shadow DOMs, a common feature on modern websites. Ensure the selector paths are updated if the page structure changes.
OpenAI API Usage: The GPT-3 API calls in ask_gpt are rate-limited by your OpenAI subscription. Be mindful of usage and potential costs.
Timeouts and Delays: Randomized delays and timeouts are included to prevent detection by anti-bot mechanisms. Adjust these values as needed.

Disclaimer
This script is intended for personal use and must comply with Dice's terms of service. Use responsibly and avoid excessive requests that may violate Dice’s usage policies.

License
MIT License
