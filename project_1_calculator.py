from tkinter import *

# window
window = Tk()
window.title('Mathematical Operations GUI')
window.geometry('1000x800')
# window.maxsize()
window.configure(background='white')

# first heading
label_1 = Label(window, text="Welcome to Tkinter Tutorial", font=("Times New Roman", 25))
label_1.grid(row=0, column=41, padx=0, pady=50, ipadx=30)

# second heading
label_2 = Label(window, text="Mini calculator", font=("Times New Roman", 15))
label_2.grid(row=1, column=41, pady=10, padx=10)

# first number -> label and text field
first_number_label = Label(window, text='first_number', font=("Times New Roman", 15))
first_number_label.grid(row=3, column=40, pady=30)

first_number_txt = Text(window, height=1, width=10)
first_number_txt.grid(row=3, column=41, pady=30)

# second number -> label and text field
second_number_label = Label(window, text='second_number', font=("Times New Roman", 15))
second_number_label.grid(row=4, column=40, pady=30)

second_number_txt = Text(window, height=1, width=10)
second_number_txt.grid(row=4, column=41, pady=30)


# Addition
def add():
    a = int(first_number_txt.get("1.0"))
    b = int(first_number_txt.get('1.0'))
    result = a + b
    result_label = Label(window, text='The addition value of two number is ' + str(result),
                         font=("Times New Roman", 15))
    result_label.grid(row=15, column=41, pady=50)


add_button = Button(window, text="ADD", width=10, height=2, font=("Times New Roman", 10), command=add)
add_button.grid(row=10, column=40, pady=20, ipadx=10)


# Subtraction
def sub():
    a = int(first_number_txt.get("1.0"))
    b = int(second_number_txt.get("1.0"))
    result = a - b
    result_label = Label(window, text="The subtraction value of two number is " + str(result), font=("Times New Roman", 15))
    result_label.grid(row=15, column=41, pady=50, ipadx=20)


sub_button = Button(window, text="SUB", width=10, height=2, font=("Times New Roman", 10), command=add)
sub_button.grid(row=10, column=41, pady=20, ipadx=10)


# Multiplication
def mul():
    a = int(first_number_txt.get("1.0"))
    b = int(second_number_txt.get("1.0"))
    result = a * b
    result_label = Label(window, text="The multiplication value of two number is " + str(result), font=("Times New Roman", 15))
    result_label.grid(row=15, column=41, pady=50, ipadx=20)


mul_button = Button(window, text="MUL", width=10, height=2, font=("Times New Roman", 10), command=mul)
mul_button.grid(row=10, column=42, pady=20, ipadx=10)


# Division
def div():
    a = int(first_number_txt.get("1.0"))
    b = int(second_number_txt.get("1.0"))
    result = a / b
    result_label = Label(window, text="The Division value of two number is " + str(result), font=("Times New Roman", 15))
    result_label.grid(row=15, column=41, pady=50, ipadx=20)


div_button = Button(window, text="DIV", width=10, height=2, font=("Times New Roman", 10), command=div)
div_button.grid(row=10, column=43, pady=20, ipadx=20)

# Exit button
button_exit = Button(window, text='Exit', font=('Times New Roman', 30), command=window.destroy)
button_exit.grid(row=11, column=41, pady=20, ipadx=10)


window.mainloop()
