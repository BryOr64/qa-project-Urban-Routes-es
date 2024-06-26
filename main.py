from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import helps

class UrbanRoutesPage:

    #selectores punto 1 del proryecto configurar la direccion from and to
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #selectores punto 2 del proyecto seleccion de la tarifa confort
    comfort_mode_flash = (By.XPATH, '//div[text()="Flash"]')
    comfort_take_taxi = (By.XPATH, '//button[text()="Pedir un taxi"]')
    comfort_select = (By.CSS_SELECTOR, 'img[alt = "Comfort"]')
    comfort_mane = (By.XPATH, './/div[@class="tcard active"]//div[text()="Comfort"]')

    #Selectores punto 3 del proyecto rellenar el numero telefonico
    phone_number_field = (By.CLASS_NAME, 'np-button')
    phone_number = (By.ID, 'phone')
    phone_number_bt_next = (By.XPATH,'//div[@class = "section active"]//form/div[@class = "buttons"]'
                                     '//button[@class = "button full"]')
    phone_number_code = (By.ID,'code')
    phone_number_code_confirm = (By.XPATH,'//div[@class = "section active"]//form/div[@class = "buttons"]'
                                          '//button[@type="submit"]')
    phone_number_check = (By.XPATH, '//div[@class = "np-text"]')

    #selectores punto 4 del proyecto agregar una targeta de credito
    pay_method = (By.CSS_SELECTOR, 'img[alt = "cash"]')
    pay_add_target = (By.XPATH, '//div[@class = "section active"]//div[@class ="pp-row disabled"]')
    pay_number_target = (By.XPATH, '//div[@class = "section active unusual"]//input[@id ="number"]')
    pay_code_target = (By.XPATH, '//div[@class = "section active unusual"]//input[@id ="code"]')
    pay_aux_click = (By.CLASS_NAME, 'card-wrapper')
    pay_button_add_target = (By.XPATH, './/div[@class="section active unusual"]//button[text()="Agregar"]')
    pay_select_target = (By.ID, 'card-1')
    pay_button_close = (By.XPATH, './/div[@class="payment-picker open"]//div[@class="section active"]'
                                  '//button[@class="close-button section-close"]')
    pay_verify_text_target = (By.CLASS_NAME, 'pp-value-text')

    #selectores punto 5 del proyecto escribir un SMS al conductor
    message_driver = (By.ID, 'comment')

    #selectores punto 6 del proyecto pedir manta y pañuelos
    blanket_scarves = (By.CSS_SELECTOR, '.reqs-body .r-type-switch:nth-of-type(1) .slider')


    #selectores punto 7 del proyecto pedir 2 helados
    icecream_add = (By.XPATH, ".//div[@class='r r-type-group']//div[@class='counter-plus']")
    icecream_value = (By.CSS_SELECTOR, '.r-group-items .r-type-counter:nth-of-type(1) .counter-value')

    #selectores punto 8 del proyecto aparece un modal para pedir un taxi
    order_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    order_taxi_verify = (By.CLASS_NAME, 'order-header-title')

    #selectores punto 9 del proyecto trabajo con el modal de pedir un taxi
    order_header_title = (By.XPATH, '//div[contains(text(),"El conductor llegará en")]')
    
    def __init__(self, driver):
        self.driver = driver

    #metodos para la prueba 1 configurar la direccion from and to
    def set_from(self, pepito):
        helps.wait(self.from_field, self.driver)
        self.driver.find_element(*self.from_field).send_keys(pepito)

    def set_to(self, to_address):
        helps.wait(self.to_field, self.driver)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    #metodos para la prueba 2 seleccion de la tarifa confort
    def click_flash_taxi(self):
        helps.wait(self.comfort_take_taxi, self.driver)
        self.driver.find_element(*self.comfort_mode_flash).is_enabled()
        self.driver.find_element(*self.comfort_take_taxi).click()

    def click_select_comfort(self):
        helps.wait(self.comfort_select, self.driver)
        self.driver.find_element(*self.comfort_select).click()

    def get_name_comfort(self):
        helps.wait(self.comfort_mane, self.driver)
        return self.driver.find_element(*self.comfort_mane).text

    def select_comfort_plan(self):
        self.click_flash_taxi()
        self.click_select_comfort()

    #metodos para la prueba 3 rellenar el numero telefonico
    def click_number_field(self):
        helps.wait(self.phone_number_field, self.driver)
        self.driver.find_element(*self.phone_number_field).click()

    def set_phone_number(self, number_phone):
        helps.wait(self.phone_number, self.driver)
        self.driver.find_element(*self.phone_number).send_keys(number_phone)

    def next_phone_number(self):
        helps.wait(self.phone_number_bt_next, self.driver)
        self.driver.find_element(*self.phone_number_bt_next).click()

    def set_code_phone_number(self):
        helps.wait(self.phone_number_code, self.driver)
        code_phone = helps.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_number_code).send_keys(code_phone)

    def confirm_code_phone_number(self):
        helps.wait(self.phone_number_code_confirm, self.driver)
        self.driver.find_element(*self.phone_number_code_confirm).click()

    def get_phone_number(self):
        helps.wait(self.phone_number_check, self.driver)
        return self.driver.find_element(*self.phone_number_check).text

    def phone_number_client(self, number_phone):
        self.click_number_field()
        self.set_phone_number(number_phone)
        self.next_phone_number()
        self.set_code_phone_number()
        self.confirm_code_phone_number()

    #metodos para la prueba 4 agregar una targeta de credito
    def clik_target_field(self):
        helps.wait(self.pay_method, self.driver)
        self.driver.find_element(*self.pay_method).click()

    def add_target(self):
        helps.wait(self.pay_add_target, self.driver)
        self.driver.find_element(*self.pay_add_target).click()

    def set_pay_number(self, pay_number):
        helps.wait(self.pay_number_target, self.driver)
        self.driver.find_element(*self.pay_number_target).click()
        self.driver.find_element(*self.pay_number_target).send_keys(pay_number)

    def set_pay_code(self, pay_code):
        helps.wait(self.pay_code_target, self.driver)
        self.driver.find_element(*self.pay_code_target).send_keys(pay_code)

    def click_aux(self):
        helps.wait(self.pay_aux_click, self.driver)
        self.driver.find_element(*self.pay_aux_click).click()

    def add_target_button(self):
        helps.wait(self.pay_button_add_target, self.driver)
        self.driver.find_element(*self.pay_button_add_target).click()

    def select_target(self):
        return self.driver.find_element(*self.pay_select_target).is_selected()

    def close_modal_target(self):
        helps.wait(self.pay_button_close, self.driver)
        self.driver.find_element(*self.pay_button_close).click()

    def get_name_target(self):
        return self.driver.find_element(*self.pay_verify_text_target).text

    def target_new(self, number, code):
        self.clik_target_field()
        self.add_target()
        self.set_pay_number(number)
        self.set_pay_code(code)
        self.click_aux()
        self.add_target_button()
        self.select_target()
        self.close_modal_target()

    #metodos para la prueba 5 escribir un SMS al conductor
    def set_message(self, message):
        helps.wait(self.message_driver, self.driver)
        self.driver.find_element(*self.message_driver).send_keys(message)

    def get_message(self):
        return self.driver.find_element(*self.message_driver).get_property('value')

    #metodos para la prueba 6 pedir manta y pañuelos
    def click_blanket_scarves(self):
        helps.wait(self.blanket_scarves, self.driver)
        self.driver.find_element(*self.blanket_scarves).click()

    def select_blanket_scarves(self):
        return self.driver.find_element(*self.blanket_scarves).is_enabled()

    #metodos para la prueba 7 pedir 2 helados
    def click_add_icecream(self):
        helps.wait(self.icecream_add, self.driver)
        self.driver.find_element(*self.icecream_add).click()

    def get_icecream_num(self):
        helps.wait(self.icecream_value, self.driver)
        return self.driver.find_element(*self.icecream_value).text

    def icecream_client(self):
        self.click_add_icecream()
        self.click_add_icecream()

    #metodos para la prueba 8 aparece un modal para pedir un taxi
    def click_take_taxi(self):
        helps.wait(self.order_taxi_button, self.driver)
        self.driver.find_element(*self.order_taxi_button).click()

    def get_take_taxi_verify(self):
        helps.wait(self.order_taxi_verify, self.driver)
        return self.driver.find_element(*self.order_taxi_verify).text

    #metodos para la prueba 9 trabajo con el modal de pedir un taxi
    def get_name_window_driver(self):
        WebDriverWait(self.driver, 45).until(expected_conditions.visibility_of_element_located(self.order_header_title))
        return self.driver.find_element(*self.order_header_title).text