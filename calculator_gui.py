import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

display = tk.Entry(
    window,
    width=20,
    font=("Arial", 20),
    justify="right"
)
display.grid (row=0, column=0,
              columnspan=3, padx=10, pady=10)


def click(number):
     display.insert(tk.END, number)

button1 = tk.Button(
    window, 
    text="1", 
    width=5, 
    height=2,
    command=lambda:click("1")
)
button1.grid(row=1, column=0, padx=2, pady=2)

button2 = tk.Button(
    window, 
    text="2", 
    width=5, 
    height=2,
    command=lambda:click("2")
)
button2.grid(row=1, column=1, padx=2, pady=2)

button3 = tk.Button(
    window, 
    text="3", 
    width=5, 
    height=2,
    command=lambda:click("3")
)
button3.grid(row=1, column=2, padx=2, pady=2)

button4 = tk.Button(
    window, 
    text="4", 
    width=5, 
    height=2,
    command=lambda:click("4")
)
button4.grid(row=2, column=0, padx=2, pady=2)

button5 = tk.Button(
    window, 
    text="5", 
    width=5, 
    height=2,
    command=lambda:click("5")
)
button5.grid(row=2, column=1, padx=2, pady=2)


button6 = tk.Button(
    window, 
    text="6", 
    width=5, 
    height=2,
    command=lambda:click("6")
)
button6.grid(row=2, column=2, padx=2, pady=2)

button7 = tk.Button(window, text="7",
                    command=lambda:
click("7"))
button7.grid(row=3, column=0)

button8 = tk.Button(window, text="8",
                    command=lambda:
click("8"))
button8.grid(row=3, column=1)

button9 = tk.Button(window, text="9",
                    command=lambda:
click("9"))
button9.grid(row=3, column=2)

button0 = tk.Button(window, text="0",
                    command=lambda:
click("0"))
button0.grid(row=4, column=0)


def clear():
    display.delete(0, tk.END)

clear_button = tk.Button(window,
                         text="Clear",
                         command=clear)

clear_button.grid(row=4, column=1)


def calculate():
    try:
        expression = display.get()

        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(tk.END, result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


button_add = tk.Button(window, text="+", width=6, height=3, command=lambda:
                 click("+"))
button_add.grid(row=1, column=3)

button_sub = tk.Button(window, text="-", width=6, height=3, command=lambda:
            click("-"))
button_sub.grid(row=2, column=3)

button_mul = tk.Button(window, text="*", width=6, height=3, command=lambda:
            click("*"))
button_mul.grid(row=3, column=3)

button_div = tk.Button(window, text="/", width=6, height=3, command=lambda:
              click("/"))
button_div.grid(row=4, column=3)

button_equal = tk.Button(window, text="=", width=6, height=3,
               command=calculate)
button_equal.grid(row=4, column=2)


window.mainloop()


