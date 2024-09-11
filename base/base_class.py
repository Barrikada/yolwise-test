class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)
        return get_url

    """Method assert word"""
    def get_assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, f"Expected word '{result}', but got '{value_word}'"
        print("Good value word")

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Get value URL')