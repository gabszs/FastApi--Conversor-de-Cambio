# FastAPI Currency Converter

Este é um projeto para converter moedas usando a API Alpha Vantage. O projeto utiliza o FastAPI para lidar com as solicitações e respostas HTTP.

## 🚀 Começando

The API allows for both synchronous and asynchronous conversions, and accepts a from_currency and a list of to_currencies along with the value to be converted. The endpoints follow the format /converter/{from_currency}, /converter/async/{from_currency} and converter/async/v2/{from_currency} + bodyJson for synchronous and asynchronous conversions, respectively.

To use this project, you will need to add your Alpha Vantage API key as an environment variable in a .env file in the root directory of the project. The name of the environment variable should be ALPHAVANTAGE_APIKEY.

### 📋 Pré-requisitos

Para o projeto, somente e necessario o PYPOETRY e PYENV estalados e sua maquina, seja ela linux ou WIndonws, os pacotes e dependencias seram adionados automaticamente via POETRY

### 🔧 Instalação

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Para configurar e baixar o projeto localmente, siga os passos:
1º Certifique-se de ter o git instaldo localmente

2º Abra o terminal ou o prompt de comando e navegue até o diretório em que deseja clonar o repositório

3º Obtenha o URL do repositório que deseja clonar. Normalmente, você pode encontrá-lo na página principal do repositório no GitHub
ou em outra plataforma de hospedagem de código.

4º Use o comando git clone seguido do URL do repositório para cloná-lo em seu diretório local. Por exemplo, se o URL do repositório for https://github.com/username/repository, o comando será:

```
git clone https://github.com/username/repository
```

5º Aguarde até que o Git termine de clonar o repositório. Isso criará uma pasta com o nome do repositório no seu diretório atual.

6º Digite no console local o comando para inicial o PYPOETRY:

```
poetry shell
```

E repita o seguinte codigo para instalar as dependecias:

```
poetry install
```

Apos isso, se configurado corretamente, tente iniciar o uvicorn e assim ter acesso aos ENDPOINTS (--reload caso queira a funcao hot reload ativada)

```
uvicorn main:app --reload
```

## ⚙️ Executando os testes

Para executar os testes, em alguma ferramenta API Client de preferencia, tente as seguintes requisicoes (a rota 127.0.0.1 foi a usada localmente, caso tenha configurado outra, troque tambem o a URL base do ENDPOINT):

Para a rota sincrona:

```
127.0.0.1:8000/converter/BRL?to_currencies=USD,GBP,JPY&price=10
```

Para a primeira rota assincrona:

```
127.0.0.1:8000/converter/async/BRl?to_currencies=USD,GBP&price=10
```

Para a segunda rota assincrona, adicione tambem o body parameter como um json:

Modelo Json:

```
{
  "price": 0,
  "to_currencies": [
    "string"
  ]
}
```

EndPoint:

```
127.0.0.1:8000/converter/async/BRl?to_currencies=USD,GBP&price=10
```

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

- [FastApi](http://www.dropwizard.io/1.0.2/docs/) - O framework Rest usado para construir os endpoints
- [Poetry](https://python-poetry.org/docs/) - Gerente de Dependência e de ambientes vituais
- [Pyenv](https://github.com/pyenv/pyenv) - Usado para implemntar o python no ambiente de desinvolvimento

## 📌 Versionamento

Foi usado [Git](https://git-scm.com/doc) para controle de versão.

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

- **Gabriel Carvalho** - Implementacao da API - [GabrielCarvalho](https://github.com/gabszs)

- **linkedin** - [Gabriel Carvalho](https://www.linkedin.com/in/gabzsz/)
