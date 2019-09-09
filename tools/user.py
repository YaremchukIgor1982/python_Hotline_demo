import time

from selenium.webdriver.common.keys import Keys

from data.data import base


class User:

    def __init__(self, app):
        self.app = app

    def account_icon(self):
        return self.app.driver.find_element_by_css_selector('.item-login')

    def log_in(self, email, pwd):
        self.app.driver.find_element_by_css_selector("[name='login']").send_keys(email)
        self.app.driver.find_element_by_css_selector("[name='password']").send_keys(pwd)

    def button_submit(self):
        return self.app.driver.find_element_by_css_selector("input.btn-graphite")

    def change_First_last(self, name, last):

        self.app.driver.find_element_by_css_selector("[name='user_personal_data_form[firstName]']").clear()
        self.app.driver.find_element_by_css_selector("[name='user_personal_data_form[firstName]']").send_keys(name)

        self.app.driver.find_element_by_css_selector("[name='user_personal_data_form[lastName]']").clear()
        self.app.driver.find_element_by_css_selector("[name='user_personal_data_form[lastName]']").send_keys(last)

    def go_to_personaldata(self):
        self.app.driver.find_element_by_css_selector("a[href*='/personal/']").click()

    def search(self, item):
        search = self.app.driver.find_element_by_css_selector("#searchbox")
        search.send_keys(item)
        search.send_keys(Keys.ENTER)

    def go_to_Smarts_catalog(self):
        time.sleep(3)
        posts = self.app.driver.find_elements_by_css_selector(".active li a")
        posts[1].click()

    def sort_to_Buy(self):
        self.app.driver.get(base + "?checkout=1")

    def mini_cart(self):
        cart_icon = self.app.driver.find_element_by_css_selector('.item-cart')
        print("Count in menu cart :" + cart_icon.find_element_by_css_selector(".box-in span.count").text)
        return cart_icon

    def mini_cart_Popup(self):
        return self.app.driver.find_element_by_css_selector(".dropdown-bd.active")

    def mini_cart_Popup_Item_price(self):
        price = self.mini_cart_Popup().find_element_by_css_selector('.m_b-md .price-md span.value').text
        print("Phone in mini cart :" + self.app.driver.find_element_by_css_selector(
            ".viewbox-striped.border-t .cell-9.text").text)
        return price

    def checkout(self):
        checkout_price = self.app.driver.find_element_by_css_selector('.price-box span.value').text
        checkout_name = self.app.driver.find_element_by_css_selector('.info-box a').text
        return ({'name': checkout_name, 'cost': checkout_price})
