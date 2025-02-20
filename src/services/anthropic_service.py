# src/services/openai_service.py
from src.interface.ia_services import IAService
import anthropic

class AnthropicService(IAService):
    
    def __init__(self, api_key: str):
       
        self.client = anthropic.Anthropic(api_key=api_key)

    def gerar_resposta(self, mensagem: str) -> str:
       
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            temperature=0.7,
            top_p=0.9,       
            messages=[{"role": "user", "content": mensagem}]
        )
        if response and response.content:
            return response.content[0].text 
        
        return "Erro: resposta vazia da API."