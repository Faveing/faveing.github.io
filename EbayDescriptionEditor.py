import tkinter as tk
from tkinter import ttk

def main_screen():

    global root

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

    root.config(menu=menubar)

    main_frame = tk.Frame()

    ask_file_botton = tk.Button(text="")

def Open():
    filename = tk.filedialog.askopenfilename(initialdiri = "C:\Users\Baby Carrot", title = "Select file", filetypes = (("html","*.html")))

def Logout():
    quit()

main_screen()

tk.mainloop()