import json
import csv

# Cargar el archivo JSON
with open("productos_mercadona.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Preparar lista de campos que queremos extraer desde "price_instructions"
campos_objetivo = [
    "iva", "is_new", "is_pack", "pack_size", "unit_name", "unit_size",
    "bulk_price", "unit_price", "approx_size", "size_format", "total_units",
    "unit_selector", "bunch_selector", "drained_weight", "selling_method",
    "price_decreased", "reference_price", "min_bunch_amount", "reference_format",
    "previous_unit_price", "increment_bunch_amount"
]

# Crear CSV
with open("precios_productos.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    # Cabecera del CSV
    writer.writerow(["display_name"] + campos_objetivo)
    
    # Procesar cada producto
    for producto in data:
        fila = [producto.get("display_name")]
        price_info = producto.get("price_instructions", {})
        
        for campo in campos_objetivo:
            fila.append(price_info.get(campo))
        
        writer.writerow(fila)
