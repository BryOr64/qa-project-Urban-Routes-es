# Casos de Prueba Automatizados — Urban Routes

## Objetivo

Documentar los escenarios automatizados del flujo de solicitud de un viaje en la aplicación Urban Routes.

## Alcance

Las pruebas cubren el flujo principal de solicitud de un taxi en la tarifa Comfort, incluyendo datos de ruta, teléfono, método de pago, mensaje al conductor, servicios adicionales y confirmación del viaje.

---

## TC-01 — Configurar ruta

**Objetivo:** Verificar que el usuario pueda ingresar correctamente las direcciones de origen y destino.

**Datos de prueba:**
- Origen: East 2nd Street, 601
- Destino: 1300 1st St

**Pasos:**
1. Abrir la aplicación Urban Routes.
2. Ingresar la dirección de origen.
3. Ingresar la dirección de destino.

**Resultado esperado:**
Las direcciones ingresadas deben mostrarse correctamente en sus respectivos campos.

---

## TC-02 — Seleccionar tarifa Comfort

**Objetivo:** Verificar que el usuario pueda seleccionar la tarifa Comfort.

**Precondición:**
La ruta debe estar configurada.

**Pasos:**
1. Solicitar un taxi.
2. Seleccionar la tarifa Comfort.

**Resultado esperado:**
La tarifa seleccionada debe mostrarse como “Comfort”.

---

## TC-03 — Registrar número telefónico

**Objetivo:** Verificar que el usuario pueda registrar y confirmar un número telefónico.

**Datos de prueba:**
- Teléfono: +1 123 123 12 12

**Pasos:**
1. Abrir el formulario de número telefónico.
2. Ingresar el número.
3. Solicitar el código de confirmación.
4. Ingresar el código recibido.
5. Confirmar.

**Resultado esperado:**
El número telefónico debe quedar registrado correctamente.

---

## TC-04 — Agregar método de pago

**Objetivo:** Verificar que el usuario pueda agregar una tarjeta como método de pago.

**Datos de prueba:**
- Número de tarjeta: 1234 5678 9100
- Código: 111

**Pasos:**
1. Abrir los métodos de pago.
2. Seleccionar la opción para agregar una tarjeta.
3. Ingresar número y código.
4. Guardar la tarjeta.
5. Cerrar el modal.

**Resultado esperado:**
La tarjeta debe quedar seleccionada como método de pago.

---

## TC-05 — Enviar mensaje al conductor

**Objetivo:** Verificar que el usuario pueda escribir un mensaje para el conductor.

**Datos de prueba:**
- Mensaje: “Muéstrame el camino al museo”

**Pasos:**
1. Ubicar el campo de mensaje.
2. Ingresar el texto.

**Resultado esperado:**
El mensaje debe permanecer visible en el campo correspondiente.

---

## TC-06 — Solicitar manta y pañuelos

**Objetivo:** Verificar que el usuario pueda activar la opción de manta y pañuelos.

**Pasos:**
1. Ubicar la opción de manta y pañuelos.
2. Activarla.

**Resultado esperado:**
La opción debe quedar habilitada.

---

## TC-07 — Solicitar dos helados

**Objetivo:** Verificar que el usuario pueda agregar dos unidades de helado.

**Pasos:**
1. Presionar dos veces el botón para agregar helados.

**Resultado esperado:**
El contador debe mostrar el valor “2”.

---

## TC-08 — Solicitar taxi

**Objetivo:** Verificar que el usuario pueda iniciar la búsqueda de un automóvil.

**Pasos:**
1. Presionar el botón para solicitar el taxi.

**Resultado esperado:**
Debe aparecer el modal con el texto “Buscar automóvil”.

---

## TC-09 — Validar información del conductor

**Objetivo:** Verificar que el sistema muestre información del conductor asignado.

**Pasos:**
1. Esperar la asignación del conductor.
2. Validar el título del modal.

**Resultado esperado:**
Debe aparecer un mensaje que incluya “El conductor”.

---

## Resultado general

La suite automatizada valida nueve escenarios del flujo principal de solicitud de un viaje en Urban Routes.
