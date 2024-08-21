
# task-10 program to get followers and following count
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the Instagram profile
profile_url = 'https://www.instagram.com/guviofficial/'
driver.get(profile_url)

# Wait for page to load
driver.implicitly_wait(10)

# Extract followers count
followers_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[2]/ul/li[2]/div/button")
followers_count = followers_element.text

# Extract following count
following_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[2]/ul/li[3]/div/button")
following_count = following_element.text

# Print the results
print(f"Followers: {followers_count}")
print(f"Following: {following_count}")

# Close the browser
driver.quit()

