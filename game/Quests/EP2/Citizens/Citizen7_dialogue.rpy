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
        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart3startsCompleted == True:
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
