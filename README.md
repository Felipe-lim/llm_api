---

## README.md

# API de Integração de Modelos de Linguagem

Esta é uma API construída com FastAPI que permite a interação com vários modelos de linguagem, incluindo GPT (OpenAI), Gemini, Cohere e Anthropic. A API permite o envio de prompts para esses modelos e o recebimento de respostas geradas automaticamente.

## Tabela de Conteúdos

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
  - [Endpoints Disponíveis](#endpoints-disponíveis)
- [Exemplos de Requisições](#exemplos-de-requisições)
- [Licença](#licença)

## Pré-requisitos

- Python 3.7 ou superior
- Chaves de API válidas para os seguintes serviços:
  - OpenAI
  - Gemini (Google Generative AI)
  - Cohere
  - Anthropic

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/sua-api.git
   cd sua-api
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```env
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

Substitua `your_openai_api_key_here`, `your_gemini_api_key_here`, `your_cohere_api_key_here` e `your_anthropic_api_key_here` pelas suas chaves de API respectivas.

## Uso

Para iniciar a API, execute o comando:

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

### Endpoints Disponíveis

- `GET /`: Endpoint de boas-vindas para verificar se a API está ativa.
- `POST /gpt/`: Envia um prompt para o modelo GPT da OpenAI.
- `POST /gemini/`: Envia um prompt para o modelo Gemini (Google Generative AI).
- `POST /cohere/`: Envia um prompt para o modelo Cohere.
- `POST /anthropic/`: Envia um prompt para o modelo Anthropic.

## Exemplos de Requisições

### 1. Requisição para o GPT da OpenAI

Endpoint: `/gpt/`

#### Corpo da Requisição (JSON)

```json
{
  "prompt": "Escreva um poema sobre o espaço.",
  "max_tokens": 100,
  "temperature": 0.7
}
```

### 2. Requisição para o Gemini

Endpoint: `/gemini/`

#### Corpo da Requisição (JSON)

```json
{
  "prompt": "Explique a teoria da relatividade de forma simples.",
  "max_tokens": 100,
  "temperature": 0.5
}
```

### 3. Requisição para o Cohere

Endpoint: `/cohere/`

#### Corpo da Requisição (JSON)

```json
{
  "prompt": "Quais são as vantagens do aprendizado de máquina?",
  "max_tokens": 100,
  "temperature": 0.6
}
```

### 4. Requisição para o Anthropic

Endpoint: `/anthropic/`

#### Corpo da Requisição (JSON)

```json
{
  "prompt": "Descreva uma cena de um nascer do sol em uma floresta tropical.",
  "max_tokens": 100,
  "temperature": 0.9
}
```

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
