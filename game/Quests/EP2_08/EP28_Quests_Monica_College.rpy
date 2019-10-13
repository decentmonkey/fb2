default ep28_monica_eric_meeting_completed = False

label ep28_monica_bardie_init:
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_college_check_bardie_bedroom_clothes", scene="floor2", priority = 300, label="bedroom_bardie_check_cloth")
    $ add_hook("basement_monica_after_nap", "ep28_monica_bardie_init2", scene="global", once=True)
    return

label ep28_monica_bardie_init2: #next day
    call ep28_betty_college_init() # инициализируем линию Бетти по колледжу
    $ add_hook("Teleport_BedroomBardie", "ep28_monica_bardie_eric_meeting", scene="floor2", label="bardie_eric_meeting")
    return

label ep28_monica_college_check_bardie_bedroom_clothes:
    if cloth_type != "Governess" and get_active_objects("Bardie", scene="bedroom_bardie") != False:
        call dialogue_betty_college_7_cloth()
        return False
    return

label ep28_monica_bardie_eric_meeting: # Знакомство с Эриком (Моника заходит вечером к Барди)
    if get_active_objects("Bardie", scene="bedroom_bardie") == False:
        return

    $ ep28_monica_eric_meeting_completed = True
    return

label ep28_monica_college_bardie_eric_quest_check:

    return
