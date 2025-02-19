import google.generativeai as genai
from src.interface.ia_services import IAService

class GeminiService(IAService):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)

    def gerar_resposta(self, mensagem: str) -> str:
        modelo = genai.GenerativeModel("gemini-1.5-flash")  # Instancia o modelo corretamente

        resposta = modelo.generate_content(
            mensagem,  # O prompt vai aqui
            generation_config={
                "temperature": 1.0,
                "top_p": 1.0,
                "max_output_tokens": 1000,
            }
        )

        # Verifica se a resposta foi gerada com sucesso e retorna o texto.
        if resposta.text:
            return resposta.text
        else:
            return "Não foi possível gerar uma resposta."  # Lida com erros
