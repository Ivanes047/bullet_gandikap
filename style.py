def set_style(style):
    style.theme_use('default')
    
    style.configure("L.TLabel", foreground="white", background = "#272A33", font=("Inter", 12))
    
    # Игроки
    style.configure("BW.TLabel", foreground="white", background="#58595e", font=("Inter", 12), width=20, padding = [5, 0])
    
    # Победитель
    style.configure("Win.TLabel", background="#FF7324", font=("Inter", 10), foreground="white", width = 3)
    # Проигравший
    style.configure("Los.TLabel", background="#787a80", font=("Inter", 10), width = 3)
    # Время
    style.configure("T.TLabel", foreground="black", background="#787a80", font=("Inter", 8), padding = [2, 0])

    style.configure('TFrame', background = "#272A33")
    
    # Вкладки
    style.configure("TNotebook", background="#272A33")
    style.map("TNotebook.Tab", background=[("selected", "#FF7324")])
    style.configure("TNotebook.Tab", background="#272A33", foreground="white", focuscolor="#FF7324", padding=[10, 0])
    
    # Кнопка
    style.map("TButton",
    foreground=[('!active', 'white'),('pressed', 'white'), ('active', 'white')],
    background=[ ('!active','#FF7324'),('pressed', '#FF7324'), ('active', '#FF7324')],
    focuscolor="#FF7324"
    )