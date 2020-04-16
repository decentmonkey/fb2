default ep212_quests_load_init_flag = False

label ep212_quests_load_init:
    if ep212_quests_load_init_flag == False:
        if monica_college_stage == 3:
            call ep212_quests_bardie_ralph1()
        $ ep212_quests_load_init_flag = True
    return
