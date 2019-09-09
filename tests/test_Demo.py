import fastnumbers as fastnumbers
import random
import time
from pprint import pprint

from assertpy import assert_that

from data.data import base, user


def test_login(app):
    app.driver.get(base)
    if app.user.account_icon().text == "Вход":
        app.user.account_icon().click()
    app.user.log_in(user['user'], user['passw'])
    app.user.submit().click()
    assert_that(app.user.account_icon().text).is_equal_to("Ihor_QA")


def test_change_account_settings(app):
    app.user.account_icon().click()
    app.user.go_to_personaldata()
    app.user.change_First_last()
    app.user.submit().click()


def test_catch_lenova_phones(app):
    app.user.search('Lenovo')
    app.user.go_to_Smarts_catalog()

    app.driver.get(app.driver.current_url + "?checkout=1")

    devices = app.phone.get_all_items()

    random_phone = random.choice(devices)
    product_info = app.phone.product_info(random_phone)
    product_info['name'].click()
    time.sleep(3)
    assert_that(app.driver.current_url).is_equal_to(product_info['link'])
    resume_info = app.phone.get_Resume_info()

    app.user.mini_cart().click()
    print("Cart item : ", app.user.mini_cart_Popup_Item_price())
    phone_in_checkout = app.user.checkout()

    assert_that(resume_info['cost']).is_equal_to(phone_in_checkout['cost'])
    if resume_info['cost'] == phone_in_checkout['cost']:
        print("Equal")


def test_iphone_sort_minimal_price(app):
    app.driver.get(base + "mobile/mobilnye-telefony-i-smartfony/?checkout=1&q=Iphone+X")
    devices = app.phone.get_all_items()
    del devices[0]
    all = []
    for device in devices:
        iphone=app.phone.product_info(device)
        all.append(iphone)
    seq = [iphone['costa'] for iphone in all]
    for iphone in all:
        if iphone['costa'] == min(seq):
            print("MINIMAL PRICE IS ", iphone)
