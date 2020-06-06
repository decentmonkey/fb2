default ep213_escort5_lift_talk = False
default ep213_escort5_sex_this_time = False
# сцена 5 эскорта
label ep213_escort5_1:
    call ep213_dialogues2_escort_1()
    $ move_object("Visitor2", "rich_hotel_lift")
    call ep213_dialogues2_escort_2() # Моника садится за свой столик
    $ add_objective("go_administrator", t_("Пойти на ресепшн к администратору."), c_orange, 135)
    $ add_hook("MonicaTable", "ep211_escort_scene1_17", scene="rich_hotel_restaurant", label="escort_scene5")
    $ add_hook("before_open", "ep213_escort5_2_reception", scene="rich_hotel_reception", label="escort_scene5")
    return

label ep213_escort5_2_reception:
    call ep213_dialogues2_escort_3()
    $ remove_objective("go_administrator")
    $ richHotelListVisitor2Suffix = 1
    call rich_hotel_lift_init3()
    $ move_object("Visitor2", "rich_hotel_lift")
    $ richHotelLiftSceneSuffix = ""
    $ richHotelLiftMonicaSuffix = 4
    $ add_hook("Teleport_Reception", "ep213_dialogues2_escort_5a", scene="rich_hotel_lift", label="escort_scene5")
    $ add_hook("Visitor2", "ep213_escort5_3_linda", scene="rich_hotel_lift", label="escort_scene5")
    $ add_hook("Lift", "ep213_escort5_4_lift", scene="rich_hotel_lift", label="escort_scene5")
    call change_scene("rich_hotel_lift", "Fade_long")
    $ ep213_escort5_lift_talk = False
    $ ep213_escort5_sex_this_time = False
    return

label ep213_escort5_3_linda:
    if act=="l":
        call ep213_dialogues2_escort_5b()
        return False
    call ep213_dialogues2_escort_4()
    $ ep213_escort5_lift_talk = True
    call refresh_scene_fade()
    return False

label ep213_escort5_4_lift:
    if act=="l":
        return
    $ move_object("Visitor2", "rich_hotel_restaurant")
    $ richHotelLiftSceneSuffix = "_Closed"
    $ richHotelLiftMonicaSuffix = 1
    $ remove_hook(label="escort_scene5")
    if ep213_escort5_lift_talk == False:
        call ep213_dialogues2_escort_4()
    call ep213_dialogues2_escort_5()
    if _return == -1: # увольнение
        call bitch(20, "escort5")
        call ep212_dialogues3_escort_hotel_5_1()
        $ ep212_escort_monica_fired = True
        $ ep212_escort5_monica_fired = True
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
        call ep211_quests_escort2_end_day()
        return False

    call ep213_dialogues2_escort_6()
    if _return == 0: # убежала
        pass
    if _return == -1: # увольнение
        call bitch(20, "escort5")
        call ep212_dialogues3_escort_hotel_5_1()
        $ ep212_escort_monica_fired = True
        $ ep212_escort5_monica_fired = True
        $ add_hook("Teleport_Rich_Hotel_Reception", "ep212_dialogues3_escort_hotel_7_2", scene="street_rich_hotel", priority = 500) # Блокируем вход в отель
        $ autorun_to_object("ep212_dialogues3_escort_hotel_7_1", scene="street_rich_hotel")
        call ep211_quests_escort2_end_day()
        return False
    if _return == 1: # все сделано
        $ ep213_escort5_sex_this_time = True
        $ add_corruption(25, "escort5")


    call ep213_dialogues2_escort_7()
    $ autorun_to_object("ep213_dialogues2_escort_8", scene="street_rich_hotel")
    $ add_hook("MonicaTable", "ep213_escort5_5_table_after", scene="rich_hotel_restaurant", label="escort_scene5", priority=200)
    $ ep212_escort5_completed = True
    call ep211_quests_escort2_end_day()
    return False

label ep213_escort5_5_table_after: # Над Моникой пытаются смеяться после события
    $ remove_hook()
    call ep213_dialogues2_escort_9()
    call refresh_scene_fade_long()
    return False
