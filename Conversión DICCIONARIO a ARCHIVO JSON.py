"""
UTILIDAD PARA GENERAR UN ARCHIVO JSON A PARTIR DE UN DICCIONARIO PYTHON
"""

import json

# *****************************************************
# DICCIONARIO DE LA ENTIDAD A CARGAR EN EL ARCHIVO JSON
# *****************************************************
# Pegar a continuación la variable diccionario y sus datos

renta = {
    "01": {
        "idRenta": "2025.05.10.12.00.00",
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
        "idRenta": "2025.05.05.15.30.00",
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
        "idRenta": "2025.05.12.09.45.00",
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
        "idRenta": "2025.04.03.18.00.00",
        "idCliente": "04",
        "dias": 3,
        "fecha Devolucion": "2025.05.03.18.00.00",
        "total": 4500.0,
        "deposito": 5000.0,
        "estado": "cancelado",
        "metodoPago": "transferencia",
        "idAccesorio": "01",
        "cantidad": "2"
    },
    "05": {
        "idRenta": "2025.06.20.20.00.00",
        "idCliente": "05",
        "dias": 15,
        "fecha Devolucion": "2025.07.20.20.00.00",
        "total": 22500.0,
        "deposito": 30000.0,
        "estado": "ocupado",
        "metodoPago": "tarjeta",
        "idAccesorio": "04",
        "cantidad": "25"
    }
}
# *****************************************************
# CARGA DEL DICCIONARIO EN EL ARCHIVO JSON
# *****************************************************
# En las siguientes 2 líneas ajustar:
# - Nombre del nuevo archivo JSON
# - Nombre de la variable diccionario anterior
archivoJSON = "renta.json"
variableDicc= renta

f = open(archivoJSON, mode='w', encoding="utf-8")
json.dump(variableDicc, f, ensure_ascii=False, indent=4) 
f.close()

