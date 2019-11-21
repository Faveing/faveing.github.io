import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import json
import xml.dom.minidom
from html.parser import HTMLParser
import re

def main_screen():

    global root
    global link_entry
    global descirption

    root = tk.Tk()
    root.title("SimplyInventory")
    width = 1500
    height = 1000
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenmmheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (width/2)

    root.geometry("1500x1000")
    #root.resizable(0,0)

    banner = tk.Frame(root)
    banner.pack(pady=10)

    #titleBanner = tk.Label(banner, text="Simply Inventory")
    #titleBanner.pack()
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu2 = tk.Menu(menubar, tearoff=0)
    menu3 = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=Open)
    filemenu.add_command(label="Save")
    filemenu.add_cascade(label="Quit", command=Logout)
    menubar.add_cascade(label="File", menu=filemenu)

    product_frame = tk.Frame(root)

    link_entry = tk.Entry(product_frame)
    descirption = tk.Text(product_frame)
    tk.Label(product_frame, text="Product Link:").grid(row=1, column=0)
    tk.Label(product_frame, text="Product Description:").grid(row=2, column=0)

    link_entry.grid(row=1, column=1)
    descirption.grid(row=2, column=1)
    product_frame.pack()

    root.config(menu=menubar)

    main_frame = tk.Frame()

    ask_file_botton = tk.Button(text="")

def update_products(link, textdescription):
    link_entry.insert("0", link)
    descirption.insert("1.0", textdescription)

def Open():
    filename = tk.filedialog.askopenfilename(title = "Select file", filetypes =(("Html Files", "*.html"),("All Files","*.*")))

    print(filename)

    textfile = open(filename, "r")

    openedhtml = textfile.read()

    product = openedhtml.split("<!-- Product -->")

    link = product[1].split("<!-- Image link -->")

    link = link[1].split("<!-- Link -->")

    print(link[1])

    link = link[1].split("'")

    print(link[1])

    textdescription = product[1].split("<!-- Description Text-->")

    update_products(link[1], textdescription[1])

    # print(openedhtml)

    textfile.close()

def Logout():
    quit()

main_screen()

tk.mainloop()