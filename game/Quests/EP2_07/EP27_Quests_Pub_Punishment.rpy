default pubMonicaWaitressTipsPunishmentJoeStage = 0
default pubMonicaWaitressTipsPunishmentAshleyStage = 0

label ep22_quests_pub_punishment_joe:
    music2 stop
    call ep27_dialogues7_pub9()
    if _return == False:
        call refresh_scene_fade_long()
        return False
    music stop
    img black_screen
    with diss
    img scene_Pub_BackRoom1
    with fadelong
    call ep27_dialogues7_pub9a()
    $ sceneIdx = _return
    music stop
    call textonblack(_("Спустя некоторое время..."))
    img black_screen
    with Dissolve(1)
    if sceneIdx == 1:
        call ep27_dialogues7_pub10()
        if _return == False:
            call change_scene("hostel_street", "Fade_long")
            return False
        $ pubMonicaWaitressTipsPunishmentJoeStage = 1
        $ add_char_progress("Bartender", monicaTipsPunishmentJoeProgress, "monicaTipsPunishmentJoeProgress1")
        call ep27_quests_pub_work7_tips_punishment_forgive()
        call ep27_dialogues7_pub14()
        call refresh_scene_fade_long()
        return
    if sceneIdx == 2:
        call ep27_dialogues7_pub11()
        if _return == False:
            call change_scene("hostel_street", "Fade_long")
            return False
        $ pubMonicaWaitressTipsPunishmentJoeStage = 2
        $ add_char_progress("Bartender", monicaTipsPunishmentJoeProgress, "monicaTipsPunishmentJoeProgress2")
        call ep27_quests_pub_work7_tips_punishment_forgive()
        call ep27_dialogues7_pub14()
        call refresh_scene_fade_long()
        return
    if sceneIdx == 3:
        call ep27_dialogues7_pub12()
        if _return == False:
            call change_scene("hostel_street", "Fade_long")
            return False
        $ pubMonicaWaitressTipsPunishmentJoeStage = 3
        $ add_char_progress("Bartender", monicaTipsPunishmentJoeProgress, "monicaTipsPunishmentJoeProgress3")
        call ep27_quests_pub_work7_tips_punishment_forgive()
        call ep27_dialogues7_pub14()
        call refresh_scene_fade_long()
        return
    if sceneIdx == 4:
        call ep27_dialogues7_pub13()
        if _return == False:
            call change_scene("hostel_street", "Fade_long")
            return False
        $ pubMonicaWaitressTipsPunishmentJoeStage = 4
        $ add_char_progress("Bartender", monicaTipsPunishmentJoeProgress, "monicaTipsPunishmentJoeProgress4")
        call ep27_quests_pub_work7_tips_punishment_forgive()
        call ep27_dialogues7_pub14()
        call refresh_scene_fade_long()
        return
    return

label ep22_quests_pub_punishment_joe1:
    return

label ep22_quests_pub_punishment_ashley:
    music2 stop
    call ep27_dialogues7_pub14a()
    if _return == False:
        call refresh_scene_fade_long()
        return False
    music stop
    img black_screen
    with diss
    img scene_Pub_BackRoom1
    with fadelong
    call ep27_dialogues7_pub14b()
    $ sceneIdx = _return
    music stop
    call textonblack(_("Спустя некоторое время..."))
    img black_screen
    with Dissolve(1)
    if sceneIdx == 1:
        call ep27_dialogues7_pub15()
        if _return == False:
            call change_scene("hostel_street", "Fade_long")
            return False
        $ pubMonicaWaitressTipsPunishmentAshleyStage = 1
        $ add_char_progress("Bartender_Waitress", monicaTipsPunishmentAshleyProgress, "monicaTipsPunishmentAshleyProgress1")
        call ep27_quests_pub_work7_tips_punishment_forgive()
        call ep27_dialogues7_pub18()
        call refresh_scene_fade_long()
        return
    if sceneIdx == 2:
        call ep27_dialogues7_pub16()
        if _return == False:
            call change_scene("hostel_street", "Fade_long")
            return False
        $ pubMonicaWaitressTipsPunishmentAshleyStage = 2
        $ add_char_progress("Bartender_Waitress", monicaTipsPunishmentAshleyProgress, "monicaTipsPunishmentAshleyProgress1")
        call ep27_quests_pub_work7_tips_punishment_forgive()
        call ep27_dialogues7_pub18()
        call refresh_scene_fade_long()
        return
    if sceneIdx == 3:
        call ep27_dialogues7_pub17()
        if _return == False:
            call change_scene("hostel_street", "Fade_long")
            return False
        $ pubMonicaWaitressTipsPunishmentAshleyStage = 3
        $ add_char_progress("Bartender_Waitress", monicaTipsPunishmentAshleyProgress, "monicaTipsPunishmentAshleyProgress1")
        call ep27_quests_pub_work7_tips_punishment_forgive()
        call ep27_dialogues7_pub18()
        call refresh_scene_fade_long()
        return
    return

label ep22_quests_pub_punishment_ashley1:
    return
