# Convert to Float
import xlrd
import xlwt
import itertools

book = xlrd.open_workbook("new_eye.xls")
first_sheet = book.sheet_by_index(0)
# Section for writing to a new excel file.
wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet')

for i in range(first_sheet.ncols-1):
	for j in range(first_sheet.nrows-1):
		ws.write(j, i, str(float(first_sheet.cell(j,i).value)))
wb.save('finaleye' + '.xls')
