# QA PROJECT URBAN ROUTES es

Este proyecto realiza una prueba de automatizacion de la pagina web **URBAN ROUTES**. 
Este proyecto es una aplicación web que proporciona servicios de transporte urbano. Permite a los usuarios 
planificar rutas, solicitar taxis y seleccionar diferentes tarifas de servicio.

Tendremos que realizar una revision automatisada donde veremos testearemos solamante la utomatizacion de la 
tarifa de taxis **COMFORT** para ver el funcionamiento. 

podremos revisar y conocer mas del lenguaje de Python, tambien realizaremos varias pruebas para la ejecucion 
automatizada.

## Herramientas

las Herramientas que utilizaremos en este proyecto seran Python, selenium y pytest todo esto configurado en 
el ID de pycharm.

## Instalación de herramientas

Instrucciones detalladas para descargar el proyecto e instalar alguanos complementos que 
necesitaremos en el proyecto son:

```python
# El ID que se esta utilizando
    PYCHARM descargalo en https://www.jetbrains.com/pycharm/

# Clonar el repositorio
    git clone https://github.com/usuario/qa-project-Urban-Routes-es.git

# Entrar al directorio del proyecto
    cd ./qa-project-Urban-Routes-es

# Instalar selenium mediante la consola
    pip install selenium
    o
    pip3 install selenium

# Instalar Pytest mediante la consola
    pip install pytest
    o
    pip3 install pytest
```
# Estructura del Proyecto
 
 - **data.py** - contiene la información que se va a utilizar para las pruebas.
 - **main.py** - contiene los localizadores, clases y los metodos que se utilizaran.
 - **TestUrbanRoutes.py** - contiene todos los test que se realizaran.
 - **helps** - se encuentran 2 metodos 
   -  **retrieve_phone_code:** que nos ayuda con la recuperacion 
   del codigo para introducir el numero telefonico.
   - **wait:** este metodo nos ayuda a colocar los tiempos de 
   espera en el codigo

# Ejecución del Proyecto
   1. Como primer paso tenemos que ver que este **ChromeDriver** instalado 
     y que esten condfigurado en tu PATH
   2. Ejecutar el archivo TestUrbanRoutes.py

# Conclusiones
En este proyecto pudimos ver las maneras que podemos llamar a un Xpath asi tambien pudimos
ver que todas las pruebas pasaron correctamente sin reportar ningun error eso nos lleva a 
la conclucion de que la tarifa de taxi **COMFORT** esta funcionando correctamente.

# Lista de Comprobación

| **PRUEBAS**                                                          | **ESTADO**   |
|----------------------------------------------------------------------|--------------|
| *1. Configurar la dirección*                                         | ***PASSED*** |
| *2. Seleccionar la tarifa comfort*                                   | ***PASSED*** |
| *3. Rellenar el número de teléfono*                                  | ***PASSED*** |
| *4. Agregar una tarjeta de crédito*                                  | ***PASSED*** |
| *5. Escribir un mensaje para el conductor*                           | ***PASSED*** |
| *6. Pedir una manta y pañuelos*                                      | ***PASSED*** |
| *7. Pedir 2 helados*                                                 | ***PASSED*** |
| *8. Aparecer el modal para buscar un taxi*                           | ***PASSED*** |
| *9. Esperar a que aparezca la información del conductor en el modal* | ***PASSED*** |
