🚀 Experimente e descubra qual LLM entrega as melhores respostas para suas perguntas!
# LLM-Compare

## Introdução ao Projeto:
O LLM Compare é uma aplicação que acessa e compara respostas geradas por pelos Modelos de Linguagem de Grande Escala (LLMs) GEMINI, MISTRAL, ANTHROPIC. O objetivo é fornecer uma análise comparativa da qualidade das respostas para uma mesma pergunta, permitindo avaliar pontos fortes e limitações de cada modelo.

## Critérios de Avaliação

As respostas dos modelos são analisadas com base em três critérios principais:

* 1️⃣ Precisão da Informação – A resposta apresenta informações corretas e sem erros? Há omissões ou inconsistências? 
* 2️⃣ Clareza e Coerência – A resposta é direta, compreensível e bem estruturada?
* 3️⃣ Criatividade ou Profundidade – A resposta adiciona contexto interessante, curiosidades ou explicações adicionais que enriquecem a resposta?

Cada critério recebe uma nota de 0 a 10, e o modelo com a maior média de pontuação é destacado como o melhor para aquela pergunta específica.

A avaliação é feita automaticamente por outro modelo de IA, garantindo uma análise imparcial entre as respostas dos concorrentes.


## 🛠️ Tecnologias utilizadas

* Python
* VScode
  
## 🛠️ Instalação e Configuração

Siga os passos abaixo para baixar, instalar e rodar a aplicação localmente.

### 1️⃣ Clonar o Repositório

git clone https://github.com/SamuelOliveira-M/LLM-Compare.git
cd LLM-Compare

### 2️⃣ Criar e Configurar o Ambiente Virtual (Opcional, mas Recomendado)

Se estiver usando Python, crie um ambiente virtual para evitar conflitos de dependências:

python -m venv venv

Ative o ambiente virtual:

    No Windows:

venv\Scripts\activate

No Linux/macOS:

    source venv/bin/activate

### 3️⃣ Instalar as Dependências

Para instalar as bibliotecas necessárias, rode:

    pip install dotenv

    pip install anthropic

    pip install google-generativeai

    pip install Mistral

    pip install mistralai


### 4️⃣ Configurar as Credenciais das APIs

O projeto utiliza diferentes LLMs, então é necessário criar um arquivo .env com suas chaves de API.

Crie um arquivo chamado .env na raiz do projeto e adicione as credenciais :

```

```
Adicione o codigo acima dentro do arquivo .env

### 5️⃣ Executar a Aplicação

* python app.py


OBS: As variáveis ANTHROPIC, GEMINI_KEY e MISTRAL_API_KEY irar funcionar até o dia 21 de fevereiro de 2025.
