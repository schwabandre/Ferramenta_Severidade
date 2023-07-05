from flask import Flask, render_template

app = Flask(__name__)


#Criar a 1° pagina do site
#Route -> Camino pós barra, ex: soloferramenta.com/FinOps

#Template

#Função -> O que você quer exibir naquela página
@app.route("/")
def homepage():
    return render_template("finops.html")

@app.route("/segurança")
def segurança():
    return render_template("seguranca.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


# servidor do heroku


