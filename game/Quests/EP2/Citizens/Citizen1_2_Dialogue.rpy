label citizen1_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
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
                                citizen1 "А то ты не знаешь, тетя! Конечно тебя!"
                                citizen2 "Мой брат слишком груб, но в целом он прав."
                                imgl Dial_Monica_Sandwich_2
                                menu:
                                    "Что?! Да как вы можете просить такое?":
                                        m "Что?! Да как вы можете просить такое?"
                                        return
                    else:
                        imgr Dial_Citizen_1_4
                        citizen1 "Нам не нужны твои флаеры, тетя!"
                        $ kebabWorkMonicaRefusedAmount += 1

        "Уйти.":
            pass
    return
# диалог доступен только когда моника не работает на раздаче флаеров
label citizen1_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_1_1
    m "Эй, парни! Скажите, у вас есть деньги?"
    citizen1 "Смотря для чего, тетя. А тебе зачем?"
    m "Вы помнится хотели на меня посмотреть..."
    citizen1 "Да, тетя, и до сих пор хотим!"
    imgr Dial_Citizen_1_3
    m "Ну, я могу Вам кое-что показать, только нам лучше уйти отсюда."
    citizen1 "Конечно, тетя, без проблем."
    # уходят к пилону.
    citizen1 "Ну что, тетя..."
    label .loop1:
    menu:
        "Покажи сиськи.":
            citizen1 "Покажи нам свои классные сиськи!"
            m "Я не собираюсь раздеваться, только так."
            # img показывает сиськи
            citizen1 "Отличные сиськи, но как насчет того, чтобы снять все лишнее?"
            m "Ну уж нет."
            citizen1 "Ну и так не плохо."
            jump .loop1
        "Покажи попу.":
            citizen1 "Покажи нам свои красивый зад!"
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            citizen1 "Шикарная жопа, тетя!"
            jump .loop1
        "Достаточно на сегодня.":
            citizen1 "Ну все, тетя, хватит. До следующщео раза. Вот, держи."
            # дает монике копейку если были показы
            m "Что?! Так мало? Ну ничего, скоро я стану богатой и верну свою жизнь..."
            #если не было
            citizen1 "Тетя, и за что тебе платить? Ничего не получишь."
    return
