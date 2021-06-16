from flask import Flask, render_template
#importamos la librería de Flask


#creamos un objeto de Flask
app = Flask(__name__)

#creamos una ruta # raíz
@app.route('/')

#creamos una función de ruteo para mostrar index.html
def index():
    return render_template('index.html')
# Press the green button in the gutter to run the script.
#creamos una condicional para tener un archivo de ejecución
#se ejecuta en terminal con: python nombredelarchivo.py
if __name__ == '__main__':
    app.run(port=80, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/