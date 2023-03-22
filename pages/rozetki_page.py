import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait

class Rozetki_page(Base):
    # на этой странице я выбираю фильтр по стране-производителю, и по виду товара
    # прощу учесть, что явное ожидание тут по причине того, что как только фильтры применены, система долго реагирует
    # на странице ничего не показывает, что загрузка идет, это можно увидеть только по вращаещемуся значку на вкладке браузера
    # вы увидите, что кол-во товаров сначала "...", потом "1538" , загрузка, и уже потом "21"
    # далее идет сортировка от большой цены к малой, потому что я могу поставить цену в базе данных миллион, и выбираться будет
    # всегда этот товар, тогда как самых дешевый позиций часто нет в наличии, и тест упадет только из-за этого (нет кнопки купить)
    # по этой же причине я выбираю первый продукт в каталоге (выбранный мной селектор подходит для всех продуктов,
    # но первый попавшийся, то есть мой самый дорогой, и будет использоваться)
    # конечно можно сделать привязку к названию товара, но я так и не смогла подобрать селектор, как не пыталась, там по сути ссылка и все
    # а по ссылке не находит
    # было много попыток, в итоге опытным путем вышло, что если нажать сортировку до окончания зарузки, то результаты будут совсем некорректные
    # поэтому было принято решение ждать это количество секунд, на котором не падает тест
    # также сделано, что модалы для фильтров и сортировки закрыты после сделанного выбора
    #

    # Locators
    link_more_filters = '//div[@data-action="show_more_filters"]'
    filter_strana = '//*[contains(text(), "Страна-изготовитель")]'
    checkbox_for_russia = '//span[@title="Россия"]'
    filter_vid = '//*[@id="main-second-column"]/div[2]/div/form/section[2]/div[4]/div[1]/div'
    checkbox_for_vid_combinirovanny = '//span[@title="Комбинированный"]'
    sort_button = '//*[contains(text(), "Сортировать")]'
    checkbox_sort_by_high_price = '//*[contains(text(), "от большей")]'
    item_rozetka_etud = '//div[@class ="catalog_product"]'



    # Getters возвращают данные локаторы

    def get_link_more_filters(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_more_filters)))

    def get_filter_strana(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_strana)))

    def get_checkbox_for_russia(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_for_russia)))

    def get_filter_vid(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_vid)))

    def get_checkbox_for_vid_combinirovanny(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_for_vid_combinirovanny)))

    def get_sort_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_button)))

    def get_checkbox_sort_by_high_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_sort_by_high_price)))

    def get_item_rozetka_etud(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.item_rozetka_etud)))


    # Actions

    def click_link_more_filters(self):
        self.get_link_more_filters().click()
        print("more_filters кликнута")

    def click_get_filter_strana(self):
        self.get_filter_strana().click()
        print("filter strana кликнута")

    def check_get_checkbox_for_russia(self):
        self.get_checkbox_for_russia().click()
        self.get_filter_strana().click()
        print("Россия чекбокс кликнут")

    def click_get_filter_vid(self):
        self.get_filter_vid().click()
        print("filter vid кликнут")

    def check_get_checkbox_for_vid_combinirovanny(self):
        self.get_checkbox_for_vid_combinirovanny().click()
        self.get_filter_vid().click()
        time.sleep(15)
        print("Combined чекбокс кликнут и данные загружены")

    def click_get_sort_button(self):
        self.get_sort_button().click()
        print("Сортировка кликнута")

    def click_checkbox_sort_by_high_price(self):
        self.get_checkbox_sort_by_high_price().click()
        print("Сортировка по высокой цене выбрана")
        time.sleep(3)
        print("Отсортировано")


    def click_get_item_rozetka_etud(self):
        self.get_item_rozetka_etud().click()
        print("Розетка выбрана")


# Methods
    def select_filters_for_rozetki(self):
        self.get_current_url()
        self.click_link_more_filters()
        self.click_get_filter_strana()
        self.check_get_checkbox_for_russia()
        self.click_get_filter_vid()
        self.check_get_checkbox_for_vid_combinirovanny()
        self.click_get_sort_button()
        self.click_checkbox_sort_by_high_price()
        self.click_get_item_rozetka_etud()



