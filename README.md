# HTML Link Modifier

Enhance your HTML code effortlessly by ensuring that all external
links open in a new tab. Simply modify your HTML code with the
addition of the
<code>target="\_blank"</code> attribute, providing a seamless
experience for users exploring your website. Choose the method that suits you best!

## Method 1: Command Line

### Prerequisites:

- Python installed on your system.

### Edit HTML File:

1. Save your HTML code in a text file (e.g., `html_input.txt`).

### Run the Script:

2. Open a terminal or command prompt.
3. Navigate to the directory containing the script (`src/ha.py`).
4. Execute the following command:
   ```bash
   python3 ha.py html_input.txt
   ```

### Check Output:

5. The script will process your HTML code and update the .txt/.html file with modified code.

## Method 2: GUI Application

1. **Find the Executable:**

   - Navigate to the `dist` directory based on your OS.

   - **For Windows:**

     - `Windows/ha_gui/ha_gui.exe`

   - **For MacOS:**
     - `MacOS/ha_gui/ha_gui`

2. **Run the GUI Application:**

   - Run `ha_gui.exe` or `ha_gui` depending on your OS.

3. **Use the GUI:**

   - Click the "Browse" button to select the HTML/.txt file you want to update.
   - Click the "Open" button.

4. **Check Output:**
   - The GUI will prompt "Modification Complete".
   - The HTML file will be updated with the fixed HTML code.

## Method 3: Web Interface

1. **Run the Flask App:**

   - Ensure you have Flask installed (`pip install flask`).
   - Run the Flask app using `python app.py`.
   - Open your browser and navigate to `http://localhost:5000`.

2. **Use the Web Interface:**

   - Paste or upload your HTML code.
   - Click the appropriate button to modify and download your HTML.

3. **Check Output:**
   - The modified HTML code will be displayed on the website and available as a downloadable file to download.
