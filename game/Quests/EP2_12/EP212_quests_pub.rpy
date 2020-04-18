default pubPrivate1Count = 0

label ep212_quests_pub_menu_private: # Меню приватов
    call ep212_dialogues2_shiny_hole_menu_private()
    if _return == -1: # Танцев не выбрано
#        $ dancePrivateLastDay = day
        return
    if _return == 0: # Танец для Мистера Беркельбауха.
        call ep211_dialogues5_shiny_hole_1()
        if _return == False:
            call ep211_quests_pub3_fired()
            return False
        call ep211_dialogues5_shiny_hole_2()
        if _return == False:
            call ep211_quests_pub3_fired()
            return False
        $ autorun_to_object("ep211_dialogues5_shiny_hole_9", scene="pub_makeuproom")
        call refresh_scene_fade_long()
        return
    if _return == 1: # Приват1
        call ep212_dialogues2_shiny_hole_1()
        if _return == False:
            return
        $ add_objective("go_dance_private", t_("Идти в подсобку барменов и станцевать приват."), c_orange, 105)
        $ add_hook("Teleport_Pub", "ep212_quests_pub_private1_1", scene="pub_makeuproom", label="pub_private_dance1", priority = 10001)
        return
    return

label ep212_quests_pub_private1_1: # Приват 1
    if cloth_type != "StripOutfit":
        call ep211_dialogues5_shiny_hole_8()
        return False
    # сцена
    $ remove_objective("go_dance_private")
    $ remove_hook(label="pub_private_dance1")
    $ pubPrivate1Count += 1
    $ dancePrivateLastDay = day
    call ep212_dialogues2_shiny_hole_2()
    if _return == -1:
        call refresh_scene_fade_long()
        return

    $ customer3_after_private = True
    call refresh_scene_fade_long()
    return
