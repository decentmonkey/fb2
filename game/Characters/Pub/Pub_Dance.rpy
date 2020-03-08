default pubDanceGirlsBlockedDay = 0
default monica_strip_tips_today = 0
default monica_shared_tips_with_ashley_last_day = 0
default pubDanceCount = 0
default monicaDancedLastDay = 0
default monicaDancingTopless = False
default monicaDancingJoeAskedAboutPrivate = False
default monicaDancingWillingly = False
default monicaAshleyTalkedAboutSharingTips = False
default monicaAshleyTalkedAboutSharingTipsDay = 0
default monicaDancingStage = 0 # 0 - корсет (1..3), 1 - топлесс (4..6), 2 - топлесс (7..9)
default monicaDancingInProgress = False
default monicaStartedStripDanceFlag = True
default monicaDanceStartHookInited = False

label pub_dance_movegirls_to_makeuproom:
    # перемещение стриптизерш в гримерку (вызывается при начале танцев)
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False:
        $ move_object("Pub_StripteaseGirl1", "pub_makeuproom")
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        $ move_object("Pub_StripteaseGirl2", "pub_makeuproom")
    return


label pub_dance_movegirls_to_stage:
    # перемещение стриптизерш из гримерки на сцену (вызывается при окончании танцев)
    if get_active_objects("Pub_StripteaseGirl1", scene="pub_makeuproom") != False:
        $ move_object("Pub_StripteaseGirl1", "pub")
    if get_active_objects("Pub_StripteaseGirl2", scene="pub_makeuproom") != False:
        $ move_object("Pub_StripteaseGirl2", "pub")
    return

label pub_dance_init:
    $ monicaDancingWillingly = True
    $ add_hook("monica_pole_dance", "pub_dance1", scene="global", label="monica_pole_dance", quest="monica_dance_pub")
    $ add_hook("monica_pole_dance_end", "pub_dance_end1", scene="global", label="monica_pole_dance_end", quest="monica_dance_pub")
    $ add_hook("Teleport_Hostel_Street", "pub_dance_exit_check", scene="pub", label="monica_pole_dance_exit_check", quest="monica_dance_pub", priority = 201)
    $ add_hook("Teleport_Pub", "pub_dance_close", scene="pub_makeuproom", label="monica_pole_dance_close", quest="monica_dance_pub")
    $ add_hook("enter_scene", "pub_dance_scene_return", scene="pub_stage1", label="monica_dance_return_stage", quest="monica_dance_pub")
    $ add_hook("Pub_StripteaseGirl2", "ep29_quests_pub1_day4_claire", scene="pub_makeuproom", label="monica_dance_claire_regular_dialogue1", quest="monica_dance_pub")

    $ pubMonicaDanceTipsKoeffText = "30"
    return

label pub_dance_start: # Начало танцев (выбор в меню)
    call dialogue_5_dance_strip_20() # Разговор о начале танцев
    if _return == False:
        call refresh_scene_fade()
        return
    $ set_active("Teleport_Pub_MakeupRoom", True, scene="pub")
    $ monicaDancingInProgress = True
    if pubMakeupRoomGirlsRandomSuffix == True:
        $ pub_makeuproom_claire_suffix= rand(1,7)
        $ pub_makeuproom_molly_suffix = rand(1,8)
    call pub_dance_movegirls_to_makeuproom()
    if monicaDanceStartHookInited == False:
        $ add_hook("start_dance_event", "pub_dance_start_event_hook", scene="global", label="pub_dance_start_event_hook")
        $ monicaDanceStartHookInited = True
    call process_hooks("start_dance_event", "global")
    call refresh_scene_fade()
    return

label pub_dance_close: # Закрывание гримерки
    if monicaDancingInProgress == True and monicaDancedLastDay != day:
        return

    $ set_active("Teleport_Pub_MakeupRoom", False, scene="pub")
    $ monicaDancingInProgress = False
    return

label pub_dance_scene_return:
    # Моника заходит к сцене после танцев
    if cloth_type == "StripOutfit" and monicaDancedLastDay == day: # Моника выходит к сцене сразу после танцев
        sound snd_applause1
        call dialogue_5_dance_strip_5ca()
    return

label pub_dance_ashley_after:
    if act=="l":
        return
    if monicaDancedLastDay != day:
        if monicaDancingInProgress == True:
            call dialogue_5_dance_strip_4na()
            return False
        return
    if monicaAshleyTalkedAboutSharingTipsDay < day and monica_shared_tips_with_ashley_last_day != day:
        call dialogue_5_dance_strip_22()
        $ monica_shared_tips_with_ashley_last_day = day
        return False
    call dialogue_5_dance_strip_4m()
    return False

label pub_dance_joe_after:
    if act=="l":
        return
    if monicaDancedLastDay != day:
        if monicaDancingInProgress == True:
            call dialogue_5_dance_strip_4na()
            return False
        return
    if monicaAshleyTalkedAboutSharingTipsDay < day and monica_shared_tips_with_ashley_last_day != day:
        call dialogue_5_dance_strip_22()
        $ monica_shared_tips_with_ashley_last_day = day
        return False
    call dialogue_5_dance_strip_4m()
    return False

label pub_dance_remove_stage_visitors:
    $ set_active("Pub_Visitor7", False, scene="pub")
    $ set_active("Pub_Visitor8", False, scene="pub")
    return

label pub_dance1: # Обычные танцы
    $ remove_objective("go_dance")
    $ monica_strip_tips_today = 0
    $ pubDanceCount += 1

    call pub_dance1_stage_start1()
#    m "Танцы"
#    if pubDanceCount == 1:
#        $ monica_strip_tips_today = 0
#    if pubDanceCount > 1:
#        $ monica_strip_tips_today = rand(5,30)
        # dialogue_5_dance_strip_11!!!
    $ move_object("Pub_StripteaseGirl2", "empty")
    $ move_object("Pub_StripteaseGirl1", "empty")
    $ monicaDancedLastDay = day
    return

label pub_dance_end1: # Обычное завершение танцев
    $ add_hook("enter_scene", "dialogue_5_dance_strip_18", scene="pub_makeuproom", once=True, label="dialogue_5_dance_strip_18")
    call pub_dance_remove_stage_visitors()
    if monicaAshleyTalkedAboutSharingTips == False: # Эшли говорила Монике о том, что та должна отдавать ей часть чаевых (танцы по желанию)
        $ monicaAshleyTalkedAboutSharingTips = True
        $ add_hook("Teleport_Pub", "pub_dance_ashley_tips1", scene="pub_makeuproom", label="monica_dance_ashley_tips1", quest="monica_dance_pub")

    if monicaDancingJoeAskedAboutPrivate == False and monicaDancingStage >= 2:
        # Джо спрашивает о приватных танцах
        call dialogue_5_dance_strip_24()
        $ monicaDancingJoeAskedAboutPrivate = True
    if ep29_quests_molly_fall_panties_planned == True and ep29_quests_molly_fall_panties_completed == False and monicaDancingTopless == True:
        # Падают трусики
        call ep210_dialogues4_dance_strip_12()
        call ep210_dialogues4_dance_strip_13()
        $ ep29_quests_molly_fall_panties_planned = False
        $ ep29_quests_molly_fall_panties_completed = True

    if ep29_quests_monica_molly_was_fine == True and ep211_quests_pub_started_stole_tips == False: # Если Моника оправдали после Молли и она еще не крала чаевых
        call ep211_quests_pub1()

    if monicaPubDanceStoleTipsBankerPlanned == True:
        call ep211_quests_pub3_start_banker_quest()
        if _return == False:
            return False

    $ ep29_quests_claire_dance_planned = False
    $ remove_hook(label="remove_after_dance")
    $ move_object("Pub_StripteaseGirl2", "empty")
    $ move_object("Pub_StripteaseGirl1", "empty")
    $ pubDanceGirlsBlockedDay = day
    $ pub_makeuproom_monica_suffix = 2
    call change_scene("pub_makeuproom", "Fade_long")
    return False

label pub_dance_ashley_tips1:
    if cloth_type == "StripOutfit":
        return
    $ remove_hook()
    call dialogue_5_dance_strip_21() # Эшли говорит о том, что Моника должна делиться чаевыми
    $ monicaAshleyTalkedAboutSharingTipsDay = day
    return

label pub_dance_exit_check: # проверка на выход из бара

    if monicaDancingInProgress == True:
        # Закрываем танцы
        $ monicaDancingInProgress = False
        $ set_active("Teleport_Pub_MakeupRoom", False, scene="pub")
        call pub_dance_movegirls_to_stage()
        return
    if monicaAshleyTalkedAboutSharingTipsDay < day and monica_shared_tips_with_ashley_last_day != day and monicaDancedLastDay == day:
        # Моника сегодня танцевала и не отдавала чаевые
        call dialogue_5_dance_strip_23()
        if _return == True:
            call refresh_scene_fade()
            return False
    return


label pub_dance_start_event_hook:
    # Начало события (после разговора с Эшли/Джо)
    if monicaDancingJoeAskedAboutPrivate == True: # Если Джо уже спрашивал о приватах
        call ep210_quests_pub1() # Проверяем на события

    return
