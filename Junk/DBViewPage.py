import tkinter as tk
from tkinter import ttk, messagebox
import database

class DbPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Database - Home")
        self.root.geometry("900x500")
        self.root.configure(bg="#f8f8f8")

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True)

        self.setup_criminals_tab()
        # Add similar functions: setup_crimes_tab(), setup_stations_tab(), etc.

    def setup_criminals_tab(self):
        frame = ttk.Frame(self.tabs)
        self.tabs.add(frame, text="Criminals")

        self.criminals_tree = ttk.Treeview(frame, columns=("ID", "Name", "Gender", "DOB", "Address"), show='headings')
        for col in self.criminals_tree["columns"]:
            self.criminals_tree.heading(col, text=col)
            self.criminals_tree.column(col, width=150)
        self.criminals_tree.pack(fill="both", expand=True, pady=10, padx=10)

        self.load_criminals()

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Add Criminal", command=self.add_criminal).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_criminal).grid(row=0, column=1, padx=10)
        # You can also add: Update Selected

    def load_criminals(self):
        for row in self.criminals_tree.get_children():
            self.criminals_tree.delete(row)
        criminals = database.read_documents(database.criminals, {})
        for c in criminals:
            self.criminals_tree.insert('', 'end', values=(c["_id"], c["name"], c["gender"], c["dob"]["$date"][:10], c["address"]))

    def add_criminal(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Criminal")
        add_window.geometry("400x300")

        fields = ["ID", "Name", "Gender", "DOB (YYYY-MM-DD)", "Address"]
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(add_window, text=field).grid(row=i, column=0, pady=5, padx=10)
            entry = tk.Entry(add_window, width=30)
            entry.grid(row=i, column=1, pady=5)
            entries[field] = entry

        def save_criminal():
            data = {
                "_id": entries["ID"].get(),
                "name": entries["Name"].get(),
                "gender": entries["Gender"].get(),
                "dob": {"$date": entries["DOB (YYYY-MM-DD)"].get() + "T00:00:00.000Z"},
                "address": entries["Address"].get()
            }
            database.create_document(database.criminals, data)
            self.load_criminals()
            add_window.destroy()

        tk.Button(add_window, text="Save", command=save_criminal).grid(row=len(fields), column=0, columnspan=2, pady=10)

    def delete_criminal(self):
        selected = self.criminals_tree.selection()
        if not selected:
            messagebox.showwarning("Delete", "Select a criminal to delete.")
            return
        values = self.criminals_tree.item(selected[0])['values']
        database.delete_document(database.criminals, {"_id": values[0]})
        self.load_criminals()

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
