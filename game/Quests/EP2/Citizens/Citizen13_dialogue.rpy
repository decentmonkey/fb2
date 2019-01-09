label citizen13_dialogue:
    imgl Dial_Monica_Sandwich_0
    menu:
        "Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            imgr Dial_Citizen_13_1
            if citizen13_offered_last_day == day:
                imgr Dial_Citizen_13_4
                citizen13 "Милая, давай в другой раз, я занят."
                return
            citizen13 "Ой, привет! Что у тебя, подруга?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    imgl Dial_Monica_Sandwich_1
                    $ citizen13_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if rand(0, citizen13_refuse_probability) > 0:
                        imgr Dial_Citizen_13_2
                        citizen13 "Кебаб? Фу...Ты разве не знаешь, они вредны для фигуры."
                        m "Но никто же не заставляет тебя его покупать. Просто возьми флаер."
                        citizen13 "А ты смешная. Ладно, я возьму один, только обещай мне, что ты не будешь есть эти противные кебабы."
                        "Хотя ты знаешь, у них есть одно достоинство и ты наверное знаешь какое."
                        m "?"
                        imgr Dial_Citizen_13_3
                        citizen13 "Глупенькая, ну конечно форма. На что они похожи?"
                        label .loop1:
                            menu:
                                "На кебабы.":
                                    imgl Dial_Monica_Sandwich_0
                                    m "Не знаю... На кебабы."
                                    imgr Dial_Citizen_13_4
                                    citizen13 "Нууу...С тобой не интересно"
                                    $ kebabWorkMonicaRefusedAmount += 1
                                    return
                                "На пенис... (requires 30 corruption)" if corruption < 30:
                                    jump .loop1
                                "На пенис..." if corruption >= 30:
                                    $ kebabWorkHarassmentAmount +=1
                                    imgl Dial_Monica_Sandwich_0
                                    mt "Боже, что за извращенец?! Пожалуй, скажу то, что он хочет услышать."
                                    m "Ну он немного напоминает пенис."
                                    imgr Dial_Citizen_13_3
                                    citizen13 "Дааа! Только я думаю, что совсем не немного. Я знал, что мы найдем общий язык."

                                    imgr Dial_Citizen_13_2
                                    imgl Dial_Monica_Sandwich_1
                                    call reduce_flyers() from _call_reduce_flyers_6
                                    citizen13 "Приятно было пообщаться."
                                    return
                    else:
                        imgr Dial_Citizen_13_4
                        citizen13 "Детка, мне совсем некуда его положить..."
                        $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen13_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_13_1
    m "Привет! Ты меня помнишь?"
    imgr Dial_Citizen_13_3
    citizen13 "Кончно помню, подруга! Ты разносишь флаеры с рекламой этих ужасных кебабов."
    m "Ну да, иногда."
    mt "А он выглядит дружелюбно и похоже, я ему не интересна."
    m "Не будет ли у тебя лишних денег?"
    citizen13 "А тебе зачем, подруга? Если нужна защита, дак у меня есть!"
    mt "Да за кого он меня принимает?"
    m "Нет, мне нужна наличка."
    citizen13 "Ну для тебя у меня есть немного, но ты же знаешь, что ничегго не делается просто так."
    m "Ты мог бы мне одолжить."
    citizen13 "Ха-ха-ха. Подруга, я похож на идиота?"
    citizen13 "А вообще знаешь, раз тебе так нужны деньги, у меня есть идея. Пошли."
     # уходят к пилону.
    citizen13 "Вот мы и пришли. Вечером тут полно народу. А теперь..."
    $ showedBoobs = False
    $ showedButt = False
    label citizen13_dialogue_pilon_loop13:
    menu:
        "Покажи сиськи.":
            call pylonController(2, 3, 1)
            citizen13 "Подруга, а что у тебя под футболкой?"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13

            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            # img показывает сиськи
            call showRandomImages(boobsImages, 4)
            call pylonController(2, 3, 1)
            citizen13 "Прекрасно, я вижу форму!"
            call pylonController(1, 1, 2)
            citizen13 "Не дурно!"
            call pylonController(2, 3, 1)
            $ showedBoobs = True
            jump citizen13_dialogue_pilon_loop13
        "Покажи попу.":
            call pylonController(2, 3, 1)
            citizen13 "А что у тебя сзади? Покажи!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13
            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4)
            call pylonController(2, 3, 1)
            # img показывает зад
            citizen13 "Оу, шикарная попка! Уж поверь, в этом я понимаю!"
            call pylonController(1, 1, 2)
            $ showedButt = True
            jump citizen13_dialogue_pilon_loop13
        "Достаточно на сегодня.":
            if showedBoobs == True and showedButt == True:
                $ add_money(0.5)
                citizen13 "Славно потрудилась, подруга! Вот, держи."
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            if showedBoobs == True or showedButt == True:
                citizen13 "Славно потрудилась, подруга! Вот, держи."
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                $ add_money(0.25)
                return
            #если не было
            citizen13 "Подруга, в следующий раз не халтурь."
            return
    return
