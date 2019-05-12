default monicaGotJoint = False
label citizen3_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_3_1
    if monicaGotJoint == True:
        imgr Dial_Citizen_3_4
        citizen3 "Тебе нужно к Найджелу..."
        return
    if citizen3_offered_last_day == day:
        imgr Dial_Citizen_3_4
        citizen3 "В другой раз, я занят!"
        return
    citizen3 "Да, конечно, красотка!"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen3_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
#                    if renpy.random.randint(0, 3) =:
            imgr Dial_Citizen_3_4
            citizen3 "Не хочу, мне он не нужен."
            imgl Dial_Monica_Sandwich_0
            menu:
                "Попросить вежливо.":
                    #img Моника спрашивает
                    imgl Dial_Monica_Sandwich_1
                    m "Мистер, пожалуйста, возьмите флаер, Вы меня очень выручите."
                    imgr Dial_Citizen_3_2
                    citizen3 "Хорошо, я помогу тебе в обмен на небольшую услугу."
                    m "Какую еще услугу? Ты всего лишь возьмешь у меня флаер..."
                    citizen3 "Да, и попрошу тебя кое что передать моему другу Найджелу. Он на другой стороне улицы и ты его узнаешь по синему пуховику, в котором он круглый год."
                    imgl Dial_Monica_Sandwich_0
                    m "И что же я должна ему передать?"
                    mt "(Что за ?! )"
                    # citizen3показывает монике косяк
                    imgr Dial_Citizen_3_joint
                    m "Что это? Наркотики?!"
#                            imgr Dial_Citizen_3_3
                    citizen3 "(Шепотом) С каких пор травку слали приравнивать к наркотикам? Она абсолютно легальна. Ну дак что, поможешь мне?"
                    menu:
                        "Ладно.":
                            m "(Всего несколько метров...)Хорошо, я сделаю это."
                            #Моника берет косяк и отдает флаер.
                            $ add_inventory("joint", 1, True)
                            imgr Dial_Citizen_3_2
                            citizen3 "Не забудь сказать, что ты от Джека."
                            m "Хорошо"
                            citizen3 "Да, и самое главное: Ты должна будешь сказать Найджелу наш пароль, чтобы он понял, что все чисто."
                            m "Какой еще пароль?"
                            imgr Dial_Citizen_3_3
                            citizen3 "Потрогай мою сиську."
                            imgl Dial_Monica_Sandwich_2
                            m "(Что за?)"
                            imgl Dial_Monica_Sandwich_0
                            menu:
                                "Черт с ним.":
                                    imgl Dial_Monica_Sandwich_0
                                    m "И у кого хватило ума придумал такой пароль?!"
                                    citizen3 "А ты как думаешь? Конечно Найджел, но не переживай, как только ты произнесешь пароль, он сразу все поймет."
                                    call reduce_flyers() from _call_reduce_flyers_13
                                    m "Ладно, но если ты меня обманываешь..."
                                    #citizen33
                                    imgr Dial_Citizen_3_4
                                    citizen3 "Что ты, детка, зачем мне это?"
                                    $ monicaGotJoint = True
                                    return
                                "Ну уж нет, это слишком.":
                                    imgl Dial_Monica_Sandwich_2
                                    #злая моника
                                    $ remove_inventory("joint", 1, True)
                                    m "Я не буду говорить такие вещи!"
                                    return
                        "Ну уж нет.":
                            imgl Dial_Monica_Sandwich_2
                            m "Ты что, за дуру меня держишь?"
                            # смена арта у ситизена
                            imgr Dial_Citizen_3_4
                            citizen3 "Возвращайся, если передумаешь."
                            $ kebabWorkMonicaRefusedAmount += 1
                            return
                "Попросить настойчиво.":
                    imgl Dial_Monica_Sandwich_1
                    #img Моника спрашивает с недовольным выражением лица.
                    m "Неужели для Вас это так сложно?!."
                    imgr Dial_Citizen_3_4
                    citizen3 "Отвали."
                    imgl Dial_Monica_Sandwich_0
                    mt "(Вот засранец.)"
                    imgr Dial_Citizen_3_2
                    $ kebabWorkMonicaRefusedAmount += 1
#                        call reduce_flyers()
#                        citizen3 "Хорошо."
#                        img Dial_Citizen_3_3
#                        citizen3 "А что на нем? Ваш номер телефона?"
#                        "Вы девочка по вызову?"
#                        label citizen3_loop1:
#                            menu:
#                                "НЕТ!":
#                                    #img Моника злится
#                                    m "НЕТ!"
#                                "В общем нет, но... (disabled)":
#                                    jump citizen3_loop1
#                    else:
#                        img Dial_Citizen_3_3
#                        citizen3 "Я занят! Пожалуйста, не отвлекайте меня!"
#        "Уйти.":
#            pass
    return

# диалог доступен только когда моника не работает на раздаче флаеров
label citizen3_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_3_1
    m "Привет! Ты меня помнишь?"
    citizen3 "Конечно, помню, тебя сложно забыть."
    m "Могу тебе, кое что показать."
    citizen3 "Детка, ты говоришь о том, что я думаю?"
    imgr Dial_Citizen_3_3
    m "Возможно..."
    citizen3 "У меня много дел, но такое я пропустить не могу."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_242
    call pylonController(2, 1) from _call_pylonController_248
    with fade
    citizen3 "Ну что, тетя..."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen3_dialogue_pilon_loop3:
    call pylonController(1, 1) from _call_pylonController_249
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_250 #(2- камера со спины Моники, чуваки лицом, 3 - эмоция и поза чувака, 1 - Моника стоит спиной скрестив руки)
            citizen3 "Покажи ка свои сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen3_dialogue_pilon_loop3

            call pylonController(3, 3) from _call_pylonController_251 #(1 - камера со спины чуваков, Моника лицом, 1 - эмоция, 2 - Моника недовольно отвечает, жестикулируя)
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает сиськи
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_56
            call pylonController(3, 3) from _call_pylonController_252 #(2- камера со спины Моники, чуваки лицом, 3 - эмоция и поза чувака, 3 - Моника стоит спиной, показывая грудь в одежде)
            citizen3 "Детка, нет слов! Теперь сними свою курточку."
            call pylonController(3, 2) from _call_pylonController_253 #(1 - камера со спины чуваков, Моника лицом, 1 - эмоция, 2 - Моника недовольно отвечает, жестикулируя)
            m "Ну уж нет."
            call pylonController(3, 1) from _call_pylonController_254 #(2- камера со спины Моники, чуваки лицом, 3 - эмоция и поза чувака, 1 - Моника стоит спиной скрестив руки)
            citizen3 "Надо же с чего-то начинать..."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen3_dialogue_pilon_loop3
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_255
            citizen3 "Детка, повернись ко мне спиной. И покажи свою попку."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen3_dialogue_pilon_loop3
            call pylonController(4, 5) from _call_pylonController_256
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4) from _call_showRandomImages_57
            call pylonController(4, 5) from _call_pylonController_257
            citizen3 "Детка, ты красотка!"
            call pylonController(4, 5) from _call_pylonController_258
            citizen3 "Какая красота!"
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen3_dialogue_pilon_loop3
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_259
            citizen3 "Потанцуй для меня, не зря же сюда пришли."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_260
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen3_dialogue_pilon_loop3
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_261
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages2, 4) from _call_showRandomImages_58
#            call pylonController(4, 5)
            citizen3 "Прекрасно. Ты никогда не задумывалась этим зарабатывать? Раздача флаеров не очень прибыльное дело."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_262
            with fade
            mt "Ни за что..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen3_dialogue_pilon_loop3
        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart3startsCompleted == True:
            call pylonController(4, 1) from _call_pylonController_263
            citizen3 "Детка, хочу взглянуть еще раз на твои сиськи, только сними курточку."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_264
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen3_dialogue_pilon_loop3
            call pylonController(4, 5) from _call_pylonController_265
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_59
            call pylonController(4, 5) from _call_pylonController_266
            citizen3 "Очень хорошо. Сиськи как у Сары! Ты знакома с Сарой?"
            "Хотя почему я спрашиваю? Конечно вы знакомы."
            call pylonController(4, 1) from _call_pylonController_267
            citizen3 "Да ладно тебе, поговори со мной! Что думаешь?"
            m "Я не знаю о ком ты говоришь."
            call pylonController(4, 5) from _call_pylonController_268
            citizen3 "Ну как же, Сара! У нее лучшие сиськи на районе!"
            citizen3 "Надо будет как нибудь устроить соревнование. да, это отличная идея!"
            mt "Интересно, о ком это он? Хотя какая разница, у меня нет соперниц."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen3_dialogue_pilon_loop3
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
                call pylonController(2, 1) from _call_pylonController_269
                citizen3 "Ты сделала мой день, отлично потрудилась."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_270
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_271
            citizen3 "Похоже, я только зря потратил с тобой время..."
            return False
    return

# первый раз
label cit3_naked_boobs_1st:
    citizen3 "Ты знаешь, есть одна вещь, которая меня сильно интригует!"
    m "?"
    citizen3 "Уж очень мне интересно, как выглядят твои сиськи без этого чудесного топа!"
    mt "Они выглядят отлично!"
    citizen3 "Покажи их мне!"
    menu:
        "Почему бы и нет.":
            pass
        "Хватит и того, что ты уже видел!":
            m "Хватит и того, что ты уже видел!"
            return False
    m "Ладно, но руками не трогать!"
    # сиськи
    citizen3 "Ха! Я уверен, что где-то уже видел твои сиськи... Или не твои.."
    citizen3 "Не подскажешь, где я мог их видеть?"
    m "Нигде."
    # сиськи еще
    citizen3 "Странно, очень странно..."
    # citizen смотрит в сторону задумавшись, моника продолжает показывать
    citizen3 "Ладно, в другой раз вспомню..."
    $ nakedBoobsFirstly_Cit3 = True
    return True

# вариант 1
label cit3_naked_boobs_variant1:
    citizen3 "Дорогуша, покажи мне свои красивые сиськи!"
    citizen3 "Не за бесплатно конечно же."
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            m "Хватит и того, что ты уже видел!"
            return False
    m "Так и быть, только руками не трогать."
    # сиськи
    citizen3 "Да! Я вспомнил!"
    m "?"
    # сиськи еще
    citizen3 "Сиськи как у Сары! Ты знакома с Сарой?"
    citizen3 "Хотя почему я спрашиваю? Конечно вы знакомы."
    m "Я не знаю о ком ты говоришь."
    # сиськи еще
    citizen3 "Ну как же, Сара! У нее лучшие сиськи на районе!"
    citizen3 "Надо будет как нибудь устроить соревнование. да, это отличная идея!"
    mt "Интересно, о ком это он? Хотя какая разница, у меня нет соперниц."
    return True

# вариант 2
label cit3_naked_boobs_variant2:
    citizen3 "Детка, хочу взглянуть еще раз на твои сиськи, только сними курточку."
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            m "Хватит и того, что ты уже видел!"
            return False
    m "Так и быть, только руками не трогать."
    # сиськи
    citizen3 "Ага... Да..."
    # сиськи еще
    citizen3 "Хорошо... Вроде бы..."
    # сиськи еще
    mt "Интересно, что это с ним сегодня? Обычно он более разоворчив..."
    citizen3 "А что если?"
    # ситизен внезапно хватает монику за грудь
    # смена картинки, моника злая
    m "Ах ты говнюк! Какого черта?!"
    citizen3 "Что то не так?"
    m "Что то не так! Ты трогал мою грудь!"
    citizen3 "А, ты про это..."
    citizen3 "Это твоя вина! Я никак не мог вспомнить видел ли я где-то твою грудь и был вынужден ее поторгать, чтобы убедиться."
    m "Да я тебя сейчас..."
    citizen3 "Все, все, не злись! Я прошу прощения и заверяю тебя, что раньше твою грудь я не видел."
    citizen3 "И даже больше: она просто прекрасна, уж можешь поверить."
    citizen3  "И хоть я и не самый хороший парень, но я виноват, признаю."
    citizen3 "Как насчет компенсации? Знаю, что ты не против..."
    $ add_money(2);
    citizen3 "Наш конфликт улажен?"
    mt "Были бы мы не в этих трущебах, я бы тебя прибила..."
    m "...Да."
    return True
