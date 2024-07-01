from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def display_cookies(driver, stage):
    cookies = driver.get_cookies()
    print(f"\nCookies {stage}:")
    for cookie in cookies:
        print(cookie)


def login_saucedemo(driver, username, password):
    # Navigate to the URL
    driver.get("https://www.saucedemo.com/")

    # Display cookies before login
    display_cookies(driver, "before login")

    # Locate and fill in the username and password fields
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)

    # Click the login button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # Display cookies after login
    display_cookies(driver, "after login")


def logout_saucedemo(driver):
    # Click the menu button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()

    # Click the logout button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()


if _name_ == "_main_":
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Use the appropriate driver for your browser

    try:
        # Perform login
        login_saucedemo(driver, "standard_user", "secret_sauce")

        # Perform logout
        logout_saucedemo(driver)

        # Verify the cookies after logout
        display_cookies(driver, "after logout")

    finally:
        # Close the WebDriver
        driver.quit()