from flask import Flask, render_template, request

app = Flask(__name__)

recipes = {
    "bolo de cenoura": "🍰 Receita de Bolo de Cenoura:<br>Ingredientes:<br>- 3 cenouras médias<br>- 4 ovos<br>- 1 xícara de óleo<br>- 2 xícaras de açúcar<br>- 2 e 1/2 xícaras de farinha<br>- 1 colher de fermento<br><br>Modo de preparo:<br>Bata as cenouras, ovos e óleo no liquidificador. Misture com os ingredientes secos. Asse por 40 minutos a 180°C.",
    "lasanha": "🍝 Receita de Lasanha:<br>Ingredientes:<br>- Massa de lasanha<br>- Molho de tomate<br>- Presunto e queijo<br>- Carne moída<br>- Temperos a gosto<br><br>Modo de preparo:<br>Monte camadas com molho, massa, carne e queijo. Asse por 30 minutos a 200°C.",
    "panqueca": "🥞 Receita de Panqueca:<br>Ingredientes:<br>- 1 ovo<br>- 1 xícara de leite<br>- 1 xícara de farinha<br><br>Modo de preparo:<br>Misture tudo, frite em frigideira antiaderente, recheie e enrole.",
    "arroz": "🍚 Receita de Arroz:<br>Ingredientes:<br>- 1 xícara de arroz<br>- 2 xícaras de água<br>- Alho, óleo e sal<br><br>Modo de preparo:<br>Refogue o alho no óleo, adicione o arroz, frite um pouco, coloque a água e o sal, e cozinhe até secar.",
    "obrigada": "Obrigada! Fico feliz que tenha gostado! 😊",
    "obrigado": "Obrigada! Fico feliz que tenha gostado! 😊",
    "gostei": "Obrigada! Fico feliz que tenha gostado! 😊",
    "amei": "Obrigada! Fico feliz que tenha gostado! 😊",
    "tchau": "Tchau! Até a próxima receita! 👋"
}

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = "🍽️ Olá! O que você quer cozinhar hoje?"
    if request.method == "POST":
        user_input = request.form["mensagem"].lower()
        resposta = recipes.get(user_input, "Desculpe, ainda não tenho essa receita. Tente outra! 😊")
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)
