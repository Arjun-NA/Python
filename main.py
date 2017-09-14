import DBconnect
from  tkinter import *
import export
#-----------------------------------------------------------------------------------------------------#
                                ###     MAIN WINDOW     ###
#-----------------------------------------------------------------------------------------------------#
root=Tk()
root.title("TITLE")
#root.geometry("400x400")
root.attributes("-fullscreen", True)
root.config(bg='#81db91')
root.bind('<Escape>',exit)

    # ALL FRAMES
#--------------------#
display=Frame(root)
display.grid(row=0,column=2)

leftWindow=Frame(root,bd=5,cursor='arrow',pady=25,padx=50,relief='groove')   #relief option ( raised,flat,sunken,groove,ridge)
leftWindow.grid(row=0,column=0,rowspan=30,sticky=N)

requiredDetails=Frame(leftWindow,relief='sunken',bd=2,pady=30)
requiredDetails.grid(row=0,column=0)

topLabel=Frame(leftWindow,bd=2,relief='sunken',pady=30)
topLabel.grid(row=1,column=0)

Selection=Frame(leftWindow,pady=25,width=40,bd=5,)
Selection.grid(row=3,column=0,pady=20)

exportFrame=Frame(leftWindow, width=50,pady=25)
exportFrame.grid(row=5,column=0)

radioButtons=Frame(topLabel,bd=5)
radioButtons.grid(row= 1,column=0)

fromEntry=Frame(Selection)
fromEntry.grid(row=1,column=0)

toEntry=Frame(Selection)
toEntry.grid(row=3,column=0)

buttons=Frame(Selection,width=50)
buttons.grid(row=4,column=0)


#-----------------------------------------------------------------------------------------------------#
                                ###   RIGHT WINDOW   ###
#-----------------------------------------------------------------------------------------------------#

#SCROLL BAR OF THE DISPLAY #
#--------------------------#

scrollbar = Scrollbar(display)
scrollbar.pack(side=RIGHT, fill=Y)
tableText=Text(display,relief=RIDGE,bg='White',padx=10,pady=5,
               exportselection=0,height=45,width=100, 
               bd=5)
tableText.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tableText.yview)

#-----------------------------------#
# Creating and Formating the table #    
#-----------------------------------#

def table(DATA) :
    global tableText 
    tableText.insert(INSERT,DATA)
    tableText.pack()        
    tableText.tag_add("heading", "1.0","1.100")
    tableText.tag_add("start", "2.0","2.100")
    tableText.tag_config("heading", background="yellow", foreground="blue")
    tableText.tag_config("start", background="yellow", foreground="blue")

    # Collect info LABEL frame #
#---------------------------------#

label=Label(topLabel,font="helvica 12 bold italic",text="FILTER BY :",width=30)
label.grid(row = 0, column=0,pady=10)


#-----------------------------------------------------------------------------------------------------#
                               ### LEFT WINDOW ###
#-----------------------------------------------------------------------------------------------------#
    # Radio button frame
#--------------------------#

def f1():
   value=var.get()
   fromLabel.configure(text="From\t:  "+value)
   toLabel.configure(text="To\t:  "+value)
   
     
var = StringVar()
radio=list()
radioOptions=["option1","option2","option3","option4","option5","option6"]
for i in range(6):
   radio.append(Radiobutton(radioButtons,text=radioOptions[i],activebackground='white',foreground='black',
                   variable=var,value=radioOptions[i],command=f1,padx=10))
   radio[i].grid(row=i//3,column=i%3)

#radio1=Radiobutton(radioButtons,text="Date",activebackground='white',foreground='black',
#                   variable=var,value='Date',command=f1)
#radio2=Radiobutton(radioButtons,text="ID",activebackground='green',foreground='black',
#                   variable=var,value='ID',command=f1)
#radio3=Radiobutton(radioButtons,text="Value",activebackground='lightgreen',foreground='black',
#                   variable=var,value='Value',command=f1)
#radio4=Radiobutton(radioButtons,text="Option1",activebackground='white',foreground='black',
#                   variable=var,value='Option1',command=f1)
#radio5=Radiobutton(radioButtons,text="Option2",activebackground='green',foreground='black',
#                   variable=var,value='Option2',command=f1)
#radio6=Radiobutton(radioButtons,text="Option3",activebackground='lightgreen',foreground='black',
#                   variable=var,value='Option3',command=f1)
#radio1.grid(row = 0, column = 0)
#radio2.grid(row = 0, column = 1)
#radio3.grid(row = 0, column = 2)
#radio4.grid(row = 1, column = 0)
#radio5.grid(row = 1, column = 1)
#radio6.grid(row = 1, column = 2)

    # Selection options with respect to the radio buttons 
#------------------------------------------------------------#


# LABEL FROM 

fromLabel=Label(Selection,text="From \t:",anchor=W,width=30)
fromLabel.grid(row=0,column=0)




 
    
# DATE Entry
#------------------#
F1  = Spinbox(fromEntry, from_=2016, to=2019, width=7, relief='flat')
F2  = Spinbox(fromEntry, from_=1,    to=12,   width=7, relief='flat')
F3  = Spinbox(fromEntry, from_=1,    to=31,   width=7, relief='flat')
F1.grid(row=1,column=0)
F2.grid(row=1,column=2)
F3.grid(row=1,column=3)

#LABEL TO

toLabel=Label(Selection,text="To \t:", anchor=W,width=30)
toLabel.grid(row=2,column=0)



#Value Entry
T1  = Spinbox(toEntry, from_=2016, to=2019, width=7,relief='flat')
T2  = Spinbox(toEntry, from_=1, to=12,width=7,relief='flat')
T3  = Spinbox(toEntry, from_=1, to=31, width=7,relief='flat')
T1.grid(row=0,column=0)
T2.grid(row=0,column=2)
T3.grid(row=0,column=3)


#------------------------------------------------------------------------------#
                        ### ButtonS ###
#------------------------------------------------------------------------------#

Tdate="1/1/1 0:0:0"
Fdate="1/1/1 0:0:0"
def buttonPress() :
    global tableText
    tableText.delete("1.0","100.0")
    global Fdate
    Fdate = F3.get()+'/'+F2.get()+'/'+F1.get()+' '+"00:00:00"
    print(Fdate)
    global Tdate
    Tdate =T3.get()+'/'+T2.get()+'/'+T1.get()+' '+"00:00:00"
    print(Tdate)
    Fdate = DBconnect.dateToStamp(Fdate)
    Tdate = DBconnect.dateToStamp(Tdate)
    global output
    output= DBconnect.read_db_bwts(Fdate,Tdate)
    table(export.View(output))
    checked = ""
    for i in range(6):
        if c[i].get()!="" :
            checked=checked+c[i].get()+","
    checked=checked[:-1]
    print(checked)
    print(filename.get())
def clearPress():
    global table
    tableText.delete("1.0","100.0")
#----------------------------------------------------#
# Button Frames #
#----------------------------------------------------#

# GO Button
goButton=Button(buttons,text ="GO", command = buttonPress,width=12)
goButton.grid(row=0,column=0)
# Clear Button
clearButton=Button(buttons,text ="Clear", command = clearPress,width=7)
clearButton.grid(row=0,column=2)
#----------------------------------------------------#
#       REQUEST DATA(S)       #
#----------------------------------------------------#


rqD=Label(requiredDetails,font="helvica 12 bold italic",text="REQUIRED DETAILS :",width=30)
rqD.grid(row=0,column=0,columnspan=3,pady=10)
c=list()
check=list()
checkOptions=["option1","option2","option3","option4","option5","option6"]
for i in range(len(checkOptions)): c.append(StringVar())
for i in range(len(checkOptions)):
  check.append(Checkbutton(requiredDetails,text=checkOptions[i],variable=c[i],onvalue=checkOptions[i],offvalue=""))
  check[i].select()
  check[i].grid(row=1+i//3,column=i%3)
#check1 = Checkbutton(requiredDetails,text="option1",variable=c[0],onvalue="opt1",offvalue="")
#check2 = Checkbutton(requiredDetails,text="option2",variable=c[1],onvalue="opt2",offvalue="")
#check3 = Checkbutton(requiredDetails,text="option3",variable=c[2],onvalue="opt3",offvalue="")
#check4 = Checkbutton(requiredDetails,text="option4",variable=c[3],onvalue="opt4",offvalue="")
#check5 = Checkbutton(requiredDetails,text="option5",variable=c[4],onvalue="opt5",offvalue="")
#check6 = Checkbutton(requiredDetails,text="option6",variable=c[5],onvalue="opt6",offvalue="")
#check1.select()
#check2.select()
#check3.select()
#check4.select()
#check5.select()
#check6.select()
#check1.grid(row=1,column=0)
#check2.grid(row=1,column=1)
#check3.grid(row=1,column=2)
#check4.grid(row=2,column=0)
#check5.grid(row=2,column=1)
#check6.grid(row=2,column=2)

#-----------------------------------------------------------------------------------------------------#
                                       ### EXPORT TO ###
#-----------------------------------------------------------------------------------------------------#
def exportPress():
   export.Write(output,filename.get())
   global exportButton
   exportButton.config(text="Exported",bg='lightgreen')
l=Label(exportFrame,text="Export  to  Excel  with ",font="bold 12 italic")
enterName=Label(exportFrame,text="FileName :",font="bold 10 italic ")
filename=Entry(exportFrame,bd=5,width=30)
l.grid(row=0,column=0,columnspan=2)
enterName.grid(row=1,column=0)
filename.grid(row=1,column=1)
exportButton=Button(exportFrame,text="EXPORT -> ",padx=10,pady=10,command=exportPress)
exportButton.grid(row=2,column=1)
#-----------------------------------------------------------------------------------------------------#
                                       ### MAIN LOOP ###
#------------------------------------------------------------------------------------------------------#
root.mainloop()