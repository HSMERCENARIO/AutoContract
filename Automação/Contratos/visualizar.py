from docx import Document
import os
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
data_HOJE = datetime.date.today()
data = data_HOJE.strftime('%d de %B de %Y')

doc = Document("modelo.docx")

def pedir_nome():
    while True:
        NOME = input("Digite o nome completo: ").strip()

        if NOME:
            return NOME

        print("O nome não pode ficar vazio. Tente novamene.")

def pedir_cpf():
    while True:
        CPF = input("Digite o CPF: ").strip()

        CPF_numeros = CPF.replace(".","").replace("-","")

        if CPF_numeros.isdigit() and len(CPF_numeros) == 11:
            return CPF

        print("CPF inválido. Digite um CPF com 11 números.")

def pedir_cargo():
    while True:
        cargo = input("Digite o cargo: ").strip()

        if cargo:
            return cargo

        print("O cargo não pode ficar vazio. Tente novamente.")

def pedir_RG():
    while True:
        RG = input("Digite o RG: ").strip()

        RG_numeros = RG.replace(".","").replace("-","")

        if RG_numeros.isdigit():
            return RG 
        print("Digite um RG válido!")


NOME = pedir_nome()
CARGO = pedir_cargo()
RG = pedir_RG()
ORG = input("Digite o orgão emissor do RG: ")
CPF = pedir_cpf()
ENDR = input("Digite o endereço: ")
NUMERO = input("Digite o numero do endereço: ")
BAIRRO = input("Digite o bairro: ")
CIDADE = input("Digite a cidade: ")
ESTADO = input("Digite o estado(Ex:SP): ")
CEP =  input("Digite o cep: ")
DATA = data

campos = {
    "{{NOME}}": NOME,
    "{{CARGO}}": CARGO,
    "{{RG}}": RG,
    "{{ORG}}": ORG,
    "{{CPF}}": CPF,
    "{{ENDR}}": ENDR,
    "{{NUMERO}}": NUMERO,
    "{{BAIRRO}}": BAIRRO,
    "{{CIDADE}}": CIDADE,
    "{{ESTADO}}": ESTADO,
    "{{CEP}}": CEP,
    "{{DATA}}": DATA
}

for paragrafo in doc.paragraphs:
    for campo, valor in campos.items():
        if campo in paragrafo.text:
            paragrafo.text = paragrafo.text.replace(
                campo,
                valor
            )





def limpar_nome_arquivo(NOME):
    caracteres_proibidos = '\\/:*?"<>|'

    for caracteres in caracteres_proibidos:
        NOME = NOME.replace(caracteres, "")

    NOME = NOME.replace(" ", "_")

    return NOME

pasta = "Contratos Gerados"

nome_limpo = limpar_nome_arquivo(NOME)

nome_arquivo = f"Contrato_{nome_limpo}.docx"

os.makedirs(pasta, exist_ok=True)

caminho_arquivo = os.path.join(pasta,nome_arquivo)

doc.save(caminho_arquivo)

print("Contrato preenchido com sucesso!")
print("Contrato criado com sucesso!")