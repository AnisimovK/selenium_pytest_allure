import pytest
import allure
from allure_commons.types import AttachmentType

from Pages.MainPage import MainPage
from Tests.test_base import BaseTest


class TestMain(BaseTest):

    @allure.story('Проверить наличие поля поиска')
    @allure.severity('trivial')
    def test_search_field(self):
        self.MainPage = MainPage(self.driver)
        flag = self.MainPage.is_search_field_exists()
        assert flag, 'Поле поиска не найдено'

    @allure.story('Проверить, что появилась таблица с подсказками (suggest)')
    @allure.severity('trivial')
    def test_suggest_exists(self):
        self.MainPage = MainPage(self.driver)
        flag = self.MainPage.is_suggest_exists()
        assert flag, 'Suggest не появился'

    @allure.story('Проверить 1 ссылка ведет на сайт tensor.ru')
    @allure.severity('critical')
    def test_first_link(self):
        self.MainPage = MainPage(self.driver)
        result = self.MainPage.check_first_result()
        with allure.step('Do screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        assert "tensor.ru" in result, '1 ссылка не ведёт на tensor.ru'
