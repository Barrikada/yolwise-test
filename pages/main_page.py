import time
from datetime import datetime, timedelta

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class MainPage(Base):

    url = "https://yolwise.com/main"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    departure_avia = "//input[@placeholder='Nereden']"
    arrival_avia = "//input[@placeholder='Nereye']"
    search_button = "//span[@class='_content_8h06k_16']"
    departure_city = ("//*[@id='root']/div/div/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/"
                 "div/div[2]/div/div[2]")
    arrival_city = ("//*[@id='root']/div/div/div[2]/div/div"
                    "[1]/div/div/div[1]/div[1]/div[1]/div[3]/div/div[2]/div/div/div[2]")
    main_word = "//*[@id='root']/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[1]"

    # Getters

    def get_departure_avia(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.departure_avia)))

    def get_arrival_avia(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.arrival_avia)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_departure_city(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.departure_city)))

    def get_arrival_city(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.arrival_city)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_departure_avia(self):
        self.get_departure_avia().click()
        print("Click avia from")

    def click_arrival_avia(self):
        self.get_arrival_avia().click()
        print("Click avia to")

    def click_search_button(self):
        self.get_search_button().click()
        print("Click button find")

    def send_departure_avia(self, city_from):
        self.click_departure_avia()
        self.get_departure_avia().send_keys(city_from)
        print("Input avia from")

    def send_arrival_avia(self, city_to):
        self.click_arrival_avia()
        self.get_arrival_avia().send_keys(city_to)

    def click_departure_city(self):
        self.get_departure_city().click()
        print("Click city from")

    def click_arrival_city(self):
        self.get_arrival_city().click()

    # Methods

    def find_avia_today(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        self.get_current_url()
        self.click_departure_avia()
        self.click_departure_city()
        self.click_arrival_avia()
        self.click_arrival_city()
        time.sleep(2)
        self.click_search_button()
        self.get_assert_word(self.get_main_word(), "Aktarmalar")
