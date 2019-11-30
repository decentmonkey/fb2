default stageMusicControlEnabled = False # включено-ли произвольное управление музыкой
default stageMusicMode = 0 # 0 - последовательно, 1 - случайно, 2 - произвольная музыка
default stageLastMusic = 1 # индекс последней игравшей музыки
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
            {"intro":"track3_intro", "loop":"track3"},
            {"intro":"track4_intro", "loop":"track4"},
            {"intro":"track5_intro", "loop":"track5"},
            {"intro":"track6_intro", "loop":"track6"},
            {"intro":"track7_intro", "loop":"track7"},
            {"intro":"track8_intro", "loop":"track8"},
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
    music stageCurrentMusicIntro
    call pub_dance_dialogues_start_dancing() # Комментарий при начале танца


    $ shotsTotalAmount = 27
    $ stage_Monica_shoots_array_current = []

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
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_A1 = Movie(play="video/v_Monica_Strip_A1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A1_end.jpg")
        show videov_Monica_Strip_A1
        pause 1.8
        img black_screen
        w
        show screen atl_test1()
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_A2 = Movie(play="video/v_Monica_Strip_A2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A2_end.jpg")
        show videov_Monica_Strip_A2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_A3 = Movie(play="video/v_Monica_Strip_A3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_A3_end.jpg")
        show videov_Monica_Strip_A3
        #pause 1.8
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
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_B1 = Movie(play="video/v_Monica_Strip_B1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B1_end.jpg")
        show videov_Monica_Strip_B1
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_B2 = Movie(play="video/v_Monica_Strip_B2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B2_end.jpg")
        show videov_Monica_Strip_B2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_B3 = Movie(play="video/v_Monica_Strip_B3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_B3_end.jpg")
        show videov_Monica_Strip_B3
        #pause 1.8
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
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_C1 = Movie(play="video/v_Monica_Strip_C1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C1_end.jpg")
        show videov_Monica_Strip_C1
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_C2 = Movie(play="video/v_Monica_Strip_C2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C2_end.jpg")
        show videov_Monica_Strip_C2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_C3 = Movie(play="video/v_Monica_Strip_C3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_C3_end.jpg")
        show videov_Monica_Strip_C3
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)


    menu:
        "Снять корсет.":
            pass
        "Завершить танец.":
            jump pub_dance1_stage_stop

    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    music stop
    img black_screen
    with diss
    pause 1.0
    show screen photoshot_screen()
    if pubDanceCount%3 == 0:
        scene black
        image videov_Monica_Strip_Undress1A = Movie(play="video/v_Monica_Strip_Undress1A.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1A_end.jpg")
        show videov_Monica_Strip_Undress1A
        sound snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        #pause 1.8
        wclean
    if pubDanceCount%3 == 1:
        scene black
        image videov_Monica_Strip_Undress1B = Movie(play="video/v_Monica_Strip_Undress1B.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1B_end.jpg")
        show videov_Monica_Strip_Undress1B
        sound snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        #pause 1.8
        wclean
    if pubDanceCount%3 == 2:
        scene black
        image videov_Monica_Strip_Undress1C = Movie(play="video/v_Monica_Strip_Undress1C.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_Undress1C_end.jpg")
        show videov_Monica_Strip_Undress1C
        sound snd_applause_undress1
        pause 0.7
        hide screen photoshot_screen
        #pause 1.8
        wclean

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
    $ result = ui.interact()
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    music stageCurrentMusicLoop
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_D1 = Movie(play="video/v_Monica_Strip_D1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D1_end.jpg")
        show videov_Monica_Strip_D1
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_D2 = Movie(play="video/v_Monica_Strip_D2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D2_end.jpg")
        show videov_Monica_Strip_D2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_D3 = Movie(play="video/v_Monica_Strip_D3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_D3_end.jpg")
        show videov_Monica_Strip_D3
        #pause 1.8
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
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_E1 = Movie(play="video/v_Monica_Strip_E1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E1_end.jpg")
        show videov_Monica_Strip_E1
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_E2 = Movie(play="video/v_Monica_Strip_E2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E2_end.jpg")
        show videov_Monica_Strip_E2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_E3 = Movie(play="video/v_Monica_Strip_E3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_E3_end.jpg")
        show videov_Monica_Strip_E3
        #pause 1.8
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
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_F1 = Movie(play="video/v_Monica_Strip_F1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F1_end.jpg")
        show videov_Monica_Strip_F1
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_F2 = Movie(play="video/v_Monica_Strip_F2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F2_end.jpg")
        show videov_Monica_Strip_F2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_F3 = Movie(play="video/v_Monica_Strip_F3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_F3_end.jpg")
        show videov_Monica_Strip_F3
        #pause 1.8
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
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_G1 = Movie(play="video/v_Monica_Strip_G1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G1_end.jpg")
        show videov_Monica_Strip_G1
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_G2 = Movie(play="video/v_Monica_Strip_G2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G2_end.jpg")
        show videov_Monica_Strip_G2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_G3 = Movie(play="video/v_Monica_Strip_G3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_G3_end.jpg")
        show videov_Monica_Strip_G3
        #pause 1.8
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
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_H1 = Movie(play="video/v_Monica_Strip_H1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H1_end.jpg")
        show videov_Monica_Strip_H1
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_H2 = Movie(play="video/v_Monica_Strip_H2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H2_end.jpg")
        show videov_Monica_Strip_H2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_H3 = Movie(play="video/v_Monica_Strip_H3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_H3_end.jpg")
        show videov_Monica_Strip_H3
        #pause 1.8
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
    hide screen poledance
    hide screen poledance_camera_icon
    hide screen love_bar_screen
    if result == "stop":
        jump pub_dance1_stage_stop
    if result == "up":
        scene black
        image videov_Monica_Strip_I1 = Movie(play="video/v_Monica_Strip_I1.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I1_end.jpg")
        show videov_Monica_Strip_I1
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "side":
        scene black
        image videov_Monica_Strip_I2 = Movie(play="video/v_Monica_Strip_I2.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I2_end.jpg")
        show videov_Monica_Strip_I2
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)
    if result == "down":
        scene black
        image videov_Monica_Strip_I3 = Movie(play="video/v_Monica_Strip_I3.mkv", fps=25, loop=False, image="/images/Slides/v_Monica_Strip_I3_end.jpg")
        show videov_Monica_Strip_I3
        #pause 1.8
        wclean
        call pub_dance_dialogues_react(pose, result)


    m "here"
    return

label pub_dance1_stage_stop:
    # Прерывание танца
    jump pub_dance1_stage_end

label pub_dance1_stage_end:
    music stop
    $ stage_Monica_last_shoots_array = stage_Monica_shoots_array_current
    return

label pub_dance_stage_flash:
    show screen photoshot_screen()
    pause 0.7
    hide screen photoshot_screen
    return
