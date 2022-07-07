"""
Un movimiento debe tener:

1. Fecha
2. Concepto
3. Tipo (I-ngreso, G-asto)
4. Cantidad
"""
import csv
from datetime import date, datetime

from . import FICHERO


class Movimiento:
    def __init__(self, dic_datos):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(dic_datos["fecha"])
        except ValueError:
            self.errores.append("Formato de la fecha no es válido")
        
        
        self.concepto = dic_datos["concepto"]
        self.tipo = dic_datos["tipo"]
        self.cantidad = dic_datos["cantidad"]

    def __str__(self):
        return "fecha: {} concepto: {} tipo: {} cantidad: {}".format(
            self.fecha,
            self.concepto,
            self.tipo,
            self.cantidad
        )

    def validar_fecha(fecha):
        pass


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                # creo un movimiento para cada apartado y guardarlo
                mov = Movimiento(linea)
                self.movimientos.append(mov)

        # es otra manera de hacer el bloque anterior
        # file = open("data/movements.csv", "r")
        # reader = csv.DictReader(file)
        # for line in reader:
        #     self.movements_list.append(line)
        # file.close()