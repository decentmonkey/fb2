default ep213_quests_biff1_inited = False
default ep213_dialogues4_biff_2_day = 0
label ep213_quests_biff1_init: # инициализация второй презентации
    call ep213_dialogues4_biff_1()
    if _return == False:
        return
    $ ep213_quests_biff1_inited = True
    $ add_hook("Biff", "ep213_quests_biff2_biff", scene="monica_office_cabinet_table", label=["monica_presentation2", "evening_time_temp"])
    $ ep213_dialogues4_biff_2_day = day
    $ add_hook("enter_scene", "ep213_dialogues4_biff_2", scene="monica_office_entrance", label="monica_presentation2")
    $ add_hook("before_open", "ep213_quests_biff3_presentation", scene="monica_office_cabinet", label="monica_presentation2")
    return

label ep213_quests_biff2_biff:
    if act=="l":
        return
    call ep213_dialogues4_biff_1b()
    return False

label ep213_quests_biff3_presentation:
    # перезентация
    call ep213_dialogues4_biff_3()
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep213_dialogues4_biff_4", scene="monica_office_secretary", label="presentation2_block")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep213_dialogues4_biff_4", scene="monica_office_secretary", label="presentation2_block")
    $ miniMapEnabledOnly = ["Office_PhotoStudio", "Office_Monica_Secretary"]
    $ add_hook("AlexPhotograph", "ep213_quests_biff4_Alex", scene="monica_office_photostudio", label="monica_presentation2")
    $ add_hook("Teleport_Monica_Office_MakeupRoom", "ep213_quests_biff5_makeup_room", scene="monica_office_photostudio", label="monica_presentation2")
    $ add_objective("go_photostudio", t_("Идти в фотостудию и провести фотосессию."), c_orange, 115)

    call change_scene("monica_office_secretary", "Fade_long")
    return False

label ep213_quests_biff4_Alex:
    if act=="l":
        return
    call ep213_dialogues4_biff_5()
    call refresh_scene_fade()
    return False

label ep213_quests_biff5_makeup_room:
    call ep213_dialogues4_biff_6()
    if _return == False:
        $ miniMapEnabledOnly = []
        $ remove_hook(label="monica_presentation2")
        $ remove_hook(label="presentation2_block")
        $ remove_objective("go_photostudio")
        $ add_hook("Biff", "ep213_quests_biff6_biff_repeat", scene="monica_office_cabinet_table", label="monica_presentation2") # Повторный разговор с Бифом о работе
        $ autorun_to_object("ep213_dialogues4_biff_13", scene="street_monica_office")
        call change_scene("street_monica_office", "Fade_long")

    # фотосессия
    call ep213_quests_photoshoot9()
    return False

label ep213_quests_biff6_biff_repeat: # Повторный разговор с Бифом о работе
    if act=="l":
        return
    call ep213_dialogues5_photoshoot_7()
    if _return == False:
        $ autorun_to_object("ep213_dialogues4_biff_13", scene="street_monica_office")
        call change_scene("street_monica_office", "Fade_long")
        return False
    $ add_hook("Teleport_Monica_Office_Cabinet", "ep213_dialogues4_biff_4", scene="monica_office_secretary", label="presentation2_block")
    $ add_hook("Teleport_Monica_Office_Entrance", "ep213_dialogues4_biff_4", scene="monica_office_secretary", label="presentation2_block")
    $ miniMapEnabledOnly = ["Office_PhotoStudio", "Office_Monica_Secretary"]
    $ add_hook("AlexPhotograph", "ep213_quests_biff4_Alex", scene="monica_office_photostudio", label="monica_presentation2")
    $ add_hook("Teleport_Monica_Office_MakeupRoom", "ep213_quests_biff5_makeup_room", scene="monica_office_photostudio", label="monica_presentation2")
    $ add_objective("go_photostudio", t_("Идти в фотостудию и провести фотосессию."), c_orange, 115)
    call change_scene("monica_office_secretary", "Fade_long")

    return False
