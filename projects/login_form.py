import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Database connection function
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="sachin",
        password="Raoinfotech@123",
        database="login_db"
    )

# Login function
def login():
    uname = username_entry.get().strip()
    pwd = password_entry.get().strip()

    if uname == "" or pwd == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (uname, pwd))
        row = cursor.fetchone()
        if row:
            messagebox.showinfo("Success", f"Welcome {uname}")
        else:
            messagebox.showerror("Failed", "Invalid Username or Password")
        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Database Error: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Login Form")
root.geometry("400x300")

# Load background image using Pillow
try:
    bg_image = Image.open("/home/raoinfotech/vscode/python/projects/bgimage.png")
    bg_image = bg_image.resize((400, 300), Image.Resampling.LANCZOS)  # Fixed for Pillow 10+
    bg_photo = ImageTk.PhotoImage(bg_image)
except Exception as e:
    messagebox.showerror("Image Error", f"Failed to load background image:\n{str(e)}")
    root.destroy()
    exit()

# Create canvas and set background
canvas = tk.Canvas(root, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create a frame for the login form on top of the background
form_frame = tk.Frame(root, bg="white", bd=2)
form_frame.place(relx=0.5, rely=0.5, anchor="center")

# Username
tk.Label(form_frame, text="Username", bg="white").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password
tk.Label(form_frame, text="Password", bg="white").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login Button
tk.Button(form_frame, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()