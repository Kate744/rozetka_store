
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from pages.card_rozetka_page import Card_rozetka_page
from utilities.logger import Logger


class Confirm_order_page(Base):
    # здесь мы вводим телефон, и НЕ нажимаем кнопку оформить заказ
    # потому что после этого заказ действительно идет в работу
    # делаем скриншот и тест окончен


    url_of_confirm_order_page = "https://saray.ru/personal/order/make/"
    # Locators поиск локаторов

    field_phone_number = '//input[@id="ORDER_PROP_3"]'
    button_submit_order = '//div[@class="checkout"]'


    # Getters возвращают данные локаторы


    def get_field_phone_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.field_phone_number)))

    def get_button_submit_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.field_phone_number)))


    # Actions производимые действия (ввод слов, нажатие кнопок)

    def enter_get_field_phone_number(self):
        self.get_field_phone_number().send_keys("88083567899")
        print("Телефон введен")



    # Methods список производимых действий
    def confirm_the_order(self):
        Logger.add_start_step(method="confirm_the_order")
        self.get_current_url()
        self.assert_url_of_page(self.url_of_confirm_order_page)
        self.enter_get_field_phone_number()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="confirm_the_order")






