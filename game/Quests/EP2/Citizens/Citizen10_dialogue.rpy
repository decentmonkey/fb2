label citizen10_dialogue:
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_10_1
            if citizen10_offered_last_day == day:
                imgr Dial_Citizen_10_4
                citizen10 "Я Вас не знаю! Не отвлекайте меня!"
                return
            citizen10 "Да? Я Вас откуда-то знаю?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen10_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        imgr Dial_Citizen_10_2
                        call reduce_flyers()
                        citizen10 "Флаер? Хорошо..."
                        imgr Dial_Citizen_10_3
                        citizen10 "Оу! Какая ты красотка! Прямо как бутон молодой орхидеи."
                        mt "Что? Странный тип..."
                    else:
                        imgr Dial_Citizen_10_3
                        citizen10 "У меня полные карманы всяких бумажек!"
        "Уйти.":
            pass
    return
