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
    $ questLog(52, True)
    call refresh_scene_fade()
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
    call refresh_scene_fade()
    return
