import google.generativeai as genai
from src.interface.ia_services import IAService

class GeminiService(IAService):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)

    def gerar_resposta(self, mensagem: str) -> str:
        modelo = genai.GenerativeModel("gemini-1.5-flash")

        resposta = modelo.generate_content(
            mensagem,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.9,
                "max_output_tokens": 1024,
            }
        )

        if resposta.text:
            return resposta.text
        else:
            return "Não foi possível gerar uma resposta."
