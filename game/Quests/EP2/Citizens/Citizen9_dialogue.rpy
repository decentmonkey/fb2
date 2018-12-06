label citizen9_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_9_1
            if citizen9_offered_last_day == day and monicaGotJoint != True:
                imgr Dial_Citizen_9_4
                citizen9 "Хэй! Мы уже разговаривали."
                return
            citizen9 "А? Да?"
            "Что?"
            menu:
                "Потрогай мою сиську." if monicaGotJoint == True:
                    imgl Dial_Monica_Sandwich_0
                    m "Потрогай мою сиську."
                    imgr Dial_Citizen_9_3
                    citizen9 "Как скажешь, дамочка."
                    #подходит к монике сзади и хватает за грудь. так как на ней табличка, ей сложно сопротивляться.
                    m "Идиот! Что ты делаешь?"
                    imgr Dial_Citizen_9_3
                    citizen9 "То, что ты мне сказала! Хе-хе-хе. Отличная грудь кстати!"
                    m "Идиот! Я от Джека!"
                    imgr Dial_Citizen_9_2
                    citizen9 "Ууу, дамочка, с этого и надо было начинать. Что у тебя?"
                    #citizen9 отходит
                    menu:
                        "Дать косяк.":
                            $ remove_inventory("joint", 1, True)
                            imgl Dial_Monica_Sandwich_0
                            m "Вот."
                            imgr Dial_Citizen_9_3
                            citizen9 "Отлично. Узнаю старину Джека. Отличная вещь. Хочешь?"
                            imgl Dial_Monica_Sandwich_1
                            call reduce_flyers()
                            m "Нет, спасибо. Вот, возьми еще флаер."
                            imgr Dial_Citizen_9_2
                            citizen9 "Флаер? Ладно. Как насчет потрогать сиську еще раз?"
                            imgl Dial_Monica_Sandwich_2
                            m "Нет!"
                            mt "Идиот."
                            $ monicaGotJoint = False
                            $ citizen9_offered_last_day = day
                            $ kebabWorkHarassmentAmount +=1
                            return
                        "Ничего":
                            imgl Dial_Monica_Sandwich_0
                            m "Ничего, я, кажется, ошиблась..."
                            return

                "Возьмите, пожалуйста, этот флаер..." if citizen9_offered_last_day != day:
                    imgl Dial_Monica_Sandwich_1
                    $ citizen9_offered_last_day = day
                    #если нет косяка
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen9_refuse_probability) > 0:
                        imgr Dial_Citizen_9_2
                        citizen9 "А? Что?"
                        "Флаер?"
                        call reduce_flyers()
                        imgr Dial_Citizen_9_3
                        "Хорошо..."
                    else:
                        imgr Dial_Citizen_9_4
                        citizen9 "Отстань, дамочка! Я пытаюсь кое-что вспомнить..."
                        citizen9 "Вы меня отвлекаете!"
                        $ kebabWorkMonicaRefusedAmount += 1
                "Уйти.":
                    pass
        "Уйти.":
            pass
    return

label Citizen_9_use_joint:
    $ obj_name = "Citizen_9"
    call citizens_dialogue_process()
    $ restore_music()
    return
