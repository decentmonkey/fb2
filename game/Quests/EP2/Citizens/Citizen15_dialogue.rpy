label citizen15_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_15_1
            if citizen15_offered_last_day == day:
                imgr Dial_Citizen_15_4
                citizen15 "Я важная персона! Ты отвлекаешь меня!"
                return
            citizen15 "Йо! Бэби! Что ты хочешь?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen15_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen15_refuse_probability) > 0:
                        imgr Dial_Citizen_15_2
                        citizen15 "Флаер?..."
                        call reduce_flyers()
                        "Давай!"
                        imgr Dial_Citizen_15_3
                        citizen15 "А что дальше?"
                        m "В смысле?"
                        citizen15 "Я важная персона! Все девочки тащатся от меня!"
                        "Продолжай подкатывать ко мне! Мне нравится!"
                        label .loop1:
                            menu:
                                "Я не собираюсь к тебе подкатывать!":
                                    $ kebabWorkHarassmentAmount +=1
                                    imgl Dial_Monica_Sandwich_2
                                    #img Моника злится
                                    m "Я не собираюсь к тебе подкатывать!"
                                "Я не подкатываю, но все-же... (disabled)":
                                    jump .loop1
                    else:
                        imgr Dial_Citizen_15_4
                        citizen15 "Я важная персона! У меня нет времени на флаеры!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
