label citizen1_dialogue:
    menu:
        "Можно к Вам обратиться?":
            m "Эй, ребята... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_1_1
            if citizen1_offered_last_day == day:
                imgr Dial_Citizen_1_4
                citizen "Эй! Тетя!"
                "Ты уже подходила к нам!"
                "Хватит с нас твоих флаеров!"
                return
            citizen1 "Да, тетя? Что тебе надо?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen1_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 3) <= 2:
                        imgr Dial_Citizen_1_2
                        citizen1 "Тетя, не видишь, мы заняты, нам сейчас не до тебя."
                        citizen2 "Погоди, Том, разве ты не видишь? Она работает."
                        citizen1 "С такой внешностью тебе бы не флаеры раздавать!"
                        mt "(Вот козел...)"
                        citizen2 "А я возьму, давай свой флаер."
                        # на 3 раз будут они давать какие то задания ей
                        imgr Dial_Citizen_1_3
                        citizen1 "Тетя! А больше ты ничего мне не можешь дать?"
                        label citizen1_loop1:
                            menu:
                                "Больше ничего!":
                                    #img Моника злится
                                    call reduce_flyers()
                                    m "Больше ничего!"
                                "А что бы ты хотел? (disabled)":
                                    jump citizen1_loop1
                    else:
                        imgr Dial_Citizen_1_3
                        citizen1 "Нам не нужны твои флаеры, тетя!"

        "Уйти.":
            pass
    return
