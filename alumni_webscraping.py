from selenium import webdriver
from selenium.webdriver.common.by import By
import time


linkedin_login_page = "https://www.linkedin.com/login/"
ufsc_alumni_page = 'https://www.linkedin.com/school/ufsc/people/'


browser = webdriver.Firefox()
browser.get(linkedin_login_page)


with open("config.txt") as file:
    lines = file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()

# Locate the username and password elements
username_element = browser.find_element(By.ID, 'username')
password_element = browser.find_element(By.ID, 'password')

# Send the credentials to the input fields
username_element.send_keys(username)
password_element.send_keys(password)

login_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()

#wait for 5 seconds, in order to see the result
time_to_wait = 3
time.sleep(time_to_wait)

browser.get(ufsc_alumni_page)

time_to_wait = 3

# Locate the parent button or div that contains the SVG
# button_element = browser.find_element(By.XPATH, '//button[@type="button"]')
# # Click the button
# button_element.click()
# button_element.click()
# button_element.click()
