default stageMusicControlEnabled = False # включено-ли произвольное управление музыкой
default stageMusicMode = 0 # 0 - последовательно, 1 - случайно, 2 - произвольная музыка
default stageLastMusic = -1 # индекс последней игравшей музыки
default stageCustomMusic = 0 # индекс произвольной музыки

default stageCurrentMusicIntro = False
default stageCurrentMusicLoop = False

default stage_Monica_shoots_array = []
default stage_Monica_shoots_array_current = []
default stage_Monica_last_shoots_array = []
default stage_Monica_last_zone = False

default stage_Monica_Excitement_Current = 0
default stage_Monica_Excitement_Last = 0

#monicaDancingStage

label pub_dance1_stage_start1:
    $ stageMusicControlEnabled = True
    music stop
    music2 stop
    call dialogue_5_dance_strip_scene_menu() # выбор музыки
    $ stage_Monica_Excitement_Current = 0
    $ stage_Monica_Excitement_Last = 0
    python:
        excitementTableUp = [
            [3,5,9], #1 - бар от 0 до 27 - 4 бакса чаевых
            [5,4,9], #2
            [9,4,5], #3
            [5,9,7], #4 - бар от 27 до 54 - 7 баксов чаевых
            [9,3,6], #5
            [6,7,9], #6

            [10,9,15], #7 - бар от 54 до 69 - 11 баксов чаевых
            [9,8,15], #8 - бар от 69 до 84 - 20 баксов
            [15,10,9], #9 - бар от 84 до 99 - 35 баксов (максимум 99 баксов, 30% - 29.7 баксов)
        ]
        excitementTableDown = [
            [2,2,2], #1
            [3,3,3], #2
            [4,4,4], #3
            [4,4,4], #4
            [5,5,5], #5
            [6,6,6], #6

            [7,7,7], #7
            [8,8,8], #8
            [9,9,9], #9
        ]
        musicList = [
            {"intro":"track1_intro", "loop":"track1"},
            {"intro":"track2_intro", "loop":"track2"},
            {"intro":"track7_intro", "loop":"track7"},
            {"intro":"track3_intro", "loop":"track3"},
            {"intro":"track4_intro", "loop":"track4"},
            {"intro":"track5_intro", "loop":"track5"},
            {"intro":"track8_intro", "loop":"track8"},
            {"intro":"track6_intro", "loop":"track6"},
        ]
        if stageMusicMode == 0:
            stageLastMusic += 1
            if stageLastMusic >= len(musicList):
                stageLastMusic = 0
        if stageMusicMode == 1:
            stageLastMusic = rand(1,len(musicList)) - 1
        if stageMusicMode == 2:
            stageLastMusic = stageCustomMusic
        stageCurrentMusicIntro = musicList[stageLastMusic]["intro"]
        stageCurrentMusicLoop = musicList[stageLastMusic]["loop"]

    music stop
    img black_screen
    with diss
    pause 2.0
    if cloth == "StripOutfit2":
        music stageCurrentMusicLoop
    else:
        music stageCurrentMusicIntro
    call pub_dance_dialogues_start_dancing() # Комментарий при начале танца


    $ shotsTotalAmount = 27
    $ stage_Monica_shoots_array_current = []

    if cloth == "StripOutfit2":
        jump pub_dance1_stage_start1_topless
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True

    #stage_Monica_shoots_array

    # Поза1
    # A
    $ pose = 1
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_A1 = Movie(play="video/v_Monica_Strip_A1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A1_end.jpg")
        show videov_Monica_Strip_A1
        pause 1.8
        hide videov_Monica_Strip_A1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_A2 = Movie(play="video/v_Monica_Strip_A2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A2_end.jpg")
        show videov_Monica_Strip_A2
        pause 1.8
        hide videov_Monica_Strip_A2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_A3 = Movie(play="video/v_Monica_Strip_A3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A3_end.jpg")
        show videov_Monica_Strip_A3
        pause 1.8
        hide videov_Monica_Strip_A3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_A3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # B
    $ pose = 2
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_B1 = Movie(play="video/v_Monica_Strip_B1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B1_end.jpg")
        show videov_Monica_Strip_B1
        pause 1.8
        hide videov_Monica_Strip_B1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_B2 = Movie(play="video/v_Monica_Strip_B2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B2_end.jpg")
        show videov_Monica_Strip_B2
        pause 1.8
        hide videov_Monica_Strip_B2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_B3 = Movie(play="video/v_Monica_Strip_B3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B3_end.jpg")
        show videov_Monica_Strip_B3
        pause 1.8
        hide videov_Monica_Strip_B3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_B3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # C
    $ pose = 3
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_C1 = Movie(play="video/v_Monica_Strip_C1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C1_end.jpg")
        show videov_Monica_Strip_C1
        pause 1.8
        hide videov_Monica_Strip_C1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_C2 = Movie(play="video/v_Monica_Strip_C2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C2_end.jpg")
        show videov_Monica_Strip_C2
        pause 1.8
        hide videov_Monica_Strip_C2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_C3 = Movie(play="video/v_Monica_Strip_C3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C3_end.jpg")
        show videov_Monica_Strip_C3
        pause 1.8
        hide videov_Monica_Strip_C3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_C3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    $ menu_corruption = [monicaPutStripClothToplessStage]
    menu:
        "Снять корсет.":
            if pubDanceCount < monicaDanceAmountToTopless or len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToTopless:
                hide screen poledance
                hide screen poledance_camera_icon
                hide screen love_bar_screen
                hide screen poledance_shoot
                hide screen poledance_coins
                call dialogue_5_dance_strip_4g()
                jump pub_dance1_stage_end
            call dialogue_5_dance_strip_4h()
        "Завершить танец.":
            jump pub_dance1_stage_stop

    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    music pub_noise1
#    music stop
    img black_screen
    with diss
    pause 1.0
    show screen photoshot_screen()
    if pubDanceCount%3 == 0:
        scene black
        image videov_Monica_Strip_Undress1A = Movie(play="video/v_Monica_Strip_Undress1A.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1A_end.jpg")
        show videov_Monica_Strip_Undress1A
        music2 snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        pause 2.1
        hide videov_Monica_Strip_Undress1A
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Undress1A_end.jpg")
        wclean
    if pubDanceCount%3 == 1:
        scene black
        image videov_Monica_Strip_Undress1B = Movie(play="video/v_Monica_Strip_Undress1B.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1B_end.jpg")
        show videov_Monica_Strip_Undress1B
        music2 snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        pause 2.1
        hide videov_Monica_Strip_Undress1B
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Undress1B_end.jpg")
        wclean
    if pubDanceCount%3 == 2:
        scene black
        image videov_Monica_Strip_Undress1C = Movie(play="video/v_Monica_Strip_Undress1C.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1C_end.jpg")
        show videov_Monica_Strip_Undress1C
        music2 snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        pause 2.1
        hide videov_Monica_Strip_Undress1C
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_Undress1C_end.jpg")
        wclean
label pub_dance1_stage_start1_topless:
    $ monicaDancingTopless = True
    if monicaDancingStage < 1:
        $ monicaDancingStage = 1
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # D
    $ pose = 4
    show screen love_bar_screen(stage_Monica_Excitement_Last, stage_Monica_Excitement_Current)
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    music2 stop
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    music stop
    img black_screen
    with diss
    pause 1.0
    music stageCurrentMusicLoop
    if result == "up":
        scene black
        image videov_Monica_Strip_D1 = Movie(play="video/v_Monica_Strip_D1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D1_end.jpg")
        show videov_Monica_Strip_D1
        pause 1.8
        hide videov_Monica_Strip_D1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_D1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_D2 = Movie(play="video/v_Monica_Strip_D2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D2_end.jpg")
        show videov_Monica_Strip_D2
        pause 1.8
        hide videov_Monica_Strip_D2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_D2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_D3 = Movie(play="video/v_Monica_Strip_D3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D3_end.jpg")
        show videov_Monica_Strip_D3
        pause 1.8
        hide videov_Monica_Strip_D3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_D3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # E
    $ pose = 5
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_E1 = Movie(play="video/v_Monica_Strip_E1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E1_end.jpg")
        show videov_Monica_Strip_E1
        pause 1.8
        hide videov_Monica_Strip_E1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_E2 = Movie(play="video/v_Monica_Strip_E2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E2_end.jpg")
        show videov_Monica_Strip_E2
        pause 1.8
        hide videov_Monica_Strip_E2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_E3 = Movie(play="video/v_Monica_Strip_E3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E3_end.jpg")
        show videov_Monica_Strip_E3
        pause 1.8
        hide videov_Monica_Strip_E3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_E3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # F
    $ pose = 6
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_F1 = Movie(play="video/v_Monica_Strip_F1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F1_end.jpg")
        show videov_Monica_Strip_F1
        pause 1.8
        hide videov_Monica_Strip_F1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_F2 = Movie(play="video/v_Monica_Strip_F2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F2_end.jpg")
        show videov_Monica_Strip_F2
        pause 1.8
        hide videov_Monica_Strip_F2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_F3 = Movie(play="video/v_Monica_Strip_F3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F3_end.jpg")
        show videov_Monica_Strip_F3
        pause 1.8
        hide videov_Monica_Strip_F3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_F3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # G
    $ pose = 7
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    if len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
        call dialogue_5_dance_strip_4k()
        jump pub_dance1_stage_end
    if monicaDancingStage < 2:
        $ monicaDancingStage = 2

    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_G1 = Movie(play="video/v_Monica_Strip_G1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G1_end.jpg")
        show videov_Monica_Strip_G1
        pause 1.8
        hide videov_Monica_Strip_G1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_G1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_G2 = Movie(play="video/v_Monica_Strip_G2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G2_end.jpg")
        show videov_Monica_Strip_G2
        pause 1.8
        hide videov_Monica_Strip_G2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_G2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_G3 = Movie(play="video/v_Monica_Strip_G3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G3_end.jpg")
        show videov_Monica_Strip_G3
        pause 1.8
        hide videov_Monica_Strip_G3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_G3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # H
    $ pose = 8
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_H1 = Movie(play="video/v_Monica_Strip_H1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H1_end.jpg")
        show videov_Monica_Strip_H1
        pause 1.8
        hide videov_Monica_Strip_H1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_H2 = Movie(play="video/v_Monica_Strip_H2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H2_end.jpg")
        show videov_Monica_Strip_H2
        pause 1.8
        hide videov_Monica_Strip_H2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_H3 = Movie(play="video/v_Monica_Strip_H3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H3_end.jpg")
        show videov_Monica_Strip_H3
        pause 1.8
        hide videov_Monica_Strip_H3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_H3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True
    $ arrowStop = True
    # Поза1
    # I
    $ pose = 9
    show screen poledance_camera_icon(stage_Monica_shoots_array)
    show screen poledance()
    $ result = ui.interact()
    if result == "stop":
        jump pub_dance1_stage_stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    if result == "up":
        scene black
        image videov_Monica_Strip_I1 = Movie(play="video/v_Monica_Strip_I1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I1_end.jpg")
        show videov_Monica_Strip_I1
        pause 1.8
        hide videov_Monica_Strip_I1
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I1_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_I2 = Movie(play="video/v_Monica_Strip_I2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I2_end.jpg")
        show videov_Monica_Strip_I2
        pause 1.8
        hide videov_Monica_Strip_I2
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I2_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_I3 = Movie(play="video/v_Monica_Strip_I3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I3_end.jpg")
        show videov_Monica_Strip_I3
        pause 1.8
        hide videov_Monica_Strip_I3
        show screen poledance_shoot("/images/Slides/v_Monica_Strip_I3_end.jpg")
        wclean
        call pub_dance_dialogues_react(pose, result)

    jump pub_dance1_stage_end

label pub_dance1_stage_stop:
    # Прерывание танца
    call dialogue_5_dance_strip_4m()
    jump pub_dance1_stage_end

label pub_dance1_stage_end:
    music stop
    music2 stop
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    hide screen poledance_shoot
    hide screen poledance_coins
    img black_screen
    with diss
    pause 1.0
    $ stage_Monica_last_shoots_array = stage_Monica_shoots_array_current
    return

label pub_dance_stage_flash:
    show screen photoshot_screen()
    pause 0.7
    hide screen photoshot_screen
    return

transform coin_appear1:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

transform coin_appear2:
    pause 0.1
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear3:
    pause 0.2
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear4:
    pause 0.3
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear5:
    pause 0.4
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear6:
    pause 0.5
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform coin_appear7:
    pause 0.6
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
