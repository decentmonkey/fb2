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
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart4startsCompleted == True:
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
    img 12163
    citizen8 "Предлагаю вывести нашу сделку на новый уровень!"
    img 12164
    m "Что ты имеешь ввиду?"
    img 12165
    citizen8 "Все просто: показываешь голые сиськи, получаешь больше денег."
    citizen8 "Ты согласна?"
    img 12166
    menu:
        "Почему бы и нет.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12167
            m "Хватит и того, что ты уже видел!"
            return False
    img 12168
    m "Хорошо."
    m "Отвернись!"
    img 12169
    citizen8 "Хм...На первый раз отвернусь..."
    # отворачивается, моника переодевается...
    img 12170
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    img 12171
    w
    img 12172
    w
    img 12173
    citizen8 "Да, новая сделка того стоит."
    citizen8 "Хороший размер и форма."
    # сиськи еще
    img 12174
    w
    img 12175
    w
    img 12176
    citizen8 "Какая красота!"
    # моника продолжает показывать
    img 12177
    w
    img 12178
    w
    img 12179
    citizen8 "На сколько ты оцениваешь свою грудь?!"
    img 12180
    menu:
        "1000$":
            img 12181
            m "1000$"
            img 12182
            citizen8 "Да, она бы могла столько стоить, но не здесь!"
            citizen8 "Учитывая обстоятельства, свой дополнительный доллар ты заработала."
            pass
        "Ни на сколько!":
            img 12183
            m "Ни на сколько!"
            img 12184
            citizen8 "Гордость? Мне нравится."
            citizen8 "Возможно скоро ты узнаешь, что у всего есть цена."
            pass
    img 12185
    citizen8 "Ладно, сделка состоялась. Можешь одеваться, если, конечно, хочешь."
    img 12186
    mt "Конечно хочу!"
    $ nakedBoobsFirstly_Cit8 = True
    return True

# вариант 1
label cit8_naked_boobs_variant1:
    img 12187
    citizen8 "Ну что, продолжим! Я уже даже подзабыл какая у тебя грудь."
    citizen8 "Покажи мне ее!"
    img 12188
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12189
            m "Хватит и того, что ты уже видел!"
            return False
    img 12190
    m "Хорошо."
    m "Но руками не трогать!"
    # сиськи
    img 12191
    w
    img 12192
    w
    img 12193
    citizen8 "Красота!"
    # сиськи еще
    img 12194
    w
    img 12195
    w
    img 12196
    citizen8 "Знаешь, цена нашей сделки пропорционально твоему размеру груди."
    citizen8 "Думаю, ты догадалась, что нужно, чтобы получать больше."
    img 12197
    mt "Конечно догадалась...Извращенец."
    # моника продолжает показывать
    img 12198
    w
    img 12199
    w
    img 12200
    citizen8 "Вернемся к сделка. Покажи мне язычек."
    img 12201
    menu:
        "Хорошо.":
            # моника высовывает язык
            img 12202
            w
            img 12203
            citizen8 "Нет, это не похоже на честную сделку."
            citizen8 "Я же вижу, что ты халтуришь."
            citizen8 "Открой рот шире и высунь язык как следует!"
            img 12204
            menu:
                "Хорошо.":
                    # моника высовывает язык большие
                    img 12205
                    w
                    img 12206
                    citizen8 "Вот, теперь я вижу, что ты стараешься."
                    pass
                "Это максимум!":
                    img 12207
                    m "Я больше не могу!"
                    img 12208
                    citizen8 "Обманщица. Ну да ладно. Но я это запомню..."
                    pass
            pass
        "Ну уж нет!":
            img 12209
            m "Ну уж нет!"
            img 12210
            citizen8 "Странно, раньше ты была чуть сговорчивее."
            citizen8 "Ну как хочешь..."
            pass
    img 12211
    citizen8 "Ладно, сделка состоялась. Можешь одеваться, если, конечно, хочешь."
    img 12212
    mt "Конечно хочу!"
    return True

# вариант 2
label cit8_naked_boobs_variant2:
    img 12213
    citizen8 "Давай еще разок взглянем на твою грудь."
    img 12214
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12215
            m "Хватит и того, что ты уже видел!"
            return False
    img 12216
    m "Хорошо."
    m "Отвернись!"
    img 12217
    citizen8 "Знаешь, не сегодня."
    img 12218
    m "Не поняла."
    img 12219
    citizen8 "Переодевайся, а я посмотрю."
    img 12220
    mt "Снимать одежду, когда на меня смотрит незнакомый мужчина..."
    mt "Хотя какой он мужчина... Но все равно... Стоит ли мне это делать?"
    img 12221
    menu:
        "Хорошо.":
            img 12222
            m "Ну... Ладно."
            # моника переодевается...
            img 12223
            w
            img 12224
            citizen8 "А знаешь, это в каком то смысле лучше, чем просто смотреть!"
            # моника переодевается...
            img 12225
            w
            img 12226
            citizen8 "Скажи, тебя это заводит? Хотя что за вопросы, я знаю, что да."
            img 12227
            mt "Ничего ты не знаешь..."
            pass
        "Нет, я так не могу!":
            img 12228
            m "Нет, я так не могу!"
            img 12229
            citizen8 "Хорошо, тогда эта часть сделки анулируется."
            return False
    # сиськи
    img 12230
    w
    img 12231
    w
    img 12232
    w
    img 12233
    citizen8 "Постой."
    img 12234
    m "Что?"
    # моника просто стоит с голыми сиськами
    img 12235
    w
    img 12236
    citizen8 "Если не знать меры, можно превратиться в животное."
    citizen8 "Не подумай ничего плохого, твои сиськи прекрасны."
    img 12237
    mt "Он что, меня отшивает?!"
    img 12238
    citizen8 "Я уже посмотрел как ты переодеваешься и пока этого хватит."
    citizen8 "Но ты выполнила свою часть сделки отлично!"
    img 12239
    mt "Странный тип..."
    return True
