from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class LoginPage(Base):

    url = "https://yolwise.com/login"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    email_name = "//input[@type='email']"
    password = "//input[@type='password']"
    login_button = "//button[@type='submit']"
    main_word = "//button[@type='submit']"

    # Getters
    def get_email_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_email_name(self, email_name):
        self.get_email_name().send_keys(email_name)
        print("Input email name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_email_name("demo@turkey.today")
        self.input_password("demo")
        self.click_login_button()
        # self.get_assert_word(self.get_main_word(), "Ara")
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url != self.url)
        print("Authorization successful, current URL:", self.driver.current_url)