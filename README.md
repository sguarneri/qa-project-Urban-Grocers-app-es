# Suite de pruebas automatizadas para la plataforma Urban Grocers.

Descripición: Este proyecto se desarrolló para acreditar el Sprint 7 **"Introducción a las automatizaciones de pruebas"** del Bootcamp **QA Engineer** de TripleTen.

## Tabla de contenidos.
- Introducción.
- Instalación.
- Uso.
- Estructura del proyecto.
- Lista de comprobación de pruebas.

## Introducción.

Este código se enfoca en realizar múltiples pruebas que buscan el correcto funcionamiento del campo "name" para la creación de un kit en la plataforma Urban Grocers, misma que otorga TripleTen. 

Esta experiencia me permitió consolidar mis habilidades en **Python, Git, Github y PyCharm.**

## Requisitos previos.

Se requiere la instalación de las librerías:
- requests
- pytest

## Uso.

Para correr las pruebas basta con escribir el comando ' pytest '.

## Estructura del proyecto.

`sender_stand_request.py`: Contiene las solicitudes que se envían al servidor para crear al usuario y el kit.
`create_kit_name_kit_test.py`: Contiene las funciones que dan estructura a la suite de pruebas automatizadas con el siguiente orden:
- Obtener nuevo nombre de kit.
- Obtener token de nuevo usuario.
- Confirmación positiva para pruebas.
- Confirmación negativa para pruebas.
- Pruebas (9).

`data.py`: Contiene los cuerpos de las solicitudes necesarias en formato JSON.
`configuration.py`: Contiene URL y endpoints necesarios.

## Lista de comprobación de pruebas.

| № | Description                                                                                                                                             | ER                                                                                                                           |
|---|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 1 | **El número permitido de caracteres (1):** kit_body = { "name": "a"}                                                                                    | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud. |
| 2 | **El número permitido de caracteres (511):** kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}                           | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud. |
| 3 | **El número de caracteres es menor que la cantidad permitida (0):** kit_body = { "name": "" }                                                           | Código de respuesta: 400.                                                                                                    |
| 4 | **El número de caracteres es mayor que la cantidad permitida (512):** kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } | Código de respuesta: 400.                                                                                                    |
| 5 | **Se permiten caracteres especiales:** kit_body = { "name": ""№%@"," }                                                                                  | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud. |
| 6 | **Se permiten espacios:** kit_body = { "name": " A Aaa " }                                                                                              | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud. |
| 7 | **Se permiten números:** kit_body = { "name": "123" }                                                                                                   | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud. |
| 8 | **El parámetro no se pasa en la solicitud:** kit_body = { }                                                                                             | Código de respuesta: 400.                                                                                                    |
| 9 | **Se ha pasado un tipo de parámetro diferente (número):** kit_body = { "name": 123 }                                                                    | Código de respuesta: 400.                                                                                                    |

## Fuente de la documentación utilizada.

apiDoc Urban Grocers: https://cnt-a3275ede-6462-4c54-9944-ef9ff4997d94.containerhub.tripleten-services.com/docs/

## Tecnologías y técnicas utilizadas.

### Tecnologías.

`Python` `PyCharm` `Git` `Github` `apiDoc`

### Técnicas utilizadas.

- Creación de funciones.
- Creación de archivos.
- Instalación de librerías.
- Importación de librerías.
- Importación de datos entre archivos.
- Depuración de código.
- Control de versiones con Git.
 - Clonar, Fusionar, Actualización, Extracción.
- Navegación en ramificaciones Git.

