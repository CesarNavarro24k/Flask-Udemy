from flask import Flask,request
import random

app = Flask(__name__)

from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi App Flask</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Hello, World!</h1>
        <a href="/datos">¡Ver un dato aleatorio!</a>
        <a href="/moneda">¡Ver un lanzamiento de moneda!</a>
        <br><br>
        <form action="/suma" method="get">
            <h1>Coloca números para hacer la suma:</h1>
            <label for="num1">Número 1:</label>
            <input type="number" id="num1" name="num1" required>
            <label for="num2">Número 2:</label>
            <input type="number" id="num2" name="num2" required>
            <button type="submit">Sumar</button>
        </form>

        <form action="/resta" method="get">
            <h1>Coloca números para hacer la resta:</h1>
            <label for="num1">Número 1:</label>
            <input type="number" id="num1" name="num1" required>
            <label for="num2">Número 2:</label>
            <input type="number" id="num2" name="num2" required>
            <button type="submit">Restar</button>
        </form>

        <form action="/multi" method="get">
            <h1>Coloca números para hacer la multiplicación:</h1>
            <label for="num1">Número 1:</label>
            <input type="number" id="num1" name="num1" required>
            <label for="num2">Número 2:</label>
            <input type="number" id="num2" name="num2" required>
            <button type="submit">Multiplicar</button>
        </form>
    </body>
    </html>
    """

#/saludo/Cesar
#Bienvenido a Flask Cesar
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"<h1>Bienvenido a Flask {nombre} </h1>"
#/suma/8/2
#La suma de 8 con 2 es 10 ---> resultado
@app.route("/suma")
def suma():
    num1 = int(request.args.get("num1", 0))  # Si no hay valores, usa 0 por defecto
    num2 = int(request.args.get("num2", 0))
    return f"<h1 style = ' text-align: center;'>La suma de {num1} con {num2} es {num1 + num2}</h1>"
@app.route("/resta")
def resta():
    num1 = int(request.args.get("num1", 0))  # Si no hay valores, usa 0 por defecto
    num2 = int(request.args.get("num2", 0))
    return f"<h1 style = ' text-align: center;'>La resta de {num1} con {num2} es {num1 - num2}</h1>"
@app.route("/multi")
def multi():
    num1 = int(request.args.get("num1", 0))  # Si no hay valores, usa 0 por defecto
    num2 = int(request.args.get("num2", 0))
    return f"<h1 style = ' text-align: center;'>La multiplicación de {num1} con {num2} es {num1 * num2}</h1>"
@app.route("/datos")
def datos():
    lista_datos = [
        "Jupiter es el planeta mas grande del sistema solar",
        "El pokemon mas OP es eternatus forma dinamax eterno",
        "Linux es gratis ",
        "Un bebe tiene mas huesos que un adulto",
        "La banda sonora del Hollow Knight fue hecha por un artista"
    ]
    return f"<h1>Aqui tienes algunos datos random: {random.choice(lista_datos)} <h1>"
@app.route("/moneda")
def moneda():
    carasMoneda = random.randint(0,1)
    if carasMoneda == 0:
        return " <h1>Cara </h1>"
    else:
        return " <h1>Sello </h1>"
@app.route("/contraseñas")
def contraseñas():
    caracteres = "hjhjhjhjhsdf87878977832w"
    return f" {random.choice(caracteres)}"
app.run(debug=True)
