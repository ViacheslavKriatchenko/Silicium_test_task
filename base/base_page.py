# import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_open(self):
        self.wait.until(EC.url_to_be((self.PAGE_URL)))

    def scroll_by(self, x, y):  # Скролл по x и y
        self.driver.execute_script(f"window.scrollTo({x}, {y})")
