import sys
from flask import Flask, make_response
from flask_cors import CORS, cross_origin

#sys.path.insert(0, r"C:\Users\lucia\OneDrive\Área de Trabalho\ProjetosDev\FlaskDemo\src\controladores")
from Gerar_Contas_Pagar_Receber_Decimo_Terceiro import upload_decimo_terceiro
from Gerar_Contas_Pagar_Receber_Ferias import upload_ferias
from Gerar_Contas_Pagar_Receber_Seguro  import upload_seguro
from Gerar_Contas_Pagar_Receber_Flash  import upload_flash
from Criar_Invoice_Wide_Brazil  import download_invoice

app = Flask(__name__)
CORS(app)

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route('/upload-decimo')
def uploadDecimo():
    upload_decimo_terceiro()
    return "Décimo Funcionando"

@app.route('/upload-ferias')
def uploadFerias():
    upload_ferias()
    return "Férias Funcionando"

@app.route('/upload-seguro')
def uploadSeguro():
    upload_seguro()
    return "Seguro Funcionando"

@app.route('/upload-flash')
def uploadFlash():
    upload_flash()
    return "Flash Funcionando"

@app.route('/download-invoice')
def downloadInvoice():
    download_invoice()
    return "Invoice Gerado"

app.run(debug=True, port=3000)
