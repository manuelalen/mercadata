import subprocess
import sys

print("🟢 Ejecutando ame.py...")
subprocess.run([sys.executable, "ame.py"], check=True)

print("🟢 Ejecutando reader_json.py...")
subprocess.run([sys.executable, "reader_json.py"], check=True)

print("🟢 Ejecutando mercadona_db_inserter.py...")
subprocess.run([sys.executable, "mercadona_db_inserter.py"], check=True)

print("✅ Todos los módulos se han ejecutado correctamente.")
