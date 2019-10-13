label ep28_monica_bardie_init:
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_college_check_bardie_bedroom_clothes", scene="floor2", priority = 300, label="bedroom_bardie_check_cloth")
    $ add_hook("basement_monica_after_nap", "ep28_monica_bardie_init2", scene="global", once=True)
    return

label ep28_monica_bardie_init2: #next day
    call ep28_betty_college_init() # инициализируем линию Бетти по колледжу
    return

label ep28_monica_college_check_bardie_bedroom_clothes:
    if cloth_type != "Governess" and get_active_objects("Bardie", scene="bedroom_bardie") != False:
        call dialogue_betty_college_7_cloth()
        return False
    return
