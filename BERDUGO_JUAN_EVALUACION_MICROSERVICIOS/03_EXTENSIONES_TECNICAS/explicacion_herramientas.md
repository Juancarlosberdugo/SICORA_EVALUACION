# Explicación del porqué de la elección de herramientas y tecnologías

Este documento explica por qué se eligieron las herramientas y tecnologías principales del proyecto, enfocándose en los motivos prácticos y técnicos que justifican su uso.

---

## 1. FastAPI
Se eligió FastAPI porque permite construir APIs modernas, seguras y eficientes en Python, aprovechando la validación automática de datos, la generación de documentación interactiva y el soporte nativo para programación asíncrona. Esto facilita el desarrollo rápido, la integración con otras herramientas y la mantenibilidad del código.

---

## 2. SQLAlchemy ORM y Alembic
SQLAlchemy fue seleccionada por su capacidad para mapear clases Python a tablas de bases de datos, evitando SQL manual y facilitando la portabilidad entre motores. Alembic complementa esto permitiendo gestionar cambios en el esquema de la base de datos de forma controlada y reproducible, esencial para equipos y CI/CD.

---

## 3. Pydantic
Pydantic se utiliza porque permite validar y serializar datos de manera sencilla y segura usando type hints. Esto asegura que la API reciba y envíe datos correctos, reduciendo errores y mejorando la robustez del sistema.

---

## 4. JWT (PyJWT)
Se usa JWT para la autenticación y autorización porque permite transmitir información segura y verificable entre partes, facilitando la gestión de sesiones y la integración con clientes web y móviles.

---

## 5. Pytest
Pytest es el framework de testing elegido por su flexibilidad y facilidad para escribir pruebas, preparar datos de test y simular dependencias externas. Esto ayuda a mantener la calidad del código y detectar errores de forma temprana.

---

## 6. Redis
Redis fue seleccionado por su velocidad y eficiencia como base de datos en memoria, ideal para cachear datos, gestionar sesiones y soportar arquitecturas distribuidas y de alta concurrencia.

---

## 7. Uvicorn/ASGI
Uvicorn se utiliza como servidor ASGI porque permite ejecutar aplicaciones asíncronas, manejar muchas conexiones concurrentes y soportar tecnologías modernas como WebSockets, lo que es fundamental para la escalabilidad y el rendimiento del sistema.
