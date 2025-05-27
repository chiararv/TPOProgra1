def altaAccesorio(accesorios,codigo,nombre, descripcion, stock, precioUnitario, colores=None, activo=True):
    if colores is None:
        colores = []
    
    accesorio = {
        'activo': activo,
        'nombre': nombre,
        'Descripcion': descripcion,
        'Stock': stock,
        'PrecioUnitario': precioUnitario,
        'Colores': colores
        }
    accesorios[codigo] = accesorio
    return accesorios
    
    
accesorios = {
    '01': {
        "activo": True,
        "nombre": "Gafas de sol",
        "Descripcion": "Gafas de sol con protección UV",
        "Stock": 10,
        "PrecioUnitario": 25.99,
        "Colores": {
            "color1": "rojo",
            "color2": "azul",
            "color3": "negro"
        }
    },
    '02': {
        "activo": True,
        "nombre": "Guantes térmicos",
        "Descripcion": "Guantes resistentes al agua con forro interior",
        "Stock": 15,
        "PrecioUnitario": 34.50,
        "Colores": {
            "color1": "negro",
            "color2": "gris",
            "color3": "azul"
        }
    },
    '03': {
        "activo": True,
        "nombre": "Casco de ski",
        "Descripcion": "Casco liviano con ventilación y ajuste regulable",
        "Stock": 8,
        "PrecioUnitario": 89.99,
        "Colores": {
            "color1": "blanco",
            "color2": "negro",
            "color3": "naranja"
        }
    },
    '04': {
        "activo": True,
        "nombre": "Pañuelo térmico",
        "Descripcion": "Cuello polar para proteger del frío y viento",
        "Stock": 20,
        "PrecioUnitario": 12.00,
        "Colores": {
            "color1": "azul marino",
            "color2": "verde militar",
            "color3": "gris"
        }
    },
    '05': {
        "activo": True,
        "nombre": "Mochila impermeable",
        "Descripcion": "Mochila de ski resistente al agua, 20L",
        "Stock": 6,
        "PrecioUnitario": 59.90,
        "Colores": {
            "color1": "negro",
            "color2": "rojo",
            "color3": "celeste"
        }
    },
    '06': {
        "activo": True,
        "nombre": "Antiparras profesionales",
        "Descripcion": "Antiparras con doble lente y antiempañante",
        "Stock": 12,
        "PrecioUnitario": 79.99,
        "Colores": {
            "color1": "violeta",
            "color2": "negro",
            "color3": "verde"
        }
    },
    '07': {
        "activo": True,
        "nombre": "Cubrebotas",
        "Descripcion": "Protector térmico y resistente al agua para botas",
        "Stock": 18,
        "PrecioUnitario": 22.49,
        "Colores": {
            "color1": "negro",
            "color2": "gris oscuro",
            "color3": "azul"
        }
    },
    '08': {
        "activo": True,
        "nombre": "Polainas",
        "Descripcion": "Polainas ajustables para nieve y lluvia",
        "Stock": 9,
        "PrecioUnitario": 27.75,
        "Colores": {
            "color1": "verde oliva",
            "color2": "negro",
            "color3": "rojo"
        }
    },
    '09': {
        "activo": True,
        "nombre": "Cinturón porta objetos",
        "Descripcion": "Cinturón con bolsillos para llevar celular, llaves y snack",
        "Stock": 25,
        "PrecioUnitario": 14.30,
        "Colores": {
            "color1": "gris",
            "color2": "azul",
            "color3": "negro"
        }
    },
    '10': {
        "activo": True,
        "nombre": "Protector solar de montaña",
        "Descripcion": "Protección SPF 50+ resistente al agua y al sudor",
        "Stock": 30,
        "PrecioUnitario": 9.90,
        "Colores": {
            "color1": "único"
        }
    },
    '11': {
        "activo": True,
        "nombre": "Botella térmica",
        "Descripcion": "Botella de acero inoxidable que conserva el calor",
        "Stock": 14,
        "PrecioUnitario": 19.99,
        "Colores": {
            "color1": "plateado",
            "color2": "azul",
            "color3": "negro"
        }
    }
}

def listarAccesorios(accesorios):
    for codigo, accesorio in accesorios.items():
        print(f"Código: {codigo}")
        print(f"Activo: {accesorio['activo']}")
        if accesorio['activo'] == False:
            print("El accesorio no está activo.")
            print("-" * 40)
            continue
        print(f"Nombre: {accesorio['nombre']}")
        print(f"Descripción: {accesorio['Descripcion']}")
        print(f"Stock: {accesorio['Stock']}")
        print(f"Precio Unitario: ${accesorio['PrecioUnitario']:.2f}")
        print("Colores:")
        for claveColor, valorColor in accesorio['Colores'].items():
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