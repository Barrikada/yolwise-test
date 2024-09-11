import time
from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.landing_page import LandingPage


def test_find_avia():
    driver = webdriver.Chrome()
    print("Start test find avia")

    # landing = LandingPage(driver)
    # landing.landing_page()

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.find_avia_today()

    print("Finish test find avia")
    time.sleep(5)
    driver.quit()

