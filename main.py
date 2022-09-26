from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return "este es el home"

@app.route('/entero/<int:edad>')
def ejemplo1(edad):
    return f"estoy retornando el valor entero {edad}"

@app.route('/float/<float:peso>')
def ejemplo2(peso):
    return f"estoy retornando el valor float {peso}"

@app.route('/string/<string:saludo>')
def ejemplo3(saludo):
    return f"estoy retornando el valor string {saludo}"

@app.route('/valor/<valor>')
def ejemplo4(valor):
    return f"estoy retornando el valor cualquiera {valor}"

@app.route('/formulario/')
def formulario():
    return render_template("formulario.html")

# @app.route('/formulario/guardarget/', methods=["GET"])
# def formularioGuardarGet():
#     codigo = request.args.get("txtCodigo")
#     nombre = request.args.get("txtNombre")
#     precio = request.args.get("txtPrecio")
#     return f"Codigo: {codigo}, nombre: {nombre}, precio: {precio}"

# @app.route('/formulario/guardarpost/',methods=["POST"])
# def formularioGuardarPost():
#     codigo = request.form["txtCodigo"]
#     nombre = request.form["txtNombre"]
#     precio = request.form["txtPrecio"]
#     return f"Codigo: {codigo}, nombre: {nombre}, precio: {precio}"

@app.route("/formulario/guardargetpost/", methods=["GET", "POST"])
def formularioGuardarGetPost():
    if request.method == "POST":
        codigo = request.form["txtCodigo"]
        nombre = request.form["txtNombre"]
        precio = request.form["txtPrecio"]
        
    else:
        codigo = request.args.get("txtCodigo")
        nombre = request.args.get("txtNombre")
        precio = request.args.get("txtPrecio")
        
    return f"Codigo: {codigo}, nombre: {nombre}, precio: {precio}"

@app.route("/tienda/")
def tienda():
    tit = "administrador de productos"
    return render_template("producto.html", titulo = tit)

if __name__ == '__main__':
    app.run(debug=True)


