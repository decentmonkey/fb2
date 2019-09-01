default ep27_quests_melanie_init_flag = False
label ep27_quests_melanie1_init:
    if melanieMonicaSawFarmTattoo == True and ep27_quests_melanie_init_flag == False:
        $ remove_hook(label="melanie_returned_dialogue1")
        $ add_hook("Melanie", "ep27_quests_melanie2_dialogue", scene="monica_office_makeup_room", label="melanie_returned_dialogue2")
        $ ep27_quests_melanie_init_flag = True

    return

label ep27_quests_melanie2_dialogue: # Диалог с Мелани
    call ep27_dialogues1_melanie1()
    if _return == False:
        call refresh_scene_fade_long()
        return False
    $ remove_hook(label="melanie_returned_dialogue2")
    $ add_hook("Melanie", "ep27_dialogues1_melanie1a", scene="monica_office_makeup_room", label="melanie_returned_dialogue3")
    $ autorun_to_object("ep27_dialogues1_melanie1a", scene="monica_office_photostudio")
    $ add_hook("basement_monica_after_sleep_dialogue", "ep27_dialogues1_melanie1b", scene="global") # Диалог о Мелани после просыпания
    $ add_hook("change_time_day", "ep27_quests_melanie2_init_map", scene="global")
    call change_scene("monica_office_photostudio", "Fade_long")
    return False

label ep27_quests_melanie2_init_map: # Инициализация посещения Мелани (карта)
    $ remove_hook()
    call locations_init_melanie_home()
    $ add_objective("go_to_melanie", _("Идти к Мелани домой"), c_red, 30)
    $ map_objects["Teleport_Melanie_Home"] = {"text" : _("АПАРТАМЕНТЫ МЕЛАНИ"), "xpos" : 1726, "ypos" : 791, "base" : "map_marker", "state" : "visible"}
    $ add_hook("map_teleport", "ep27_quests_melanie4_melanie_check_whore_cloth", scene="global", priority = 2000, label="melanie_home_checkcloth")
    $ add_hook("open", "ep27_quests_melanie3_melanie_home_scene", scene="melanie_home")
    return

label ep27_quests_melanie3_melanie_home_scene:
    $ remove_hook()
    $ remove_hook(label="melanie_returned_dialogue3")
    $ remove_hook(label="melanie_home_checkcloth")
    $ add_hook("map_teleport", "ep27_dialogues1_melanie4", scene="global", priority = 2000, label="melanie_home_restrict") # Блокируем дом Мелани
    call ep27_dialogues1_melanie2()
    music stop
    img black_screen
    with diss
    pause 1.5
    $ changeDayTime("evening")
    $ autorun_to_object("ep27_dialogues1_melanie3", scene="street_house_outside") # Комментарий после встречи с Мелани
    call change_scene("street_house_outside", "Fade_long", "highheels_run2")
    return

label ep27_quests_melanie4_melanie_check_whore_cloth: # Переодеваем Монику перед приходом к Мелани
    if cloth != "Whore" and cloth_type != "Nude":
        mt "Мелани просила меня придти в другой... Одежде..."
        return False
#        menu:
#            "Переодеться в одежду шлюхи.":
#                $ cloth = "Whore" #Принудительно переодеваем Монику
#                $ cloth_type = "Whore"
    return
