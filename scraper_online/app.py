from flask import Flask, jsonify, request, render_template
from scraper_selenium import fetch_products_from_url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re

app = Flask(__name__)

# Validação de URL
def is_valid_url(url):
    """Verifica se a URL fornecida tem um formato válido"""
    pattern = re.compile(
        r'^(https?://)?'  # protocolo (opcional)
        r'([a-zA-Z0-9-]+\.)?'  # subdomínio (opcional)
        r'([a-zA-Z0-9-]+\.[a-zA-Z]{2,6})'  # domínio
        r'(/[\w\-./?%&=]*)?'  # caminho (opcional)
    )
    return pattern.match(url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    # Verifica se a URL possui protocolo; se não, adiciona "https://"
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    if not is_valid_url(url):
        return jsonify({"error": "URL inválida"}), 400

    # Realiza o scraping
    products = fetch_products_from_url(url)
    if isinstance(products, dict) and 'error' in products:
        return jsonify(products), 500  # Retorna erro se houver falha no scraping
    
    return jsonify(products=products), 200
  
if __name__ == "__main__":
    app.run(debug=True)
