import time,math,random,os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# Initializing various Python modules like time, math, random, os, and Selenium-related classes.

options = Options()   # Creating a new instance of Chrome Options
webdriver_path = r"C:\chromedriver.exe"   # Path to the ChromeDriver executable

# Create a Service object and pass it to the WebDriver
service = Service(webdriver_path)  # Creating a Service object with the path to the ChromeDriver

class Dice:
    def __init__(self):
            # Constructor of the Dice class
            # Here, we are configuring Chrome options for the Selenium WebDriver.
        
            options.add_argument(r"--user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\User Data")  # Setting the user data directory for Chrome
            options.add_argument(r'--profile-directory=Profile 1')  # Setting the profile directory for Chrome
            options.add_argument('--disable-gpu')  # Disable GPU (useful for headless mode)
            options.add_argument('--no-sandbox')  # Disable the sandbox (if running as root)
            options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
            #options.add_argument(r'--profile-directory=Profile')
            self.driver = webdriver.Chrome(service=service, options=options)   # Creating the Chrome WebDriver with the specified service and options


    def diceJobApply(self):
        # Main method to apply for jobs on Dice
        print("Starting diceJobApply method")
        #self.generateUrls()
        countApplied = 0
        countJobs = 0

        self.driver.get("https://www.dice.com/")
        time.sleep(random.uniform(4, 7))
        # Find the first shadow host element on the page
        first_shadow_host = self.driver.find_element(By.TAG_NAME, "dhi-seds-nav-header")
        # Use JavaScript to retrieve the shadow root from the shadow host
        first_shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", first_shadow_host)
        # Find the nested shadow host element within the first shadow root
        #second_shadow_host = first_shadow_root.find_element(By.TAG_NAME, "dhi-seds-nav-header-display")
        second_shadow_host = first_shadow_root.find_element(By.CLASS_NAME, "hydrated")
        # Use JavaScript to retrieve the shadow root from the shadow host
        second_shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", second_shadow_host)
        # Find your target element within the nested shadow root
        target = second_shadow_root.find_element(By.CSS_SELECTOR, "a.icon[href='https://www.dice.com/jobs']")
        target.click()
        time.sleep(5)
        #time.sleep(random.uniform(3, 7))

        # input the search keyword
        self.driver.find_element(By.CSS_SELECTOR, "#typeaheadInput").clear()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#typeaheadInput").send_keys("QA")
        time.sleep(5)
        # enter the location
        #self.driver.find_element(By.CSS_SELECTOR, "#google-location-search").clear()
        #self.driver.find_element(By.CSS_SELECTOR, "#google-location-search").send_keys("Remote Only")
        #time.sleep(5)
        # click the search button
        self.driver.find_element(By.CSS_SELECTOR, "#submitSearch-button").click()
        time.sleep(15)
        
        # Locate the element containing the job count
        print("I'm locating the element containing the job count")
        job_count_element = self.driver.find_element(By.CSS_SELECTOR, "span[data-cy='search-count-mobile']")
        # Extract the text content of the element
        job_count_text = job_count_element.text
        print("Job Count Text:", job_count_text)  # Example: "15,920"

        # Parse the text content to extract the number
        print("I'm parsing the text content to extract the number")
        job_count = int(job_count_text.replace(",", ""))
        print("Total jobs found:", job_count)

        self.driver.execute_script("window.scrollTo(0, 70);")

        # get all the job links
        # Find all job posting elements by their class name
        job_posting_elements = self.driver.find_elements(By.CLASS_NAME, "card-title-link")
        print("Total jobs found: ", len(job_posting_elements))
        # Extract the IDs from these elements
        job_ids = [elem.get_attribute('id') for elem in job_posting_elements if elem.get_attribute('id')]
        print("Job IDs:", job_ids)
        time.sleep(15)

        for job_id in job_ids:
            # Construct the XPath using the ID
            job_link_xpath = f"//a[@id='{job_id}']"
            print("Job link XPath:", job_link_xpath)

            # Find the element and click it
            try:
                job_link = self.driver.find_element(By.XPATH, job_link_xpath)
                time.sleep(2)
                print("I'M clicking job link")
                job_link.click()
                time.sleep(5) # wait for new tab to open 
                print("Clicked job link:", job_link)
                # Switch to the new tab
                # Get all window handles
                all_windows = self.driver.window_handles
                new_window = all_windows[-1]  # The new tab should be the last one
                self.driver.switch_to.window(new_window)  # Switch to the new tab
                time.sleep(5)
                print("Switched to new tab")
                # Handle actions in the new page or tab here
                # ...

                # Return to the job listings page
                # Close the new tab
                self.driver.close()
                # Switch back to the original window
                self.driver.switch_to.window(all_windows[0])
                time.sleep(2)  # Adjust timing based on page load speed

            except Exception as e:
                print(f"Error clicking job link with ID {job_id}: {e}")

                # Re-find job posting elements to avoid stale element reference
                job_posting_elements = self.driver.find_elements(By.CLASS_NAME, "card-title-link")
                job_ids = [elem.get_attribute('id') for elem in job_posting_elements if elem.get_attribute('id')]

start = time.time()
Dice().diceJobApply()
end = time.time()