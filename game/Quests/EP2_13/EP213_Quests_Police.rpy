default ep213_quests_police_inited = False

default ep213_quests_police_money_stored = 0
default ep213_quests_police_inventory_stored = []

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
    if act=="l":
        return
label ep213_quests_police2_turniket:
    call ep213_dialogues_police2b()
    $ ep213_quests_police_money_stored = money
    $ money = 0
    $ ep213_quests_police_inventory_stored = inventory
    $ inventory = []
    $ add_inventory("butt_plug", 1, False)

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
