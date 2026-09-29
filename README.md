# Automação de Contratos com Python

Projeto desenvolvido em Python para automatizar o preenchimento e a geração de contratos em formato `.docx`.

A aplicação recebe os dados do usuário pelo terminal, valida algumas informações, preenche um modelo de contrato com os dados fornecidos e salva o documento gerado automaticamente em uma pasta específica.

## Objetivo

O objetivo deste projeto é praticar Python desenvolvendo uma automação simples que pode facilitar tarefas repetitivas de preenchimento de documentos em um ambiente empresarial.

## Funcionalidades

- Coleta de dados pelo terminal;
- Validação básica de nome;
- Validação de CPF;
- Validação de RG;
- Validação de CEP;
- Preenchimento automático de um modelo `.docx`;
- Substituição de campos utilizando um dicionário;
- Criação automática da pasta de contratos gerados;
- Geração automática do nome do arquivo;
- Limpeza de caracteres inválidos no nome do arquivo;
- Exibição do caminho onde o contrato foi salvo.

## Tecnologias utilizadas

- Python
- python-docx
- Microsoft Word

## Estrutura do projeto

```text
Automação/
└── Contratos/
    ├── modelo.docx
    ├── visualizar.py
    ├── README.md
    └── Contratos Gerados/
```

A pasta Contratos Gerados será criada automaticamente após o primeiro contrato ser gerado.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/HSMERCENARIO/AutoContract
```

Entre na pasta do projeto:

```bash
cd AutoContract
```

Instale a biblioteca necessária:

```bash
pip install python-docx
```

## Como executar

Execute o arquivo Python:

```bash
python visualizar.py
```

O programa solicitará os dados necessários pelo terminal.

Após o preenchimento, o contrato será salvo automaticamente dentro da pasta:

```text
Contratos Gerados/
```

## Exemplo

Durante a execução, o programa solicita informações como:

```text
Digite o nome completo:
Digite o cargo:
Digite o RG:
Digite o órgão emissor do RG:
Digite o CPF:
Digite o endereço:
Digite o número do endereço:
Digite o bairro:
Digite a cidade:
Digite o estado:
Digite o CEP:
```

Depois de preencher os dados, o programa gera automaticamente o contrato utilizando o arquivo `modelo.docx`.

## Autor

Desenvolvido por Kauã como projeto para praticar Python e automatizar tarefas repetitivas.