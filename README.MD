# API Django

Este proyecto es una API desarrollada con Django y Django REST Framework (DRF). Está diseñada para demostrar conceptos clave de desarrollo backend y manejo de APIs en Django.

## 🚀 Características

- CRUD (Crear, Leer, Actualizar, Eliminar) para los modelos configurados.
- Uso de Django REST Framework para crear endpoints de manera sencilla y eficiente.
- Configuración básica lista para escalar con autenticación, permisos y serializadores.


## 🛠️ Tecnologías Utilizadas

- **Django**: Framework principal para el backend.
- **Django REST Framework**: Para la creación de endpoints de API.
- **SQLite**: Base de datos ligera para desarrollo.

## 📦 Requisitos Previos

Asegúrate de tener instalado:

- Python 3.x
- pip (Gestor de paquetes de Python)
- Un entorno virtual configurado (opcional, pero recomendado)

## 📥 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/guillermoMat/api-django.git
    ```
2. Navega al directorio del proyecto:
  `cd api-django`

3. Instala las dependencias en un entorno virtual:
```bash
  python -m venv env
  source env/bin/activate  # En Windows: env\Scripts\activate
  pip install -r requirements.txt
   ```
4. Aplica las migraciones para configurar la base de datos:
 `python manage.py migrate`

5. Ejecuta el servidor de desarrollo:
`python manage.py runserver`

