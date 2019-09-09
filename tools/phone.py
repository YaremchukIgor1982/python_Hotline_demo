import fastnumbers


class Phone:
    def __init__(self,app):
        self.app = app

    def get_all_items(self):
        return self.app.driver.find_elements_by_css_selector(".tile-viewbox .product-item")

    def product_info(self,device):
        model = device.find_element_by_css_selector(".item-info p a")
        price = device.find_element_by_css_selector('.item-price.stick-bottom span.value').text
        converted = fastnumbers.fast_real(price)
        phone = ({"name": model.text, "costa": converted, "link": model.get_attribute('href')})
        return phone
    def get_Resume_info(self):
        resume_price = self.app.driver.find_element_by_css_selector('.resume-item.resume-checkout .price-format span.value').text
        resume_name = self.app.driver.find_element_by_css_selector('h1').text
        resume_phone = {'name': resume_name, 'cost': fastnumbers.fast_real(resume_price)}

    def button_Buy_click(self):
        if self.app.driver.find_element_by_css_selector('.btn-blue.m_b-sm').is_enabled() == True:
            self.app.driver.find_element_by_css_selector('.btn-blue.m_b-sm').click()
        else:
            self.app.driver.refresh()