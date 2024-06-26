# Excel-to-Deepl-Translator
This for translating Excel files through the Deepl Translator API. Because the Deepl API cannot translate Excel files, this program first copies the text from the Excel file to a txt file, then translates through Deepl, returns the text to a txt file, then places the English text into the 2nd column in the corresponding row of the Excel file. It also adds 'Translated' to the file name.

![Process](process.jpg)

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Author](#author)
- [License](#license)

## Features
- Takes an excel document with chunks of Japanese text in to 1st column, and adds a US English translation to the 2nd column
- Adds 'Translated' to the Excel file name

## Requirements
- [Deepl API Authentication Key](https://www.deepl.com/docs-api/api-access/authentication)
- [deepl](https://pypi.org/project/deepl/)
- [openpyxl](https://pypi.org/project/openpyxl/)

## Usage
1. Install the required Python packages:

    ```bash
    pip install openpyxl deepl
    ```

2. Update the following information in the Python script:

    - Get an authentication key from deepl and enter it here `authentication_key = "################################"`.
    - Replace `'file.xlsx'` with the name of the Excel file you wish to translate. Alternatively, change the name of your Excel file to `file.xlsx`.

3. Place the Excel file you wish to translate into the same directory as the Python script.

4. Run the script:

    ```bash
    python Excel Deepl Translator.py
    ```

5. The `output.txt` file will have the translated cells in seperate groups of text.

## File Structure
- `Excel Deepl Translator.py` Python script for translating excel file to English and saving it as `output.txt`.
- `input.txt`: Text file used to hold text from Excel file, and be translated by deepl as a document
- `output.txt`: Text file containing translated text
- `file.xlsx`: An Excel file that you wish to translate into English needs to be placed in this directory and name configured in the script or its file name changed to `file.xslx`.

## Author
Alex McKinley

## License
This project is licensed under the [MIT License](LICENSE).
