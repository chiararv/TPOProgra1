
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

def altaAccesorio(accesorios,codigo,nombre, descripcion, stock, precioUnitario, colores=None, activo=True):
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

def modificarAccesorio(accesorio, codigo):
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

def listarAccesorios(accesorios):
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
    for clave in accesorios.keys():
        if clave == codigo:
            del accesorios[codigo]
            print(f"Accesorio con código {codigo} eliminado exitosamente.")
            return accesorios
    else:
       print(f"No se encontró un accesorio con el código {codigo}.")


while True:
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
    
    altaAccesorio(accesorios, codigo,nombre, descripcion, stock, precioUnitario, colores, activo)
    print("Accesorio agregado exitosamente.")

listarAccesorios(accesorios)

codigoEliminar = input("Ingrese el código del accesorio a eliminar: ")
eliminarAccesorios(accesorios, codigoEliminar)
listarAccesorios(accesorios)

codigoModificar = input("Ingrese el código del accesorio a modificar: ")
modificarAccesorio(accesorios, codigoModificar)
listarAccesorios(accesorios)