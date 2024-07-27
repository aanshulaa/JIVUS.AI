from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import openai

app = Flask(__name__)

# Initialize OpenAI or other LLM
openai.api_key = 'your-api-key'  # Replace 'your-api-key' with your actual API key

def get_product_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract relevant information from the product page
    data = {
        'features': soup.find('div', class_='features').text if soup.find('div', class_='features') else 'Not available',
        'dimensions': soup.find('div', class_='dimensions').text if soup.find('div', class_='dimensions') else 'Not available',
        # Add more data extraction as needed
    }
    return data

def generate_response(question, data):
    # Use LLM or any text generation tool to answer based on data
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following question based on the provided product data:\nQuestion: {question}\nProduct Data: {data}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/process', methods=['POST'])
def process():
    if 'questionsFile' not in request.files or 'websiteUrl' not in request.form:
        return jsonify({'error': 'Missing file or URL'}), 400

    questions_file = request.files['questionsFile']
    website_url = request.form['websiteUrl']

    if not questions_file or not website_url:
        return jsonify({'error': 'File or URL not provided'}), 400

    questions = questions_file.read().decode('utf-8').splitlines()
    product_data = get_product_data(website_url)

    responses = [generate_response(q, product_data) for q in questions]
    return jsonify({'responses': responses})

if __name__ == '__main__':
    app.run(debug=True)


