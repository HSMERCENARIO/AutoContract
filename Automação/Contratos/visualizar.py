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



NOME = pedir_nome()
CARGO = pedir_cargo()
RG = input("Digite o RG com pontuação: ")
ORG = input("Digite o orgão emissor do RG: ")
CPF = pedir_cpf()
ENDR = input("Digite o endereço: ")
NUMERO = input("Digite o numero do endereço: ")
BAIRRO = input("Digite o bairro: ")
CIDADE = input("Digite a cidade: ")
ESTADO = input("Digite o estado(Ex:SP): ")
CEP =  input("Digite o cep: ")
DATA = data

for paragrafo in doc.paragraphs:
    if "{{NOME}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{NOME}}",
            NOME
        )

for paragrafo in doc.paragraphs:
    if "{{CARGO}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{CARGO}}",
            CARGO
        )

for paragrafo in doc.paragraphs:
    if "{{RG}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{RG}}",
            RG
        )

for paragrafo in doc.paragraphs:
    if "{{ORG}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{ORG}}",
            ORG
        )

for paragrafo in doc.paragraphs:
    if "{{CPF}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{CPF}}",
            CPF
        )

for paragrafo in doc.paragraphs:
    if "{{ENDR}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{ENDR}}",
            ENDR
        )

for paragrafo in doc.paragraphs:
    if "{{NUMERO}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{NUMERO}}",
            NUMERO
        )

for paragrafo in doc.paragraphs:
    if "{{BAIRRO}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{BAIRRO}}",
            BAIRRO
        )

for paragrafo in doc.paragraphs:
    if "{{CIDADE}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{CIDADE}}",
            CIDADE
        )

for paragrafo in doc.paragraphs:
    if "{{ESTADO}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{ESTADO}}",
            ESTADO
        )

for paragrafo in doc.paragraphs:
    if "{{CEP}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{CEP}}",
            CEP
        )

for paragrafo in doc.paragraphs:
    if "{{DATA}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{DATA}}",
            DATA
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