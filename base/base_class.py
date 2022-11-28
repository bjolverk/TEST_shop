import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    """METHOD GET CURRENT URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url is " + get_url)

    """METHOD ASSERT WORD"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good walue word")

    """METHOD SCREENSHOT"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot {now_date}.png'
        self.driver.save_screenshot(r'..\TEST_shop\screen\\' + name_screenshot)

    """METHOD ASSERT URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good walue url")



