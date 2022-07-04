
import csv
from . import FILE

class Movement:
    def __init__(self, date, concept, type, quantity):
        self.date = date
        self.concept = concept
        self.type = type
        self.quantity = quantity

class MovementsList:
    def __init__(self):
        self.movements_list = []

    def read_file(self):
        with open(FILE, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                self.movements_list.append(line)

        # es otra manera de hacer el bloque anterior
        # file = open("data/movements.csv", "r")
        # reader = csv.DictReader(file)
        # for line in reader:
        #     self.movements_list.append(line)
        # file.close()