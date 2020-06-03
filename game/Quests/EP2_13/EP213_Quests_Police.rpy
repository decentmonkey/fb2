default ep213_quests_police_inited = False

default ep213_quests_police_money_stored = 0
default ep213_quests_police_inventory_stored = []
default ep213_quests_police_objectives_stored = []

default ep213_quests_prisoner = False
default ep213_quests_prisoner1_offended = False

label ep213_quests_police1_check_init:
    if ep213_quests_police_inited == True:
        return True
    if day - ep28_quests_completed_day >= 7 or ep28_quests_completed_day == 0: # Если прошла неделя с посещения, либо день не был зафиксирован
        call ep213_dialogues_police1() # Если с момента прошлого посещения Маркуса прошла неделя, то Моника при клике на полицию говорит
        if _return == 0:
            return False
        if _return == 1:
            $ add_objective("take_buttplug", t_("Вернуться к полиции с анальной пробкой."), c_red, 105)
            $ remove_hook(label="police2_buttplug")
            $ add_hook("ButtPlug", "ep213_quests_police3_takeplug", scene="basement_bedroom2", label="police2_buttplug", quest="police2")
        if _return == 2:
            $ ep213_quests_police_inited = True
            call ep213_dialogues_police2()
            $ autorun_to_object("ep213_dialogues_police2a", scene="police_entrance")
            $ add_hook("Teleport_Inside", "ep213_quests_police2_turniket", scene="police_entrance", quest="police2")
            $ add_hook("Reception", "ep213_quests_police2_talk_reception", scene="police_entrance", quest="police2")
            $ remove_hook(label="marcus_block1")
            $ remove_hook(label="police_quest1")
            $ add_hook("Building", "ep213_quests_police4_enter_police", scene="street_police", quest="police2")
            call change_scene("police_entrance", "Fade_long")
            return False

        return False

    return True


label ep213_quests_police2_talk_reception:
label ep213_quests_police2_turniket:
    call ep213_dialogues_police2b()
    $ remove_objective("take_buttplug")
    $ ep213_quests_police_money_stored = money
    $ money = 0
    $ ep213_quests_police_inventory_stored = inventory
    $ inventory = []
    $ add_inventory("butt_plug", 1, False)
    $ ep213_quests_police_objectives_stored = objectives_list
    $ objectives_list = []
    $ add_objective("freedom", t_("Избежать наказания"), c_red, 0)

    fadeblack
    pause 2.0
    $ cloth = "NudePlug"
    $ cloth_type = "Nude"
    $ add_hook("Monica", "ep213_dialogues_police3", scene="police_cell1", label="police_day1", quest="police2")
    $ add_hook("Teleport_Cage2", "ep213_dialogues_police4", scene="police_cell1", label="police_day1", quest="police2")
    $ add_hook("Sortir", "ep213_dialogues_police5", scene="police_cell1", label="police_day1_sortir", quest="police2")
    $ add_hook("Bed", "ep213_quests_police5_day1_bed", scene="police_cell1", label="police_day1", quest="police2")
    $ police_cell1_monica_breath = False
    $ monicaPoliceCellSuffixMode = 1
    $ monicaPoliceCell1Suffix = 1
    $ monicaPoliceCell2Suffix = 1
    call change_scene("police_cell1", "Fade_long", False)

    return False

label ep213_quests_police3_takeplug: # взять пробку
    if act=="l":
        return
    $ remove_hook()
    $ set_active("ButtPlug", False)
    fadeblack
    pause 1.0
    sound chpok2
    pause 1.5
    $ add_inventory("butt_plug", 1, True)
    call refresh_scene_fade()
    return False

label ep213_quests_police4_enter_police:
    if act=="l":
        return
    call change_scene("police_entrance", "Fade_long")
    return False

label ep213_quests_police5_day1_bed:
    if act=="l":
        return
    $ remove_hook(label="police_day1")
    call ep213_dialogues_police7()
    call police_cell1_init2()
    call police_cell2_init2()
    $ ep213_quests_prisoner = _return
    if _return == True:
        $ police_cell1_monica_breath = True
        $ add_hook("Prisoner1", "ep213_quests_police6_prisoner1_regular", scene="police_cell1", label="police_prisoner1_regular", quest="police2")
        $ add_hook("Prisoner1", "ep213_quests_police6_prisoner1_regular", scene="police_cell2", label="police_prisoner1_regular", quest="police2")
        $ add_hook("Prisoner1", "ep213_quests_police7_day1_action1", scene="police_cell2", label="police_day1", quest="police2")
        $ monicaPoliceCell1Suffix = 1
        $ prisoner1Cell1Suffix = 2
    else:
        $ monicaPoliceCell1Suffix = 2
    $ cloth = "Jail_Cloth3"
    $ add_hook("Sortir", "ep213_dialogues_police14", scene="police_cell1", label="police_day1_sortir", quest="police2")
    $ add_hook("Bed", "ep213_quests_police7_day1_bed2", scene="police_cell1", label="police_day1", quest="police2")
    call refresh_scene_fade()
    return False

label ep213_quests_police6_prisoner1_regular:
    if ep213_quests_prisoner1_offended == False:
        call ep213_dialogues_police15()
    else:
        call ep213_dialogues_police16()
    return False

label ep213_quests_police7_day1_bed2:
    if act=="l":
        return
    call ep27_dialogues_marcus1_10()
    if _return == True:
        jump ep213_quests_police7_day1_action1
    return False

label ep213_quests_police7_day1_action1:
    if act=="l":
        return
    if ep213_quests_prisoner == True:
        call ep213_dialogues_police8()
        call refresh_scene_fade()

    music2 stop
    fadeblack
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(t_("День 2"))
    img black_screen
    with Dissolve(2.0)

    $ remove_hook(label="police_day1")

    #### ДЕНЬ 2
    if ep213_quests_prisoner == True and ep213_quests_prisoner1_offended == False:
        call ep213_dialogues_police9()
    else:
        call ep213_dialogues_police9a()

    call refresh_scene_fade()
    return False
















#
