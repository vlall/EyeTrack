import xlrd

book = xlrd.open_workbook("new.xlsx")
first_sheet = book.sheet_by_index(0)

'''
Example cell value we can use:
cell_value = first_sheet.cell(0,1).value
(0,1) is Pic001a
(1,1) is indoor4.png
'''
# Nest the list in an outter list to keep all arrays managable
listoutter=[]
listinner=[]
listoutter.append(listinner)
# Starting point for image name (indoor4.png)
x=1 
y=1

# Starting poit for x-coordinate starting cell
a=8
b=1
# Starting poit for y-coordinate starting cell
c=9
d=1
# Starting poit for y-coordinate starting cell
e=6
f=1


# Loop through and make a 2-d array (x values for each image)
for i in range(3):
	listinner = listoutter[i]
	listinner.append(first_sheet.cell(a,b).value) #first_sheet.cell(x,y).value
	listinner.append(first_sheet.cell(c,d).value) #first_sheet.cell(x,y).value
	listinner.append(first_sheet.cell(e,f).value) #first_sheet.cell(x,y).value


	while (first_sheet.cell(x,y).value == first_sheet.cell(x,y+1).value):
		listinner.append(first_sheet.cell(a,b+1).value)
		listinner.append(first_sheet.cell(c,d+1).value)
		listinner.append(first_sheet.cell(e,f+1).value) #first_sheet.cell(x,y).value

		y+=1
		b+=1
		d+=1
		f+=1

	else:
		listoutter.append([])
		print(len(listinner))
		y+=1
		b+=1
		d+=1
		f+=1


# Print (cell_value)
print (listoutter)

# Extend lists to contain the length of the max list. Add 0's to make up for the extra space.
maxLen = max(map(len, listoutter))
for row in listoutter:
    if len(row) < maxLen:
        row.extend([0 for z in xrange((maxLen) - len(row))])

# Print nested lists' lengths.
print (listoutter)
for j in range (len(listoutter)):
	print len(listoutter[j])


# Print nested lists' lengths.
print (listoutter)
for j in range (len(listoutter)):
	print len(listoutter[j])
