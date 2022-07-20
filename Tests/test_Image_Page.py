from Config.config import TestData
from Pages.ImagePage import ImagePage
from Tests.test_base import BaseTest
import allure


def check_not_none(item):
    if item is not None:
        return True
    else:
        assert False


class TestImage(BaseTest):
    @allure.story('Проверить, что ссылка «Картинки» присутствует на странице')
    @allure.severity('trivial')
    def test_image_link_exists(self):
        self.ImagePage = ImagePage(self.driver)
        assert TestData.IMAGE_HREF == self.ImagePage.is_image_href_exists(), 'Ссылка "картинки" не присутствует на ' \
                                                                             'странице '

    @allure.story('Проверить, что перешли на url https://yandex.ru/images/')
    @allure.severity('trivial')
    def test_right_image_link(self):
        self.ImagePage = ImagePage(self.driver)
        self.ImagePage.image_click()
        cur_url = self.driver.current_url
        self.ImagePage.image_closing_tabs()
        assert TestData.IMAGE_HREF == cur_url, 'Переход не на "https://yandex.ru/images/"'

    @allure.story('Проверить, что название категории отображается в поле поиска')
    @allure.severity('trivial')
    def test_first_category(self):
        self.ImagePage = ImagePage(self.driver)
        self.ImagePage.image_click()
        res_text_1 = self.ImagePage.get_result_text()
        self.ImagePage.open_first_category()
        res_text_2 = self.ImagePage.get_another_result_text()
        self.ImagePage.image_closing_tabs()
        assert res_text_1 == res_text_2, 'Название категории не отображается в поле поиска'

    @allure.story('Проверить, что картинка открылась')
    @allure.severity('trivial')
    def test_first_image(self):
        self.ImagePage = ImagePage(self.driver)
        self.ImagePage.image_click()
        self.ImagePage.open_first_category()
        self.ImagePage.open_first_image()
        flag = self.ImagePage.is_full_image()
        self.ImagePage.image_closing_tabs()
        assert flag, 'Картинка не открылась'

    @allure.story('Проверить, что картинка сменилась')
    @allure.severity('trivial')
    def test_step_forward(self):
        self.ImagePage = ImagePage(self.driver)
        self.ImagePage.image_click()
        self.ImagePage.open_first_category()
        self.ImagePage.open_first_image()
        res_1 = self.ImagePage.get_image_src()
        check_not_none(res_1)
        self.ImagePage.click_forward()
        res_2 = self.ImagePage.get_image_src()
        check_not_none(res_2)
        self.ImagePage.image_closing_tabs()
        assert hash(res_1) != hash(res_2), 'Картинка не сменилась'

    @allure.story('Проверить вернулись ли на предыдущую картинку')
    @allure.severity('trivial')
    def test_step_forward_back(self):
        self.ImagePage = ImagePage(self.driver)
        self.ImagePage.image_click()
        self.ImagePage.open_first_category()
        self.ImagePage.open_first_image()
        res_1 = self.ImagePage.get_image_src()
        check_not_none(res_1)
        self.ImagePage.click_forward()
        self.ImagePage.click_back()
        res_2 = self.ImagePage.get_image_src()
        check_not_none(res_2)
        self.ImagePage.image_closing_tabs()
        assert hash(res_1) == hash(res_2), 'Вернулись не на предыдущую картинку'


