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

def obtenerNuevoValor(etiqueta, valorActual, parseFn=lambda x: x):
    """
    Muestra un prompt indicando el valor actual.
    - Si el usuario pulsa ENTER sin escribir nada, devuelve `valorActual`.
    - En otro caso, aplica `parseFn` a la entrada y devuelve el resultado.

    Args:
        etiqueta: Texto a mostrar antes del prompt.
        valorActual: Valor que se mantendrá si la entrada está vacía.
        parseFn: Función que transforma la entrada de cadena
                            en el tipo requerido (str a bool/int/float/etc).

    Returns:
        El valor convertido o el valor actual si no se ingresa respuesta.
    """
    entrada = input(f"{etiqueta} (actual: {valorActual}): ").strip()
    if entrada:
        return parseFn(entrada)
    else:
        return valorActual

def parseBool(x):
    """convierte string a boolean"""
    return x.lower() == "true"
def parseInt(x): 
    """convierte string a entero"""
    return int(x)

def parseFloat(x): 
    """convierte string a float"""
    return float(x)

def parseTelefonos(x):
    """convierte números de teléfono separados por coma a un diccionario"""
    return {
        f"telefono{i+1}": t.strip()
        for i, t in enumerate(x.split(","))
        if t.strip()
    }
def parseColors(texto: str) -> dict:
    """Convierte 'rojo, azul' ➜ {'color1': 'rojo', 'color2': 'azul'}."""
    return {f"color{i+1}": c.strip()
            for i, c in enumerate(texto.split(",")) if c.strip()}

def obtenerEtiqueta(clave: str):
    '''
        Retorna la etiqueta de una clave.
        Parámetros:
            clave (str): Clave a convertir.
        Retorna:
            str: Etiqueta de la clave.
    '''
    etiquetas = {
        # General
        "nombre":         "Nombre",
        "activo":         "¿Está activo? (True/False)",
        
        # Cliente
        "idCliente":      "Documento",
        "tipoDocumento":  "Tipo de documento",
        "apellido":       "Apellido",
        "email":          "Email",
        "fechaNacimiento":"Fecha de nacimiento (YYYY-MM-DD)",
        "telefonos":      "Teléfonos (separados por coma)",
        
        # Renta
        "idRenta":        "ID de Renta",
        "dias":           "Cantidad de días",
        "fechaDevolucion":"Fecha de devolución (AAAA.MM.DD.hh.mm.ss)",
        "total":          "Total",
        "deposito":       "Depósito",
        "estado":         "Estado",
        "metodoPago":     "Método de pago",
        "idAccesorio":    "ID de Accesorio",
        "cantidad":       "Cantidad",
        
        # Accesorio
        "descripcion":    "Descripción",
        "stock":          "Cantidad en stock del accesorio",
        "precioUnitario": "Precio unitario",
        "colores":        "Colores disponibles (separados por coma)"
    }
    return etiquetas.get(clave, clave.capitalize())


def altaAccesorio(accesorios,codigo,nombre, descripcion, stock, precioUnitario, colores=None, activo=True):
    '''
        Agrega un accesorio al diccionario de accesorios.
            Parámetros:
                accesorios (dict):
                codigo (str)
                nombre (str)
                descripcion (str)
                stock (int)
                precioUnitario (float)
                colores (dict, opcional)
                activo (bool, opcional)
            Retorna:
                dict: El diccionario de accesorios actualizado.
    '''
    if colores is None:
        colores = []
    
    accesorio = {
        'activo': activo,
        'nombre': nombre,
        'descripcion': descripcion,
        'stock': stock,
        'precioUnitario': precioUnitario,
        'colores': colores
        }
    accesorios[codigo] = accesorio
    return accesorios

def listarAccesorios(accesorios):
    '''
        Imprime los detalles de los accesorios activos.
            Parámetros:
                accesorios (dict): Diccionario de accesorios.
    '''
    for codigo, accesorio in accesorios.items():
        print(f"Código: {codigo}")
        print(f"Activo: {accesorio['activo']}")
        if accesorio['activo'] == False:
            print("El accesorio no está activo.")
            print("-" * 40)
            continue
        print(f"Nombre: {accesorio['nombre']}")
        print(f"Descripción: {accesorio['descripcion']}")
        print(f"Stock: {accesorio['stock']}")
        print(f"Precio Unitario: ${accesorio['precioUnitario']:.2f}")
        print("Colores:")
        for claveColor, valorColor in accesorio['colores'].items():
            print(f"  {claveColor}: {valorColor}")
        print("-" * 40)
  
def eliminarAccesorios(accesorios,codigo):
    '''
        Elimina un accesorio del diccionario de accesorios.
        Parametros:
            accesorios (dict): Diccionario de accesorios.
            codigo (str): Código del accesorio a eliminar.
        Retorna:
            dict: El diccionario de accesorios actualizado.
    '''
    for clave in accesorios.keys():
        if clave == codigo:
            del accesorios[codigo]
            print(f"Accesorio con código {codigo} eliminado exitosamente.")
            return accesorios
    else:
       print(f"No se encontró un accesorio con el código {codigo}.")

def modificarAccesorio(accesorios: dict, codigo: str) -> dict:
    '''
        Modifica los detalles de un accesorio existente y si tocamos la tecla enter, esa variable no se modifica y queda como esta actualmente al ingreso.
        Parámetros:
            accesorio (dict): Diccionario de accesorios.
            codigo (str): Código del accesorio a modificar.
        Retorna:
            dict: El diccionario de accesorios actualizado.
    '''
    if codigo not in accesorios:
        print(f"No se encontró un accesorio con el código {codigo}.")
        return accesorios

    print("Ingrese datos a modificar. ENTER mantiene el valor actual.\n")
    datos = accesorios[codigo]

    parsers = {
        "activo":         parseBool,
        "stock":          parseInt,
        "precioUnitario": parseFloat,
        "colores":        parseColors,
    }

    for campo, valorActual in datos.items():
        if campo == "codigo":
            continue

        valorMostrado = (
            ", ".join(valorActual.values()) if campo == "colores" else valorActual
        )
        parseFn = parsers.get(campo, lambda x: x)
        datos[campo] = obtenerNuevoValor(obtenerEtiqueta(campo),
                                 valorMostrado,
                                 parseFn)

    print(f"\nAccesorio con código {codigo} modificado exitosamente.\n")
    return accesorios


def altaRenta(rentas):
    '''
        Agrega una renta al diccionario de rentas.
        Parámetros:
            rentas (dict): Diccionario de rentas.
        Retorna:
            dict: El diccionario de rentas actualizado.
    '''
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
        "fechaDevolucion": fechaDevolucion,
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
    '''
        Elimina una renta del diccionario de rentas.
        Parámetros:
            rentas (dict): Diccionario de rentas.
        Retorna:
            dict: El diccionario de rentas actualizado.
    '''
    print("--- Baja de Renta ---")
    idRenta = input("Ingrese ID de Renta a eliminar: ")
    if idRenta in rentas:
        del rentas[idRenta]
        print("Renta eliminada.")
    else:
        print("ERROR: No se encontró una renta con ese ID.")
    return rentas

def modificarRenta(rentas):
    """
    Modifica los datos de una renta existente.
    Si el ID no existe, informa error y no altera el dict.
    Args:
        rentas (dict): diccionario de rentas
    Returns:
        dict: el dict `rentas` actualizado
    """
    print("--- Modificar Renta ---")
    idRenta = input("Ingrese ID de Renta a modificar: ").strip()
    if idRenta not in rentas:
        print("ERROR: No se encontró una renta con ese ID.")
        return rentas

    renta = rentas[idRenta]
    print("Ingrese nuevos valores. ENTER mantiene el actual.\n")

    parsers = {
        "dias":    parseInt,
        "total":   parseFloat,
        "deposito": parseFloat,
    }

    for clave, valorActual in renta.items():
        if clave == "idRenta":
            continue
        parseFn = parsers.get(clave, lambda x: x)
        renta[clave] = obtenerNuevoValor(obtenerEtiqueta(clave), valorActual, parseFn)

    print(f"\nRenta {idRenta} modificada exitosamente.\n")
    return rentas

def listarRentas(rentas):
    '''
        Imprime los detalles de las rentas activas.
        Parámetros:
            rentas (dict): Diccionario de rentas.
    '''
    print("--- Listado de Rentas ---")
    if not rentas:
        print("No hay rentas registradas.")
        return

    print(f"{'ID':<5} {'Cliente':<10} {'Días':<5} {'F. Devolución':<20} {'Total':<10} {'Depósito':<10} {'Estado':<12} {'Pago':<13} {'Accesorio':<12} {'Cant.':<8}")
    print("-" * 112)

    for renta in rentas.values():
        print(f"{renta['idRenta']:<5} {renta['idCliente']:<10} {renta['dias']:<5} {renta['fechaDevolucion']:<20} {renta['total']:<10.2f} {renta['deposito']:<10.2f} {renta['estado']:<12} {renta['metodoPago']:<15} {renta['idAccesorio']:<10} {renta['cantidad']:<6}")

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

def modificarCliente(clientes: dict, documento: str) -> dict:
    """
    Modifica los datos de un cliente existente.
    Si se cambia 'idCliente', actualiza la clave principal del dict `clientes`.

    Args:
        clientes (dict): Diccionario global de clientes.
        documento (str): Documento (clave) del cliente a modificar.

    Returns:
        dict: El mismo dict `clientes` actualizado.
    """

    print("Ingrese datos a modificar. ENTER mantiene el valor actual.\n")
    cliente = clientes[documento]

    parsers = {
        "telefonos": parseTelefonos,
        "activo":    parseBool,
    }

    for clave, valorActual in list(cliente.items()):
        valorActual = (
            ", ".join(valorActual.values()) if clave == "telefonos" else valorActual
        )

        parseFn = parsers.get(clave, lambda x: x)
        nuevoValor = obtenerNuevoValor(obtenerEtiqueta(clave),
                               valorActual,
                               parseFn)

        if clave == "telefonos" and isinstance(nuevoValor, dict):
            cliente[clave] = nuevoValor
        else:
            cliente[clave] = nuevoValor

        # Si cambió idCliente, mover la entrada en el dict raíz
        if clave == "idCliente" and nuevoValor != documento:
            clientes[nuevoValor] = cliente
            del clientes[documento]
            documento = nuevoValor 

    print(f"\nCliente {documento} modificado exitosamente.\n")
    mostrarCliente(cliente, documento)
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
    accesorios = {
        '01': {
            "activo": True,
            "nombre": "Gafas de sol",
            "descripcion": "Gafas de sol con protección UV",
            "stock": 10,
            "precioUnitario": 25.99,
            "colores": {
                "color1": "rojo",
                "color2": "azul",
                "color3": "negro"
            }
        },
        '02': {
            "activo": True,
            "nombre": "Guantes térmicos",
            "descripcion": "Guantes resistentes al agua con forro interior",
            "stock": 15,
            "precioUnitario": 34.50,
            "colores": {
                "color1": "negro",
                "color2": "gris",
                "color3": "azul"
            }
        },
        '03': {
            "activo": True,
            "nombre": "Casco de ski",
            "descripcion": "Casco liviano con ventilación y ajuste regulable",
            "stock": 8,
            "precioUnitario": 89.99,
            "colores": {
                "color1": "blanco",
                "color2": "negro",
                "color3": "naranja"
            }
        },
        '04': {
            "activo": True,
            "nombre": "Pañuelo térmico",
            "descripcion": "Cuello polar para proteger del frío y viento",
            "stock": 20,
            "precioUnitario": 12.00,
            "colores": {
                "color1": "azul marino",
                "color2": "verde militar",
                "color3": "gris"
            }
        },
        '05': {
            "activo": True,
            "nombre": "Mochila impermeable",
            "descripcion": "Mochila de ski resistente al agua, 20L",
            "stock": 6,
            "precioUnitario": 59.90,
            "colores": {
                "color1": "negro",
                "color2": "rojo",
                "color3": "celeste"
            }
        },
        '06': {
            "activo": True,
            "nombre": "Antiparras profesionales",
            "descripcion": "Antiparras con doble lente y antiempañante",
            "stock": 12,
            "precioUnitario": 79.99,
            "colores": {
                "color1": "violeta",
                "color2": "negro",
                "color3": "verde"
            }
        },
        '07': {
            "activo": True,
            "nombre": "Cubrebotas",
            "descripcion": "Protector térmico y resistente al agua para botas",
            "stock": 18,
            "precioUnitario": 22.49,
            "colores": {
                "color1": "negro",
                "color2": "gris oscuro",
                "color3": "azul"
            }
        },
        '08': {
            "activo": True,
            "nombre": "Polainas",
            "descripcion": "Polainas ajustables para nieve y lluvia",
            "stock": 9,
            "precioUnitario": 27.75,
            "colores": {
                "color1": "verde oliva",
                "color2": "negro",
                "color3": "rojo"
            }
        },
        '09': {
            "activo": True,
            "nombre": "Cinturón porta objetos",
            "descripcion": "Cinturón con bolsillos para llevar celular, llaves y snack",
            "stock": 25,
            "precioUnitario": 14.30,
            "colores": {
                "color1": "gris",
                "color2": "azul",
                "color3": "negro"
            }
        },
        '10': {
            "activo": True,
            "nombre": "Protector solar de montaña",
            "descripcion": "Protección SPF 50+ resistente al agua y al sudor",
            "stock": 30,
            "precioUnitario": 9.90,
            "colores": {
                "color1": "único"
            }
        },
        '11': {
            "activo": True,
            "nombre": "Botella térmica",
            "descripcion": "Botella de acero inoxidable que conserva el calor",
            "stock": 14,
            "precioUnitario": 19.99,
            "colores": {
                "color1": "plateado",
                "color2": "azul",
                "color3": "negro"
            }
        }
    }

    rentas = {
        "01": {
            "idRenta": "01",
            "idCliente": "01",
            "dias": 10,
            "fechaDevolucion": "2025.06.10.12.00.00",
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
            "fechaDevolucion": "2025.06.05.15.30.00",
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
            "fechaDevolucion": "2025.06.12.09.45.00",
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
            "fechaDevolucion": "2025.06.03.18.00.00",
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
            "fechaDevolucion": "2025.06.20.20.00.00",
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
                    while True:
                        # Ingresar accesorio y el  -1 para terminar
                        codigo = input("Ingrese el código del accesorio (o '-1' para terminar): ")
                        if codigo == '-1':
                            break
                        while codigo in accesorios:
                            print("El accesorio ya existe. No se puede agregar.")
                            codigo = input("Ingrese un nuevo código para el accesorio: ")
                        activo = input("Ingrese True o False: ").lower()
                        if activo == "true":
                            activo = True
                        else:
                            activo = False
                        nombre = input("Ingrese el nombre del accesorio: ")
                        descripcion = input("Ingrese la descripción del accesorio: ")
                        stock = int(input("Ingrese el stock del accesorio: "))
                        precioUnitario = float(input("Ingrese el precio unitario del accesorio: "))
                        colores = input("Ingrese los colores del accesorio (separados por comas): ").split(',')
                        colores = {f'color{i+1}': color.strip() for i, color in enumerate(colores)}
                        # Agregar el accesorio al diccionario
                        altaAccesorio(accesorios, codigo,nombre, descripcion, stock, precioUnitario, colores, activo)
                        print("Accesorio agregado exitosamente.")

                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    # Modificar accesorio
                    codigoModificar = input("Ingrese el código del accesorio a modificar: ")
                    modificarAccesorio(accesorios, codigoModificar)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    # Eliminar accesorio
                    codigoEliminar = input("Ingrese el código del accesorio a eliminar: ")
                    eliminarAccesorios(accesorios, codigoEliminar)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    # Listar accesorios activos
                    listarAccesorios(accesorios)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
                
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
                    rentas = altaRenta(rentas)
                elif opcionSubmenu == "2":
                    rentas = bajaRenta(rentas)
                elif opcionSubmenu == "3":
                    rentas = modificarRenta(rentas)
                elif opcionSubmenu == "4":
                    listarRentas(rentas)

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
