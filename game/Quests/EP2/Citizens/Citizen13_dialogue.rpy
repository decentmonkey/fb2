label citizen13_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_13_1
    if citizen13_offered_last_day == day:
        imgr Dial_Citizen_13_4
        citizen13 "Милая, давай в другой раз, я занят."
        return
    citizen13 "Ой, привет! Что у тебя, подруга?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen13_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen13_refuse_probability) > 0:
                imgr Dial_Citizen_13_2
                citizen13 "Кебаб? Фу...Ты разве не знаешь, они вредны для фигуры."
                m "Но никто же не заставляет тебя его покупать. Просто возьми флаер."
                citizen13 "А ты смешная. Ладно, я возьму один, только обещай мне, что ты не будешь есть эти противные кебабы."
                "Хотя ты знаешь, у них есть одно достоинство и ты наверное знаешь какое."
                m "?"
                imgr Dial_Citizen_13_3
                citizen13 "Глупенькая, ну конечно форма. На что они похожи?"
                label .loop1:
                    menu:
                        "На кебабы.":
                            imgl Dial_Monica_Sandwich_0
                            m "Не знаю... На кебабы."
                            imgr Dial_Citizen_13_4
                            citizen13 "Нууу...С тобой не интересно"
                            $ kebabWorkMonicaRefusedAmount += 1
                            return
                        "На пенис... (requires 30 corruption)" if corruption < 30:
                            jump .loop1
                        "На пенис..." if corruption >= 30:
                            $ kebabWorkHarassmentAmount +=1
                            imgl Dial_Monica_Sandwich_0
                            mt "Боже, что за извращенец?! Пожалуй, скажу то, что он хочет услышать."
                            m "Ну он немного напоминает пенис."
                            imgr Dial_Citizen_13_3
                            citizen13 "Дааа! Только я думаю, что совсем не немного. Я знал, что мы найдем общий язык."

                            imgr Dial_Citizen_13_2
                            imgl Dial_Monica_Sandwich_1
                            call reduce_flyers() from _call_reduce_flyers_6
                            citizen13 "Приятно было пообщаться."
                            return
            else:
                imgr Dial_Citizen_13_4
                citizen13 "Детка, мне совсем некуда его положить..."
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen13_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_13_1
    m "Привет! Ты меня помнишь?"
    imgr Dial_Citizen_13_3
    citizen13 "Кончно помню, подруга! Ты разносишь флаеры с рекламой этих ужасных кебабов."
    m "Ну да, иногда."
    mt "А он выглядит дружелюбно и, похоже, я ему не интересна."
    m "Не будет ли у тебя лишних денег?"
    citizen13 "А тебе зачем, подруга? Если нужна контрацептив, дак у меня есть!"
    mt "Да за кого он меня принимает?"
    m "Нет, мне нужна наличка."
    citizen13 "Ну для тебя у меня есть немного, но ты же знаешь, что ничего не делается просто так."
    m "Ты мог бы мне одолжить."
    citizen13 "Ха-ха-ха. Подруга, я похож на идиота?"
    citizen13 "А вообще знаешь, раз тебе так нужны деньги, у меня есть идея. Пошли."
     # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_200
    call pylonController(2, 1) from _call_pylonController_94
    with fadelong
    citizen13 "Вот мы и пришли. Вечером тут полно народу. А теперь..."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen13_dialogue_pilon_loop13:
    call pylonController(1, 1) from _call_pylonController_95
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_96
            citizen13 "Подруга, а что у тебя под футболкой?"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_97
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13

            call pylonController(3, 3) from _call_pylonController_98
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает сиськи
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_17
            call pylonController(3, 3) from _call_pylonController_99
            citizen13 "Прекрасно, я вижу форму!"
            call pylonController(3, 3) from _call_pylonController_100
            citizen13 "Не дурно!"
            call pylonController(3, 1) from _call_pylonController_101
            w
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen13_dialogue_pilon_loop13
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_102
            citizen13 "А что у тебя сзади? Покажи!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_103
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13
            call pylonController(4, 5) from _call_pylonController_104
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_18
            call pylonController(4, 5) from _call_pylonController_105
            # img показывает зад
            citizen13 "Оу, шикарная попка! Уж поверь, в этом я понимаю!"
            call pylonController(4, 5) from _call_pylonController_106

            citizen13 "Подруга, а шлепни себя по попке! Меня это заводит!"
            label citizen13_dialogue_pilon_loop13_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothAssSpankCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothAssSpankCorruptionRequired] corruption"
                        jump citizen13_dialogue_pilon_loop13_1
                    m "Ладно."
                    call pylonController(3, 1) from _call_pylonController_107
                    with fade
                    w
                    # добавить звук шлепка
                    sound snd_slap1
                    call showRandomImages(assSpankImages, 1) from _call_showRandomImages_19
                    call pylonController(3, 1) from _call_pylonController_108
                    citizen13 "Ух! Да, подруга, ты прямо огонь!"
                    $ store_citizen_action("AssClothSpank", 1)
                "Ну уж нет!":
                    call pylonController(3, 1) from _call_pylonController_109
                    m "Не собираюсь, и так достаточно."
                    citizen13 "Нууу...Ну пожалуйста?"
                    m "Нет. Ты и так видел многое."

            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen13_dialogue_pilon_loop13
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_110
            citizen13 "Дорогая, сделай пару оборотов на пилоне, очень хочется на это посмотреть."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_111
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_112
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages1, 4) from _call_showRandomImages_20
#            call pylonController(4, 5)
            citizen13 "Здорово, а ты молодец! Надо будет также попробовать."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_113
            with fade
            mt "Да уж, представляю что получится..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen13_dialogue_pilon_loop13
        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart3startsCompleted == True:
            call pylonController(4, 1) from _call_pylonController_114
            citizen13 "Прошлый раз ты меня обманула: не показала, что у тебя под футболкой. Давай теперь честно, мы же подруги."
            mt "Что он такое говорит? Он вообще нормальный?"
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_115
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            call pylonController(4, 5) from _call_pylonController_116
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикаснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_21
            call pylonController(4, 5) from _call_pylonController_117
            citizen13 "А тебе есть что показать! Когда нибудь у меня будут такие же!"
            call pylonController(4, 1) from _call_pylonController_118
            mt "Да не дай бог..."
            citizen13 "Подруга, а где ты такие сделала?"
            m "Что?! Они настоящие!"
            call pylonController(4, 5) from _call_pylonController_119
            citizen13 "Да?! Хорошо сохранилась, подруга!"
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen13_dialogue_pilon_loop13
        "Достаточно на сегодня.":
            $ earnedMoney = 0
            if showedBoobs == True or showedButt == True or showedDance == True or showedNakedBoobs == True:
                if showedBoobs == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedButt == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedDance == True:
                    $ earnedMoney += monicaWhoringClothDanceMoney
                if showedNakedBoobs == True:
                    $ earnedMoney += monicaWhoringNakedBoobsMoney
                call pylonController(2, 1) from _call_pylonController_120
                citizen13 "Славно потрудилась, подруга! Вот, держи."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_121
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_122
            citizen13 "Подруга, в следующий раз не халтурь."
            return False
    return
