from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
from tournament_page import clicked

def create_login_page(tab_control):
    tab1 = ttk.Frame(tab_control, style="TFrame")  
    tab_control.add(tab1, text='Вход')
    frame = ttk.Frame(tab1)
    frame.pack(padx=5, pady=5)
    frame_btn = ttk.Frame(tab1)
    lbl1 = ttk.Label(frame, text="Username: ", style="L.TLabel")
    lbl1.grid(column=0, row=0, sticky='NE', pady=[20, 0])
    username = ttk.Entry(frame,width=45) 
    username.grid(column=1, row=0, pady=[20, 0])
    
    lbl2 = ttk.Label(frame, text="Api key: ", style="L.TLabel")
    lbl2.grid(column=0, row=1, sticky='NE')
    api_key = ttk.Entry(frame,width=45)  
    api_key.grid(column=1, row=1)  
    
    lbl3 = ttk.Label(frame, text="ID турнира: ", style="L.TLabel")
    lbl3.grid(column=0, row=2, sticky='NE')
    id_tournament = ttk.Entry(frame,width=45)  
    id_tournament.grid(column=1, row=2)  
    
    frame_btn.pack(padx=5, pady=5)
    btn = ttk.Button(frame_btn, text="Войти!", cursor='hand2', command=lambda: clicked(username.get(), api_key.get(), id_tournament.get(), tab_control), style="TButton")  
    btn.grid(pady=[20, 0])  
    
