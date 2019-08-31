default ep27_quests_initialized = False
label ep27_quests1:
    # Инициализация v0.7
    $ char_info["Bartender"]["enabled"] = True 
    $ ep27_quests_initialized = True
    return
