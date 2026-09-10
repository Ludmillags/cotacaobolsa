# Cotação de Moedas em Python

Aplicação desktop desenvolvida em **Python + Tkinter** para consultar cotações atualizadas de **Dólar (USD), Euro (EUR) e Bitcoin (BTC)** em relação ao Real brasileiro (BRL).

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-4B8BBE) ![API](https://img.shields.io/badge/API-AwesomeAPI-0A66C2) ![Portfolio](https://img.shields.io/badge/Portfolio-Project-19a558)

## Objetivo do projeto

O projeto foi criado para praticar integração com API, tratamento de respostas JSON e criação de interface gráfica em Python. A aplicação consulta dados externos em tempo real e apresenta as cotações em uma interface simples para o usuário.

## Funcionalidades

- consulta de USD/BRL, EUR/BRL e BTC/BRL;
- interface gráfica com Tkinter;
- consumo de API REST com `requests`;
- tratamento de erros de conexão e resposta da API;
- formatação das cotações para leitura mais clara;
- botão para atualização manual das cotações.

## Tecnologias

- Python
- Tkinter
- Requests
- JSON
- REST API

## Como executar

1. Instale o Python 3.10 ou superior.
2. Clone este repositório.
3. Instale a dependência:

```bash
pip install -r requirements.txt
```

4. Execute:

```bash
python app.py
```

## Estrutura do projeto

```text
cotacaobolsa/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── codigopython       # versão original do estudo
└── main.exe           # executável legado
```

## O que este projeto demonstra

Este projeto demonstra fundamentos importantes para automação e análise de dados: consumo de APIs, manipulação de dados estruturados, construção de uma interface simples e tratamento de situações de erro.

## Evolução do projeto

A versão atual organiza e melhora o código original, mantendo o projeto simples e didático. Evoluções possíveis incluem histórico de cotações, gráficos, exportação para Excel/CSV e criação de uma versão web.

## Fonte de dados

As cotações são consultadas pela API pública AwesomeAPI. Como os dados dependem de uma fonte externa, disponibilidade e valores podem variar conforme o serviço.

## Autoria

Projeto de portfólio por **Ludmilla G. Costa**.
