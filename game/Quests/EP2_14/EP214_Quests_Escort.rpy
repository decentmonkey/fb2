default ep214_dialogues3_escort_10_flag1 = False
default ep214_dialogues3_escort_10_flag2 = False
default ep214_dialogues3_escort_6b_flag = False

label ep214_quests_escort1:
    call ep214_dialogues3_escort_1()
    if _return == False:
        call refresh_scene_fade()
        return False
    call ep214_dialogues3_escort_2()
    if _return == False: # увольнение
        call bitch(20, "escort4")
#        call ep212_dialogues3_escort_hotel_5_1()
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


label ep214_quests_escort2:
    # сцена с местью
    call ep214_dialogues3_escort_6()
    if _return == False:
        return False
    $ ep214_dialogues3_escort_6b_flag = False
    $ richHotelLiftSceneSuffix = ""
    $ move_object("EscortCustomer1", "rich_hotel_lift")
    $ richHotelLiftMonicaSuffix = 2
    $ set_active("Teleport_Reception", False, scene="rich_hotel_lift")
    $ add_hook("EscortCustomer1", "ep214_dialogues3_escort_6b", scene="rich_hotel_lift", label="escort6")
    $ add_hook("Monica", "ep214_dialogues3_escort_6b", scene="rich_hotel_lift", label="escort6")
    $ add_hook("Lift", "ep214_quests_escort2b", scene="rich_hotel_lift", label="escort6")
    call change_scene("rich_hotel_lift", "Fade_long", "snd_lift")
    return True


label ep214_quests_escort2b:
    if act=="l":
        return
    if ep214_dialogues3_escort_6b_flag == False:
        call ep214_dialogues3_escort_6b()
    $ remove_hook(label="escort6")
    $ richHotelLiftSceneSuffix = "_Closed"
    $ richHotelLiftMonicaSuffix = 1
    $ move_object("EscortCustomer1", "empty")
    $ set_active("Teleport_Reception", True, scene="rich_hotel_lift")
    sound snd_lift
    call ep214_dialogues3_escort_7()
    if _return == False:
        $ autorun_to_object("ep214_dialogues3_escort_9", scene="street_rich_hotel")
        $ add_money(100.0)
        call ep211_quests_escort2_end_day()
        return True
    call bitch(15, "escort6")
    $ autorun_to_object("ep214_dialogues3_escort_8", scene="street_rich_hotel")
    $ ep214_dialogues3_escort_10_flag1 = True
    $ ep214_dialogues3_escort_10_flag2 = True
    call ep211_quests_escort2_end_day()
    $ add_money(300.0)
    return False

















#
