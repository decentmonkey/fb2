default ep224_quests_load_init_flag = False
label ep224_quests_load_init:
    if ep224_quests_load_init_flag == True:
        return
    $ ep224_quests_load_init_flag = True
    if ep218_quests_julia_completed_last_day > 0:
        call ep224_quests_julia_init()
    if ep219_quests_photoshoot10_day > 0:
        call ep224_quests_office_init()
    if ep219_quests_linda_after_stage_day > 0 and ep218_quests_meeting2_day > 0:
        call ep224_quests_escort_init() # инитим эскорт
    return
