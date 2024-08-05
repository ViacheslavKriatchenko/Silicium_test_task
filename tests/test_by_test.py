import allure
import pytest
from base.base_test import BaseTest
from time import sleep
import random


class TestProfile(BaseTest):

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
        self.test_page.open()
        self.test_page.is_open()
        self.test_page.scroll_by(0, 200)  # скролл из-за рекламы
        # steps
        # step_1
        self.test_page.enter_first_name(first_name)
        sleep(2)  # для отладки
        # step_2
        self.test_page.enter_last_name(last_name)
        sleep(2)
        # step_3
        self.test_page.move_down()  # нажатие стрелки вниз
        self.test_page.enter_email(email)
        sleep(2)
        # step_4
        self.test_page.move_down()
        self.test_page.choose_a_gender_Male()
        sleep(2)
        # step_5
        self.test_page.move_down()
        self.test_page.enter_mobile_number(
            random.randint(1000000000, 9999999999)
            )
        sleep(2)
        # step_6
        self.test_page.move_down()
        self.test_page.enter_date_of_birth()
        sleep(2)
        # step_7
        self.test_page.enter_subjects()
        sleep(2)
        # чек-бокс
        self.test_page.move_down()
        self.test_page.choose_checkbox_sport()
        sleep(2)
        # step_8
        self.test_page.move_down()
        self.test_page.download_picture()
        sleep(2)
        # step_9
        self.test_page.move_down()
        self.test_page.enter_current_address(address)
        sleep(2)
        # step_10
        self.test_page.move_down()
        self.test_page.select_state(state)
        sleep(2)
        # step_11
        self.test_page.move_down()
        self.test_page.select_city(city)
        sleep(2)
        # step_12
        self.test_page.move_down()
        self.test_page.click_submit_button()
        sleep(2)
        # er_1
        self.test_page.check_form()
        self.test_page.move_down()
        sleep(5)
        # er_2
        self.test_page.assert_field()
