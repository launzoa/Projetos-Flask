from flask import Flask, render_template, request, escape
from procurador import procurar_letras



app = Flask(__name__)

def log_request(req='flask_request', res=''):

    with open('vsearch.log', 'a') as log:

        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/vsearch', methods=['POST'])

def letters_search():   
    frase = request.form['frase']
    letras = request.form['letras']
    titulo = 'Aqui estão os resultados da pesquisa:'
    resultado = str(procurar_letras(frase,letras))
    log_request(request, resultado)

    return render_template('results.html', 
                        the_titulo= titulo,
                        the_frase = frase,
                        the_letras = letras,
                        the_resultado = resultado,
                        )

@app.route('/')
@app.route('/entry')

def entry_page():

    return render_template('entry.html', 
                        the_titulo='Bem vindo ao procurador de letras!')


@app.route('/viewlog')

def viewlog_page():

    conteudo = []

    with open('vsearch.log') as log:

        for line in log:
            
            conteudo.append([])

            for item in line.split("|"):

                conteudo[-1].append(escape(item))

    titulos = ['Form Data', 'Remote_addr', 'User_agent', 'Results']
    
    return render_template('viewlog.html',
                            the_titulo="Banco de dados",
                            the_row_titulo= titulos,
                            the_row_dados= conteudo
                           )


if __name__ == '__main__':
     
    app.run(debug=True)      