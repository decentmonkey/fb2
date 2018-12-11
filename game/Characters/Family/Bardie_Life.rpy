default bardieStage = 0

label Bardie_Life_init:
    $ add_hook("change_time_day", "Bardie_Life_day", scene="global")
    $ add_hook("change_time_evening", "Bardie_Life_evening", scene="global")
    $ add_hook("Bardie_Life_day", "Bardie_Life_Day1", scene="global")
    $ add_hook("Bardie_Life_evening", "Bardie_Life_evening1", scene="global")

    return

label Bardie_Life_day:
    call process_hooks("Bardie_Life_day", "global") from _call_process_hooks_6
    return True

label Bardie_Life_Day1:
#    $ move_object("biff", "empty")
    if bardieStage == 0:
        $ rand1 = rand(1,2)
        if rand1 == 1:
            $ move_object("Bardie", "street_house_main_yard") #во дворе
        if rand1 == 2:
            $ move_object("Bardie", "bedroom_bardie") #в своей комнате

    return

label Bardie_Life_evening:
    call process_hooks("Bardie_Life_evening", "global") from _call_process_hooks_7
    return True

label Bardie_Life_evening1:
#    $ move_object("biff", "monica_office_cabinet")
    if bardieStage == 0:
        $ move_object("Bardie", "bedroom_bardie")
    return

label Bardie_Life_evening2: #Барди вечером преследует Монику у лестницы
    $ move_object("Bardie", "floor1_stairs")
    return False

label Bardie_Life_Monica_Cleaning_Start:
    if "bedroom_bardie" in rooms_dirty:
        $ move_object("Bardie", "bedroom_bardie")
        return
    if "floor1" in rooms_dirty:
        $ move_object("Bardie", "floor1")
        return
    if "bedroom_second" in rooms_dirty:
        $ move_object("Bardie", "bedroom_second")
        return

    return

label Bardie_Life_Monica_Cleaning_End:
    call Bardie_Life_day() from _call_Bardie_Life_day
    return
