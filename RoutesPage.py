from selenium.webdriver.common.by import By

class RoutesPages:
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