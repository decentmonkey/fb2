default ep215_quests_load_init_flag = False

label ep215_quests_load_init:
    if ep215_quests_load_init_flag == False:
        $ ep215_quests_load_init_flag = True
        if ep29_revenge_quest_started == True:
            call ep215_quests_revenge_fix()

    return

label ep215_quests_revenge_fix:
    if check_inventory("butt_plug",1) != False: # если есть пробка в инвентаре, убираем ее под кровать
        $ remove_inventory("butt_plug", 1, True)
        $ move_object("ButtPlug", "basement_bedroom2")
    return
