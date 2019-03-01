

label ep23_quests_melanie1: # Моника подходит первый раз попросить о помощи
    call ep23_dialogues5_2()
    if _return == False:
        call refresh_scene_fade()
        return False
    $ monicaNeedToAskMelanieForHelp = False
    if monicaOutfitsEnabled[3] == False:
        $ melanieWaitingOpenedOutfits = True #Если костюм еще не открыт, то запускаем открытие по достижению костюма 4
    else:
        $ monicaOutfitsEnabled[4] = True # Открываем фотосессию с Мелани
    $ add_hook("Melanie", "ep23_quests_melanie2", scene="monica_office_photostudio")

    $ add_object_to_scene("Teleport_Monica_Office_MakeupRoom", {"type":3, "text" : _("ГРИМЕРНАЯ КОМНАТА"), "larrow" : "arrow_left_2", "base":"empty", "click" : "monica_office_photostudio_teleport", "xpos" : 276, "ypos" : 983, "zorder":12, "teleport":True})
    $ add_location("monica_office_makeup_room", caption=_("ГРИМЕРНАЯ КОМНАТА"), label="monica_office_makeup_room", init_label="monica_office_makeup_room_init", parent="monica_office_entrance")
    $ char_info["Melanie"]["enabled"] = True
    $ char_info["Melanie"]["caption"] = _("Мелани очень любит себя.")
    $ add_char_progress("Melanie", 10, "Melanie_help1")
    call questLog_init()
    $ questLog(13, False)
    $ questLog(24, True)

    call refresh_scene_fade()
    return

label ep23_quests_melanie2: #Если Моника подходит к Мелани после этого, то Мелани отвечает когда будет фотосессия.
    if act=="l":
        return
    call ep23_dialogues5_2a()
    call refresh_scene_fade()
    return False

label ep23_quests_melanie3: #Фотосессия завершена
    $ monicaOutfitsEnabled[4] = False # Закрываем фотосессию с Мелани
    $ add_hook("Teleport_Monica_Office_Entrance", "ep23_dialogues5_3b", scene="monica_office_secretary", label="photoshoot_melanie_exit", priority = 101) #Блокируем выход пока не получили деньги от Бифа

    $ move_object("Melanie", "monica_office_makeup_room")
    $ add_hook("Melanie_Life_day", "ep23_quests_melanie_life1", scene="global", label="melanie_makeuproom_life")
    $ add_hook("Melanie_Life_evening", "ep23_quests_melanie_life1", scene="global", label="melanie_makeuproom_life")
    $ add_hook("Melanie", "ep23_quests_melanie4", scene="monica_office_makeup_room", label="melanie_makeuproom_life")
    $ add_hook("change_time_evening", "ep23_quests_melanie6", scene="global") # Мелани пойдет к Дику
    return

label ep23_quests_melanie_life1: #Мелани все время находится в гримерке
    $ move_object("Melanie", "monica_office_makeup_room")
    return False

label ep23_quests_melanie4: #Моника говорит с Мелани после фотосессии
    if act=="l":
        return
    $ remove_hook(label="photoshoot_melanie_exit")
    call ep23_dialogues6()
    $ replace_hook("ep23_quests_melanie4", "ep23_quests_melanie5", scene="monica_office_makeup_room")
    $ questLog(24, False)
    $ questLog(25, True)
    $ move_object("Melanie", "empty")
    call refresh_scene_fade()
    return False
label ep23_quests_melanie5: #Моника говорит с Мелани после фотосессии повтор
    if act=="l":
        return
    call ep23_dialogues6a()
    call refresh_scene_fade()
    return False

label ep23_quests_melanie6: #Мелани идет к Дику
    $ remove_hook()
    $ remove_hook(label="melanie_makeuproom_life")
    m "Дик!"
    return






















#
