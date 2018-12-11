label citizen1_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
            m "Эй, ребята... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_1_1
            if citizen1_offered_last_day == day:
                imgr Dial_Citizen_1_4
                citizen1 "Эй! Тетя!"
                "Ты уже подходила к нам!"
                "Хватит с нас твоих флаеров!"
                return
            citizen1 "Да, тетя? Что тебе надо?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen1_offered_last_day = day
                    imgl Dial_Monica_Sandwich_1
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen1_refuse_probability) > 0:
                        imgr Dial_Citizen_1_2
                        citizen1 "Тетя, не видишь, мы заняты, нам сейчас не до тебя."
                        imgr Dial_Citizen_2_3
                        citizen2 "Погоди, Том, разве ты не видишь? Она работает."
                        imgr Dial_Citizen_1_3
                        citizen1 "С такой внешностью тебе бы не флаеры раздавать!"
                        imgl Dial_Monica_Sandwich_0
                        mt "(Вот козел...)"
                        imgr Dial_Citizen_2_2
                        imgl Dial_Monica_Sandwich_1
                        call reduce_flyers() from _call_reduce_flyers
                        citizen2 "А я возьму, давай свой флаер."
                        # на 3 раз будут они давать какие то задания ей
                        imgr Dial_Citizen_1_3
                        citizen1 "Тетя! А больше ты ничего мне не можешь дать?"
                        label citizen1_loop1:
                            menu:
                                "Больше ничего!":
                                    imgl Dial_Monica_Sandwich_2
                                    #img Моника злится
                                    m "Больше ничего!"
                                    $ kebabWorkHarassmentAmount +=1
                                "А что бы ты хотел? (disabled)":
                                    jump citizen1_loop1
                    else:
                        imgr Dial_Citizen_1_4
                        citizen1 "Нам не нужны твои флаеры, тетя!"
                        $ kebabWorkMonicaRefusedAmount += 1

        "Уйти.":
            pass
    return
