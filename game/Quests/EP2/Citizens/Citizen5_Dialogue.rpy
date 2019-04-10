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
                call reduce_flyers()
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
    call change_scene("hostel_edge_1_a", "Fade_long")
    call pylonController(2, 1)
    with fadelong
    citizen5 "Очень хорошо! Давай начнем."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen5_dialogue_pilon_loop5:
    call pylonController(1, 1)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1)
            citizen5 "Я хотеть смотреть твои груди."
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(3, 3)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(3, 3)
            # img показывает сиськи
            citizen5 "Да, твои обе груди прекрасны!"
            call pylonController(3, 3)
            citizen5 "Я очень ошеломлен!"
            call pylonController(3, 3)
            citizen5 "Я почти потерял дар говорить при виде этих великолепных сисек!"
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Покажи попу.":
            call pylonController(4, 1)
            citizen5 "Оголи свою попку."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(4, 5)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4)
            call pylonController(4, 5)
            # img показывает зад
            citizen5 "Твоя попка красивее всех поп в моей стране!"
            call pylonController(4, 5)
            citizen5 "Готов смотреть на нее все время."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1)
            citizen5 "Я желаю ведеть тебя танцующей."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6)
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages4, 4)
#            call pylonController(4, 5)
            citizen5 "Ооо! Какие красивые изгибания!"
            citizen5 "Они похожи гору Фудзи, только две. Ты быда там?"
            call pylonController(4, 1)
            m "Нет, и не очень то и хочется."
            citizen5 "Вот и зря! Побывать нужно незамедлительно!"
            call pylonController(4, 5)
            $ restore_music()
            call pylonController(4, 1)
            with fade
            mt "Как же он странно разговаривает..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen5_dialogue_pilon_loop5
        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart3startsCompleted == True:
            call pylonController(4, 1)
            citizen5 "Оголи свои манящие груди."
            mt "Ему бы книги писать..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen5_dialogue_pilon_loop5
            call pylonController(4, 5)
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4)
            call pylonController(4, 5)
            citizen5 "Я только что лицезрел гору Фудзи, точнее две!"
            call pylonController(4, 1)
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
                call pylonController(2, 1)
                citizen5 "Ты дать мистеру величайшее наслаждение. Мы видеться скоро вновь!"
                $ add_money(earnedMoney)
                call pylonController(1, 1)
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1)
            citizen5 "Мистер разочарован, он ничего не посмотрел."
            return False
    return
