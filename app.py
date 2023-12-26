from flask import Flask, render_template, request, send_file
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
        return modified_code
    except Exception as e:
        return f"Error: {e}"


@app.route('/')
def index():
    return render_template('index.html', modified_code=None)


@app.route('/process', methods=['POST'])
def process():
    html_code = request.form['html_code']
    modified_code = process_html_code(html_code)
    return modified_code


@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        
        if file:
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            result = process_html_file(file_path)
            return result
        else:
            return "Error: No file provided."

    except Exception as e:
        return f"Error: {e}" 


@app.route('/download', methods=['POST'])
def download():
    modified_code = request.form['modified_code']
    format_option = request.form['format_option']

    file_extension = 'html' if format_option == 'html' else 'txt'
    file_path = f'downloads/modified_code.{file_extension}'

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_code)

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run()
