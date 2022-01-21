from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def nivelBasico(x=8, y=8, colorx="yellow", colory="lightblue"):
    return render_template("index.html", x=int(x), y=int(y), colorx=colorx, colory=colory)

@app.route("/<x>", methods = ["GET"])
def nivelIntermedio1(x, y=8, colorx="yellow", colory="lightblue"):
    return render_template("index.html", x=int(x), y=int(y), colorx=colorx, colory=colory)

@app.route("/<x>/<y>", methods = ["GET"])
def nivelIntermedio2(x, y, colorx="yellow", colory="lightblue"):
    return render_template("index.html", x=int(x), y=int(y), colorx=colorx, colory=colory)

@app.route("/<x>/<y>/<colorx>", methods = ["GET"])
def nivelAvanzado1(x, y, colorx, colory="lightblue"):
    return render_template("index.html", x=int(x), y=int(y), colorx=colorx, colory=colory)

@app.route("/<x>/<y>/<colorx>/<colory>", methods = ["GET"])
def nivelAvanzado2(x, y, colorx, colory):
    return render_template("index.html", x=int(x), y=int(y), colorx=colorx, colory=colory)

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo mas tarde"

if __name__ == "__main__":
    app.run(debug=True)