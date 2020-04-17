default ep212_quests_load_init_flag = False

label ep212_quests_load_init:
    if ep212_quests_load_init_flag == False:
        if monica_college_stage == 3:
            call ep212_quests_bardie_ralph1()
        $ ep212_quests_load_init_flag = True
        if ep211_julia_second_date_completed == True:
            $ add_hook("before_open", "ep212_quests_julia2_fred_catch", scene="working_office", label="ep212_quests_julia2_fred_catch", priority=1000)
            $ add_hook("before_open", "ep212_quests_julia2_fred_catch", scene="working_office_cabinet", label="ep212_quests_julia2_fred_catch", priority=1000)
        if monicaOutfitsEnabled[8] == True and ep211_quests_photoshot8_opened_day == 0:
            $ ep211_quests_photoshot8_opened_day = day
            call ep212_quests_photoshoot8_after_init()

    return
