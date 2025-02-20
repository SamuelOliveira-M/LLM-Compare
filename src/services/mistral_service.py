from src.interface.ia_services import IAService
from mistralai import Mistral

class MistralService(IAService):
    
    def __init__(self, api_key: str):
        self.client = Mistral(api_key=api_key)


    def gerar_resposta(self, mensagem: str) -> str:
        
        response = self.client.chat.complete(
            model = "mistral-large-latest",
            max_tokens=1024,
            temperature=0.7,
            top_p=0.9,       
            messages=[{"role": "user", "content": mensagem}]
        )

        if response:
            return response.choices[0].message.content
        
        return "Erro: resposta vazia da API."