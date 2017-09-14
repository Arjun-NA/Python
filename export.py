import xlwt
from tabulate import tabulate
maxWidth=[3,10,5]

wb = xlwt.Workbook()
ws = wb.add_sheet("My Sheet")
def Write(DATA,filename) :
    # Add headings with styling and froszen first row
    heading_xf = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')
    headings = ['ID', 'Time Stamp','Value']
    rowx = 0
    ws.set_panes_frozen(True)       # frozen headings instead of split panes
    ws.set_horz_split_pos(rowx+1)   # in general, freeze after last heading row
    ws.set_remove_splits(True)      # if user does unfreeze, don't leave a split there
    for colx, value in enumerate(headings):
        ws.write(rowx, colx, value, heading_xf)
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            ws.write(i+1, j, str(col))
    for i in range(len(maxWidth)) :
        ws.col(i).width = 1000 * maxWidth[i]
    #file=filename+".xls"
    wb.save(filename+".xls")
def View(DATA):
    t = tabulate(DATA,headers=['ID','TIME STAMP','VALUE'],tablefmt='orgtbl') 
    print(t)
    return t