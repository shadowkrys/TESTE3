from flask import Flask, render_template

cardapio = Flask(__name__)

# Dados do cardápio (por enquanto, em uma lista de dicionários)
menu_items = [
    {"nome": "Hambúrguer Clássico", "descricao": "Pão, carne, queijo, alface e tomate.", "preco": "R$ 25,00"},
    {"nome": "Batata Frita", "descricao": "Porção generosa de batatas crocantes.", "preco": "R$ 15,00"},
    {"nome": "Refrigerante", "descricao": "Lata 350ml.", "preco": "R$ 8,00"}
]

@cardapio.route('/')
def home():
    return render_template('index.html', items=menu_items)

if __name__ == '__main__':
    cardapio.run(host='0.0.0.0', debug = True)