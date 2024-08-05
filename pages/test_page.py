from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep


class TestPage(BasePage):

    PAGE_URL = Links.TEST_PAGE_URL

# page locators

    FIRST_NAME_FIELD_LOCATOR = ("id", "firstName")  # через id
    LAST_NAME_FIELD_LOCATOR = ("css selector", "input#lastName")  # selector
    EMAIL_FIELD_LOCATOR = ("xpath", "//input[@id='userEmail']")
    GENDER_MALE_RADIO = ("xpath", "//input[@id='gender-radio-1']")
    GENDER_MALE_LABEL_LOCATOR = ("xpath", "//label[@for='gender-radio-1']")
    MOBILE_FIELD = ("xpath", "//input[@id='userNumber']")
    DATEofBIRTH_FIELD_LOCATOR = ("xpath", "//input[@id='dateOfBirthInput']")
    YEAR_LOCATOR = ("xpath", "//select[contains(@class, 'year')]")
    MONTH_LOCATOR = ("xpath", "//select[contains(@class, 'month')]")
    SUBJECTS_FIELD_LOCATOR = ("xpath", "//div[@id='subjectsContainer']")
    HOBBIES_CHECK_SPORTS = ("xpat", "//input[@id='hobbies-checkbox-1']")
    HOBBIES_LABEL_LOCATOR = ("xpath", "//label[@for='hobbies-checkbox-1']")
    UPLOAD_PICKTURE_BUTTON = ("xpath", "//input[@id='uploadPicture']")
    ADDRESS_FIELD_LOCATOR = ("xpath", "//textarea[@id='currentAddress']")
    DROP_STATE_LOCATOR = ("xpath", "//div[@id='state']")
    DROP_CITY_LOCATOR = ("xpath", "//div[@id='city']")
    SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[@id='submit']")

    CLOSE_BUTTON_LOCATOR = ("xpath", "//button[@id='closeLargeModal']")
    TEXT_LOCATOR = ("xpath", "//div[@id='example-modal-sizes-title-lg']")
    SUBJECTS_ELEMENT_LOCATOR = ("xpath", "//div[contains(@id, 'react-select-2') and contains(text(), 'Computer')]")

# actions
# скрипт эмулятор стрелки вниз 1 нажатие
    def move_down(self):
        self.driver.find_element("xpath", "//body").send_keys(Keys.ARROW_DOWN)

# ввод имени
    def enter_first_name(self, first_name: str):
        self.wait.until(
            EC.element_to_be_clickable((self.FIRST_NAME_FIELD_LOCATOR))
            ).send_keys(first_name)

# ввод фамилии
    def enter_last_name(self, last_name: str):
        self.wait.until(
            EC.element_to_be_clickable((self.LAST_NAME_FIELD_LOCATOR))
        ).send_keys(last_name)

# вводим email
    def enter_email(self, email):
        self.wait.until(
            EC.element_to_be_clickable((self.EMAIL_FIELD_LOCATOR))
        ).send_keys(email)

# выбираем пол
    def choose_a_gender_Male(self):
        self.wait.until(
            EC.element_to_be_clickable((self.GENDER_MALE_LABEL_LOCATOR))
        ).click()
        assert self.driver.find_element(
            *self.GENDER_MALE_RADIO
        ).is_selected() is True, "кнопка не выбрана"

# телефонный номер
    def enter_mobile_number(self, number: int):
        self.wait.until(
            EC.element_to_be_clickable((self.MOBILE_FIELD))
        ).send_keys(number)

# выбор даты рождения
# через select
    def enter_date_of_birth(self):
        date_picker = self.driver.find_element(
            "xpath", "//input[@id='dateOfBirthInput']"
            )
        date_picker.click()
        sleep(2)
        select_month = Select(
            self.driver.find_element(
                "xpath", "//select[@class='react-datepicker__month-select']"
                )
            )
        select_month.select_by_value("5")
        sleep(2)
        select_year = Select(
            self.driver.find_element(
                "xpath", "//select[@class='react-datepicker__year-select']"
                )
        )
        select_year.select_by_value("1985")
        sleep(2)
        self.driver.find_element(
            "xpath", "//div[contains(@class, 'datepicker__day')][text()='5'][1]"
            ).click()

# поле subjects через actions
    def enter_subjects(self):
        self.wait.until(
            EC.element_to_be_clickable((self.SUBJECTS_FIELD_LOCATOR))
        ).click()
        sleep(2)
        subjects = self.driver.find_element(*self.SUBJECTS_FIELD_LOCATOR)
        actions = ActionChains(self.driver)
        actions.move_to_element(subjects).send_keys("Computer").perform()
        sleep(2)
        self.wait.until(
            EC.element_to_be_clickable((self.SUBJECTS_ELEMENT_LOCATOR))
            ).click()
        # self.driver.find_element(
        #     "xpath", "//div[contains(text(), 'Computer')]"
        #     ).click()

# выбор чекбокса спорт
    def choose_checkbox_sport(self):
        self.wait.until(
            EC.element_to_be_clickable((self.HOBBIES_LABEL_LOCATOR))
        ).click()

# загрузка фото
    def download_picture(self):
        self.wait.until(
            EC.element_to_be_clickable((self.UPLOAD_PICKTURE_BUTTON))
        ).send_keys(f'{os.getcwd()}\\tests\\images.png')

# ввод в поле адрес
    def enter_current_address(self, address: str):
        self.wait.until(
            EC.element_to_be_clickable((self.ADDRESS_FIELD_LOCATOR))
        ).send_keys(address)

# выбор штата
    def select_state(self, state):
        self.wait.until(
            EC.element_to_be_clickable((self.DROP_STATE_LOCATOR))
        ).click()
        elements = self.driver.find_elements(
            "xpath", "//div[contains(@id, 'react-select-3')]"
            )
        for element in elements:
            if state in element.text:
                return element.click()

# выбор города
    def select_city(self, city):
        self.wait.until(
            EC.element_to_be_clickable((self.DROP_CITY_LOCATOR))
        ).click()
        elements = self.driver.find_elements(
            "xpath", "//div[contains(@id, 'react-select-4')]"
            )
        for element in elements:
            if city in element.text:
                return element.click()

# нажатие кнопки
    def click_submit_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.SUBMIT_BUTTON_LOCATOR))
        ).click()

# проверить заголовок
    def check_form(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (self.TEXT_LOCATOR), 'Thanks for submitting the form')
        )
        assert self.driver.find_element(
            *self.TEXT_LOCATOR
            ).text == 'Thanks for submitting the form'

    def assert_field(self):
        table = self.driver.find_element("xpath", "//table")
        print(table.text)

# закрыть всплывающее окно
    def click_close_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable((self.CLOSE_BUTTON_LOCATOR))
        )
        ActionChains(self.driver).scroll_to_element(
            *self.CLOSE_BUTTON_LOCATOR
            )  \
            .click(button)  \
            .perfome()
