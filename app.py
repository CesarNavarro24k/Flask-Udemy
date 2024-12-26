from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <h1> Bienvenidos a mi página web </h1>
    <p> Esta es una página de prueba </p>
    <h2> Encontraras rutas a paginas webs para: </h2>
    <ul>
        <li> Saludar </li>
        <li> Sumar </li>
        <li> Restar </li>
        <li> Multiplicar </li>
        <li> Dividir </li>
    </ul>
    """
@app.route("/saludo/<nombre>/<edad>")
def saludo(nombre, edad):
    return f" <h1>Hola {nombre} bienvenido a nuestra página, tu edad es {edad}</h1>" 
@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"<h1>La suma de {num1} y {num2} es {num1 + num2}</h1>"
@app.route("/resta/<int:num1>/<int:num2>")
def resta(num1, num2):
    return f"<h1>La resta de {num1} y {num2} es {num1 - num2}</h1>"
@app.route("/multiplicacion/<int:num1>/<int:num2>")
def multiplicacion(num1, num2):
    return f"<h1> La multiplicación de {num1} y {num2} es {num1 * num2} </h1>"
@app.route("/division/<int:num1>/<int:num2>")
def division(num1, num2):
    if num2 == 0:
        return "<h1> No se puede dividir por 0 </h1>"
    else:
        return f"<h1> La división de {num1} y {num2} es {num1 / num2}</h1>"
if __name__ == '__main__':
    app.run(debug=True)














