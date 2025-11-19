import tkinter as tk
import mysql.connector
from tkinter import messagebox
root=tk.Tk()
attempts=3
def login():
    USERNAME=username_enterd.get()
    PASSWORD=password_entry.get()
    conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="********************",
            database="56r",
            port="3306"
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM LOGIN WHERE USERNAME=%s AND USER_PASSWORD=%s",(USERNAME,PASSWORD))
    result=cur.fetchone()
    
    if result:
        messagebox.showinfo("login successfull","LOGIN SUCCESSFULL!!!!!!!!!")
    else:
        global attempts
        attempts-=1
        messagebox.showwarning("unsuccessful ",f"left attempts:{attempts}")
        if attempts==0:
            messagebox.showerror("locked","too many attemps")
    
    conn.close()

root.title('MY FIRST GUI')
root.geometry('500x500')
tk.Label(root,text='USERNAME').grid(row=0,column=0,pady=20)
username_enterd=tk.Entry(root)
username_enterd.grid(row=0,column=1)


tk.Label(root,text='PASSWORD').grid(row=1,column=0)
password_entry=tk.Entry(root)
password_entry.grid(row=1,column=1)



tk.Button(root,text='LOGIN',command=login).grid(row=2,column=2)



root.mainloop()
















