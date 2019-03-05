default pubInited = False

label ep23_quests_pub_init: #инициализация локации бара
    $ pubInited = True
#    $ hostelStreetSceneName = "scene_Hostel_Street_Pub[day_suffix]"
    $ add_hook("enter_scene", "ep23_quests_pub", scene="hostel_street")
    $ add_object_to_scene("Teleport_Hostel_Pub", {"type":3, "text" : _("SHINY HOLE"), "larrow" : "arrow_down_2_a", "base":"Hostel_Street_Pub_Teleport_Pub", "click" : "hostel_street_teleport", "xpos" : 1641, "ypos" : 471, "zorder":16, "b":0.13, "tint":[1.0, 1.0, 0.7], "teleport":True, "high_sprite_hover":True}, scene="hostel_street")
    return
label ep23_quests_pub:
    $ remove_hook()
    call ep23_dialogues1_1()
    $ add_location("pub", caption=_("SHINY HOLE"), label="pub", init_label="pub_init", parent="Street_Corner")
    call characters_pub_init()
    call Pub_Life_init()
    $ add_hook("Teleport_Hostel_Pub", "ep23_dialogues1_1a", scene="hostel_street")
    $ add_hook("enter_scene", "ep23_quests_pub1", scene="pub")
    return

label ep23_quests_pub1: #Моника заходит в бар первый раз
    $ remove_hook()
    call ep23_dialogues1_2()
    $ add_hook("Bartender", "ep23_quests_pub2", scene="pub", label="pub_dialogue")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub2", scene="pub", label="pub_dialogue")
    call refresh_scene_fade()
    return

label ep23_quests_pub2: #при клике на бармена или барменшу
    if act=="l":
        return
    $ remove_hook()
    call ep23_dialogues1_2a()
    call refresh_scene_fade()
    $ add_hook("enter_scene", "ep23_quests_pub3", scene="hostel_street")
    music2 stop
    call change_scene("hostel_street")
    return

label ep23_quests_pub3: #комментарий на улице
    $ remove_hook()
    call ep23_dialogues1_2c()
    $ remove_hook(label="pub_dialogue")
    $ add_hook("Bartender", "ep23_quests_pub4", scene="pub", label="pub_dialogue")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub4", scene="pub", label="pub_dialogue")
    return

label ep23_quests_pub4: # диалог о приеме на работу
    call ep23_dialogues1_3()
    if _return == False:
        if act != "l":
            music2 stop
            call change_scene("hostel_street")
        return False
    $ monicaWorkingAsDishwasher = True
    $ add_location("pub_bar1", caption=_("SHINY HOLE"), label="pub_bar1", init_label="pub_bar1_init", parent="pub")
    $ add_hook("Monica", "ep23_quests_pub6_dishes", scene="pub_bar1", label="pub_dishes_process")
    $ add_hook("Pub_Bar1_Washbasin", "ep23_quests_pub6_dishes", scene="pub_bar1", label="pub_dishes_process")
    $ add_hook("Bartender", "ep23_quests_pub6_dishes_bartender", scene="pub_bar1", label="pub_dishes_process")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub6_dishes_bartender_waitress", scene="pub_bar1", label="pub_dishes_process")

    $ remove_hook(label="pub_dialogue")
    $ add_hook("Bartender", "ep23_quests_pub5_dishes", scene="pub", label="pub_dishes")
    $ add_hook("Bartender_Waitress", "ep23_quests_pub5_dishes", scene="pub", label="pub_dishes")
    $ add_object_to_scene("Pub_Washbasin", {"type" : 2, "base" : "Pub_Washbasin", "click" : "pub_environment", "actions" : "lh", "zorder":0, "group":"environment"}, scene="pub")
    $ add_hook("Pub_Washbasin", "ep23_quests_pub5_dishes", scene="pub", label="pub_dishes")

    $ questLog(30, True)
    call Pub_Life2_init() # Обычное наполнение бара
    call refresh_scene_fade()
    return False


label ep23_quests_pub5_dishes: # Моника моет посуду
    if act=="l" and obj_name != "Pub_Bar1_Washbasin":
        return False
    call ep23_dialogues1_4a()
    if _return == False:
        call refresh_scene_fade()
        return False
    if monicaEatedLastDay == day:
        call ep23_dialogues1_4()
        return False
#    $ rand1 = rand(1,10)
#    if rand1 >= 7:
#        $ set_active("Bartender", False, scene="pub_bar1")
#        $ set_active("Bartender_Waitress", True, scene="pub_bar1")
#    else:
#        $ set_active("Bartender", True, scene="pub_bar1")
#        $ set_active("Bartender_Waitress", False, scene="pub_bar1")
    call change_scene("pub_bar1")
    return False

label ep23_quests_pub6_dishes: # Клик на Монику
    # Мытье посуды без приставаний
    call ep23_dialogues1_4a2()
    img 9650
    with fadelong
    call ep23_dialogues1_5()
    call monicaEat()
    call change_scene("hostel_street", "Fade_long")
    return False

label ep23_quests_pub6_dishes_bartender: # Клик на Бармена
    call ep23_dialogues1_4a2()
    call ep23_dialogues1_4b()
    call ep23_dialogues1_5()
    call monicaEat()
    call change_scene("hostel_street", "Fade_long")
    return False

label ep23_quests_pub6_dishes_bartender_waitress: # Клик на Барменшу
    call ep23_dialogues1_4a2()
    call ep23_dialogues1_4c()
    call ep23_dialogues1_5()
    call monicaEat()
    call change_scene("hostel_street", "Fade_long")
    return False



#
