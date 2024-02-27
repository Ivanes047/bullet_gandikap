from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
from login_page import create_login_page
from style import set_style
import os

basedir = os.path.dirname(__file__)

window = Tk()
window.geometry('600x400')
window.title("Пулька Гандикап")
style = ttk.Style()
set_style(style)
tab_control = ttk.Notebook(window, style="TNotebook")
create_login_page(tab_control)
tab_control.pack(expand=1, fill='both')
window.iconbitmap(os.path.join(basedir, "icon.ico"))

window.mainloop()