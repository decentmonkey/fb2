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

#    if moveRepeated == True or zoneRepeated == True: # движение не понравилось
    if zoneRepeated == True: # движение не понравилось
        if moveRepeated == True:
            $ notif(_("Моника делала это движение в прошлый раз"))
        if zoneRepeated == True:
            $ notif(_("Моника повторяет направления танца"))
        call pub_dance_dialogues_excitement_down(pose, zone)
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
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
        show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
        call pub_dance_dialogues_excitement_tips()
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
    $ notif_clean()

    return

label pub_dance_dialogues_excitement_up(pose, zone):
    python:
        idx1 = 0
        if zone == "up":
            idx1 = 0
        if zone == "side":
            idx1 = 1
        if zone == "down":
            idx1 = 2
        excitementAmount = excitementTableUp[pose-1][idx1]
        stage_Monica_Excitement_Last = stage_Monica_Excitement_Current
        stage_Monica_Excitement_Current += excitementAmount
        if stage_Monica_Excitement_Current > 100:
            stage_Monica_Excitement_Current = 100
    return

label pub_dance_dialogues_excitement_down(pose, zone):
    python:
        idx1 = 0
        if zone == "up":
            idx1 = 0
        if zone == "side":
            idx1 = 1
        if zone == "down":
            idx1 = 2
        excitementAmount = excitementTableDown[pose-1][idx1]
        stage_Monica_Excitement_Last = stage_Monica_Excitement_Current
        stage_Monica_Excitement_Current -= excitementAmount
        if stage_Monica_Excitement_Current < 0:
            stage_Monica_Excitement_Current = 0
    return

label pub_dance_dialogues_excitement_tips():
#    $ kupury = [1,2,5,10,20,50]
    $ kupury = [50,20,10,5,2,1]
    if stage_Monica_Excitement_Current <= 27:
        $ money = rand(3,5)
    else:
        if stage_Monica_Excitement_Current <= 54:
            $ money = rand(6,8)
        else:
            if stage_Monica_Excitement_Current <= 69:
                $ money = rand(10,12)
            else:
                if stage_Monica_Excitement_Current <= 84:
                    $ money = rand(18,22)
                else:
                    if stage_Monica_Excitement_Current <= 100:
                        $ money = rand(30, 40)

    python:
        kupury_out = []
        curMoney = 0

        while curMoney < money:
            flag1 = False
            for idx1 in range(0, len(kupury)):
                if kupury[idx1] < money-curMoney:
                    kupury_out.append(kupury[idx1])
                    curMoney += kupury[idx1]
                    flag1 = True
            if flag1 == False:
                curMoney = money
        shuffle(kupury_out)
        for kupura in kupury_out:
            money += kupura
    if money < 9:
        sound2 fx_coins_b3
    else:
        if money < 20:
            sound2 fx_coins_b2
        else:
            sound2 fx_coins_b1
    show screen poledance_coins(kupury_out)
    return
