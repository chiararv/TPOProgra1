"""
-----------------------------------------------------------------------------------------------
Título: Gestión de Accesorios de Ski
Autor: Grupo 3

Descripción: Programa para gestionar clientes y accesorios de ski: alta, baja, modificación y listados.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaCliente(_clientes):
    ...
    return _clientes

def altaRenta(rentas):
    print("--- Alta de Renta ---")
    idRenta = input("Ingrese ID de Renta: ")
    if idRenta in rentas:
        print("ERROR: Ya existe una renta con ese ID.")
        return rentas

    idCliente = input("Ingrese ID de Cliente: ")
    dias = int(input("Ingrese cantidad de días: "))
    fechaDevolucion = input("Ingrese fecha de devolución (AAAA.MM.DD.hh.mm.ss): ")
    total = float(input("Ingrese total: "))
    deposito = float(input("Ingrese depósito: "))
    estado = input("Ingrese estado: ")
    metodoPago = input("Ingrese método de pago: ")
    idAccesorio = input("Ingrese ID de Accesorio: ")
    cantidad = input("Ingrese cantidad: ")

    rentas[idRenta] = {
        "idRenta": idRenta,
        "idCliente": idCliente,
        "dias": dias,
        "fecha Devolucion": fechaDevolucion,
        "total": total,
        "deposito": deposito,
        "estado": estado,
        "metodoPago": metodoPago,
        "idAccesorio": idAccesorio,
        "cantidad": cantidad
    }
    print("Renta registrada exitosamente.")
    return rentas

def bajaRenta(rentas):
    print("--- Baja de Renta ---")
    idRenta = input("Ingrese ID de Renta a eliminar: ")
    if idRenta in rentas:
        del rentas[idRenta]
        print("Renta eliminada.")
    else:
        print("ERROR: No se encontró una renta con ese ID.")
    return rentas

def modificarRenta(rentas):
    print("--- Modificar Renta ---")
    idRenta = input("Ingrese ID de Renta a modificar: ")
    if idRenta not in rentas:
        print("ERROR: No se encontró una renta con ese ID.")
        return rentas

    renta = rentas[idRenta]
    print(f"Datos actuales: {renta}")

    for clave in renta:
        if clave == "idRenta":
            continue
        nuevo_valor = input(f"Modificar '{clave}' (actual: {renta[clave]}) - Enter para mantener: ")
        if nuevo_valor:
            if clave in ["dias"]:
                renta[clave] = int(nuevo_valor)
            elif clave in ["total", "deposito"]:
                renta[clave] = float(nuevo_valor)
            else:
                renta[clave] = nuevo_valor

    print("Renta modificada con éxito.")
    return rentas

def listarRentas(rentas):
    print("--- Listado de Rentas ---")
    if not rentas:
        print("No hay rentas registradas.")
        return

    print(f"{'ID':<5} {'Cliente':<10} {'Días':<5} {'F. Devolución':<20} {'Total':<10} {'Depósito':<10} {'Estado':<12} {'Pago':<13} {'Accesorio':<12} {'Cant.':<8}")
    print("-" * 112)

    for renta in rentas.values():
        print(f"{renta['idRenta']:<5} {renta['idCliente']:<10} {renta['dias']:<5} {renta['fecha Devolucion']:<20} {renta['total']:<10.2f} {renta['deposito']:<10.2f} {renta['estado']:<12} {renta['metodoPago']:<15} {renta['idAccesorio']:<10} {renta['cantidad']:<6}")


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    clientes = {...}

    Renta = {
        "01": {
            "idRenta": "01",
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
            "idRenta": "02",
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
            "idRenta": "03",
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
            "idRenta": "04",
            "idCliente": "04",
            "dias": 3,
            "fecha Devolucion": "2025.06.03.18.00.00",
            "total": 4500.0,
            "deposito": 5000.0,
            "estado": "cancelado",
            "metodoPago": "transferencia",
            "idAccesorio": "05",
            "cantidad": "2"
        },
        "05": {
            "idRenta": "05",
            "idCliente": "05",
            "dias": 15,
            "fecha Devolucion": "2025.06.20.20.00.00",
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
            print("[4] Opción 4")
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
                    clientes = altaCliente(clientes)
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
                    Renta = altaRenta(Renta)
                elif opcionSubmenu == "2":
                    Renta = bajaRenta(Renta)
                elif opcionSubmenu == "3":
                    Renta = modificarRenta(Renta)
                elif opcionSubmenu == "4":
                    listarRentas(Renta)

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

        elif opcionMenuPrincipal == "4":
            ...

        elif opcionMenuPrincipal == "5":
            ...

        if opcionSubmenu != "0":
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

main()
