default monicaPoliceCell1Suffix = 1

label police_cell1:
    $ print "enter_police_cell1"
    $ miniMapData = []

    music Jail_Clock
    music2 audio_woman_breathing_painfully

    $ scene_image = "scene_Police_Cell1"
    return

label police_cell1_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Police_Cell1_Monica_[cloth]_[monicaPoliceCell1Suffix]", "click" : "police_cell1_environment", "actions" : "l", "zorder" : 10}, scene="police_cell1")

    $ add_object_to_scene("Lamp", {"type":2, "base":"Police_Cell_1_Lamp", "click" : "police_cell1_environment", "actions" : "l", "zorder" : 0, "group":"environment"}, scene="police_cell1")
    $ add_object_to_scene("Bed", {"type":2, "base":"Police_Cell_1_Bed", "click" : "police_cell1_environment", "actions" : "lh", "zorder" : 0, "group":"environment"}, scene="police_cell1")
    $ add_object_to_scene("Sortir", {"type":2, "base":"Police_Cell_1_Sortir", "click" : "police_cell1_environment", "actions" : "lh", "zorder" : 0, "group":"environment"}, scene="police_cell1")

    $ add_object_to_scene("Teleport_Cage2", {"type":3, "text" : _("РЕШЕТКА"), "rarrow" : "arrow_right_2", "base":"empty", "click" : "police_cell1_teleport", "xpos" : 1680, "ypos" : 233, "zorder":5, "teleport":True}, scene="police_cell1")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label police_cell1_teleport:
    if obj_name == "Teleport_Cage2":
        call change_scene("police_cell2", "Fade_long")
    return

label police_cell1_environment:
    if obj_name == "Monica":
        mt "Мне надо кого-то позвать!"
        "Я не могу находиться здесь!!!"

    if obj_name == "Bed":
        if act=="l":
            mt "Жуткая кровать."
            mt "Это ужас!"
        if act=="h":
            call ep27_dialogues_marcus1_10()
            if _return == False:
                call refresh_scene_fade()
                return
            call ep27_dialogues_marcus1_11()
            return

    if obj_name == "Lamp":
        mt "Эта лампа светит ядовитым светом..."
    if obj_name == "Sortir":
        if act=="l":
            img 5088
            with fade
        mt "Какой ужас!"
        mt "О БОЖЕ!"
        call refresh_scene_fade()
        return
    if obj_data["action"] == "h":
        mt "Если честно, я не хочу подходить к ЭТОМУ..."
        mt "Если только мне совсем не захочется..."
        mt "Но, в любом случае, я буду делать это только пока никто не видит!"


    return
