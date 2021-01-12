default ep218_quests_load_init_flag = False

label ep218_quests_load_init:
    if ep218_quests_load_init_flag == False:
        $ ep218_quests_load_init_flag = True
        if ep217_quests_betty_visit3_completed_day > 0:
            call ep218_quests_betty_init()
    return
