default bardieStage = 0

label Bardie_Life_day:
#    $ move_object("Beef", "empty")
    if bardieStage == 0:
        $ rand1 = rand(1,2)
        if rand1 == 1:
            $ move_object("Bardie", "street_house_main_yard") #во дворе
        if rand1 == 2:
            $ move_object("Bardie", "bedroom_bardie") #в своей комнате

    return

label Bardie_Life_evening:
#    $ move_object("Beef", "monica_office_cabinet")
    if bardieStage == 0:
        $ move_object("Bardie", "bedroom_bardie")
    return

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
    return
