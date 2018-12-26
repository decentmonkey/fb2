label citizen4_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Мистер... Можно к Вам обратиться?":
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
                                сitizen4 "Я бы хотел узнать по ближе такую красотку. Думаю, мы бы договорились."
                                m "Договорились о чем?"
                                citizen4 "Что за вопросы? Обычно девушки вашей профессии это понимают."
                                mt "Да что за люди здесь живут?! Всем надо одно и то же..."
                    else:
                        imgr Dial_Citizen_4_4
                        citizen4 "Давайте в другой раз!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
