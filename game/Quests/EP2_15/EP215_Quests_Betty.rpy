default ep215_quests_betty_stage = 0
default ep215_quests_betty_refused = False
default ep215_quests_betty_visit1_day = 0
default ep215_quests_betty_visit2_day = 0

label ep215_quests_betty_check:
    if monicaBettyRalphSeduction4 == True and ep215_quests_betty_stage == 0:
        # Моника замечает соседа
        call ep215_dialogues2_betty_1()
        $ ep215_quests_betty_stage = 1
        # на следующий день Бетти идет к соседу
        $ add_hook("change_time_day", "ep215_quests_betty1_init1", scene="global", label="ep215_quests_betty1_init1")
        return

    return

label ep215_quests_betty1_init1:
    $ remove_hook()
    # Сосед приходит к Бетти
    call ep215_dialogues2_betty_2()
    call ep215_dialogues2_betty_3()
    if _return == False:
        $ ep215_quests_betty_refused = True
        return
    call ep215_dialogues2_betty_4()

    # инициализируем дом соседа с Бетти
    call locations_init_house_neighbour()
    call street_house_outside_init3()
    $ street_house_neighbour_betty_suffix = 1
    $ street_house_outside_betty_suffix = 1
    $ street_house_neighbour_neighbour_suffix = 1
    $ set_active("Betty", True, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Neighbour", True, "street_house_outside")
    $ set_active("Betty", True, scene="street_house_neighbour")
    $ set_active("Neighbour", True, scene="street_house_neighbour")
    $ add_hook("Betty", "ep215_dialogues2_betty_8", scene="street_house_outside", label="betty_neighbour", owner="Betty")
    $ add_hook("Teleport_House_Outside_Neighbour", "ep215_quests_betty1_teleport_neighbour", scene="street_house_outside", label="betty_neighbour", owner="Betty")

    $ add_hook("Betty", "ep215_dialogues2_betty_8", scene="street_house_neighbour", label="betty_neighbour", owner="Betty")
    $ add_hook("Neighbour", "ep215_dialogues2_betty_8", scene="street_house_neighbour", label="betty_neighbour", owner="Betty")
    $ add_hook("Teleport_House_Neighbour_Farm", "ep215_dialogues2_betty_9", scene="street_house_neighbour", label="betty_neighbour", owner="Betty")
    $ add_hook("Teleport_House_Outside", "street_house_neighbour_teleport", scene="street_house_neighbour", label="betty_neighbour", owner="Betty")
    $ set_active("Door", False, scene="street_house_neighbour")
    $ add_hook("Neighbour", "ep215_quests_betty2_talk_neighbour", scene="street_house_neighbour", label="ep215_quests_betty2_talk_neighbour", owner="Betty")

    call change_owner("Betty")
    $ map_objects = {
            "Teleport_House" : {"text" : t_("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active", "owner":"Betty"}
    }
    $ miniMapEnabledOnly = ["none"]
    $ hudDaySkipToEveningEnabled = False
    call change_scene("street_house_outside", "Fade_long")

    return

label ep215_quests_betty1_teleport_neighbour:
    call change_scene("street_house_neighbour", "Fade_long")
    return

label ep215_quests_betty2_talk_neighbour:
    if act=="l":
        return
    $ remove_hook()
    call ep215_dialogues2_betty_5()
    if _return == False:
        $ ep215_quests_betty_refused = True
    else:
        # планируем второй приход
        $ add_hook("change_time_day", "ep215_quests_betty3_init", scene="global", label="ep215_quests_betty1_init1")

    $ ep215_quests_betty_visit1_day = day
    call change_owner("Monica")
    $ set_active("Teleport_House_Outside_Neighbour", False, "street_house_outside")
    $ miniMapEnabledOnly = []
    $ hudDaySkipToEveningEnabled = True
    fadeblack 2.0
    return False

label ep215_quests_betty3_init:
    $ remove_hook()
    # второй приход к соседу
    $ street_house_neighbour_betty_suffix = 2
    $ street_house_outside_betty_suffix = 2
    $ set_active("Betty", True, scene="street_house_outside")
    $ set_active("Teleport_House_Outside_Neighbour", True, "street_house_outside")
    $ set_active("Betty", True, scene="street_house_neighbour")
    $ set_active("Neighbour", False, scene="street_house_neighbour")
    $ set_active("Door", True, scene="street_house_neighbour")
    $ add_hook("Door", "ep215_quests_betty2_talk_neighbour", scene="street_house_neighbour", label="ep215_quests_betty2_talk_neighbour", owner="Betty")

    return

label ep215_quests_betty3_enter_door:
    if act=="l":
        call ep215_dialogues2_betty_8()
        return False
    # второй приход к соседу
    $ ep215_quests_betty_visit2_day = day
    call 

    return False
