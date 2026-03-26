# 🐍 Python API Automation Suite

Este repositorio contiene una suite de pruebas automatizadas para validar endpoints REST, desarrollada con **Python** y **Pytest**.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.14.3
- **Framework de Pruebas:** Pytest
- **Librería HTTP:** Requests (con manejo de Session y Headers)
- **Reportes:** Pytest-html

## 🎯 Escenarios de Prueba
1. **GET Users:** Validación de status 200 y presencia de datos.
2. **POST Create User:** Verificación de creación exitosa (Status 201).
3. **Negative Test (404):** Validación de manejo de errores en usuarios inexistentes.
4. **Functional POST:** Simulación de creación de contenido (Posts).
5. **Invalid Route:** Verificación de seguridad ante rutas no definidas.

## 🔧 Notas Técnicas (Troubleshooting)
Durante el desarrollo, se implementó una arquitectura basada en `requests.Session()` y configuraciones personalizadas de `User-Agent` para emular el comportamiento de un navegador real, garantizando la estabilidad de los tests ante protecciones de red (WAF/Cloudflare).

## 🚀 Ejecución
1. Activar entorno virtual: `.\venv\Scripts\activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar suite y generar reporte:
   ```bash
   pytest -v --html=report.html