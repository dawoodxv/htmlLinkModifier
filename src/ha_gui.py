import os
import sys
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog, messagebox

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

        messagebox.showinfo("Success", f"Modification complete. HTML code in '{file_path}' updated.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        _, file_extension = os.path.splitext(file_path.lower())
        allowed_extensions = {'.html', '.htm', '.txt'}

        if file_extension in allowed_extensions:
            process_html_file(file_path)
        else:
            messagebox.showerror("Error", "Invalid file type. Please select an HTML or text file.")
            
def main():
    root = tk.Tk()
    root.title("HTML Link Modifier")

    browse_button = tk.Button(root, text="Browse", command=browse_file)
    browse_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
