default ep210_quests_load_init_flag = False

label ep210_quests_load_init:
    if ep210_quests_load_init == False:
        call ep210_quests_bardie_init()
        $ add_hook("change_time_day", "ep210_quest_everyday_check", scene="global", label="ep210_quest_everyday_check")
        $ ep210_quests_load_init = True
    return

label ep210_quest_everyday_check:
    return
