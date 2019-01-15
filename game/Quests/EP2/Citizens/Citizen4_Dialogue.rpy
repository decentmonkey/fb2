label citizen4_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_4_1
    if citizen4_offered_last_day == day:
        imgr Dial_Citizen_4_4
        citizen4 "Нельзя!"
        return
    citizen4 "Да?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen4_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen4_refuse_probability) > 0:
                imgr Dial_Citizen_4_2
                call reduce_flyers() from _call_reduce_flyers_2
                citizen4 "Хорошо."
                citizen4 "А что на нем?"
                m "Это реклама вкусного кебаба... Там же написано!"
                imgr Dial_Citizen_4_3
                citizen4 "А я подумал Вы решили познакомиться со мной!"
                menu:
                    "У меня нет желания знакомиться с Вами!":
                        $ kebabWorkHarassmentAmount +=1
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "У меня нет желания знакомиться с Вами!"
                    "Что Вы подразумеваете под знакомством?":
                        m "Что вы имеете ввиду?"
                        сitizen4 "Я бы хотел узнать по ближе такую красотку. Думаю, мы бы договорились."
                        m "Договорились о чем?"
                        citizen4 "Что за вопросы? Обычно девушки вашей профессии это понимают."
                        mt "Да что за люди здесь живут?! Всем надо одно и то же..."
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."
            else:
                imgr Dial_Citizen_4_4
                citizen4 "Давайте в другой раз!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen4_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_4_1
    m "Привет! Помню, ты хотел познакомиться поближе?"
    imgr Dial_Citizen_4_3
    citizen4 "Конечно, давай познакомимся."
    m "Ну я не о близком знакомстве...Немного о другом."
    citizen4 "Да не вопрос, я понимаю о чем речь. Любой из нашего района тебя поймет с полуслова."
    # уходят к пилону.
    $ citizenId = 4
    call falling_path_store_customer()
    citizen4 "Ну что, давай начнем."
    $ showedBoobs = False
    $ showedButt = False
    label citizen4_dialogue_pilon_loop4:
    menu:
        "Покажи сиськи.":
            call pylonController(2, 3, 1)
            citizen4 "Покажи мне свои сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(2, 3, 1)
            # img показывает сиськи
            citizen4 "Да, очень хорошо, но я видел сиськи и получше!"
            call pylonController(1, 1, 2)
            mt "Козел!"
            call pylonController(2, 3, 1)
            citizen4 "Хотя весьма не плохо."
            $ showedBoobs = True
            jump citizen4_dialogue_pilon_loop4
        "Покажи попу.":
            call pylonController(2, 3, 1)
            citizen4 "Покажи свой задницу."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(1, 1, 2)
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4)
            call pylonController(2, 3, 1)
            citizen4 "Красивая задница, но я люблю побольше!"
            call pylonController(1, 1, 2)
            citizen4 "Но ее можно увеличить, подумай об этом."
            $ showedButt = True
            jump citizen4_dialogue_pilon_loop4
        "Достаточно на сегодня.":
            if showedBoobs == True and showedButt == True:
                $ add_money(0.5)
                citizen4 "А ты ничего такая, надо будет вернуться к нашему знакомству. Держи, заслужила."
                # дает монике копейку если были показы
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            if showedBoobs == True or showedButt == True:
                citizen4 "А ты ничего такая, надо будет вернуться к нашему знакомству. Держи, заслужила."
                # дает монике копейку если были показы
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                $ add_money(0.25)
                return
            #если не было
            citizen4 "Какое то не продуктивное вышло знакомство. Надеюсь, в другой раз будет лучше."
            return
    return
