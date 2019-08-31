default pubMonicaWorkingWaitress = False
default pubMonicaWorkedWaitressLastDay = 0
default pubMonicaWaitressTips = 0
default pubMonicaWaitressTipsStolen = False
default pubMonicaWaitressServedCustomersToday = 0
default pubMonicaWaitressServedCustomersTotal = 0
default pubMonicaWaitressWorkedDaysTotal = 0
default pubMonicaWaitressVisitorsServed = []

default pubMonicaWaitressClothBefore = ""
default pubMonicaWaitressClothTypeBefore = ""


label ep27_quests_pub_work1: # Моника спрашивает о повышении
    call ep27_dialogues7_pub1()
    music2 stop
    if _return == False or _return == -1:
        call change_scene("hostel_street", "Fade_long")
        return False
    # Моника принята на работу официанткой
    $ pubMonicaWorkingWaitress = True

    if day_time == "day":
        call process_hooks("Pub_Life_day", "global")
    else:
        call process_hooks("Pub_Life_evening", "global")

    $ questLog(52, True)
    call refresh_scene_fade_long()
    return False

label ep27_quests_pub_work2_begin: #Работать официанткой в Shiny Hole.
    if pubMonicaWorkedWaitressLastDay == day: # уже работала сегодня
        call ep27_dialogues7_pub3()
        call refresh_scene_fade()
        return False

    # Начинаем работу официанткой

    call ep27_dialogues7_pub4()
    music2 stop
    $ set_var("Monica", zorder = 1, scene="pub")
#    $ set_var("Monica", zorder = 200, scene="pub")
    call ep27_pub_visitors_init()
    
    $ pubMonicaWaitressVisitorsServed = []
    $ pubMonicaWaitressWorkedDaysTotal += 1
    $ pubMonicaWaitressTips = 0
    $ pubMonicaWaitressServedCustomersToday = 0
    $ pubMonicaWaitressClothTypeBefore = cloth_type
    $ pubMonicaWaitressClothBefore = cloth
    $ cloth = "Waitress"
    $ cloth_type = "Waitress"
    $ add_hook("Teleport_Hostel_Street", "ep27_quests_pub_work3_exit", scene="pub", label="working_waitress")
    $ add_hook("Bartender", "ep27_quests_pub_work4", scene="pub", label="working_waitress")
    $ add_hook("Bartender_Waitress", "ep27_quests_pub_work4", scene="pub", label="working_waitress")
    $ add_hook_multi("ep27_pub_visitors_click", scene="pub", label="working_waitress", filter={"group":"visitors"})
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 0.5
    call refresh_scene_fade_long()
    return

label ep27_quests_pub_work3_exit: # Моника пытается выйти из паба во время работы
    call ep27_dialogues7_pub6() # Вопрос о том, чтобы уйти без чаевых
    if _return == True:
        return False
    $ remove_hook(label="working_waitress")
    $ pubMonicaWaitressTipsStolen = True
    $ set_var("Monica", zorder = 200, scene="pub") # Делаем Монику снова спереди
    if pubMonicaWaitressTips > 0:
        $ autorun_to_object("ep27_dialogues7_pub6a", scene="hostel_street")
    $ cloth_type = pubMonicaWaitressClothTypeBefore
    $ cloth = pubMonicaWaitressClothBefore
    music2 stop
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    $ notif(_("Моника украла чаевые из Shiny Hole"))
    call change_scene("hostel_street", "Fade_long")
    return False

label ep27_quests_pub_work4: # Клик на барменов
    if act=="l":
        return
    call ep27_dialogues7_pub7a()
    if _return == False:
        return False
    # Заканчиваем работу самостоятельно
    call ep27_quests_pub_work5()
    return False

label ep27_quests_pub_work5:
    # Заканчиваем работу
    call ep27_dialogues7_pub7()
    music2 stop
    $ remove_hook(label="working_waitress")
    $ pubMonicaWorkedWaitressLastDay = day
    $ cloth_type = pubMonicaWaitressClothTypeBefore
    $ cloth = pubMonicaWaitressClothBefore
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    $ notif(_("Моника закончила смену официантки"))
    $ set_var("Monica", zorder = 200, scene="pub") # Делаем Монику снова спереди
    call change_scene("hostel_street", "Fade_long")
    return
