from flask import Flask, render_template, request, redirect, session
import os
import locale

app = Flask(__name__)
app.secret_key = os.urandom(24)  

produtos = [
    {"id": 1, "nome": "Casadinho ", "descricao": "Bambolê Leite Ninho Recheado", "preco": 20.00, "quantidade": 4, "categoria": "Doces", "imagem": "/static/imagens/bambole_ninho.jpg"},
    {"id": 2, "nome": "Casadinho ", "descricao": "Florzinha de Leite Condensado Recheada", "preco": 20.00, "quantidade": 4, "categoria": "Doces", "imagem": "/static/imagens/florzinha_recheada.jpg"},
    {"id": 3, "nome": "Casadinho ", "descricao": "Casadinho de Nata Recheado", "preco": 20.00, "quantidade": 5, "categoria": "Doces", "imagem": "/static/imagens/casadinho_nata.jpg"},        
    {"id": 4, "nome": "Casadinho ", "descricao": "Rosquinha de Nata", "preco": 20.00, "quantidade": 5, "categoria": "Doces", "imagem": "/static/imagens/rosquinha_nata.jpg"}, 
    {"id": 5, "nome": "Casadinho ", "descricao": "Romeu com Coco", "preco": 20.00, "quantidade": 3, "categoria": "Doces", "imagem": "/static/imagens/romeu_coco.jpg"}, 
    {"id": 6, "nome": "Casadinho ", "descricao": "Flocos", "preco": 20.00, "quantidade": 2, "categoria": "Doces", "imagem": "/static/imagens/flocos.jpg"},      
    {"id": 7, "nome": "Casadinho", "descricao": "Florzinha de Leite Condensado", "preco": 20.00, "quantidade": 3, "categoria": "Biscoitos", "imagem": "/static/imagens/florzinha.jpg"},
    {"id": 8, "nome": "Casadinho", "descricao": "Sem Recheio de leite condensado", "preco": 20.00, "quantidade": 15, "categoria": "Biscoito", "imagem": "/static/imagens/coxinha.jpg"},
    {"id": 9, "nome": "Casadinho", "descricao": "Leite Ninho Com Recheio de Goiabada", "preco": 20.00, "quantidade": 15, "categoria": "Biscoito", "imagem": "/static/imagens/coxinha.jpg"},
    {"id": 10, "nome": "Casadinho", "descricao": "Leite Condensado", "preco": 20.00, "quantidade": 15, "categoria": "Biscoito", "imagem": "/static/imagens/coxinha.jpg"},
    {"id": 11, "nome": "Salgadinho", "descricao": "Sabor  de Bacon", "preco": 20.00, "quantidade": 4, "categoria": "Salgadinhos", "imagem": "/static/imagens/bacon.jpg"},
    {"id": 12, "nome": "Salgadinho", "descricao": "Sabor  de Cebola e Salsa", "preco": 20.00, "quantidade": 3, "categoria": "Salgadinhos", "imagem": "/static/imagens/cebola_salsa.jpg"},
    {"id": 13, "nome": "Salgadinho", "descricao": "Sabor  de Picanha", "preco": 20.00, "quantidade": 6, "categoria": "Salgadinhos", "imagem": "/static/imagens/picanha.jpg"},
    {"id": 14, "nome": "Salgadinho", "descricao": "Sabor  de Pizza", "preco": 20.00, "quantidade": 5, "categoria": "Salgadinhos", "imagem": "/static/imagens/pizza.jpg"},
    {"id": 15, "nome": "Salgadinho", "descricao": "Sabor  de Pimenta Mexicana", "preco": 20.00, "quantidade": 6, "categoria": "Salgadinhos", "imagem": "/static/imagens/pimenta_mexicana.jpg"}, 
    {"id": 16, "nome": "Salgadinho", "descricao": "Sabor  de Costelinha com limão", "preco": 20.00, "quantidade": 3, "categoria": "Salgadinhos", "imagem": "/static/imagens/costelinha_limao.jpg"},  
    {"id": 17, "nome": "Paçoca", "descricao": "Paçoca com chocolate", "preco": 22.00, "quantidade": 2, "categoria": "Doces", "imagem": "/static/imagens/paçoca.jpg"},
    {"id": 18, "nome": "Trufas", "descricao": "Trufas Sabores Variados", "preco": 32.00, "quantidade": 8, "categoria": "Doces", "imagem": "/static/imagens/trufas.jpg"},
    {"id": 19, "nome": "Amendoin ", "descricao": "Amendoin Crocante de Pimenta", "preco": 18.00, "quantidade": 2, "categoria": "Salgadinhos", "imagem": "/static/imagens/amendoin_pimenta.jpg"},
    {"id": 20, "nome": "Amendoin ", "descricao": "Amendoin Crocante Churrasco", "preco": 18.00, "quantidade": 1, "categoria": "Salgadinhos", "imagem": "/static/imagens/amendoin_churrasco.jpg"},
    {"id": 21, "nome": "Amendoin ", "descricao": "Amendoin Crocante Natural", "preco": 18.00, "quantidade": 1, "categoria": "Salgados", "imagem": "/static/imagens/amendoin_natural.jpg"},
    {"id": 22, "nome": "Amendoin ", "descricao": "Amendoin Cebola e Salsa", "preco": 18.00, "quantidade": 2, "categoria": "Salgados", "imagem": "/static/imagens/amendoin_cebola_salsa.jpg"},
    {"id": 23, "nome": "Amendoin ", "descricao": "Amendoin Crocante", "preco": 18.00, "quantidade": 6, "categoria": "Salgados", "imagem": "/static/imagens/crocante.jpg"},
    {"id": 24, "nome": "Chocolate ", "descricao": "Delícias de Minas", "preco": 24.00, "quantidade": 1, "categoria": "Doces", "imagem": "/static/imagens/delicias_minas.jpg"},
    {"id": 25, "nome": "Chocolate ", "descricao": "Delícias de Minas Choco Festa", "preco": 24.00, "quantidade": 1, "categoria": "Doces", "imagem": "/static/imagens/delicias_choco_festa.jpg"},
    {"id": 26, "nome": "Chocolate ", "descricao": "Delícias de Minas Rosca de Brigadeiro", "preco": 24.00, "quantidade": 1, "categoria": "Doces", "imagem": "/static/imagens/delicias_rosca_brigadeiro.jpg"},
    {"id": 27, "nome": "Chocolate ", "descricao": "Delícias de Minas Prestococo", "preco": 24.00, "quantidade": 1, "categoria": "Doces", "imagem": "/static/imagens/delicias_prestoco.jpg"},
    {"id": 28, "nome": "Chocolate ", "descricao": "Delícias de Minas Prestigio", "preco": 24.00, "quantidade": 1, "categoria": "Doces", "imagem": "/static/imagens/delicias_prestigio.jpg"},

]

def formatar_moeda(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  
    return locale.currency(valor, grouping=True)

# Registra o filtro no Flask
app.jinja_env.globals.update(formatar_moeda=formatar_moeda)


def calcular_total():
    total = 0
    for item in session.get('carrinho', []):
        total += item['preco'] * item['quantidade']
    return total


@app.route('/')
def home():
    categorias = list(set(produto["categoria"] for produto in produtos))
    return render_template('home.html', produtos=produtos, categorias=categorias)

@app.route('/add_to_cart/<int:produto_id>', methods=['POST'])
def add_to_cart(produto_id):
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if produto and produto['quantidade'] > 0:
        if 'carrinho' not in session:
            session['carrinho'] = []  
        
     
        item_no_carrinho = next((item for item in session['carrinho'] if item['id'] == produto_id), None)
        if item_no_carrinho:
         
            item_no_carrinho['quantidade'] += 1
        else:
            
            produto_carrinho = produto.copy()  
            produto_carrinho['quantidade'] = 1
            session['carrinho'].append(produto_carrinho)

        produto['quantidade'] -= 1  
        session.modified = True  
    return redirect('/cart')

@app.route('/update_quantity/<int:produto_id>', methods=['POST'])
def update_quantity(produto_id):
    quantidade = int(request.form.get('quantidade'))
    if 'carrinho' in session:
        for item in session['carrinho']:
            if item['id'] == produto_id:
                item['quantidade'] = quantidade  
                break
    return redirect('/cart')


@app.route('/cart')
def cart():
    carrinho = session.get('carrinho', [])
    total = calcular_total()
    return render_template('cart.html', carrinho=carrinho, total=formatar_moeda(total))


@app.route('/remove_from_cart/<int:produto_id>', methods=['POST'])
def remove_from_cart(produto_id):
    if 'carrinho' in session:
        for item in session['carrinho']:
            if item['id'] == produto_id:
                session['carrinho'].remove(item)
                produto = next((p for p in produtos if p['id'] == produto_id), None)
                if produto:
                    produto['quantidade'] += item['quantidade']  
                break
    return redirect('/cart')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        nome = request.form.get('nome')
        endereco = request.form.get('endereco')
        forma_pagamento = request.form.get('forma_pagamento')
        entrega = request.form.get('entrega')
        taxa_entrega = 7.00 if entrega == "Sim" else 0.00
        total = calcular_total() + taxa_entrega

      
        carrinho_atual = session.get('carrinho', [])

       
        for item in carrinho_atual:
            produto = next((p for p in produtos if p['id'] == item['id']), None)
            if produto:
                produto['quantidade'] -= item['quantidade'] 
        
       
        session['carrinho'] = []

       
        produtos_comprados = "\n".join([f"{item['quantidade']}x {item['nome']} - {formatar_moeda(item['preco'] * item['quantidade'])}" for item in carrinho_atual])

   
        mensagem = (
            f"Compra realizada!\n\n"
            f"Nome: {nome}\n"
            f"Endereço: {endereco}\n"
            f"Forma de pagamento: {forma_pagamento}\n"
            f"Taxa de entrega: {formatar_moeda(taxa_entrega)}\n"
            f"Total: {formatar_moeda(total)}\n"
            f"Produtos comprados:\n{produtos_comprados}\n\n"
            f"PIX: 31991070255"
        )

        
        mensagem_codificada = mensagem.replace(' ', '%20').replace('\n', '%0A')

        # Redireciona para o link do WhatsApp com a mensagem
        return redirect(f"https://wa.me/31991708075?text={mensagem_codificada}")

    return render_template('checkout.html', carrinho=session.get('carrinho', []), total=formatar_moeda(calcular_total() + 7))


def calcular_total():
  
    carrinho = session.get('carrinho', [])
    return sum(item['preco'] * item['quantidade'] for item in carrinho)

@app.route('/finalizado')
def finalizado():
    return render_template('finalizado.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
