default steveVisit1PlannedComplete = False
default steveVisit1DayShowed0 = False
default steveVisit1DayShowed = False

label ep24_quests_steve1:
    # После второго посещения фитнеса, планируем приход Стива на субботу
    $ steveVisit1PlannedComplete = True # Флаг блокировки повторения

    $ add_hook_day("ep24_quests_steve2", week_day = 6)
    $ add_hook("monica_cleaning_end", "ep24_quests_steve3", scene="global", label="steve_visit1")
    $ add_hook("map_teleport", "ep24_quests_steve4", scene="global", label="steve_visit1")

    $ add_hook("basement_monica_before_nap", "ep24_quests_steve5", scene="global", label="steve_visit1") # В пятницу вечером также запускаем сцену с Бетти о приходе Стива

    # Перехват телепортации по миникарте
    $ add_hook("before_open", "ep24_quests_steve4", scene="floor1_stairs", label="steve_visit1") # Переход ногами на лестницу из подвала
    $ add_hook("before_open", "ep24_quests_steve4", scene="bedroom1", label="steve_visit1")
    $ add_hook("before_open", "ep24_quests_steve4", scene="bedroom2", label="steve_visit1")
    $ add_hook("before_open", "ep24_quests_steve4", scene="bathroom_bath", label="steve_visit1")
    $ add_hook("before_open", "ep24_quests_steve4", scene="floor1", label="steve_visit1")
    $ add_hook("before_open", "ep24_quests_steve4", scene="floor2", label="steve_visit1")
    $ add_hook("before_open", "ep24_quests_steve4", scene="kitchen2", label="steve_visit1")
    $ add_hook("before_open", "ep24_quests_steve4", scene="street_house_main_yard", label="steve_visit1")
#    $ photoShootDisabledNextWeek = True

    return

label ep24_quests_steve2:
    # Перехват субботы первого посещения Стива
    $ basementBedSkipUntilFridayEnabled = False
    $ skipDaysInterrupted = True
    call ep24_dialogues2_steve3()
    $ cloth = "Governess"
    $ cloth_type = "Governess"
    call change_scene("floor1", "Fade_long", False)
    $ rooms_clean_list_exclude = ["living_room"]
    $ move_object("Betty", scene="living_room")
    $ move_object("Ralph", scene="living_room")
    $ add_hook("Teleport_LivingRoom", "ep24_dialogues2_steve4", scene="floor1", label="steve_visit1")

#    $ add_hook("map_teleport", "ep24_quests_steve6", scene="global", label="steve_visit1a")
#    $ add_hook("enter_scene", "ep24_quests_steve6", scene="basement_bedroom1", label="steve_visit1a")
#    $ add_hook("enter_scene", "ep24_quests_steve6", scene="basement_bedroom2", label="steve_visit1a")
    $ add_hook("exit_scene", "ep24_quests_steve6", scene="floor1", label="steve_visit1a")

    $ add_hook("change_time_evening", "ep24_quests_steve6b", scene="global", label="steve_visit1")
    $ add_hook("basement_monica_before_sleep", "ep24_quests_steve7", scene="global", label="steve_visit1")
    return

label ep24_quests_steve3:
    # Бетти говорит Монике после уборки что в субботу придет Стив
    $ remove_hook()
    call ep24_dialogues2_steve1()
    return

label ep24_quests_steve4:
    # Бетти говорит Монике при попытке выйти по карте что завтра придет Стив (пятница)
    if week_day != 5:
        return
    $ remove_hook(label="steve_visit1")
    call ep24_dialogues2_steve2()
    return

label ep24_quests_steve5:
    # Блокировка сна в пятницу, если Бетти не говорила Монике о Стиве
    if week_day != 5:
        return
    help "Отдых отменен. В доме остались незавершенные события..."
    $ skipDaysInterrupted = True
    return False


label ep24_quests_steve6:
    # Срабатывание дня первого застолья при переходе по карте или в спальню
    $ remove_hook(label = "steve_visit1a")
    if steveVisit1DayShowed0 == True:
        return
    call ep24_dialogues2_steve5() # День первого застолья
    $ move_object("Betty", scene="living_room")
    $ move_object("Ralph", scene="living_room")
    $ steveVisit1DayShowed0 = True
    return

label ep24_quests_steve6b:
    # Срабатывание продолжения дня первого застолья
    call ep24_dialogues2_steve5a()
    $ move_object("Betty", scene="living_room")
    $ move_object("Ralph", scene="living_room")
    $ steveVisit1DayShowed = True
    return

label ep24_quests_steve7:
    # Срабатывание вечера первого застолья
    $ remove_hook(label = "steve_visit1")
    if steveVisit1DayShowed == False:
        call ep24_dialogues2_steve5a()

    call ep24_dialogues2_steve6() # вечер первого застолья

    call ep24_dialogues2_steve7() # сцена Бетти и Стива на кухне
#    $ move_object("Betty", scene="living_room")
#    $ move_object("Ralph", scene="living_room")
#    $ set_var("Ralph", base = "House_LivingRoom_Ralph_Sleeping[day_suffix]", scene="living_room")
#    $ add_hook("change_time_day", "ep24_quests_steve8", scene="global") # Возвращаем спрайт Ральфа
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 2.0
    $ skipDaysInterrupted = False
    $ rooms_clean_list_exclude = []
    $ questLog(31, True)

    $ add_hook("monica_cleaning_end", "ep24_quests_bardie1", scene="global")
    return

label ep24_quests_steve8:
    # Возвращаем спрайт Ральфа
    $ remove_hook()
    $ set_var("Ralph", base = "House_LivingRoom_Ralph[day_suffix]", scene="living_room")
    return
















#
