label citizen11_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_11_1
            if citizen11_offered_last_day == day:
                imgr Dial_Citizen_11_4
                citizen11 "Ох, не сейчас..."
                return
            citizen11 "Да? Что? Ох, моя голова..."
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen11_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
#                    if renpy.random.randint(0, 1) == 0:
                    imgr Dial_Citizen_11_2
                    citizen11 "Милая, флаер это последнее, что мне сейчас нужно. Нет ли у тебя чего покрепче?"
                    m "Вы про алкоголь?"
                    citizen11 "Господи, ну конечно..."
                    menu:
                        #этот пункт меню будет появляться если моника найдет к примеру рядом с помойкой или где еще полупустую бутылку. Надо подумать куда ее поставить.
                        "Вот, возьмите.zzz":
                            m "Вот, возьмите, тут кое что есть."
                            imgl Dial_Monica_Gives_Bottle
                            imgr Dial_Citizen_11_drink
                            citizen11 "(Пьет) Ооо, Богиня! Ты меня спасла! Давай выпьем со мной, мне одному грустно."
                            m "Нет, что-то, не хочется."
                            mt "Ни за что."
                            citizen11 "И очень даже зря. Божественный напиток. Дак что ты хотела?"
                            m "Возьмите, пожалуйста, этот флаер..."
                            citizen11 "Флаер? Конечно, сколько угодно!"
                            call reduce_flyers()
                        "У меня нет алкоголя.":
                            imgl Dial_Monica_Sandwich_1
                            m "Мистер, у меня нет алкоголя, только флаеры с рекламой вкуснейших кебабов..."
                            imgr Dial_Citizen_11_4
                            citizen11 "Каких еще кебабов? Проваливай отсюда!"
                            imgl Dial_Monica_Sandwich_0
                            mt "Старый алкаш..."
                            $ kebabWorkMonicaRefusedAmount += 1
                            return
    #                    else:
    #                        img Dial_Citizen_11_3
    #                        # можно ему бутыль в руку дорисовать?
    #                        citizen11 "Не отрывай меня от глубоких мыслей! Я размышляю о бренности этого великолепного напитка!"
        "Уйти.":
            pass
    return
