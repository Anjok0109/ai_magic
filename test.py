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


style.configure('TButton', foreground='#F6F6F7')
style.configure('TCheckbutton', foreground='#F6F6F7')
style.configure('TCombobox', foreground='#F6F6F7')
style.configure('TEntry', foreground='#F6F6F7')
style.configure('TFrame', foreground='#F6F6F7')
style.configure('TLabel', foreground='#F6F6F7')
style.configure('TLabelFrame', foreground='#F6F6F7')
style.configure('TMenubutton', foreground='#F6F6F7')
style.configure('TPanedwindow', foreground='#F6F6F7')
style.configure('TProgressbar', foreground='#F6F6F7')
style.configure('TRadiobutton', foreground='#F6F6F7')
style.configure('TScale', foreground='#F6F6F7')
style.configure('TScrollbar', foreground='#F6F6F7')
style.configure('TSeparator', foreground='#F6F6F7')
style.configure('TSizegrip', foreground='#F6F6F7')
style.configure('TNotebook', foreground='#F6F6F7')
style.configure('TTreeview', foreground='#F6F6F7')
