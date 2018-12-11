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
                        call reduce_flyers() from _call_reduce_flyers_6
                        citizen8 "Взять флаер? Хорошо..."
                        imgr Dial_Citizen_8_3
                        citizen8 "Детка! Ты подошла только за этим?"
                        "Хочешь предложить что-то еще?"
                        label .loop1:
                            menu:
                                "Я ничего не собираюсь предлагать!":
                                    imgl Dial_Monica_Sandwich_2
                                    $ kebabWorkHarassmentAmount +=1
                                    #img Моника злится
                                    m "Я ничего не собираюсь предлагать!"
                                "А что бы Вы хотели? (disabled)":
                                    jump .loop1
                    else:
                        imgr Dial_Citizen_8_4
                        citizen8 "Детка! Не приставай ко мне с этим!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
