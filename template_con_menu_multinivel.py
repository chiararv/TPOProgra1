"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaCliente(_clientes):
    ...
    return _clientes

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

def modificarAccesorio(accesorio, codigo):
    '''
        Modifica los detalles de un accesorio existente y si tocamos la tecla enter, esa variable no se modifica y queda como esta actualmente al ingreso.
        Parámetros:
            accesorio (dict): Diccionario de accesorios.
            codigo (str): Código del accesorio a modificar.
        Retorna:
            dict: El diccionario de accesorios actualizado.
    '''
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

        stockInput = input(f"Ingrese el stock del accesorio (actual: {datosActuales['stock']}): ")
        if stockInput == "":
            stock = datosActuales['stock']
        else:
            stock = int(stockInput)

        precioInput = input(f"Ingrese el precio unitario del accesorio (actual: {datosActuales['precioUnitario']}): ")
        if precioInput == "":
            precioUnitario = datosActuales['precioUnitario']
        else:
            precioUnitario = float(precioInput)

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
        print(f"Accesorio con código {codigo} modificado exitosamente.")
    else:
        print(f"No se encontró un accesorio con el código {codigo}.")

    return accesorio



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    clientes = {...}

    # Diccionario de accesorios con algunos ejemplos
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
                    print("[2] Opción 2")
                    print("[3] Opción 3")
                    print("[4] Opción 4")
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
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ...
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ...
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ...

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