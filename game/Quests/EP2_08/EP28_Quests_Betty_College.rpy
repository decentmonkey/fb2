default bettyCollegeDay1JobFinished = False
default bettyCollegeDay = 0

label ep28_betty_college_init:
    call dialogue_betty_college_0_1()
#    $ add_hook("Teleport_BedroomBardie",
    $ add_hook("enter_scene", "dialogue_betty_college_0_1b", scene="floor2", once=True)
    $ cloth = "Governess"
    $ cloth_type = "Governess"
    call change_scene("floor2", "Fade_long")

    $ add_hook("change_time_day", "ep28_betty_college2", scene="global", once=True, label="ep28_betty_college2")
    return

label ep28_betty_college2:
    call dialogue_betty_college_1() # Барди говорит Бетти что надо идти в колледж

    # инициализируем колледж

    $ streetCollegeBettySuffix = 1 # Бетти смотрит на школу
    $ set_active("Betty", True, scene="street_college")
    $ set_active("Betty", True, scene="college_class")
    $ add_hook("Betty", "dialogue_betty_college_1_1s", scene="street_college", label="betty_college_common", owner="Betty")
    $ add_hook("Betty", "dialogue_betty_college_1_1s", scene="college_class", label="betty_college_common", owner="Betty")

    $ add_hook("College", "ep28_betty_college2_building", scene="street_college", label=["betty_college_common"], owner="Betty")
    $ add_hook("College", "ep28_betty_college2_building_day1", scene="street_college", label=["betty_college_common", "betty_college_day1"], owner="Betty")

    $ add_hook("Teleport_Street_College", "ep28_betty_college2_class_teleport_back", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_Books", "dialogue_betty_college_1_1m", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_Desk", "dialogue_betty_college_1_1n", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_Formulas", "dialogue_betty_college_1_1r", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_SchoolTables", "dialogue_betty_college_1_1p", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_Windows", "dialogue_betty_college_1_1l", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("College_Class_WorldMap", "dialogue_betty_college_1_1o", scene="college_class", label="betty_college_common", owner="Betty")

    $ add_hook("Teacher", "ep28_betty_college2_teacher", scene="college_class", label="betty_college_common", owner="Betty")
    $ add_hook("Teacher", "ep28_betty_college2_teacher_day1", scene="college_class", label="betty_college_day1", owner="Betty")

    $ add_hook("enter_scene", "dialogue_betty_college_1_1a", scene="street_house_main_yard", once=True, owner="Betty")
    call locations_init_college()
    call ep28_betty_init()
    $ move_object("Ralph", "living_room")
    $ add_objective("bardie_college", _("Уладить проблему Барди в колледже"), c_green, 15)
    return

label ep28_betty_college2_building:
    if act=="l":
        call dialogue_betty_college_1_1s()
        return
    call dialogue_betty_college_1_1b()
    return False

label ep28_betty_college2_building_day1:
    if act=="l":
        return
    call change_scene("college_class", "Fade_long", "highheels_run2")
    return False

label ep28_betty_college2_class_teleport_back:
    $ streetCollegeBettySuffix = 2
    call change_scene("street_college", "Fade_long", "highheels_run2")
    return

label ep28_betty_college2_teacher:

    if act=="l":
        call dialogue_betty_college_1_1k()
        return
    return


label ep28_betty_college2_teacher_day1: # Сцена учителя с Бетти день 1
    if act=="l":
        call dialogue_betty_college_1_1_2()
        return False
    $ bettyCollegeDay = 1
    call dialogue_betty_teacher_1()
    if _return == True:
        $ bettyCollegeDay1JobFinished = True
        $ add_hook("enter_scene", "dialogue_betty_college_1_1_3", scene="street_college", owner="Betty", once=True)

    $ remove_hook(label="betty_college_day1")

    $ streetCollegeBettySuffix = 2
    call change_scene("street_college", "Fade_long", "highheels_run2")

    $ move_object("Bardie", "street_house_main_yard")
    $ add_hook("Bardie", "ep28_betty_college2_teacher_day1b", scene="street_house_main_yard", owner="Betty", label="betty_college_day1")
    $ add_hook("Betty", "dialogue_betty_college_1_1i", scene="street_house_main_yard", owner="Betty", label="betty_college_day1")
    $ add_hook("Driver", "dialogue_betty_college_1_1a0", scene="street_house_main_yard", owner="Betty", label="betty_college_day1")

    return False

label ep28_betty_college2_teacher_day1b: # Бетти возвращается из колледжа, говорит с Барди
    if act=="l":
        call dialogue_betty_college_1_1c()
        return False
    if bettyCollegeDay1JobFinished == True:
        call dialogue_betty_college_2()
    else:
        call dialogue_betty_college_2_1()
        $ add_hook("change_time_day", "ep28_betty_college2_teacher_day1d", scene="global", label="betty_college_aborted")
    $ remove_hook(label="betty_college_day1")
    $ move_object("Bardie", "empty")
    $ add_hook("enter_scene", "ep28_betty_college2_teacher_day1c", scene="floor1", owner="Betty", once=True)
    call refresh_scene_fade()
    return False

label ep28_betty_college2_teacher_day1c: # Бетти заходит в дом (переход управления к Монике)
    if bettyCollegeDay1JobFinished == True:
        call dialogue_betty_college_3()
    $ move_object("Betty", "bedroom1")
    music stop
    img black_screen
    with diss
    pause 1.5
    $ hudDaySkipToEveningEnabled = True
    call change_scene("basement_bedroom2", "Fade_long", False)
    call change_owner("Monica")

    $ add_hook("change_time_day", "ep28_betty_college2_teacher_day2", scene="global", label="betty_college_day2")

    return False

label ep28_betty_college2_teacher_day1d: # Квест остановлен
    return


label ep28_betty_college2_teacher_day2: # Инициализация 2-го дня похода к учителю
    if week_day == 7:
        return
    $ remove_hook()

    $ add_hook("enter_scene", "dialogue_betty_college_1_1_4", scene="street_college", once=True, owner="Betty")
    $ add_hook("College", "ep28_betty_college2_building_day1", scene="street_college", label="betty_college_day2", owner="Betty")
    $ add_hook("Teacher", "ep28_betty_college2_teacher_day2_teacher", scene="college_class", label="betty_college_day2", owner="Betty")

    $ move_object("Ralph", "living_room")

    $ streetCollegeBettySuffix = 1

    call change_owner("Betty")
    $ set_active("Betty", True, scene="House", recursive=True)
    $ set_active("Betty", True, scene="street_college", recursive=True)
    $ hudDaySkipToEveningEnabled = False

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(_("Утро..."))
    img black_screen
    with Dissolve(2.0)

    call change_scene("street_house_main_yard")
    return

label ep28_betty_college2_teacher_day2_teacher: # Разговор с учителем
    if act=="l":
        return
    call dialogue_betty_teacher_2()
    $ bettyCollegeDay = 2

    $ add_hook("enter_scene", "dialogue_betty_college_1_1_5", scene="street_college", owner="Betty", once=True)
    $ remove_hook(label="betty_college_day2")
    $ streetCollegeBettySuffix = 2

    music stop
    img black_screen
    with diss
    pause 2.0
    call change_scene("street_college", "Fade_long", "highheels_run2")

    $ move_object("Bardie", "street_house_main_yard")
    $ add_hook("Bardie", "ep28_betty_college2_teacher_day2b", scene="street_house_main_yard", owner="Betty", label="betty_college_day2")
    $ add_hook("Betty", "dialogue_betty_college_1_1i", scene="street_house_main_yard", owner="Betty", label="betty_college_day2")
    $ add_hook("Driver", "dialogue_betty_college_1_1a0", scene="street_house_main_yard", owner="Betty", label="betty_college_day2")


    return False

label ep28_betty_college2_teacher_day2b: # Разговор с Барди после сцены 2-го дня
    if act=="l":
        call dialogue_betty_college_1_1c()
        return False
    call dialogue_betty_college_4()

    $ remove_hook(label="betty_college_day2")
    $ move_object("Bardie", "empty")
    $ add_hook("enter_scene", "ep28_betty_college2_teacher_day2c", scene="floor1", owner="Betty", once=True)
    call refresh_scene_fade()
    return False

label ep28_betty_college2_teacher_day2c: # Бетти заходит в дом, завершение дня 2
    call dialogue_betty_college_3()
    $ move_object("Betty", "bedroom1")
    music stop
    img black_screen
    with diss
    pause 1.5
    $ hudDaySkipToEveningEnabled = True
    call change_scene("basement_bedroom2", "Fade_long", False)
    call change_owner("Monica")

    $ add_hook("change_time_day", "ep28_betty_college2_teacher_day3", scene="global", label="betty_college_day3")

    return

label ep28_betty_college2_teacher_day3:
    if week_day == 7:
        return
    return
#
