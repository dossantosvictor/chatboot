import openai

chave_api = 'CHAVE_DE_API_AQUI'

openai.api_key = chave_api

def obter_resposta_pergunta(pergunta):    
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "user", "content": pergunta}],        
        max_tokens=100  
    )

    
    return resposta.choices[0]["message"]


pergunta_usuario = input("Faça uma pergunta: ")
resposta_chatgpt = obter_resposta_pergunta(pergunta_usuario)
print("Resposta:", resposta_chatgpt)