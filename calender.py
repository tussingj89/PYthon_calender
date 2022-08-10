from tkinter import *
import calendar

# viewed calender
def showCalender():
    screen = Tk()
    screen.config(background='light blue')
    screen.title("Calender for the year")
    screen.geometry("550x600")
    year = int(year_field.get())
    screen_content= calendar.calendar(year)
    calYear = Label(screen, text= screen_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    screen.mainloop()

# elements on the gui
if __name__=='__main__':
    new = Tk()
    new.config(background='light blue')
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="Calender",background= "light blue",font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='light blue')
    year_field=Entry(new)
    button = Button(new, text='Show Calender',
    fg='Black',bg='light green',command=showCalender)


# maping on the main gui
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=3, column=2)
    new.mainloop()
