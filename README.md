# 🛒 Mercadata: Scraper de productos de Mercadona

![Mercadata Banner](images/mercadata.png)

**Mercadata** es una herramienta de scraping que extrae datos de productos desde la API pública de [Mercadona](https://tienda.mercadona.es/), los transforma en un formato CSV y los inserta en una base de datos MySQL para su posterior análisis.

## 🚀 ¿Qué hace este proyecto?

1. **Scrapea todas las categorías y productos** desde la API oficial de Mercadona.
2. **Guarda los datos crudos** en un archivo JSON llamado `productos_mercadona.json`.
3. **Transforma los datos** relevantes de precios e información del producto en un CSV (`precios_productos.csv`).
4. **Inserta los datos** en una tabla MySQL llamada `m_products_mercadona`.

---

## 📁 Estructura del Proyecto

```
📦mercadata/
 ┣ 📜main.py
 ┣ 📜ame.py
 ┣ 📜reader_json.py
 ┣ 📜mercadona_db_inserter.py
 ┣ 📁images/
 ┃ ┗ 📸mercadata.png
 ┣ 📜.env
 ┣ 📜requirements.txt
 ┗ 📜README.md
```

---

## ⚙️ Requisitos

- Python 3.8+
- MySQL en ejecución
- Archivo `.env` con las credenciales de conexión

### Ejemplo de `.env`:

```
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_contraseña
MYSQL_DATABASE=dev_testeos
```

---

## 🧪 Instalación

```bash
# Clona el proyecto
git clone https://github.com/tuusuario/mercadata.git
cd mercadata

# Crea un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
python main.py
```

Este comando ejecutará los tres módulos principales en orden:

1. `ame.py`: scraping desde la API y guardado en JSON.
2. `reader_json.py`: transforma los productos al CSV.
3. `mercadona_db_inserter.py`: inserta el CSV en MySQL.

---

## 🗃️ Tabla MySQL generada

La tabla `m_products_mercadona` incluye los siguientes campos:

- `display_name`, `iva`, `is_new`, `is_pack`, `pack_size`, `unit_name`, `unit_size`, etc.
- `inserted_at` con timestamp automático de inserción.

---

## ✍️ Autor

Desarrollado por [Tu Nombre].

---

## 📄 Licencia

MIT License

---

## ❤️ Agradecimientos

- A Mercadona por permitir el acceso a su API pública para el análisis de productos.
