from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
import google.generativeai as genai
import cohere
import anthropic

from dotenv import load_dotenv
 
# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Chaves de API
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(OPENAI_API_KEY)
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Inicializa o FastAPI
app = FastAPI()

# Modelos de dados para as requisições
class GPTRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    temperature: float = None # between 0 and 2

class GeminiRequest(BaseModel):
    prompt: str
    max_tokens: int = 100 # ainda não está funcionando / poderia fazer o max tokens de entrada manualmente
    temperature: float = None # between 0 and 1

class CohereRequest(BaseModel):
    prompt: str
    max_tokens: int = 100 # ainda não está funcionando / poderia fazer o max tokens de entrada manualmente
    temperature: float = None # between 0 and 1

class AnthropicRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    temperature: float = None # between 0 and 2

@app.get("/")
def read_root():
    return {"message": "Welcome to the GPT, Gemini, Cohere and Anthropic API"}

@app.post("/gpt/")
def call_gpt(request: GPTRequest):

    client = OpenAI() # setting api key

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": request.prompt,
            },
        ],
        max_tokens = request.max_tokens,
        temperature = request.temperature,
    )
    
    return (completion.choices[0].message.content)
    

@app.post("/gemini/")
def call_gemini(request: GeminiRequest):

    genai.configure(api_key=GEMINI_API_KEY) # setting api key
    model = genai.GenerativeModel('gemini-1.5-flash')

    generation_c = genai.types.GenerationConfig(
        max_output_tokens=request.max_tokens, 
        temperature=request.temperature)

    response = model.generate_content(request.prompt, generation_config=generation_c)
    return response.text

@app.post("/cohere/")
def call_cohere(request: CohereRequest):

    co = cohere.Client(api_key=COHERE_API_KEY)

    response = co.chat(
        model="command-r-plus",
        message=request.prompt,
        temperature=request.temperature
        )

    return response.text

@app.post("/anthropic/")
def call_anthropic(request: AnthropicRequest):
    
    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=request.max_tokens,
        temperature=request.temperature,
        #system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": request.prompt
                    }
                ]
            }
        ]
    )

    return response.content[0].text
