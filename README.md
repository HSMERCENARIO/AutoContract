ENGLISH:

# Contract Automation with Python

A Python project developed to automate the filling and generation of contracts in `.docx` format.

The application receives user data through the terminal, validates some information, fills out a contract template with the provided data, and automatically saves the generated document in a specific folder.

## Objective

The objective of this project is to practice Python by developing a simple automation that can help reduce repetitive document-filling tasks in a business environment.

## Features

- Collects data through the terminal;
- Basic name validation;
- CPF validation;
- RG validation;
- ZIP code validation;
- Automatic filling of a `.docx` template;
- Placeholder replacement using a dictionary;
- Automatic creation of the generated contracts folder;
- Automatic file name generation;
- Removal of invalid characters from file names;
- Displays the path where the contract was saved.

## Technologies Used

- Python
- python-docx
- Microsoft Word

## Project Structure

```text
Automation/
└── Contracts/
    ├── modelo.docx
    ├── visualizar.py
    ├── README.md
    └── Contratos Gerados/
```

The `Contratos Gerados` folder will be created automatically after the first contract is generated.

## Installation

Clone the repository:

```bash
git clone https://github.com/HSMERCENARIO/AutoContract
```

Navigate to the project folder:

```bash
cd AutoContract
```

Install the required library:

```bash
pip install python-docx
```

## How to Run

Run the Python file:

```bash
python visualizar.py
```

The program will request the required information through the terminal.

After the information is provided, the contract will be automatically saved inside the:

```text
Contratos Gerados/
```

folder.

## Example

During execution, the program requests information such as:

```text
Enter your full name:
Enter the job title:
Enter the RG:
Enter the RG issuing authority:
Enter the CPF:
Enter the address:
Enter the address number:
Enter the neighborhood:
Enter the city:
Enter the state:
Enter the ZIP code:
```

After entering the required information, the program automatically generates the contract using the `modelo.docx` template.

## Author

Developed by Kauã as a project to practice Python and automate repetitive tasks.



🇧🇷 PORTUGUÊS:

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