from docx import Document

doc = Document("modelo.docx")

NOME = input("Digite o Nome completo: ")
RG = input("Digite o RG: ")
ORG = input("Digite o orgão emissor do RG com pontuação: ")
CPF = input("Digite o CPF com pontuação: ")
ENDR = input("Digite o endereço: ")
NUMERO = input("Digite o numero do endereço: ")
BAIRRO = input("Digite o bairro: ")
CIDADE = input("Digite a cidade: ")
ESTADO = input("Digite o estado(Ex:SP): ")
CEP =  input("Digite o cep: ")

for paragrafo in doc.paragraphs:
    if "{{NOME}}" in paragrafo.text:
        paragrafo.text = paragrafo.text.replace(
            "{{NOME}}",
            NOME
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

print("Contrato preenchido com sucesso!")
doc.save(f"Contrato_{NOME}.docx")
print("Contrato criado com sucesso!")