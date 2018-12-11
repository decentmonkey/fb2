label Betty_Life_init:
    $ add_hook("change_time_day", "Betty_Life_day", scene="global")
    $ add_hook("change_time_evening", "Betty_Life_evening", scene="global")
    $ add_hook("Betty_Life_day", "Betty_Life_day1", scene="global")
    $ add_hook("Betty_Life_evening", "Betty_Life_evening1", scene="global")

    $ add_hook("Betty", "Betty_Life_Dialogue_Floor2", scene="floor2")
    $ add_hook("Betty", "Betty_Life_Dialogue_Bedroom1", scene="bedroom1")
    return

label Betty_Life_day:
    call process_hooks("Betty_Life_day", "global")
    return True


label Betty_Life_evening:
    call process_hooks("Betty_Life_evening", "global")
    return True

label Betty_Life_day1:
    call bettyGetTodayPanties()
    $ bedroom1_betty_suffix = ""
#    $ move_object("biff", "empty")
    $ rnd = rand(1,3)
    if rnd == 1 or rnd == 2:
        $ move_object("Betty", "floor2")
    if rnd == 3:
        $ move_object("Betty", "bedroom1")
    return

label Betty_Life_day1_lower:
    m "lower onetime"
    $ move_object("Betty", "floor2")
    return

label Betty_Life_evening1:
#    $ move_object("biff", "monica_office_cabinet")
    $ bedroom1_betty_suffix = bettyPantiesCurrent
    $ move_object("Betty", "bedroom1")
    #bedroom1_betty_suffix
    return

label Betty_Life_Monica_Cleaning_Start:
    return

label Betty_Life_Monica_Cleaning_End:
    return

label Betty_Life_Dialogue_Floor2:
    if act == "t":
        if cloth_type == "Governess":
            call cleaning_betty_comment1()
        else:
            call bettyDialogue3()
        return False
    return

label Betty_Life_Dialogue_Bedroom1:
    if act == "t":
        if day_time == "day":
            if cloth_type == "Governess":
                call bettyDialogue1()
            else:
                call bettyDialogue3()
            return False
        if day_time == "evening":
            call bettyDialogue2()
            return False
    return
