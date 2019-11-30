default pub_dance_dialogues_up_list = []
default pub_dance_dialogues_up_list2 = []
default pub_dance_dialogues_side_list = []
default pub_dance_dialogues_side_list2 = []
default pub_dance_dialogues_down_list = []
default pub_dance_dialogues_down_list2 = []

default pub_dance_dialogues_up_list3 = []
default pub_dance_dialogues_up_list4 = []
default pub_dance_dialogues_side_list3 = []
default pub_dance_dialogues_side_list4 = []
default pub_dance_dialogues_down_list3 = []
default pub_dance_dialogues_down_list4 = []

label pub_dance_dialogues_start_dancing:
    # Моника вышла на сцену
    if monicaDancingStage == 0:
        img 22901
        with fadelong
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call dialogue_5_dance_strip_4a()
        if rand1 == 2:
            call dialogue_5_dance_strip_4b()

    if monicaDancingStage == 1:
        if cloth == "StripOutfit1":
            img 22900
        if cloth == "StripOutfit2":
            img 22900
        with fadelong
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call dialogue_5_dance_strip_4c()
        if rand1 == 2:
            call dialogue_5_dance_strip_4d()

    if monicaDancingStage == 2:
        if cloth == "StripOutfit1":
            img 22902
        if cloth == "StripOutfit2":
            img 22902
        with fadelong
        $ rand1 = rand(1,2)
        if rand1 == 1:
            call dialogue_5_dance_strip_4e()
        if rand1 == 2:
            call dialogue_5_dance_strip_4f()
    return

label pub_dance_dialogues_react(pose, zone): # Реакция зала

    show screen poledance_camera_icon(stage_Monica_shoots_array)
    python:
        checkZoneKey = str(pose) + zone
        moveRepeated = False
        if checkZoneKey in stage_Monica_last_shoots_array:
            moveRepeated = True
        zoneRepeated = False
        if zone == stage_Monica_last_zone:
            zoneRepeated = True

        stage_Monica_shoots_array_current.append(checkZoneKey)
        stage_Monica_shoots_array.append(checkZoneKey)
        stage_Monica_last_zone = zone

    if moveRepeated == True or zoneRepeated == True: # движение не понравилось
        if moveRepeated == True:
            $ notif(_("Моника повторяет направления танца"))
        if zoneRepeated == True:
            $ notif(_("Моника делала это движение в прошлый раз"))
        call pub_dance_dialogues_excitement_down(pose, zone)
        show screen love_bar_screen(0.0, 0.4)
        $ idx = rand(1,4)
        $ crowdSound = "snd_crowd_uuu" + str(idx)
        sound crowdSound
        if zone == "up":
            if pose < 4:
                call dialogue_5_dance_strip_5a1()
            else:
                call dialogue_5_dance_strip_5d2()
        if zone == "side":
            if pose < 4:
                call dialogue_5_dance_strip_5b2()
            else:
                call dialogue_5_dance_strip_5e2()
        if zone == "down":
            if pose < 4:
                call dialogue_5_dance_strip_5c2()
            else:
                call dialogue_5_dance_strip_5f2()
    else:
        # Движение понравилось
        call pub_dance_dialogues_excitement_up(pose, zone)
        show screen love_bar_screen(0.0, 0.4)
        $ idx = rand(1,3)
        $ applauseSound = "snd_applause" + str(idx)
        sound applauseSound
        call pub_dance_stage_flash()
        if zone == "up":
            if pose < 4:
                call dialogue_5_dance_strip_5a()
            else:
                call dialogue_5_dance_strip_5d()
        if zone == "side":
            if pose < 4:
                call dialogue_5_dance_strip_5b()
            else:
                call dialogue_5_dance_strip_5e()
        if zone == "down":
            if pose < 4:
                call dialogue_5_dance_strip_5c()
            else:
                call dialogue_5_dance_strip_5f()


#    wclean

    return

label pub_dance_dialogues_excitement_up(pose, zone):

    return

label pub_dance_dialogues_excitement_down(pose, zone):
    return

label pub_dance_dialogues_excitement_tips():
    return
