from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    aluno = {
        "nome": "Kinque",
        "turma": "2° Ensino Médio Técnico"
    }
    professores = [
        {
            "nome": "Felipe Ishara",
            "materia": "Web II"
        },
        {
            "nome": "Edidio Lima",
            "materia": "Software"
        }
    ]
    return render_template('index.html', title="Home", aluno=aluno, professores=professores)

@app.route("/boletim")
def boletim():
    return render_template('boletim.html', title="Boletim")

@app.route("/sobre")
def sobre():
    return render_template('Sobre.html', title="Sobre")

@app.route('/validacao', methods=['GET', 'POST'])
def validacao():
    nome = ""
    sobrenome = ""
    idade = 0
    pode_votar = False
    pode_dirigir = False
    mensagem = ""

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        sobrenome = request.form.get('sobrenome', '').strip()
        idade = int(request.form.get('idade', 0) or 0)

        contador = 0
        while contador < 1:
            pode_votar = idade >= 16
            pode_dirigir = idade >= 18
            contador += 1

        mensagem = (
            f"{nome} {sobrenome}, você {'pode' if pode_votar else 'não pode'} votar "
            f"e {'pode' if pode_dirigir else 'não pode'} dirigir."
        )

    return render_template(
        'validacao.html',
        title='Validação',
        nome=nome,
        sobrenome=sobrenome,
        idade=idade,
        pode_votar=pode_votar,
        pode_dirigir=pode_dirigir,
        mensagem=mensagem
    )

if __name__ == "__main__":
    app.run(debug=True)
