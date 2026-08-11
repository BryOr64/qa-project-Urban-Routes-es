# 🚕 Urban Routes — QA Automation

Proyecto de automatización de pruebas End-to-End para la aplicación web Urban Routes.

El objetivo del proyecto es validar el flujo completo de solicitud de un viaje en la tarifa Comfort mediante pruebas automatizadas desarrolladas con Python, Selenium WebDriver y Pytest.

## 🎯 Objetivo

Automatizar los principales escenarios del proceso de solicitud de un taxi y verificar que las funcionalidades involucradas respondan correctamente.

## 🧪 Escenarios automatizados

La suite valida los siguientes escenarios:

1. Configuración de las direcciones de origen y destino.
2. Selección de la tarifa Comfort.
3. Registro del número telefónico.
4. Registro de una tarjeta como método de pago.
5. Envío de un mensaje al conductor.
6. Solicitud de manta y pañuelos.
7. Solicitud de dos helados.
8. Validación del modal de búsqueda del taxi.
9. Validación de la información del conductor.

## 🛠️ Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Git
- GitHub
- PyCharm

## 📂 Estructura del proyecto

- `data.py` — Datos utilizados durante las pruebas.
- `main.py` — Localizadores y métodos utilizados para interactuar con la aplicación.
- `TestUrbanRoutes.py` — Casos de prueba automatizados.
- `helps.py` — Funciones auxiliares y utilidades necesarias durante la ejecución.

## ▶️ Ejecución

### 1. Clonar el repositorio

git clone https://github.com/BryOr64/qa-project-Urban-Routes-es.git

### 2. Entrar al proyecto

cd qa-project-Urban-Routes-es

### 3. Instalar las dependencias

Instalar Python, Selenium y Pytest según los requisitos del proyecto.

### 4. Ejecutar las pruebas

pytest TestUrbanRoutes.py

## 📊 Resultados

La suite automatizada contiene nueve comprobaciones relacionadas con el flujo de solicitud de un viaje.

Durante la ejecución documentada del proyecto, las nueve pruebas finalizaron correctamente.

## 💡 Habilidades aplicadas

Este proyecto me permitió practicar:

- Diseño y automatización de escenarios de prueba.
- Automatización de pruebas web con Selenium WebDriver.
- Uso de localizadores para interactuar con elementos de la interfaz.
- Validación de resultados mediante pruebas automatizadas.
- Organización del código de pruebas.
- Manejo de datos de prueba.
- Uso de funciones auxiliares.
- Ejecución de pruebas mediante Pytest.
- Control de versiones con Git y GitHub.

## 🚀 Próximas mejoras

Como evolución del proyecto se pueden incorporar:

- Mayor reutilización de componentes de automatización.
- Mejor documentación de casos de prueba.
- Reportes automáticos de ejecución.
- Capturas de pantalla ante pruebas fallidas.
- Integración continua.
- Refactorización progresiva siguiendo patrones de automatización.

## 👤 Autor

Bryan Orosco

QA Engineer Junior | Ingeniería de Sistemas

LinkedIn:
https://www.linkedin.com/in/bryan-orosco-2312981bb/

GitHub:
https://github.com/BryOr64
