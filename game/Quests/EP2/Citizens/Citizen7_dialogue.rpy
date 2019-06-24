label citizen7_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_7_1
    if citizen7_offered_last_day == day:
        imgr Dial_Citizen_7_4
        citizen7 "Я пытаюсь сосредоточиться на искусстве!"
        "Не отвлекайте меня!"
        return
    citizen7 "Да? Что Вы хотели?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen7_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            # Реально ли тут сделать картинку или что то в этом духе, как художник достает кисть и измеряет монику?
            img 7118
            w
            img 7117
            citizen7 "Прекрасно, очень хорошо! А теперь повернитесь!"
            img 7116
            w
            img 7117
            $ add_corruption(1, "monica_art_day_" + str(day))
            mt "Что вообще происходит?"
            # тут эффект, что художник подходит к монике сзади и точно также ее мереет, либо она настолько становится паражена от этих манипуляций, что поворачивается. Что проще реализовать ?
            img scene_Hostel_Street3
            imgl Dial_Monica_Sandwich_1
            imgr Dial_Citizen_7_1
            m "Эй, мистер, Вы возьмете флаер?"
#                    // художник делает еще несколько кругов\замеров
            # здесь будет вставка новых событий
            if rand(0, citizen7_refuse_probability) > 0:
                imgr Dial_Citizen_7_2
                call reduce_flyers() from _call_reduce_flyers_12
                imgr Dial_Citizen_7_2
                citizen7 "Я закончил. Флаер? Да давайте уже..."
                imgr Dial_Citizen_7_3
                citizen7 "Я бы хотел провести блее детальные замеры. В менее людном месте, это необходимо. Давайте отойдем чуть подальше."
                menu:
                    "Я никуда с тобой не пойду":
                        $ kebabWorkHarassmentAmount +=1
                        #img Моника злится
                        m "Мне ничего от тебя не нужно!"
                    "Куда именно?":
                        m "Куда именно?"
                        citizen7 "Здесь в подворотне есть прекрасное место для вдохновения. Мне нужно оценить ваши формы."
                        mt "Кажется я знаю о каком месте он говорит..."
                        m "Не дождешься!"
                        citizen7 "И напрасно. Вы же понимаете, что работа модели всегда оплачивается?"
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."

            else:
                imgr Dial_Citizen_7_4
                citizen7 "Я пытаюсь сосредоточиться на искусстве!"
                "Не отвлекайте меня!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen7_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_7_1
    m "Привет! Думаю, я могу помочь тебе с вдохновением."
    imgr Dial_Citizen_7_3
    citizen7 "Как хорошо! Не зря ты мне снилась прошлой ночью!"
    m "Только нам нужно не самое людное место..."
    citizen7 "Конечно, как скажешь. Я знаю одно подходящее, пойдем!"
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_239
    call pylonController(2, 1) from _call_pylonController_221
    with fadelong
    citizen7 "Вдохновение вещь сложная: очень сложно его найти... С чего бы нам начать?"
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen7_dialogue_pilon_loop7:
    call pylonController(1, 1) from _call_pylonController_222
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_223
            citizen7 "Милая, покажи свою чудесную грудь!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_224
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen7_dialogue_pilon_loop7
            call pylonController(3, 3) from _call_pylonController_225
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_52
            call pylonController(3, 3) from _call_pylonController_226
            # img показывает сиськи
            citizen7 "Божественно, я так и вижу идею для новой картины!"
            call pylonController(3, 3) from _call_pylonController_227
            citizen7 "Еще немного..."
            call pylonController(3, 3) from _call_pylonController_228
            citizen7 "Отлично!"
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen7_dialogue_pilon_loop7
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_229
            citizen7 "Как насчет попы? Уверен, она прекрасна, как и ты!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_230
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen7_dialogue_pilon_loop7
            call pylonController(4, 5) from _call_pylonController_231
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_53
            call pylonController(4, 5) from _call_pylonController_232
            # img показывает зад
            citizen7 "Не дурно! Очень похожа на персик, на картине моего коллеги. Милая, ты ему не позировала?"
            call pylonController(4, 5) from _call_pylonController_233
            mt "Что за извращенец..."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen7_dialogue_pilon_loop7
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_234
            citizen7 "Милая, потанцуй немного."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_235
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen7_dialogue_pilon_loop7
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_236
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages6, 4) from _call_showRandomImages_54
#            call pylonController(4, 5)
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_237
            with fade
            citizen7 "Прекрасно двигаешься!"
#            call pylonController(4, 1)
            mt "Не поспоришь..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen7_dialogue_pilon_loop7
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart4startsCompleted == True:
            call pylonController(4, 1) from _call_pylonController_238
            citizen7 "Покажи свою грудь, только не забудь снять одежду."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_239
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen7_dialogue_pilon_loop7
            call pylonController(4, 5) from _call_pylonController_240
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_55
            call pylonController(4, 5) from _call_pylonController_241
            citizen7 "Я так и знал, что они восхитительны!"
            mt "Это правда."
            call pylonController(4, 1) from _call_pylonController_242
            citizen7 "Думаю, я знаю, чему будет посвящена моя следующая картина!"
            citizen7 "Да, кстати, как насчет того, чтобы стать моей моделью? Это новый уровень!"
            m "Нет, спасибо."
            call pylonController(4, 5) from _call_pylonController_243
            citizen7 "Уверен, ты передумаешь! Сотни девушек мечтают о карьере модели!"
            call pylonController(4, 1) from _call_pylonController_244
            mt "Мне ли не знать, хе-хе..."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen7_dialogue_pilon_loop7
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
                call pylonController(2, 1) from _call_pylonController_245
                citizen7 "Как и любой модели, тебе полагается награда."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_246
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_247
            citizen7 "Ты не дала мне ни капли вдохновения!"
            return False
    return

# первый раз
label cit7_naked_boobs_1st:
    img 12055
    citizen7 "Мне не хватает вдохновения! Ты должны мне помочь!"
    img 12056
    m "Не понимаю. Ты же сам сказал, что я даю тебе вдохновение..."
    img 12057
    citizen7 "Да, но этого не достаточно! Это все не то!"
    img 12058
    m "Как это?"
    img 12059
    citizen7 "Ты не поймешь..."
    citizen7 "Мне нужно увидеть твою грудь, только на этот раз голую!"
    img 12060
    m "И это поможет?"
    img 12061
    citizen7 "Я не знаю, но это должно придать вдохновнения. Ну дак что?"
    img 12062
    menu:
        "Почему бы и нет.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12063
            m "Хватит и того, что ты уже видел!"
            return False
    img 12064
    m "Хорошо!"
    img 12065
    citizen7 "Я в предвкушении..."
    # отворачивается, моника переодевается...
    img 12066
    m "Но руками не трогать!"
    img 12067
    citizen7 "Конечно, я же человек искусства."
    # сиськи
    img 12068
    w
    img 12069
    w
    img 12070
    w
    img 12071
    citizen7 "Великолепно!"
    citizen7 "Это непревзойденно!"
    # сиськи еще
    img 12072
    w
    img 12073
    w
    img 12074
    citizen7 "Думаю, я должен слепить скульптуру!"
    citizen7 "Скажи, кто нибудь уже это делал?"
    img 12075
    m "Насколько я знаю, нет..."
    # моника продолжает показывать
    img 12076
    w
    img 12077
    w
    img 12078
    citizen7 "Это просто замечательно!"
    # моника продолжает показывать
    img 12079
    w
    img 12080
    w
    img 12081
    m "Ну ладно, хватит с тебя."
    img 12082
    citizen7 "Нет, подожди, я еще не..."
    img 12083
    m "Нет, все."
    img 12084
    citizen7 "..."
    citizen7 "Ну что же, надуюсь, этого хватит..."
    img 12085
    mt "Интересно, для чего?"
    $ nakedBoobsFirstly_Cit7 = True
    return True

# вариант 1
label cit7_naked_boobs_variant1:
    img 12086
    citizen7 "Детка, после одной из наших встреч, есть кое что, чего мне не хватает."
    img 12087
    m "И что же это?"
    img 12088
    citizen7 "Я хочу лицезреть твою голую грудь, и ты должна понимать, зачем я это прошу!"
    img 12089
    mt "Для вдохновения, ну конечно..."
    img 12090
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12091
            m "Хватит и того, что ты уже видел!"
            return False
    img 12092
    m "Отвернись!"
    # отворачивается, моника переодевается...
    img 12093
    w
    img 12094
    m "Можешь повернуться."
    m "Только руками не трогать!"
    img 12095
    citizen7 "Конечно!"
    # сиськи
    img 12096
    w
    img 12097
    w
    img 12098
    citizen7 "Ох, замечательно!"
    # сиськи еще
    img 12099
    w
    img 12100
    w
    img 12101
    citizen7 "Да, я это чувствую! Но это немного не то!"
    img 12102
    m "В смысле?"
    img 12103
    citizen7 "Представь себе, что ты модель! Попозируй для меня!"
    img 12104
    menu:
        "Хорошо.":
            img 12105
            m "Хорошо."
            # моника позирует как на камеру
            img 12106
            w
            img 12107
            w
            img 12108
            citizen7 "Ох, какая красота!"
            # моника позирует как на камеру еще
            img 12109
            w
            img 12110
            w
            img 12111
            citizen7 "Картина! Да, я знаю, что я напишу! Или нет..."
            pass
        "Не собираюсь!":
            img 12112
            m "Я не собираюсь этого делать!"
            img 12113
            citizen7 "Ооо... Почему ты так жестока со мной?"
            img 12114
            m "Не правда"
            img 12115
            citizen7 "Конечно правда, ты лишаешь меня вдохновения..."
            pass
    img 12116
    m "Ну ладно, хватит."
    img 12117
    citizen7 "Ох, надеюсь этого хватит для моего очередного творения!"
    return True

# вариант 2
label cit7_naked_boobs_variant2:
    img 12118
    citizen7 "Мне необходимо вдохновение! Обнажи свои очаровательные груди!"
    img 12119
    mt "А по твоим фразам этого не скажешь..."
    img 12120
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12121
            m "Хватит и того, что ты уже видел!"
            return False
    img 12122
    m "Отвернись!"
    # отворачивается, моника переодевается...
    img 12123
    w
    img 12124
    w
    img 12125
    m "Можешь повернуться."
    m "Только руками не трогать!"
    img 12126
    citizen7 "Конечно!"
    # сиськи
    img 12127
    w
    img 12128
    w
    img 12129
    citizen7 "Ох, замечательно! Как бы я хотел их трахнуть!"
    img 12130
    m "Что?!"
    img 12131
    citizen7 "Что?"
    img 12132
    m "Что ты сейчас сказал?"
    img 12133
    citizen7 "Я? Ничего, я восхищаюсь твоей грудью и думаю как соединить ее с искусством..."
    img 12134
    mt "Извращенец..."
    # сиськи еще
    img 12135
    w
    img 12136
    w
    img 12137
    citizen7 "Мне нужно больше!"
    citizen7 "Представь себе, что ты модель! Попозируй для меня!"
    img 12138
    menu:
        "Хорошо.":
            img 12139
            m "Хорошо."
            # моника позирует как на камеру
            img 12140
            w
            img 12141
            w
            img 12142
            w
            img 12143
            citizen7 "Ох, какая красота!"
            # моника позирует как на камеру еще
            img 12144
            w
            img 12145
            w
            img 12146
            w
            img 12147
            citizen7 "Да, это прекрасно, но это не совсем то. Давай я тебе помогу!"
            img 12148
            menu:
                "Хорошо.":
                    img 12149
                    citizen7 "Положи обе руки за голову."
                    # кладет
                    img 12150
                    w
                    img 12151
                    citizen7 "А теперь присядь так, чтобы я думал, что ты на лошади!"
                    # здесь можно добавить аля мысль художника как он представляет монику
                    # расскажу, если не очень понятно
                    img 12152
                    mt "Что же это будет..."
                    mt "Боже!"
                    img 12153
                    m "Да ни за что! Извращенец!"
                    img 12154
                    citizen7 "Ты ничего не понимаешь в искусстве...
                    pass
                "Нет, спасибо.":
                    img 12155
                    m "И так достаточно."
                    img 12156
                    citizen7 "Сразу видно, ты ничего не понимаешь в искусстве..."
                    pass
            pass
        "Не собираюсь!":
            img 12157
            m "Я не собираюсь этого делать!"
            img 12158
            citizen7 "Ооо... Почему ты так жестока со мной?"
            img 12159
            m "Не правда"
            img 12160
            citizen7 "Конечно правда, ты лишаешь меня вдохновения..."
            pass
    img 12161
    m "Ну ладно, хватит."
    img 12162
    citizen7 "Ох, надеюсь этого хватит для моего очередного творения!"
    return True
