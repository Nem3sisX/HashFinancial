from tkinter import *

root = Tk()
root.title(string="HashFinancial")

frame1=Frame(root)
frame1.pack(side=TOP,fill=X)

frame2=Frame(root)
frame2.pack(side=TOP, fill=X)


# **** ToolBar *******

hashfinance=Frame(frame1,bg='green')
hashfinance.pack(side=TOP,fill=X)
hashname = Label(hashfinance, text='HashFinancial', bg="black", fg='green')
hashname.pack(fill=X)


# ****** main centre window *****
symbol=Label(frame2,text='Enter Stock Symbol : ')
symbol.grid(row=4,column=0,sticky=E)

entry1=Entry(frame2)
entry1.grid(row=4,column=1)

predict=Button(frame2,text='Predict Now', fg="green")
predict.grid(columnspan=2)


# **** StatusBar ******************
status= Label(root,text='Live Stock Price Ticker : ',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
