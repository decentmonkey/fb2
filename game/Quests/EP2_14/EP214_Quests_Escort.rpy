label ep214_quests_escort1:
    call ep214_dialogues3_escort_1()
    if _return == False:
        call refresh_scene_fade()
        return False
    call ep214_dialogues3_escort_2()
    if _return == False: # увольнение
        call bitch(20, "escort4")
        call ep212_dialogues3_escort_hotel_5_1()
        $ ep212_escort_monica_fired = True
        $ ep212_escort5_monica_fired = True
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
        call ep211_quests_escort2_end_day()
        return False
    call ep214_dialogues3_escort_3()
    if _return == -1: # увольнение
        call bitch(20, "escort4")
        call ep212_dialogues3_escort_hotel_5_1()
        $ ep212_escort_monica_fired = True
        $ ep212_escort5_monica_fired = True
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
        call ep211_quests_escort2_end_day()
        return False
    if _return == -2: # увольнение, укусила
        call bitch(20, "escort4")
        call ep214_dialogues3_escort_4()
        $ ep212_escort_monica_fired = True
        $ ep212_escort5_monica_fired = True
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
        call ep211_quests_escort2_end_day()
        return False
    # Моника все сделала
    call ep214_dialogues3_escort_5()
    $ add_corruption(25, "escort4")
    $ autorun_to_object("ep211_escort_scene2_15", scene="street_rich_hotel")
    call ep211_quests_escort2_end_day()
    return False
