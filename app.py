# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Blanca" # escribe tu nombre
    age = "26" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
@app.route('/papa')
def papa():

    name = "José"
    age = "53"

    return render_template('father.html', name = name, age = age)

# define la ruta a la página web de tu madre.
@app.route('/mama')
def mama():

    name =  "Sonia"
    age = "54"

    return render_template("mother.html", name = name, age = age)

# define la ruta a la página web de tus amigos.
@app.route('/ange')
def ange():

    name = "Angelica"
    age = "28"

    return render_template("friend.html", name = name, age = age)

# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
