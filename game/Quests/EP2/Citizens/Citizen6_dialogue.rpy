label citizen6_dialogue:
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
                    $ citizen6_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        imgr Dial_Citizen_6_2
                        call reduce_flyers()
                        citizen6 "Взять флаер? Хорошо..."
                        imgr Dial_Citizen_6_3
                        citizen6 "Какой красивый флаер! Прямо такой-же как Вы!"
                        m "Спасибо конечно, но меня не нужно сравнивать с флаером."
                    else:
                        imgr Dial_Citizen_6_3
                        citizen6 "Я тороплюсь! Давайте в другой раз!"
        "Уйти.":
            pass
    return
