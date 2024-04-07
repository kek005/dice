import time,math,random,os
from selenium import webdriver
import requests
import datetime
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


class Dice:
    def __init__(self):
            options = Options()
            # Path to your Firefox profile
            profile_path = r'C:\Users\DELL\AppData\Roaming\Mozilla\Firefox\Profiles\6d4dc8w2.default-release'
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            #options.add_argument('--headless')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-extensions')
            # Set up Firefox options if necessary
            # Set the profile using the .profile property
            options.profile = profile_path
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service, options=options)
            self.countJobApply = 0


    def diceJobApply(self):
        # Main method to apply for jobs on Dice
        print("Starting diceJobApply method")
        print("code line 45")
        #self.generateUrls()
        countJobClicked = 0
        countJobs = 0

        #self.driver.get("https://www.dice.com/")
        self.driver.get("https://www.dice.com/home/home-feed")
        time.sleep(random.uniform(15, 20))

        # JavaScript to navigate through shadow DOMs and click the target element
        js_click_script = """
        var firstShadowHost = document.querySelector('dhi-seds-nav-header');
        var firstShadowRoot = firstShadowHost.shadowRoot;
        var secondShadowHost = firstShadowRoot.querySelector('.hydrated');
        var secondShadowRoot = secondShadowHost.shadowRoot;
        var thirdShadowHost = secondShadowRoot.querySelector('.hydrated');
        var thirdShadowRoot = thirdShadowHost.shadowRoot;
        var target = thirdShadowRoot.querySelector("a.icon[href='https://www.dice.com/jobs']");
        target.click();
        """
        # Execute the JavaScript code
        self.driver.execute_script(js_click_script)
        time.sleep(random.uniform(3, 7))

        # input the search keyword
        # Locate the input element
        input_element = self.driver.find_element(By.CSS_SELECTOR, "#typeaheadInput")
        # Click the input field, select all text, and delete
        input_element.click()  # Focus on the element
        input_element.send_keys(Keys.CONTROL + "a")  # Select all text in the input
        input_element.send_keys(Keys.BACK_SPACE)  # Delete the selected text
        #self.driver.find_element(By.CSS_SELECTOR, "#typeaheadInput").clear()
        time.sleep(random.uniform(3, 7))
        self.driver.find_element(By.CSS_SELECTOR, "#typeaheadInput").send_keys("QA")
        time.sleep(random.uniform(3, 7))
        # enter the location
        self.driver.find_element(By.CSS_SELECTOR, "#google-location-search").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#google-location-search").send_keys("Remote Only")
        time.sleep(5)
        # click the search button
        self.driver.find_element(By.CSS_SELECTOR, "#submitSearch-button").click()
        time.sleep(random.uniform(3, 7))

        # JavaScript to find and click the button to select today's job postings
        js_click_script = """
        var buttons = document.querySelectorAll('button[data-cy="posted-date-option"]');
        for(var i = 0; i < buttons.length; i++) {
            if(buttons[i].getAttribute('data-cy-index') == '1') {
                buttons[i].click();
                break;
            }
        }
        """
        # Execute the JavaScript code
        self.driver.execute_script(js_click_script)
        time.sleep(random.uniform(3, 7))

        # JavaScript to click the button to filter search results by remote
        # JavaScript snippet to click an element based on XPath
        js_script = """
        var xpath = "//button[@aria-label='Filter Search Results by Remote']//i[@class='fa ng-tns-c584973506-10 fa-square-o']";
        var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (element) element.click();
        """
        print("I'm executing the JavaScript script to click the button to filter search results by remote")
        # Execute the JavaScript script
        self.driver.execute_script(js_script)

        # //i[@class='fa fa-square-o']

        # JavaScript to click the button to filter search results by easy apply
        js_script = """
        var xpath = "//i[@class='fa fa-square-o']";
        var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (element) element.click();
        """
        print("I'm executing the JavaScript script to click the button to filter search results by easy apply")
        # Execute the JavaScript script
        self.driver.execute_script(js_script)




        # select 100 jobs per page and get the total number of jobs
        try:
            # JavaScript code to select the option with value="100"
            js_script = """
                var select = document.querySelector('#pageSize_2');
                for(var i = 0; i < select.options.length; i++){
                    if(select.options[i].value == '100'){
                        select.selectedIndex = i;
                        select.dispatchEvent(new Event('change'));
                        break;
                    }
                }
                """
            # Execute the JavaScript code
            self.driver.execute_script(js_script)
            # Adding a wait time for the page to load after changing the number of jobs per page
            time.sleep(random.uniform(3, 7))
            total_pages = 2
            print("Total pages:", total_pages)
            print("code line 115") 
        except:
             pass
        
        total_pages = 2
        # Loop through all the pages
        for page in range(1, total_pages + 1):
            print("I'm applying on Page:", page)
            print("code line 121")
            # get all the job links
            try:
                # get all the job links on curent page
                # Find all job posting elements by their class name
                job_posting_elements = self.driver.find_elements(By.CLASS_NAME, "card-title-link")
                print("Total jobs found on this page: ", len(job_posting_elements))
                print("code line 129")
                # Extract the IDs from these elements
                job_ids = [elem.get_attribute('id') for elem in job_posting_elements if elem.get_attribute('id')]
                print("Job IDs:", job_ids)
                time.sleep(random.uniform(5, 10))
            except Exception as e:
                print("Error getting job links on current page:", e)

            # loop through all the job links on current page
            for job_id in job_ids:
                # Construct the XPath using the ID
                print("I m constructing the Xpath using the IDs")
                job_link_xpath = f"//a[@id='{job_id}']"
                print("Job link XPath:", job_link_xpath)
                time.sleep(random.uniform(2, 4))

                # Find the element and click it
                try:
                    print("I'm getting the webElement from the xpath locator to click job link")
                    job_link = self.driver.find_element(By.XPATH, job_link_xpath)
                    time.sleep(random.uniform(2, 7))
                    print("I'M clicking job link")
                    original_window = self.driver.current_window_handle
                    job_link.click()
                    time.sleep(random.uniform(6, 9)) # wait for new tab to open 
                    print("Clicked job link:", job_link)
                    print("code line 152")
                    print("Because I clicked the job link, a new tab has been opened")
                    print("Now I will switch to the new tab")
                    print("Before that I will wait for the total number of windows to be 2")
                    # Wait for a new window/tab to open
                    WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
                    print("I just waited for the total number of windows to be 2")
                    print("Now I will try to switch to the new tab")
                    # Switch to the new tab
                    for window_handle in self.driver.window_handles:
                        if window_handle != original_window:
                            self.driver.switch_to.window(window_handle)
                            break
                    time.sleep(random.uniform(8, 13))
                    print("I just Switched to new tab")
                    print("code line 162")
                    # Handle actions in the new page or tab here
                    job_title = self.driver.find_element(By.CSS_SELECTOR, "#jobdetails > h1").text # #jobdetails > h1  or body > div:nth-child(3) > div:nth-child(5) > main:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > h1:nth-child(1)
                    print("Job Title:", job_title)
                    print("code line 162")
                    job_company = self.driver.find_element(By.CSS_SELECTOR, "#jobdetails > div > ul > li.job-header_jobDetailFirst__xI_5S.job-header_companyName__Mx3ZU.text-center.font-sans.text-base.non-italic.font-normal.md\:mr-4.md\:text-left.md\:flex-nowrap > ul > li > a").text
                    print("Job Company:", job_company)
                    print("code line 165")

                    # Apply for the job
                    print("I'm calling the apply_for_job method")
                    self.apply_for_job(job_id, job_title, job_company)
                    print("I just return from the method apply_for_job")
                    print("code line 179")

                    countJobClicked += 1
                    time.sleep(random.uniform(5, 7))
                    print(f"Total job clicked: {countJobClicked}")
                    print(f"Total job applied: {self.countJobApply}")
                    print("I'm going back to the job listings page")

                    # Return to the job listings page
                    # Close the new tab
                    self.driver.close()
                    time.sleep(random.uniform(5, 7))
                    # Switch back to the original window
                    self.driver.switch_to.window(original_window)
                    print("I just switch back to ll_windows[0]the first window")
                    print("End of the try block line 189")
                    time.sleep(random.uniform(4, 7))  # Adjust timing based on page load speed

                except Exception as e:
                    print("Inside the except block for the try block to click job link")
                    print("code line 199")
                    print(f"Here is the error message {job_id}: {e}")

                    # Re-find job posting elements to avoid stale element reference
                    job_posting_elements = self.driver.find_elements(By.CLASS_NAME, "card-title-link")
                    job_ids = [elem.get_attribute('id') for elem in job_posting_elements if elem.get_attribute('id')]

            # Navigate to the next page if not the last page
            if page < total_pages:
               try:
                    # Find the next button element
                    next_button = self.driver.find_element(By.CSS_SELECTOR, "li[class='pagination-next page-item ng-star-inserted'] a[class='page-link']")
                    # Click the next button
                    next_button.click()
                    time.sleep(random.uniform(3, 7))
               except Exception as e:
                    print("Error getting next button:", e)


    def apply_for_job(self, job_id, job_title, job_company):
        # Initialization
        start_time = time.time()
        form_completed = True

        # Navigate to the job details page, and interact with the shadow DOM to click the apply button
        try:
            # click the apply button
            # Find the shadow host
            shadow_host = self.driver.find_element(By.CSS_SELECTOR, f'apply-button-wc[job-id="{job_id}"]')
            # Get the shadow root
            shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
            # Find the button inside the shadow root and click it
            apply_button = shadow_root.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
            self.driver.execute_script('arguments[0].click()', apply_button)
            time.sleep(random.uniform(3, 7))
            print("I just Clicked apply button")
            print("I'm scrolling down the page")
            self.driver.execute_script("window.scrollTo(0, 570);")
            time.sleep(random.uniform(3, 7))

            # After clicking the Apply button, click the Next or Submit buttons as required
            print("I arleady clicked the apply button")
            print("Now trying to click the next button")
            print("code line 243")
            try:
                # Click the Next or Submit buttons as required
                while True:
                    # Timeout check
                    if time.time() - start_time > 190:  # 300 seconds timeout
                        form_completed = True
                        print(f"Timeout reached for job {job_id}")
                        print("Unable to apply for job code line 218")
                        break
                    
                    # Click the first next on the resume page
                    print("Im clicking the first next button on resume page")
                    print("code line 247")
                    first_next = self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary btn-next btn-block']")
                    first_next.click()
                    print("I just clicked the first next button on resume page")
                    #self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary btn-next btn-block']")
                    print("First Next button has been cliked")
                    print("code line 250")
                    time.sleep(random.uniform(3, 7))

                    # Check if the Next button is present, then click it
                    print("I'm checking if the Next button is present after form completion and click it")
                    print("code line 270")
                    next_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[class='btn btn-primary btn-next btn-split']") #button[type='button'] span
                    if next_buttons:
                        next_buttons[0].click()
                        print("I just clicked the second next button")
                        print("I'm setting form complextion to True as the application most likely has 2 next button lifetime")
                        form_completed = True  # Set form completion to True since the form has likely been submitted
                        time.sleep(random.uniform(3, 7))
                    else:
                        # If neither Next nor Submit button is found, assume the submission was successful
                        print("No Next or Submit button found, assuming form submission was successful")
                        form_completed = True  # Set form completion to True since the form has likely been submitted
                        print("I set form completion to True since the form has likely been submitted line 248 in code")
                        break

                if not form_completed:
                    print(f"Could not complete form for job {job_title}")
                    self.log_incomplete_job(job_title=job_title, job_company=job_company)
                    print("I'm logging incomplete job")
                else:
                    print(f"Applied for job {job_title}")
                    self.log_completed_job(job_title=job_title, job_company=job_company)
                    print("I'm logging completed job")

            except Exception as e:
                print(f"Just applied job: {job_title}")
                self.countJobApply += 1
                print(f"Total job applied: {self.countJobApply}")
                self.log_completed_job(job_title, job_company)  # Log the exception case as incomplete
                print("I just applied for the job and I'm returning from the Apply job method")

        except Exception as e:
            print(f"The button Apply is not available, which mean job has already been applyied  {job_title}: {e}")
            self.log_alreadycomplete_job(job_title, job_company)
            print("I'm returning from the apply_for_job method at except block that show that job has already been applied for")
            print("code line 241")

        

    def log_incomplete_job(self, job_title, job_company):
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Logic to log the job ID with timestamp for which form completion failed
        with open("incomplete_jobs.log", "a") as log_file:
            log_file.write(f"{current_time} - Failed to complete application for job title: {job_title} from {job_company}\n")
            
    def log_completed_job(self, job_title, job_company):
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Logic to log the job ID with timestamp for which application was successfully completed
        with open("completed_jobs.log", "a") as log_file:
            log_file.write(f"{current_time} - Successfully applied for job: {job_title} from {job_company}\n")

            
    def log_alreadycomplete_job(self, job_title, job_company):
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Logic to log the job ID with timestamp for which application was successfully completed
        with open("alreadycomplete_jobs.log", "a") as log_file:
            log_file.write(f"{current_time} - Job already applied for: {job_title} from {job_company}\n")


start = time.time()
Dice().diceJobApply()
end = time.time()