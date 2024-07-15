import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import databases
from newp import page


app = customtkinter.CTk()
app.title('Employees Management System')
app.geometry('900x420')
app.config(bg='#161C25')
#app.resizable(False,False)
font1 = ('Arial',20,'bold')
font2 = ('Arial',12,'bold')


def add_to_treeview():
    employees = databases.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
       tree.insert('', END, values=employee)


def insert():
    id = id_entry.get()
    name = name_entry.get()
    role = role_entry.get()
    gender: str = variablr1.get()
    status = status_entry.get()
    if not (id and name and role and gender and status):
        messagebox.showerror('Error','Enter all fields.')
    elif databases.id_exist(id):
        messagebox.showerror('Error', 'ID already exists.')

    else:
        databases.insert_employee(id, name,role, gender, status,)
        add_to_treeview()
        messagebox.showinfo('success', 'Data has been inserted.')



add_button = customtkinter.CTkButton(app,command=page,font=font1,text_color='#fff',cursor='hand2',text='Add Employee', fg_color='#05A312',bg_color='#161C25',border_color='#157004', border_width=2,corner_radius=15,width=260,hover_color='#00850B')
add_button.place(x=561,y=390)

id_label = customtkinter.CTkLabel(app, font=font1, text='ID:', text_color='#fff', bg_color='#161C25',)
id_label.place(x=20, y=20)

id_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
id_entry.bind("<FocusIn>",lambda e: id_entry.delete('0','end'))

id_entry.place(x=100, y=20)


name_label = customtkinter.CTkLabel(app, font=font1,text='NAME:', text_color='#fff',bg_color='#161C25')
name_label.place(x=20,y=80)

name_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
name_entry.bind("<FocusIn>",lambda e: name_entry.delete('0','end'))

name_entry.place(x=100,y=80)

role_label = customtkinter.CTkLabel(app, font=font1,text='Role:', text_color='#fff',bg_color='#161C25')
role_label.place(x=20,y=140)

role_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
role_entry.bind("<FocusIn>",lambda e: role_entry.delete('0','end'))

role_entry.place(x=100,y=140)

gender_label = customtkinter.CTkLabel(app, font=font1,text='Gender:', text_color='#fff',bg_color='#161C25')
gender_label.place(x=20,y=200)

options = ['Male','Female']
variablr1 = StringVar()

gender_option = customtkinter.CTkComboBox(app,font=font1,text_color='#0C9295', button_hover_color='#0C9295',border_color ='#0C9295',width=180,variable=variablr1,values=options)
gender_option.set('Male')
gender_option.place(x=100,y=200)

status_label = customtkinter.CTkLabel(app, font=font1,text='Status:', text_color='#fff',bg_color='#161C25')
status_label.place(x=20,y=260)

status_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff', border_color='#0C9295',border_width=2, width=180)
status_entry.bind("<FocusIn>",lambda e: status_entry.delete('0','end'))
status_entry.place(x=100,y=260)

add_button = customtkinter.CTkButton(app,command=insert,font=font1,text_color='#fff',cursor='hand2',text='Add Employee', fg_color='#05A312',bg_color='#161C25',border_color='#157004', border_width=2,corner_radius=15,width=260,hover_color='#00850B')
add_button.place(x=20,y=310)

clear_button = customtkinter.CTkButton(app,font=font1,text_color='#fff',cursor='hand2',text='Clear Employee', fg_color='#161C25',bg_color='#161C25',border_color='#157004', border_width=2,corner_radius=15,width=260,hover_color='#FF5002')
clear_button.place(x=20,y=360)

update_button = customtkinter.CTkButton(app,font=font1,text_color='#fff',cursor='hand2',text='Update Employee', fg_color='#161C25',bg_color='#161C25',border_color='#157004', border_width=2,corner_radius=15,width=260,hover_color='#FF5002')
update_button.place(x=300,y=360)

delete_button = customtkinter.CTkButton(app,font=font1,text_color='#fff',cursor='hand2',text='Delete Employee', fg_color='#E40404',bg_color='#161C25',border_color='#E40404', border_width=2,corner_radius=15,width=260,hover_color='#AE0000')
delete_button.place(x=580,y=360)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('TreeView', font=font2,foreground='#fff',background='#000',fieldbackground='#313837')
style.map('TreeView', background=[('selected','#1ABF2D')])

tree =ttk.Treeview(app,height=15)

tree['columns']=('id','name','role','gender','status')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('id', anchor=tk.CENTER, width=120)
tree.column('name', anchor=tk.CENTER, width=120)
tree.column('role', anchor=tk.CENTER, width=120)
tree.column('gender', anchor=tk.CENTER, width=100)
tree.column('status',anchor=tk.CENTER,width=120)

tree.heading('id',text='ID')
tree.heading('name',text='Name')
tree.heading('role',text='Role')
tree.heading('gender',text='Gender')
tree.heading('status',text='Status')

tree.place(x=300,y=20)


#add_to_treeview()






app.mainloop()