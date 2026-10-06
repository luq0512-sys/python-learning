import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

display = tk.Entry(window, width=20)
display.grid (row=0, column=0,
              columnspan=3, padx=10, pady=10)


def click(number):
     display.insert(tk.END, number)

button1 = tk.Button(window, text="1",
                    command=lambda:
click("1"))
button1.grid(row=1, column=0)

button2 = tk.Button(window, text="2",
                    command=lambda:
click("2"))
button2.grid(row=1, column=1)

button3 = tk.Button(window, text="3",
                    command=lambda:
click("3"))
button3.grid(row=1, column=2)

button4 = tk.Button(window, text="4",
                    command=lambda:
click("4"))
button4.grid(row=2, column=0)

button5 = tk.Button(window, text="5",
                    command=lambda:
click("5"))
button5.grid(row=2, column=1)

button6 = tk.Button(window, text="6",
                    command=lambda:
click("6"))
button6.grid(row=2, column=2 )

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


window.mainloop()


