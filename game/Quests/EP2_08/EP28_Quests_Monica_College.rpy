default ep28_monica_eric_meeting_completed = False
default ep28_monica_bardie_eric_college_inited = False
default ep28_monica_bardie_eric_quest_stage = 0

label ep28_monica_bardie_init:
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_college_check_bardie_bedroom_clothes", scene="floor2", priority = 300, label="bedroom_bardie_check_cloth")
    $ add_hook("basement_monica_after_nap", "ep28_monica_bardie_init2", scene="global", once=True)
    return

label ep28_monica_bardie_init2: #next day
    call ep28_betty_college_init() # инициализируем линию Бетти по колледжу
#    $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_meeting", scene="floor2", label="bardie_eric_meeting")
    return

label ep28_monica_college_check_bardie_bedroom_clothes:
    if cloth_type != "Governess" and get_active_objects("Bardie", scene="bedroom_bardie") != False:
        call dialogue_betty_college_7_cloth()
        return False
    return

label ep28_monica_bardie_eric_meeting_init: # Инициализация знакомства с Эриком
    $ add_hook("enter_scene", "ep28_monica_bardie_eric_meeting_a", scene="basement_bedroom2", label="ep28_monica_bardie_eric_meeting_a")
    return

label ep28_monica_bardie_eric_meeting_a:
    if day_time != "evening":
        return
    $ remove_hook()
    call dialogue_classmate_1()

    $ map_enabled = False
    $ miniMapEnabledOnly = ["Floor2", "Basement"]
    call refresh_scene_fade()
    $ autorun_to_object("dialogue_classmate_1b", scene="basement_bedroom2")
    $ add_objective("go_to_bardie", _("Идти к Барди в комнату"), c_orange, 45)
    $ move_object("Betty", "empty")

    $ add_hook("Teleport_Basement_Side", "dialogue_classmate_1c", scene="basement_hole", label="monica_bardie_eric_meeting_block")
    $ add_hook("Teleport_Street", "dialogue_classmate_1c", scene="floor1", label="monica_bardie_eric_meeting_block")
    $ add_hook("Teleport_Kitchen", "dialogue_classmate_1c", scene="floor1", label="monica_bardie_eric_meeting_block")
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_meeting", scene="floor2", label="monica_bardie_eric_meeting", priority = 100)
    $ monicaLastCleaningOfferedDay = day
    return

label ep28_monica_bardie_eric_meeting: # Знакомство с Эриком (Моника заходит вечером к Барди)
    if day_time != "evening":
        return
    call dialogue_classmate_1a()
    $ remove_hook(label="monica_bardie_eric_meeting_block")
    $ remove_objective("go_to_bardie")
    $ map_enabled = True
    $ miniMapEnabledOnly = []
    $ autorun_to_object("dialogue_classmate_15a", scene="floor2")
    if _return == True:
        $ autorun_to_object("dialogue_classmate_1b1", scene="floor2")
        $ remove_hook(label="monica_bardie_eric_meeting")
        $ ep28_monica_eric_meeting_completed = True
        $ add_hook("Teleport_BedroomBardie", "dialogue_classmate_1_1", scene="floor2", label=["bardie_eric_quest_college", "evening_time_temp"]) # Разблокируем комнату Барди на след.день
#        if bettyCollegeTeacherRefused == True: # Если был отказ у Бетти, то продолжаем линию квестов с Моникой без нее
        call ep28_monica_bardie_eric_college_init()
    call refresh_scene_fade()
    return False

label ep28_monica_bardie_eric_college_init: # инициализация квеста колледжа с Эриком и Моникой
    $ add_hook("change_time_day", "ep28_monica_bardie_eric_college0", scene="global", label="bardie_eric_quest_college")
    $ ep28_monica_bardie_eric_college_inited = True
    return

label ep28_monica_bardie_eric_college0:
    $ remove_hook()
    $ add_hook("enter_scene", "ep28_monica_bardie_eric_college1", scene="basement_bedroom2", label="bardie_eric_quest_college")
    return
label ep28_monica_bardie_eric_college1:
    if day_time != "evening":
        return
    $ remove_hook()
    $ autorun_to_object("dialogue_classmate_1b", scene="basement_bedroom2")
    $ add_objective("go_to_bardie", _("Идти к Барди в комнату"), c_orange, 45)
    $ move_object("Betty", "empty")
    call refresh_scene_fade()
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_college2", scene="floor2", label="bardie_eric_quest_college")
    return

label ep28_monica_bardie_eric_college2:
    $ remove_hook()
    call dialogue_classmate_2() # Барди говорит Монике притворяться мамой Эрика
    $ add_hook("Teleport_BedroomBardie", "dialogue_classmate_1_1", scene="floor2", label=["bardie_eric_quest_college", "evening_time_temp"]) # Разблокируем комнату Барди на след.день
    return

label ep28_monica_bardie_eric_college3:
    if bettyCollegeTeacherStage > 0:
        call ep28_betty_college_monica_lesbie_init()
    return

label ep28_monica_college_bardie_erick_quest_check:

    return
