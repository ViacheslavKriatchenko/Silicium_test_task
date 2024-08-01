import pytest
from pages.test_page import TestPage


class BaseTest:

    test_page: TestPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.test_page = TestPage(driver)
