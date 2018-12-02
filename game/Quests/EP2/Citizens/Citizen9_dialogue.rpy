label citizen9_dialogue:
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_9_1
            if citizen9_offered_last_day == day:
                imgr Dial_Citizen_9_4
                citizen9 "Хэй! Мы уже разговаривали."
                return
            citizen9 "А? Да?"
            "Что?"
            menu:
                "Потрогай мою сиську." if monicaGotJoint == True:
                    m "Потрогай мою сиську."
                    citizen9 "Как скажешь, дамочка."
                    #подходит к монике сзади и хватает за грудь. так как на ней табличка, ей сложно сопротивляться.
                    m "Идиот! Что ты делаешь?"
                    citizen9 "То, что ты мне сказала! Хе-хе-хе. Отличная грудь кстати!"
                    m "Идиот! Я от Джека!"
                    citizen9 "Ууу, дамочка, с этого и надо было начинать. Что у тебя?"
                    #citizen9 отходит
                    menu:
                        "Дать косяк.":
                            m "Вот."
                            citizen9 "Отлично. Узнаю старину Джека. Отличная вещь. Хочешь?"
                            m "Нет, спасибо. Вот, возьми еще флаер."
                            citizen9 "Флаер? Ладно. Как насчет потрогать сиську еще раз?"
                            m "Нет!"
                            mt "Идиот."
                            $ monicaGotJoint = False
                            $ citizen9_offered_last_day = day
                            return
                        "Ничего":
                            m "Ничего, я, кажется, ошиблась..."
                            return

                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen9_offered_last_day = day
                    #если нет косяка
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        imgr Dial_Citizen_9_2
                        call reduce_flyers()
                        citizen9 "А? Что?"
                        "Флаер?"
                        "Хорошо..."
                        imgr Dial_Citizen_9_3
                    else:
                        imgr Dial_Citizen_9_3
                        citizen9 "Отстань, дамочка! Я пытаюсь кое-что вспомнить..."
                        citizen9 "Вы меня отвлекаете!"
        "Уйти.":
            pass
    return
