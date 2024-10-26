🛒 Scraper de Produtos

Este projeto é um scraper de produtos que utiliza Flask e Selenium para capturar informações de produtos a partir de uma URL fornecida. A interface simples permite que o usuário insira uma URL de uma página de produtos, visualize o progresso do scraping e obtenha os detalhes dos produtos, como nome e preço.
✨ Funcionalidades

    Interface Intuitiva: Basta colar a URL e clicar em "Buscar Produtos".
    Feedback Visual: Ícone de carregamento enquanto os dados são coletados.
    Validação de URL: Verifica a URL e adiciona https:// automaticamente se necessário.
    Resultado Organizado: Exibe o título e preço dos produtos encontrados em uma lista clara.

📋 Pré-requisitos

    Python 3.x
    Firefox e GeckoDriver (necessário para o Selenium)

Instalando o GeckoDriver

Baixe o GeckoDriver aqui e certifique-se de que ele esteja no PATH ou especifique o caminho no código (scraper_selenium.py).
⚙️ Instalação

    Clone este repositório:

    bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie um ambiente virtual e ative-o:

bash

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Instale as dependências:

bash

pip install -r requirements.txt

Atualize o caminho do GeckoDriver em scraper_selenium.py, caso necessário:

python

    service = Service(r"C:\caminho\para\geckodriver.exe")

🚀 Como Executar

    Inicie o servidor Flask:

    bash

python app.py

Abra o navegador e acesse:

arduino

    http://127.0.0.1:5000/

    Insira a URL de uma página de produtos e clique em "Buscar Produtos".

📂 Estrutura do Projeto

    app.py: Configuração e rotas do servidor Flask.
    scraper_selenium.py: Código para capturar dados da página usando Selenium.
    templates/index.html: Interface HTML para inserir a URL e visualizar os resultados.
    static/styles.css: Estilos CSS para a interface.

🛠 Tecnologias Utilizadas

    Flask para a criação da API e interface web.
    Selenium para automação e scraping de páginas web.
    HTML/CSS para a interface do usuário.

📄 Exemplo de Resposta

Aqui está um exemplo do formato de resposta com produtos encontrados:

json

{
    "products": [
        {"title": "Produto A", "price": "R$ 100,00"},
        {"title": "Produto B", "price": "R$ 150,00"}
    ]
}

🔧 Solução de Problemas

    Timeout: Certifique-se de que a página de produtos está acessível e funcional.
    URL inválida: URLs sem http:// ou https:// recebem automaticamente o https://.
    GeckoDriver não encontrado: Ajuste o caminho do GeckoDriver no scraper_selenium.py ou adicione-o ao PATH do sistema.