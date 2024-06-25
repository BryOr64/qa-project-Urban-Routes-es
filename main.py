from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from RoutesPage import RoutesPages


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def retrieve_phone_code(self, driver) -> str:
        """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
        Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
        El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

        import json
        import time
        from selenium.common import WebDriverException
        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = driver.execute_cdp_cmd('Network.getResponseBody',
                                                  {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(1)
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
            return code

    def wait(self, element_visibility):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(element_visibility))

    #metodos para la prueba 1 configurar la direccion from and to
    def set_from(self, pepito):
        self.wait(RoutesPages.from_field)
        self.driver.find_element(*RoutesPages.from_field).send_keys(pepito)

    def set_to(self, to_address):
        self.wait(RoutesPages.to_field)
        self.driver.find_element(*RoutesPages.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*RoutesPages.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*RoutesPages.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    #metodos para la prueba 2 seleccion de la tarifa confort
    def click_flash_taxi(self):
        self.wait(RoutesPages.comfort_take_taxi)
        self.driver.find_element(*RoutesPages.comfort_mode_flash).is_enabled()
        self.driver.find_element(*RoutesPages.comfort_take_taxi).click()

    def click_select_comfort(self):
        self.wait(RoutesPages.comfort_select)
        self.driver.find_element(*RoutesPages.comfort_select).click()

    def get_name_comfort(self):
        self.wait(RoutesPages.comfort_mane)
        return self.driver.find_element(*RoutesPages.comfort_mane).text

    def select_comfort(self):
        self.click_flash_taxi()
        self.click_select_comfort()

    #metodos para la prueba 3 rellenar el numero telefonico
    def click_number_field(self):
        self.wait(RoutesPages.phone_number_field)
        self.driver.find_element(*RoutesPages.phone_number_field).click()

    def set_phone_number(self, numbers):
        self.wait(RoutesPages.phone_number)
        self.driver.find_element(*RoutesPages.phone_number).send_keys(numbers)

    def next_phone_number(self):
        self.wait(RoutesPages.phone_number_bt_next)
        self.driver.find_element(*RoutesPages.phone_number_bt_next).click()

    def set_code_phone_number(self):
        self.wait(RoutesPages.phone_number_code)
        code = self.retrieve_phone_code(self.driver)
        self.driver.find_element(*RoutesPages.phone_number_code).send_keys(code)

    def confirm_code_phone_number(self):
        self.wait(RoutesPages.phone_number_code_confirm)
        self.driver.find_element(*RoutesPages.phone_number_code_confirm).click()

    def get_phone_number(self):
        self.wait(RoutesPages.phone_number_check)
        return self.driver.find_element(*RoutesPages.phone_number_check).text

    def phone_number(self, numbers):
        self.click_number_field()
        self.set_phone_number(numbers)
        self.next_phone_number()
        self.set_code_phone_number()
        self.confirm_code_phone_number()

    #metodos para la prueba 4 agregar una targeta de credito
    def clik_target_field(self):
        self.wait(RoutesPages.pay_method)
        self.driver.find_element(*RoutesPages.pay_method).click()
    def add_target(self):
        self.wait(RoutesPages.pay_add_target)
        self.driver.find_element(*RoutesPages.pay_add_target).click()

    def set_pay_number(self, pay_number):
        self.wait(RoutesPages.pay_number_target)
        self.driver.find_element(*RoutesPages.pay_number_target).click()
        self.driver.find_element(*RoutesPages.pay_number_target).send_keys(pay_number)

    def set_pay_code(self, pay_code):
        self.wait(RoutesPages.pay_code_target)
        self.driver.find_element(*RoutesPages.pay_code_target).send_keys(pay_code)

    def click_aux(self):
        self.wait(RoutesPages.pay_aux_click)
        self.driver.find_element(*RoutesPages.pay_aux_click).click()

    def add_target_button(self):
        self.wait(RoutesPages.pay_button_add_target)
        self.driver.find_element(*RoutesPages.pay_button_add_target).click()

    def select_target(self):
        return self.driver.find_element(*RoutesPages.pay_select_target).is_selected()

    def close_modal_target(self):
        self.wait(RoutesPages.pay_button_close)
        self.driver.find_element(*RoutesPages.pay_button_close).click()

    def get_name_target(self):
        return self.driver.find_element(*RoutesPages.pay_verify_text_target).text

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
        self.wait(RoutesPages.message_driver)
        self.driver.find_element(*RoutesPages.message_driver).send_keys(message)

    def get_message(self):
        return self.driver.find_element(*RoutesPages.message_driver).get_property('value')

    #metodos para la prueba 6 pedir manta y pañuelos

    def click_blanket_scarves(self):
        self.wait(RoutesPages.blanket_scarves)
        self.driver.find_element(*RoutesPages.blanket_scarves).click()

    def select_blanket_scarves(self):
        return self.driver.find_element(*RoutesPages.blanket_scarves).is_enabled()

    #metodos para la prueba 7 pedir 2 helados
    def click_add_icecream(self):
        self.wait(RoutesPages.icecream_add)
        self.driver.find_element(*RoutesPages.icecream_add).click()

    def get_icecream_num(self):
        self.wait(RoutesPages.icecream_value)
        return self.driver.find_element(*RoutesPages.icecream_value).text

    def icecream_add(self):
        self.click_add_icecream()
        self.click_add_icecream()

    #metodos para la prueba 8 aparece un modal para pedir un taxi
    def click_take_taxi(self):
        self.wait(RoutesPages.order_taxi_button)
        self.driver.find_element(*RoutesPages.order_taxi_button).click()

    def get_take_taxi_verify(self):
        self.wait(RoutesPages.order_taxi_verify)
        return self.driver.find_element(*RoutesPages.order_taxi_verify).text

    #metodos para la prueba 9 trabajo con el modal de pedir un taxi
    def get_name_window_driver(self):
        WebDriverWait(self.driver, 45).until(expected_conditions.visibility_of_element_located(RoutesPages.order_header_title))
        return self.driver.find_element(*RoutesPages.order_header_title).text