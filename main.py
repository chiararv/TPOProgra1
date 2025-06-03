
'''
-----------------------------------------------------------------------------------------------
Título: Gestión de Accesorios de Ski
Fecha: 29-05-2025
Autor: Equipo 3

Descripción:
  Programa para gestionar clientes y accesorios de ski: alta, baja, modificación y listados.

Pendientes:
  Implementar regex para validar entradas de email y teléfono.
  Manejar excepciones para entradas inválidas.
  Implementar persistencia de datos.

-----------------------------------------------------------------------------------------------
'''

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

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


def obtenerDatosCliente(documento):
    """
    Solicita por consola los datos de un cliente y devuelve un diccionario con su información.
    Args:
        documento (str): DNI u otro identificador del cliente.
    Returns:
        dict: Diccionario con las claves:
              idCliente, tipoDocumento, nombre, apellido, email,
              fechaNacimiento, telefonos (dict) y activo (bool).
    """
    tipoDocumento = input("Ingrese el tipo de documento (DNI, Pasaporte, etc.): ")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    email = input("Ingrese el email del cliente: ")
    fechaNacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    telefonosRaw = input("Ingrese los teléfonos del cliente (separados por comas): ").split(',')
    telefonos = {f"telefono{i+1}": tel.strip() for i, tel in enumerate(telefonosRaw) if tel.strip()}
    activo = input("¿El cliente está activo? (True/False): ").lower() == 'true'

    return {
        "idCliente": documento,
        "tipoDocumento": tipoDocumento,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "fechaNacimiento": fechaNacimiento,
        "telefonos": telefonos,
        "activo": activo
    }


def altaCliente(clientes):
    """
    Agrega uno o varios clientes al dict `clientes`, pidiendo datos por consola.
    Args:
        clientes (dict): Diccionario existente de clientes.
    Returns:
        dict: El mismo dict `clientes` actualizado.
    """
    while True:
        documento = input("Ingrese el documento del cliente (o -1 para terminar): ")
        if documento == '-1':
            break
        if documento in clientes:
            print("El cliente ya existe. Intente con otro documento.")
            continue
        cliente = obtenerDatosCliente(documento)
        clientes[documento] = cliente
        print(f"Cliente {documento} agregado.")
    return clientes

def mostrarCliente(cliente, idCliente):
    """
    Muestra por consola los datos de un cliente.
    Args:
        cliente (dict): Diccionario con los datos del cliente.
        idCliente (str): Documento o identificador del cliente.
    Returns:
        None
    """
    print(f"Documento: {idCliente}")
    print(f"Tipo de Documento: {cliente['tipoDocumento']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Apellido: {cliente['apellido']}")
    print(f"Email: {cliente['email']}")
    print(f"Fecha de Nacimiento: {cliente['fechaNacimiento']}")
    print("Teléfonos:")

    if isinstance(cliente['telefonos'], dict) and cliente['telefonos']:
        for claveTel, valorTel in cliente['telefonos'].items():
            print(f"  {claveTel}: {valorTel}")

    print("-" * 40)

def listarClientes(clientes):
    """
    Muestra por consola todos los clientes que estén activos.
    Args:
        clientes (dict): Diccionario de clientes.
    Returns:
        None
    """
    for idCliente, cliente in clientes.items():
        if not cliente.get('activo', False):
            continue
        mostrarCliente(cliente, idCliente)



def eliminarCliente(clientes, documento):
    """
    Elimina el cliente con el documento dado si es que existe.
    Args:
        clientes (dict): Diccionario de clientes.
        documento (str): Documento del cliente a eliminar.
    Returns:
        dict: El dict `clientes` actualizado.
    """
    if documento in clientes:
        del clientes[documento]
        print(f"Cliente con documento {documento} eliminado exitosamente.")
    else:
        print(f"No se encontró un cliente con el documento {documento}.")
    return clientes

def leerCampo(label, valorActual, parseFn=lambda x: x):
    """
    Muestra un prompt indicando el valor actual.
    - Si el usuario pulsa ENTER sin escribir nada, devuelve `valorActual`.
    - En otro caso, aplica `parseFn` a la entrada y devuelve el resultado.

    Args:
        label: Texto a mostrar antes del prompt.
        valorActual: Valor que se mantendrá si la entrada está vacía.
        parseFn: Función que transforma la entrada de cadena
                            en el tipo requerido (str a bool/int/float/etc).

    Returns:
        El valor convertido o el valor actual si no se ingresa respuesta.
    """
    entrada = input(f"{label} (actual: {valorActual}): ").strip()
    if entrada == "":
        return valorActual
    return parseFn(entrada)

parseBool    = lambda x: x.lower() == "true"
parseTelefonos = lambda x: {
    f"telefono{i+1}": t.strip()
    for i, t in enumerate(x.split(","))
    if t.strip()
}

def modificarCliente(clientes, documento):
    """
    Modifica los datos de un cliente existente.
    Si se modifica el 'idCliente', actualiza la clave del dict `clientes`.
    Args:
        clientes (dict): Diccionario de clientes.
        documento (str): Documento del cliente a modificar.
    Returns:
        dict: El dict `clientes` actualizado.
    """
    print("Ingrese datos a modificar, presione ENTER para mantener el valor actual.")
    datos = clientes[documento]
  
    nuevoDoc = leerCampo("Ingrese nuevo documento", datos['idCliente'])
    if nuevoDoc != datos['idCliente']:
        datos['idCliente'] = nuevoDoc
        clientes[nuevoDoc] = datos
        del clientes[documento]
        documento = nuevoDoc  

    telefonosActual = ", ".join(datos['telefonos'].values())
    nuevosTel= leerCampo("Teléfonos", telefonosActual, parseTelefonos)
    if isinstance(nuevosTel, dict):  
        datos['telefonos'] = nuevosTel 

    datos['tipoDocumento']  = leerCampo("Tipo de documento",   datos['tipoDocumento'])
    datos['nombre']        = leerCampo("Nombre",              datos['nombre'])
    datos['apellido']      = leerCampo("Apellido",            datos['apellido'])
    datos['email']         = leerCampo("Email",               datos['email'])
    datos['fechaNacimiento'] = leerCampo("Fecha de nacimiento (YYYY-MM-DD)", datos['fechaNacimiento'])
    datos['activo']        = leerCampo("¿Está activo? (True/False)", datos['activo'],   parseBool)

    print(f"\nCliente {documento} modificado exitosamente.\n")
    mostrarCliente(datos, documento)
    return clientes

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal: muestra el menú y delega acciones de clientes y accesorios.
    """

    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------

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

    clientes = {
        '41110978': {
            "idCliente": "41110978",
            "tipoDocumento": "DNI",
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juanperez@gmail.com",
            "fechaNacimiento": "1990-01-01",
            "telefonos": {
                "telefono1": "123456789",
                "telefono2": "987654321"
            },
            "activo": True
        },
        '12345678': {
            "idCliente": "12345678",
            "tipoDocumento": "DNI",
            "nombre": "Ana",
            "apellido": "Gómez",
            "email": "anagomez@gmail.com",
            "fechaNacimiento": "1990-01-01",
            "telefonos": {
                "telefono1": "123456789",
                "telefono2": "987654321"
            },
            "activo": False
        }
    }
    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------

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
            print("[4] Informes")
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
                    print("[2] Modificar Clientes")
                    print("[3] Eliminar Clientes")
                    print("[4] Listar Clientes Activos")
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

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    clientes = altaCliente(clientes)
                    print("Cliente agregado exitosamente.")
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    documento = input("Ingrese el documento del cliente a modificar: ")
                    cliente = clientes.get(documento)

                    if not cliente:
                        print("Documento no encontrado.")
                        continue
                    modificarCliente(clientes, documento)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    documento = input("Ingrese el documento del cliente a eliminar: ")
                    clientes = eliminarCliente(clientes, documento)
                    
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("Listado de clientes activos:")
                    listarClientes(clientes)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        elif opcionMenuPrincipal == "2": 
            # Opción 2 del menú principal
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
