from selenium import webdriver
from pages.login_page import LoginPage


def authorization():
    driver = webdriver.Chrome()

    print("Start Test")

    try:
        login = LoginPage(driver)
        login.authorization()
    finally:
        driver.quit()

    print("Finish Test")