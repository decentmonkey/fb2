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
    $ add_objective("go_to_melanie", _("Идти к Мелани домой"), c_red, 30)
    return
