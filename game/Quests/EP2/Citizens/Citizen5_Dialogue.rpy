label citizen5_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_5_1
    if citizen5_offered_last_day == day:
        imgr Dial_Citizen_5_4
        citizen5 "Мистер занят! Вы отнимать у Мистера время!"
        return
    citizen5 "Что Вы хотеть от Мистера?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen5_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen5_refuse_probability) > 0:
                imgr Dial_Citizen_5_2
                citizen5 "Да, да, конечно...Я взять этот флаер... Но ты мне должна. Акира сан никогда не делает ничего просто так."
                mt "О чем это он?"
                imgr Dial_Citizen_5_3
                citizen5 "Я думать Вы предлагать место?"
                call reduce_flyers() from _call_reduce_flyers_11
                menu:
                    "Я ничего не предлагаю! Просто возьмите флаер!":
                        $ kebabWorkHarassmentAmount +=1
                        #img Моника злится
                        m "Я ничего не предлагаю! Просто возьмите флаер!"
                    "Место для чего?":
                        m "Место для чего?"
                        citizen5 "Место для развлечения! Я очень любить трогать большие попы!"
                        m "Что вы такое говорите?"
                        mt "Лучше пойду отсюда..."
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."
            else:
                imgr Dial_Citizen_5_4
                citizen5 "У Мистера нет времени вашего места!"
                #img Моника злится
                imgl Dial_Monica_Sandwich_0
                m "Какого еще места?"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen5_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_5_1
    m "Привет! Я могу тебе предложить одну вещь."
    imgr Dial_Citizen_5_3
    citizen5 "Вы предлагать место?"
    m "Ну да, мы можем сходить с вами в одно место."
    citizen5 "Да, да, место для утех. Вы мне показы, я вам американские деньги."
    mt "И откуда он такой?"
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_216
    call pylonController(2, 1) from _call_pylonController_194
    with fadelong
    citizen5 "Очень хорошо! Давай начнем."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen5_dialogue_pilon_loop5:
    call pylonController(1, 1) from _call_pylonController_195
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_196
            citizen5 "Я хотеть смотреть твои груди."
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_197
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(3, 3) from _call_pylonController_198
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_48
            call pylonController(3, 3) from _call_pylonController_199
            # img показывает сиськи
            citizen5 "Да, твои обе груди прекрасны!"
            call pylonController(3, 3) from _call_pylonController_200
            citizen5 "Я очень ошеломлен!"
            call pylonController(3, 3) from _call_pylonController_201
            citizen5 "Я почти потерял дар говорить при виде этих великолепных сисек!"
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_202
            citizen5 "Оголи свою попку."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_203
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(4, 5) from _call_pylonController_204
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_49
            call pylonController(4, 5) from _call_pylonController_205
            # img показывает зад
            citizen5 "Твоя попка красивее всех поп в моей стране!"
            call pylonController(4, 5) from _call_pylonController_206
            citizen5 "Готов смотреть на нее все время."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_207
            citizen5 "Я желаю ведеть тебя танцующей."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_208
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_209
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages4, 4) from _call_showRandomImages_50
#            call pylonController(4, 5)
            citizen5 "Ооо! Какие красивые изгибания!"
            citizen5 "Они похожи гору Фудзи, только две. Ты быда там?"
            call pylonController(4, 1) from _call_pylonController_210
            m "Нет, и не очень то и хочется."
            citizen5 "Вот и зря! Побывать нужно незамедлительно!"
            call pylonController(4, 5) from _call_pylonController_211
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_212
            with fade
            mt "Как же он странно разговаривает..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart4startsCompleted == True:
            call pylonController(4, 1) from _call_pylonController_213
            citizen5 "Оголи свои манящие груди."
            mt "Ему бы книги писать..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_214
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(4, 5) from _call_pylonController_215
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_51
            call pylonController(4, 5) from _call_pylonController_216
            citizen5 "Я только что лицезрел гору Фудзи, точнее две!"
            call pylonController(4, 1) from _call_pylonController_217
            w
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen5_dialogue_pilon_loop5
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
                call pylonController(2, 1) from _call_pylonController_218
                citizen5 "Ты дать мистеру величайшее наслаждение. Мы видеться скоро вновь!"
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_219
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_220
            citizen5 "Мистер разочарован, он ничего не посмотрел."
            return False
    return

# первый раз
label cit5_naked_boobs_1st:
    img 11879
    citizen5 "Может быть ты согласна показать мне свои груди?"
    img 11880
    m "Думаю, ты уже их видел."
    img 11881
    citizen5 "Да, конечно, но было бы прекрасно их оголить. У мистера есть деньги! Много денег!"
    img 11882
    mt "Он выглядит не очень умным... Возможно это мой шанс получить несколько сотен, а может быть и тысяч долларов..."
    img 11883
    m "И сколько же у мистера денег?!"
    img 11884
    citizen5 "У мистера очень много денег! Тебе нужно верить мистеру!"
    citizen5 "Дак ты оголишь свои груди?"
    img 11885
    menu:
        "Почему бы и нет.":
            pass
        "Хватит и того, что ты уже видел!":
            img 11886
            m "Хватит и того, что ты уже видел!"
            return False
    img 11887
    m "Отвернись!"
    img 11888
    citizen5 "Да, конечно, мистер отвернется."
    # отворачивается, моника переодевается...
    img 11889
    w
    img 11890
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    img 11891
    w
    img 11892
    w
    img 11893
    citizen5 "Невероятно! Именно такими я себе их и представлял!"
    citizen5 "Они изумительны!"
    img 11894
    mt "Ну прямо мастер комплиментов..."
    # сиськи еще
    img 11895
    w
    img 11896
    w
    img 11897
    citizen5 "Какая красота!"
    # моника продолжает показывать
    img 11898
    w
    img 11899
    w
    img 11900
    w
    img 11901
    m "Ну ладно, хватит с тебя."
    img 11902
    citizen5 "Как? Мистер еще не до конца насладился!"
    img 11903
    m "А где деньги мистера?"
    img 11904
    citizen5 "У меня нет сегодня моих миллионов! Только несколько зеленых бумажек. Но ты их получишь."
    img 11905
    mt "Миллионов? Интересно, это правда? Хотя вряд ли у него столько денег..."
    img 11906
    m "Ну раз миллионов нет, тогда на сегодня все."
    img 11907
    citizen5 "Ооо...Ну ничего, скоро ты их увидишь!"
    $ nakedBoobsFirstly_Cit5 = True
    return True

# вариант 1
label cit5_naked_boobs_variant1:
    img 11908
    citizen5 "Оголи свои манящие груди."
    img 11909
    mt "Ему бы книги писать..."
    img 11910
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 11911
            m "Хватит и того, что ты уже видел!"
            return False

    # отворачивается, моника переодевается...
    img 11912
    m "Хорошо."
    img 11913
    w
    img 11914
    m "Только руками не трогать!"
    # сиськи
    img 11914
    w
    img 11915
    w
    img 11916
    w
    img 11917
    citizen5 "Лучезарно! Кажется, в такие моменты я попадаю в рай!"
    img 11918
    mt "Ого... Да он прямо поплыл! Кажется, он говорил о миллионах..."
    # сиськи еще
    img 11919
    w
    img 11920
    w
    img 11921
    m "Тебе нравится?"
    img 11922
    citizen5 "О да! Это великолепно!"
    # сиськи еще
    img 11923
    w
    img 11924
    w
    img 11925
    citizen5 "Мне кажется, я видел их во сне! Или я гулял между холмов..."
    img 11926
    m "Кстати, кажется, ты в прошлый раз говорил о миллионах?"
    img 11927
    citizen5 "Да, да! У мистера есть миллионы!"
    # сиськи еще
    img 11928
    w
    img 11929
    w
    img 11930
    m "Может быть ты дашь мне несколько?"
    # сиськи еще
    img 11931
    w
    img 11932
    w
    img 11933
    citizen5 "Да, конечно! Мистер даст тебе много миллионов! Но они у мистера дома."
    img 11934
    mt "Что он несет? Неужели у него и правда есть столько денег..."
    img 11935
    m "Чтож, тогда на сегодня все."
    img 11936
    citizen5 "Ох, какая жалость! Мне очень стыдно, но я принесу мои миллионы в следующий раз!"
    img 11937
    m "Хорошо, буду ждать."
    return True

# вариант 2
label cit5_naked_boobs_variant2:
    img 11938
    citizen5 "Оголи свои манящие груди."
    img 11939
    mt "Ему бы книги писать..."
    img 11940
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 11941
            m "Хватит и того, что ты уже видел!"
            return False
    img 11942
    m "Отвернись!"
    # отворачивается, моника переодевается...
    img 11943
    w
    img 11944
    w
    img 11945
    m "Можешь повернуться."
    m "Только руками не трогать!"
    # сиськи
    img 11946
    w
    img 11947
    w
    img 11948
    citizen5 "Мистер вспомнил! Он принес деньги! Очень много денег!"
    img 11949
    mt "Серьезно?! Думаю, стоит ему подиграть..."
    img 11950
    m "Мистер обещал дать мне много миллионов!"
    # сиськи еще
    img 11951
    w
    img 11952
    w
    img 11953
    m "Мистеру нравится?"
    img 11954
    citizen5 "Конечно да!"
    # сиськи еще
    img 11955
    w
    img 11956
    w
    img 11957
    m "Мистер готов дать мне 400 миллионов?"
    # сиськи еще
    img 11958
    w
    img 11959
    w
    img 11960
    citizen5 "Да, да, готов! Но у мистера небольшое условие."
    citizen5 "Мистер хочет увидеть на тебе это."
    # показывает зажим для сосков
    citizen5 "Мистер будет очень благодарен когда увидит на тебе это."
    mt "Что это еще такое?! Что делать?"
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            m "Ну уж нет! Мне не нужны твои извращенные штучки!"
            return False
    mt "Черт, а что если у него и правда есть много денег..."
    m "Хорошо, но только быстро."
    # моника зажимает соски
    m "Готово."
    citizen5 "Это самое лучшее представление, которое я видел!"
    citizen5 "Подожди, постой так немного!"
    # сиськи - еще поза
    citizen5 "Ох, это нечто!"
    # сиськи еще
    citizen5 "Мистер очень доволен, вот твои миллионы!"
    # Дает ей миллионы долларов Зимбабве )
    m "Что это такое?"
    citizen5 "Я даю тебе миллионы долларов!"
    m "Зимбабве?! Да не них здесь ничего не купить!"
    citizen5 "Мистер не знает, но ты теперь миллионер!!!"
    mt "Черт, похоже он очень глуп, даже говорить с ним нет смысла..."
    return True
