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
                    $ imagesArr = ["7110", "7111", "7112", "7113", "7114"]
                    $ images = random.sample(set(imagesArr), 2)
                    sound Jump2
                    img images[0]
                    w
                    img images[1]
                    w
                    img scene_Hostel_Street
                    imgl Dial_Monica_Sandwich_0
                    imgr Dial_Citizen_9_3
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
                            $ add_corruption(1, "monica_give_joint_day_" + str(day))
                            m "Вот."
                            imgr Dial_Citizen_9_3
                            citizen9 "Отлично. Узнаю старину Джека. Отличная вещь. Хочешь?"
                            imgl Dial_Monica_Sandwich_1
                            call reduce_flyers() from _call_reduce_flyers_7
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
                        call reduce_flyers() from _call_reduce_flyers_8
                        imgr Dial_Citizen_9_3
                        "Хорошо..."
                        citizen9 "Ооо, дамочка, а пойдемте к пилону! я потрогаю твою сиську еще разок!"
                        menu:
                            "Да ни за что на свете!":
                                $ kebabWorkHarassmentAmount +=1
                                #img Моника злится
                                m "Мне ничего от тебя не нужно!"
                            "Ну точно не сейчас.":
                                m "Не в этот раз."
                                citizen7 "Ооо, ты не отказываешься... Хорошо. Тогда приходи, как будешь не так занята. Кстати, у Найджела есть деньги!"
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
    call citizens_dialogue_process() from _call_citizens_dialogue_process_1
    $ restore_music()
    return
