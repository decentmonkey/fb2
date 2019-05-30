default monicaSellingDressInProgress = False
default monicaSellingDressDays = 0
default monicaSellingDressRefuseLastDay = 0
default shopVisitorStage1 = 1
default shopVisitorStage2 = 1
default shopVisitorStage3 = 1
default shopVisitorStage4 = 1
default shopVisitorStage5 = 1
default shopVisitorStage6 = 1
default shopVisitorStage7 = 1
default shopVisitorStage8 = 1
default shopVisitorStage9 = 1
default shopVisitorStage10 = 1

label ep25_quests_shop_visitors1:
    if act=="l":
        mt "Какой-то фрик... Может он купит это платье?"
        return False
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage1 == 1:
        call cit1_dialog_1()
        $ shopVisitorStage1 = 2
        $ set_active("Shop_Visitor1", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage1 == 2: #?????
        $ store_music()
        call cit1_dialog_2()
        $ shopVisitorStage1 = 3
        $ restore_music()
        $ set_active("Shop_Visitor1", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    return

label ep25_quests_shop_visitors2:
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage2 == 1:
        call cit2_dialog_1()
        if _return != False:
            $ shopVisitorStage2 = 2
        $ set_active("Shop_Visitor2", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        sound highheels_short_walk
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage2 == 2:
        $ store_music()
        call cit2_dialog_2()
        if _return != False:
            $ shopVisitorStage2 = 3
        $ restore_music()
        $ set_active("Shop_Visitor2", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        sound highheels_short_walk
        call refresh_scene_fade_long()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage2 == 3:
        $ store_music()
        call cit2_dialog_3()
        if _return != False:
            $ shopVisitorsList.remove("Shop_Visitor2")
        $ restore_music()
        $ set_active("Shop_Visitor2", False)
        $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        sound highheels_short_walk
        call refresh_scene_fade_long()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    return
label ep25_quests_shop_visitors3:
    if act=="l":
        mt "Очередной ненормальный..."
        return False
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage3 == 1:
        $ store_music()
        call cit3_dialog_1()
        if _return != False:
            $ shopVisitorStage3 = 2
        $ restore_music()
        $ set_active("Shop_Visitor3", False)
        $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_view2")
        sound highheels_short_walk
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage3 == 2:
        $ store_music()
        call cit3_dialog_2()
        if _return != False:
            $ shopVisitorStage3 = 3
            $ autorun_to_object("ep25_dialogues1_shop15", scene="cloth_shop_view2")
            $ shopVisitorsList.remove("Shop_Visitor3")
        else:
            $ autorun_to_object("ep25_dialogues1_shop23", scene="cloth_shop_view1")
        $ restore_music()
        $ set_active("Shop_Visitor3", False)
        sound highheels_short_walk
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    return
label ep25_quests_shop_visitors4:
    if act=="l":
        mt "Какая-то рыжеволосая стерва. Отвратительный цвет волос, Фи!"
        return False
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage4 == 1:
        call cit4_dialog_1()
        $ shopVisitorStage4 = 2
        $ set_active("Shop_Visitor4", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage4 == 2:
        $ store_music()
        call cit4_dialog_2()
        if _return != False:
            $ shopVisitorStage4 = 3
        $ restore_music()
        $ set_active("Shop_Visitor4", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False


    return
label ep25_quests_shop_visitors5:
    if act=="l":
        mt "Какая-то малявка. Что она делает в магазине? У нее есть вообще деньги?"
        return False
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage5 == 1:
        call cit5_dialog_1()
        $ shopVisitorStage5 = 2
        $ set_active("Shop_Visitor5", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage5 == 2:
        call cit5_dialog_2()
        $ shopVisitorStage5 = 3
        $ set_active("Shop_Visitor5", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage5 == 3:
        $ store_music()
        call cit5_dialog_3()
        if _return != False:
            $ shopVisitorsList.remove("Shop_Visitor5")
        $ restore_music()
        $ set_active("Shop_Visitor5", False)
        $ autorun_to_object("ep25_dialogues1_shop24c", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False
    return
label ep25_quests_shop_visitors6:
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage6 == 1:
        $ store_music()
        call cit6_dialog_1()
        $ restore_music()
        if _return != False:
            $ shopVisitorStage6 = 2
        $ set_active("Shop_Visitor6", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage6 == 2:
        $ store_music()
        call cit6_dialog_2()
        $ restore_music()
        if _return != False:
            $ shopVisitorStage6 = 3
        $ set_active("Shop_Visitor6", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view1")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False
    return
label ep25_quests_shop_visitors7:
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage7 == 1:
        $ store_music()
        call cit7_dialog_1()
        $ restore_music()
        if _return != False:
            $ shopVisitorStage7 = 2
        $ set_active("Shop_Visitor7", False)
        $ autorun_to_object("ep25_dialogues1_shop24b", scene="cloth_shop_view2")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    return
label ep25_quests_shop_visitors8:
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage8 == 1:
        call cit8_dialog_1()
        $ shopVisitorStage8 = 2
        $ set_active("Shop_Visitor8", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False
    if shopVisitorStage8 == 2:
        $ store_music()
        call cit8_dialog_2()
        if _return != False:
            $ shopVisitorStage8 = 3
        $ restore_music()
        $ set_active("Shop_Visitor8", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    return
label ep25_quests_shop_visitors9:
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage9 == 1:
        $ store_music()
        call cit9_dialog_1()
        $ restore_music()
        if _return != False:
            $ shopVisitorStage9 = 2
        $ set_active("Shop_Visitor9", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view2")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage9 == 2:
        $ store_music()
        call cit9_dialog_2()
        $ restore_music()
        if _return != False:
            $ shopVisitorStage9 = 3
        $ set_active("Shop_Visitor9", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    if shopVisitorStage9 == 3:
        $ store_music()
        call cit9_dialog_3()
        $ restore_music()
        if _return != False:
            $ shopVisitorsList.remove("Shop_Visitor9")
        $ set_active("Shop_Visitor9", False)
        $ autorun_to_object("ep25_dialogues1_shop24d", scene="cloth_shop_view2")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False

    return
label ep25_quests_shop_visitors10:
    if act=="l":
        return
    if monicaSellingDressInProgress == False:
        call ep25_quests_shop_visitors_not_working()
        return False
    if get_active_objects(scene="cloth_shop_dressing_room2", group="cloth_shop_visitors") != False:
        call ep25_dialogues1_shop21() # Ждет покупатель в примерочной
        return False

    if shopVisitorStage10 == 1:
        $ store_music()
        call cit10_dialog_1()
        $ restore_music()
        if _return != False:
            $ shopVisitorStage10 = 2
        $ set_active("Shop_Visitor10", False)
        $ autorun_to_object("ep25_dialogues1_shop24a", scene="cloth_shop_view2")
        call refresh_scene_fade()
        call ep25_quests_shop13() # Проверка на конец работы (нет посетителей)
        return False
    return

label ep25_quests_shop_visitors_not_working:
    call ep25_dialogues1_shop19()
    return
