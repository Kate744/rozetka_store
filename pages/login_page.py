
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base

class Login_page(Base):
 # На этой странице пользователь вводит свои данные для авторизации

    url = "https://saray.ru"
    email = "legardioleviosa@tuta.io"
    password = "Legardioleviosa5"


    # Locators поиск локаторов
    sign_in_link = "//a[@href='/lk/']"
    email_field = "//input[@id='login_form']"
    password_field = "//input[@id='password_form']"
    button_sign_in = "//input[@type='submit']"
    privetstvie = "/html/body/main/article/div[2]/div[2]/div[1]/div[1]/div/h1"


    # Getters возвращают данные локаторы

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     # self.time = None

    def get_sign_in_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_link)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_button_sign_in(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_sign_in)))




    # Actions производимые действия (ввод слов, нажатие кнопок)

    def click_sign_in_link(self):
        self.get_sign_in_link().click()
        print("Sign In кликнута")

    def enter_email(self, email):
        self.get_email_field().send_keys(email)
        print("Email введен")

    def enter_password(self, password):
        self.get_password_field().send_keys(password)
        print("Password введен")

    def click_sign_in_button(self):
        self.get_button_sign_in().click()
        print("Кнопка Sign In кликнута")


    # Methods список производимых действий
    def authorization(self):
        self.driver.get(self.url)
        self.click_sign_in_link()
        self.get_current_url()
        self.enter_email(self.email)
        self.enter_password(self.password)
        self.click_sign_in_button()


