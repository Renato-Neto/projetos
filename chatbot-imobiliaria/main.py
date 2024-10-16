from fastapi import FastAPI
from app.routes import chatbot

# Inicializando o FastAPI
app = FastAPI()

# Incluindo a rota do chatbot
app.include_router(chatbot.router)

# Rota inicial apenas para verificar se o servidor está rodando
@app.get("/")
async def root():
    return {"message": "API de atendimento imobiliário está ativa!"}
