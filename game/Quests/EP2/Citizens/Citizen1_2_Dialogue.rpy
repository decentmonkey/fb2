label citizen1_dialogue:
    imgl Dial_Monica_Sandwich_0
#    "Можно к Вам обратиться?"
    m "Эй, ребята... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_1_1
    if citizen1_offered_last_day == day:
        imgr Dial_Citizen_1_4
        citizen1 "Эй! Тетя!"
        "Ты уже подходила к нам!"
        "Хватит с нас твоих флаеров!"
        return
    citizen1 "Да, тетя? Что тебе надо?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            $ citizen1_offered_last_day = day
            imgl Dial_Monica_Sandwich_1
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen1_refuse_probability) > 0:
                imgr Dial_Citizen_1_2
                citizen1 "Тетя, не видишь, мы заняты, нам сейчас не до тебя."
                imgr Dial_Citizen_2_3
                citizen2 "Погоди, Том, разве ты не видишь? Она работает."
                imgr Dial_Citizen_1_3
                citizen1 "С такой внешностью тебе бы не флаеры раздавать!"
                imgl Dial_Monica_Sandwich_0
                mt "(Вот козел...)"
                imgr Dial_Citizen_2_2
                imgl Dial_Monica_Sandwich_1
                call reduce_flyers() from _call_reduce_flyers_9
                citizen2 "А я возьму, давай свой флаер."
                # на 3 раз будут они давать какие то задания ей
                imgr Dial_Citizen_1_3
                citizen1 "Тетя! А больше ты ничего мне не можешь дать?"
                menu:
                    "Больше ничего!":
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "Больше ничего!"
                        $ kebabWorkHarassmentAmount +=1
                    "А что бы вы хотели?":
                        m "А что бы вы хотели?"
                        imgr Dial_Citizen_1_3
                        citizen1 "А то ты не знаешь, тетя! Конечно тебя!"
                        imgr Dial_Citizen_2_3
                        citizen2 "Мой брат слишком груб, но в целом он прав."
                        imgl Dial_Monica_Sandwich_2
                        menu:
                            "Что?! Да как вы можете просить такое?":
                                m "Что?! Да как вы можете просить такое?"
                                return
                            "Я подумаю, но сейчас я занята..." if fallingPathStarted == True:
                                m "Я подумаю, но сейчас я занята..."
                                mt "В любом случае я не могу ничего поделать в этом жутком наряде..."
                                return

            else:
                imgr Dial_Citizen_1_4
                citizen1 "Нам не нужны твои флаеры, тетя!"
                $ kebabWorkMonicaRefusedAmount += 1

    return
# диалог доступен только когда моника не работает на раздаче флаеров
label citizen1_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_1_1
    m "Эй, парни! Скажите, у вас есть деньги?"
    citizen1 "Смотря для чего, тетя. А тебе зачем?"
    m "Вы помнится хотели на меня посмотреть..."
    imgr Dial_Citizen_1_3
    citizen1 "Да, тетя, и до сих пор хотим!"
    m "Ну, я могу Вам кое-что показать, только нам лучше уйти отсюда."
    citizen1 "Конечно, тетя, без проблем."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long")
    call pylonController(2, 1)
    with fade
    citizen1 "Ну что, тетя..."
    $ showedBoobs = False
    $ showedButt = False

    label citizen1_dialogue_pilon_loop1:
    call pylonController(1, 1)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) #
            citizen1 "Покажи нам свои классные сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1

            call pylonController(3, 3)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(3, 3)
            # img показывает сиськи
            citizen1 "Отличные сиськи, но как насчет того, чтобы снять все лишнее?"
            call pylonController(3, 2)
            m "Ну уж нет."
            call pylonController(3, 1)
            citizen1 "Ну и так не плохо."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen1_dialogue_pilon_loop1
        "Покажи попу.":
            call pylonController(4, 1)
            citizen1 "Покажи нам свои красивый зад!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            call pylonController(4, 5)
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4)
            call pylonController(4, 5)
            citizen1 "Шикарная жопа, тетя!"
            call pylonController(4, 5)
            citizen1 "Почти как у моей бывшей."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen1_dialogue_pilon_loop1
        "Станцуй. (disabled)" if pylonpart2startsCompleted == False:
            pass
        "Станцуй." if pylonpart2startsCompleted == True:
            call pylonController(4, 1)
            citizen1 "Покрутись на пилоне, тетя."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            call pylonController(4, 5)
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages, 4)
            call pylonController(4, 5)
            citizen1 "А ты крутишься как профессионал. Мне нравится!"
            call pylonController(4, 1)
            mt "Не думаю, что буду это делать часто..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen1_dialogue_pilon_loop1
        "Голые сиськи. (disabled)" if pylonpart2startsCompleted == False:
            pass
        "Голые сиськи." if pylonpart2startsCompleted == True:
            call pylonController(4, 1)
            citizen1 "Мы хотим поглядеть на твои классные сиськи еще раз. Снимай все!"
            mt "Грязные панки..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            call pylonController(4, 5)
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4)
            call pylonController(4, 5)
            citizen1 "Черт, тетя! Они шикарны! И что же ты их раньше от нас прятала?"
            call pylonController(4, 1)

            citizen1 "Эй, тетя! Как насчет того, чтобы получить немного больше?"
            m "..."
            citizen1 "Сожми ка свои аппетитные соски!"
            label citizen1_dialogue_pilon_loop1_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothNakedBoobsNippleSquizeCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothNakedBoobsNippleSquizeCorruptionRequired] corruption"
                        jump citizen1_dialogue_pilon_loop1_1
                    m "Ладно."
                    call pylonController(3, 4)
                    with fade
                    w
                    call showRandomImages(nakedboobssquizenipplesImages, 1)
                    call pylonController(3, 4)
                    citizen1 "Уф...А ты горячая!"
                "Ну уж нет!":
                    call pylonController(3, 1)
                    m "Не собираюсь, и так достаточно."
                    citizen1 "Не ожидал я такого тетя. Думаю, ты скоро передумаешь."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen1_dialogue_pilon_loop1
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
                call pylonController(2, 1)
                citizen1 "Ну все, тетя, хватит. До следующего раза. Вот, держи."
                $ add_money(earnedMoney)
                call pylonController(1, 1)
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1)
            citizen1 "Тетя, и за что тебе платить? Ничего не получишь."
            return False
    return
