import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Credentials
username = "standard_user"
password = "secret_sauce"

# Expected URL after successful login
expected_url = "https://www.saucedemo.com/inventory.html"

# Initialize the WebDriver (assuming you have the appropriate WebDriver for your browser)
driver = webdriver.Chrome()  # You can choose a different browser

# Step 1: Open the site
driver.get("https://www.saucedemo.com/")

# Step 2: Locate the Username field and enter the username
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(username)

# Step 3: Locate the Password field and enter the password
password_field = driver.find_element(By.XPATH, "//input[@type='password']")
password_field.send_keys(password)

# Step 4: Click the Login button
login_button = driver.find_element(By.NAME, "login-button")
login_button.click()

# Step 5: Get the current URL
current_url = driver.current_url

# Step 6: Check if the current URL matches the expected URL
assert current_url == expected_url


# Close the browser window
driver.quit()
