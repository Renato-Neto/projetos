from pydantic import BaseModel

class UserQuery(BaseModel):
    """
    Modelo de dados para a requisição do usuário.
    """
    question: str
