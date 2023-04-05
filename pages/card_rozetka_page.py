
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from utilities.logger import Logger


class Card_rozetka_page(Base):
    # на странице товара было принято решение не проверять название товара, потому что его название это гипер ссылка
    # которую мы и кликали при выборе товара, это одно и то же поле/значение, нет смысла их сравнивать
    # здесь считаем цену на странице карточки товара и нажмем купить
    # на попапе также выбирааем, что готовы купить

    price_rozetka_on_product_card_page_to_text = ""

    # Locators поиск локаторов

    price_rozetka = "//span[@class='price_value']"
    buy_button = '//div[@class="button_block"]'
    korzina_button_on_popup = '//a[@class="popup_item__button popup_item__button_cart"]'


    # Getters возвращают данные локаторы


    def get_price_rozetka(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_rozetka)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_korzina_button_on_popup(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.korzina_button_on_popup)))

    # Actions производимые действия (ввод слов, нажатие кнопок)


    def save_price_rozetka_on_product_card_page(self):
        price_rozetka_on_product_card_page = self.get_price_rozetka()
        global price_rozetka_on_product_card_page_to_text
        price_rozetka_on_product_card_page_to_text = price_rozetka_on_product_card_page.text
        print("Считали цену розетки")
        print(price_rozetka_on_product_card_page_to_text)
        return price_rozetka_on_product_card_page_to_text

    def click_buy_button_on_product_card_page(self):
        self.get_buy_button().click()
        print("Кнопка купить нажата")

    def click_get_korzina_button_on_popup(self):
        self.get_korzina_button_on_popup().click()
        print("Кнопка на попапе нажата")

    # Methods список производимых действий
    def select_rozetka_to_buy(self):
        with allure.step("Select rozetka to buy"):
            Logger.add_start_step(method="select_rozetka_to_buy")
            self.get_current_url()
            self.save_price_rozetka_on_product_card_page()
            self.click_buy_button_on_product_card_page()
            self.click_get_korzina_button_on_popup()
            Logger.add_end_step(url=self.driver.current_url, method="select_rozetka_to_buy")



