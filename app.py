from flask import Flask, make_response, Response
from flask_cors import CORS

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
    _build_cors_preflight_response()
    upload_decimo_terceiro()
    res = Response(status=200)
    return res

@app.route('/upload-ferias')
def uploadFerias():
    _build_cors_preflight_response()
    upload_ferias()
    res = Response(status=200)
    return res

@app.route('/upload-seguro')
def uploadSeguro():
    _build_cors_preflight_response()
    upload_seguro()
    res = Response(status=200)
    return res

@app.route('/upload-flash')
def uploadFlash():
    _build_cors_preflight_response()
    upload_flash()
    res = Response(status=200)
    return res

@app.route('/download-invoice')
def downloadInvoice():
    _build_cors_preflight_response()
    download_invoice()
    res = Response(status=200)
    return res

app.run(debug=False, port='')

