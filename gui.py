import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from main import scan_ips
import subprocess
from src.database import load_data_to_tree


def open_file(filepath):
    subprocess.Popen(["notepad.exe", filepath])
    
def run_gui():
    root = tk.Tk()

    root.title("Shodan parser")
    root.geometry("1000x600")

    label = tk.Label(root, text = "Parser danych o wykrytych podatnosciach")
    label.pack(pady=10)

    button1 = tk.Button(root, text = "Skanuj adresy z pliku", command=scan_ips)
    button1.pack(pady=10)

    button2 = tk.Button(root, text = "Otworz plik ips.txt", command = lambda: open_file("input/ips.txt"))
    button2.pack(pady=10)

    button3 = tk.Button(root, text = "Otworz plik results.txt", command = lambda: open_file("output/results.txt"))
    button3.pack(pady=10)

    button4 = tk.Button(root, text = "Odświerz rekordy z bazy", command= lambda: load_data_to_tree(tree))
    button4.pack(pady=10)

    tree = ttk.Treeview(root)
    tree['columns'] = ("Id","Data skanu","IP","Porty","Organizacje","ISP","Kod kraju","Serwery","Typy serwera","Podatności","Domeny SSL")
    tree.column("#0", width=0, stretch=False)
    tree.column("Id", width=40, anchor="center")
    tree.column("Data skanu", width=120)
    tree.column("IP", width=100)
    tree.column("Porty", width=120)
    tree.column("Organizacje", width=200)
    tree.column("ISP", width=200)
    tree.column("Kod kraju", width=80, anchor="center")
    tree.column("Serwery", width=150)
    tree.column("Typy serwera", width=150)
    tree.column("Podatności", width=200)
    tree.column("Domeny SSL", width=200)

    tree.heading("Id", text="Id")
    tree.heading("Data skanu", text="Data skanu")
    tree.heading("IP", text="IP")
    tree.heading("Porty", text="Porty")
    tree.heading("Organizacje", text="Organizacja")
    tree.heading("ISP", text="ISP")
    tree.heading("Kod kraju", text="Kod kraju")
    tree.heading("Serwery", text="Serwery")
    tree.heading("Typy serwera", text="Typy serwera")
    tree.heading("Podatności", text="Podatności")
    tree.heading("Domeny SSL", text="Domeny SSL")

    scrollbar = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=scrollbar.set)

    scrollbar.pack(side="bottom", fill="x")
    tree.pack(fill="both", expand=True)

    def on_row_click(event):
        item = tree.focus()
        values = tree.item(item, "values")

        messagebox.showinfo(
            "Szczegóły hosta",
            f"""
                ID: {values[0]}
                IP: {values[2]}

                Porty:
                {values[3]}

                Serwery:
                {values[7]}

                Typy serwera:
                {values[8]}

                Podatności:
                {values[9]}

                Domeny SSL:
                {values[10]}
            """
                    )
    
    tree.bind("<Double-1>", on_row_click)

    load_data_to_tree(tree)

    root.mainloop()


run_gui()