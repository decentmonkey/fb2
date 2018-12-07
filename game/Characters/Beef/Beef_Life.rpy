default biffOnlyFridayEvening = False

label biff_Life_init:
    $ add_hook("change_time_day", "biff_Life_day", scene="global")
    $ add_hook("change_time_evening", "biff_Life_evening", scene="global")
    $ add_hook("biff_Life_day", "biff_Life_Day1", scene="global")
    $ add_hook("biff_Life_evening", "biff_Life_evening1", scene="global")
    return

label biff_Life_day:
    call process_hooks("biff_Life_day1", "global")
    return True


label biff_Life_evening:
    call process_hooks("biff_Life_evening1", "global")
    return True

label biff_Life_day1:
    $ move_object("biff", "empty")
    return

label biff_Life_evening1:
    if biffOnlyFridayEvening == True:
        if week_day == 5:
            $ move_object("biff", "monica_office_cabinet")
        return
    $ move_object("biff", "monica_office_cabinet")
    return
