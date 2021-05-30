default ep225_quests_rayan1_init_flag = False
default ep225_quests_rayan_visit_day = 0
default ep225_quests_rayan_completed_day = 0

label ep225_quests_rayan1_init:
    if ep225_quests_rayan1_init_flag == True:
        return
    $ ep225_quests_rayan1_init_flag = True
    $ questHelp("office_62")
    $ add_hook("office_work_process", "ep225_quests_rayan2", scene="global", label="ep225_quests_rayan2", priority=2)

    return

label ep225_quests_rayan2:
    $ remove_hook()
    call ep22_5_dialogues4_rayan_1()
    $ map_objects["Teleport_Rayan_Studio"] = {"text" : t_("СТУДИЯ РАЙАНА"), "xpos" : 1361, "ypos" : 926, "base" : "map_marker", "state" : "visible"}
    $ add_hook("enter_scene", "ep225_quests_rayan3", scene="street_monica_office", label="ep225_quests_rayan3")
    $ questHelp("office_62", True)
    $ questHelp("office_63")
    return

label ep225_quests_rayan3:
    $ remove_hook()
    call ep22_5_dialogues4_rayan_1a()
    if _return == True:
        $ focus_map("Teleport_Rayan_Studio", "ep22_5_dialogues4_rayan_1b")
        $ hudDaySkipToEveningEnabled = False
        call map_show()

    $ add_hook("Teleport_Rayan_Studio", "ep22_5_dialogues4_rayan_1c", scene="map", label="ep22_5_dialogues4_rayan_1c")
    $ add_hook("Teleport_Rayan_Studio", "ep225_quests_rayan4", scene="map", label="ep225_quests_rayan4")
    return

label ep225_quests_rayan4:
    if day_time != "evening":
        $ changeDayTime("evening")
    $ ep225_quests_rayan_visit_day = day
    $ hudDaySkipToEveningEnabled = True
    $ unfocus_map()
    call map_close()
    if cloth != "CasualDress1":
        sound snd_fabric1
        fadeblack 2.0
        $ cloth = "CasualDress1"
        $ cloth_type = "CasualDress"
    call ep22_5_dialogues4_rayan_3()
    if _return == False:
        $ questHelp("office_63", False)
        $ add_hook("enter_scene", "ep225_quests_rayan5", scene="street_monica_office", label="ep225_quests_rayan5")
        $ autorun_to_object("ep22_5_dialogues4_rayan_5", scene="street_house_outside")
    else:
        $ questHelp("office_63", True)
        $ ep225_quests_rayan_completed_day = day
        $ remove_hook(label="ep225_quests_rayan5")
        $ remove_hook(label="ep225_quests_rayan4")
        $ autorun_to_object("ep22_5_dialogues4_rayan_6", scene="street_house_outside")
    fadeblack 2.0
    call process_change_map_location("House")
    call change_scene("street_house_outside", "Fade_long")
    return False

label ep225_quests_rayan5:
    if day > ep225_quests_rayan_visit_day and day_time == "evening":
        $ remove_hook()
        call ep22_5_dialogues4_rayan_4()
    return
