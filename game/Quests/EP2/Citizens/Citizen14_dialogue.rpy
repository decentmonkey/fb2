label citizen14_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_14_1
            if citizen14_offered_last_day == day:
                imgr Dial_Citizen_14_4
                citizen14 "Я тороплюсь! У меня много важных дел!"
                return
            citizen14 "Какая красавица! Что тебе надо от такого как Я? Ик!..."
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen14_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen14_refuse_probability) > 0:
                        imgr Dial_Citizen_14_2
                        citizen14 "Флаер?..."
                        call reduce_flyers()
                        "Хорошо... Ик!"
                        imgr Dial_Citizen_14_3
                        citizen14 "Но ты же не просто так подошла ко мне!"
                        "Я ведь понравился тебе? Хрюк..."
                        label .loop1:
                            menu:
                                "Мне никто не может понравиться в этой дыре!":
                                    $ kebabWorkHarassmentAmount +=1
                                    imgl Dial_Monica_Sandwich_2
                                    #img Моника злится
                                    m "Мне никто не может понравиться в этой дыре!"
                                "Может и так... (disabled)":
                                    jump .loop1
                    else:
                        imgr Dial_Citizen_14_4
                        citizen14 "Не возьму... Я все-равно его потеряю... Хрюк..."
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
