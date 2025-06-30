import mysql.connector
import tkinter as tk
# from tkinter import Tk
from tkinter import messagebox

class User:
    def __init__(self, name, email, phone,age):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        
def connect_to_sqlServer():
    
    try:
        conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        port = 3306)
        return conn
    except mysql.connector.Error as error:
        print("Could not able to reach server:{error}")
        messagebox.showerror("Error","Could not able to reach server:{error}")
        exit(1)
        
        
def initialize_database():
    try:
        conn = connect_to_sqlServer()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS userDB")
        cursor.close()
    except AttributeError as error:
        print("Cannot init : {error}")
        messagebox.showerror("Error","Could not Initialize DB:{error}")
        exit(1)
    

def connect_to_database():
    try:
        conn = connect_to_sqlServer()
        conn.database = "userDB"
        return conn
    except mysql.connector.Error as error:
        print("Could not able to connect database: {error}")
        messagebox.showerror("Error","Could not connect:{error}")
        exit(1)
    
def  creat_table():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS userData(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), email VARCHAR(50), phone VARCHAR(20), age INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS login (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")
    conn.commit()
    cursor.close()
    conn.close()
    
def insert_user():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    age = age_entry.get()
    
    try:
        user  = User(name,email,phone,age)
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO userData (name, email, phone, age) VALUES (%s,%s,%s,%s)",(user.name, user.email, user.phone, user.age))
        conn.commit()
        cursor.close()
        conn.close()
        print("User data inserted")
        messagebox.showinfo("Success", "Data Inserted")
    except Exception as e:
        print("Insert error: {e}") 
        messagebox.showerror("Failed", "Data not Inserted")
        
def read_users():
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userData")
        rows = cursor.fetchall()
        print("USer Data: \n")
        result = ""
        for row in rows:
            print(row)
            result += f"ID: {row[0]}, Name: {row[1]}, email: {row[2]}, phone: {row[3]}, age: {row[4]}\n" 
        messagebox.showinfo("All USers", result)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Read error: {e}")
        messagebox.showerror("Read error: {e}")
        
# def delete_user_by_name():
#     try:
#         conn = connect_to_database()
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM userData WHERE name = %s", (name_var.get(),))
#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("Deleted Data")
#     except Exception as e:
#         print("Error delete: {e}") "hello " +"hello" = "hello hello"
        
        
def launch_main_app():
    root = tk.Tk()
    root.title("MySQL App")
    root.geometry("500x600")

    global name_entry,email_entry,phone_entry,age_entry
    #create lable
    name_label= tk.Label(root, text="Name")
    name_label.grid(row=0,column=0,padx=5,pady=10)
    email_label = tk.Label(root, text="Email")
    email_label.grid(row=1,column=0,padx=5,pady=10)
    phone_lable = tk.Label(root,text="Phone")
    phone_lable.grid(row=2,column=0,padx=5,pady=10)
    age_lable = tk.Label(root,text="Age")
    age_lable.grid(row=3,column=0,padx=5,pady=10)

    #create entry
    name_entry= tk.Entry(root)
    name_entry.grid(row=0,column=1,padx=5,pady=10)
    email_entry = tk.Entry(root)
    email_entry.grid(row=1,column=1,padx=5,pady=10)
    phone_entry = tk.Entry(root)
    phone_entry.grid(row=2,column=1,padx=5,pady=10)
    age_entry = tk.Entry(root)
    age_entry.grid(row=3,column=1,padx=5,pady=10)



    btn1 = tk.Button(root, text="Insert Data",command=insert_user)
    btn1.grid(row=4,column=0,padx=5,pady=10)
    btn2 = tk.Button(root,text="Read User",command=read_users)
    btn2.grid(row=5,column=0,padx=5,pady=10)
    btn3 = tk.Button(root,text="Exit", command=root.destroy)
    btn3.grid(row=6,column=0,padx=5,pady=10)

    root.mainloop()

def registeration_window():
    reg = tk.Tk()
    reg.title("Register")
    reg.geometry("300x250")
    tk.Label(reg,text="Username").pack()
    tk.Label(reg,text="Passwword").pack()
    
    new_user = tk.Entry(reg)
    new_user.pack()
    
    new_pass = tk.Entry(reg,show="*")
    new_pass.pack()
    
    def register_user():
        uname = new_user.get()
        pwd = new_pass.get()
        
        if not uname or not pwd:
            messagebox.showwarning("Missing","Username and password is required")
            return
        
        try:
            conn = connect_to_database()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO login(username,password) VALUES(%s,%s)",(uname,pwd))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Successs", "Username created")
            reg.destroy()
        except Exception as e:
            messagebox.showerror("Error", "Registraion Failed")
    reg_button = tk.Button(reg,text="Regiter",command=register_user)
    reg_button.pack()
    reg.mainloop()
    
def login_window():
    login = tk.Tk()
    login.title("Login")
    login.geometry("300x250")
    
    tk.Label(login,text="Username").pack()
    tk.Label(login,text="Passwword").pack()
    
    username_entry = tk.Entry(login)
    username_entry.pack()
    
    password_entry = tk.Entry(login,show="*")
    password_entry.pack()
    
    def validate_login():
        uname = username_entry.get()
        pwd = password_entry.get()
        if not uname or not pwd:
            messagebox.showwarning("Missing","Username and password is required")
            return
        
        try:
            conn = connect_to_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s",(uname,pwd))
            result  = cursor.fetchone()
            if result:
                messagebox.showinfo("SUccess","Login validated")
                login.destroy()
                launch_main_app()
            else:
                messagebox.showerror("Errro", "Invalid Credentials")
            cursor.close()
            conn.close()
            
        except Exception as e:
            messagebox.showerror("Error", "Login Failed")
        # if uname == "admin" and pwd == "admin123":
        #     print("login has successfull")
        #     messagebox.showinfo("SUccess","Login validated")
        #     login.destroy()
        #     launch_main_app()
            
        # else:
        #     messagebox.showerror("Errro", "Invalid Credentials")
            
    login_button = tk.Button(login,text="Login",command=validate_login)
    register_button = tk.Button(login,text="Register",command=registeration_window)
    login_button.pack()
    register_button.pack()
    login.mainloop()


initialize_database()
creat_table()
login_window()

















# while True:
    
#     choice = input("Enter Users Choice:")
#     if choice == "1":
#         name  = input("Enter Name: ")
#         email = input("enter email: ")
#         phone = input("enter mobile: ")
#         age = input("Age: ")
#         user  = User(name,email,phone,age)
#         insert_user(user)
        
#     if choice == "2":
#         read_users()
    
