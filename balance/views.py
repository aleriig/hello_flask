from flask import render_template

from balance import app
from .models import MovementsList


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    movements = MovementsList()
    movements.read_file()
    return render_template("start.html", movs=movements.movements_list)
    

@app.route('/new')
def new():
    return "Creacion de movimiento"

@app.route('/modify')
def update():
    return "Actualizar movimiento"

@app.route('/delete')
def borrar():
    return "Borrar movimiento"
