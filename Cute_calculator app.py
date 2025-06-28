import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculations():
    global calculation

    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def on_enter(e):
    e.widget['background'] = "#eeffea"

def on_leave(e):
    e.widget['background'] = e.widget.default_bg


root = tk.Tk()
root.geometry("335x400")
root.config(bg = "#fff1f1")
root.title("cute calculator")
icon = tk.PhotoImage(file = "heart icon_calc.png")
root.iconphoto(False, icon)


text_result = tk.Text(root, height = 2, width = 16, bg = "#e9ffe3", font = ("Comic Sans MS", 24))
text_result.grid( row=0, column=1, columnspan=4, padx=5, pady=10, sticky="ew" )

button1 = tk.Button(root, text = "1", command = lambda: add_to_calculation(1), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button1.grid(row = 5, column = 1, padx=5, pady=5)
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)
button1.default_bg = "#feced6"
button2 = tk.Button(root, text = "2", command = lambda: add_to_calculation(2), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button2.grid(row = 5, column = 2, padx=5, pady=5)
button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)
button2.default_bg = "#feced6"
button3 = tk.Button(root, text = "3", command = lambda: add_to_calculation(3), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button3.grid(row = 5, column = 3, padx=5, pady=5)
button3.bind("<Enter>", on_enter)
button3.bind("<Leave>", on_leave)
button3.default_bg = "#feced6"
button4 = tk.Button(root, text = "4", command = lambda: add_to_calculation(4), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button4.grid(row = 4, column = 1, padx=5, pady=5)
button4.bind("<Enter>", on_enter)
button4.bind("<Leave>", on_leave)
button4.default_bg = "#feced6"
button5 = tk.Button(root, text = "5", command = lambda: add_to_calculation(5), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button5.grid(row = 4, column = 2, padx=5, pady=5)
button5.bind("<Enter>", on_enter)
button5.bind("<Leave>", on_leave)
button5.default_bg = "#feced6"
button6 = tk.Button(root, text = "6", command = lambda: add_to_calculation(6), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button6.grid(row = 4, column = 3, padx=5, pady=5)
button6.bind("<Enter>", on_enter)
button6.bind("<Leave>", on_leave)
button6.default_bg = "#feced6"
button7 = tk.Button(root, text = "7", command = lambda: add_to_calculation(7), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button7.grid(row = 3, column = 1, padx=5, pady=5)
button7.bind("<Enter>", on_enter)
button7.bind("<Leave>", on_leave)
button7.default_bg = "#feced6"
button8 = tk.Button(root, text = "8", command = lambda: add_to_calculation(8), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button8.grid(row = 3, column = 2, padx=5, pady=5)
button8.bind("<Enter>", on_enter)
button8.bind("<Leave>", on_leave)
button8.default_bg = "#feced6"
button9 = tk.Button(root, text = "9", command = lambda: add_to_calculation(9), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button9.grid(row = 3, column = 3, padx=5, pady=5)
button9.bind("<Enter>", on_enter)
button9.bind("<Leave>", on_leave)
button9.default_bg = "#feced6"
button0 = tk.Button(root, text = "0", command = lambda: add_to_calculation(0), width = 5, bg = "#feced6", font = ("Comic Sans MS", 14))
button0.grid(row = 6, column = 2, padx=5, pady=5) 
button0.bind("<Enter>", on_enter)
button0.bind("<Leave>", on_leave)
button0.default_bg = "#feced6"
buttondiv = tk.Button(root, text = "/", command = lambda: add_to_calculation("/"), width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttondiv.grid(row = 2, column = 4, padx=5, pady=5)
buttondiv.default_bg = "#fb9aaa"
buttondiv.bind("<Enter>", on_enter)
buttondiv.bind("<Leave>", on_leave)
buttonmul = tk.Button(root, text = "*", command = lambda: add_to_calculation("*"), width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttonmul.grid(row = 3, column = 4, padx=5, pady=5)
buttonmul.default_bg = "#fb9aaa"
buttonmul.bind("<Enter>", on_enter)
buttonmul.bind("<Leave>", on_leave)
buttonmin = tk.Button(root, text = "-", command = lambda: add_to_calculation("-"), width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttonmin.grid(row = 4, column = 4, padx=5, pady=5)
buttonmin.default_bg = "#fb9aaa"
buttonmin.bind("<Enter>", on_enter)
buttonmin.bind("<Leave>", on_leave)
buttonplus = tk.Button(root, text = "+", command = lambda: add_to_calculation("+"), width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttonplus.grid(row = 5, column = 4, padx=5, pady=5)
buttonplus.default_bg = "#fb9aaa"
buttonplus.bind("<Enter>", on_enter)
buttonplus.bind("<Leave>", on_leave)
buttonper = tk.Button(root, text = "%", command = lambda: add_to_calculation("%"), width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttonper.grid(row = 2, column = 3, padx=5, pady=5)
buttonper.default_bg = "#fb9aaa"
buttonper.bind("<Enter>", on_enter)
buttonper.bind("<Leave>", on_leave)
buttonopen = tk.Button(root, text = "(", command = lambda: add_to_calculation("("), width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttonopen.grid(row = 6, column = 1, padx=5, pady=5)
buttonopen.default_bg = "#fb9aaa"
buttonopen.bind("<Enter>", on_enter)
buttonopen.bind("<Leave>", on_leave)
buttonclose = tk.Button(root, text = ")", command = lambda: add_to_calculation(")"), width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttonclose.grid(row = 6, column = 3, padx=5, pady=5)
buttonclose.default_bg = "#fb9aaa"
buttonclose.bind("<Enter>", on_enter)
buttonclose.bind("<Leave>", on_leave)
buttondot = tk.Button(root, text = ".", command = lambda: add_to_calculation("."), width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttondot.grid(row = 2, column = 2, padx=5, pady=5)
buttondot.default_bg = "#fb9aaa"
buttondot.bind("<Enter>", on_enter)
buttondot.bind("<Leave>", on_leave)
buttonequal = tk.Button(root, text = "=", command = evaluate_calculations, width = 5, bg = "#fb9aaa", font = ("Comic Sans MS", 14))
buttonequal.grid(row = 6, column = 4, padx=5, pady=5)
buttonequal.default_bg = "#fb9aaa"
buttonequal.bind("<Enter>", on_enter)
buttonequal.bind("<Leave>", on_leave)
buttonclear = tk.Button(root, text = "C", command = clear_field , width = 5, bg = "#fb9aaa", fg = "#1E1D1D", font = ("Comic Sans MS", 14))
buttonclear.grid(row = 2, column = 1, padx=5, pady=5)
buttonclear.default_bg = "#fb9aaa"
buttonclear.bind("<Enter>", on_enter)
buttonclear.bind("<Leave>", on_leave)


root.mainloop()


