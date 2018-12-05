label Ralph_Life_init:
    $ add_hook("change_time_day", "Ralph_Life_day", scene="global")
    $ add_hook("change_time_evening", "Ralph_Life_evening", scene="global")
    $ add_hook("Ralph_Life_day", "Ralph_Life_Day1", scene="global")
    $ add_hook("Ralph_Life_evening", "Ralph_Life_evening1", scene="global")
    return

label Ralph_Life_day:
    call process_hooks("Ralph_Life_day1", "global")
    return True


label Ralph_Life_evening:
    call process_hooks("Ralph_Life_evening1", "global")
    return True

label Ralph_Life_day1:
#    $ move_object("Beef", "empty")
    return

label Ralph_Life_evening1:
#    $ move_object("Beef", "monica_office_cabinet")
    return

label Ralph_Life_Monica_Cleaning_Start:
    return

label Ralph_Life_Monica_Cleaning_End:
    return
