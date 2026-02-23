import os

# 📂 Ruta de la carpeta (cámbiala por la tuya)
carpeta = r"C:\Users\Nel\Desktop\ecodata info\Fotos equip"

for nombre in os.listdir(carpeta):
    ruta_antigua = os.path.join(carpeta, nombre)
    
    # Solo archivos (no carpetas)
    if os.path.isfile(ruta_antigua):
        nuevo_nombre = nombre.replace(" ", "_")
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)

        if nombre != nuevo_nombre:
            os.rename(ruta_antigua, ruta_nueva)
            print(f"Renombrado: {nombre} → {nuevo_nombre}")

print("✅ Listo.")