label Pub_Life_init: # Первое время, когда Моника только обнаруживает бар. Много народа
    $ add_hook("change_time_day", "Pub_Life_day", scene="global")
    $ add_hook("change_time_evening", "Pub_Life_evening", scene="global")
    $ add_hook("Pub_Life_day", "Pub_Life_day1", scene="global", label="pub_life")
    $ add_hook("Pub_Life_evening", "Pub_Life_evening1", scene="global", label="pub_life")

    # Сразу наполняем бар
    if day_time == "day":
        call Pub_Life_day()
    else:
        call Pub_Life_evening()
    return

label Pub_Life2_init: # Обычное наполнение бара
    $ remove_hook(label="pub_life")
    $ add_hook("Pub_Life_day", "Pub_Life_day2", scene="global", label="pub_life")
    $ add_hook("Pub_Life_evening", "Pub_Life_evening2", scene="global", label="pub_life")
    return

label Pub_Life_day:
    call process_hooks("Pub_Life_day", "global")
    return True

label Pub_Life_evening:
    call process_hooks("Pub_Life_evening", "global")
    return True

label Pub_Life_day1: # Первое время, когда Моника только обнаруживает бар. Много народа
    $ set_active("Bartender", True, scene="pub")
    $ set_active("Bartender_Waitress", True, scene="pub")
    $ set_active("Pub_StripteaseGirl1", False, scene="pub")
    $ set_active("Pub_StripteaseGirl2", True, scene="pub")
    call Pub_Visitors_RemoveAll()
    call Pub_Visitors_Add_Random(3,5)
    call Pub_Visitors_Full_Food() # у всех еда
    $ set_active("Pub_Visitor1", True, scene="pub") # эти посетители есть на кадре
    $ set_active("Pub_Visitor11", True, scene="pub")
    $ set_active("Pub_Visitor6", True, scene="pub")
    call Pub_Visitors_CheckStripLooking() # Если есть стриптизерши, то смотрят, иначе нет
    return
label Pub_Life_evening1:
    $ set_active("Bartender", True, scene="pub")
    $ set_active("Bartender_Waitress", True, scene="pub")
    $ set_active("Pub_StripteaseGirl1", False, scene="pub")
    $ set_active("Pub_StripteaseGirl2", True, scene="pub")

    call Pub_Visitors_RemoveAll()
    call Pub_Visitors_Add_Random(5,7)
    call Pub_Visitors_Full_Food() # Все посетители + у всех еда
    $ set_active("Pub_Visitor1", True, scene="pub") # эти посетители есть на кадре
    $ set_active("Pub_Visitor11", True, scene="pub")
    $ set_active("Pub_Visitor6", True, scene="pub")
    call Pub_Visitors_CheckStripLooking() # Если есть стриптизерши, то смотрят, иначе нет
    return


label Pub_Life_day2: # Обычное наполнение бара, все с едой
    $ set_active("Bartender", True, scene="pub")
    $ set_active("Bartender_Waitress", True, scene="pub")
    $ set_active("Pub_StripteaseGirl1", False, scene="pub")
    $ set_active("Pub_StripteaseGirl2", False, scene="pub")
    call Pub_Visitors_RemoveAll()
    call Pub_Visitors_Add_Random(2,4)
    call Pub_Visitors_Full_Food() # у всех еда
    call Pub_Visitors_CheckStripLooking() # Если есть стриптизерши, то смотрят, иначе нет
    return
label Pub_Life_evening2:
    $ set_active("Bartender", True, scene="pub")
    $ set_active("Bartender_Waitress", True, scene="pub")
    $ set_active("Pub_StripteaseGirl1", False, scene="pub")
    $ set_active("Pub_StripteaseGirl2", False, scene="pub")
    if day%2 == 0:
        $ set_active("Pub_StripteaseGirl1", True, scene="pub")
    else:
        $ set_active("Pub_StripteaseGirl2", True, scene="pub")

    call Pub_Visitors_RemoveAll()
    call Pub_Visitors_Add_Random(5,7)
    call Pub_Visitors_Full_Food() # Все посетители + у всех еда
    call Pub_Visitors_CheckStripLooking() # Если есть стриптизерши, то смотрят, иначе нет
    return
