from tkinter import *
class DC(Tk): #display cars
    def __init__(self):
        Tk.__init__(self)
        t = SimpleTable(self, len(cars),8)
        t.pack(side="top", fill="x")
        t.set(0,0,"Make")
        t.set(0,1,"Model")
        t.set(0,2,"Km/l")
        t.set(0,3,"Passengers")
        t.set(0,4,"Doors")
        t.set(0,5,"Reg")
        t.set(0,6,"Daily Cost")
        t.set(0,7,"Weekly Cost")
        t.set(0,8,"Weekend Cost")



class SimpleTable(Frame):
    def __init__(self, parent, rows, columns):


        reg_list=cars.keys()
        Frame.__init__(self, parent, background="black")
        self._widgets = []

        #for row in range(rows):
            #current_row = []
            #current_reg=reg_list[row]

        for row in range(1,rows+1): #amended to start at row 1
            current_row = []
            current_reg=reg_list[row-1]

            make = Label(self, text=cars[current_reg].make,borderwidth=0, width=10)
            make.grid(row=row, column=0, sticky="nsew", padx=1, pady=1)
            current_row.append(make)

            model = Label(self, text=cars[current_reg].model,borderwidth=0, width=10)
            model.grid(row=row, column=1, sticky="nsew", padx=1, pady=1)
            current_row.append(model)

            kml = Label(self, text=cars[current_reg].kml,borderwidth=0, width=10)
            kml.grid(row=row, column=2, sticky="nsew", padx=1, pady=1)
            current_row.append(kml)

            passengers = Label(self, text=cars[current_reg].passengers,borderwidth=0, width=10)
            passengers.grid(row=row, column=3, sticky="nsew", padx=1, pady=1)
            current_row.append(passengers)

            doors = Label(self, text=cars[current_reg].doors,borderwidth=0, width=10)
            doors.grid(row=row, column=4, sticky="nsew", padx=1, pady=1)
            current_row.append(doors)

            reg = Label(self, text=cars[current_reg].reg,borderwidth=0, width=10)
            reg.grid(row=row, column=5, sticky="nsew", padx=1, pady=1)
            current_row.append(reg)

            daily = Label(self, text=cars[current_reg].daily_cost,borderwidth=0, width=10)
            daily.grid(row=row, column=6, sticky="nsew", padx=1, pady=1)
            current_row.append(daily)

            weekly = Label(self, text=cars[current_reg].weekly_cost,borderwidth=0, width=10)
            weekly.grid(row=row, column=7, sticky="nsew", padx=1, pady=1)
            current_row.append(weekly)

            weekend = Label(self, text=cars[current_reg].weekend_cost,borderwidth=0, width=10)
            weekend.grid(row=row, column=8, sticky="nsew", padx=1, pady=1)
            current_row.append(weekend)





    self._widgets.append(current_row)

    for column in range(columns):
        self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)
new=DC()