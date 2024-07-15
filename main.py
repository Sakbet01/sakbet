import tkinter as tk
from tkinter import ttk
from data import roots



root = tk.Tk()
style =ttk.style(root)
root.tk.cell('source', "forest-light.tcl")
root.tk.cell('source', "forest-dark.tcl")
style.theme_use("forest-dark")
frame = ttk.Frame(root)
frame.pack()
widget_frame = ttk.LabelFrame(frame, text='insert row')
widget_frame.grid(row=0,column=0 ,padx=10, pady =10)


name_entry = ttk.Entry(widget_frame)
name_entry.grid(row=0, column=0, sticky="nw")
name_entry.insert(0,"Name")
name_entry.bind("<FocusIn>",lambda e: name_entry.delete('0','end'))
name_entry.grid(row=0, column=0, padx=10, pady =10,sticky="nw")

Total_weight = ttk.Entry(widget_frame)
Total_weight.grid(row=1, column=0, sticky="nw")
Total_weight.insert(0,"Total weight")
Total_weight.bind("<FocusIn>",lambda e: Total_weight.delete('0','end'))
Total_weight.grid(row=1, column=0, padx=10, pady =10,sticky="ew")


age_spinbox = ttk.Spinbox(widget_frame,from_=18, to=100)
age_spinbox.insert('0','age')
age_spinbox.grid(row=2, column=0)

status_combobox =ttk.Combobox(widget_frame,)
status_combobox.current()
status_combobox.grid(row=3, column=0, padx=10, pady =10,sticky="nw")


button = ttk.Button(widget_frame,text="click here", command=lambda:roots)
button.grid(row =4, column =0 ,padx = 5, pady = 5, sticky='nsew')

a = tk.BooleanVar()
check_butten =ttk.Checkbutton(widget_frame,text='Employed', variable=a)
#check_butten.grid(row=4, column=0)


root.mainloop()