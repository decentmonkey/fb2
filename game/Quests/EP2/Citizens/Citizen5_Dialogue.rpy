label citizen5_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_5_1
            if citizen5_offered_last_day == day:
                img Dial_Citizen_5_4
                citizen "Мистер занят! Вы отнимать у Мистера время!"
                return
            citizen "Что Вы хотеть от Мистера?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen5_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_5_2
                        call reduce_flyers()
                        citizen "Да, да, конено...Я взять этот флаер... Но ты мне должна. Акира сан никогда не делает ничего просто так."
                        mt "О чем это он?"
                        img Dial_Citizen_5_3
                        citizen "Я думать Вы предлагать место?"
                        label citizen5_loop1:
                            menu:
                                "Я ничего не предлагаю! Просто возьмите флаер!":
                                    #img Моника злится
                                    m "Я ничего не предлагаю! Просто возьмите флаер!"
                                "Место для чего? (disabled)":
                                    jump citizen5_loop1
                    else:
                        img Dial_Citizen_5_3
                        citizen "У Мистера нет времени вашего места!"
                        #img Моника злится
                        m "Какого еще места?"
        "Уйти.":
            pass
    return
