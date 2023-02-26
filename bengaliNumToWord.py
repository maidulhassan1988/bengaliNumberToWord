import os
import PyPDF2
import re
import openpyxl as xl



# getting the .pdf and .xlsx files from current directory
directory = os.getcwd()
files = os.listdir(directory)
pdf_files = []
xl_files = []
for file in files:
	if file.endswith('.pdf'):
		pdf_files.append(file)
	elif file.endswith('.xlsx'):
		xl_files.append(file)



# creating a function to make a list out of prizebond pdfs
def pdfinfo(file_name):
	with open(file_name, 'rb') as pdfFile:
		reader = PyPDF2.PdfReader(pdfFile)
		page1 = reader.pages[0]
		text = page1.extract_text()
		c = re.findall(r'\d{2,7}', text)
	
	# creating a integer list of c list
	int_c = []
	for num in c:
		y = int(num)
		int_c.append(y)
	return int_c



for names in xl_files:
	# reading the values and storing into a list from excel file
	wb = xl.load_workbook(names) 
	ws = wb.active

	# getting the real value
	real_value = []
	for row in ws.values:
		for value in row:
			real_value.append(value)

	# getting rid of the None values
	prizebond_number = []
	for val in real_value:
		if val != None:
			prizebond_number.append(val)

	for n in pdf_files:
		winner = pdfinfo(n)

		for find in winner:
			for i in prizebond_number:
				if find == i:
					print(f'{find}   :   {names[:-5]} in {n[:-4]}')
