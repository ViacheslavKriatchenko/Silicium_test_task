import allure
import pytest
from base.base_test import BaseTest
from time import sleep
import random


class TestProfile(BaseTest):

    @allure.title("Automation test demoqa")
    @allure.description("Test assignment for participation in the Silicium workshop")
    @allure.tag("demoqa", "smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://demoqa.com/automation-practice-form", name="Website")
    @allure.testcase("TC-1")
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        'first_name, last_name, email, address, state, city',
        [(
                'Ivan',
                'Ivanov',
                'ivanov@example.com',
                'planet Earth',
                'Rajasthan',
                'Jaipur',
        )
        ])
    def test_task_practice(self, first_name, last_name, email, address, state, city):
        # description
        with allure.step('Go to and check URL'):
            self.test_page.open()
            self.test_page.is_open()
            self.test_page.scroll_by(0, 200)  # скролл из-за рекламы
        # steps
        # step_1
        with allure.step(f'Enter {first_name} in the first_name field'):
            self.test_page.enter_first_name(first_name)
        # sleep(2)  # для отладки
        # step_2
        with allure.step(f'Enter {last_name} in the last_name field'):
            self.test_page.enter_last_name(last_name)
        # sleep(2)
        # step_3
        self.test_page.move_down()  # нажатие стрелки вниз
        with allure.step(f'Enter {email} in the email field'):
            self.test_page.enter_email(email)
        # sleep(2)
        # step_4
        self.test_page.move_down()
        with allure.step('Click Male radiobutton'):
            self.test_page.choose_a_gender_Male()
        # sleep(2)
        # step_5
        self.test_page.move_down()
        with allure.step('Enter random 10 numbers in the mobile field'):
            self.test_page.enter_mobile_number(
                random.randint(1000000000, 9999999999)
            )
        # sleep(2)
        # step_6
        self.test_page.move_down()
        with allure.step('Choose date of birth'):
            self.test_page.enter_date_of_birth()
        # sleep(2)
        # step_7
        self.test_page.scroll_by(0, 650)
        with allure.step('Choose subject about computer'):
            self.test_page.enter_subjects()
        # sleep(2)
        # чек-бокс
        with allure.step('Click checkbox Sport'):
            self.test_page.choose_checkbox_sport()
        # sleep(2)
        # step_8
        with allure.step('Download picture'):
            self.test_page.download_picture()
        # sleep(2)
        # step_9
        with allure.step(f'Enter {address} in the address field'):
            self.test_page.enter_current_address(address)
        # sleep(2)
        # step_10
        with allure.step(f'Select {state} state'):
            self.test_page.select_state(state)
        # sleep(2)
        # step_11
        with allure.step(f'Select {city} city'):
            self.test_page.select_city(city)
        # sleep(2)
        # step_12
        self.test_page.move_down()
        with allure.step('Click submit button'):
            self.test_page.click_submit_button()
        # sleep(2)
        # er_1
        with allure.step('A pop-up window appears with the title "Thanks for submitting the form"'):
            self.test_page.print_table_data()
            self.test_page.check_visability_table_form()
            assert 'Thanks for submitting the form' in self.driver.find_element(
                "xpath", "//div[@id='example-modal-sizes-title-lg']"
                ).text
        # er_2
        with allure.step('Check the previously entered values'):
            self.test_page.verify_full_name(first_name, last_name)
            self.test_page.verify_email(email)
            self.test_page.verify_gender()
            self.test_page.verify_Mobile()
            self.test_page.verify_Date_of_Birth()
            self.test_page.verify_subjects()
            self.test_page.verify_picture()
            self.test_page.verify_address(address)
            self.test_page.verify_state_and_city(state, city)
        with allure.step('Результат теста'):
            print('Test passed successfully')
