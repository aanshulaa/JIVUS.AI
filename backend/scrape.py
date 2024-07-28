import requests
from bs4 import BeautifulSoup

def scrape_product_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant information (example)
    product_info = {
        'remote_control': soup.find('div', {'id': 'remote-control'}).text.strip(),
        'scheduling': soup.find('div', {'id': 'scheduling'}).text.strip(),
        'security_features': soup.find('div', {'id': 'security-features'}).text.strip(),
        'dimensions': soup.find('div', {'id': 'dimensions'}).text.strip(),
        'design': soup.find('div', {'id': 'design'}).text.strip(),
        'countdown_timer': soup.find('div', {'id': 'countdown-timer'}).text.strip(),
    }
    return product_info

