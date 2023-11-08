import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

username = "notabot"
password = "1234"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(browser):
    browser.get("https://www.demoblaze.com/")

    login_button = browser.find_element(By.ID, "login2")
    login_button.click()

    username_field = browser.find_element(By.ID, "loginusername")
    password_field = browser.find_element(By.ID, "loginpassword")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = browser.find_element(By.XPATH, "//button[@onclick='logIn()']")
    login_button.click()

    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.visibility_of_element_located((By.ID, "logout2")))

    yield browser
