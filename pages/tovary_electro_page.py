import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait

from utilities.logger import Logger


class Tovary_electro_page(Base):
    # На этой странице пользователь, уже будучи авторизированным, кликает на меню, чтобы попасть в нужный раздел, а именно Электротовары
    # далее переходит на страницу с категориями Электротоваров, и выбирает Розетки (потому что там больше всего товаров)
    # интересно, что расположение категорий товаров постоянно меняется (новая загрузка страницы - новое расположение)
    # поэтому ушло много времени на поиск таких локаторов, которые останутся неизменны
    # также сделан скролл, чтобы все категории были видны, потому что из-за изменения порядка карточек, нужная категория иногда была вне зоны видимости боаузера


    # Locators
    header_tovary = "//li[@id='catalog_menu_strio']"
    menu_item_electro = "/html/body/header/div/div[2]/nav/ul/li[1]/div/table/tbody/tr/td[1]/ul/li[5]"
    sub_menu_item_rozetki = "Розетки"

    # Getters возвращают данные локаторы

    def get_header_tovary(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.header_tovary)))

    def get_menu_item_electro(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_item_electro)))

    def get_sub_menu_item_rozetki(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.sub_menu_item_rozetki)))

    # Actions

    def click_header_tovary(self):
        self.get_header_tovary().click()
        print("header_tovary кликнута")

    def click_get_menu_item_electro(self):
        self.get_menu_item_electro().click()
        print("Категория electro выбрана")

    def scroll_to_show_all_items(self):
        self.driver.execute_script("window.scrollTo(0, 250)")
        print("Проскролено")

    def click_get_sub_menu_item_rozetki(self):
        self.get_sub_menu_item_rozetki().click()
        print("sub_menu_item_rozetki кликнута")


# Methods
    def select_product_category(self):
        with allure.step("Select_product_category"):
            Logger.add_start_step(method="select_product_category")
            self.get_current_url()
            self.click_header_tovary()
            self.click_get_menu_item_electro()
            self.scroll_to_show_all_items()
            self.click_get_sub_menu_item_rozetki()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_category")


