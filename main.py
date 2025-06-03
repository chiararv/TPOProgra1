"""
-----------------------------------------------------------------------------------------------
Título: Gestión de informe
Autor: Grupo 3

Descripción: Programa para gestionar informe  y accesorios de ski: alta, baja, modificación y listados.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from datetime import datetime, timedelta

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def mostrar_tabla_renta(rentas):
    if not rentas:
        print("No hay rentas que mostrar.")
        return

    columnas = list(rentas.keys())
    campos = list(rentas[columnas[0]].keys())

    # Calcular el ancho máximo de cada columna (por campo)
    anchos = {}
    anchos["Campo"] = max(len(campo) for campo in campos)

    for col in columnas:
        anchos[col] = max(len(str(rentas[col][campo])) for campo in campos)

    # Aumentar los espacios por estética, se puede quitar
    for k in anchos:
        anchos[k] += 2

    # Encabezado
    print("Campo".ljust(anchos["Campo"]), end=" || ")
    for col in columnas:
        print(col.center(anchos[col]), end=" || ")
    print()

    # Separador
    total_ancho = sum(anchos.values()) + (4 * len(columnas)) + 3
    print("-" * total_ancho)

    # Filas
    for campo in campos:
        print(campo.ljust(anchos["Campo"]), end=" || ")
        for col in columnas:
            valor = str(rentas[col].get(campo, ""))
            print(valor.center(anchos[col]), end=" || ")
        print()


def filtrar_rentas_por_mes(rentas, mes):
    """
    Filtra las rentas por un mes específico (1-12).
    
    Args:
        rentas (dict): Diccionario con todas las rentas
        mes (int): Mes a filtrar (1-12)
    
    Returns:
        dict: Diccionario con las rentas del mes especificado
    """
    rentas_filtradas = {}
    
    for key, datos in rentas.items():
        try:
            # mes de idRenta (formato: YYYY.MM.DD.HH.MM.SS)
            fecha_parts = datos["idRenta"].split('.')
            renta_mes = int(fecha_parts[1])  # El mes es el segundo elemento
            
            if renta_mes == mes:
                rentas_filtradas[key] = datos
        except Exception as e:
            print(f"Error en renta {key}: {e}")
    
    return rentas_filtradas

def informe_mes_especifico(rentas):
    """
    Muestra un informe de rentas para un mes específico.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
    """
    while True:
        try:
            print("\n--- Informe por Mes Específico ---")
            mes = int(input("Ingrese el mes a consultar (1-12): "))
            
            if 1 <= mes <= 12:
                rentas_filtradas = filtrar_rentas_por_mes(rentas, mes)
                
                if rentas_filtradas:
                    print(f"\nRentas del mes {mes}:")
                    mostrar_tabla_renta(rentas_filtradas)
                else:
                    print(f"No hay rentas registradas en el mes {mes}.")
                
                break
            else:
                print("El mes debe estar entre 1 y 12. Intente nuevamente.")
        except ValueError:
            print("Por favor ingrese un número válido (1-12).")


def filtrar_rentas_mes_actual(rentas):
    """
    Filtra las rentas del mes actual.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
    
    Returns:
        dict: Diccionario con las rentas del mes actual
    """
    rentas_filtradas = {}
    mes_actual = datetime.now().month  # Obtenemos el mes actual (1-12)
    
    for key, datos in rentas.items():
        try:
            # Extraemos el mes de idRenta (formato: YYYY.MM.DD.HH.MM.SS)
            fecha_parts = datos["idRenta"].split('.')
            renta_mes = int(fecha_parts[1])  # El mes es el segundo elemento
            
            if renta_mes == mes_actual:
                rentas_filtradas[key] = datos
        except Exception as e:
            print(f"Error en renta {key}: {e}")
    
    return rentas_filtradas

def informe_mes_actual(rentas):
    """
    Muestra un informe de rentas para el mes actual.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
    """
    rentas_filtradas = filtrar_rentas_mes_actual(rentas)
    mes_actual = datetime.now().month
    
    if rentas_filtradas:
        print(f"\nRentas del mes actual ({mes_actual}):")
        mostrar_tabla_renta(rentas_filtradas)
    else:
        print(f"No hay rentas registradas en el mes actual ({mes_actual}).")


def recuento_accesorios_por_mes(rentas):
    """
    Genera un recuento de accesorios rentados por mes.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
    
    Returns:
        dict: Diccionario con el formato {idAccesorio: {mes: cantidad_total}}
    """
    recuento = {}
    
    for renta in rentas.values():
        try:
            # Extraer mes de idRenta (formato: YYYY.MM.DD.HH.MM.SS)
            mes = int(renta["idRenta"].split('.')[1])
            id_accesorio = renta["idAccesorio"]
            cantidad = int(renta["cantidad"])
            
            # Inicializar estructura si no existe
            if id_accesorio not in recuento:
                recuento[id_accesorio] = {m: 0 for m in range(1, 13)}
            
            # Sumar cantidad al mes correspondiente
            recuento[id_accesorio][mes] += cantidad
            
        except Exception as e:
            print(f"Error procesando renta {renta.get('idRenta', '')}: {e}")
    
    return recuento

def obtener_nombre_mes(mes_numero, year):
    """
    Devuelve el nombre del mes abreviado (3 letras) con el año. Ej: ENE.25
    """
    meses = [
        "ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
        "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"
    ]
    return f"{meses[mes_numero-1]}.{str(year)[-2:]}"

def mostrar_recuento_accesorios(recuento, year=2025):
    """
    Muestra el recuento de accesorios por mes en formato de tabla.
    """
    if not recuento:
        print("No hay datos de accesorios para mostrar.")
        return
    
    # Obtener todos los idAccesorios y ordenarlos
    id_accesorios = sorted(recuento.keys())
    meses = list(range(1, 13))
    
    # Calcular anchos de columnas
    ancho_id = max(len("Accesorio"), max(len(id) for id in id_accesorios)) + 2
    ancho_mes = 8  # Suficiente para "ENE.25" y los valores
    
    # Encabezado con año
    print(f"\nRECUENTO DE ACCESORIOS POR MES - AÑO {year}")
    print("Accesorio".ljust(ancho_id), end=" || ")
    for mes in meses:
        print(obtener_nombre_mes(mes, year).center(ancho_mes), end=" || ")
    print()
    
    # Separador
    total_ancho = ancho_id + (len(meses) * (ancho_mes + 4)) + 3
    print("-" * total_ancho)
    
    # Filas de datos
    for id_accesorio in id_accesorios:
        print(id_accesorio.ljust(ancho_id), end=" || ")
        for mes in meses:
            cantidad = recuento[id_accesorio].get(mes, 0)
            print(str(cantidad).center(ancho_mes), end=" || ")
        print()
def generar_matriz_dinero_por_mes(rentas):
    """
    Genera una matriz de depósitos por mes.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
    
    Returns:
        tuple: (matriz, id_clientes, meses)
          - matriz: Lista de listas con los depósitos sumados
          - id_clientes: Lista ordenada de ids de clientes (opcional, se puede cambiarlo a otra categoría si prefiere incluso)
          - meses: Lista de meses (1-12)
    """
    # Recolecta todos los idClientes únicos (para las filas)
    id_clientes = sorted(set(renta["idCliente"] for renta in rentas.values()))
    meses = list(range(1, 13))
    
    # Inicializa la matriz con ceros
    matriz = [[0 for _ in meses] for _ in id_clientes]
    
    # Llena la matriz con los depósitos
    for renta in rentas.values():
        try:
            mes = int(renta["idRenta"].split('.')[1])
            id_cliente = renta["idCliente"]
            deposito = float(renta["deposito"])
            
            fila = id_clientes.index(id_cliente)
            columna = meses.index(mes)
            matriz[fila][columna] += deposito
        except Exception as e:
            print(f"Error procesando renta {renta.get('idRenta', '')}: {e}")
        
    # Añadir fila de subtotales
    subtotales = [sum(fila[mes] for fila in matriz) for mes in range(len(meses))]
    matriz.append(subtotales)
    id_clientes.append("SUBTOTAL")  # Etiqueta para la fila adicional
    
    return matriz, id_clientes, meses

def mostrar_matriz_dinero(matriz, id_clientes, meses, year=2025):
    """
    Muestra la matriz de depósitos por mes en formato de tabla.
    """
    if not matriz or not id_clientes:
        print("No hay datos de depósitos para mostrar.")
        return
    
    # Calcular anchos de columnas
    ancho_id = max(len("Cliente"), max(len(id) for id in id_clientes)) + 2
    ancho_mes = 10  # Ajustado para valores como "30000.00"
    
    # Encabezado con año
    print(f"\nRECUENTO DE DINERO POR MES - AÑO {year}")
    print("Cliente".ljust(ancho_id), end=" || ")
    for mes in meses:
        print(obtener_nombre_mes(mes, year).center(ancho_mes), end=" || ")
    print()
    
    # Separador
    total_ancho = ancho_id + (len(meses) * (ancho_mes + 4)) + 3
    print("-" * total_ancho)
    
    # Filas de datos
    for i, id_cliente in enumerate(id_clientes):
        print(id_cliente.ljust(ancho_id), end=" || ")
        for j, mes in enumerate(meses):
            # Formatear todos los valores con 2 decimales y ancho fijo
            valor = matriz[i][j]
            dinero = f"{valor:.2f}" if valor != 0 else "0.00"
            print(dinero.center(ancho_mes), end=" || ")
        print()

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    clientes = {...}

    Renta = {
        "01": {
            "idRenta": "2025.05.10.12.00.00",
            "idCliente": "01",
            "dias": 10,
            "fecha Devolucion": "2025.06.10.12.00.00",
            "total": 15000.0,
            "deposito": 20000.0,
            "estado": "ocupado",
            "metodoPago": "efectivo",
            "idAccesorio": "01",
            "cantidad": "20"
        },
        "02": {
            "idRenta": "2025.05.05.15.30.00",
            "idCliente": "02",
            "dias": 5,
            "fecha Devolucion": "2025.06.05.15.30.00",
            "total": 7500.0,
            "deposito": 10000.0,
            "estado": "pendiente",
            "metodoPago": "tarjeta",
            "idAccesorio": "03",
            "cantidad": "5"
        },
        "03": {
            "idRenta": "2025.05.12.09.45.00",
            "idCliente": "03",
            "dias": 7,
            "fecha Devolucion": "2025.06.12.09.45.00",
            "total": 10500.0,
            "deposito": 15000.0,
            "estado": "finalizado",
            "metodoPago": "efectivo",
            "idAccesorio": "02",
            "cantidad": "10"
        },
        "04": {
            "idRenta": "2025.04.03.18.00.00",
            "idCliente": "04",
            "dias": 3,
            "fecha Devolucion": "2025.05.03.18.00.00",
            "total": 4500.0,
            "deposito": 5000.0,
            "estado": "cancelado",
            "metodoPago": "transferencia",
            "idAccesorio": "01",
            "cantidad": "2"
        },
        "05": {
            "idRenta": "2025.06.20.20.00.00",
            "idCliente": "05",
            "dias": 15,
            "fecha Devolucion": "2025.07.20.20.00.00",
            "total": 22500.0,
            "deposito": 30000.0,
            "estado": "ocupado",
            "metodoPago": "tarjeta",
            "idAccesorio": "04",
            "cantidad": "25"
        }
    }

    while True:
        while True:
            opciones = 5
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de clientes")
            print("[2] Gestión de accesorios")
            print("[3] Gestión de rentas")
            print("[4] Informe")
            print("[5] Opción 5")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()

            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0":
            exit()

        elif opcionMenuPrincipal == "1":
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE CLIENTES")
                    print("---------------------------")
                    print("[1] Ingresar Clientes")
                    print("[2] Opción 2")
                    print("[3] Opción 3")
                    print("[4] Opción 4")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0":
                    break
                elif opcionSubmenu == "1":
                    ...
                elif opcionSubmenu == "2":
                    ...
                elif opcionSubmenu == "3":
                    ...
                elif opcionSubmenu == "4":
                    ...

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

        elif opcionMenuPrincipal == "2":
            ...

        elif opcionMenuPrincipal == "3":
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE RENTAS")
                    print("---------------------------")
                    print("[1] Ingresar Renta")
                    print("[2] Eliminar Renta")
                    print("[3] Modificar Renta")
                    print("[4] Listar Rentas")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0":
                    break
                elif opcionSubmenu == "1":
                    ...
                elif opcionSubmenu == "2":
                    ...
                elif opcionSubmenu == "3":
                    ...
                elif opcionSubmenu == "4":
                    ...

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

        elif opcionMenuPrincipal == "4":
            while True:
                while True:
                    opciones = 5
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > Informe")
                    print("---------------------------")
                    print("[1] Informe Total")
                    print("[2] Informe del ultimo Mes")
                    print("[3] Informe de un Mes")
                    print("[4] recuento accesorios por mes")
                    print("[5] mostrar dinero por mes")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0":
                    break
                elif opcionSubmenu == "1":
                    mostrar_tabla_renta(Renta)
                elif opcionSubmenu == "2":
                    informe_mes_actual(Renta)
                elif opcionSubmenu == "3":
                    informe_mes_especifico(Renta)
                elif opcionSubmenu == "4":
                    recuento = recuento_accesorios_por_mes(Renta)
                    mostrar_recuento_accesorios(recuento, year=2025)
                elif opcionSubmenu == "5":
                    matriz, ids, meses = generar_matriz_dinero_por_mes(Renta)
                    mostrar_matriz_dinero(matriz, ids, meses, year=2025)

        elif opcionMenuPrincipal == "5":
            ...

        if opcionSubmenu != "0":
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

main()