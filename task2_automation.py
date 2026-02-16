from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
import time

# random email & password
random_email = ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"
random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:8000")

wait = WebDriverWait(driver, 10)

# Find email using placeholder
email_field = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email']"))
)

# Find password using type=password
password_field = driver.find_element(By.XPATH, "//input[@type='password']")

email_field.send_keys(random_email)
password_field.send_keys(random_password)

time.sleep(3)

driver.quit()

print("Automation completed successfully.")
