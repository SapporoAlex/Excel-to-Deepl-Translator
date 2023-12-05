import deepl
import openpyxl as xl

# You can get a free authentication key here https://support.deepl.com/hc/en-us/articles/360020695820-Authentication-Key
authentication_key = "################################"
translator = deepl.Translator(authentication_key)

# Place the Excel file in the same folder and change the file name accordingly
fhandle = xl.load_workbook("file.xlsx")
# Make sure the Sheet name is the same
sheet = fhandle["Sheet1"]
tmp = open("input.txt", 'w')
tt = open("output.txt", 'w')
input_path = "input.txt"
output_path = "output.txt"

# text in the first column of the Excel file is copied into a txt file, translated, then copied to the output.txt file
for row in range(1, sheet.max_row + 1):
    cell = sheet.cell(row, 1)
    if cell.value is not None:
        tbt = cell.value
        str(tbt)
        tmp.write(tbt + '\n\n')

tmp.close()
translator.translate_document_from_filepath(input_path, output_path, target_lang='EN-GB')
tt.close()
