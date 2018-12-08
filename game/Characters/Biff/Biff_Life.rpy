default biffOnlyFridayEvening = False

label Biff_Life_init:
    $ add_hook("change_time_day", "Biff_Life_day", scene="global")
    $ add_hook("change_time_evening", "Biff_Life_evening", scene="global")
    $ add_hook("Biff_Life_day", "Biff_Life_day1", scene="global")
    $ add_hook("Biff_Life_evening", "Biff_Life_evening1", scene="global")
    return

label Biff_Life_day:
    call process_hooks("Biff_Life_day", "global")
    return True


label Biff_Life_evening:
    call process_hooks("Biff_Life_evening", "global")
    return True

label Biff_Life_day1:
    $ move_object("Biff", "empty")
    return

label Biff_Life_evening1:
    if biffOnlyFridayEvening == True:
        if week_day == 5:
            $ move_object("Biff", "monica_office_cabinet")
        return
    $ move_object("Biff", "monica_office_cabinet")
    return
