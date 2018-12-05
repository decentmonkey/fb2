label Betty_Life_init:
    $ add_hook("change_time_day", "Betty_Life_day", scene="global")
    $ add_hook("change_time_evening", "Betty_Life_evening", scene="global")
    $ add_hook("Betty_Life_day", "Betty_Life_Day1", scene="global")
    $ add_hook("Betty_Life_evening", "Betty_Life_evening1", scene="global")
    return

label Betty_Life_day:
    call process_hooks("Betty_Life_day1", "global")
    return True


label Betty_Life_evening:
    call process_hooks("Betty_Life_evening1", "global")
    return True

label Betty_Life_day1:
#    $ move_object("Beef", "empty")
    return

label Betty_life_evening1:
#    $ move_object("Beef", "monica_office_cabinet")
    return

label Betty_Life_Monica_Cleaning_Start:
    return

label Betty_Life_Monica_Cleaning_End:
    return
