label citizen7_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_7_1
            if citizen7_offered_last_day == day:
                imgr Dial_Citizen_7_4
                citizen7 "Я пытаюсь сосредоточиться на искусстве!"
                "Не отвлекайте меня!"
                return
            citizen7 "Да? Что Вы хотели?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen7_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    # Реально ли тут сделать картинку или что то в этом духе, как художник достает кисть и измеряет монику?
                    img 7118
                    w
                    img 7117
                    citizen7 "Прекрасно, очень хорошо! А теперь повернитесь!"
                    img 7116
                    w
                    img 7117
                    $ add_corruption(1, "monica_art_day_" + str(day))
                    mt "Что вообще происходит?"
                    # тут эффект, что художник подходит к монике сзади и точно также ее мереет, либо она настолько становится паражена от этих манипуляций, что поворачивается. Что проще реализовать ?
                    img scene_Hostel_Street3
                    imgl Dial_Monica_Sandwich_1
                    imgr Dial_Citizen_7_1
                    m "Эй, мистер, Вы возьмете флаер?"
#                    // художник делает еще несколько кругов\замеров
                    # здесь будет вставка новых событий
                    if rand(0, citizen7_refuse_probability) > 0:
                        imgr Dial_Citizen_7_2
                        call reduce_flyers() from _call_reduce_flyers_11
                        imgr Dial_Citizen_7_2
                        citizen7 "Я закончил. Флаер? Да давайте уже..."
                        imgr Dial_Citizen_7_3
                    else:
                        imgr Dial_Citizen_7_4
                        citizen7 "Я пытаюсь сосредоточиться на искусстве!"
                        "Не отвлекайте меня!"
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return
