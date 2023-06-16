from flask import Flask

app=Flask(__name__)

#ruta
@app.route('/')
#vista
def index():
    return 'Hola, Edgar, bienvenido!!'

@app.route('/about/<nombre>')
def about(nombre):
    return f'!hola, yo soy {nombre} y estoy estudiando programación'

@app.route('/estadio/<nombre_estadio>')
def estadio(nombre_estadio):
    return f'Bienvenidos al estadio {nombre_estadio} el estadio del mejor equipo del mundo'