label ep25_quests_steve1:
    # инициализация сцен и входа
    $ add_hook("Teleport_Building", "ep25_quests_steve2", scene = "street_steve_office", priority = 200, label="steve_office_check_evening")
    $ add_hook("Teleport_Building", "ep25_quests_steve3", scene="street_steve_office", label = "steve_office_enter")
    return

label ep25_quests_steve2:
    # Вход в здание Стива, проверка на вечер
    if act == "l":
        return
    if day_time == "evening":
        mt "Уже вечер. Офис Стива закрыт."
        return False
    return

label ep25_quests_steve3:
    # Вход в офис Стива
    if act == "l":
        return
    if act == "w":
        m "here"
        call locations_init_steve_office()
        call change_scene("steve_office_secretary", "Fade_long", "snd_lift")
    return False
