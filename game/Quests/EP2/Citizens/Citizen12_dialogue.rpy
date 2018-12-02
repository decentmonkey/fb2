label citizen12_dialogue:
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
                    $ citizen12_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        imgr Dial_Citizen_12_2
                        citizen12 "Ээээ... взять что?"
                        m "Возьмите, пожалуйста, этот флаер..."
                        call reduce_flyers()
                        citizen12 "Ок..."
                        imgr Dial_Citizen_12_3
                        citizen12 "И все? А как же развлечься?"
                        label .loop1:
                            menu:
                                "Я никого не собираюсь развлекать!":
                                    #img Моника злится
                                    m "Я никого не собираюсь развлекать!"
                                "Чем тебя развлечь? (disabled)":
                                    jump .loop1
                    else:
                        imgr Dial_Citizen_12_3
                        citizen12 "Мне неинтересны никакие флаеры!"
        "Уйти.":
            pass
    return
