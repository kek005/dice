import time,math,random,os
from selenium import webdriver
import requests
import datetime
import json
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
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
        print("code line 45")
        #self.generateUrls()
        countJobClicked = 0
        countJobs = 0
        countJobApply = 0

        #self.driver.get("https://www.dice.com/")
        self.driver.get("https://www.dice.com/home/home-feed")
        time.sleep(random.uniform(7, 11))
        # Find the first shadow host element on the page
        first_shadow_host = self.driver.find_element(By.TAG_NAME, "dhi-seds-nav-header")
        # Use JavaScript to retrieve the shadow root from the shadow host
        first_shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", first_shadow_host)
        # Find the nested shadow host element within the first shadow root
        #second_shadow_host = first_shadow_root.find_element(By.TAG_NAME, "dhi-seds-nav-header-display")
        second_shadow_host = first_shadow_root.find_element(By.CLASS_NAME, "hydrated")
        # Use JavaScript to retrieve the shadow root from the shadow host
        second_shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", second_shadow_host)
        # Find the nested shadow host element within the second shadow root
        third_shadow_host = second_shadow_root.find_element(By.CLASS_NAME, "hydrated")
        # Use JavaScript to retrieve the shadow root from the shadow host
        third_shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", third_shadow_host)
        # Find your target element within the nested shadow root
        target = third_shadow_root.find_element(By.CSS_SELECTOR, "a.icon[href='https://www.dice.com/jobs']")
        target.click()
        time.sleep(random.uniform(3, 7))
        #time.sleep(random.uniform(3, 7))

        # input the search keyword
        self.driver.find_element(By.CSS_SELECTOR, "#typeaheadInput").clear()
        time.sleep(random.uniform(3, 7))
        self.driver.find_element(By.CSS_SELECTOR, "#typeaheadInput").send_keys("QA")
        time.sleep(random.uniform(3, 7))
        # enter the location
        #self.driver.find_element(By.CSS_SELECTOR, "#google-location-search").clear()
        #self.driver.find_element(By.CSS_SELECTOR, "#google-location-search").send_keys("Remote Only")
        #time.sleep(5)
        # click the search button
        self.driver.find_element(By.CSS_SELECTOR, "#submitSearch-button").click()
        time.sleep(random.uniform(3, 7))

        # select 100 jobs per page and get the total number of jobs
        try:
            # Locate the dropdown element
            dropdown_element = self.driver.find_element(By.CSS_SELECTOR, "#pageSize_2")
            # Create a Select instance
            dropdown = Select(dropdown_element)
            # Select the option with value="100"
            #dropdown.select_by_value("100")
            dropdown.select_by_value("20")
            # Adding a wait time for the page to load after changing the number of jobs per page
            time.sleep(random.uniform(3, 7))
            self.driver.execute_script("window.scrollTo(0, 170);")
            # Locate the element containing the job count
            print("I'm locating the element containing the job count")
            print("code line 99")
            #job_count_element = self.driver.find_element(By.CSS_SELECTOR, "span[data-cy='search-count-mobile']")
            time.sleep(random.uniform(3, 7))
            job_count_element = self.driver.find_element(By.CSS_SELECTOR, "span[data-cy='search-count-mobile']") # span[data-cy='search-count-mobile'] #totalJobCount
            # Extract the text content of the element
            job_count_text = job_count_element.text
            print("Job Count Text:", job_count_text)  # Example: "15,920"
            print("code line 104")
            # Parse the text content to extract the number
            print("I'm parsing the text content to extract the number")
            job_count = int(job_count_text.replace(",", ""))
            print("Total jobs found:", job_count)
            print("code line 109")
            #job_per_page = 100
            job_per_page = 20
            # Find the total number of pages
            total_pages = math.ceil(job_count / job_per_page)
            print("Total pages:", total_pages) 
            print("code line 115") 
        except:
             pass
        
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
                job_link_xpath = f"//a[@id='{job_id}']"
                print("Job link XPath:", job_link_xpath)
                time.sleep(random.uniform(2, 4))

                # Find the element and click it
                try:
                    print("I'm constructing an xpath locator to click job link")
                    job_link = self.driver.find_element(By.XPATH, job_link_xpath)
                    time.sleep(random.uniform(2, 7))
                    print("I'M clicking job link")
                    job_link.click()
                    time.sleep(random.uniform(6, 9)) # wait for new tab to open 
                    print("Clicked job link:", job_link)
                    print("code line 152")
                    print("Because I clicked the job link, a new tab has been opened")
                    print("Now I will switch to the new tab")
                    # Switch to the new tab
                    # Get all window handles
                    all_windows = self.driver.window_handles
                    new_window = all_windows[-1]  # The new tab should be the last one
                    self.driver.switch_to.window(new_window)  # Switch to the new tab
                    time.sleep(random.uniform(4, 7))
                    print("Switched to new tab")
                    print("code line 162")
                    # Handle actions in the new page or tab here
                    # ...
                    #job_title = "test"
                    #job_company = "test"
                    job_title = self.driver.find_element(By.CSS_SELECTOR, "#jobdetails > h1").text # #jobdetails > h1  or body > div:nth-child(3) > div:nth-child(5) > main:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > h1:nth-child(1)
                    print("Job Title:", job_title)
                    print("code line 162")
                    job_company = self.driver.find_element(By.CSS_SELECTOR, "#jobdetails > div > ul > li.job-header_jobDetailFirst__xI_5S.job-header_companyName__Mx3ZU.text-center.font-sans.text-base.non-italic.font-normal.md\:mr-4.md\:text-left.md\:flex-nowrap > ul > li > a").text
                    print("Job Company:", job_company)
                    print("code line 165")

                    # Apply for the job
                    print("I'm calling the apply_for_job method")
                    self.apply_for_job(job_id, job_title, job_company, countJobApply)
                    print("Returning from the method apply_for_job")
                    print("code line 179")

                    countJobClicked += 1
                    time.sleep(random.uniform(5, 7))
                    print(f"Total job clicked: {countJobClicked}")
                    print(f"Total job applied: {countJobApply}")
                    print("I'm going back to the job listings page")

                    # Return to the job listings page
                    # Close the new tab
                    self.driver.close()
                    # Switch back to the original window
                    self.driver.switch_to.window(all_windows[0])
                    time.sleep(random.uniform(4, 7))  # Adjust timing based on page load speed

                except Exception as e:
                    print("Inside the except block for the try block to click job link")
                    print("code line 199")
                    print(f"Error clicking job link with ID {job_id}: {e}")
                    print("Why this error message?")

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


    def apply_for_job(self, job_id, job_title, job_company, countJobApply):
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

        except Exception as e:
            print(f"The button Apply is not available, which mean job has already been applyied  {job_title}: {e}")
            self.log_alreadycomplete_job(job_title, job_company)
            print("I'm returning from the apply_for_job method at except block")
            print("code line 241")
            return

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
                print("Next button has been cliked")
                print("code line 250")
                time.sleep(random.uniform(3, 7))

                # Check if there is a form present to be filled
                # Here, instead of if self.is_form_present(), directly handle form elements
                try:
                    print("I'm checking if there is a form present to be filled inside the try")
                    self.check_and_handle_form_elements(form_completed)
                except Exception as e:
                    print(f"Something bad happen when checking for form to apply. Here is the error: {e}")
                    print("There is no element to handle that is why it was not itterable")
                    form_completed = True

                # Check if the Next button is present and click it
                # Next button and Submit button have the same CSS selector
                # So no need to check for Submit button separately

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

                # Check for error message
                print("I'M CHECKING FOR ERROR MESSAGE JUST IN INCASE")
                error_message_elements = self.driver.find_elements(By.CSS_SELECTOR, ".error-text")
                if error_message_elements and error_message_elements[0].is_displayed():
                    print(f"Error in form submission for job {job_id}: {error_message_elements[0].text}")
                    form_completed = False
                    print("I set form completion to False since there is an error message")
                    break

                print("while loop is done")
                print("code line 290")
                print("I'm going to break the while loop")
                print("If correct it should go back to click the first next button")
                print("And because there is no next button it should go to the except block where it will print job applied")
                print("code line 306")

            if not form_completed:
                print(f"Could not complete form for job {job_title}")
                self.log_incomplete_job(job_title=job_title, job_company=job_company)
                print("I'm logging incomplete job")
            else:
                print(f"Applied for job {job_title}")
                self.log_completed_job(job_title=job_title, job_company=job_company)
                print("I'm logging completed job")

            #print(f"Applied for job {job_id}")
        except Exception as e:
            print(f"Just applied job: {job_title}")
            countJobApply += 1
            print(f"Total job applied: {countJobApply}")
            self.log_completed_job(job_title, job_company)  # Log the exception case as incomplete

    
    def check_and_handle_form_elements(self, form_completed):
        print("I'm inside the function: check_and_handle_form_elements()")
        # Selectors for different form elements
        form_selectors = {
            'radio': "input[type='radio']:not(:checked)",
            'input_text': "input[type='text']:not([value]), input[type='email']:not([value]), input[type='number']:not([value])",
            'select': "select",
            'textarea': "textarea:not([value])",
            'checkbox': "input[type='checkbox']:not(:checked)"
        }

        # Iterate over the selectors to find and handle form elements
        for element_type, selector in form_selectors.items():
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            for elem in elements:
                self.handle_form_element(elem, element_type, form_completed)  # Handle each element
        
        print("I'm returning from the function: check_and_handle_form_elements()")

    
    def handle_form_element(self, element, element_type, form_completed):
        print("I'm inside the function: handle_form_element()")
        print("I will set the form completion to False as the gpt is not working to answer the questions for now")
        form_completed = False  # Set form completion to False as the GPT-3 call is not working for now
        print("I set form completion to False as the GPT-3 call is not working for now")
        try:
            # Logic to interact with the element based on its type
            if element_type == 'input_text' or element_type == 'textarea':
                # Handle input text, email, number, and textareas
                answer = self.ask_gpt("Please provide a suitable answer")  # Replace with the appropriate GPT-3 call
                element.send_keys(answer)

            elif element_type == 'radio':
                # Assuming 'element' is the shadow host for the radio buttons
                shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
                question_slot = shadow_root.find_element(By.CSS_SELECTOR, "h4 > slot")
                question_text = self.driver.execute_script("return arguments[0].textContent", question_slot).strip()
                # Now you have the question_text, send it to GPT-3
                gpt_response = self.ask_gpt(question_text)  # This function should call GPT-3 API and return the response
                # gpt_response is assumed to be "Yes" or "No" based on your use case
                # Find the radio button with the value that matches the GPT-3 response
                radio_buttons = shadow_root.find_elements(By.CSS_SELECTOR, "input[type='radio']")
                for radio in radio_buttons:
                    if radio.get_attribute('value') == gpt_response:
                        self.driver.execute_script("arguments[0].click()", radio) # Click the radio button based on the GPT response
                        break  # Break after clicking the matching radio button

            elif element_type == 'checkbox':
                # Handle checkboxes by clicking the first unchecked option
                element.click()

            elif element_type == 'select':
                # Handle select dropdowns by selecting the first option that isn't the placeholder
                Select(element).select_by_index(1)

            print("I'm returning from the function: handle_form_element() on try block")

        except Exception as e:
            print(f"Error handling form element: {e}")
            print("This exception is from the handle_form_element function")
            form_completed = False  # Set form completion to False as the GPT-3 call is not working for now
            print("I set form completion to False in the except block for the try block in the handle_form_element function")
            print("line 369")
            print("I'm returning from the function: handle_form_element() on except block")

    
    def ask_gpt(self, question):
        # Replace 'your_api_key' with your actual OpenAI API key and adjust the payload as necessary
        headers = {
            'Authorization': 'Bearer your_api_key',
            'Content-Type': 'application/json',
        }
        data = {
            'model': 'text-davinci-003',
            'prompt': question,
            'temperature': 0.7,
            'max_tokens': 60,
        }
        response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=json.dumps(data))
        response_json = response.json()
        answer = response_json.get('choices', [{}])[0].get('text', '').strip()
        return answer

    def log_incomplete_job(self, job_title, job_company):
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Logic to log the job ID with timestamp for which form completion failed
        with open("incomplete_jobs.log", "a") as log_file:
            log_file.write(f"{current_time} - Failed to complete application for job title: {job_title} from {job_company}\n")

        # Additional logic for logging can be added here
            
    def log_completed_job(self, job_title, job_company):
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Logic to log the job ID with timestamp for which application was successfully completed
        with open("completed_jobs.log", "a") as log_file:
            log_file.write(f"{current_time} - Successfully applied for job: {job_title} from {job_company}\n")

        # Additional logic for logging can be added here.
            
    def log_alreadycomplete_job(self, job_title, job_company):
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Logic to log the job ID with timestamp for which application was successfully completed
        with open("alreadycomplete_jobs.log", "a") as log_file:
            log_file.write(f"{current_time} - Job already applied for: {job_title} from {job_company}\n")

        # Additional logic for logging can be added here.


start = time.time()
Dice().diceJobApply()
end = time.time()