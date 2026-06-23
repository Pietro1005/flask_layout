from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():]
    aluno = {
        "nome": "Kinque"
        "turma": "2° Ensino Medio Técnico"
    }
    professores = [
        {
            "nome" = "Felipe Ishara",
            "materia": "Web II"
        },

        {
            "nome" = "Edidio Lima"
            "materia" = "Software"
        }
    ]
    return render_template('index.html', title="home" aluno=aluno, professores=professores )

@app.route("/boletim")
def boletim():
    return render_template('boletim.html', title="boletim")