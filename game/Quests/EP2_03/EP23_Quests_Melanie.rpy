default monicaMelanieCastingPlanned = False
default monicaMelanieWentToDick = False
default melanieDisappeared = False
default melanieDisappearedDay = 0
default monicaMelanieCastingCummed = False
default monicaMelanieCastingLickedDildo = False
default monicaMelanieCastingLickedPussies = False

label ep23_quests_melanie1: # Моника подходит первый раз попросить о помощи
    call ep23_dialogues5_2() from _call_ep23_dialogues5_2
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_95
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
    call questLog_init() from _call_questLog_init_2
    $ questLog(13, False)
    $ questLog(24, True)

    call refresh_scene_fade() from _call_refresh_scene_fade_96
    return

label ep23_quests_melanie2: #Если Моника подходит к Мелани после этого, то Мелани отвечает когда будет фотосессия.
    if act=="l":
        return
    call ep23_dialogues5_2a() from _call_ep23_dialogues5_2a
    call refresh_scene_fade() from _call_refresh_scene_fade_97
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
    call ep23_dialogues6() from _call_ep23_dialogues6
    $ replace_hook("ep23_quests_melanie4", "ep23_quests_melanie5", scene="monica_office_makeup_room")
    $ questLog(24, False)
    $ questLog(25, True)
    $ move_object("Melanie", "empty")
    call refresh_scene_fade() from _call_refresh_scene_fade_98
    return False
label ep23_quests_melanie5: #Моника говорит с Мелани после фотосессии повтор
    if act=="l":
        return
    call ep23_dialogues6a() from _call_ep23_dialogues6a
    call refresh_scene_fade() from _call_refresh_scene_fade_99
    return False

label ep23_quests_melanie6: #Мелани идет к Дику
    $ remove_hook()
    $ remove_hook(label="melanie_makeuproom_life")
    call ep23_dialogues6_1() from _call_ep23_dialogues6_1
    sound snd_lift
    scene black_screen
    with Dissolve(1)
    music m80s_Things
    scene black_screen
    with Dissolve(1)

    call ep23_dialogues6_2() from _call_ep23_dialogues6_2
    call ep23_dialogues7() from _call_ep23_dialogues7

    # Мелани днем в гримерке
    $ add_hook("Melanie", "ep23_quests_melanie7", scene="monica_office_makeup_room")
    $ add_hook("Melanie_Life_day", "Melanie_Life_day2", scene="global", label="melanie_makeuproom_life")

    return

label ep23_quests_melanie7: #Разговор с Мелани после Дика
    if act=="l":
        return
    $ remove_hook()
    call ep23_dialogues8_2() from _call_ep23_dialogues8_2
    call refresh_scene_fade() from _call_refresh_scene_fade_100
    $ add_hook("Melanie", "ep23_quests_melanie8", scene="monica_office_makeup_room", label="melanie_talk_repeat1")
    $ add_hook("change_time_day", "ep23_quests_melanie9", scene="global")
    $ questLog(25, False)
    $ questLog(26, True)

    return False

label ep23_quests_melanie8 : #Разговор с Мелани после Дика повтор
    if act=="l":
        return
    call ep23_dialogues8_2a from _call_ep23_dialogues8_2a
    return False

label ep23_quests_melanie9: # Комментарий Моники с утра
    $ remove_hook()
    call ep23_dialogues8_3() from _call_ep23_dialogues8_3
    $ remove_hook(label="melanie_talk_repeat1")
    $ add_hook("Melanie_Life_evening", "Melanie_Life_evening2", scene="global", label="melanie_makeuproom_life") # Вечером Мелани тоже в гримерке
    $ add_hook("Melanie", "ep23_quests_melanie10", scene="monica_office_makeup_room", label="melanie_talk_repeat1")
    return

label ep23_quests_melanie10:
    if act=="l":
        return
    call ep23_dialogues8_4() from _call_ep23_dialogues8_4
    if _return == False:
        call refresh_scene_fade() from _call_refresh_scene_fade_101
        return False
    $ remove_hook()
    if monicaMelanieCastingPlanned == False: #Мелани помогает без кастинга
        $ remove_hook(label="melanie_makeuproom_life")
        $ questLog(26, False)
        $ questLog(28, True)
        call ep23_quests_melanie_disappeared() from _call_ep23_quests_melanie_disappeared
        call refresh_scene_fade() from _call_refresh_scene_fade_102
        return False

    $ questLog(26, False)
    $ questLog(29, True)
    $ move_object("Melanie", "empty")
    $ add_hook("map_teleport", "ep23_quests_melanie11", scene="global")
    $ remove_hook("Melanie_Life_evening", "Melanie_Life_evening2", scene="global") # Вечером Мелани больше нет
    call refresh_scene_fade() from _call_refresh_scene_fade_103
    return False


label ep23_quests_melanie_disappeared: # Мелани пропала
    $ move_object("Melanie", "empty")
    $ add_hook("Melanie_Life_day", "Melanie_Life_disappeared", scene="global", label="melanie_disappeared_life") # Мелани нет
    $ add_hook("Melanie_Life_evening", "Melanie_Life_disappeared", scene="global", label="melanie_disappeared_life") # Мелани нет
    $ day1 = day+2
    $ add_hook("change_time_day", "ep23_quests_melanie_disappeared2", scene="global")
    $ melanieDisappearedDay = day
#    $ add_hook_day("ep23_quests_melanie_disappeared2", day = day1)
    return

label ep23_quests_melanie_disappeared2:
    if day - melanieDisappearedDay >= 2:
        $ remove_hook()
        $ questLog(28, False)
        $ questLog(29, False)
        $ questLog(27, True)
        $ melanieDisappeared = True
        $ add_hook("basement_monica_after_sleep_dialogue", "ep23_quests_melanie_disappeared2_comment_morning", scene="global")
    return

label ep23_quests_melanie_disappeared2_comment_morning:
    $ remove_hook()
    call ep23_dialogue9_5d() from _call_ep23_dialogue9_5d
    return

label ep23_quests_melanie11: # Мелани говорит с мартышкой
    if day_time == "day" and obj_name == "Teleport_Monica_Office":
        $ remove_hook()
        call ep23_dialogue9_1() from _call_ep23_dialogue9_1
        $ add_hook("Melanie", "ep23_quests_melanie12", scene="monica_office_makeup_room")
        return

    return

label ep23_quests_melanie12: # Диалог с Мелани перед кастингом и сам кастинг
    if act=="l":
        return
    call ep23_dialogue9_2() from _call_ep23_dialogue9_2
    if _return == False:
        call change_scene("street_monica_office", "Fade_long", "highheels_run2") from _call_change_scene_243
        return False
    $ remove_hook()
    $ add_hook("Teleport_Monica_Office_Entrance", "ep23_dialogue9_3", scene="monica_office_secretary", label="melanie_exit", priority = 101) #Блокируем выход
    $ add_hook("Melanie", "ep23_quests_melanie13", scene="monica_office_makeup_room")
    $ questLog(29, False)
    call change_scene("monica_office_secretary") from _call_change_scene_244
#    call refresh_scene_fade()
    return

label ep23_quests_melanie13: # Диалог с Мелани после кастинга
    if act=="l":
        return
    call ep23_dialogue9_4() from _call_ep23_dialogue9_4
    $ questLog(28, True)
    call ep23_quests_melanie_disappeared() from _call_ep23_quests_melanie_disappeared_1
    $ remove_hook(label="melanie_exit")
    call refresh_scene_fade() from _call_refresh_scene_fade_104
    return







#
