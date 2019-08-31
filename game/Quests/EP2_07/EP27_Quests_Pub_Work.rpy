default pubMonicaWorkingWaitress = False
default pubMonicaWorkedWaitressLastDay = 0
default pubMonicaWaitressTips = 0

default pubMonicaWaitressClothBefore = ""
default pubMonicaWaitressClothTypeBefore = ""


label ep27_quests_pub_work1: # Моника спрашивает о повышении
    call ep27_dialogues7_pub1()
    if _return == False or _return == -1:
        call change_scene("hostel_street", "Fade_long")
        return False
    # Моника принята на работу официанткой
    $ pubMonicaWorkingWaitress = True

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
    $ pubMonicaWaitressTips = 0
    $ pubMonicaWaitressClothTypeBefore = cloth_type
    $ pubMonicaWaitressClothBefore = cloth
    $ cloth = "Waitress"
    $ cloth_type = "Waitress"
    $ add_hook("Teleport_Hostel_Street", "ep27_quests_pub_work3_exit", scene="pub", label="working_waitress")
    call refresh_scene_fade()
    return

label ep27_quests_pub_work3_exit: # Моника пытается выйти из паба во время работы
    call ep27_dialogues7_pub6() # Вопрос о том, чтобы уйти без чаевых

    return
