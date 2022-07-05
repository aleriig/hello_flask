"""
Un movimiento debe tener:

1. Fecha
2. Concepto
3. Tipo (I-ngreso, G-asto)
4. Cantidad
"""
import csv

from . import FICHERO


class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad


class ListaMovimientos:
    def __init__(self):
        self.lista_movimientos = []

    def leer_archivo(self):
        with open(FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                self.lista_movimientos.append(linea)

        # es otra manera de hacer el bloque anterior
        # file = open("data/movements.csv", "r")
        # reader = csv.DictReader(file)
        # for line in reader:
        #     self.movements_list.append(line)
        # file.close()