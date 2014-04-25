'''
This script will utilize PyExcel to read xls(x) Eyetracker data.
We will read the data and save it as a list within a list:

[outterlist [innerlist1],[innerlist2],........[innerlistN] ]

Our neural networks need a vector, but our information is in 3-Dimensions:
(x-fixation, y-fixation, duration of fixation or-> x,y,t)
therefore we convert the matrix:
[ x1 y1 t1 ]
[ x2 y2 t2 ]
[ x3 y3 t3 ]

into a column vector:
[ x1 ]
[ y1 ]
[ t1 ]
[ x2 ]
[ y2 ]
[ t2 ]
[ x3 ]
[ y3 ]
[ t3 ]

Our NN not only requires 1-dimenesional data, it also needs an EQUAL amount of outputs 
for every training set. To do this, we will then find the maximum length of a given
list and replace the lists that do not meet this max with zeros. This will result
in an equal amount of outputs.

-----------------------------------
After reading the data, we will create a new xls(x) spreadsheet that will 
reorganize and reformat the original data so that it can be read by BackProp.py,
our PyBrain NN creator.

Please read BackProp.py to find the application of this script in an NN.

TODO:
1) The final value is not printed in the loop (minor)
'''
import xlrd
import xlwt
import itertools

book = xlrd.open_workbook("new.xlsx")
first_sheet = book.sheet_by_index(0)
# Section for writing to a new excel file.
wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet')

'''
Example cell value we can use:
cell_value = first_sheet.cell(0,1).value
(0,1) is Pic001a
(1,1) is indoor4.png

some useful methods:
This gives you the number of columns and rows
print first_sheet.ncols
print first_sheet.nrows
ws.write(2, 0, 'asdf')
'''
# Nest the list in an outter list to keep all arrays managable
listoutter=[]
listinner=[]
listoutter.append(listinner)
# Starting point for image name (indoor4.png)
x=1 
y=1
# Starting point for x-coordinate starting cell
a=8
b=1
# Starting point for y-coordinate starting cell
c=9
d=1
# Starting point for y-coordinate starting cell
e=6
f=1

# Loop through and make a 2-d array (x values for each image)
# 25x(24 minus the 2 mistrials)= 25*23- this gives you the number of images shown. 
# I did (24*23-1) so i wouldn't go over the index bound (549). I substract another 1 to stop before the final cells
# Because there's nothing to compare them to.
for i in range(548):
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
# Print nested lists' lengths.
print (listoutter)

# Extend lists to contain the length of the max list. Add 0's to make up for the extra space.
maxLen = max(map(len, listoutter))
for row in listoutter:
    if len(row) < maxLen:
        row.extend([0 for z in xrange((maxLen) - len(row))])

'''
OLD METHOD,
COMMENT OUT-
This was used to make multiple inner lists into a single list:
-----------------------------------------------
singleList = list(itertools.chain(*listoutter))
for v in range (len(singleList)-1):
	#no more than 256 columns allowed for xls, so use xlsb
	ws.write(v, 0, str(singleList[v]))
wb.save('new346' + '.xls')
'''
for r in range(len(listoutter)-1):
	for col in range (len(listoutter[r])-1):
		ws.write(r, col, str(listoutter[r][col]))
wb.save('new346' + '.xls')
