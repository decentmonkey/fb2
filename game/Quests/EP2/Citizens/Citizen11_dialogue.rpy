label citizen11_dialogue:
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_11_1
            if citizen11_offered_last_day == day:
                img Dial_Citizen_11_4
                citizen "Ох, не сейчас..."
                return
            citizen "Да? Что? Ох, моя голова..."
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen11_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                    citizen "Милая, флаер это последнее, что мне сейчас нужно. Нет ли у тебя чего покрепче?"
                    m "Вы про алкоголь?"
                    citizen "Господи, ну конечно..."
                    menu
                    #будет появляться если моника найдет к примеру рядом с помойкой или где еще полупустую бутылку. Надо подумать куда ее поставить.
                    "Вот, возьмите."
                    m "Вот, возьмите, тут кое что есть."
                    # дает бутылку
                    citizen "(Пьет) Ооо, Богиня! Ты меня спасла! Давай выпьем со мной, мне одному грустно."
                    menu
                    "Давай."
                    #потом будут другие реплики
                    mt "Ни за что."  и возврат к выбору
                    "Ну уж нет."
                    m "Нет, что-то, не хочется."
                    citizen "И очень даже зря. Божественный напиток. Дак что ты хотела?"
                    m "Возьмите, пожалуйста, этот флаер..."
                    citizen "Флаер? Конечно, сколько угодно!"
                    "У меня нет алкоголя."
                    m "Мистер, у меня нет алкоголя, только флаеры с рекламой вкуснейших кебабов..."
                    #злая картинка citizen
                    citizen "Каких еще кебабов? Проваливай отсюда!"
                    mt "Старый алкаш..."
                        call reduce_flyers()
                        img Dial_Citizen_11_2
                    else:
                        img Dial_Citizen_11_3
                        # можно ему бутыль в руку дорисовать?
                        citizen "Не отрывай меня от глубоких мыслей! Я размышляю о бренности этого великолепного напитка!"
        "Уйти.":
            pass
    return
