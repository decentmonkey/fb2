default citizen13BoobsNakesShowedLastDay = 0
default citizen13BoobsNakesShowedCount = -1
label citizen13_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
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
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen13_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_13_1
    m "Привет! Ты меня помнишь?"
    imgr Dial_Citizen_13_3
    citizen13 "Кончно помню, подруга! Ты разносишь флаеры с рекламой этих ужасных кебабов."
    m "Ну да, иногда."
    mt "А он выглядит дружелюбно и, похоже, я ему не интересна."
    m "Не будет ли у тебя лишних денег?"
    citizen13 "А тебе зачем, подруга? Если нужна контрацептив, дак у меня есть!"
    mt "Да за кого он меня принимает?"
    m "Нет, мне нужна наличка."
    citizen13 "Ну для тебя у меня есть немного, но ты же знаешь, что ничего не делается просто так."
    m "Ты мог бы мне одолжить."
    citizen13 "Ха-ха-ха. Подруга, я похож на идиота?"
    citizen13 "А вообще знаешь, раз тебе так нужны деньги, у меня есть идея. Пошли."
     # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_200
    call pylonController(2, 1) from _call_pylonController_94
    with fadelong
    citizen13 "Вот мы и пришли. Вечером тут полно народу. А теперь..."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen13_dialogue_pilon_loop13:
    call pylonController(1, 1) from _call_pylonController_95
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_96
            citizen13 "Подруга, а что у тебя под футболкой?"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_97
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13

            call pylonController(3, 3) from _call_pylonController_98
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает сиськи
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_17
            call pylonController(3, 3) from _call_pylonController_99
            citizen13 "Прекрасно, я вижу форму!"
            call pylonController(3, 3) from _call_pylonController_100
            citizen13 "Не дурно!"
            call pylonController(3, 1) from _call_pylonController_101
            w
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen13_dialogue_pilon_loop13
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_102
            citizen13 "А что у тебя сзади? Покажи!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_103
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13
            call pylonController(4, 5) from _call_pylonController_104
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_18
            call pylonController(4, 5) from _call_pylonController_105
            # img показывает зад
            citizen13 "Оу, шикарная попка! Уж поверь, в этом я понимаю!"
            call pylonController(4, 5) from _call_pylonController_106

            citizen13 "Подруга, а шлепни себя по попке! Меня это заводит!"
            label citizen13_dialogue_pilon_loop13_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothAssSpankCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothAssSpankCorruptionRequired] corruption"
                        jump citizen13_dialogue_pilon_loop13_1
                    m "Ладно."
                    call pylonController(3, 1) from _call_pylonController_107
                    with fade
                    w
                    # добавить звук шлепка
                    sound snd_slap1
                    call showRandomImages(assSpankImages, 1) from _call_showRandomImages_19
                    call pylonController(3, 1) from _call_pylonController_108
                    citizen13 "Ух! Да, подруга, ты прямо огонь!"
                    $ store_citizen_action("AssClothSpank", 1)
                "Ну уж нет!":
                    call pylonController(3, 1) from _call_pylonController_109
                    m "Не собираюсь, и так достаточно."
                    citizen13 "Нууу...Ну пожалуйста?"
                    m "Нет. Ты и так видел многое."

            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen13_dialogue_pilon_loop13
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_110
            citizen13 "Дорогая, сделай пару оборотов на пилоне, очень хочется на это посмотреть."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_111
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen13_dialogue_pilon_loop13
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_112
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages1, 4) from _call_showRandomImages_20
#            call pylonController(4, 5)
            citizen13 "Здорово, а ты молодец! Надо будет также попробовать."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_113
            with fade
            mt "Да уж, представляю что получится..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen13_dialogue_pilon_loop13
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen13BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen13BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen13BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen13BoobsNakesShowedCount == -1:
                call cit13_naked_boobs_1st() from _call_cit13_naked_boobs_1st
                if _return != False:
                    $ citizen13BoobsNakesShowedCount += 1
            else:
                if citizen13BoobsNakesShowedCount%2 == 0:
                    call cit13_naked_boobs_variant1() from _call_cit13_naked_boobs_variant1
                if citizen13BoobsNakesShowedCount%2 == 1:
                    call cit13_naked_boobs_variant2() from _call_cit13_naked_boobs_variant2
                $ citizen13BoobsNakesShowedCount += 1
            if _return != False:
                $ citizen13BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen13_dialogue_pilon_loop13



            call pylonController(4, 1) from _call_pylonController_114
            citizen13 "Прошлый раз ты меня обманула: не показала, что у тебя под футболкой. Давай теперь честно, мы же подруги."
            mt "Что он такое говорит? Он вообще нормальный?"
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_115
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            call pylonController(4, 5) from _call_pylonController_116
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикаснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_21
            call pylonController(4, 5) from _call_pylonController_117
            citizen13 "А тебе есть что показать! Когда нибудь у меня будут такие же!"
            call pylonController(4, 1) from _call_pylonController_118
            mt "Да не дай бог..."
            citizen13 "Подруга, а где ты такие сделала?"
            m "Что?! Они настоящие!"
            call pylonController(4, 5) from _call_pylonController_119
            citizen13 "Да?! Хорошо сохранилась, подруга!"
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen13_dialogue_pilon_loop13
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
                call pylonController(2, 1) from _call_pylonController_120
                citizen13 "Славно потрудилась, подруга! Вот, держи."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_121
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_122
            citizen13 "Подруга, в следующий раз не халтурь."
            return False
    return

# первый раз
label cit13_naked_boobs_1st:
    music Groove2_85
    img 12323
    with fade
    citizen13 "Подруга, скажу тебе по секрету, я очень тебе завидую!"
    img 12324
    m "Это почему?"
    img 12325
    citizen13 "Ну как же, у тебя есть две классных подружки!"
    img 12326
    mt "Неужели он про этих куриц, с которые ходят на фитнес?!"
    m "Ты это о ком?"
    img 12327
    citizen13 "Ну как же, о твоих красивых сисечках!"
    img 12328
    mt "И он туда же..."
    img 12329
    citizen13 "Покажи их мне, не стесняйся, а я дам тебе деньжат!"
    img 12330
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 12331
            m "Хватит и того, что ты уже видел!"
            return False
    img 12333
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12332
    citizen13 "Конечно, мы же подруги."
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 12334
    with fadelong
    w
    music Loved_Up
    img 12335
    with diss
    m "Можешь повернуться."
    m "Но руками не трогать!"
    img 12336
    citizen13 "Не разрешаешь? Ну хорошо..."
    # сиськи
    img 12337
    with diss
    w
    img 12338
    with diss
    w
    img 12339
    citizen13 "Вау! Тебе очень повезло с подружками!"
    # сиськи еще
    img 12340
    w
    img 12341
    w
    img 12342
    citizen13 "Такие большие и сочные!"
    # моника продолжает показывать
    img 12343
    w
    img 12344
    citizen13 "Ух, могу говорить о них хоть до утра!"
    # сиськи еще
    img 12345
    with diss
    w
    img 12346
    with diss
    citizen13 "Ох, подруга, как же я тебе завидую!"

    music Groove2_85
    img 12347
    with fade
    m "Ну ладно, хватит!"
    img 12348
    citizen13 "Ну хорошо, но ты должна обещать, что я увижу их снова!"
    img 12349
    m "Хорошего понемногу."
    $ nakedBoobsFirstly_Cit13 = True
    return True

# вариант 1
label cit13_naked_boobs_variant1:
    music Groove2_85
    img 12350
    with fade
    citizen13 "Дорогая, покажи мне своих подружек, никак не могу забыть нашу первую встречу!"
    img 12351
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12352
            m "Хватит и того, что ты уже видел!"
            return False
    img 12353
    with fade
    m "Хорошо."
    m "Только руками не трогай"
    img 12354
    citizen13 "Конечно, мы же подруги."
    sound snd_fabric1
    music Loved_Up
    img 12355
    with fadelong
    citizen13 "А тебе есть что показать! Когда нибудь у меня будут такие же!"
    img 12356
    with diss
    mt "Да неужели..."
    # сиськи
    img 12357
    with diss
    w
    img 12358
    with diss
    w
    img 12359
    with diss
    w
    img 12360
    citizen13 "Подруга, а где ты такие сделала?"
    music Groove2_85
    img 12361
    with fade
    m "Что?! Они настоящие!"
    img 12362
    citizen13 "Ой, да не обманывай! Ну честно, ты делала их у Джузеппе?"
    img 12363
    m "Я не знаю о ком ты говоришь..."
    img 12364
    citizen13 "А, ну да, конфеденциальность, понимаю..."
    citizen13 "Значит у него! Да, отличная работа!"
    img 12365
    with diss
    m "Они настоящие!"
    img 12366
    citizen13 "Ууу! Ладно, подруга, не злись!"
    citizen13 "Все таки они у тебя классные!"
    # сиськи
    music Loved_Up
    img 12367
    with diss
    w
    img 12368
    with diss
    w
    music Groove2_85
    img 12369
    with fade
    m "Ну ладно, хватит!"
    img 12370
    citizen13 "Ну хорошо, но ты должна обещать, что я увижу их снова!"
    img 12371
    with fade
    mt "Посмотрим..."
    return True

# вариант 2
label cit13_naked_boobs_variant2:
    music Groove2_85
    img 12373
    with fade
    citizen13 "Дорогая, сегодня особенный день и ты просто обязана показать мне свои сисечки!"
    img 12372
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12374
            m "Хватит и того, что ты уже видел!"
            return False
    img 12375
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12376
    citizen13 "Конечно, мы же подруги."
    # отворачивается, моника переодевается
    sound snd_fabric1
    img 12377
    with fadelong
    w
    music Loved_Up
    img 12378
    with diss
    w
    img 12379
    citizen13 "Ох, какие же они у тебя...Просто чудо."
    img 12380
    with diss
    mt "Тут не поспоришь."
    # сиськи
    img 12381
    with diss
    w
    img 12382
    with diss
    w
    img 12383
    with diss
    w
    music Groove2_85
    img 12384
    with fade
    citizen13 "Ты знаешь, где то я уже такие видел..."
    citizen13 "..."
    img 12385
    citizen13 "Точно, вспомнил! Вчера вечером я смотрел один фильм..."
    citizen13 "Дак там 10 мужчин... Хотя что я рассказываю, уверен, ты такое каждый день видешь."
    img 12386
    with diss
    mt "10 мужчин?! О боже..."
    # сиськи
    music Loved_Up
    img 12387
    with diss
    w
    img 12388
    with diss
    w
    img 12389
    citizen13 "Кстати, ты никогда не хотела стать актрисой?"
    img 12390
    m "Нет."
    img 12391
    citizen13 "Ну и зря. Уверен, у тебя бы получилось!"
    citizen13 "Мне бы очень хотелось увидеть тебя в кино."
    # сиськи
    img 12392
    with diss
    w
    img 12393
    with diss
    w
    img 12394
    with fade
    citizen13 "Подожди ка..."
    # Достает телефон и фоткает
    img 12395
    with diss
    w
    music stop
    img 12396
    with Dissolve(0.2)
    w
    call photoshop_flash() from _call_photoshop_flash_148
    w
    music Power_Bots_Loop
    img 12397
    with fade
    m "Эй! Что ты сделал?"
    img 12398
    citizen13 "Подруга, ты злишься? Я тебя сфотографировал!"
    citizen13 "Хочу показать твое фото одному моему знакомому, он снимает фильмы!"
    img 12399
    with diss
    m "Удали это фото немедленно!!!"
    # какая то поза моники или просто берет за шквар нигера...
    img 12401
    with diss
    w
    img 12402
    with diss
    w
    music Groove2_85
    img 12400
    with fade
    citizen13 "Ууу! Ладно, подруга, не злись!"
    citizen13 "Хорошо, хорошо, удаляю..."
    # удаляет
    img 12403
    w
    sound click1
    img 12404
    with diss
    w
    img 12405
    with fade
    citizen13 "Эх, подруга, зря ты так, могла бы стать знаменитой..."
    img 12406
    with diss
    mt "Я и так знаменита, только пока у меня не самая удачная полоса в жизни..."
    m "Ну ладно, хватит!"
    img 12407
    citizen13 "Ну хорошо, но ты должна обещать, что я увижу их снова!"
    img 12408
    with fade
    mt "Посмотрим..."
    return True
