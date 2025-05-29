'''
-----------------------------------------------------------------------------------------------
Título: Gestión de Accesorios de Ski
Fecha: 29-05-2025
Autor: Equipo 3

Descripción:
  Programa para gestionar clientes y accesorios de ski: alta, baja, modificación y listados.

Pendientes:

-----------------------------------------------------------------------------------------------
'''

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

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
    telefonos = {f"telefono{i+1}": tel.strip() for i, tel in enumerate(telefonosRaw)}
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

def modificarCliente(clientes, documento, claves):
    """
    Modifica de forma selectiva los campos indicados de un cliente.
    Si se modifica 'idCliente', actualiza también la clave del dict `clientes`.
    Args:
        clientes (dict): Diccionario de clientes.
        documento (str): Documento del cliente a modificar.
        claves (list of str): Lista de campos a actualizar, ya normalizados a las claves internas.
    Returns:
        dict: El dict `clientes` actualizado.
    """
    if documento not in clientes:
        print(f"No se encontró un cliente con el documento {documento}.")
        return clientes

    cliente = clientes[documento]

    for clave in claves:
        if clave not in cliente:
            print(f"La clave '{clave}' no existe en el cliente.")
            continue
        valorActual = cliente[clave]
        if clave == 'telefonos':
            nuevoValor = input(f"Ingrese los teléfonos del cliente separados por comas (actual: {valorActual}): ").split(',')
        else:
            nuevoValor = input(f"Ingrese nuevo valor para '{'documento' if clave == 'idCliente' else clave }' (actual: {valorActual}): ")

        if clave == 'activo':
            cliente[clave] = nuevoValor.lower() == 'true'
        elif clave == 'idCliente':
            nuevoDocumento = nuevoValor
            cliente['idCliente'] = nuevoValor
            clientes[nuevoDocumento] = cliente
            del clientes[documento]
        elif clave == 'telefonos':
                telefonos = {f"telefono{i+1}": tel.strip() for i, tel in enumerate(nuevoValor) if tel.strip()}
                cliente['telefonos'] = telefonos
        else:
            cliente[clave] = nuevoValor

    print(f"Cliente con documento {cliente['idCliente']} modificado exitosamente.")
    mostrarCliente(cliente, cliente['idCliente'])
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
            print("[3] Gestion de Renta")
            print("[4] Informes")
            print("[5] Opción 5")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
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
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
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
                    # Mostrar claves disponibles
                    clavesDisp = [ 'documento' if k=='idCliente' else k for k in cliente.keys() ]
                    print("Opciones a modificar:", ", ".join(clavesDisp))

                    clavesModificarRaw = input("Opciones a modificar (separadas por comas): ").split(',')
                    # Normalizar 'documento' a 'idCliente'
                    clavesModificar = ["idCliente" if c.strip().lower()=="documento" else c.strip() for c in clavesModificarRaw]
                    modificarCliente(clientes, documento, clavesModificar)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    documento = input("Ingrese el documento del cliente a eliminar: ")
                    clientes = eliminarCliente(clientes, documento)
                    
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("Listado de clientes activos:")
                    listarClientes(clientes)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE ACCESORIOS")
                    print("---------------------------")
                    print("[1] Ingresar Accesorio")
                    print("[2] Modificar Accesorio")
                    print("[3] Eliminar Accesorio")
                    print("[4] Listar Accesorios Activos")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    ...
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...
                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            ...
        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            ...

        elif opcionMenuPrincipal == "5":   # Opción 5 del menú principal
            ...

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")



# Punto de entrada al programa
main()
