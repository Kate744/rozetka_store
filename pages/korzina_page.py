
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from pages.card_rozetka_page import Card_rozetka_page
from utilities.logger import Logger


class Korzina_page(Base):
    # в корзине сравниваем цену товара, которая была на странице карточки товара и здесь
    # также нажимаем кнопку оформить заказ

    price_rozetka_in_korzina_to_text = ""

    # Locators поиск локаторов
    title_rozetka_in_korzina_element = '//a[href="/catalog/detail/blok_op_etyud_1_m_rozetka_s_zazeml_zashch_shtorki_2_kl_vykl_sosna_sche_bpa16_202d/"]'
    price_rozetka_in_korzina_element = "//div[@class='current_price']"
    button_complete_order = '//a[@class="checkout btn btn-default btn-lg"]'


    # Getters возвращают данные локаторы


    def get_title_rozetka_in_korzina(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.title_rozetka_in_korzina_element)))

    def get_price_rozetka_in_korzina(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_rozetka_in_korzina_element)))

    def get_button_complete_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_complete_order)))


    # Actions производимые действия (ввод слов, нажатие кнопок)


    def give_price_rozetka_in_korzina(self):
        price_rozetka_in_korzina = self.get_price_rozetka_in_korzina()
        global price_rozetka_in_korzina_to_text
        price_rozetka_in_korzina_to_text = price_rozetka_in_korzina.text[:-5]
        print("Считали цену розетки в корзине")
        print(price_rozetka_in_korzina_to_text)
        return price_rozetka_in_korzina_to_text


    def click_get_button_complete_order(self):
        self.get_button_complete_order().click()
        print("Кнопка Оформить заказ нажата")

    # Methods список производимых действий
    def rozetka_in_korzina(self):
        with allure.step("Rozetka_in_korzina"):
            Logger.add_start_step(method="rozetka_in_korzina")
            self.get_current_url()
            self.assert_url_of_page("https://saray.ru/personal/cart/")
            self.give_price_rozetka_in_korzina()
            self.assert_price(Card_rozetka_page.price_rozetka_on_product_card_page_to_text, self.price_rozetka_in_korzina_to_text)
            self.click_get_button_complete_order()
            Logger.add_end_step(url=self.driver.current_url, method="rozetka_in_korzina")



