default citizen8_varA = 1

label citizen8_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
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
                $ citizen8_varA += 1

                # следующая реплика будет зависеть от значения созданной переменной A
                if citizen8_varA%2 == 0:
                    citizen8 "Показала язык." # if A == 1
                if citizen8_varA%2 == 1:
                    citizen8 "Шлепнула себя по попе. " # if A == 2
                # ...
                mt "Что за бред. Это только ради того, чтобы он взял флаер?! Что же делать..."
                menu:
                    "Выполнить просьбу.":
                        m "Ну ладно."
                        mt "Скорее бы уже раздать эти флаеры..."
                        if citizen8_varA%2 == 0:
                            imgl Dial_Monica_Sandwich_3
                        if citizen8_varA%2 == 1:
                            imgl Dial_Monica_Sandwich_4
                        # картинка - моника показывает язык (опять же картинка будет зависеть от A)
                        imgr Dial_Citizen_8_3
                        citizen8 "Миленько, ты отлично справилась."
                        call reduce_flyers() from _call_reduce_flyers_4
                    "Ну уж нет, извращенец!":
                        m "Извращенец! Я не собираюсь выполнять твои извращенные просьбы!"
                        return
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
                        m "А что бы вы хотели?"
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
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen8_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_8_1
    m "Привет! Ты меня помнишь?"
    imgr Dial_Citizen_8_3
    citizen8 "Конечно! Твой язычек сложно забыть!"
    m "Я хочу предложить сделку: ты мне дашь денег. Взамен я разрешу тебе на меня посмотреть."
    citizen8 "Звучит как честная сделка, но лучше совершить ее не здесь."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_188
    call pylonController(2, 1) from _call_pylonController_68
    with fadelong
    citizen8 "С чего бы нам начать..."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen8_dialogue_pilon_loop8:
    call pylonController(1, 1) from _call_pylonController_69
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_70
            citizen8 "Покажи мне свои сиськи."
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_71
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen8_dialogue_pilon_loop8
            call pylonController(3, 3) from _call_pylonController_72
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_12
            call pylonController(3, 3) from _call_pylonController_73
            # img показывает сиськи
            citizen8 "Хорошо, а теперь высунь язык!"
            label citizen8_dialogue_pilon_loop8_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothBoobsTongueCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothBoobsTongueCorruptionRequired] corruption"
                        jump citizen8_dialogue_pilon_loop8_1
                    m "Ладно."
                    call pylonController(3, 4) from _call_pylonController_74
                    with fade
                    w
                    call showRandomImages(boobsImagesTonque, 1) from _call_showRandomImages_13
                    call pylonController(3, 4) from _call_pylonController_75
                    # img показывает сиськи и язык
                    citizen8 "Чудно, а ты молодец!"
                    $ store_citizen_action("BoobsClothTongue", 1)
                "Ну уж нет!":
                    call pylonController(3, 1) from _call_pylonController_76
                    m "Не собираюсь, и так достаточно."
                    citizen8 "Ладно, но с этим цена сделки могла стать выше."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen8_dialogue_pilon_loop8
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_77
            citizen8 "Развернись и поверти задом."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_78
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen8_dialogue_pilon_loop8
            call pylonController(4, 5) from _call_pylonController_79
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_14
            call pylonController(4, 5) from _call_pylonController_80
            # img показывает зад
            citizen8 "Молодец, цена нашей сделки растет."
            mt "И почему он говорит все об этой сделке. Я же вроде не продаю себя..."
            call pylonController(4, 5) from _call_pylonController_81
            citizen8 "О да!"
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen8_dialogue_pilon_loop8
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_82
            citizen8 "Потанцуй, пилон сзади."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_83
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen8_dialogue_pilon_loop8
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_84
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages7, 4) from _call_showRandomImages_15
#            call pylonController(4, 5)
            citizen8 "Нормально, но нужно еще тренироваться и тренироваться."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_85
            with fade
            mt "Не думаю, что буду это делать часто..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen8_dialogue_pilon_loop8
        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart3startsCompleted == True:
            call pylonController(4, 1) from _call_pylonController_86
            citizen8 "Покажи мне грудь, только теперь без одежды."
            mt "Он и вправду говорит как бизнесмен, заключающий сделку..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_87
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen8_dialogue_pilon_loop8
            call pylonController(4, 5) from _call_pylonController_88
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_16
            call pylonController(4, 5) from _call_pylonController_89
            citizen8 "Очень хорошо. Отличный старт."
            call pylonController(4, 1) from _call_pylonController_90
            mt "Что значит старт?"
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen8_dialogue_pilon_loop8
        "Достаточно на сегодня.":
            $ earnedMoney = 0
            if showedBoobs == True or showedButt == True or showedDance == True or showedNakedBoobs == True:
                if showedBoobs == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedButt == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedDance == True:
                    $ earnedMoney += monicaWhoringClothDanceMoney
                if showedNakedBoobs == True:
                    $ earnedMoney += monicaWhoringNakedBoobsMoney
                call pylonController(2, 1) from _call_pylonController_91
                citizen8 "Славно потрудилась. Вот, держи."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_92
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_93
            citizen8 "Сделки нет, ты не выполнила свою часть."
            return False
    return

# первый раз
label cit8_naked_boobs_1st:
    citizen8 "Предлагаю вывести нашу сделку на новый уровень!"
    m "Что ты имеешь ввиду?"
    citizen8 "Все просто: показываешь голые сиськи, получаешь больше денег."
    citizen8 "Ты согласна?"
    menu:
        "Почему бы и нет.":
            pass
        "Хватит и того, что ты уже видел!":
            m "Хватит и того, что ты уже видел!"
            return False
    m "Хорошо."
    m "Отвернись!"
    citizen8 "Хм...На первый раз отвернусь..."
    # отворачивается, моника переодевается...
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    citizen8 "Да, новая сделка того стоит."
    citizen8 "Хороший размер и форма."
    # сиськи еще
    citizen8 "Какая красота!"
    # моника продолжает показывать
    citizen8 "На сколько ты оцениваешь свою грудь?!"
    menu:
        "1000$":
            m "1000$"
            citizen8 "Да, она бы могла столько стоить, но не здесь!"
            citizen8 "Учитывая обстоятельства, свой дополнительный доллар ты заработала."
            pass
        "Ни на сколько!":
            m "Ни на сколько!"
            citizen8 "Гордость? Мне нравится."
            citizen8 "Возможно скоро ты узнаешь, что у всего есть цена."
            pass
    citizen8 "Ладно, сделка состоялась. Можешь одеваться, если, конечно, хочешь."
    mt "Конечно хочу!"
    $ nakedBoobsFirstly_Cit8 = True
    return True

# вариант 1
label cit8_naked_boobs_variant1:
    citizen8 "Ну что, продолжим! Я уже даже подзабыл какая у тебя грудь."
    citizen8 "Покажи мне ее!"
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            m "Хватит и того, что ты уже видел!"
            return False
    m "Хорошо."
    m "Отвернись!"
    citizen8 "Ну...Ладно."
    # отворачивается, моника переодевается...
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    citizen8 "Красота!"
    # сиськи еще
    citizen8 "Знаешь, цена нашей сделки пропорционально твоему размеру груди."
    citizen8 "Думаю, ты догадалась, что нужно, чтобы получать больше."
    mt "Конечно догадалась...Извращенец."
    # моника продолжает показывать
    citizen8 "Вернемся к сделка. Покажи мне язычек."
    menu:
        "Хорошо.":
            # моника высовывает язык
            citizen8 "Нет, это не похоже на честную сделку."
            citizen8 "Я же вижу, что ты халтуришь."
            citizen8 "Открой рот шире и высунь язык как следует!"
            menu:
                "Хорошо.":
                    # моника высовывает язык большие
                    citizen8 "Вот, теперь я вижу, что ты стараешься."
                    pass
                "Это максимум!":
                    m "Я больше не могу!"
                    citizen8 "Обманщица. Ну да ладно. Но я это запомню..."
                    pass
            pass
        "Ну уж нет!":
            m "Ну уж нет!"
            citizen8 "Странно, раньше ты была чуть сговорчивее."
            citizen8 "Ну как хочешь..."
            pass
    citizen8 "Ладно, сделка состоялась. Можешь одеваться, если, конечно, хочешь."
    mt "Конечно хочу!"
    return True

# вариант 2
label cit8_naked_boobs_variant2:
    citizen8 "Давай еще разок взглянем на твою грудь."
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            m "Хватит и того, что ты уже видел!"
            return False
    m "Хорошо."
    m "Отвернись!"
    citizen8 "Знаешь, не сегодня."
    m "Не поняла."
    citizen8 "Переодевайся, а я посмотрю."
    mt "Снимать одежду, когда на меня смотрит незнакомый мужчина..."
    mt "Хотя какой он мужчина... Но все равно... Стоит ли мне это делать?"
    menu:
        "Хорошо.":
            m "Ну... Ладно."
            # моника переодевается...
            citizen8 "А знаешь, это в каком то смысле лучше, чем просто смотреть!"
            # моника переодевается...
            citizen8 "Скажи, тебя это заводит? Хотя что за вопросы, я знаю, что да."
            mt "Ничего ты не знаешь..."
            pass
        "Нет, я так не могу!":
            m "Нет, я так не могу!"
            citizen8 "Хорошо, тогда эта часть сделки анулируется."
            return False
    # сиськи
    citizen8 "Постой."
    m "Что?"
    # моника просто стоит с голыми сиськами
    citizen8 "Если не знать меры, можно превратиться в животное."
    citizen8 "Не подумай ничего плохого, твои сиськи прекрасны."
    mt "Он что, меня отшивает?!"
    citizen8 "Я уже посмотрел как ты переодеваешься и пока этого хватит."
    citizen8 "Но ты выполнила свою часть сделки отлично!"
    mt "Странный тип..."
    return True
