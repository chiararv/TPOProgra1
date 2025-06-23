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
from datetime import datetime

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def obtenerDatosRegistro(plantilla, parsers=None):
    """
    Pide por consola los valores de cada campo en 'plantilla' y devuelve
    un nuevo diccionario completo.

    Args:
        plantilla (dict): claves = nombre de campo; valores = valor actual
                          (None si es un registro nuevo).
        parsers  (dict):  campo -> función de conversión (opcional).

    Returns:
        dict: Registro con todos los campos completados.
    """
    if parsers is None:
        parsers = {}

    nuevo = {}
    for campo, valorActual in plantilla.items():
        etiqueta = obtenerEtiqueta(campo)

        # Para sub-dicts como 'telefonos' o 'colores' mostramos los valores separados por coma
        if isinstance(valorActual, dict):
            valorMostrado = ", ".join(valorActual.values())
        else:
            valorMostrado = valorActual if valorActual is not None else ""

        if valorActual is None:                       # Alta
            entrada = input(f"{etiqueta}: ").strip()
        else:                                         # Modificación
            entrada = input(f"{etiqueta} (actual: {valorMostrado}) ➜ ").strip()

        # Elegir valor a guardar
        if entrada == "" and valorActual is not None:
            nuevoValor = valorActual                  # ENTER mantiene el valor actual
        else:
            parseFn = parsers.get(campo, lambda x: x)
            nuevoValor = parseFn(entrada)

        nuevo[campo] = nuevoValor

    return nuevo

def parseBool(x):
    """convierte string a boolean"""
    return x.lower() == "true"

def parseInt(x): 
    """convierte string a entero"""
    return int(x)

def parseFloat(x): 
    """convierte string a float"""
    return float(x)

def parseDateTimeToString(x):
    """convierte string a fecha y hora en formato 'AAAA.MM.DD.hh.mm.ss'"""
    dt = datetime.strptime(x, "%Y-%m-%d %H:%M:%S")  
    return dt.strftime("%Y.%m.%d.%H.%M.%S")

def parseTelefonos(x):
    """convierte números de teléfono separados por coma a un diccionario"""
    telefonosLimpios = [t.strip() for t in x.split(',') if t.strip()]
    return {f"telefono{i + 1}": tel for i, tel in enumerate(telefonosLimpios)}

def parseColors(texto: str) -> dict:
    """convierte colores separados por coma a un diccionario"""
    coloresLimpios = [c.strip() for c in texto.split(',') if c.strip()]
    return {f"color{i + 1}": col for i, col in enumerate(coloresLimpios)}

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
        "idRenta":        "ID de Renta (AAAA-MM-DD hh:mm:ss)",
        "dias":           "Cantidad de días",
        "fechaDevolucion":"Fecha de devolución (AAAA-MM-DD hh:mm:ss)",
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

def altaAccesorio(accesorios):
    '''
        Agrega uno o varios accesorios al diccionario de accesorios.
            Parámetros:
                accesorios (dict):
            Retorna:
                dict: El diccionario de accesorios actualizado.
    '''
    while True:
        codigo = input("Ingrese el código del accesorio (o -1 para terminar): ")
        if codigo == '-1':
            break
        if codigo in accesorios:
            print("ERROR: Ya existe un accesorio con ese código.")
            continue

        plantilla = {
            "activo": None,
            "nombre": None,
            "descripcion": None,
            "stock": None,
            "precioUnitario": None,
            "colores": None
        }
        parsers = {
            "stock": parseInt,
            "precioUnitario": parseFloat,
            "colores": parseColors
        }
        
        accesorios[codigo] = obtenerDatosRegistro(plantilla, parsers)
        print(f"Accesorio con código {codigo} agregado.")
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
        if not accesorio['activo']:
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
    if codigo in accesorios:
        del accesorios[codigo]
        print(f"Accesorio con código {codigo} eliminado exitosamente.")
    else:
        print(f"No se encontró un accesorio con el código {codigo}.")
    return accesorios

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

    parsers = {
        "activo":         parseBool,
        "stock":          parseInt,
        "precioUnitario": parseFloat,
        "colores":        parseColors,
    }
    accesorios[codigo] = obtenerDatosRegistro(accesorios[codigo], parsers)
    print(f"\nAccesorio con código {codigo} modificado exitosamente.\n")
    return accesorios

def altaRenta(rentas):
    '''
        Agrega una o varias rentas al diccionario de rentas.
        Parámetros:
            rentas (dict): Diccionario de rentas.
        Retorna:
            dict: El diccionario de rentas actualizado.
    '''
    print("--- Alta de Renta ---")
    while True:
        idRenta = input("Ingrese ID de Renta (o -1 para terminar): ")
        if idRenta == '-1':
            break
        if idRenta in rentas:
            print("ERROR: Ya existe una renta con ese ID.")
            continue

        plantilla = {
            "idCliente":       None,
            "dias":            None,
            "fechaDevolucion": None,
            "total":           None,
            "deposito":        None,
            "estado":          None,
            "metodoPago":      None,
            "idAccesorio":     None,
            "cantidad":        None
        }

        parsers = {
            "dias":     parseInt,
            "total":    parseFloat,
            "deposito": parseFloat,
            "cantidad": parseInt,
            "fechaDevolucion": parseDateTimeToString
        }
        rentas[idRenta] = obtenerDatosRegistro(plantilla, parsers)
        rentas[idRenta]["idRenta"] = parseDateTimeToString(idRenta)
        print(f"Renta {idRenta} registrada exitosamente.")
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

    print("Ingrese nuevos valores. ENTER mantiene el actual.\n")

    parsers = {
        "dias":    parseInt,
        "total":   parseFloat,
        "deposito": parseFloat,
    }

    rentas[idRenta] = obtenerDatosRegistro(rentas[idRenta], parsers)

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

    print(f"{'ID':<20} {'Cliente':<10} {'Días':<5} {'F. Devolución':<20} {'Total':<10} {'Depósito':<10} {'Estado':<12} {'Pago':<13} {'Accesorio':<12} {'Cant.':<8}")
    print("-" * 128)

    for renta in rentas.values():
        print(f"{renta['idRenta']:<20} {renta['idCliente']:<10} {renta['dias']:<5} {renta['fechaDevolucion']:<20} {renta['total']:<10.2f} {renta['deposito']:<10.2f} {renta['estado']:<12} {renta['metodoPago']:<15} {renta['idAccesorio']:<10} {renta['cantidad']:<6}")

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
        plantilla = {
            "tipoDocumento":  None,
            "nombre":         None,
            "apellido":       None,
            "email":          None,
            "fechaNacimiento":None,
            "telefonos":      None,
            "activo":         None
        }
        parsers = {
            "telefonos": parseTelefonos,
            "activo":    parseBool
        }
        clientes[documento] = obtenerDatosRegistro(plantilla, parsers)
        clientes[documento]["idCliente"] = documento
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
    Si se cambia 'idCliente', actualiza la clave principal en `clientes`.
    Parámetros:
        clientes (dict): Diccionario de clientes.
        documento (str): Documento del cliente a modificar.
    Retorna:
        dict: El dict `clientes` actualizado.
    """

    print("Ingrese datos a modificar. ENTER mantiene el valor actual.\n")

    parsers = {
        "telefonos": parseTelefonos,
        "activo":    parseBool,
    }

    clienteActual   = clientes[documento]
    clienteEditado  = obtenerDatosRegistro(clienteActual, parsers)

    nuevoDoc = clienteEditado["idCliente"]

    if nuevoDoc != documento:
        if nuevoDoc in clientes:
            print(f"ERROR: ya existe un cliente con documento {nuevoDoc}.")
            return clientes          
        del clientes[documento]
        clientes[nuevoDoc] = clienteEditado
        print(f"\nDocumento actualizado de {documento} ➜ {nuevoDoc}.\n")
    else:
        clientes[documento] = clienteEditado
        print(f"\nCliente {documento} modificado exitosamente.\n")

    mostrarCliente(clienteEditado, nuevoDoc)
    return clientes

def mostrarTablaRenta(rentas):
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
    totalAncho = sum(anchos.values()) + (4 * len(columnas)) + 3
    print("-" * totalAncho)

    # Filas
    for campo in campos:
        print(campo.ljust(anchos["Campo"]), end=" || ")
        for col in columnas:
            valor = str(rentas[col].get(campo, ""))
            print(valor.center(anchos[col]), end=" || ")
        print()


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
    Muestra el recuento de accesorios por mes en formato de tabla.
    
    Args:
        recuento (dict): Diccionario con el recuento de accesorios por mes
    """
    if not recuento:
        print("No hay datos de accesorios para mostrar.")
        return
    
    # Obtener todos los idAccesorios y ordenarlos
    idAccesorios = sorted(recuento.keys())
    meses = list(range(1, 13))
    
    # Calcular anchos de columnas
    anchoId = max(len("Accesorio"), max(len(id) for id in idAccesorios)) + 2
    anchoMes = 8  # Suficiente para "Mes X" y los valores
    
    # Encabezado
    print("Accesorio".ljust(anchoId), end=" || ")
    for mes in meses:
        print(f"Mes {mes}".center(anchoMes), end=" || ")
    print()
    
    # Separador
    totalAncho = anchoId + (len(meses) * (anchoMes + 4)) + 3
    print("-" * totalAncho)
    
    # Filas de datos
    for idAccesorio in idAccesorios:
        print(idAccesorio.ljust(anchoId), end=" || ")
        for mes in meses:
            cantidad = recuento[idAccesorio].get(mes, 0)
            print(str(cantidad).center(anchoMes), end=" || ")
        print()

def generarMatrizDineroPorMes(rentas):
    """
    Genera una matriz de depósitos por mes.
    
    Args:
        rentas (dict): Diccionario con todas las rentas
    
    Returns:
        tuple: (matriz, idClientes, meses)
          - matriz: Lista de listas con los depósitos sumados
          - idClientes: Lista ordenada de ids de clientes
          - meses: Lista de meses (1-12)
    """
    # Recolecta todos los idClientes únicos (para las filas)
    idClientes = sorted(set(renta["idCliente"] for renta in rentas.values()))
    meses = list(range(1, 13))
    
    # Inicializa la matriz con ceros
    matriz = [[0 for _ in meses] for _ in idClientes]
    
    # Llena la matriz con los depósitos
    for renta in rentas.values():
        try:
            mes = int(renta["idRenta"].split('.')[1])
            idCliente = renta["idCliente"]
            deposito = float(renta["deposito"])
            
            fila = idClientes.index(idCliente)
            columna = meses.index(mes)
            matriz[fila][columna] += deposito
        except Exception as e:
            print(f"Error procesando renta {renta.get('idRenta', '')}: {e}")
        
    # Añadir fila de subtotales
    subtotales = [sum(fila[mes] for fila in matriz) for mes in range(len(meses))]
    matriz.append(subtotales)
    idClientes.append("SUBTOTAL")  # Etiqueta para la fila adicional
    
    return matriz, idClientes, meses

def mostrarMatrizDinero(matriz, idClientes, meses):
    """
    Muestra la matriz de depósitos por mes en formato de tabla.
    """
    if not matriz or not idClientes:
        print("No hay datos de depósitos para mostrar.")
        return
    
    # Calcular anchos de columnas
    anchoId = max(len("Cliente"), max(len(id) for id in idClientes)) + 2
    anchoMes = 10  # Ajustado para valores como ej "30000.00"
    
    # Encabezado (usando "Plos" en lugar de "Mes")
    print("Cliente".ljust(anchoId), end=" || ")
    for mes in meses:
        print(f"Plos {mes}".center(anchoMes), end=" || ")
    print()
    
    # Separador
    totalAncho = anchoId + (len(meses) * (anchoMes + 4)) + 3
    print("-" * totalAncho)
    
    # Filas de datos
    for i, idCliente in enumerate(idClientes):
        print(idCliente.ljust(anchoId), end=" || ")
        for j, mes in enumerate(meses):
            # Formatear todos los valores con 2 decimales y ancho fijo
            valor = matriz[i][j]
            dinero = f"{valor:.2f}" if valor != 0 else "0.00"
            # Asegurar que SUBTOTAL tenga el mismo formato
            if idCliente == "SUBTOTAL":
                dinero = dinero.center(anchoMes)  # Forzar alineación central
            print(dinero.center(anchoMes), end=" || ")
        print()


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
            "idRenta": "2025.06.03.18.00.00",
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
            "idRenta": "2025.06.04.18.00.00",
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
            "idRenta": "2025.06.05.18.00.00",
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
            "idRenta": "2025.06.06.18.00.00",
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
            "idRenta": "2025.06.07.18.00.00",
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
                    altaAccesorio(accesorios)
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
                    mostrarTablaRenta(rentas)
                elif opcionSubmenu == "2":
                    informeMesActual(rentas)
                elif opcionSubmenu == "3":
                    informeMesEspecifico(rentas)
                elif opcionSubmenu == "4":
                    recuento = recuentoAccesoriosPorMes(rentas)
                    mostrarRecuentoAccesorios(recuento)
                elif opcionSubmenu == "5":
                    matriz, ids, meses = generarMatrizDineroPorMes(rentas)
                    mostrarMatrizDinero(matriz, ids, meses)

        elif opcionMenuPrincipal == "5":
            ...

        if opcionSubmenu != "0":
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

main()