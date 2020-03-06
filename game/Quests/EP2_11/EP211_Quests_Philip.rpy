label ep211_quests_philip:
    call ep211_dialogues7_Phillip_home_1()
    call ep211_dialogues7_Phillip_home_2()
    if _return == 1: #double blowjob
        call ep211_dialogues7_Phillip_home_3()
        if _return == False:
            # убегает
            $ move_object("Bitch1", "empty")
            $ autorun_to_object("ep210_dialogues2_escort_start_Phillip_18", scene="street_philiphome")
            call refresh_scene_fade_long()
            return False
        call ep211_dialogues7_Phillip_home_4()
        $ monica_philip_visits_double_blowjobs += 1
        $ move_object("Bitch1", "empty")
        $ autorun_to_object("ep211_dialogues7_Phillip_home_5", scene="street_philiphome")
        call refresh_scene_fade_long()
        return False
    return
