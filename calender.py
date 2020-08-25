from tkinter import *
import calendar

win =Tk()
win.title("Calendar")

l1= Label(win,text="Month :").grid(row=0,column=0)
l2= Label(win,text="Year :").grid(row=0,column=1)


m=Spinbox(win,from_=1,to=12,width=5)
m.grid(row=1,column=0)
y=Spinbox(win,from_=1700,to=2100,width=10)
y.grid(row=1,column=1,padx=8)


def go():
    mn= m.get()
    yr= y.get()
    mi= int(mn)
    yi= int(yr)
    cal= calendar.month(yi,mi)
    tf.delete(0.0,END)
    tf.insert(INSERT,cal)
    
    


b=Button(win,text="Go",command=go).grid(row=1,column=2)

tf=Text(win,height=10,width=25,foreground="red")
tf.grid(row=3,columnspan=3)

win.mainloop()
