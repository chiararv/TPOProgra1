"""
UTILIDAD PARA GENERAR UN ARCHIVO JSON A PARTIR DE UN DICCIONARIO PYTHON
"""

import json

# *****************************************************
# DICCIONARIO DE LA ENTIDAD A CARGAR EN EL ARCHIVO JSON
# *****************************************************
# Pegar a continuación la variable diccionario y sus datos

productos = {
        "TEX1000": {"activo": True,
                    "descripcion": "SÁBANA BÁSICA MICROFIBRA 1 1/2 PLAZA",
                    "stock": 520,
                    "unitario": 44000.00,
                    "colores": {"color1": "BLANCO",
                                "color2": "VERDE",
                                "color3": "ROSA",
                                "color4": "GRIS",
                                },
                    },
        "TEX1001": {"activo": True,
                    "descripcion": "ACOLCHADO PLUS QUEEN",
                    "stock": 310,
                    "unitario": 115000.00,
                    "colores": {"color1": "GRIS",
                                "color2": "AZUL",
                                },
                    },
        "TEX1002": {"activo": True,
                    "descripcion": "FUNDA ALMOHADA ALGODÓN EGIPCIO KING",
                    "stock": 450,
                    "unitario": 35000.00,
                    "colores": {"color1": "BLANCO",
                                "color2": "NATURAL",
                                "color3": "PERLA",
                                },
                    },
        "TEX1003": {"activo": True,
                    "descripcion": "JUEGO DE SÁBANAS PERCAL 200 HILOS TWIN",
                    "stock": 280,
                    "unitario": 78000.00,
                    "colores": {"color1": "CELESTE",
                                "color2": "BLANCO",
                                "color3": "BEIGE",
                                },
                    },
        "TEX1004": {"activo": True,
                    "descripcion": "PROTECTOR DE COLCHÓN IMPERMEABLE KING SIZE",
                    "stock": 150,
                    "unitario": 52000.00,
                    "colores": {"color1": "BLANCO",
                                },
                    },
        "TEX1005": {"activo": True,
                    "descripcion": "CUBRECAMA RÚSTICO TUSOR 2 1/2 PLAZAS",
                    "stock": 190,
                    "unitario": 95000.00,
                    "colores": {"color1": "CRUDO",
                                "color2": "GRIS TOPO",
                                "color3": "TERRACOTA",
                                },
                    },
        "TEX1006": {"activo": True,
                    "descripcion": "ALMOHADA VISCOELÁSTICA CERVICAL STANDARD",
                    "stock": 300,
                    "unitario": 62000.00,
                    "colores": {"color1": "BLANCO",
                                },
                    },
        "TEX1007": {"activo": True,
                    "descripcion": "EDREDÓN DE PLUMAS SINTÉTICAS QUEEN",
                    "stock": 120,
                    "unitario": 135000.00,
                    "colores": {"color1": "BLANCO",
                                "color2": "GRIS PERLA",
                                },
                    },
        "TEX1008": {"activo": True,
                    "descripcion": "SÁBANA AJUSTABLE JERSEY DE ALGODÓN FULL",
                    "stock": 400,
                    "unitario": 58000.00,
                    "colores": {"color1": "ROSA VIEJO",
                                "color2": "VERDE SECO",
                                "color3": "BLANCO",
                                "color4": "MAÍZ",
                                },
                    },
        "TEX1009": {"activo": True,
                    "descripcion": "MANTA POLAR SOFT ESKIMO KING",
                    "stock": 250,
                    "unitario": 71000.00,
                    "colores": {"color1": "AZUL MARINO",
                                "color2": "BORDEAUX",
                                "color3": "CHOCOLATE",
                                },
                    },
        "TEX1010": {"activo": True,
                    "descripcion": "JUEGO DE TOALLA Y TOALLÓN MICROFIBRA SECADO RÁPIDO",
                    "stock": 600,
                    "unitario": 38000.00,
                    "colores": {"color1": "AQUA",
                                "color2": "CORAL",
                                "color3": "GRIS CLARO",
                                },
                    },
            }



# *****************************************************
# CARGA DEL DICCIONARIO EN EL ARCHIVO JSON
# *****************************************************
# En las siguientes 2 líneas ajustar:
# - Nombre del nuevo archivo JSON
# - Nombre de la variable diccionario anterior
archivoJSON = "productos.json"
variableDicc= productos

f = open(archivoJSON, mode='w', encoding="utf-8")
json.dump(variableDicc, f, ensure_ascii=False, indent=4) 
f.close()

