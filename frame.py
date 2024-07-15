import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import databases

app = customtkinter.CTk()
app.title('Guessing Game')
app.geometry('900x420')
app.config(bg='#161C25')
app.resizable(False,False)

font1 = ('Arial',20,'bold')
font2 = ('Arial',12,'bold')


menu = customtkinter.CTkOptionMenu(app)
menu.pack(padx=10,pady=15)
kjkm,87h,first_number = customtkinter.CTkLabel(app, font=font1,text='First Number:', text_color='#fff',bg_color='#161C25')
first_number.place(x=20,y=50)

first_number_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
first_number_entry.bind("<FocusIn>",lambda e: first_number_entry.delete('0','end'))
first_number_entry.place(x=200, y=50)

second_number = customtkinter.CTkLabel(app, font=font1,text='SECOND Number:', text_color='#fff',bg_color='#161C25')
second_number.place(x=20,y=100)

second_number_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
second_number_entry.bind("<FocusIn>",lambda e: second_number_entry.delete('0','end'))
second_number_entry.place(x=200,y=100)

third_number = customtkinter.CTkLabel(app, font=font1,text='THIRD Number:', text_color='#fff',bg_color='#161C25')
third_number.place(x=20,y=150)

third_number_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
third_number_entry.bind("<FocusIn>",lambda e: second_number_entry.delete('0','end'))
third_number_entry.place(x=200,y=150)


style = ttk.Style(app)
style.theme_use('clam')
style.configure('TreeView', font=font2,foreground='#fff',background='#000',fieldbackground='#313837')
style.map('TreeView', background=[('selected','#1ABF2D')])

tree =ttk.Treeview(app,height=5)

tree['columns']=('id')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('id', anchor=tk.CENTER, width=120)

tree.heading('id',text='Result')




tree.place(x=400,y=50)







app.mainloop()