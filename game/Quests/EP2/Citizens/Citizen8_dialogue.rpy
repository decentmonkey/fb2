default citizen8_varA = 1

label citizen8_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_8_1
            if citizen8_offered_last_day == day:
                imgr Dial_Citizen_8_4
                citizen8 "Детка! Не приставай ко мне!"
                return
            citizen8 "Да, детка? Что ты хочешь мне предложить?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen8_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen8_refuse_probability) > 0:
                        imgr Dial_Citizen_8_2
                        citizen8 "Взять флаер? Хорошо... Но что я получу взамен?"
                        m "Вы получите флаер, разве этого мало?"
                        citizen8 "Для меня он бесполезен. Я бы хотел чтобы ты..."
                        $ citizen8_varA += 1

                        # следующая реплика будет зависеть от значения созданной переменной A
                        if citizen8_varA%2 == 0:
                            citizen8 "Показала язык." # if A == 1
                        if citizen8_varA%2 == 1:
                            citizen8 "шлепнула себя по попе. " # if A == 2
                        # ...
                        mt "Что за бред. Это только ради того, чтобы он взял флаер?! Что же делать..."
                        menu:
                            "Выполнить просьбу.":
                                m "Ну ладно."
                                mt "Скорее бы уже раздать эти флаеры..."
                                if citizen8_varA%2 == 0:
                                    imgl Dial_Monica_Sandwich_3
                                if citizen8_varA%2 == 1:
                                    imgl Dial_Monica_Sandwich_4
                                # картинка - моника показывает язык (опять же картинка будет зависеть от A)
                                imgr Dial_Citizen_8_3
                                citizen8 "Миленько, ты отлично справилась."
                                call reduce_flyers() from _call_reduce_flyers_4
                            "Ну уж нет, извращенец!":
                                m "Извращенец! Я не собираюсь выполнять твои извращенные просьбы!"
                                return
                        return
                        citizen8 "Детка! Ты подошла только за этим?"
                        "Хочешь предложить что-то еще?"
                        #label .loop1:
                        menu:
                            "Я ничего не собираюсь предлагать!":
                                imgl Dial_Monica_Sandwich_2
                                $ kebabWorkHarassmentAmount +=1
                                #img Моника злится
                                m "Я ничего не собираюсь предлагать!"
                            "А что бы Вы хотели?":
                                #menu: #показывается если A != 0
                                m "А что бы вы хоотели?"
                                citizen8 "Покажи мне свой язык."
                                m "Ну ладно."
                                imgl Dial_Monica_Tongue_Out_1
                                citizen8 "Чудесно, ты просто молодец! Вот, возьми это..."
                                # Citizen дает монике доллар
                                #jump .loop1
                    else:
                        imgr Dial_Citizen_8_4
                        citizen8 "Детка! Не приставай ко мне с этим!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen8_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_8_1
    m "Привет! Ты меня помнишь?"
    imgr Dial_Citizen_8_3
    citizen8 "Конечно! Твой язычек сложно забыть!"
    m "Я хочу предложить сделку: ты мне дашь денег. Взамен я разрешу тебе на меня посмотреть."
    citizen8 "Звучит как честная сделка, но лучше совершить ее не здесь."
    # уходят к пилону.
    citizen8 "С чего бы нам начать..."
    $ showedBoobs = False
    $ showedButt = False
    label citizen8_dialogue_pilon_loop8:
    menu:
        "Покажи сиськи.":
            call pylonController(2, 3, 1)
            citizen8 "Покажи мне свои сиськи."
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen8_dialogue_pilon_loop8
            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(2, 3, 1)
            # img показывает сиськи
            citizen8 "Хорошо, а теперь высунь язык!"
            label citizen8_dialogue_pilon_loop8_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothBoobsTongueCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothBoobsTongueCorruptionRequired] corruption"
                        jump citizen8_dialogue_pilon_loop8_1
                    m "Ладно."
                    call pylonController(1, 3, 1)
                    call showRandomImages(boobsImagesTonque, 1)
                    # img показывает сиськи и язык
                    citizen8 "Чудно, а ты молодец!"
                "Ну уж нет!":
                    m "Не собираюсь, и так достаточно."
                    citizen8 "Ладно, но с этим цена сделки могла стать выше."
            $ showedBoobs = True
            jump citizen8_dialogue_pilon_loop8
        "Покажи попу.":
            call pylonController(2, 3, 1)
            citizen8 "Развернись и поверти задом."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen8_dialogue_pilon_loop8
            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4)
            call pylonController(2, 3, 1)
            # img показывает зад
            citizen8 "Молодец, цена нашей сделки растет."
            mt "И почему он говорит все об этой сделке. Я же вроде не продаю себя..."
            call pylonController(1, 1, 2)
            citizen8 "О да!"
            $ showedButt = True
            jump citizen8_dialogue_pilon_loop8
        "Достаточно на сегодня.":
            if showedBoobs == True and showedButt == True:
                $ add_money(0.5)
                citizen8 "Славно потрудилась. Вот, держи."
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            if showedBoobs == True or showedButt == True:
                citizen8 "Славно потрудилась. Вот, держи."
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                $ add_money(0.25)
                return
            #если не было
            citizen8 "Сделки нет, ты не выполнила свою часть."
            return
    return
