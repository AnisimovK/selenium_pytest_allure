from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """By locators"""
    LOCATOR_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_POPUP_SUGGEST = (By.CSS_SELECTOR, 'ul.mini-suggest__popup-content')
    LOCATOR_FIRST_LINK = (By.XPATH, "//*[@id='search-result']/li[1]")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""
    def is_search_field_exists(self):
        return self.is_visible(self.LOCATOR_SEARCH_FIELD)

    def is_suggest_exists(self):
        self.do_send_keys(self.LOCATOR_SEARCH_FIELD, TestData.SEARCH_NAME)
        return self.is_visible(self.LOCATOR_POPUP_SUGGEST)

    def check_first_result(self):
        self.do_send_keys(self.LOCATOR_SEARCH_FIELD, TestData.SEARCH_NAME)
        self.do_enter(self.LOCATOR_SEARCH_FIELD)
        res = self.get_element_text(self.LOCATOR_FIRST_LINK)
        return res

