import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class LandingPage(Base):

    url = "https://yolwise.com"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    authorization_button = "/html/body/div/div[1]/div/div/div[14]/a"

    # Getters
    def get_authorization_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.authorization_button)))

    # Actions
    def click_authorization_button(self):
        self.get_authorization_button().click()
        print("Click authorization button")

    # Methods
    def landing_page(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.get_current_url()
        self.click_authorization_button()
        print("Open login page, current URL:", self.driver.current_url)
