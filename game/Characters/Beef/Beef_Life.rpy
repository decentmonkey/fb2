default beefOnlyFridayEvening = False

label Beef_Life_init:
    $ add_hook("change_time_day", "Beef_Life_day", scene="global")
    $ add_hook("change_time_evening", "Beef_Life_evening", scene="global")
    $ add_hook("Beef_Life_day", "Beef_Life_Day1", scene="global")
    $ add_hook("Beef_Life_evening", "Beef_Life_evening1", scene="global")
    return

label Beef_Life_day:
    call process_hooks("Beef_Life_day1", "global")
    return True


label Beef_Life_evening:
    call process_hooks("Beef_Life_evening1", "global")
    return True

label Beef_Life_day1:
    $ move_object("Beef", "empty")
    return

label Beef_Life_evening1:
    if beefOnlyFridayEvening == True:
        if week_day == 5:
            $ move_object("Beef", "monica_office_cabinet")
        return
    $ move_object("Beef", "monica_office_cabinet")
    return
