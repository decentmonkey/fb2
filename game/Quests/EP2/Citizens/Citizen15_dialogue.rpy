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

label citizen15_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_15_1
    m "Привет! Кажется, ты говорил, что я могу заработать денег..."
    imgr Dial_Citizen_15_3
    citizen15 "Да, и сейчас говорю. Только учти: у меня от таких как ты отбоя нет. Ты должна мне показать что-то особенное."
    mt "Самодовольный козел...Да кем он себя возомнил? Черт, мне нужны деньги."
    m "Куда ты хотел пойти?"
    citizen15 "Ты же наверняка видала подворотню с пилоном? Вот туда и пойдем."
    # уходят к пилону.
    citizen15 "Ну что, начинай, только не разочаруй меня."
    $ showedBoobs = False
    $ showedButt = False
    label .loop15:
    menu:
        "Покажи сиськи.":
            call pylonController(2, 3, 1)
            citizen15 "Для начала сиськи, показывай!"
            if corruption < 50:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется 50 corruption"
                jump .loop15

            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(2, 3, 1)
            citizen15 "И это все?"
            call pylonController(1, 1, 2)
            # img показывает сиськи
            citizen15 "Мда, ну и так сойдет..."
            $ showedBoobs = True
            jump .loop15
        "Покажи попу.":
            call pylonController(2, 3, 1)
            citizen15 "А теперь повернсь и покажи свой зад!"
            if corruption < 70:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется 70 corruption"
                jump .loop15
            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4)
            call pylonController(2, 3, 1)
            # img показывает зад
            citizen15 "Зад, 10 долларовой шлюхи, но еще рабочий."
            call pylonController(1, 1, 2)
            mt "Что за козел. Врезать может ему?"
            $ showedButt = True
            jump .loop15
        "Достаточно на сегодня.":
            if showedBoobs == True and showedButt == True:
                $ add_money(0.5)
                citizen15 "Красивая шлюшка. Уверен, ты можешь больше, а пока так..."
                m "Что?! Так мало? Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            if showedBoobs == True or showedButt == True:
                citizen15 "Красивая шлюшка. Уверен, ты можешь больше, а пока так..."
                m "Что?! Так мало? Ну ничего, скоро я стану богатой и верну свою жизнь..."
                $ add_money(0.25)
                return
            #если не было
            citizen15 "Сходи поищи себе кого-нибудь еще."
            return
    return
