import tkinter as tk
from tkinter import messagebox, ttk
import database
import os

class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login / Sign Up")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.login_frame = tk.Frame(root, bg="#f0f0f0")
        self.signup_frame = tk.Frame(root, bg="#f0f0f0")

        self.setup_styles()
        self.setup_login()
        self.setup_signup()

        self.login_frame.pack(fill="both", expand=True)

    def setup_styles(self):
        style = ttk.Style()
        style.configure("TEntry", padding=5)
        style.configure("TButton", padding=5, font=("Arial", 10, "bold"))
        style.map("TButton", background=[('active', '#0052cc')], foreground=[('active', 'white')])

    def add_placeholder(self, entry, placeholder_text, is_password=False):
        entry.insert(0, placeholder_text)

        def on_focus_in(event):
            if entry.get() == placeholder_text:
                entry.delete(0, 'end')
                if is_password:
                    entry.config(show='*')

        def on_focus_out(event):
            if entry.get() == '':
                entry.insert(0, placeholder_text)
                if is_password:
                    entry.config(show='')

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def create_title(self, frame, text):
        return tk.Label(frame, text=text, font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")

    def setup_login(self):
        self.create_title(self.login_frame, "Login").pack(pady=20)

        self.login_username = ttk.Entry(self.login_frame, width=30)
        self.login_username.pack(pady=10)
        self.add_placeholder(self.login_username, "Username")

        self.login_password = ttk.Entry(self.login_frame, width=30)
        self.login_password.pack(pady=10)
        self.add_placeholder(self.login_password, "Password", is_password=True)

        ttk.Button(self.login_frame, text="Login", command=self.login).pack(pady=15)
        ttk.Button(self.login_frame, text="Go to Sign Up", command=self.show_signup).pack()

    def setup_signup(self):
        self.create_title(self.signup_frame, "Sign Up").pack(pady=20)

        self.signup_username = ttk.Entry(self.signup_frame, width=30)
        self.signup_username.pack(pady=10)
        self.add_placeholder(self.signup_username, "New Username")

        self.signup_password = ttk.Entry(self.signup_frame, width=30)
        self.signup_password.pack(pady=10)
        self.add_placeholder(self.signup_password, "New Password", is_password=True)

        ttk.Button(self.signup_frame, text="Sign Up", command=self.signup).pack(pady=15)
        ttk.Button(self.signup_frame, text="Go to Login", command=self.show_login).pack()

    def login(self):
        user = self.login_username.get()
        pwd = self.login_password.get()
        found = database.read_documents(database.users, {"username": user, "password": pwd})
        if found:
            messagebox.showinfo("Login", f"Welcome back, {user}!")
            self.user = user
            self.root.destroy()
            self.open_home()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def signup(self):
        user = self.signup_username.get()
        pwd = self.signup_password.get()

        if database.read_documents(database.users, {"username": user}):
            messagebox.showerror("Sign Up Failed", "Username already exists.")
            return

        database.create_document(database.users, {"username": user, "password": pwd})
        messagebox.showinfo("Sign Up", f"Signed up as {user}")
        self.show_login()
        self.root.destroy()
        self.open_home()

    def show_signup(self):
        self.login_frame.pack_forget()
        self.signup_frame.pack(fill="both", expand=True)

    def show_login(self):
        self.signup_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def open_home(self):
        from HomePage import HomePage  # If HomePage is in home.py

        home_root = tk.Tk()
        HomePage(home_root, self.user)
        home_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()
