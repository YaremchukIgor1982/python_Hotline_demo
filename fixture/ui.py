import inspect

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui
from webdriver_manager.chrome import ChromeDriverManager

from tools.cart import Cart
from tools.phone import Phone
from tools.user import User


class Ui :
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")

    def __init__(self, chrome_options=chrome_options):


        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.wait = ui.WebDriverWait(self.driver,2000, poll_frequency=1)
        self.user = User(self)
        self.phone = Phone(self)
        self.cart = Cart(self)

    def scroll(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def func_name(self):
        return (inspect.stack()[1][3])

    def destroy(self):
        self.driver.close()


class Headless(Ui):
    options = Options()
    options.add_argument("--headless")

    def __init__(self):
        super(Headless, self).__init__(chrome_options=self.options)