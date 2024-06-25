import data
from selenium import webdriver
from main import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        '''
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
        '''

        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

    """1 Configurar la dirección (esta parte se ha escrito para ti como ejemplo)."""
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    """2 seleccionar la tarifa confort"""
    def test_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort()
        assert routes_page.get_name_comfort() == 'Comfort'

    """ 3 rellenar el numero telefonico"""
    def test_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        number = data.phone_number
        routes_page.phone_number(number)
        assert routes_page.get_phone_number() == number

    """ 4 agregar una targeta de credito"""
    def test_add_target(self):
        routes_page = UrbanRoutesPage(self.driver)
        number = data.card_number
        code = data.card_code
        routes_page.target_new(number, code)
        assert routes_page.select_target() == True
        assert routes_page.get_name_target() == 'Tarjeta'

    """ 5 escribir un SMS al conductor"""
    def test_sms(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.set_message(message)
        assert routes_page.get_message() == data.message_for_driver

    """ 6  pedir manta y pañuelos"""
    def test_blanket_scarves(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_scarves()
        assert routes_page.select_blanket_scarves() == True

    """ 7 pedir 2 helados"""
    def test_icecream_add(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.icecream_add()
        assert routes_page.get_icecream_num() == '2'

    """ 8 aparece un modal para pedir un taxi"""
    def test_take_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_take_taxi()
        assert routes_page.get_take_taxi_verify() == 'Buscar automóvil'

    """ 9 trabajo con el modal de pedir un taxi"""
    def test_wait_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        title = routes_page.get_name_window_driver()
        assert "El conductor" in title

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()