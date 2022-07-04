from balance import app


@app.route('/')
def home():
    return "Homepage"
@app.route('/new')
def new():
    return "Creacion de movimiento"
@app.route('/modify')
def update():
    return "Actualizar movimiento"
@app.route('/delete')
def borrar():
    return "Borrar movimiento"
