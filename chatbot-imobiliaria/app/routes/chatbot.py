from fastapi import APIRouter, HTTPException
from app.services.chatbot_service import process_user_query
from pydantic import BaseModel

# Definindo a rota para o chatbot
router = APIRouter()

# Modelo para a requisição do usuário
class UserQuery(BaseModel):
    question: str

@router.post("/chatbot/")
async def chatbot_response(user_query: UserQuery):
    """
    Endpoint que recebe a pergunta do usuário e retorna a resposta do chatbot.
    """
    try:
        # Processar a pergunta do usuário e obter a resposta
        response = process_user_query(user_query.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a solicitação: {e}")
