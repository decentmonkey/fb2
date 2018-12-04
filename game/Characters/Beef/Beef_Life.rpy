default beefOnlyFridayEvening = False

label Beef_Life_day:
    $ move_object("Beef", "empty")
    return

label Beef_Life_evening:
    if beefOnlyFridayEvening == True:
        if week_day == 5:
            $ move_object("Beef", "monica_office_cabinet")
        return
    $ move_object("Beef", "monica_office_cabinet")
    return
