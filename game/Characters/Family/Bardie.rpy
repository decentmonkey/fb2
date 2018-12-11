default bardieLocation = "none"
default monicaBardieOffended1 = False

label bardieInteract1:
    if act == "l":
        mt "Этот маленький оболтус меня бесит!"
        return
    if act == "t":
        if scene_name == "street_house_main_yard":
            call bardie_comment5() from _call_bardie_comment5
            return
        if scene_name == "bedroom_bardie":
            if day_time == "day":
                call bardieDialogue1() from _call_bardieDialogue1
            else:
                call bardie_comment5() from _call_bardie_comment5_1
            return
    return
#        if bardieLocation == "BedroomBardie":
#            call bardieDialogue1()
#            return

#    if bardieLocation == "Floor1" and act == "w":
#        call change_scene("floor1_fountain", "Fade", "snd_fountain")


    return


label bardieMonicaCleaningInteract:
    if act == "l":
        mt "Он так и пытается подкрасться ко мне!"
        "Мне надо быть осторожнее..."
        return False
    if act == "t":
        if scene_name == "floor1":
            call cleaning_bardie_comment1() from _call_cleaning_bardie_comment1
        if scene_name == "bedroom_bardie":
            call cleaning_bardie_comment2() from _call_cleaning_bardie_comment2
        if scene_name == "bedroom_second":
            call cleaning_bardie_comment3() from _call_cleaning_bardie_comment3
        $ move_object("Bardie", "empty")
        $ monicaCleaningObject = "" # Ставим Монику в исходное положение стоя
        $ add_char_progress("Bardie", bardieCleaningUpskirtTry, "cleaning_upskirt_day " + str(day))
        call refresh_scene_fade() from _call_refresh_scene_fade_20
        return False
    return

label bardieProgressLevelUp1:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ add_hook("monica_cleaning_end", "bardieProgressApplyAfterCleaning", scene="global")
        $ char_data["enabled"] = False #закрываем прогресс до следующей версии
    return

label bardieProgressApplyAfterCleaning:
    $ add_hook("Bardie_Life_evening", "Bardie_Life_evening2", scene="global")
    $ add_hook("Bardie", "bardieStairsFloor1Hook1", scene="floor1_stairs", label="bardie_catch_monica_at_stairs") # Диалог с Барди у лестницы
    $ add_hook("Teleport_Basement_Pool", "bardieCatchAtStaitsTeleportPoolHook", scene="floor1_stairs", label="bardie_catch_monica_at_stairs_onetime")
    $ add_hook("mimimap_teleport", "bardieCatchAtStaitsMinimapHook", scene="global", label="bardie_catch_monica_at_stairs_onetime")
    $ remove_hook()
    return


label bardieStairsFloor1Hook1:
    if cloth_type != "Governess":
        bardie "Моника! Покажи трусики!"
        return False
    call bardie_comment4() from _call_bardie_comment4
    $ add_hook("exit_scene", "bardieStairsLeaveOnMonicaLocationExit", scene="floor1_stairs")
    return False

label bardieCatchAtStaitsMinimapHook:
    if target_scene_name == "basement_bedroom2" and get_active_objects("Bardie", scene="floor1_stairs") != False and cloth_type == "Governess":
        call bardie_comment4() from _call_bardie_comment4_1
        call change_scene("floor1_stairs", "Fade", False) from _call_change_scene_39
        $ add_hook("exit_scene", "bardieStairsLeaveOnMonicaLocationExit", scene="floor1_stairs")
        return False
    return True

label bardieCatchAtStaitsTeleportPoolHook:
    if get_active_objects("Bardie", scene="floor1_stairs") != False and cloth_type == "Governess":
        call bardie_comment4() from _call_bardie_comment4_2
        $ add_hook("exit_scene", "bardieStairsLeaveOnMonicaLocationExit", scene="floor1_stairs")
        return False
    return

label bardieStairsLeaveOnMonicaLocationExit:
    $ move_object("Bardie", "bedroom_bardie")
    $ remove_hook()
    return
