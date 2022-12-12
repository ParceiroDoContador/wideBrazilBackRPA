import sys
from flask import Flask
from flask_cors import CORS, cross_origin

#sys.path.insert(0, r"C:\Users\lucia\OneDrive\Área de Trabalho\ProjetosDev\FlaskDemo\src\controladores")
from Gerar_Contas_Pagar_Receber_Decimo_Terceiro import upload_decimo_terceiro
from Gerar_Contas_Pagar_Receber_Ferias import upload_ferias
from Gerar_Contas_Pagar_Receber_Seguro  import upload_seguro
from Gerar_Contas_Pagar_Receber_Flash  import upload_flash
from Criar_Invoice_Wide_Brazil  import download_invoice

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/upload-decimo')
@cross_origin()
def uploadDecimo():
    upload_decimo_terceiro()
    return "Décimo Funcionando"

@app.route('/upload-ferias')
@cross_origin()
def uploadFerias():
    upload_ferias()
    return "Férias Funcionando"

@app.route('/upload-seguro')
@cross_origin()
def uploadSeguro():
    upload_seguro()
    return "Seguro Funcionando"

@app.route('/upload-flash')
@cross_origin()
def uploadFlash():
    upload_flash()
    return "Flash Funcionando"

@app.route('/download-invoice')
@cross_origin()
def downloadInvoice():
    download_invoice()
    return "Invoice Gerado"

app.run(debug=True, port=3000)
