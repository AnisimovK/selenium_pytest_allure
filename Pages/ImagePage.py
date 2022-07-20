from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class ImagePage(BasePage):
    """ By locators """
    LOCATOR_IMAGE_HREF = (By.XPATH, "//a[@data-id='images']")
    LOCATOR_TEXT_FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-SearchText")
    LOCATOR_1 = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div/div/div[1]/a/div[1]")
    LOCATOR_CATEGORY_INPUT_FIELD = (By.XPATH, "//input[@name='text']")
    LOCATOR_FIRST_IMAGE = (By.XPATH, "//*[@role='listitem']/div/a")
    LOCATOR_FULL_IMAGE = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/div/div")
    LOCATOR_SRC = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img")
    LOCATOR_CLICK_FORWARD = (By.CLASS_NAME, "CircleButton_type_next")
    LOCATOR_CLICK_BACK = (By.CLASS_NAME, "CircleButton_type_prev")

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.original_window = self.driver.current_window_handle

    def is_image_href_exists(self):
        res = self.get_element(self.LOCATOR_IMAGE_HREF).get_attribute("href")
        return res

    def image_click(self):
        self.wait_download_page()
        self.do_click(self.LOCATOR_IMAGE_HREF)
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != self.original_window:
                self.driver.switch_to.window(window_handle)
                break
        self.wait()

    def image_closing_tabs(self):
        self.image_close()

    def open_first_category(self):
        if self.is_visible(self.LOCATOR_1):
            self.do_click(self.LOCATOR_1)

    def get_result_text(self):
        if self.is_visible(self.LOCATOR_TEXT_FIRST_CATEGORY):
            res_1 = self.get_element_text(self.LOCATOR_TEXT_FIRST_CATEGORY)
            return res_1

    def get_another_result_text(self):
        if self.is_visible(self.LOCATOR_CATEGORY_INPUT_FIELD):
            inp = self.get_element(self.LOCATOR_CATEGORY_INPUT_FIELD)
            res_2 = inp.get_attribute("value")
            return res_2

    def open_first_image(self):
        self.do_click(self.LOCATOR_FIRST_IMAGE)

    def is_full_image(self):
        return self.is_visible(self.LOCATOR_FULL_IMAGE)

    def click_forward(self):
        self.wait_download_page()
        self.do_click(self.LOCATOR_CLICK_FORWARD)

    def click_back(self):
        self.wait_download_page()
        self.do_click(self.LOCATOR_CLICK_BACK)

    def get_image_src(self):
        res = self.get_src(self.LOCATOR_SRC)
        return res
