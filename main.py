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
from datetime import datetime
import json
import os
import re

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def leerArchivo(archivo):
    '''
       Recibe el nombre de un archivo y devuelve el contenido del archivo en formato JSON.
    '''
    try:
        f = open(archivo, mode='r', encoding='utf-8')
        datos = json.load(f)
        f.close()
        return datos
    except (FileNotFoundError, OSError) as e:
        print("No se pudo abrir el archivo:", e)
        return {}

def mostrarTablaRenta(rentas):
    if not rentas:
        print("No hay rentas que mostrar.")
        return

    # Extraer todas las claves de campos posibles
    campos = set()
    for datos in rentas.values():
        if isinstance(datos, dict):
            campos.update(datos.keys())

    campos = sorted(campos)  # orden alfabético para consistencia

    # Preparar encabezado
    encabezado = ["ID"] + campos
    anchos = {campo: len(campo) for campo in encabezado}

    # Calcular anchos máximos por columna
    for id_renta, datos in rentas.items():
        if not isinstance(datos, dict):
            continue
        anchos["ID"] = max(anchos["ID"], len(str(id_renta)))
        for campo in campos:
            valor = str(datos.get(campo, ""))
            anchos[campo] = max(anchos[campo], len(valor))

    # Imprimir encabezado
    fila_encabezado = " | ".join(campo.ljust(anchos[campo]) for campo in encabezado)
    print(fila_encabezado)
    print("-" * len(fila_encabezado))

    # Imprimir cada renta como fila
    for id_renta, datos in rentas.items():
        if not isinstance(datos, dict):
            continue
        fila = [str(id_renta).ljust(anchos["ID"])]
        for campo in campos:
            valor = str(datos.get(campo, ""))
            fila.append(valor.ljust(anchos[campo]))
        print(" | ".join(fila))




def filtrarRentasPorMes(rentas, mes):
    """
    Filtra las rentas por un mes específico (1-12).
    
    Args:
        rentas (dict): Diccionario con todas las rentas
        mes (int): Mes a filtrar (1-12)
    
    Returns:
        dict: Diccionario con las rentas del mes especificado
    """
    rentasFiltradas = {}
    
    for key, datos in rentas.items():
        try:
            # mes de idRenta (formato: YYYY.MM.DD.HH.MM.SS)
            fechaParts = datos["idRenta"].split('.')
            rentaMes = int(fechaParts[1])  # El mes es el segundo elemento
            
            if rentaMes == mes:
                rentasFiltradas[key] = datos
        except Exception as e:
            print(f"Error en renta {key}: {e}")
    
    return rentasFiltradas

def informeMesEspecifico(rentas):
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
                rentasFiltradas = filtrarRentasPorMes(rentas, mes)
                
                if rentasFiltradas:
                    print(f"\nRentas del mes {mes}:")
                    mostrarTablaRenta(rentasFiltradas)
                else:
                    print(f"No hay rentas registradas en el mes {mes}.")
                
                break
            else:
                print("El mes debe estar entre 1 y 12. Intente nuevamente.")
        except ValueError:
            print("Por favor ingrese un número válido (1-12).")


def filtrarRentasMesActual(rentas):
    """
    Filtra las rentas del mes actual.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
    
    Returns:
        dict: Diccionario con las rentas del mes actual
    """
    rentasFiltradas = {}
    mesActual = datetime.now().month  # Obtenemos el mes actual (1-12)
    
    for key, datos in rentas.items():
        try:
            # Extraemos el mes de idRenta (formato: YYYY.MM.DD.HH.MM.SS)
            fechaParts = datos["idRenta"].split('.')
            rentaMes = int(fechaParts[1])  # El mes es el segundo elemento
            
            if rentaMes == mesActual:
                rentasFiltradas[key] = datos
        except Exception as e:
            print(f"Error en renta {key}: {e}")
    
    return rentasFiltradas

def informeMesActual(rentas):
    """
    Muestra un informe de rentas para el mes actual.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
    """
    rentasFiltradas = filtrarRentasMesActual(rentas)
    mesActual = datetime.now().month
    
    if rentasFiltradas:
        print(f"\nRentas del mes actual ({mesActual}):")
        mostrarTablaRenta(rentasFiltradas)
    else:
        print(f"No hay rentas registradas en el mes actual ({mesActual}).")


def recuentoAccesoriosPorMes(rentas):
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
            idAccesorio = renta["idAccesorio"]
            cantidad = int(renta["cantidad"])
            
            # Inicializar estructura si no existe
            if idAccesorio not in recuento:
                recuento[idAccesorio] = {m: 0 for m in range(1, 13)}
            
            recuento[idAccesorio][mes] += cantidad
            
        except Exception as e:
            print(f"Error procesando renta {renta.get('idRenta', '')}: {e}")
    
    return recuento

def mostrarRecuentoAccesorios(recuento):
    """
    Muestra el recuento de accesorios por mes en formato horizontal.
    """
    if not recuento:
        print("No hay datos de accesorios para mostrar.")
        return

    meses = list(range(1, 13))
    encabezado = ["idAccesorio"] + [f"Mes {m}" for m in meses]
    anchos = {h: len(h) for h in encabezado}

    # Calcular anchos
    for idAcc, conteos in recuento.items():
        anchos["idAccesorio"] = max(anchos["idAccesorio"], len(str(idAcc)))
        for mes in meses:
            val = str(conteos.get(mes, 0))
            anchos[f"Mes {mes}"] = max(anchos[f"Mes {mes}"], len(val))

    # Encabezado
    print(" | ".join(h.ljust(anchos[h]) for h in encabezado))
    print("-" * sum(anchos[h] + 3 for h in encabezado))

    # Filas
    for idAccesorio, conteos in recuento.items():
        fila = [str(idAccesorio).ljust(anchos["idAccesorio"])]
        for mes in meses:
            val = str(conteos.get(mes, 0))
            fila.append(val.ljust(anchos[f"Mes {mes}"]))
        print(" | ".join(fila))


def generarMatrizDineroPorMes(rentas, anio_filtrado=None):
    """
    Genera una matriz de depósitos por mes agrupada por accesorio.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
        anio_filtrado (int, opcional): Año a filtrar. Si es None, incluye todos.
    
    Returns:
        tuple: (matriz, idAccesorios, meses)
    """
    idAccesorios = sorted(set(renta["idAccesorio"] for renta in rentas.values()))
    meses = list(range(1, 13))
    matriz = [[0 for _ in meses] for _ in idAccesorios]

    for renta in rentas.values():
        try:
            fecha = renta["idRenta"].split('.')
            anio = int(fecha[0])
            mes = int(fecha[1])

            if anio_filtrado and anio != anio_filtrado:
                continue

            idAccesorio = renta["idAccesorio"]
            deposito = float(renta["deposito"])

            fila = idAccesorios.index(idAccesorio)
            columna = meses.index(mes)

            matriz[fila][columna] += deposito

        except Exception as e:
            print(f"Error procesando renta {renta.get('idRenta', '')}: {e}")

    # Subtotales
    subtotales = [sum(fila[mes] for fila in matriz) for mes in range(len(meses))]
    matriz.append(subtotales)
    idAccesorios.append("SUBTOTAL")

    return matriz, idAccesorios, meses


def mostrarMatrizDinero(matriz, idAccesorios, meses):
    """
    Muestra la matriz de depósitos por mes en formato horizontal.
    """
    if not matriz or not idAccesorios:
        print("No hay datos de depósitos para mostrar.")
        return

    encabezado = ["idAccesorio"] + [f"Mes {m}" for m in meses]
    anchos = {h: len(h) for h in encabezado}

    # Calcular anchos por columna
    for idx, idAcc in enumerate(idAccesorios):
        anchos["idAccesorio"] = max(anchos["idAccesorio"], len(str(idAcc)))
        for j, mes in enumerate(meses):
            val = f"{matriz[idx][j]:.2f}"
            anchos[f"Mes {mes}"] = max(anchos[f"Mes {mes}"], len(val))

    # Imprimir encabezado
    print(" | ".join(h.ljust(anchos[h]) for h in encabezado))
    print("-" * sum(anchos[h] + 3 for h in encabezado))

    # Imprimir filas
    for i, idAccesorio in enumerate(idAccesorios):
        fila = [str(idAccesorio).ljust(anchos["idAccesorio"])]
        for j, mes in enumerate(meses):
            valor = f"{matriz[i][j]:.2f}"
            fila.append(valor.ljust(anchos[f"Mes {mes}"]))
        print(" | ".join(fila))




#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():

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
                    mostrarTablaRenta(renta)

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

        elif opcionMenuPrincipal == "4":
            # Cargar los datos de renta desde el archivo JSON
            renta = leerArchivo("renta.json")

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
                    print("[4] Recuento accesorios por mes")
                    print("[5] Mostrar dinero por mes")
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
                    mostrarTablaRenta(renta)
                elif opcionSubmenu == "2":
                    informeMesActual(renta)
                elif opcionSubmenu == "3":
                    informeMesEspecifico(renta)
                elif opcionSubmenu == "4":
                    recuento = recuentoAccesoriosPorMes(renta)
                    mostrarRecuentoAccesorios(recuento)
                elif opcionSubmenu == "5":
                    matriz, ids, meses = generarMatrizDineroPorMes(renta)
                    mostrarMatrizDinero(matriz, ids, meses)

        elif opcionMenuPrincipal == "5":
            ...

        if opcionSubmenu != "0":
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")
main()