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
                        call reduce_flyers() from _call_reduce_flyers_10
                        "Давай!"
                        imgr Dial_Citizen_15_3
                        citizen15 "А что дальше?"
                        m "В смысле?"
                        citizen15 "Я важная персона! Все девочки тащатся от меня!"
                        "Продолжай подкатывать ко мне! Мне нравится!"
                        menu:
                            "Я не собираюсь к тебе подкатывать!":
                                $ kebabWorkHarassmentAmount +=1
                                imgl Dial_Monica_Sandwich_2
                                #img Моника злится
                                m "Я не собираюсь к тебе подкатывать!"
                            "Я не подкатываю, но все-же...":
                                m "Ну я так то не совсем подкатываю..."
                                citizen15 "Да, ты знаешь толк в парнях, но для начала хотел бы посмотреть на тебя поближе."
                                m "А?"
                                citizen15 "Давай сходим за угол, там нам никто не помешает.. Глядишь и заработаешь что нибудь."
                                m "Да кем ты себя возомнил?!"
                    else:
                        imgr Dial_Citizen_15_4
                        citizen15 "Я важная персона! У меня нет времени на флаеры!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
