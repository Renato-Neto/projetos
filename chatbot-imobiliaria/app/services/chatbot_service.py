from langchain.chains import LLMChain  # Importando da forma correta
from langchain.prompts import PromptTemplate
from gpt4all import GPT4All
import os

# Caminho onde o modelo GPT-4All está armazenado (relativo ao diretório raiz do projeto)
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'gpt4all-j-v1.3-groovy.bin')

# Carregar o modelo GPT-4All usando o caminho do arquivo
try:
    gpt4all_model = GPT4All(model_name=MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Erro ao carregar o modelo GPT-4All: {e}")

# Definir um wrapper para GPT-4All para ser compatível com Langchain
class GPT4AllLLM:
    def __init__(self, model):
        self.model = model
    
    def _call(self, prompt: str) -> str:
        """Método que envia o prompt para o GPT-4All e obtém a resposta."""
        try:
            response = self.model.generate(prompt, max_tokens=100, temperature=0.7)
            return response
        except Exception as e:
            return f"Erro ao gerar resposta: {e}"

# Criar o modelo Langchain usando GPT-4All
llm = GPT4AllLLM(gpt4all_model)

# Definir o template do prompt para ser usado com Langchain
template = """Você é um assistente imobiliário prestativo. Responda à seguinte pergunta:
{question}
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template,
)

# Criar a cadeia LLMChain com o modelo e o prompt
llm_chain = LLMChain(
    llm=llm, 
    prompt=prompt
)

def process_user_query(question: str) -> str:
    """
    Função que processa a pergunta do usuário e retorna uma resposta gerada pelo GPT-4All via Langchain.
    """
    try:
        # Gerar a resposta usando Langchain com GPT-4All como modelo
        response = llm_chain.run({"question": question})
        return response
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"
