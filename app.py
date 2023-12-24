from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import os

app = Flask(__name__)


def modify_links(soup):
    for a_tag in soup.find_all('a', href=True):
        if not a_tag.has_attr('target') or a_tag['target'] != '_blank':
            a_tag['target'] = '_blank'


def process_html_code(html_code):
    try:
        soup = BeautifulSoup(html_code, 'html.parser')
        modify_links(soup)
        return str(soup)
    except Exception as e:
        return f"Error: {e}"


def process_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_code = file.read()
        modified_code = process_html_code(html_code)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_code)
        return f"Modification complete. HTML code in '{file_path}' updated."
    except Exception as e:
        return f"Error: {e}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    html_code = request.form['html_code']
    result = process_html_code(html_code)
    return result


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = 'uploads/' + file.filename
    file.save(file_path)
    result = process_html_file(file_path)
    return result


if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
