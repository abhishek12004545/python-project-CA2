from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("800x600")
def click():
    frame2.pack (fill=BOTH,expand=True, padx=10, pady=10 )
    label5=Label(frame2,text=car_owner.get())
    label5.pack()
    label6=Label(frame2,text=car_model.get())
    label6.pack()
    label8=Label(frame2,text=car_price.get())
    label8.pack()

def conFirm():
    messagebox.showinfo("Your Order Is confirmed","Thanks for Choosing Us Your order is confirmed")
    root.quit()
frame1=LabelFrame(root,text="Car details frame")
frame1.pack(fill=BOTH, expand= True, padx= 10, pady=10)

label1=Label(frame1,text="Name")
label1.pack()
car_owner=Entry(frame1)
car_owner.pack()

label2=Label(frame1,text="Car Model")
label2.pack(padx= 10, pady=10)
car_model=Entry(frame1)
car_model.pack()

label4=Label(frame1,text="Choose the vehicle")
label4.pack(padx= 10, pady=10)
clicked=StringVar()
drop=OptionMenu(frame1,clicked,"2-Wheels","3-Wheels","4-Wheels","6-Wheels","8-Wheels")
drop.pack(padx= 10, pady=10)

label3=Label(frame1,text="Service Price")
label3.pack(padx= 10, pady=10)
car_price=Entry(frame1)
car_price.pack()

Submit=Button(frame1,text="Submit Details",command=click)
Submit.pack(padx= 10, pady=20)

frame2=LabelFrame(root,text="Confirm details")
frame2.pack_forget()

confirm=Button(frame2,text="Confirm details",command=conFirm)
confirm.pack()




root.mainloop()