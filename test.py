import tkinter as tk
from tkinter import ttk, filedialog

def inspect_widgets(window):
    for child in window.winfo_children():
        print(type(child), child.winfo_class(), child)
        inspect_widgets(child)

def poll_widgets():
    print("------")
    inspect_widgets(root)
    root.after(1000, poll_widgets)  # poll every 1000ms (1 second)

root = tk.Tk()
ttk.Button(root, text="Open File Dialog", command=filedialog.askopenfilename).pack()

poll_widgets()  # Start polling
root.mainloop()



def modify_optionmenu_dropdown(menu):
    for item in menu.winfo_children():
        if isinstance(item, tk.Menu):
            item.config(foreground='red')
            modify_optionmenu_dropdown(item)
