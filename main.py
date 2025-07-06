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
from datetime import datetime, timedelta
import json
import os
import re

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def parse_string(x):
    return x.strip()

def parse_bool(x):
    return x.lower() == "true"

def es_bool_literal(x):
    return x.lower() in ("true", "false")

def parse_telefonos(x):
    if not x or not x.strip():
        return {}
    return {
        f"telefono{i+1}": t.strip()
        for i, t in enumerate(x.split(","))
        if t.strip()
    }

def validar_email(email):
    """
    Valida el formato del email usando regex.
    Args:
        email (str): Email a validar
    Returns:
        bool: True si el email es válido, False en caso contrario
    """
    try:
        pat = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pat, email) is not None
    except Exception as e:
        print(f"Error al validar email: {e}")
        return False
    
def validar_fecha(fecha):
    """
    Valida el formato de fecha YYYY-MM-DD.
    Args:
        fecha (str): Fecha a validar
    Returns:
        bool: True si la fecha es válida, False en caso contrario
    """
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    except Exception as e:
        print(f"Error al validar fecha: {e}")
        return False

def solicitar_input(prompt, validador=None, requerido=True):
    """
    Solicita input con validación opcional.
    Args:
        prompt: Mensaje a mostrar
        validador: Función que valida el input (opcional)
        requerido: Si el campo es requerido
    Returns:
        Valor validado o None si hay error
    """
    while True:
        try:
            valor = input(prompt).strip()

            if valor:
                if validador and not validador(valor):
                    print("Valor inválido. Intente nuevamente.")
                else:
                    return valor      # válido
            elif not requerido:
                return None          # opcional y vacío
            else:
                print("Este campo no puede estar vacío.")
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            return None
        except Exception as e:
            print(f"Error al leer entrada: {e}")
            return None


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
    tipoDocumento = solicitar_input("Ingrese el tipo de documento (DNI, Pasaporte, etc.): ", parse_string, requerido=True)
    nombre = solicitar_input("Ingrese el nombre del cliente: ", parse_string, requerido=True)
    apellido = solicitar_input("Ingrese el apellido del cliente: ", parse_string, requerido=True)
    email = solicitar_input("Ingrese el email del cliente: ", validar_email, requerido=True)
    fechaNacimiento = solicitar_input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ", validar_fecha, requerido=True)
    telefonosRaw = solicitar_input("Ingrese los teléfonos del cliente (separados por comas): ", parse_string, requerido=False)
    telefonos = parse_telefonos(telefonosRaw) if telefonosRaw else {}
    activo = solicitar_input("¿El cliente está activo? (True/False): ", es_bool_literal, requerido=True).lower() == "true"

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

def altaCliente(archivo):
    """
    Agrega uno o varios clientes al dict `clientes`, pidiendo datos por consola.
    Args:
        archivo (str): Nombre del archivo de clientes.
    Returns:
        None
    """
    try:
        try:
            f = open(archivo, "r", encoding="utf-8")
            clientes = json.load(f)
            f.close()
            if clientes is None:
                clientes = {}
        except (FileNotFoundError): 
            clientes = {}
        while True:
            documento = solicitar_input("Ingrese el documento del cliente (o -1 para terminar): ", parse_string, requerido=True)
            if documento == '-1':
                break
            if documento in clientes:
                print("El cliente ya existe. Intente con otro documento.")  
            else:
                cliente = obtenerDatosCliente(documento)
                clientes[documento] = cliente
                print(f"Cliente {documento} agregado.")
        f = open(archivo, mode='w', encoding='utf-8')
        json.dump(clientes, f, ensure_ascii=False, indent=4)
        f.close()

    except(OSError) as error:
        print("Error al intentar abrir archivo(s):", error)    
    
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

def listarClientes(archivo):
    """
    Muestra por consola todos los clientes que estén activos.
    Args:
        archivo (str): Nombre del archivo de clientes.
    Returns:
        None
    """

    try:
        f = open(archivo, mode='r', encoding='utf-8')
        clientes = json.load(f)
        f.close()
        if clientes is None:
            print("No hay clientes activos.")
            return
        else:
            print("Listado de clientes activos:")
            for idCliente, cliente in clientes.items():
                if  cliente.get('activo', True):
                    mostrarCliente(cliente, idCliente)
    except FileNotFoundError:
        print("No hay clientes activos.")
    except OSError as e:
        print("Error al intentar abrir archivo(s):", e)

def eliminarCliente(archivo, documento):
    """
    Elimina el cliente con el documento dado si es que existe.
    Args:
        archivo (str): Nombre del archivo de clientes.
        documento (str): Documento del cliente a eliminar.
    Returns:
        None
    """
    try:
        f = open(archivo, mode='r', encoding='utf-8')
        clientes = json.load(f)
        f.close()

        if documento in clientes:
            clientes[documento]['activo'] = False
            f = open(archivo, mode='w', encoding='utf-8')
            json.dump(clientes, f, ensure_ascii=False, indent=4)
            f.close()
            print(f"Cliente con documento {documento} eliminado exitosamente.")
        else:
            print(f"El cliente con documento {documento} ya estaba inactivo.")
    except(FileNotFoundError, OSError) as error:
        print("Error al intentar abrir archivo(s):", error)    

def leerCampo(label, valorActual, parseFn):
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
    entrada = input(f"{label} (actual: {str(valorActual)}): ").strip()
    if entrada == "":
        return valorActual
    return parseFn(entrada)

def modificarCliente(archivo, documento):
    """
    Modifica los datos de un cliente existente.
    Si se modifica el 'idCliente', actualiza la clave del dict `clientes`.
    Args:
        archivo (str): Nombre del archivo de clientes.
        documento (str): Documento del cliente a modificar.
    Returns:
        dict: El dict `clientes` actualizado.
    """
    try:
        f = open(archivo, mode='r', encoding='utf-8')
        clientes = json.load(f)
        f.close()

        if documento not in clientes:
            print(f"No se encontró un cliente con el documento {documento}.")
            return
        else:
            print("Ingrese datos a modificar, presione ENTER para mantener el valor actual.")
            datos = clientes[documento]
        
            nuevoDoc = leerCampo("Ingrese nuevo documento", datos['idCliente'], parse_string)
            if nuevoDoc != datos['idCliente']:
                datos['idCliente'] = nuevoDoc
                clientes[nuevoDoc] = datos
                del clientes[documento]
                documento = nuevoDoc  

            telefonosActual = ", ".join(datos['telefonos'].values())
            nuevosTel= leerCampo("Teléfonos", telefonosActual, parse_telefonos)
            if isinstance(nuevosTel, dict):  
                datos['telefonos'] = nuevosTel 

            datos['tipoDocumento']  = leerCampo("Tipo de documento",   datos['tipoDocumento'], parse_string)
            datos['nombre']        = leerCampo("Nombre",              datos['nombre'], parse_string)
            datos['apellido']      = leerCampo("Apellido",            datos['apellido'], parse_string)
            datos['email']         = leerCampo("Email",               datos['email'], parse_string)
            datos['fechaNacimiento'] = leerCampo("Fecha de nacimiento (YYYY-MM-DD)", datos['fechaNacimiento'], parse_string)
            activoNuevo = leerCampo(
                "¿Está activo? (True/False)",
                "true" if datos["activo"] else "false",
                parse_string
            )
            datos["activo"] = activoNuevo.lower() == "true"

            print(f"\nValor actualizado de cliente {documento}:\n")
            mostrarCliente(datos, documento)
            confirmacion = input("Ingrese 1 para confirmar, 0 para cancelar: ")
            if confirmacion == "1":
                f = open(archivo, mode='w', encoding='utf-8')
                json.dump(clientes, f, ensure_ascii=False, indent=4)
                f.close()
                print(f"Cliente {documento} modificado exitosamente.")
            else:
                print(f"Cliente {documento} no modificado.")
    
    except(FileNotFoundError, OSError) as error:
        print("Error al intentar abrir archivo(s):", error)    


def altaAccesorio(archivo,accesorios,codigo,nombre, descripcion, stock, precioUnitario, colores=None, activo=True):
    '''
        
    '''
    try:
        f = open(archivo, mode='r', encoding='utf-8')
        accesorio = json.load(f)
        f.close()

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
        
        f = open(archivo, mode='w', encoding='utf-8')
        json.dump(accesorios, f, ensure_ascii=False, indent=4)
        f.close()

    except(FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def listarAccesorios(archivo):
    '''
        
    '''
    try:
        f = open(archivo, mode='r', encoding='utf-8')
        accesorio = json.load(f)
        f.close()

        for codigo, accesorio in accesorio.items():
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
    
    except(FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def eliminarAccesorios(archivo,codigo):
    '''
      
    '''
    try:
        f = open(archivo, mode='r', encoding='utf-8')
        accesorios = json.load(f)
        f.close()

        if codigo in accesorios:
            if accesorios[codigo]['activo'] == False:
                print(f"El accesorio con código {codigo} ya estaba inactivo.")
            else:
                accesorios[codigo]['activo'] = False
                f = open(archivo, mode='w', encoding='utf-8')
                json.dump(accesorios, f, ensure_ascii=False, indent=4)
                f.close()
                print(f"Accesorio con código {codigo} marcado como inactivo.")
        else:
            print(f"No se encontró un accesorio con el código {codigo}.")
    
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def modificarAccesorio(archivo, codigo):
    '''
        
    '''
    try:
        f = open(archivo, mode='r', encoding='utf-8')
        accesorio = json.load(f)
        f.close()

    except (FileNotFoundError, OSError) as e:
        print("No se pudo abrir el archivo:", e)
        return
    
    if codigo in accesorio:
        datosActuales = accesorio[codigo]
        
        activoEstado = input(f"Ingrese True o False (actual: {datosActuales['activo']}): ").lower()
        if activoEstado == "":
            activo = datosActuales['activo']
        else:
            activo = True if activoEstado == "true" else False

        nombre = input(f"Ingrese el nombre del accesorio (actual: {datosActuales['nombre']}): ")
        if nombre == "":
            nombre = datosActuales['nombre']

        descripcion = input(f"Ingrese la descripción del accesorio (actual: {datosActuales['descripcion']}): ")
        if descripcion == "":
            descripcion = datosActuales['descripcion']

        while True:
            stockInput = input(f"Ingrese el stock del accesorio (actual: {datosActuales['stock']}): ")
            if stockInput == "":
                stock = datosActuales['stock']
                break
            try: 
                stock = int(stockInput)
                if stock < 0:
                    raise ValueError
                break
            except ValueError:
                print("Stock invalido. Ingrese un numero entero mayor o igual a 0")
                

        while True:
            precioInput = input(f"Ingrese el precio unitario del accesorio (actual: {datosActuales['precioUnitario']}): ")
            if precioInput == "":
                precioUnitario = datosActuales['precioUnitario']
                break
            try:
                precioUnitario = float(precioInput)
                if precioUnitario < 0:
                    raise ValueError
                break
            except ValueError:
                print("Precio inválido. Ingrese un número positivo.")

        coloresInput = input(f"Ingrese los colores del accesorio separados por coma (actual: {list(datosActuales['colores'].values())}): ")
        if coloresInput == "":
            colores = datosActuales['colores']
        else:
            colores = {f'color{i+1}': color.strip() for i, color in enumerate(coloresInput.split(','))}

        accesorio[codigo] = {
            'activo': activo,
            'nombre': nombre,
            'descripcion': descripcion,
            'stock': stock,
            'precioUnitario': precioUnitario,
            'colores': colores
        }
        
        try:
            f = open(archivo, mode='w', encoding='utf-8')
            json.dump(accesorio, f, ensure_ascii=False, indent=4)
            f.close()
            print(f"Accesorio con código {codigo} modificado exitosamente.")
        except (FileNotFoundError, OSError) as e:
            print("No se pudo guardar el archivo:", e)

    else:
        print(f"No se encontró un accesorio con el código {codigo}.")
    return 

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
    
def cargarRentasDesdeArchivo(nombre_archivo):
    try:
        f = open(nombre_archivo, mode='r', encoding='utf-8')
        rentas = json.load(f)
        f.close()
        return rentas
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def guardarRentasEnArchivo(nombre_archivo, rentas):
    try:
        f = open(nombre_archivo, mode='w', encoding='utf-8')
        json.dump(rentas, f, ensure_ascii=False, indent=4)
        f.close()
    except Exception as e:
        print(f"Error al guardar rentas: {e}")

def altaRenta(accesorios):
    """
        Registra una nueva renta:
        - Verifica si el ID ya existe
        - Calcula fecha de devolución y total
        - Valida stock y actualiza inventario
        - Guarda la renta en rentas.json
    """

    rentas = cargarRentasDesdeArchivo("rentas.json")
    print("--- Alta de Renta ---")
    idRenta = input("Ingrese ID de Renta: ")
    if idRenta in rentas:
        print("ERROR: Ya existe una renta con ese ID.")
        return

    idCliente = input("Ingrese ID de Cliente: ")

    try:
        dias = int(input("Ingrese cantidad de días: "))
    except ValueError:
        print("Cantidad de días inválida.")
        return

    idAccesorio = input("Ingrese ID de Accesorio: ")
    if idAccesorio not in accesorios:
        print("ERROR: Accesorio no encontrado.")
        return

    try:
        cantidad = int(input("Ingrese cantidad: "))
    except ValueError:
        print("Cantidad inválida.")
        return

    try:
        stockDisponible = int(accesorios[idAccesorio].get("stock", 0))
    except (ValueError, KeyError):
        print("Error al leer stock disponible.")
        return

    if cantidad > stockDisponible:
        print(f"No hay suficiente stock. Disponible: {stockDisponible}")
        return

    fechaDevolucion = (datetime.now() + timedelta(days=dias)).strftime("%Y.%m.%d.%H.%M.%S")

    try:
        precioUnitario = float(accesorios[idAccesorio].get("precioUnitario", 0))
    except (ValueError, KeyError):
        print("Error al leer precio unitario.")
        return

    total = cantidad * precioUnitario * dias

    try:
        deposito = float(input("Ingrese depósito: "))
    except ValueError:
        print("Depósito inválido.")
        return

    estado = input("Ingrese estado: ")
    metodoPago = input("Ingrese método de pago: ")

    accesorios[idAccesorio]["stock"] = stockDisponible - cantidad

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
        "cantidad": str(cantidad)
    }

    guardarRentasEnArchivo("rentas.json", rentas)
    print("Renta registrada exitosamente.")
    print(f"Fecha de devolución calculada: {fechaDevolucion}")
    print(f"Total calculado automáticamente: ${total:.2f}")
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------

    """
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
        },
        '23456789': {
            "idCliente": "23456789",
            "tipoDocumento": "DNI",
            "nombre": "Carlos",
            "apellido": "Rodríguez",
            "email": "carlos.rodriguez@hotmail.com",
            "fechaNacimiento": "1985-03-15",
            "telefonos": {
                "telefono1": "234567890",
                "telefono2": "876543210"
            },
            "activo": True
        },
        '34567890': {
            "idCliente": "34567890",
            "tipoDocumento": "DNI",
            "nombre": "María",
            "apellido": "López",
            "email": "maria.lopez@yahoo.com",
            "fechaNacimiento": "1992-07-22",
            "telefonos": {
                "telefono1": "345678901",
                "telefono2": "765432109"
            },
            "activo": True
        },
        '45678901': {
            "idCliente": "45678901",
            "tipoDocumento": "DNI",
            "nombre": "Roberto",
            "apellido": "Fernández",
            "email": "roberto.fernandez@gmail.com",
            "fechaNacimiento": "1988-11-08",
            "telefonos": {
                "telefono1": "456789012",
                "telefono2": "654321098"
            },
            "activo": True
        },
        '56789012': {
            "idCliente": "56789012",
            "tipoDocumento": "DNI",
            "nombre": "Laura",
            "apellido": "Martínez",
            "email": "laura.martinez@outlook.com",
            "fechaNacimiento": "1995-04-30",
            "telefonos": {
                "telefono1": "567890123",
                "telefono2": "543210987"
            },
            "activo": False
        },
        '67890123': {
            "idCliente": "67890123",
            "tipoDocumento": "DNI",
            "nombre": "Diego",
            "apellido": "García",
            "email": "diego.garcia@gmail.com",
            "fechaNacimiento": "1987-09-14",
            "telefonos": {
                "telefono1": "678901234",
                "telefono2": "432109876"
            },
            "activo": True
        },
        '78901234': {
            "idCliente": "78901234",
            "tipoDocumento": "DNI",
            "nombre": "Sofía",
            "apellido": "Hernández",
            "email": "sofia.hernandez@hotmail.com",
            "fechaNacimiento": "1993-12-05",
            "telefonos": {
                "telefono1": "789012345",
                "telefono2": "321098765"
            },
            "activo": True
        },
        '89012345': {
            "idCliente": "89012345",
            "tipoDocumento": "DNI",
            "nombre": "Miguel",
            "apellido": "Torres",
            "email": "miguel.torres@yahoo.com",
            "fechaNacimiento": "1991-06-18",
            "telefonos": {
                "telefono1": "890123456",
                "telefono2": "210987654"
            },
            "activo": True
        },
        '90123456': {
            "idCliente": "90123456",
            "tipoDocumento": "DNI",
            "nombre": "Valentina",
            "apellido": "Silva",
            "email": "valentina.silva@gmail.com",
            "fechaNacimiento": "1994-02-25",
            "telefonos": {
                "telefono1": "901234567",
                "telefono2": "109876543"
            },
            "activo": True
        }
    }
    
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
        },
        "06": {
            "idRenta": "06",
            "idCliente": "06",
            "dias": 8,
            "fecha Devolucion": "2025.06.14.14.00.00",
            "total": 9600.0,
            "deposito": 12000.0,
            "estado": "ocupado",
            "metodoPago": "efectivo",
            "idAccesorio": "01",
            "cantidad": "12"
        },
        "07": {
            "idRenta": "07",
            "idCliente": "07",
            "dias": 4,
            "fecha Devolucion": "2025.06.06.17.00.00",
            "total": 3200.0,
            "deposito": 4000.0,
            "estado": "pendiente",
            "metodoPago": "tarjeta",
            "idAccesorio": "02",
            "cantidad": "4"
        },
        "08": {
            "idRenta": "08",
            "idCliente": "08",
            "dias": 6,
            "fecha Devolucion": "2025.06.11.10.30.00",
            "total": 7800.0,
            "deposito": 10000.0,
            "estado": "finalizado",
            "metodoPago": "efectivo",
            "idAccesorio": "03",
            "cantidad": "6"
        },
        "09": {
            "idRenta": "09",
            "idCliente": "09",
            "dias": 2,
            "fecha Devolucion": "2025.06.02.13.00.00",
            "total": 2600.0,
            "deposito": 3000.0,
            "estado": "cancelado",
            "metodoPago": "transferencia",
            "idAccesorio": "05",
            "cantidad": "2"
        },
        "10": {
            "idRenta": "10",
            "idCliente": "10",
            "dias": 9,
            "fecha Devolucion": "2025.06.15.16.00.00",
            "total": 11700.0,
            "deposito": 15000.0,
            "estado": "ocupado",
            "metodoPago": "tarjeta",
            "idAccesorio": "04",
            "cantidad": "13"
        }
    }

    """
    accesorios = leerArchivo("accesorios.json") or {}
    archivoJSONAccesorios = "accesorios.json"
    archivoJSONClientes = "clientes.json"



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
                    print("[4] Listar Clientes")
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
                    altaCliente(archivoJSONClientes) 
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    documento = input("Ingrese el documento del cliente a modificar: ")
                    modificarCliente(archivoJSONClientes, documento)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    documento = input("Ingrese el documento del cliente a eliminar: ")
                    eliminarCliente(archivoJSONClientes, documento)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    listarClientes(archivoJSONClientes)

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
                        # Ingresar accesorio y el -1 para terminar
                        codigo = input("Ingrese el código del accesorio (o '-1' para terminar): ")
                        if codigo == '-1':
                            break
                        while codigo in accesorios:
                            print("El accesorio ya existe. No se puede agregar.")
                            codigo = input("Ingrese un nuevo código para el accesorio: ")
                        
                        activo = input("Ingrese True o False: ").strip().lower()
                        while activo not in ['true', 'false']:
                            activo = input("Entrada invalida. Ingrese 'True o 'False: ").strip().lower()
                        activo = (activo == "true") 
                        
                        nombre = input("Ingrese el nombre del accesorio: ").strip()
                        while nombre == "":
                            nombre = input("El nombre no puede estar vacio. Ingrese el nombre del accesorio: ").strip()
                        
                        descripcion = input("Ingrese la descripción del accesorio: ").strip()
                        while descripcion == "":
                            descripcion = input("Ingrese la descripción del accesorio: ").strip()
                        
                        while True: 
                            try: 
                                stock = int(input("Ingrese el stock del accesorio: "))
                                if stock < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                print("Stock invalido. Ingrese un numero entero mayor o igual a 0")
                        
                        while True: 
                            try: 
                                precioUnitario = float(input("Ingrese el precio unitario del accesorio: "))
                                if precioUnitario < 0:
                                    raise ValueError
                                break
                            except ValueError:
                                print("Precio Invalido. Ingrese un numero positivo")
                        
                        colores = input("Ingrese los colores del accesorio (separados por comas): ").split(',')
                        colores = {f'color{i+1}': color.strip() for i, color in enumerate(colores)}
                        
                        # Agregar el accesorio al diccionario
                        altaAccesorio(archivoJSONAccesorios, accesorios, codigo,nombre, descripcion, stock, precioUnitario, colores, activo)
                        print("Accesorio agregado exitosamente.")

                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    # Modificar accesorio
                    codigoModificar = input("Ingrese el código del accesorio a modificar: ")
                    modificarAccesorio(archivoJSONAccesorios, codigoModificar)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    # Eliminar accesorio
                    codigoEliminar = input("Ingrese el código del accesorio a eliminar: ")
                    eliminarAccesorios(archivoJSONAccesorios, codigoEliminar)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    # Listar accesorios activos
                    listarAccesorios(archivoJSONAccesorios)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE RENTAS")
                    print("---------------------------")
                    print("[1] Ingresar Renta")
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
                    altaRenta(accesorios)
                input("\nPresione ENTER para volver al menú.")
                print("\n\n")
        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            ...

        elif opcionMenuPrincipal == "5":   # Opción 5 del menú principal
            ...

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()