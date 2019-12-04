#go_to_bardie
default monica_college_stage = 0
default monice_college_teacher_refused = False
default monica_college_teacher_kicked1 = False # Моника ударила учителя (4 посещение)
default monica_teacher_handjob = False
default monica_teacher_sex = False
default monica_teacher_sex_day = 0

default ep29_quests_monica_college_inited = False
default ep29_quests_monica_college_visit4_init_days_countdown = 3
default ep29_quests_monica_college_visit4_block = False



label ep29_quests_monica_college_visit2:
    if ep29_quests_monica_college_inited == False:
        $ add_hook("Teacher", "ep29_quests_monica_college_visit2_teacher", scene="college_class", label=["bardie_eric_quest_college_teacher","bardie_eric_quest_day2"])
        $ ep29_quests_monica_college_inited = True

    if cloth_type == "CasualDress":
        call dialogue_classmate_3_2b()
        return False
    if cloth_type == "Whore":
        call dialogue_classmate_3_2bb()
        return False
    if cloth_type != "SchoolOutfit":
        call dialogue_classmate_3_2bb()
        return False
    call change_scene("college_class","Fade_long", "highheels_run2")
    return False
label ep29_quests_monica_college_visit2_teacher:
    # второе посещение учителя
    if act=="l":
        return
    $ remove_hook()
    call dialogue_classmate_8()
    $ monica_college_stage = 1
    if _return == False:
        $ add_hook("enter_scene", "dialogue_classmate_5_1a", scene="street_college", once=True)
        $ monice_college_teacher_refused = True
        $ add_hook("Teleport_BedroomBardie", "ep29_quests_monica_college_visit2_refuse_bardie", scene="floor2", label=["bardie_eric_quest_college", "ep29_quests_monica_college_visit2_refuse_bardie"]) # Разблокируем комнату Барди на след.день

    else:
        # сходила успешно
        $ add_hook("enter_scene", "dialogue_classmate_8_1", scene="street_college", once=True)
        $ add_hook("change_time_evening", "ep29_quests_monica_college_mansfield_visit1", scene="global", once=True)
        $ monice_college_teacher_refused = False
        $ add_hook("Teleport_BedroomBardie", "ep29_quests_monica_college_visit2_success_bardie", scene="floor2", label=["bardie_eric_quest_college", "ep29_quests_monica_college_visit2_success_bardie"]) # Разблокируем комнату Барди на след.день
        $ add_corruption(monicaTeacherAddCorruption2, "monicaTeacherAddCorruption2")

    $ streetCollegeMonicaSuffix = 2
    $ remove_hook(label="bardie_eric_quest_day1")
    $ remove_hook(label="bardie_eric_quest_day2")
    $ add_hook("College", "ep28_monica_bardie_eric_college4_visit1_college_block", scene="street_college", label=["evening_time_temp", "bardie_eric_quest_day2block"]) # Блокируем колледж на сегодня
    $ add_objective("go_to_bardie", _("Сообщить Барди о визите в колледж"), c_orange, 85)
    call change_scene("street_college","Fade_long", "highheels_run2")

    return False

label ep29_quests_monica_college_mansfield_visit1:
    # Мэнсфилд приходит к учителю
    call dialogue_classmate_8_2()
    return

#    help "Продолжение квеста ожидайте в следующем обновлении игры!"

label ep29_quests_monica_college_visit2_success_bardie:
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_9_1()
    $ remove_objective("go_to_bardie")
    $ add_hook("College", "ep29_quests_monica_college_visit3", scene="street_college", label=["bardie_eric_quest_college", "bardie_eric_quest_day3"])
    $ add_hook("Teacher", "ep29_quests_monica_college_visit3_teacher", scene="college_class", label=["bardie_eric_quest_college_teacher", "bardie_eric_quest_day3"])
    $ add_hook("enter_scene", "dialogue_classmate_10", scene="street_college", once=True)
    call refresh_scene_fade()
    return False

label ep29_quests_monica_college_visit2_refuse_bardie: # наказание от Барди за отказ учителю
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_5_1b() # наказание
    $ remove_objective("go_to_bardie")
    $ add_hook("College", "ep29_quests_monica_college_visit2", scene="street_college", label=["bardie_eric_quest_college", "bardie_eric_quest_day2"])
    $ add_hook("Teacher", "ep29_quests_monica_college_visit2_teacher", scene="college_class", label=["bardie_eric_quest_college_teacher", "bardie_eric_quest_day2"])
    call change_scene("basement_bedroom2", "Fade_long", False)
    return False

label ep29_quests_monica_college_visit3: # третье посещение учителя
    if act=="l":
        return
    if day_time == "evening":
        return
    if cloth_type == "CasualDress":
        call dialogue_classmate_3_2b()
        return False
    if cloth_type == "Whore":
        call dialogue_classmate_3_2bb()
        return False
    if cloth_type != "SchoolOutfit":
        call dialogue_classmate_3_2bb()
        return False
    call change_scene("college_class","Fade_long", "highheels_run2")
    return False

label ep29_quests_monica_college_visit3_teacher: #учитель, третье посещение
    if act=="l":
        return
    call dialogue_classmate_11()
    $ monica_college_stage = 2
    if _return == False:
        $ add_hook("enter_scene", "dialogue_classmate_5_1a", scene="street_college", once=True)
        $ monice_college_teacher_refused = True
        $ add_hook("Teleport_BedroomBardie", "ep29_quests_monica_college_visit3_refuse_bardie", scene="floor2", label=["bardie_eric_quest_college", "ep29_quests_monica_college_visit3_refuse_bardie"]) # Разблокируем комнату Барди на след.день
    else:
        # успешно
        $ add_hook("enter_scene", "dialogue_classmate_11_1", scene="street_college", once=True)
        $ remove_objective("check_teacher")
        $ remove_objective("eric_college")
        $ monice_college_teacher_refused = False
        $ add_hook("Teleport_BedroomBardie", "ep29_quests_monica_college_visit3_success_bardie", scene="floor2", label=["bardie_eric_quest_college", "ep29_quests_monica_college_visit3_success_bardie"]) # Разблокируем комнату Барди на след.день
        $ add_corruption(monicaTeacherAddCorruption3, "monicaTeacherAddCorruption3")


    $ streetCollegeMonicaSuffix = 2
    $ remove_hook(label="bardie_eric_quest_day3")
    $ add_hook("College", "ep28_monica_bardie_eric_college4_visit1_college_block", scene="street_college", label=["evening_time_temp", "bardie_eric_quest_day3block"]) # Блокируем колледж на сегодня
    $ add_objective("go_to_bardie", _("Сообщить Барди о визите в колледж"), c_orange, 85)
    call change_scene("street_college","Fade_long", "highheels_run2")
    return False

label ep29_quests_monica_college_visit3_success_bardie:
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_9_2()
    $ autorun_to_object("dialogue_classmate_15a", scene="floor2")
    $ remove_objective("go_to_bardie")
    $ add_hook("change_time_day", "ep29_quests_monica_college_visit4_init", scene="global", label="bardie_eric_visit4_init_planned")
    call refresh_scene_fade()
    return False

label ep29_quests_monica_college_visit3_refuse_bardie: # наказание от Барди за отказ учителю
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_5_1b() # наказание
    $ remove_objective("go_to_bardie")
    $ add_hook("College", "ep29_quests_monica_college_visit3", scene="street_college", label=["bardie_eric_quest_college", "bardie_eric_quest_day3"])
    $ add_hook("Teacher", "ep29_quests_monica_college_visit3_teacher", scene="college_class", label=["bardie_eric_quest_college_teacher", "bardie_eric_quest_day3"])
    call change_scene("basement_bedroom2", "Fade_long", False)
    return False

label ep29_quests_monica_college_visit4_init:
    $ ep29_quests_monica_college_visit4_init_days_countdown -= 1
    if ep29_quests_monica_college_visit4_init_days_countdown > 0:
        return
    $ remove_hook()
    $ add_hook("enter_scene", "ep29_quests_monica_college_visit4_init_bardie1", scene="basement_bedroom2", label="bardie_eric_visit4_init_planned_b")
    return

label ep29_quests_monica_college_visit4_init_bardie1:
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_12() # Барди зовет Монику
    # Инициализация похода к Барди
    $ map_enabled = False
    $ miniMapEnabledOnly = ["Floor2", "Basement"]

    $ autorun_to_object("dialogue_classmate_1b", scene="basement_bedroom2")
#    $ add_hook("basement_monica_after_nap_dialogue", "dialogue_classmate_1b", scene="global", once=True)
    $ add_objective("go_to_bardie", _("Идти к Барди в комнату"), c_orange, 85)
    $ move_object("Betty", "empty")
    $ move_object("Ralph", "empty")

    $ add_hook("Teleport_Basement_Side", "dialogue_classmate_1c", scene="basement_hole", label="monica_bardie_meeting_block")
    $ add_hook("Teleport_Street", "dialogue_classmate_1c", scene="floor1", label="monica_bardie_meeting_block")
    $ add_hook("Teleport_Kitchen", "dialogue_classmate_1c", scene="floor1", label="monica_bardie_meeting_block")
    $ add_hook("Teleport_BedroomBardie", "ep29_quests_monica_college_visit4_init_bardie2", scene="floor2", label="monica_bardie_visit4_init", priority = 100)
    $ ep29_quests_monica_college_visit4_block = True
    $ monicaLastCleaningOfferedDay = day
    call refresh_scene_fade()
    return

label ep29_quests_monica_college_visit4_init_bardie2:
    if day_time != "evening":
        return
    if ep29_quests_monica_college_visit4_block == True:
        $ ep29_quests_monica_college_visit4_block = False
        $ remove_hook(label="monica_bardie_eric_meeting_block")
        $ remove_objective("go_to_bardie")
        $ map_enabled = True
        $ miniMapEnabledOnly = []
    call dialogue_classmate_12a() # Барди говорит Монике что надо снова идти к Эрику
    if _return == False:
        $ autorun_to_object("dialogue_classmate_3_2e", scene="floor2")
        call refresh_scene_fade()
        return False
    # Моника согласилась

    $ remove_hook(label="monica_bardie_visit4_init")
    $ autorun_to_object("dialogue_classmate_12_1", scene="floor2")
    $ add_hook("enter_scene", "dialogue_classmate_13", scene="street_college", once=True)
    $ add_hook("College", "ep29_quests_monica_college_visit4", scene="street_college", label=["bardie_eric_quest_college", "bardie_eric_quest_day4"])
    $ add_hook("Teacher", "ep29_quests_monica_college_visit4_teacher", scene="college_class", label=["bardie_eric_quest_college_teacher", "bardie_eric_quest_day4"])
    $ add_objective("eric_college", _("Уладить проблему Эрика в колледже"), c_blue, 45)
    call refresh_scene_fade()
    return False

label ep29_quests_monica_college_visit4:
    if act=="l":
        return
    if day_time == "evening":
        return
    if cloth_type == "CasualDress":
        call dialogue_classmate_3_2b()
        return False
    if cloth_type == "Whore":
        call dialogue_classmate_3_2bb()
        return False
    if cloth_type != "SchoolOutfit":
        call dialogue_classmate_3_2bb()
        return False
    call change_scene("college_class","Fade_long", "highheels_run2")
    return False

label ep29_quests_monica_college_visit4_teacher:
    if act=="l":
        return
    $ remove_hook(label="bardie_eric_quest_day4")
    call dialogue_classmate_14()
    $ monica_college_stage = 3
    if _return == False:
        $ monica_college_teacher_kicked1 = True
    $ add_hook("enter_scene", "dialogue_classmate_14_1", scene="street_college", once=True)
    $ remove_objective("eric_college")
    $ add_objective("go_to_bardie", _("Сообщить Барди о визите в колледж"), c_orange, 85)
    $ add_hook("Teleport_BedroomBardie", "ep29_quests_monica_college_visit4_bardie", scene="floor2", label="bardie_eric_quest_college_teacher")
    call change_scene("street_college","Fade_long", "highheels_run2")
    return False

label ep29_quests_monica_college_visit4_bardie:
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_15()
    $ autorun_to_object("dialogue_classmate_15a", scene="floor2")
    $ remove_objective("go_to_bardie")
    $ add_hook("Teleport_BedroomBardie", "ep29_quests_monica_college_check_next", scene="floor2", label="ep29_quests_monica_college_check_next")
    call refresh_scene_fade()
    return False

label ep29_quests_monica_college_check_next:
    return

#
