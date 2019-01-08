default questOffendMonicaFlyersCitizen6ThanksGiven = False

label citizen6_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_6_1
            if citizen6_offered_last_day == day:
                imgr Dial_Citizen_6_4
                citizen6 "Нельзя! Я тороплюсь!"
                return
            citizen6 "Да, Леди? Что Вы хотели?"
            menu:
                # этот пункт появляется единождыпосле выполнения события нападения(проверка на переменную диалога 12)
                "Спасибо, что помог мне..." if questOffendMonicaFlyersCitizen12Completed == True and questOffendMonicaFlyersCitizen6ThanksGive == False:
                    mt "Надо бы поблагодарить его, но я не хочу делать это одетой в рекламу кебеба..."
                    return

                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen6_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen6_refuse_probability) > 0:
                        imgr Dial_Citizen_6_2
                        call reduce_flyers() from _call_reduce_flyers_1
                        citizen6 "Взять флаер? Хорошо..."
                        imgr Dial_Citizen_6_3
                        citizen6 "Какой красивый флаер! Прямо такой-же как Вы!"
                        imgl Dial_Monica_Sandwich_2
                        m "Спасибо конечно, но меня не нужно сравнивать с флаером."
                        citizen6 "Как насчет того чтобы сходить со мной в одно интересное место?"
                        menu:
                            "Я никуда с тобой не пойду":
                                $ kebabWorkHarassmentAmount +=1
                                #img Моника злится
                                m "Я ничего не предлагаю! Просто возьмите флаер!"
                            "В какое это место?":
                                m "Куда это?"
                                citizen6 "Да тут не далеко, тем более мы уже там были с тобой. Ха-ха!"
                                m "Хватит с меня этого места..."
                                citizen6 "Ну если тебе не нужны деньги..."
                                m "Ты это о чем?"
                                citizen6 "Как это о чем? Как будто ты ничего не понимаешь. За это обычно платят."
                                m "У меня есть деньги!"
                                mt "Точнее были..."
                    else:
                        imgr Dial_Citizen_6_4
                        citizen6 "Я тороплюсь! Давайте в другой раз!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen6_dialogue_after_offend:
    imgr Dial_Citizen_6_3
    m "Спасибо за помощь."
    citizen6 "Не за что, милочка. Ну что, приступим?"
    m "Приступим... К чему?"
    citizen6 "Ну как же, к моей награде."
    m "Награде?"
    citizen6 "Ага. Ты же догадываешься, какую?"
    m "Понимаешь, я сейчас не в самом лучшем финансовом положении..."
    citizen6 "Не, не... Не нужны мне твои 10 долларов!"
    m "Да как ты?!..."
    mt "Черт, у меня нет даже 10 долларов..."
    m "Что же ты хочешь?"
    citizen6 "Ты красивая, хочу на тебя посмотреть."
    m "Что?"
    citizen6 "Да! Не прикидывайся, что не понимаешь о чем я."
    m "Я не стану раздеваться!"
    citizen6 "Ха-ха! А ты не простая штучка... Ладно, пошли со мной, тут не далеко."
    m "Куда?"
    citizen6 "Не бойся, тут не далеко..."
    m "Я не собираюсь никуда с тобой идти!"
    imgr Dial_Citizen_6_3
    citizen6 "Послушай, хочу тебе напомнить: я тебя спас, ты мне обещала 'Все, что угодно'. А теперь шевели своим красивым задом, пока я добрый."
    mt "А ведь он прав...Возможно, он не такой уж и плохой."
    m "Ну хорошо, только я сказала, что не буду раздеваться."
    citizen6 "Я это уже слышал... Пошли уже."
    # переход на локацию с пилоном
    citizen6 "Ну вот, я же говтрил, что это не далеко."
    mt "Я уже была в этой грязной подворотне..."
    call pylonController(2, 3, 1)
    citizen6 "А теперь покажи сиськи!"
    if corruption < 50:
        mt "Я не могу себе этого позволить!"
        "Я еще не настолько опустилась!"
        "И, надеюсь, этого не произойдет НИКОГДА!"
        m "Да как ты можешь такое просить!?"
        citizen6 "Дорогуша, ты же обещала Все, что угодно. Дак вот, я хочу твои сиськи!"
        m "Я не могу!"
        help "Требуется 50 corruption"
        return
    m "Что? А что если нас кто-то увидит?"

    citizen6 "Расслабься, тут никого нет. Давай уже, показывай. Чем быстрее ты это сделаешь, тем быстрее пойдешь куда шла."
    call pylonController(1, 1, 2)
    mt "Что за извращенец..."
    m "Ладно..."
    # моника кажет сиськи
    call showRandomImages(boobsImages, 4)
    call pylonController(2, 3, 1)
    citizen6 "О да, какие сочные!"
    call pylonController(1, 1, 2)
    citizen6 "Да, у тебя шикарные сиськи! А теперь повернись и нагнись немного."
    if corruption < 70:
        mt "Я не могу себе этого позволить!"
        "Я еще не настолько опустилась!"
        "И, надеюсь, этого не произойдет НИКОГДА!"
        m "Ну уж нет, это слишком!"
        citizen6 "Ну ладно, я сегодня добрый. Можешь идти. Тем более твои сиськи это нечто!"
        $ questOffendMonicaFlyersCitizen6ThanksGiven = True
        $ fallingPathStarted = True
        help "Для активации этого события требовалось 70 corruption, но не переживайте, Моника еще покажет себя."
        return
    # моника кажет жопу
    call showRandomImages(assImages, 4)
    call pylonController(2, 3, 1)
    citizen6 "Да, детка, ты великолепна! Ох, у меня кажется встал... Нужно срочно отойти..."
    call pylonController(1, 1, 2)
    citizen6 "Можешь идти, считай, ты мне ничего не должна."
    # переменная отвечающая за А что бы ты хотел в диалогах с кебабом = 1
    $ questOffendMonicaFlyersCitizen6ThanksGiven = True
    $ fallingPathStarted = True
    return

label citizen6_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_6_1
    m "Привет! Помнишь, ты говорил, что я могу заработать..."
    imgr Dial_Citizen_6_3
    citizen6 "Конечно помню, у тебя все для этого есть!"
    m "..."
    citizen6 "В общем, я понимаю о чем ты. Давай не будем тратить время и пойдем уже в наше место"
    # уходят к пилону.
    citizen6 "Начнем."
    $ showedBoobs = False
    $ showedButt = False
    label .loop6:
    menu:
        "Покажи сиськи.":
            call pylonController(2, 3, 1)
            citizen6 "Покажи сиськи!"
            if corruption < 50:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется 50 corruption"
                jump .loop6

            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(2, 3, 1)
            # img показывает сиськи
            citizen6 "Корошее начало!"
            call pylonController(1, 1, 2)
            citizen6 "Ух, мне достаточно только взгляда и у меня встает..."
            call pylonController(2, 3, 1)
            citizen6 "Ооо... Как хорошо..."
            $ showedBoobs = True
            jump .loop6
        "Покажи попу.":
            call pylonController(2, 3, 1)
            citizen6 "Покажи жопу!"
            if corruption < 70:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется 70 corruption"
                jump .loop6
            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4)
            call pylonController(2, 3, 1)
            citizen6 "Вау, вот это да!"
            call pylonController(1, 1, 2)
            citizen3 "Никогда не видел таких шикарной жопы!"
            $ showedButt = True
            # img показывает зад
            jump .loop6
        "Достаточно на сегодня.":
            if showedBoobs == True and showedButt == True:
                $ add_money(0.5)
                citizen6 "Какая ты сочная! Вот держи, а я пойду займусь очень важным делом."
                m "Что?! Так мало? Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            if showedBoobs == True or showedButt == True:
                citizen6 "Какая ты сочная! Вот держи, а я пойду займусь очень важным делом."
                m "Что?! Так мало? Ну ничего, скоро я стану богатой и верну свою жизнь..."
                $ add_money(0.25)
                return
            #если не было
            citizen6 "Похоже, я зря потратил свое время, пойду найду другую шлюху."
            return
    return
