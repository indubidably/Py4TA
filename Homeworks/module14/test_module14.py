from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

username = "notabot"
password = "1234"


def test_login(browser):
    browser.get("https://www.demoblaze.com/")
    login_button = browser.find_element(By.ID, "login2")
    login_button.click()

    wait = WebDriverWait(browser, timeout=5)

    wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))

    username_field = browser.find_element(By.ID, "loginusername")
    password_field = browser.find_element(By.ID, "loginpassword")
    assert username_field.is_displayed()
    assert password_field.is_displayed()

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = browser.find_element(By.XPATH, "//button[@onclick='logIn()']")
    login_button.click()

    wait.until(EC.visibility_of_element_located((By.ID, "logout2")))
    logout_button = browser.find_element(By.ID, "logout2")

    assert logout_button.is_displayed()
    assert "Welcome " + username in browser.find_element(By.XPATH, "/html/body").text


def test_cart(login):
    price_elems = login.find_elements(By.XPATH, "//h5")
    monitors_cat = login.find_element(By.XPATH, "//a[@onclick=\"byCat('monitor')\"]")
    monitors_cat.click()

    wait = WebDriverWait(login, timeout=5)

    # wait for filter to take place

    wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//h5")) < len(price_elems))
    price_elems = login.find_elements(By.XPATH, "//h5")
    prices = []
    for i in price_elems:
        prices.append(i.text)

    # find max price and click corresponding product
    highest = max(prices)
    xpath_expression = f"//h5[text()='{highest}']/preceding-sibling::h4/a"
    that_monitor = login.find_element(By.XPATH, xpath_expression)
    title = that_monitor.text
    that_monitor.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@onclick='addToCart(10)']")))
    assert title in login.find_element(By.XPATH, "/html/body").text
    assert highest in login.find_element(By.XPATH, "/html/body").text

    add_button = login.find_element(By.XPATH, "//a[@onclick='addToCart(10)']")
    add_button.click()

    wait.until(EC.alert_is_present())
    alert = login.switch_to.alert
    alert.accept()
    login.switch_to.default_content()

    cart_button = login.find_element(By.ID, "cartur")
    cart_button.click()

    xpath_expression = f"//td[text()='{title}']"
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))

    assert title in login.find_element(By.XPATH, "/html/body").text
    assert highest[1:-1] in login.find_element(By.XPATH, "/html/body").text
