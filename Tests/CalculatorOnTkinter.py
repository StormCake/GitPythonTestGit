# Calculus with Tk
from tkinter import *


def calculus(calculus_action):
    try:
        a = int(entry_for_a.get())
        b = int(entry_for_b.get())
        if calculus_action == 1:
            calculus_result = a + b
        elif calculus_action == 2:
            calculus_result = a - b
        elif calculus_action == 3:
            calculus_result = a * b
        else:
            calculus_result = a / b
        label_result.configure(text=calculus_result)
    except ValueError:
        label_result.configure(text="error")


root = Tk()
root.title("Calculus Maximus")

entry_for_a = Entry(width=20, font=("Arial", 20))
entry_for_b = Entry(width=20, font=("Arial", 20))
button_plus = Button(text="+", font=("Arial", 20), width=2, command=lambda: calculus(1))
button_minus = Button(text="-", font=("Arial", 20), width=2,  command=lambda: calculus(2))
button_multiply = Button(text="*", font=("Arial", 20), width=2, command=lambda: calculus(3))
button_divide = Button(text="/", font=("Arial", 20), width=2,  command=lambda: calculus(4))
label_result = Label(width=20, bg='black', fg='white', text="", font=("Arial", 20))

entry_for_a.grid(column=0, row=0, columnspan=2)
entry_for_b.grid(column=0, row=1, columnspan=2)
button_plus.grid(column=0, row=2, padx=2, pady=2)
button_minus.grid(column=1, row=2, padx=2, pady=2)
button_multiply.grid(column=0, row=3, padx=2, pady=2)
button_divide.grid(column=1, row=3, padx=2, pady=2)
label_result.grid(column=0, row=4, columnspan=2)


# entry_for_a.pack()
# entry_for_b.pack()
# button_plus.pack()
# button_minus.pack()
# button_multiply.pack()
# button_divide.pack()
# label_result.pack()
entry_for_a.focus()
root.mainloop()
