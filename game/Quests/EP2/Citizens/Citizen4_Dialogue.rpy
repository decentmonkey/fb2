label citizen4_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_4_1
    if citizen4_offered_last_day == day:
        imgr Dial_Citizen_4_4
        citizen4 "Нельзя!"
        return
    citizen4 "Да?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen4_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen4_refuse_probability) > 0:
                imgr Dial_Citizen_4_2
                call reduce_flyers() from _call_reduce_flyers_2
                citizen4 "Хорошо."
                citizen4 "А что на нем?"
                m "Это реклама вкусного кебаба... Там же написано!"
                imgr Dial_Citizen_4_3
                citizen4 "А я подумал Вы решили познакомиться со мной!"
                menu:
                    "У меня нет желания знакомиться с Вами!":
                        $ kebabWorkHarassmentAmount +=1
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "У меня нет желания знакомиться с Вами!"
                    "Что Вы подразумеваете под знакомством?":
                        m "Что вы имеете ввиду?"
                        citizen4 "Я бы хотел узнать по ближе такую красотку. Думаю, мы бы договорились."
                        m "Договорились о чем?"
                        citizen4 "Что за вопросы? Обычно девушки вашей профессии это понимают."
                        mt "Да что за люди здесь живут?! Всем надо одно и то же..."
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."
            else:
                imgr Dial_Citizen_4_4
                citizen4 "Давайте в другой раз!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen4_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_4_1
    m "Привет! Помню, ты хотел познакомиться поближе?"
    imgr Dial_Citizen_4_3
    citizen4 "Конечно, давай познакомимся."
    m "Ну я не о близком знакомстве...Немного о другом."
    citizen4 "Да не вопрос, я понимаю о чем речь. Любой из нашего района тебя поймет с полуслова."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long")
    call pylonController(2, 1)
    with fade
    citizen4 "Ну что, давай начнем."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen4_dialogue_pilon_loop4:
    call pylonController(1, 1)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1)
            citizen4 "Покажи мне свои сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(3, 3)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(5, 3)
            # img показывает сиськи
            citizen4 "Да, очень хорошо, но я видел сиськи и получше!"
            call pylonController(5, 1)
            mt "Козел!"
            call pylonController(3, 1)
            citizen4 "Хотя весьма не плохо."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen4_dialogue_pilon_loop4
        "Покажи попу.":
            call pylonController(4, 1)
            citizen4 "Покажи свой задницу."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(4, 5)
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4)
            call pylonController(4, 5)
            citizen4 "Красивая задница, но я люблю побольше!"
            call pylonController(4, 5)
            citizen4 "Но ее можно увеличить, подумай об этом."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen4_dialogue_pilon_loop4
        "Станцуй. (disabled)" if pylonpart2startsCompleted == False:
            pass
        "Станцуй." if pylonpart2startsCompleted == True:
            call pylonController(4, 1)
            citizen4 "Покрутись на шесте немного. Надеюсь, ты хорошо двигаешься."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(4, 5)
            with fade
            m "Хорошо, только не долго."
            call showRandomImages(pylonClothDanceImages, 4)
            call pylonController(4, 5)
            citizen4 "Сойдет. У меня есть знакомая стриптизерша. Если хочешь, могу вас познакомить."
            "Уж она то научит тебя всему."
            call pylonController(4, 1)
            mt "И что ты за козел?!"
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen4_dialogue_pilon_loop4
        "Голые сиськи. (disabled)" if pylonpart2startsCompleted == False:
            pass
        "Голые сиськи." if pylonpart2startsCompleted == True:
            call pylonController(4, 1)
            citizen4 "Показывай сиськи, только не забудь все снять."
            mt "Урод..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(4, 5)
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4)
            call pylonController(4, 5)
            citizen4 "Должен признать, твои сиськи хороши. Но для полной картины, их нужно потрогать."
            call pylonController(4, 1)
            m "Даже не думай! С тебя хватит!"

            citizen4 "Погоди минутку. Потряси ка своими сочными сиськами!"
            label citizen4_dialogue_pilon_loop4_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothNakedBoobsShakeCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothNakedBoobsShakeCorruptionRequired] corruption"
                        jump citizen4_dialogue_pilon_loop4_1
                    m "Ладно."
                    call pylonController(3, 4)
                    with fade
                    w
                    call showRandomImages(nakedboobsshakeImages, 1)
                    call pylonController(3, 4)
                    citizen4 "О да! Теперь мне еще больше хочется их потрогать!"
                    m "Даже не думай!"
                "Ну уж нет!":
                    call pylonController(3, 1)
                    m "Не собираюсь, и так достаточно."
                    citizen4 "Как хочешь. Похоже, мне придется найти другую шлюху."

            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen4_dialogue_pilon_loop4
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
                citizen4 "А ты ничего такая, надо будет вернуться к нашему знакомству. Держи, заслужила."
                $ add_money(earnedMoney)
                call pylonController(1, 1)
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1)
            citizen4 "Какое то не продуктивное вышло знакомство. Надеюсь, в другой раз будет лучше."
            return False
    return
