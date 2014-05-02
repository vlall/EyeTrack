import xlrd
import xlwt
import itertools
import csv
class ReadExcel:
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
    # subject
    g=0
    h=1
    # image type
    j=3
    k=1

    def __init__(self, filename, ext="xlsx", sheet=0):
        self.filename = filename
        self.ext = ext
        self.sheet = sheet
        book = xlrd.open_workbook("%s.%s" % (filename, ext))
        self.first_sheet = book.sheet_by_index(sheet)
        print self.first_sheet

    def format_Array (self, images=25, trials=24, mistrials=2):
        listoutter=self.listoutter
        listinner=self.listinner
        first_sheet=self.first_sheet
        x=self.x
        y=self.y
        a=self.a
        b=self.b
        c=self.c
        d=self.d
        e=self.e
        f=self.f
        g=self.g
        h=self.g
        j=self.j
        k=self.k

        dimensions= 548#images * ((trials-mistrials)-1)-1))

        # Loop through and make a 2-d array (x values for each image)
        # 25x(24 minus the 2 mistrials)= 25*23- this gives you the number of images shown. 
        # I did (24*23-1) so i wouldn't go over the index bound (549). I substract another 1 to stop before the final cells
        # Because there's nothing to compare them to.
        for i in range(dimensions):
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
        		listinner.append(first_sheet.cell(g,h).value)
        		listinner.append(first_sheet.cell(j,k).value)
        		h+=(len(listinner)-1)/3
        		k+=(len(listinner)-1)/3	
        		listoutter.append([])
        		print(len(listinner))
        		y+=1
        		b+=1
        		d+=1
        		f+=1

        # Extend lists to contain the length of the max list. Add 0's to make up for the extra space.
        maxLen = max(map(len, listoutter))
        listoutter.pop()
        for row in listoutter:
            if len(row) < maxLen:
            	print ('IMPORTANT: ' + str(row[-1]))
            	end=row[-2]
            	#The NN requires NUMERICAL outputs. Therefore, we convert the strings to numbers.
            	if (end=='PICT001a'):
            		end=1
            	elif (end=='PICT002b'):
            		end=2
            	elif (end=='PICT003c'):
            		end=3
        		#elif (end=='PICT004d'):
            	elif (end=='PICT005a'):
            		end=4
            	elif (end=='PICT006b'):
            		end=5
            	elif (end=='PICT007c'):
            		end=6
            	elif (end=='PICT008d'):
            		end=7
            	elif (end=='PICT009a'):
            		end=8
            	elif (end=='PICT010b'):
            		end=9
            	elif (end=='PICT011c'):
            		end=10
            	#elif (end=='PICT012d'):
            	elif (end=='PICT013a'):
            		end=11
            	elif (end=='PICT014b'):
            		end=12
            	elif (end=='PICT015c'):
            		end=13
            	elif (end=='PICT016d'):
            		end=14
            	elif (end=='PICT017a'):
            		end=15
            	elif (end=='PICT018b'):
            		end=16
            	elif (end=='PICT019c'):
            		end=17
            	elif (end=='PICT020d'):
            		end=18
            	elif (end=='PICT021a'):
            		end=19
            	elif (end=='PICT022b'):
            		end=20
            	elif (end=='PICT023c'):
            		end=21
            	elif (end=='PICT024d'):  
            		end=22
            	end2=row[-1]
            	if (end2=='FACE'):
        			end2=1
            	elif (end2=='OUTDOOR'):
        			end2=2
            	elif (end2=='INDOOR'):
        			end2=3
            	elif (end2=='OBJECT'):
        			end2=4
            	elif (end2=='MANIP'):
        			end2=5
            	row.pop()
            	row.pop()
                row.extend([0.0 for z in xrange((maxLen) - len(row))])
                row.append(end)
                row.append(end2)

# This is important to know, it will tell us the amount of inputs we will use in the NN.
# Once we know this, we will work on a topolopy in BackProp.py
    def maxLength(self):
        return (maxLen)

    def printOutter(self):
        self.listoutter=listoutter 
    
    def get_Inner(self, indexNum):
        self.index=indexNum
        return self.listoutter[indexNum]

    def get_Sheet (self):
        return self.sheet

    def get_Ext (self):
        return self.ext

    def get_Name (self):
        return self.filename

    def get_Type(self,indexNum):
        self.index=indexNum
        row = self.listoutter[indexNum]
        return ('IMPORTANT: ' + str(row[-1]))

    def write_Array (self, filename, ext="xls"):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Sheet')
        for r in range(len(self.listoutter)):
            for col in range (len(self.listoutter[r])):
                ws.write(r, col, str(self.listoutter[r][col]))
        wb.save("%s.%s" %(filename, ext))

    def csv_from_excel(self, filename, ext="xls"):
        wb = xlrd.open_workbook('%s.%s' %(filename,ext))
        sh = wb.sheet_by_name('Sheet')
        your_csv_file = open('your_csv_file.csv', 'wb')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in xrange(sh.nrows):
            wr.writerow(sh.row_values(rownum))
        your_csv_file.close()

    def convert_Float(self, filenameIn, filenameOut="Floatfile", sheet=0):
        book = xlrd.open_workbook("%s.xls" % filenameIn)
        first_sheet = book.sheet_by_index(sheet)
        # Section for writing to a new excel file.
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Sheet')
        for i in range(first_sheet.ncols-1):
            for j in range(first_sheet.nrows-1):
                ws.write(j, i, str(float(first_sheet.cell(j,i).value)))
        wb.save(str(filenameOut) + '.xls')
        print ("File %s was successfully saved as a float in file %s", (filenameIn, filenameOut))

if __name__ == '__main__':
    EyeTrack = ReadExcel("new")
    EyeTrack.format_Array()
    EyeTrack.write_Array("EyeWrite")
    print EyeTrack.get_Inner(4)
    print EyeTrack.get_Name()
    print EyeTrack.get_Sheet()
    EyeTrack.write_Array('EyeWrite2')
    #EyeTrack.convert_Float("EyeWrite2")
    EyeTrack.csv_from_excel("EyeWrite2")


