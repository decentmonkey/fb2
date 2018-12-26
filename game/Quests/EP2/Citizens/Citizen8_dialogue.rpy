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
                        citizen8 "Взять флаер? Хорошо... Но что я получу взамен?"
                        m "Вы получите флаер, разве этого мало?"
                        citizen8 "Для меня он бесполезен. Я бы хотел чтобы ты..."
                        # следующая реплика будет зависеть от значения созданной переменной A
                        citizen8 "Показала язык." # if A == 1
                        #citizen8 "шлепнула себя по попе. " # if A == 2
                        # ...
                        mt "Что за бред. Это только ради того, чтобы он взял флаер?! Что же делать..."
                        menu:
                            "Выполнить просьбу.":
                                m "Ну ладно."
                                mt "Скорее бы уже раздать эти флаеры..."
                                # картинка - моника показывает язык (опять же картинка будет зависеть от A)
                                imgr Dial_Citizen_8_3
                                citizen8 "Миленько, ты отлично справилась."
                                call reduce_flyers() from _call_reduce_flyers_4
                            "Ну уж нет, извращенец!":
                                m "Извращенец! Я не собираюсь выполнять твои извращенные просьбы!"
                                return
                        citizen8 "Детка! Ты подошла только за этим?"
                        "Хочешь предложить что-то еще?"
                        #label .loop1:
                        menu:
                            "Я ничего не собираюсь предлагать!":
                                imgl Dial_Monica_Sandwich_2
                                $ kebabWorkHarassmentAmount +=1
                                #img Моника злится
                                m "Я ничего не собираюсь предлагать!"
                            "А что бы Вы хотели?":
                                #menu: #показывается если A != 0
                                m "А что бы вы хоотели?"
                                citizen8 "Покажи мне свой язык."
                                m "Ну ладно."
                                imgl Dial_Monica_Tongue_Out_1
                                citizen8 "Чудесно, ты просто молодец! Вот, возьми это..."
                                # Citizen дает монике доллар
                                #jump .loop1
                    else:
                        imgr Dial_Citizen_8_4
                        citizen8 "Детка! Не приставай ко мне с этим!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
