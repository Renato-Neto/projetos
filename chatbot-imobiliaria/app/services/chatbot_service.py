from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Carregar modelo Hugging Face (exemplo: GPT-2 em português)
model_name = "pierreguillou/gpt2-small-portuguese"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Definir template do prompt
template = """Você é um assistente imobiliário prestativo. Responda à seguinte pergunta:\n{question}\n"""
prompt = PromptTemplate(input_variables=["question"], template=template)

# Cri
# ar classe para usar o modelo na CPU


class HuggingFaceLLM:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def _call(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
# Inicializar o modelo com LangChain
llm=  HuggingFaceLLM(model, tokenizer)


llm_chain = LLMChain(llm=llm, prompt=prompt)


# Função para processar a consulta do usuário
def process_user_query(question: str) -> str:
    try:
        response = llm_chain.run({"question": question})
        return response
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"
