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


    TButton: A standard push-button widget.
    TCheckbutton: A checkbutton widget that can be in two states, checked and unchecked.
    TCombobox: A combination of a text field and a drop-down list.
    TEntry: A basic text-entry widget.
    TFrame: A simple container widget.
    TLabel: A widget to display text or images.
    TLabelFrame: A container widget, like a frame but with an optional title.
    TMenubutton: A button that can pop up a menu when pressed.
    TPanedwindow: A container widget that contains one or more resizable panes.
    TProgressbar: A widget to show the progress of an operation.
    TRadiobutton: A widget that creates a radio button.
    TScale: A slider widget.
    TScrollbar: A widget that provides a scroll bar.
    TSeparator: A separator widget, often used to separate groups of other widgets.
    TSizegrip: A size grip widget, typically seen at the bottom right corner of resizable windows.
    TNotebook: A notebook (tabbed) widget.
    TTreeview: A multicolumn listbox or tree view widget.
