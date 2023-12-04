from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import users
import time

# pip install webdriver_manager selenium-wire

# Proxy configuration
proxy_username = 'username'
proxy_password = 'password'
proxy_url = f'http://{proxy_username}:{proxy_password}@gate.nodemaven.com:8080'
seleniumwire_options = {'proxy': {'http': proxy_url, 'verify_ssl': True}}

# WebDriver setup
driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

# Navigate to Facebook
driver.get("https://www.facebook.com")

# Find login elements
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "pass")
login_btn = driver.find_element(By.NAME, "login")

# Input login credentials and click login
email_input.send_keys(users.username)
password_input.send_keys(users.password)
login_btn.click()

# Wait for 60 seconds (replace with appropriate wait conditions)
time.sleep(60)

# Close the browser window when done
driver.quit()
