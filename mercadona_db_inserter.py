import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
from tqdm import tqdm  # Barra de progreso
from datetime import datetime  # Para timestamp

# Cargar variables del .env
load_dotenv()

DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")

# Leer CSV
df = pd.read_csv("precios_productos.csv")

# Conexión a MySQL
conn = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()

# Crear tabla si no existe
create_table_sql = """
CREATE TABLE IF NOT EXISTS m_products_mercadona (
    display_name VARCHAR(255),
    iva INT,
    is_new BOOLEAN,
    is_pack BOOLEAN,
    pack_size FLOAT,
    unit_name VARCHAR(50),
    unit_size FLOAT,
    bulk_price DECIMAL(10,2),
    unit_price DECIMAL(10,2),
    approx_size BOOLEAN,
    size_format VARCHAR(10),
    total_units INT,
    unit_selector BOOLEAN,
    bunch_selector BOOLEAN,
    drained_weight FLOAT,
    selling_method INT,
    price_decreased BOOLEAN,
    reference_price DECIMAL(10,3),
    min_bunch_amount FLOAT,
    reference_format VARCHAR(10),
    previous_unit_price VARCHAR(50),
    increment_bunch_amount FLOAT,
    inserted_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""
cursor.execute(create_table_sql)

# Insertar datos con barra de carga
insert_sql = """
INSERT INTO m_products_mercadona (
    display_name, iva, is_new, is_pack, pack_size, unit_name, unit_size,
    bulk_price, unit_price, approx_size, size_format, total_units,
    unit_selector, bunch_selector, drained_weight, selling_method,
    price_decreased, reference_price, min_bunch_amount, reference_format,
    previous_unit_price, increment_bunch_amount, inserted_at
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# tqdm envuelve el iterador para mostrar progreso
for _, row in tqdm(df.iterrows(), total=len(df), desc="Insertando productos"):
    values = tuple(None if pd.isna(x) else x for x in row)
    values += (datetime.now(),)  # Añadir timestamp actual
    cursor.execute(insert_sql, values)

conn.commit()
cursor.close()
conn.close()
