from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_INPUT_LOGIN = (By.XPATH, """//span[text() = 'Username']/following::input[@type= 'text'][1]""")
    LOCATOR_INPUT_PASSWORD = (By.XPATH, """//span[text() = 'Password']/following::input[@type= 'password'][1]""")
    LOCATOR_BUTTON = (By.XPATH, """//button[@type= 'submit']""")
    LOCATOR_ERROR = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_BLOG = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE = (By.XPATH, """//button[@id="create-btn"]""")
    LOCATOR_TITLE_CREATE = (By.XPATH, """//span[text() = 'Title']/following::input[@type= 'text'][1]""")
    LOCATOR_DESCRIPTION_CREATE = (By.XPATH, """//span[text() = 'Description']//following::textarea[1]""")
    LOCATOR_CONTENT_CREATE = (By.XPATH, """//span[text() = 'Content']//following::textarea[1]""")
    LOCATOR_TITLE_PUBLIC = (By.XPATH, """//h1[@class ='svelte-tv8alb']""")
    LOCATOR_CONTENT_PUBLIC = (By.XPATH, """//div[@class = 'content svelte-tv8alb']""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_LOGIN[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_LOGIN)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_PASSWORD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_PASSWORD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_BUTTON).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR[1]}")
        return text

    def get_blog(self):
        blog = self.find_element(TestSearchLocators.LOCATOR_BLOG)
        text = blog.text
        logging.info(f"Нашли текст *{text}* локатор Блог  ")
        return text





