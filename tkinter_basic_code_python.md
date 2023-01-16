# Tkinter simple python code 

## program 1 : First program
* Importing the module, creating an object and display the text.
```
from tkinter import Tk, Label  
  
window = Tk()  
window.title("Graphical_User_Interface")  
  
lab = Label(window, text="First_Tkinter_project", font=("Times New Roman", 50))  
lab.pack()  # Its like print function of label  
  
window.mainloop()  # tells Python to run the Tkinter event loop.
```

## program 2 : Label
* using label method
```
from tkinter import Tk, Label  
  
win = Tk()  
win.title("Graphical_User_Interface")  
  
label = Label(win, text="First_Tkinter_project", font=("Times New Roman", 50))  
win.geometry('1200x1000')  
label.grid(row=200, column=500)  
label.pack()  
win.mainloop()
```

## Program 3 : Button
* Click event : We have write a code to tell what should happen when the user click that button 
```
from tkinter import *  
# * is used to import multiple functions   
window = Tk()  
window.title('GUI')  
window.geometry('800x700')  
  
# Label section  
project_label = Label(window, text='First_Tkinter_project', font=('Times New Roman', 30))  
project_label.pack()  
  
  
# function for click event  
def clicked():  
    button_message.configure(text="Welcome to Tkinter Tutorial... :)")  
  
  
# Buttons section  
button_message = Button(window, text='Message', bg='Black', fg='White', font=('Times New Roman', 30), command=clicked)  
button_message.pack()  
  
button_exit = Button(window, text='Exit', bg='Black', fg='White', font=('Times New Roman', 30),  
  command=window.destroy)  
button_exit.pack()  
  
window.mainloop()
```

## Program 4 : Entry
* It is used to put input fields in the GUI 
```
from tkinter import *  
  
# * is used to import multiple functions  
  
window = Tk()  
window.title('GUI')  
window.geometry('800x700')  
  
# Label section  
project_label = Label(window, text='First_Tkinter_project', font=('Times New Roman', 30))  
project_label.pack()  
  
  
# function for click event  
def button_message_clicked():  
    button_message.configure(text="Welcome to Tkinter Tutorial... :)")  
  
  
# Buttons section  
button_message = Button(window, text='Message', bg='Black', fg='White', font=('Times New Roman', 30), command=button_message_clicked)  
button_message.pack()  
  
# Entry section  
text_name = Entry(window, width=10, font=('Times New Roman', 30))  
# text_name.grid(column=1, row=0)  
text_name.pack()  
  
  
def text_name_clicked():  
    input_name = text_name.get() + ' Are you excited to learn Tkinter'  
  button_name.configure(text=input_name)  
  
  
button_name = Button(window, text='Please enter the name', command=text_name_clicked, font=('Times New Roman', 30))  
button_name.pack()  
  
# Exit button  
button_exit = Button(window, text='Exit', bg='Black', fg='White', font=('Times New Roman', 30), command=window.destroy)  
button_exit.pack()  
  
window.mainloop()
```
## Program 5 : Combobox
* Dropdown menu with option
```
from tkinter.ttk import *  
  
window = Tk()  
window.title('GUI')  
window.geometry('800x700')  
  
combo = Combobox(window)  
combo['values'] = (1, 2, 3, 4, 5, "text")  
combo.current(3)  
# combo.grid(column=0, row=0)  
combo.pack()
```
## Program 6 : Checkbox
```
checkbox_state = BooleanVar()  
checkbox_state.set(False)  
check_button = Checkbutton(window, text='select', variable=checkbox_state)  
check_button.pack()  
  
# Exit button  
button_exit = Button(window, text='Exit', command=window.destroy)  
button_exit.pack()  
  
window.mainloop()
```
## Program 7 : Radio button
* Value should be unique, that means unique value is used to address the radio button.
```
radio_button_2 = Radiobutton(window, text='class_2', value=2)  
radio_button_3 = Radiobutton(window, text='class_3', value=3)  
radio_button_1 = Radiobutton(window, text='class_1', value=1)  
  
radio_button_1.grid(column=0, row=0)  
radio_button_2.grid(column=1, row=0)  
radio_button_3.grid(column=2, row=0)  
  
radio_button_2.pack()  
radio_button_3.pack()  
radio_button_1.pack()
```

## Program 8 : Message Box
* substitute of configure
```
def clicked():  
    messagebox.showinfo('title', 'content')  
  
  
button_message = Button(window, text='enter', command=clicked)  
button_message.pack()
```
