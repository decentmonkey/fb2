label Melanie_Life_init:
    $ add_hook("change_time_day", "Melanie_Life_day", scene="global")
    $ add_hook("change_time_evening", "Melanie_Life_evening", scene="global")
    $ add_hook("Melanie_Life_day", "Melanie_Life_day1", scene="global")
    $ add_hook("Melanie_Life_evening", "Melanie_Life_evening1", scene="global")
    return

label Melanie_Life_day:
    call process_hooks("Melanie_Life_day", "global")
    return True

label Melanie_Life_evening:
    call process_hooks("Melanie_Life_evening", "global")
    return True

label Melanie_Life_day1:
    $ move_object("Melanie", "monica_office_photostudio")
    return
label Melanie_Life_evening1:
    $ move_object("Melanie", "empty")
    return
