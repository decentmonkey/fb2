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
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen6_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen6_refuse_probability) > 0:
                        imgr Dial_Citizen_6_2
                        call reduce_flyers() from _call_reduce_flyers_9
                        citizen6 "Взять флаер? Хорошо..."
                        imgr Dial_Citizen_6_3
                        citizen6 "Какой красивый флаер! Прямо такой-же как Вы!"
                        imgl Dial_Monica_Sandwich_2
                        m "Спасибо конечно, но меня не нужно сравнивать с флаером."
                    else:
                        imgr Dial_Citizen_6_4
                        citizen6 "Я тороплюсь! Давайте в другой раз!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
