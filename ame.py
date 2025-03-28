import requests
import json

# Lista donde guardaremos todos los productos completos
productos_guardados = []

def get_all_products():
    url = 'https://tienda.mercadona.es/api/categories/'
    response = requests.get(url)

    if response.status_code == 200:
        categorias = response.json().get('results', [])

        for categoria in categorias:
            print(f"Categoría: {categoria['name']} (ID: {categoria['id']})")

            if 'categories' in categoria:
                for subcategoria in categoria['categories']:
                    subcat_id = subcategoria['id']
                    subcat_name = subcategoria['name']
                    print(f"  Subcategoría: {subcat_name} (ID: {subcat_id})")

                    url_subcat = f'https://tienda.mercadona.es/api/categories/{subcat_id}'
                    subcat_response = requests.get(url_subcat)

                    if subcat_response.status_code == 200:
                        subcat_data = subcat_response.json()

                        if 'categories' in subcat_data:
                            for subsubcat in subcat_data['categories']:
                                if 'products' in subsubcat:
                                    for product in subsubcat['products']:
                                        product_id = product.get('id')
                                        product_name = product.get('display_name', 'Sin nombre')
                                        print(f"    Producto ID: {product_id} - {product_name}")
                                        get_product_details(product_id)
                                else:
                                    print("    ⚠️ No se encontraron productos en esta sub-subcategoría.")
                        else:
                            print("    ⚠️ No hay campo 'categories' en la subcategoría.")
                    else:
                        print(f"    ❌ Error al acceder a la subcategoría {subcat_id}: {subcat_response.status_code}")
    else:
        print(f"❌ Error al obtener las categorías: {response.status_code}")

    # Guardar al final del scraping
    with open("productos_mercadona.json", "w", encoding="utf-8") as f:
        json.dump(productos_guardados, f, indent=4, ensure_ascii=False)
        print("✅ Archivo 'productos_mercadona.json' creado con éxito.")

def get_product_details(product_id):
    url = f'https://tienda.mercadona.es/api/products/{product_id}'
    response = requests.get(url)

    if response.status_code == 200:
        product_data = response.json()
        productos_guardados.append(product_data)  # Guardamos el JSON completo
    else:
        print(f"      ❌ Error al obtener el producto {product_id}: {response.status_code}")

# Ejecutamos el scraping
get_all_products()
