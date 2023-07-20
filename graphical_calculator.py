
#Mohammad Zim


import tkinter as tk

def button_click(button_value):
    current = display_entry.get()
    if button_value == "C":
        current = ""
    elif button_value == "=":
        try:
            current = str(eval(current))
        except Exception:
            current = "Error"
    else:
        current += button_value
    display_entry.delete(0, tk.END)
    display_entry.insert(tk.END, current)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create and place the display entry widget
display_entry = tk.Entry(window)
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create and place the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row = 1
column = 0
for button in buttons:
    button_widget = tk.Button(window, text=button, width=5, height=2, command=lambda value=button: button_click(value))
    button_widget.grid(row=row, column=column, padx=5, pady=5)
    column += 1
    if column > 3:
        column = 0
        row += 1

# Start the main loop
window.mainloop()
