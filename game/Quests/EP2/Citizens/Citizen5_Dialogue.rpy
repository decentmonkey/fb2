label citizen5_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_5_1
            if citizen5_offered_last_day == day:
                imgr Dial_Citizen_5_4
                citizen5 "Мистер занят! Вы отнимать у Мистера время!"
                return
            citizen5 "Что Вы хотеть от Мистера?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen5_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen5_refuse_probability) > 0:
                        imgr Dial_Citizen_5_2
                        citizen5 "Да, да, конено...Я взять этот флаер... Но ты мне должна. Акира сан никогда не делает ничего просто так."
                        mt "О чем это он?"
                        imgr Dial_Citizen_5_3
                        citizen5 "Я думать Вы предлагать место?"
                        label citizen5_loop1:
                            menu:
                                "Я ничего не предлагаю! Просто возьмите флаер!":
                                    $ kebabWorkHarassmentAmount +=1
                                    #img Моника злится
                                    m "Я ничего не предлагаю! Просто возьмите флаер!"
                                    call reduce_flyers() from _call_reduce_flyers_2
                                "Место для чего? (disabled)":
                                    jump citizen5_loop1
                    else:
                        imgr Dial_Citizen_5_4
                        citizen5 "У Мистера нет времени вашего места!"
                        #img Моника злится
                        imgl Dial_Monica_Sandwich_0
                        m "Какого еще места?"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
