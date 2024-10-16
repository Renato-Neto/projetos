from langchain import LLMChain
from langchain.prompts import PromptTemplate
from gpt4all import GPT4All

# Caminho onde o modelo GPT-4All está armazenado
MODEL_PATH = "./models/gpt4all-lora-quantized.bin"

# Carregar o modelo GPT-4All
gpt4all_model = GPT4All(model_path=MODEL_PATH)

# Definir um wrapper para GPT-4All para ser compatível com Langchain
class GPT4AllLLM:
    def __init__(self, model):
        self.model = model
    
    def _call(self, prompt: str) -> str:
        """Método que envia o prompt para o GPT-4All e obtém a resposta."""
        return self.model.generate(prompt)

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
