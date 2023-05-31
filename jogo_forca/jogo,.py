from flask import Flask, render_template, request, url_for, redirect
import random
import palavras as p

app = Flask(__name__)

categoria = random.choice(list(p.palavras.keys()))
palavra = random.choice(p.palavras[categoria])

lista_letras = []
vidas = 5

@app.route("/", methods=["POST", "GET"])

def pagina_jogo():

    global vidas

    if request.method == "POST":

        letra = request.form['letra']
        lista_letras.append(letra)
    
        if letra not in palavra:

            vidas -= 1

            if vidas == 0:

                return render_template('fim_de_jogo.html',
                                       titulo = "Fim de jogo!",
                                       palavra = palavra
                                       )

        if all(letra in lista_letras for letra in palavra):

            return render_template('venceu.html',
                                   titulo = "Fim de jogo!",
                                   palavra = palavra)
        
        
    return render_template('jogo.html',
                            titulo = "Forca!",
                            palavra = palavra,
                            categoria = categoria,
                            letras = lista_letras,
                            vidas = vidas
                           )

@app.route("/resetar")

def resetar_jogo():

    global palavra,lista_letras, categoria

    categoria = random.choice(list(p.palavras.keys()))
    palavra = random.choice(p.palavras[categoria])
    lista_letras = []

    return redirect(url_for('pagina_jogo'))

if __name__ == '__main__':
    app.run(debug=True)