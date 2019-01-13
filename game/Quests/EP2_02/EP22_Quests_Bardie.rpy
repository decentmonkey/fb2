default EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day = 0

label EP22_Quests_Bardie_Monica_Rest_After_Cleaning:
    #Предложение отдыха после уборки
    if bardieBlackmailStage < 4:
        call ep22_dialogues3_1()
    if bardieBlackmailStage == 4:
        call ep22_dialogues3_8()

    $ remove_hook(label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
    if bardieBlackmailStage == 0:
        sound highheels_short_walk
        music Groove2_85 high
        call bardie_comment4()
        if bardieHeardAboutMarcus == True:
            # Барди будет ждать внизу
            $ EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day = day
            call EP22_Quests_Bardie_Monica_Blackmail_Stage2_init()

        $ remove_hook(label="bardie_catch_monica_at_stairs_onetime")
        $ autorun_to_object("EP22_Quests_Bardie_Monica_Rest_After_Cleaning_comment1", scene="basement_bedroom2")
        call change_scene("basement_bedroom2")
        return
    if bardieBlackmailStage == 1:
        call change_scene("basement_bedroom2")
        call EP22_Quests_Bardie1()
        return
    if bardieBlackmailStage == 2:
        call change_scene("basement_bedroom2")
        call EP22_Quests_Bardie1()
        return
    if bardieBlackmailStage == 4:
        call change_scene("basement_bedroom2")
        call EP22_Quests_Bardie5()
        return

#    m "Передых"
    return

label EP22_Quests_Bardie_Monica_Blackmail_Stage2_init:
    $ bardieBlackmailStage = 1
    $ add_hook("monica_cleaning_end", "EP22_Quests_Bardie_Monica_Rest_After_Cleaning", scene="global", label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
    call Bardie_Life_day2_init()
    $ bardieFollowMonicaDuringCleaning = False
    $ add_hook("before_open", "EP22_Quests_Bardie1", scene="basement_bedroom2", label="bardie_blackmail_basement")
    return

label EP22_Quests_Bardie_Monica_Rest_After_Cleaning_comment1:
    mt "Барди..."
    mt "Он вертится вокруг как назойливая муха!"
    mt "Надо как-то избавиться от него..."
    return

label EP22_Quests_Bardie1:
    if EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day == day:
        return
    #Барди слышал о Маркусе и идет вниз шантажировать Монику (на следующий день)
    if cloth == "Governess":
        if bardieBlackmailStage == 1:
            $ EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day = day
#            $ remove_hook()
            $ remove_hook(label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
            call ep22_dialogues3_2()
            $ add_hook("basement_monica_after_sleep", "EP22_Quests_Bardie2", scene="global") # Ночью будет сон
            $ add_hook("open", "EP22_Quests_Bardie3", scene="police_entrance") # Днем Барди в полиции
            call refresh_scene_fade()
        if bardieBlackmailStage == 2:
            $ remove_hook()
            $ remove_hook(label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
            call EP22_Quests_Bardie4()
            call refresh_scene_fade()
    return

label EP22_Quests_Bardie2: #сон
    $ remove_hook()
    #сон
    call ep22_dialogues3_3()
#    $ unfocus_map()
    $ focus_map("Teleport_Police", "ep22_dialogues3_3a")
    $ add_hook("basement_monica_before_nap", "ep22_dialogues3_3b", scene="global", label="hurry_to_police")
    $ EP22_Quests_Bardie_Monica_Blackmail_Stage2_init_day = day
    return

label EP22_Quests_Bardie3: #разговор в полиции
    $ remove_hook()
    $ remove_hook(label="hurry_to_police")
    call ep22_dialogues3_4()
    $ autorun_to_object("ep22_dialogues3_5", scene="street_police")
    $ unfocus_map()
    call change_scene("street_police")
    $ bardieBlackmailStage = 2
    $ add_hook("monica_cleaning_end", "EP22_Quests_Bardie_Monica_Rest_After_Cleaning", scene="global", label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
    return

label EP22_Quests_Bardie4: #второй разговор с Барди
    call ep22_dialogues3_6()
    $ remove_hook("Bardie_Life_day", "Bardie_Life_day3", scene="global")
    $ remove_hook("Bardie_Life_evening", "Bardie_Life_evening2", scene="global")
    $ remove_hook("Bardie_Life_evening", "Bardie_Life_evening3", scene="global")
    $ bardieFollowMonicaDuringCleaning = True
    $ bardieBlackmailStage = 3
    $ questLog(0, False)
    $ questLog(1, True)
    $ char_info["Bardie"]["caption"] = _("Барди имеет полный доступ к трусикам Моники.")
    $ basement_bedroom2_MonicaSuffix = 2
    $ add_hook("Bardie", "bardie_comment5a", scene="bedroom_bardie")
    $ autorun_to_object("ep22_dialogues3_7", scene="basement_bedroom2")
    return

label EP22_Quests_Bardie4_check_progress:
    if char_info["Bardie"]["level"] == 3 and bardieBlackmailStage == 3:
        $ bardieBlackmailStage = 4
        $ add_hook("monica_cleaning_end", "EP22_Quests_Bardie_Monica_Rest_After_Cleaning", scene="global", label="EP22_Quests_Bardie_Monica_Rest_After_Cleaning")
    return


label EP22_Quests_Bardie5: #третий разговор с Барди (трусики Бетти)
    call ep22_dialogues3_9()
    $ monicaMustWearBettyPanties = True
    $ miniMapHousePreset = "laundry"
    $ basement_bedroom2_MonicaSuffix = 2
    $ autorun_to_object("ep22_dialogues3_10", scene="basement_bedroom2")
    $ autorun_to_object("ep22_dialogues3_11", scene="basement_laundry")
    $ autorun_to_object("ep22_dialogues3_11a", scene="bedroom1")
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Basement_Laundry1_Monica_[cloth]", "click" : "ep22_dialogues3_11", "actions" : "l", "zorder":10, "tint": monica_tint}, scene="basement_laundry")
    $ add_object_to_scene("Panties_Box", {"type":2, "base":"Basement_Laundry1_Panties_Box", "click" : "EP22_Quests_Bardie6_panties_box", "actions" : "lh", "zorder" : 0, "group":"environment", "active":True}, scene="basement_laundry")
    $ questLog(1, False)
    $ questLog(2, True)
    call basement_bedroom1_init()
    call basement_bedroom2_init()
    return

label EP22_Quests_Bardie6_panties_box:
    if act == "l":
        call ep22_dialogues3_11()
        return
    $ store_music()
    music Hidden_Agenda
    call ep22_dialogues3_12() #какие трусики мне надеть?
    show screen screen_betty_panties_select()
    with Dissolve(0.2)
    $ result = ui.interact()
    if result == 6:
        $ monicaBettyPanties = False
        $ monicaBettyPantiesId = 1
    else:
        $ monicaBettyPanties = True
        $ monicaBettyPantiesId = result

    hide screen screen_betty_panties_select
    call ep22_Act_Images_monica_put_up_panties()
    $ restore_music()
    call refresh_scene_fade()
    return
