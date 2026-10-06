import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

display = tk.Entry(window, width=20)
display.pack (pady=20)


def click():
     display.insert(tk.END, "1")
button1 = tk.Button(window, text="1",
command=click)
button1.pack()

def click():
     display.insert(tk.END, "2")
button2 = tk.Button(window, text="2",
command=click)
button2.pack()


def click():
     display.insert(tk.END, "3")
button3 = tk.Button(window, text="3",
command=click)
button3.pack()

window.mainloop()