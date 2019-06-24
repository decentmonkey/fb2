default pylonpart2startsCompleted = False
default pylonpart3startsCompleted = False
default pylonpart4startsCompleted = False

label citizen15_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
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
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."

            else:
                imgr Dial_Citizen_15_4
                citizen15 "Я важная персона! У меня нет времени на флаеры!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

label citizen15_dialogue_after_showing_naked_boobs: #Моника думает после показа голых сикек за 50 баксов
    mt "ыыы"
    $ add_money(-50)
    return


label citizen15_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_15_1
    m "Привет! Кажется, ты говорил, что я могу заработать денег..."
    imgr Dial_Citizen_15_3
    citizen15 "Да, и сейчас говорю. Только учти: у меня от таких как ты отбоя нет. Ты должна мне показать что-то особенное."
    mt "Самодовольный козел...Да кем он себя возомнил? Черт, мне нужны деньги."
    m "Куда ты хотел пойти?"
    citizen15 "Обычно девочки сами придумывают куда меня вести."
    "Не забывай, у меня нет отбоя от таких как ты."
    mt "!!!"
    m "Знаю"
    citizen15 "Ты же наверняка видела подворотню с пилоном? Вот туда и пойдем."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_215
    call pylonController(2, 1) from _call_pylonController_175
    with fadelong
    citizen15 "Ну что, начинай, только не разочаруй меня."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen15_dialogue_pilon_loop15:
    call pylonController(1, 1) from _call_pylonController_176
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_177
            citizen15 "Для начала сиськи, показывай!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_178
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15

            call pylonController(3, 3) from _call_pylonController_179
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_45
            call pylonController(5, 3) from _call_pylonController_180
            citizen15 "И это все?"
            call pylonController(2, 3) from _call_pylonController_181
            # img показывает сиськи
            citizen15 "Мда, ну и так сойдет..."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen15_dialogue_pilon_loop15


        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_182
            citizen15 "А теперь повернсь и покажи свой зад!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_183
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            call pylonController(4, 5) from _call_pylonController_184
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_46
            call pylonController(4, 5) from _call_pylonController_185
            # img показывает зад
            citizen15 "Зад, 10 долларовой шлюхи, но еще рабочий."
            call pylonController(4, 1) from _call_pylonController_186
            mt "Что за козел. Врезать может ему?"
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen15_dialogue_pilon_loop15
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_187
            citizen15 "Покрутись немного на шесте, который сзади тебя."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_188
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_189
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages2, 4) from _call_showRandomImages_47
#            call pylonController(4, 5)
            citizen15 "Мда, тебе далеко до совершенства..."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_190
            with fade
            mt "Ну и урод..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen15_dialogue_pilon_loop15
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart4startsCompleted == True:
            # ПЕРЕНЕСЕНО В citizen4!!!
            jump citizen15_dialogue_pilon_loop15
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
                call pylonController(2, 1) from _call_pylonController_191
                citizen15 "Красивая шлюшка. Уверен, ты можешь больше, а пока так..."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_192
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_193
            citizen15 "Сходи поищи себе кого-нибудь еще."
            return False
    return

# первый раз
label cit15_naked_boobs_1st:
    img 12409
    citizen15 "Знаешь, обычно при виде меня девочки сами снимают кофточки!"
    citizen15 "Тебе нужно особое приглашение?"
    img 12410
    m "Я не собираюсь ее снимать."
    img 12411
    citizen15 "Хорошие девочки обычно получают за это деньги. Только не говори, что деньги тебе не нужны."
    img 12412
    mt "Самодовольный козел. Но он прав, деньги мне нужны."
    img 12413
    citizen15 "Ну дак что, голые сиськи в обмен на деньги?"
    img 12414
    menu:
        "Почему бы и нет.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12415
            m "Хватит и того, что ты уже видел!"
            return False
    img 12416
    m "Хорошо."
    m "Отвернись!"
    img 12417
    citizen15 "А ты че, стесняешься? Не переживай, можешь начинать..."
    img 12418
    m "Отвернись! Иначе ничего не покажу!"
    img 12419
    citizen15 "А ты серьезная, ладно, отвернусь."
    # отворачивается, моника переодевается...
    img 12420
    w
    img 12421
    m "Можешь повернуться."
    m "Но руками не трогать!"
    img 12422
    citizen15 "Вот так новость! Ну ничего, скоро сама попросишь меня из поторгать!"
    img 12423
    mt "Да никогда!"
    # сиськи
    img 12424
    w
    img 12425
    w
    img 12426
    citizen15 "Ну скажу честно, так себе!"
    img 12427
    mt "Что?!?!"
    # сиськи еще
    img 12428
    w
    img 12429
    w
    img 12430
    citizen15 "Видал я сиськи и получше..."
    # моника продолжает показывать
    img 12431
    w
    img 12432
    w
    img 12433
    citizen15 "Но вообще сойдет, нормально!"
    citizen15 "На 3 балла из 10!"
    img 12434
    m "Почему ты мне такое говоришь?"
    img 12435
    citizen15 "А что не так? На равду не обижаются..."
    img 12436
    m "Ну ладно, хватит!"
    img 12437
    citizen15 "Странная ты... Обычно девочки просят, чтобы я смотрел на них как можно дольше!"
    img 12438
    mt "Обещаю, когда нибудь я тебя ударю."
    $ nakedBoobsFirstly_Cit15 = True
    return True

# вариант 1
label cit15_naked_boobs_variant1:
    img 12439
    citizen15 "Ну что, показывай свои сиськи, погляжу как они там!"
    img 12440
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12441
            m "Хватит и того, что ты уже видел!"
            return False
    img 12442
    m "Хорошо."
    m "Отвернись!"
    img 12443
    citizen15 "Ты снова об этом...Ладно."
    # отворачивается, моника переодевается
    img 12444
    w
    img 12445
    w
    img 12446
    w
    img 12447
    m "Можешь поворачиваться!"
    mg 12448
    citizen15 "Как скажешь, детка."
    # сиськи
    img 12449
    w
    img 12450
    w
    img 12451
    citizen15 "Оу, что за взгляд!"
    img 12452
    mt "Да я убить тебя готова! Если бы не эти чертовы деньги..."
    img 12453
    citizen15 "Я знаю этот взгляд... Ты меня хочешь!"
    img 12454
    m "Не правда."
    # сиськи
    img 12455
    w
    img 12456
    w
    img 12457
    citizen15 "Ха! Так говорят все девочки, но я то знаю правду."
    citizen15 "Если ты меня хочешь, скажи. Не нужно скрывать."
    img 12458
    m "Я тебя не хочу."
    # сиськи
    img 12459
    w
    img 12460
    w
    img 12461
    citizen15 "Я знаю, что ты врешь! Но даже если бы ты это сказала, я бы подумал, стоит ли тебя трахать."
    img 12462
    mt "Что? Да как ты смеешь такое говорить!? Я Моника Бакфет!! Я ты ничтожество, проживающее в помойке!!"
    img 12463
    citizen15 "Ну вот, снова этот взгляд!"
    # сиськи
    img 12464
    w
    img 12465
    w
    img 12466
    m "Ну ладно, хватит!"
    img 12467
    citizen15 "Что, не можешь с собой справиться? Ха-ха... Ну не знаю, может когда нибудь я тебя и трахну, если хорошо попросишь."
    img 12468
    mt "Да ни за что на свете!"
    return True

# вариант 2
label cit15_naked_boobs_variant2:
    img 12469
    citizen15 "Время голых сисек! Давай, расчехляй!"
    img 12470
    mt "Я вырву твой вонючий язык..."
    img 12471
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12472
            m "Хватит и того, что ты уже видел!"
            return False
    img 12473
    m "Хорошо."
    m "Отвернись!"
    img 12474
    citizen15 "Конечно, детка!"
    # отворачивается, моника переодевается ситизен резко поворачивается и ее пугает
    img 12475
    w
    img 12476
    w
    img 12477
    w
    img 12478
    citizen15 "Бу!!!"
    img 12479
    m "Ой! Какого?"
    img 12480
    citizen15 "Ха-ха-ха. Девочки всегда так смешно пугаются."
    citizen15 "И после такого они уже в моей власти!"
    img 12481
    m "Что? О чем вообще ты?"
    img 12482
    citizen15 "Ну как же, разве ты не чувствуешь мое превосходство?"
    img 12483
    m "..."
    img 12484
    citizen15 "Разве не готова мне отдаться прямо здесь?"
    img 12485
    m "Знаешь что... Я не покажу тебе свою грудь..."
    img 12486
    citizen15 "Корчишь недотрогу? Такие девочки мне нравятся..."
    return False
#
