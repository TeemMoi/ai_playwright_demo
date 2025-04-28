from app.models import get_model
from app.retriever import retrieve_examples
import os
import re  # <--- Tämä tarvitaan URLin tunnistukseen
from bs4 import BeautifulSoup
import requests

from models import get_model
from retriever import retrieve_examples

def extract_url(text):
    url_pattern = r'https?://[^\s]+'
    match = re.search(url_pattern, text)
    return match.group(0) if match else None

def build_prompt(user_prompt, page_elements=None):
    examples = retrieve_examples(user_prompt)
    example_block = "\n\n".join([f"Prompt: {e['prompt']}\nCode:\n{e['code']}" for e in examples])

    element_block = ""
    if page_elements:
        buttons = ", ".join(page_elements.get('buttons', []))
        inputs = ", ".join(page_elements.get('inputs', []))
        links = ", ".join(page_elements.get('links', []))

        element_block = (
            "\n\nSivulta löytyi seuraavat elementit:\n"
            f"- Nappulat: {buttons}\n"
            f"- Lomakekentät: {inputs}\n"
            f"- Linkit: {links}\n"
        )

    best_practices = ""
    best_practices_path = os.path.join(os.path.dirname(__file__), "best_practices.txt")
    if os.path.exists(best_practices_path):
        with open(best_practices_path, "r", encoding="utf-8") as f:
            best_practices = "\n\nPlaywrightin parhaat käytännöt:\n" + f.read()

    return f"Tässä on esimerkkejä:\n\n{example_block}\n\n{element_block}\n{best_practices}\n\nTee uusi testi kuvaukselle: {user_prompt}\nCode:\n"



def generate_code(user_prompt):
    model = get_model()
    
    url = extract_url(user_prompt)
    page_elements = None

    if url:
        print(f"URL found in prompt: {url}")
        page_elements = fetch_page_elements(url)
        if page_elements:
            print(f"Page elements: {page_elements}")
        else:
            print("No elements found or failed to fetch page.")

    prompt = build_prompt(user_prompt, page_elements)

    output = model(prompt)
    return output if isinstance(output, str) else output[0]["generated_text"]

def fetch_page_elements(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        buttons = [btn.get_text(strip=True) for btn in soup.find_all('button')]
        inputs = [inp.get('name') or inp.get('id') or '' for inp in soup.find_all('input')]
        links = [a.get('href') or '' for a in soup.find_all('a')]
        
        return {
            "buttons": buttons,
            "inputs": inputs,
            "links": links
        }
    except Exception as e:
        print(f"Failed to fetch or parse URL: {e}")
        return None
