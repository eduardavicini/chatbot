from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Base de receitas conhecidas
receitas = {
    "bolo de cenoura": {
        "texto": """
🍰 Receita de Bolo de Cenoura

📝 Ingredientes:
- 3 cenouras médias
- 4 ovos
- 1 xícara de óleo
- 2 xícaras de açúcar
- 2 e 1/2 xícaras de farinha de trigo
- 1 colher (sopa) de fermento em pó

🍫 Cobertura:
- 1 colher (sopa) de manteiga
- 3 colheres (sopa) de chocolate em pó
- 1 xícara de açúcar
- 1/2 xícara de leite

👩‍🍳 Modo de preparo:
1. Bata as cenouras, ovos e óleo no liquidificador.
2. Transfira para uma tigela e misture o açúcar, a farinha e o fermento.
3. Coloque em uma forma untada e leve ao forno pré-aquecido a 180°C por 40 minutos.
4. Para a cobertura, leve todos os ingredientes ao fogo até engrossar e jogue sobre o bolo.

📺 Vídeo: https://www.youtube.com/watch?v=tgShdcf9WYI
"""
    },
    "panqueca": {
        "texto": """
🥞 Receita de Panqueca

📝 Ingredientes da massa:
- 1 xícara de farinha de trigo
- 1 xícara de leite
- 1 ovo
- 1 pitada de sal

👩‍🍳 Modo de preparo da massa:
1. Bata todos os ingredientes no liquidificador.
2. Unte uma frigideira com um pouco de óleo.
3. Despeje uma concha da massa, espalhe e frite dos dois lados.

📌 Recheie com carne moída, frango ou queijo e cubra com molho de tomate.

📺 Vídeo: https://www.youtube.com/watch?v=LoZHkdKcDDU
"""
    },
    "lasanha": {
        "texto": """
🍝 Receita de Lasanha à Bolonhesa

📝 Ingredientes:
- Massa de lasanha
- 500g de carne moída
- 1 cebola picada
- 2 dentes de alho
- 1 sachê de molho de tomate
- Queijo e presunto
- Sal, pimenta e orégano a gosto

👩‍🍳 Modo de preparo:
1. Refogue a cebola e o alho, depois adicione a carne.
2. Acrescente o molho e deixe cozinhar por 10 minutos.
3. Monte as camadas: molho, massa, presunto, queijo e repita.
4. Finalize com queijo e leve ao forno por 30 minutos a 200°C.

📺 Vídeo: https://www.youtube.com/watch?v=OmfX3x03hi8
"""
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagem', methods=['POST'])
def mensagem():
    data = request.get_json()
    mensagem = data.get('mensagem', '').strip().lower()

    if mensagem in ["obrigado", "obrigada", "valeu", "agradecido"]:
        return jsonify({"resposta": "Fico feliz que tenha gostado! 😊 Se precisar de mais receitas, é só chamar."})

    for chave, valor in receitas.items():
        if chave in mensagem:
            return jsonify({"resposta": valor["texto"]})

    # Se não encontrou a receita
    sugestoes = ', '.join(random.sample(list(receitas.keys()), min(3, len(receitas))))
    texto_resposta = (
        f"Desculpe, ainda não conheço a receita de \"{mensagem}\".\n\n"
        f"Mas posso te ajudar com: {sugestoes}."
    )
    return jsonify({"resposta": texto_resposta})

if __name__ == '__main__':
    app.run(debug=True)

