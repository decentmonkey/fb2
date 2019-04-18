default steveVisit1PlannedComplete = False
default steveVisit1DayShowed0 = False
default steveVisit1DayShowed = False
default monicaAskedVictoriaAboutSteveMoney = False

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
    $ remove_hook()
    $ basementBedSkipUntilFridayEnabled = False
    $ skipDaysInterrupted = True
    call ep24_dialogues2_steve3() from _call_ep24_dialogues2_steve3
    $ cloth = "Governess"
    $ cloth_type = "Governess"
    call change_scene("floor1", "Fade_long", False) from _call_change_scene_193
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
    call ep24_dialogues2_steve1() from _call_ep24_dialogues2_steve1
    return

label ep24_quests_steve4:
    # Бетти говорит Монике при попытке выйти по карте что завтра придет Стив (пятница)
    if week_day != 5:
        return
    $ remove_hook(label="steve_visit1")
    call ep24_dialogues2_steve2() from _call_ep24_dialogues2_steve2
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
    call ep24_dialogues2_steve5() from _call_ep24_dialogues2_steve5 # День первого застолья
    $ move_object("Betty", scene="living_room")
    $ move_object("Ralph", scene="living_room")
    $ steveVisit1DayShowed0 = True
    return

label ep24_quests_steve6b:
    # Срабатывание продолжения дня первого застолья
    call ep24_dialogues2_steve5a() from _call_ep24_dialogues2_steve5a
    $ move_object("Betty", scene="living_room")
    $ move_object("Ralph", scene="living_room")
    $ steveVisit1DayShowed = True
    return

label ep24_quests_steve7:
    # Срабатывание вечера первого застолья
    $ remove_hook(label = "steve_visit1")
    if steveVisit1DayShowed == False:
        call ep24_dialogues2_steve5a() from _call_ep24_dialogues2_steve5a_1

    call ep24_dialogues2_steve6() from _call_ep24_dialogues2_steve6 # вечер первого застолья

    call ep24_dialogues2_steve7() from _call_ep24_dialogues2_steve7 # сцена Бетти и Стива на кухне
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

    $ basementBedSkipUntilFridayEnabled = True
    $ add_hook("monica_cleaning_end", "ep24_quests_bardie1", scene="global")
    return

label ep24_quests_steve8:
    # Возвращаем спрайт Ральфа
    $ remove_hook()
    $ set_var("Ralph", base = "House_LivingRoom_Ralph[day_suffix]", scene="living_room")
    return

label ep24_quests_steve9:
    # Инициализация второго посещения Стива (вешается у Бетти в квестах)
    if week_day == 6: #Если суббота, то пропускаем до следующей субботы
        return
    $ remove_hook()
    $ add_hook_day("ep24_quests_steve13", week_day = 6)
    $ add_hook("monica_cleaning_end", "ep24_quests_steve10", scene="global", label="steve_visit2")
    $ add_hook("map_teleport", "ep24_quests_steve11", scene="global", label="steve_visit2")

    $ add_hook("basement_monica_before_nap", "ep24_quests_steve12", scene="global", label="steve_visit2") # В пятницу вечером также запускаем сцену с Бетти о приходе Стива

    # Перехват телепортации по миникарте
    $ add_hook("before_open", "ep24_quests_steve11", scene="floor1_stairs", label="steve_visit2") # Переход ногами на лестницу из подвала
    $ add_hook("before_open", "ep24_quests_steve11", scene="bedroom1", label="steve_visit2")
    $ add_hook("before_open", "ep24_quests_steve11", scene="bedroom2", label="steve_visit2")
    $ add_hook("before_open", "ep24_quests_steve11", scene="bathroom_bath", label="steve_visit2")
    $ add_hook("before_open", "ep24_quests_steve11", scene="floor1", label="steve_visit2")
    $ add_hook("before_open", "ep24_quests_steve11", scene="floor2", label="steve_visit2")
    $ add_hook("before_open", "ep24_quests_steve11", scene="kitchen2", label="steve_visit2")
    $ add_hook("before_open", "ep24_quests_steve11", scene="street_house_main_yard", label="steve_visit2")
    return

label ep24_quests_steve10:
    # Бетти говорит Монике после уборки что в субботу придет Стив
    $ remove_hook()
    call ep24_dialogues2_steve8() from _call_ep24_dialogues2_steve8
    return

label ep24_quests_steve11:
    # Бетти говорит Монике при попытке выйти по карте что завтра придет Стив (пятница)
    if week_day != 5:
        return
    $ remove_hook(label="steve_visit2")
    call ep24_dialogues2_steve9() from _call_ep24_dialogues2_steve9
    return

label ep24_quests_steve12:
    # Блокировка сна в пятницу, если Бетти не говорила Монике о Стиве
    if week_day != 5:
        return
    help "Отдых отменен. В доме остались незавершенные события..."
    $ skipDaysInterrupted = True
    return False


label ep24_quests_steve13:
    # Перехват субботы второго посещения Стива
    $ remove_hook()

    $ add_hook("Betty_Life_day", "Betty_Life_none", scene="global", label="steve_visit2")
    $ add_hook("Betty_Life_evening", "Betty_Life_none", scene="global", label="steve_visit2")
    $ move_object("Betty", scene="empty")

    $ add_hook("Gates", "ep24_quests_steve14", scene="street_house_gate", label=["steve_visit2", "house_exit_block"])
    $ map_enabled = False

#    call miniMapAddDisabled(name):
#    call miniMapRemoveDisabled(name):

    $ basementBedSkipUntilFridayEnabled = False
    $ skipDaysInterrupted = True
    call ep24_dialogues3_steve10() from _call_ep24_dialogues3_steve10
#    $ cloth = "Governess"
#    $ cloth_type = "Governess"
#    call change_scene("floor1", "Fade_long", False)
    $ rooms_clean_list_exclude = ["living_room"]
    $ move_object("Ralph", scene="living_room")
#    $ livingRoomRalphSuffix = "_Sleeping"
    call living_room_init_additional1() from _call_living_room_init_additional1
    $ add_hook("Teleport_LivingRoom", "ep24_dialogues3_steve10_enter_room2", scene="floor1", label="steve_visit2")
    $ add_hook("Teleport_LivingRoom", "ep24_dialogues3_steve10_enter_room1", scene="floor1", label="steve_visit2", priority=300)

    $ add_hook("open", "ep24_quests_steve15", scene="floor1", label="steve_visit2a")
    $ add_hook("enter_scene", "ep24_quests_steve16", scene="floor1", label="steve_visit2a")
    $ add_hook("basement_monica_before_nap", "ep24_quests_steve18", scene="global", label="steve_visit2_nap") # В пятницу вечером также запускаем сцену с Бетти о приходе Стива
    $ monicaLastCleaningOfferedDay = day # Отменяем уборку сегодня
    $ add_cleaning(True)
    return


#    $ add_hook("map_teleport", "ep24_quests_steve6", scene="global", label="steve_visit1a")
#    $ add_hook("enter_scene", "ep24_quests_steve6", scene="basement_bedroom1", label="steve_visit1a")
#    $ add_hook("enter_scene", "ep24_quests_steve6", scene="basement_bedroom2", label="steve_visit1a")
    $ add_hook("exit_scene", "ep24_quests_steve6", scene="floor1", label="steve_visit1a")

    $ add_hook("change_time_evening", "ep24_quests_steve6b", scene="global", label="steve_visit2")
    $ add_hook("basement_monica_before_sleep", "ep24_quests_steve7", scene="global", label="steve_visit2")

    return

label ep24_quests_steve14:
    # Не выпускает Монику через ворота
    if act=="l":
        return
    call ep24_dialogues3_steve10_locked1() from _call_ep24_dialogues3_steve10_locked1
    return False

label ep24_quests_steve15:
    # Срабатывание на floor1, вторая часть визита Стива (зовут Монику в первый раз)
    $ remove_hook()
    $ add_objective("steve_maid", _("Обслуживать гостей"), c_orange, 15)
    call ep24_dialogues3_steve10a() from _call_ep24_dialogues3_steve10a
    $ add_hook("Teleport_LivingRoom", "ep24_quests_steve17", scene="floor1")
    return

label ep24_quests_steve16:
    # Зовут Монику
    $ remove_hook()
    call ep24_dialogues3_steve10a2() from _call_ep24_dialogues3_steve10a2
    return

label ep24_quests_steve17:
    # Моника входит в первый раз в гостиную
    $ remove_hook()
    call ep24_dialogues3_steve10b() from _call_ep24_dialogues3_steve10b
    $ autorun_to_object("floor1", "ep24_quests_steve19")
    $ add_hook("Teleport_LivingRoom", "ep24_quests_steve19a", scene="floor1", label="steve_visit2b")
    $ add_hook("enter_scene", "ep24_quests_steve17a", scene="kitchen", label="steve_visit2")
    $ add_hook("enter_scene", "ep24_quests_steve17a", scene="kitchen2", label="steve_visit2")
#    $ add_hook_multi("ep24_quests_steve20", scene="kitchen", label = "steve_visit2b", filter={"group":"environment"})
#    $ add_hook_multi("ep24_quests_steve20", scene="kitchen2", label = "steve_visit2b", filter={"group":"environment"})
    $ add_hook("enter_scene", "ep24_quests_steve20", scene="kitchen", label="steve_visit2b")
    $ add_hook("enter_scene", "ep24_quests_steve20", scene="kitchen2", label="steve_visit2b")


    call refresh_scene_fade() from _call_refresh_scene_fade_59
    return False

label ep24_quests_steve17a:
    mt "По крайней мере, сегодня я могу наесться, пока Бетти нет..."
    return False

label ep24_quests_steve18:
    # Блокировка отдыха
    help "Отдых отменен. В доме остались незавершенные события..."
    return False

label ep24_quests_steve19:
    # Комментарий после захода в гостиную первый раз
    call ep24_dialogues3_steve10b2() from _call_ep24_dialogues3_steve10b2

    return

label ep24_quests_steve19a:
    # Запрет на вход пока не выполнено распоряжение
    call ep24_dialogues3_steve10b4() from _call_ep24_dialogues3_steve10b4
    return False

label ep24_quests_steve20:
    if cloth != "Governess":
        return
    # Взять стаканы под виски на кухне
    call ep24_dialogues3_steve10b3() from _call_ep24_dialogues3_steve10b3
    if _return == False:
        call change_scene("floor1") from _call_change_scene_194
        return False
    $ remove_hook(label="steve_visit2b")

    call ep24_dialogues3_steve10c() from _call_ep24_dialogues3_steve10c
#    $ autorun_to_object("floor1", "ep24_quests_steve20c")
    call change_scene("floor1", "Fade_long") from _call_change_scene_195
    $ add_hook("open", "ep24_quests_steve20b", scene="floor1", label="steve_visit2a")
    call refresh_scene_fade() from _call_refresh_scene_fade_60
    return False

label ep24_quests_steve20a:
    # Моника комментирует, ее зовут
    call ep24_dialogues3_steve10c2() from _call_ep24_dialogues3_steve10c2
    return

label ep24_quests_steve20c:
    return

label ep24_quests_steve20b:
    # Срабатывание третьей части
    $ remove_hook()
    $ autorun_to_object("floor1", "ep24_quests_steve20a")
    call ep24_dialogues3_steve10c3() from _call_ep24_dialogues3_steve10c3
    $ add_hook("Teleport_LivingRoom", "ep24_quests_steve21", scene="floor1", label="steve_visit2c")
    return

label ep24_quests_steve21:
    # Моника снова заходит в гостиную
    $ remove_hook()
    call ep24_dialogues3_steve10d() from _call_ep24_dialogues3_steve10d
    $ add_hook("Teleport_LivingRoom", "ep24_quests_steve19a", scene="floor1", label="steve_visit2c")
    $ autorun_to_object("floor1", "ep24_quests_steve21a")

#    $ add_hook_multi("ep24_quests_steve22", scene="kitchen", label = "steve_visit2c", filter={"group":"environment"})
#    $ add_hook_multi("ep24_quests_steve22", scene="kitchen2", label = "steve_visit2c", filter={"group":"environment"})
    $ add_hook("enter_scene", "ep24_quests_steve22", scene="kitchen", label="steve_visit2c")
    $ add_hook("enter_scene", "ep24_quests_steve22", scene="kitchen2", label="steve_visit2c")

    call refresh_scene_fade_long() from _call_refresh_scene_fade_long
    return False

label ep24_quests_steve21a:
    # Моника комментирует приказ
    call ep24_dialogues3_steve10d2() from _call_ep24_dialogues3_steve10d2
    return

label ep24_quests_steve22:
    # Принести еду
    if cloth != "Governess":
        return
    call ep24_dialogues3_steve10d3() from _call_ep24_dialogues3_steve10d3
    if _return == False:
        call change_scene("floor1") from _call_change_scene_196
        return False
    $ remove_hook(label="steve_visit2c")
    call ep24_dialogues3_steve10e() from _call_ep24_dialogues3_steve10e

    $ remove_hook(label="steve_visit2_nap")
    $ add_hook("change_time_evening", "ep24_quests_steve23", scene="global", priority = 200)
    $ add_hook("Panties_Box", "ep24_dialogues3_steve10e3", scene="basement_laundry", label="steve_visit2")
    $ monicaLaundryBettyPantiesSelectNudeDisabled = True

    $ add_hook("BasementWardrobe", "ep24_quests_steve24b", scene="basement_bedroom1", label="steve_visit2")
    if monicaBettyPanties == False and monicaUnder == "Nude":
        $ autorun_to_object("basement_laundry", "ep24_quests_steve24a")
        call change_scene("basement_laundry", "Fade_long") from _call_change_scene_197
        return False

    call change_scene("floor1", "Fade_long") from _call_change_scene_198
    return False

label ep24_quests_steve23:
    # Сцена вечер, Ральф спит
    $ remove_hook()
    call ep24_dialogues3_steve10f() from _call_ep24_dialogues3_steve10f

    $ add_hook("before_open", "ep24_quests_steve24", scene="floor1_stairs", label="steve_catch1") # Переход ногами на лестницу из подвала
    $ add_hook("before_open", "ep24_quests_steve24", scene="bedroom1", label="steve_catch1")
    $ add_hook("before_open", "ep24_quests_steve24", scene="bedroom2", label="steve_catch1")
    $ add_hook("before_open", "ep24_quests_steve24", scene="bathroom_bath", label="steve_catch1")
    $ add_hook("before_open", "ep24_quests_steve24", scene="floor1", label="steve_catch1")
    $ add_hook("before_open", "ep24_quests_steve24", scene="floor2", label="steve_catch1")
    $ add_hook("before_open", "ep24_quests_steve24", scene="kitchen2", label="steve_catch1")
    $ add_hook("before_open", "ep24_quests_steve24", scene="street_house_main_yard", label="steve_catch1")
    $ add_hook("before_open", "ep24_quests_steve24", scene="basement_pool", label="steve_catch1")

    $ add_hook("basement_monica_before_sleep", "ep24_quests_steve18", scene="global", label="steve_visit2")
    call refresh_scene_fade_long() from _call_refresh_scene_fade_long_1
    return
# rooms_clean_list_exclude = []

label ep24_quests_steve24:
    # Стив ловит Монику
    $ remove_hook(label="steve_catch1")

    # Сцена Стива и Моники
    call ep24_dialogues3_steve10g() from _call_ep24_dialogues3_steve10g
    $ questLog(31, False)

    $ remove_hook(label="steve_visit2")
    $ remove_hook(label="steve_visit2a")
    $ remove_hook(label="steve_visit2b")
    $ remove_hook(label="steve_visit2c")
    $ monicaLaundryBettyPantiesSelectNudeDisabled = False

    $ move_object("Ralph", "living_room")

    $ remove_objective("steve_maid")
    $ map_enabled = True
    $ livingRoomRalphSuffix = "_Sleeping"
    $ add_hook("Ralph", "ep24_quests_steve26", scene="living_room", label="evening_time_temp", priority = 500) # Удалится с утра
    $ add_hook("change_time_day", "ep24_quests_steve25", scene="global")

    $ add_hook("enter_scene", "ep24_quests_steve27", scene="basement_bedroom2")
    call change_scene("basement_bedroom2", "Fade_long") from _call_change_scene_199
    return

label ep24_quests_steve24a:
    $ monicaUnder = "Panties"
    call ep24_dialogues3_steve10e2() from _call_ep24_dialogues3_steve10e2
    call ep22_Act_Images_monica_put_up_panties() from _call_ep22_Act_Images_monica_put_up_panties
    call refresh_scene_fade from _call_refresh_scene_fade_61
    return

label ep24_quests_steve24b:
    if act=="l":
        return
    call ep24_dialogues3_steve10e3() from _call_ep24_dialogues3_steve10e3
    return False

label ep24_quests_steve25:
    # Следующее утро
    $ remove_hook()
    if monicaHasSexWithSteveBasement == True:
        $ questLog(31, False)
        $ questLog(32, True)
        $ add_hook("DickSecretary_Dialogue1_Menu", "ep24_quests_steve28", scene="menu", label="dicksecretary_steve_money1", caption=_("Стив прислал деньги."), priority=95)
        $ add_hook("DickSecretary", "ep22_quests_Dick8a", scene="dick_office_secretary", label="dicksecretary_alternative_dialogue1")
        $ add_hook("basement_monica_after_sleep_dialogue", "ep24_quests_steve29", scene="global")
    $ add_hook("Teleport_Building", "ep24_quests_steve30", scene="street_steve_office", label="steve_office_blocked_update")
    $ add_hook("DickSecretary", "ep22_quests_Dick8a", scene="dick_office_secretary", label="dicksecretary_alternative_dialogue1")
    $ livingRoomRalphSuffix = ""
    $ basementBedSkipUntilFridayEnabled = True

    return

label ep24_quests_steve26:
    # Моника пытается говорить со Стивом в гостиной (спит)
    call ep24_dialogues3_steve10a1() from _call_ep24_dialogues3_steve10a1
    return False

label ep24_quests_steve27:
    $ remove_hook()
    # Комментарий Моники после секса со Стивом
    call ep24_dialogues3_steve10b1() from _call_ep24_dialogues3_steve10b1
    return

label ep24_quests_steve28:
    # Разговор с Викторией о том послал-ли Стив деньги
    call ep24_dialogues3_steve12() from _call_ep24_dialogues3_steve12
    if monicaAskedVictoriaAboutSteveMoney == False:
        $ questLog(32, False)
        $ questLog(33, True)

    $ monicaAskedVictoriaAboutSteveMoney = True
    call refresh_scene_fade() from _call_refresh_scene_fade_62
    return False

label ep24_quests_steve29:
    # Моника говорит с утра после секса со Стивом
    $ remove_hook()
    call ep24_dialogues3_steve11() from _call_ep24_dialogues3_steve11
    return False

label ep24_quests_steve30:
    # Вход в здание Стива
    if act=="l":
        return
    call ep24_dialogues3_steve13() from _call_ep24_dialogues3_steve13
    return False

label ep24_quests_steve31:
    # Включение блокировки фотосессий
    $ remove_hook()
    $ photoShootDisabledNextWeek = False
    $ add_hook("photoshoots_work_available_check", "ep24_quests_steve32", scene="global", label="steve_photosessions_block")
    $ add_hook_day("ep24_quests_steve33", week_day=6) # включаем в субботу
    return

label ep24_quests_steve32:
    # Блокировка фотосессий
    return False

label ep24_quests_steve33:
    # Выключение блокировки фотосессий
    $ remove_hook()
    $ remove_hook(label="steve_photosessions_block")
    return

#
