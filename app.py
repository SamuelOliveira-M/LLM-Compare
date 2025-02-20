# main.py
from src.services.anthropic_service import AnthropicService
from src.services.gemini_service import GeminiService
from src.services.mistral_service import MistralService


import os
from dotenv import load_dotenv

load_dotenv()

def main(pergunta):
    
    api_anthropic = os.getenv("ANTHROPIC")
    api_github = os.getenv("GEMINI_KEY")
    api_mistral = os.getenv("MISTRAL_API_KEY")


    if not api_anthropic and not api_github and not api_mistral:
        raise ValueError("A chave não foi encontrada. Configure o .env corretamente.")

    # Criar uma instância do serviço
    anthropic_service = AnthropicService(api_anthropic)
    gemini_service = GeminiService(api_github)
    mistral_service = MistralService(api_mistral)


    mensagem = pergunta

    resposta_anthropic = anthropic_service.gerar_resposta(mensagem)
    resposta_opneai = gemini_service.gerar_resposta(mensagem)
    resposta_mistral = mistral_service.gerar_resposta(mensagem)


    analict_prompt = f"""Analise as seguintes respostas fornecidas por diferentes modelos de IA para a pergunta: 'Quantos planetas existem no nosso sistema solar?'. Avalie cada resposta considerando três critérios principais:

    1️ Precisão da Informação – A resposta apresenta o número correto de planetas e informações factualmente corretas? Há erros ou omissões?  
    2️ Clareza e Coerência – A resposta é direta e compreensível? Está bem estruturada e organizada logicamente?  
    3️ Criatividade ou Profundidade – A resposta adiciona contexto interessante, curiosidades ou explicações adicionais que enriquecem a resposta?  

    Para cada critério, atribua uma nota de 0 a 10 e calcule a média das avaliações. Retorne **apenas** o seguinte texto, sem explicações adicionais:

    ### Conclusão

    - Anthropic: Precisão (X), Clareza (X), Criatividade (X)  
    - Gemini: Precisão (X), Clareza (X), Criatividade (X)  
    - Mistral: Precisão (X), Clareza (X), Criatividade (X)  

    O modelo com a maior média de pontuação e que melhor respondeu à pergunta foi: [NOME DO MODELO VENCEDOR].

    Agora, avalie as seguintes respostas:

    Resposta da Anthropic: {resposta_anthropic}  
    Resposta da Gemini: {resposta_opneai}  
    Resposta da Mistral: {resposta_mistral}  
    """

    
    response_analysis_anthropic = anthropic_service.gerar_resposta(analict_prompt)
    response_analysis_gemini = gemini_service.gerar_resposta(analict_prompt)
    response_analysis_mistral = mistral_service.gerar_resposta(analict_prompt)

    ranking_prompt = f"""Some os pontos atribuídos a cada IA e ordene do maior para o menor.
        Respostas das avaliações:

        Anthropic: {response_analysis_anthropic}
        Gemini: {response_analysis_gemini}
        Mistral: {response_analysis_mistral}

        Retorne apenas um ranking final no seguinte formato, NÃO inclua explicações adicionais:

        1. [Modelo] - X pontos  
        2. [Modelo] - X pontos  
        3. [Modelo] - X pontos  
        """


    ranking_geral = gemini_service.gerar_resposta(ranking_prompt)

    print(f"""
------------------------------------------------------------------
RANKING DA PERGUNTA: {pergunta}
------------------------------------------------------------------
{ranking_geral}
\n
    """)

    

if __name__ == "__main__":
    
    perguntas = [
        "Como funciona o processo de fotossíntese nas plantas?",
        "Quem foi Albert Einstein?",
        "Explique a teoria da relatividade de forma simples.",
        "Quantos planetas existem no nosso sistema solar?"
    ]
    
    for pergunta in perguntas:
        main(pergunta)
