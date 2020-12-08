from tkinter import *
 
root = Tk()
 
root.title("Techbox")
root.geometry('300x500')
 
label_wel = Label(root, text='Login or Register')
label_choice = Label(root, text='Enter username and password.')
label_wel.grid(row=0, column=0, columnspan=2)
label_choice.grid(row=1, column=0, columnspan=2)
 
label_name = Label(root, text='Username')
label_password = Label(root, text='Password')
 
button_log =  Button(root, text='Login')
button_reg = Button(root, text='Register')
 
entry_name = Entry(root)
entry_password = Entry(root)
 
label_name.grid(column=0, row=2)
label_password.grid(column=0, row=3)
 
entry_name.grid(column=1, row=2)
entry_password.grid(column=1, row=3)
 
button_log.grid(column=0, row=4)
button_reg.grid(column=1, row=4)
 
root.mainloop()