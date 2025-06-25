import json
import os

# Ruta del archivo JSON
ARCHIVO_JSON = "datos.json"

def gestionar_datos_json():
    """
    Carga el archivo JSON, permite trabajar con los datos en el programa,
    y luego guarda los cambios en el mismo archivo.
    """
    # 1. Leer el archivo JSON
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
            try:
                datos = json.load(f)
                print("✅ Archivo JSON cargado exitosamente.")
            except json.JSONDecodeError:
                print("⚠️ El archivo existe pero está corrupto. Se inicializa vacío.")
                datos = {"clientes": {}, "productos": {}, "rentas": {}}
    else:
        print("⚠️ El archivo JSON no existe. Se creará desde cero.")
        datos = {"clientes": {}, "productos": {}, "rentas": {}}

    # 2. Aquí se llama a la lógica principal del programa
    # Esta función debe modificar el diccionario `datos`
    datos = sistema_principal(datos)

    # 3. Guardar el archivo actualizado
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
        print("✅ Cambios guardados exitosamente en el archivo JSON.")

# -------------------------------------------------------
# Función simulada: acá iría tu menú u otra función central
def sistema_principal(datos):
    """
    Función donde se trabaja con los datos.
    Puede ser reemplazada por tu `main()` o menú completo.
    """
    print("🔧 Editando los datos...")

    # EJEMPLO: modificar nombre de un cliente (si existe)
    cliente_id = input("Ingrese ID de cliente a editar: ")
    if cliente_id in datos["clientes"]:
        nuevo_nombre = input("Nuevo nombre: ")
        datos["clientes"][cliente_id]["nombre"] = nuevo_nombre
        print(f"✅ Cliente {cliente_id} modificado.")
    else:
        print("❌ Cliente no encontrado.")

    return datos

# -------------------------------------------------------

# Llamada al proceso completo
if __name__ == "__main__":
    gestionar_datos_json()
