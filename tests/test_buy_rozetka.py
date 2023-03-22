import time
from selenium import webdriver

from pages.card_rozetka_page import Card_rozetka_page
from pages.confirm_order_page import Confirm_order_page
from pages.korzina_page import Korzina_page
from pages.login_page import Login_page
from pages.rozetki_page import Rozetki_page
from pages.tovary_electro_page import Tovary_electro_page


def test_buy_rozetka():
    driver = webdriver.Chrome(executable_path='/Users/katefilippova/PycharmProjects/resourse/chromedriver')
    driver.maximize_window()
    print("Started test")

    # main = Main_page(driver) # создаем экземпляр класса
    # main.select_product_category() # вызываем оттуда метод

    login = Login_page(driver)
    login.authorization()
    time.sleep(1)
    tep = Tovary_electro_page(driver)
    tep.select_product_category()
    rp = Rozetki_page(driver)
    rp.select_filters_for_rozetki()
    crp = Card_rozetka_page(driver)
    crp.select_rozetka_to_buy()
    kp = Korzina_page(driver)
    kp.rozetka_in_korzina()
    cop = Confirm_order_page(driver)
    cop.confirm_the_order()

    print("Finished test")


    time.sleep(1)
    driver.quit()

