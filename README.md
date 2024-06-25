# QA PROJECT URBAN ROUTES es
***Bryan Orosco - QA-grupo10-Sprint 8vo  **TRIPLETEN*****

Este proyecto realiza una prueba de automatizacion de la pagina web **URBAN ROUTES**. 
Este proyecto es una aplicación web que proporciona servicios de transporte urbano. Permite a los usuarios 
planificar rutas, solicitar taxis y seleccionar diferentes tarifas de servicio.Tendremos que realizar una 
revision automatisada donde veremos en este test solamante la utomatizacion de la tarifa de taxis **COMFORT**
podremos revisar y conocer mas del lenguaje de Python, tambien realizaremos varias pruebas para la ejecucion 
automatizada.

## Instalación y Herramientas

Instrucciones detalladas para instalar el proyecto para tal efecto de instalacion se esta utilizando 
el Id **PYCHARM** para poder descargar pycharm puedes dirigiste [AQUI](https://www.jetbrains.com/pycharm/)

```python
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
## Estructura del Proyecto
 
 - data.py - contiene la información que se va a utilizar para las pruebas.
 - main.py - contiene las clases y los metodos
 - RoutesPage.py - contiene todos los localizadores.
 - TestUrbanRoutes.py - contiene todos los test que se realizaran.

## LISTA DE COMPROBACION 

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