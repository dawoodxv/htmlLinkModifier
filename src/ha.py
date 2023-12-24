import sys
from bs4 import BeautifulSoup

def modify_links(soup):
    for a_tag in soup.find_all('a', href=True):
        if not a_tag.has_attr('target') or a_tag['target'] != '_blank':
            a_tag['target'] = '_blank'

def process_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_code = file.read()

        soup = BeautifulSoup(html_code, 'html.parser')
        modify_links(soup)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

        print(f"Modification complete. HTML code in '{file_path}' updated.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <html_file_path>")
        sys.exit(1)

    html_file_path = sys.argv[1]
    process_html_file(html_file_path)
