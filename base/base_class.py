import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    #Method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url )


    # Method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(
            '/Users/katefilippova/PycharmProjects/final_exam/screen/' + name_screenshot)


    def assert_url_of_page(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL на странице соответствует ожидаемому")

    def assert_price(self, price1, price2):
        assert price1 == price2
        print("Цена на странице товара и в корзине совпадают")


