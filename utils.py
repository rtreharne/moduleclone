from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import getpass
import time
import os

class CanvasSession:
    def __init__(self):
        # Get username and password from user
        self.username = input("Input your MWS email address: ")
        self.password = getpass.getpass("Input your MWS password: ")
        
        # Configure webdriver
        
        # Get the current directory
        current_dir = os.getcwd()

        # Append the file name to the current directory
        CHROMEDRIVER_PATH = os.path.join(current_dir, 'chromedriver.exe')
        

        service = Service(executable_path=CHROMEDRIVER_PATH)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--ignore-certificate-errors')
        self.browser = webdriver.Chrome(service=service, options=chrome_options)
        
        # Login
        self.browser.get('https://canvas.liverpool.ac.uk')
        
        username_input = self.browser.find_element(By.XPATH, "//input[@name='UserName']")
        password_input = self.browser.find_element(By.XPATH, "//input[@name='Password']")

        # Get submit button by text "LOG IN"
        submit_button = self.browser.find_element(By.XPATH, "//span[contains(text(),'Sign in')]")
        
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        
        submit_button.click()
        
        # Wait for 10 seconds
        print("wait ...")
        time.sleep(10)
        
        # Find all elements with the class "verification-code"
        elements = self.browser.find_elements(By.CLASS_NAME, "verification-code")
        
        # Print the text content of each element
        for element in elements:
            print("Verification code for DUO")
            print(element.text)

        # Countdown loop
        for i in range(20, 0, -1):
            print("You have {} seconds to enter your verification code.".format(i), end="\r")
            time.sleep(1)
        
        # Confirm trust browser
        try:
            self.browser.find_element(By.ID, "trust-browser-button").click()
            print("")
            print("Login Success.")
        except:
            print("")
            print("Login Failure")


class CMSession:
    def __init__(self):
        # Get username and password from user
        self.username = input("Input your MWS username: ")
        self.password = getpass.getpass("Input your MWS password: ")

        # Get the current directory
        current_dir = os.getcwd()

        # Append the file name to the current directory
        CHROMEDRIVER_PATH = os.path.join(current_dir, 'chromedriver.exe')

        
        # Configure webdriver
        service = Service(executable_path=CHROMEDRIVER_PATH)
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(service=service, options=options)
        
        # Login
        self.browser.get('https://liverpool-curriculum.worktribe.com/')
        
        username_input = self.browser.find_element(By.XPATH, "//input[@name='j_username']")
        password_input = self.browser.find_element(By.XPATH, "//input[@name='j_password']")

        # Get submit button by text "LOG IN"
        submit_button = self.browser.find_element(By.CLASS_NAME, "form-button")
        
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        
        submit_button.click()
        
        # Wait for 10 seconds
        print("wait ...")
        time.sleep(10)
        
        print("Verify your login by DUO")

class TulipSession:
    def __init__(self):
        # Get username and password from user
        self.username = input("Input your MWS username: ")
        self.password = getpass.getpass("Input your MWS password: ")
        
        # Configure webdriver
        service = Service(executable_path="C:/Users/treharne/Documents/chromedriver.exe")
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(service=service, options=options)
        
        # Login
        self.browser.get('https://tulip.liv.ac.uk/pls/new_portal/webwise.tul_bs_portal.home')
        
        username_input = self.browser.find_element(By.XPATH, "//input[@name='p_username']")
        password_input = self.browser.find_element(By.XPATH, "//input[@name='p_password']")

        # Get submit button by text "LOG IN"
        submit_button = self.browser.find_element(By.XPATH, "//button[contains(text(),'LOG IN')]")
        
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        
        submit_button.click()
        
        # Wait for 5 seconds
        print("wait ...")
        time.sleep(5)
        
        # Find all elements with the class "verification-code"
        elements = self.browser.find_elements(By.CLASS_NAME, "verification-code")
        
        # Print the text content of each element
        for element in elements:
            print("Verification code for DUO")
            print(element.text)

        # Countdown loop
        for i in range(20, 0, -1):
            print("You have {} seconds to enter your verification code.".format(i), end="\r")
            time.sleep(1)
        
        # Confirm trust browser
        try:
            self.browser.find_element(By.ID, "trust-browser-button").click()
            print("")
            print("Login Success.")
        except:
            print("")
            print("Login Failure")


if __name__ == "__main__":
    session = TulipSession()
    