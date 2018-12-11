label citizen13_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_13_1
            if citizen13_offered_last_day == day:
                imgr Dial_Citizen_13_4
                citizen13 "Милая, давай в другой раз, я занят."
                return
            citizen13 "Ой, привет! Что у тебя, подруга?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen13_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen13_refuse_probability) > 0:
                        imgr Dial_Citizen_13_2
                        citizen13 "Кебаб? Фу...Ты разве не знаешь, они вредны для фигуры."
                        m "Но никто же не заставляет тебя его покупать. Просто возьми флаер."
                        citizen13 "А ты смешная. Ладно, я возьму один, только обещай мне, что ты не будешь есть эти противные кебабы."
                        "Хотя ты знаешь, у них есть одно достоинство и ты наверное знаешь какое."
                        m "?"
                        imgr Dial_Citizen_13_3
                        citizen13 "Глупенькая, ну конечно форма. На что они похожи?"
                        label .loop1:
                            menu:
                                "На кебабы.":
                                    imgl Dial_Monica_Sandwich_0
                                    m "Не знаю... На кебабы."
                                    imgr Dial_Citizen_13_4
                                    citizen13 "Нууу...С тобой не интересно"
                                    $ kebabWorkMonicaRefusedAmount += 1
                                    return
                                "На пенис... (disabled)" if corruption <= 30:
                                    jump .loop1
                                "На пенис..." if corruption > 30:
                                    $ kebabWorkHarassmentAmount +=1
                                    imgl Dial_Monica_Sandwich_0
                                    mt "Боже, что за извращенец?! Пожалуй, скажу то, что он хочет услышать."
                                    m "Ну он немного напоминает пенис."
                                    imgr Dial_Citizen_13_3
                                    citizen13 "Дааа! Только я думаю, что совсем не немного. Я знал, что мы найдем общий язык."

                                    imgr Dial_Citizen_13_2
                                    imgl Dial_Monica_Sandwich_1
                                    call reduce_flyers() from _call_reduce_flyers_6
                                    citizen13 "Приятно было пообщаться."
                                    return
                    else:
                        imgr Dial_Citizen_13_4
                        citizen13 "Детка, мне совсем некуда его положить..."
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
