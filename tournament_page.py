from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
import config
from get_info_from_challonge import get_info_about_tournament
import time

def create_tour_page(tab_control, matches, players, tour):
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=f"Тур №{tour}")  
    i = 1
    for match in matches:
        frame = ttk.Frame(tab)
        frame.pack(padx=0, pady=5)
        times, name1, name2, winner = make_match(match, players)
        time1 = times[0]
        time2 = times[1]
        
        lbl_time1 = ttk.Label(frame, text=time1, style="T.TLabel")
        lbl_time1.grid(column = 0, row=i, ipady=2)
        lbl_name1 = ttk.Label(frame, text=name1, style="BW.TLabel")
        lbl_name1.grid(column = 1, row=i, sticky='W')
        lbl_result1 = ttk.Label(frame, text='W' if winner == 1 else ' ', style='Win.TLabel' if winner == 1 else 'Los.TLabel', anchor="center")
        lbl_result1.grid(column = 2, row=i, ipady=1)
        
        lbl_time2 = ttk.Label(frame, text=time2, style="T.TLabel")
        lbl_time2.grid(column = 0, row=i+1, ipady=2)
        lbl_name2 = ttk.Label(frame, text=name2, style="BW.TLabel")
        lbl_name2.grid(column = 1, row=i+1, sticky='W')
        lbl_result2 = ttk.Label(frame, text='W' if winner == -1 else ' ', style='Win.TLabel' if winner == -1 else 'Los.TLabel', anchor="center")
        lbl_result2.grid(column = 2, row=i+1, ipady=1)
        i+=2
        
    frame_btn = ttk.Frame(tab)
    frame_btn.pack(padx=5, pady=5)
    btn = ttk.Button(frame_btn, text="Обновить!", cursor='hand2', style="TButton", command=lambda: clicked(config.user, config.api, config.id_tourn, tab_control))  
    btn.grid(pady=[20, 0])  
        
        
def make_match(match, players):
    player_1 = players[match[0]]
    player_2 = players[match[1]]
    winner = 0
    if (match[0] == match[2]):
        winner = 1
    elif (match[1] == match[2]):
        winner = -1
    if (player_1[1] > player_2[1]):
        return gandikap(player_1[1] - player_2[1]), player_2[0], player_1[0], -winner
    else:
        return gandikap(player_2[1] - player_1[1]), player_1[0], player_2[0], winner
    
def gandikap(diff):
    if (diff < 100):
        return "1:00", "1:00"
    elif (diff < 200):
        return "1:05", "0:55"
    elif (diff < 300):
        return "1:10", "0:50"
    elif (diff < 400):
        return "1:15", "0:45"
    elif (diff < 500):
        return "1:20", "0:40"
    elif (diff < 600):
        return "1:25", "0:35"
    elif (diff < 700):
        return "1:30", "0:30"
    elif (diff < 800):
        return "1:35", "0:25"
    elif (diff < 1000):
        return "1:40", "0:20"
    elif (diff < 1200):
        return "1:45", "0:15"
    elif (diff < 1500):
        return "1:50", "0:10"
    else:
        return "1:55", "0:05"
    

def clicked(username, api_key, id_tournament, tab_control):
    try:
        partii, players = get_info_about_tournament(username, api_key, id_tournament)
        config.user = username
        config.api = api_key
        config.id_tourn = id_tournament
        active_tab = tab_control.index(tab_control.select())
        for tab in tab_control.tabs():
            tab_control.forget(tab)
        for i in range(1, len(partii)+1):
            create_tour_page(tab_control, partii[i], players, i)
        tab_control.select(active_tab)
    except Exception as ex:
        messagebox.showerror('Ошибка', ex)
        