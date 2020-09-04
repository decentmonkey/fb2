# BATTLE1
default stage_Molly_Excitement_Current = 0
default stage_Molly_Excitement_Last = 0

label pub_dance_battle1_Molly1:
    $ stage_Monica_Excitement_Current = 0
    $ stage_Monica_Excitement_Last = 0
    $ stage_Molly_Excitement_Current = 0
    $ stage_Molly_Excitement_Last = 0
    $ stage_achievements_list = []
    python:
        excitementTableUp = [
            [7,5,5], #1 - бар от 0 до 27 - 4 бакса чаевых
            [5,4,6], #2
            [5,5,7], #3 6 + 7 + 7 = до 20, 5 +4 +5 = от 14
            [8,7,11], #4 - бар от 27 до 54 - 7 баксов чаевых
            [12,8,9], #5
            [7,8,12], #6 от 18 до 30

            [10,9,15], #7 - бар от 54 до 69 - 11 баксов чаевых
            [15,10,15], #8 - бар от 69 до 84 - 20 баксов
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            [15,10,12], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
            # от 29 до 45
            # итого: от 61 до

            # Общее:
            # stage 1 - до 20
            # stage 2 - до 35 + 20 = 55
            # stage 3 - 55 + 45 = 100

            # максимум давать 20 баксов, т.е, 66
            #
        ]
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly1_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[0]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly1"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly1A = Movie(play="video/v_StripBattle1_Molly1A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly1A_end.jpg")
            show videov_StripBattle1_Molly1A
            pause 1.8
            hide videov_StripBattle1_Molly1A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly1A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(15)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers1 "ВАУ!!! Битва сучек!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly1A_end")
            jump pub_dance_battle1_Molly1_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly1B = Movie(play="video/v_StripBattle1_Molly1B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly1B_end.jpg")
            show videov_StripBattle1_Molly1B
            pause 1.8
            hide videov_StripBattle1_Molly1B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly1B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(15)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers3 "Охренительно, детка! Ты настоящая королева!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly1B_end")
            jump pub_dance_battle1_Molly1_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly1C = Movie(play="video/v_StripBattle1_Molly1C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly1C_end.jpg")
            show videov_StripBattle1_Molly1C
            pause 1.8
            hide videov_StripBattle1_Molly1C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly1C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(20)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers2 "Да, рыжая королева! Покрути жопой! Вот так! ДАААА!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly1C_end")
            jump pub_dance_battle1_Molly1_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
#    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Monica1:

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica1_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[1]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica1"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica1A = Movie(play="video/v_StripBattle1_Monica1A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica1A_end.jpg")
            show videov_StripBattle1_Monica1A
            pause 1.8
            hide videov_StripBattle1_Monica1A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica1A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            $ stage_achievements_list.append("v_StripBattle1_Monica1A_end")
            jump pub_dance_battle1_Monica1_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica1B = Movie(play="video/v_StripBattle1_Monica1B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica1B_end.jpg")
            show videov_StripBattle1_Monica1B
            pause 1.8
            hide videov_StripBattle1_Monica1B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica1B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers4 "Давай, раздевайся, крошка!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica1B_end")
            jump pub_dance_battle1_Monica1_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica1C = Movie(play="video/v_StripBattle1_Monica1C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica1C_end.jpg")
            show videov_StripBattle1_Monica1C
            pause 1.8
            hide videov_StripBattle1_Monica1C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica1C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers5 "Покажи нам свои сиськи!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica1C_end")
            jump pub_dance_battle1_Monica1_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
#    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()

    return

label pub_dance_battle1_Monica2:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica2_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[1]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica1"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica2A = Movie(play="video/v_StripBattle1_Monica2A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica2A_end.jpg")
            show videov_StripBattle1_Monica2A
            pause 1.8
            hide videov_StripBattle1_Monica2A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica2A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers1 "ВАААУ!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica2A_end")
            jump pub_dance_battle1_Monica2_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica2B = Movie(play="video/v_StripBattle1_Monica2B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica2B_end.jpg")
            show videov_StripBattle1_Monica2B
            pause 1.8
            hide videov_StripBattle1_Monica2B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica2B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers5 "Потряси своими сиськами для нас! Давай еще!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica2B_end")
            jump pub_dance_battle1_Monica2_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica2C = Movie(play="video/v_StripBattle1_Monica2C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica2C_end.jpg")
            show videov_StripBattle1_Monica2C
            pause 1.8
            hide videov_StripBattle1_Monica2C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica2C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(20)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers5 "Покажи нам свои сиськи!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica2C_end")
            jump pub_dance_battle1_Monica2_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Molly2:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly2_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[2]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly2"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly2A = Movie(play="video/v_StripBattle1_Molly2A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly2A_end.jpg")
            show videov_StripBattle1_Molly2A
            pause 1.8
            hide videov_StripBattle1_Molly2A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly2A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers4 "Королева Молли! Покажи класс!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly2A_end")
            jump pub_dance_battle1_Molly2_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly2B = Movie(play="video/v_StripBattle1_Molly2B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly2B_end.jpg")
            show videov_StripBattle1_Molly2B
            pause 1.8
            hide videov_StripBattle1_Molly2B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly2B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers3 "ДААА! Настоящая королева Shiny Hole!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly2B_end")
            jump pub_dance_battle1_Molly2_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly2C = Movie(play="video/v_StripBattle1_Molly2C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly2C_end.jpg")
            show videov_StripBattle1_Molly2C
            pause 1.8
            hide videov_StripBattle1_Molly2C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly2C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers2 "ДА! Покажи нам свою королевскую попку!!!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly2C_end")
            jump pub_dance_battle1_Molly2_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Monica3:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Monica3_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[3]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Monica3"
        if result == "up":
            scene black
            image videov_StripBattle1_Monica3A = Movie(play="video/v_StripBattle1_Monica3A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica3A_end.jpg")
            show videov_StripBattle1_Monica3A
            pause 1.8
            hide videov_StripBattle1_Monica3A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica3A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers5 "Вот она, королева! Охренительно, детка!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica3A_end")
            jump pub_dance_battle1_Monica3_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Monica3B = Movie(play="video/v_StripBattle1_Monica3B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica3B_end.jpg")
            show videov_StripBattle1_Monica3B
            pause 1.8
            hide videov_StripBattle1_Monica3B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica3B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers2 "ДААА! Точно! Она королева!" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica3B_end")
            jump pub_dance_battle1_Monica3_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Monica3C = Movie(play="video/v_StripBattle1_Monica3C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Monica3C_end.jpg")
            show videov_StripBattle1_Monica3C
            pause 1.8
            hide videov_StripBattle1_Monica3C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Monica3C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_monica(10)
            $ pub_dance_dialogues_set_excitement_molly(-10)
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers1 "Королева Shiny Hole! А где вторая голая попка?" # танцует Моника
            $ stage_achievements_list.append("v_StripBattle1_Monica3C_end")
            jump pub_dance_battle1_Monica3_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Molly3:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly3_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[4]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly3"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly3A = Movie(play="video/v_StripBattle1_Molly3A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly3A_end.jpg")
            show videov_StripBattle1_Molly3A
            pause 1.8
            hide videov_StripBattle1_Molly3A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly3A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std")
            sound3 men_scream2
            call pub_dance_battle_dialogues_react()
            customers4 "Вау!!! Какая горячая детка!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly3A_end")
            jump pub_dance_battle1_Molly3_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly3B = Movie(play="video/v_StripBattle1_Molly3B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly3B_end.jpg")
            show videov_StripBattle1_Molly3B
            pause 1.8
            hide videov_StripBattle1_Molly3B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly3B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std")
            sound3 men_scream1
            call pub_dance_battle_dialogues_react()
            customers3 "Покажи нам свою киску, крошка!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly3B_end")
            jump pub_dance_battle1_Molly3_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly3C = Movie(play="video/v_StripBattle1_Molly3C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly3C_end.jpg")
            show videov_StripBattle1_Molly3C
            pause 1.8
            hide videov_StripBattle1_Molly3C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly3C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            call pub_dance_battle_dialogues_applause("std")
            sound3 men_scream2
            call pub_dance_battle_dialogues_react()
            wclean
            $ stage_achievements_list.append("v_StripBattle1_Molly3C_end")
            jump pub_dance_battle1_Molly3_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return

label pub_dance_battle1_Molly4:
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = False
    $ loopCnt = 0

label pub_dance_battle1_Molly4_loop:
    if arrowUp == True or arrowSide == True or arrowDown == True:
        $ loopCnt += 1
        $ notif_clean()
        show screen poledance_battle()
        show screen love_bar_screen_battle(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current, stage_Molly_Excitement_Last, stage_Molly_Excitement_Current)
        $ result = ui.interact()
        hide screen poledance_battle
        hide screen poledance_camera_icon
        hide screen love_bar_screen_battle
        hide screen poledance_shoot
        hide screen poledance_coins
        if loopCnt == 1: # первый цикл
            fadeblack 0.5
            music musicList[musicOrder[5]]["loop"]
            pause 0.5
#        else:
#            img black_screen
#            with Dissolve(0.2)

        $ pose = "Molly4"
        if result == "up":
            scene black
            image videov_StripBattle1_Molly4A = Movie(play="video/v_StripBattle1_Molly4A.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly4A_end.jpg")
            show videov_StripBattle1_Molly4A
            pause 1.8
            hide videov_StripBattle1_Molly4A
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly4A_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-15)
            sound3 men_scream5
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers5 "ДААААААА!" # танцует Молли
            customers4 "МОЛЛИ, КРОШКА, ТЫ ЭТО СДЕЛАЛАААААА!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly4A_end")
            jump pub_dance_battle1_Molly4_loop

        if result == "side":
            scene black
            image videov_StripBattle1_Molly4B = Movie(play="video/v_StripBattle1_Molly4B.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly4B_end.jpg")
            show videov_StripBattle1_Molly4B
            pause 1.8
            hide videov_StripBattle1_Molly4B
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly4B_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-15)
            sound3 men_scream4
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers3 "МОЯ КОРОЛЕВА!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly4B_end")
            jump pub_dance_battle1_Molly4_loop

        if result == "down":
            scene black
            image videov_StripBattle1_Molly4C = Movie(play="video/v_StripBattle1_Molly4C.mkv", fps=20, loop=False, image="/images/Slides/v_StripBattle1_Molly4C_end.jpg")
            show videov_StripBattle1_Molly4C
            pause 1.8
            hide videov_StripBattle1_Molly4C
            show screen poledance_shoot("/images/Slides/v_StripBattle1_Molly4C_end.jpg")
            wclean
            $ pub_dance_dialogues_set_excitement_molly(10)
            $ pub_dance_dialogues_set_excitement_monica(-10)
            sound3 men_scream3
            call pub_dance_battle_dialogues_applause("std")
            call pub_dance_battle_dialogues_react()
            customers2 "ДААА! КОРОЛЕВА SHINY HOLE!" # танцует Молли
            customers1 "ВАААААУ!" # танцует Молли
            $ stage_achievements_list.append("v_StripBattle1_Molly4C_end")
            jump pub_dance_battle1_Molly4_loop
    hide screen poledance_battle
    hide screen poledance_camera_icon
    hide screen love_bar_screen_battle
    hide screen poledance_shoot
    hide screen poledance_coins
    $ pub_dance_dialogues_fix_excitement()
    return




# BATTLE 2

label pub_dance_battle1_Molly5:
    music musicList[musicOrder[0]]["loop"]
    return

label pub_dance_battle1_Monica5:
    music musicList[musicOrder[1]]["loop"]
    return

label pub_dance_battle1_Monica6:
    music musicList[musicOrder[1]]["loop"]
    return

label pub_dance_battle1_Molly6:
    music musicList[musicOrder[2]]["loop"]
    return


label pub_dance_battle1_Monica7:
    music musicList[musicOrder[3]]["loop"]
    return

label pub_dance_battle1_Molly7:
    music musicList[musicOrder[4]]["loop"]

    return

label pub_dance_battle1_Molly8:
    music musicList[musicOrder[5]]["loop"]
    return


label pub_dance_battle1_Monica8:
    music musicList[musicOrder[6]]["loop"]
    return

label pub_dance_battle1_Monica9:
    music musicList[musicOrder[6]]["loop"]
    return





#
