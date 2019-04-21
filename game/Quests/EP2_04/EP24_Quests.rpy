default ep24_quests_initialized = False

label ep24_quests_init:
    # Инициализация v0.4
    $ set_var("Monica", zorder=15, scene="hostel_edge_1_a")
    call floor2_init_addition1() from _call_floor2_init_addition1 #Барди floor2
    call bedroom1_init_addition1() from _call_bedroom1_init_addition1 # Барди bedroom1
    if char_info["Bardie"]["level"] == 3:
        $ char_info["Bardie"]["enabled"] = False
        $ char_info["Bardie"]["caption_diabled"] = _("Ожидание дальнейшего прогресса сюжета игры...")
        $ char_info["Bardie"]["show_caption_diabled"] = True
        help "Открыто продолжение истории с Барди"
    if char_info["Betty"]["level"] == 4:
        $ char_info["Betty"]["enabled"] = False
        $ char_info["Betty"]["caption_diabled"] = _("Ожидание дальнейшего прогресса сюжета игры...")
        $ char_info["Betty"]["show_caption_diabled"] = True
        help "Открыто продолжение истории с Бетти"

    $ ep24_quests_initialized = True

    return
