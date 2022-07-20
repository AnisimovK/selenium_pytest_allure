from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from Config.config import TestData
from loguru import logger

logger.add("debug.json", format="{time} {level} {message}",
           level="DEBUG", rotation="1 week", compression="zip", serialize=True)

"""This class is the parent of all pages"""
"""it contains all the main methods and utilities for all the pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.original_window = self.driver.current_window_handle

    def wait_one_tab(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(1))
        except exceptions.TimeoutException:
            self.image_close()
            return False

    def image_close(self):
        logger.info("image_close")
        for i in self.driver.window_handles:
            if len(self.driver.window_handles) > 1:
                if self.driver.current_window_handle != self.original_window:
                    self.driver.close()
        self.wait_one_tab()
        self.driver.switch_to.window(self.original_window)

    def do_click(self, by_locator):
        logger.info("do_click")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except exceptions.TimeoutException:
            self.image_close()
            return False

    def do_enter(self, by_locator):
        logger.info("do_enter")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)
        except exceptions.TimeoutException:
            self.image_close()
            return False

    def do_send_keys(self, by_locator, text):
        logger.info("do_send_keys")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except exceptions.TimeoutException:
            self.image_close()
            return False

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except exceptions.TimeoutException:
            self.image_close()
            return False

    def get_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element
        except exceptions.TimeoutException:
            self.image_close()
            return False

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except exceptions.TimeoutException:
            self.image_close()
            return False

    def wait(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(TestData.IMAGE_TITLE))
        except exceptions.TimeoutException:
            self.image_close()
            return False

    def wait_download_page(self):
        WebDriverWait(self.driver, 3)

    def get_src(self, by_locator):
        try:
            inp = self.driver.find_element(by_locator[0], by_locator[1])
            text = inp.get_attribute("src")
            return text
        except exceptions.TimeoutException:
            self.image_close()
            return False




