label citizen12_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_12_1
            if citizen12_offered_last_day == day:
                imgr Dial_Citizen_12_4
                citizen12 "Я тороплюсь! Мне некогда!"
                return
            citizen12 "Да, Крошка? Что ты хочешь от меня?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen12_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen12_refuse_probability) > 0:
                        imgr Dial_Citizen_12_2
                        citizen12 "Ээээ... взять что?"
                        m "Возьмите, пожалуйста, этот флаер..."
                        call reduce_flyers() from _call_reduce_flyers_8
                        citizen12 "Ок..."
                        imgr Dial_Citizen_12_3
                        citizen12 "И все? А как же развлечься?"
                        label .loop1:
                            menu:
                                "Я никого не собираюсь развлекать!":
                                    $ kebabWorkHarassmentAmount +=1
                                    imgl Dial_Monica_Sandwich_2
                                    #img Моника злится
                                    m "Я никого не собираюсь развлекать!"
                                "Чем тебя развлечь? (disabled)":
                                    jump .loop1
                    else:
                        imgr Dial_Citizen_12_4
                        citizen12 "Мне неинтересны никакие флаеры!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
