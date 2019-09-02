label ep27_police1_init:
    $ add_hook("Building", "ep27_police2_enter", scene="street_police", label="police_quest1")
    return


label ep27_police2_enter: #вход в здание полиции
    if act=="l":
        return
    if day_time == "evening": # Вечером не заходим
        call ep27_dialogues_marcus1_1b()
        return False
    if cloth != "CasualDress1":
        call ep27_dialogues_marcus1_1c()
        return False
    call ep27_dialogues_marcus1_1a()
    if _return == False:
        return False
    $ autorun_to_object("ep27_dialogues_marcus1_1", scene="police_entrance")
    $ add_hook("Reception", "ep27_police2_reception_dialogue", scene="police_entrance", label="police_entrance_dialogue1")
    $ add_hook("Teleport_Inside", "ep27_police2_reception_dialogue", scene="police_entrance", label="police_entrance_dialogue1")
    $ set_var("Reception", actions="lt", scene="police_entrance")
    return

label ep27_police2_reception_dialogue: # Разговор в проходной (начало квеста)
    if act=="l" and obj_name != "Teleport_Inside":
        call ep27_dialogues_marcus1_1d()
        return
    call ep27_dialogues_marcus1_2() # Приходит Детектив
    if _return == False:
        $ autorun_to_object("ep27_dialogues_marcus1_1d", scene="street_police")
        call change_scene("street_police", "Fade_long")
        return False
    $ remove_hook(label="police_entrance_dialogue1")
    $ set_var("Reception", actions="l", scene="police_entrance")

    call ep27_dialogues_marcus1_3() # Входят в тюрьму
    call ep27_dialogues_marcus1_4() # Входят в камеру
    call ep27_dialogues_marcus1_5() # Моника в камере


    call ep27_dialogues_marcus1_9() # Боб
    call ep27_dialogues_marcus1_11()
    return False
