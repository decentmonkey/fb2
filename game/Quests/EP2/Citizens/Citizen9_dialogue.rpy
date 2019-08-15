default citizen9BoobsNakesShowedLastDay = 0
default citizen9BoobsNakesShowedCount = -1

default citizen9BoobsNakesEvent1 = False

label citizen9_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_9_1
    if citizen9_offered_last_day == day and monicaGotJoint != True:
        imgr Dial_Citizen_9_4
        citizen9 "Хэй! Мы уже разговаривали."
        return
    citizen9 "А? Да?"
    "Что?"
    menu:
        "Потрогай мою сиську." if monicaGotJoint == True:
            imgl Dial_Monica_Sandwich_0
            m "Потрогай мою сиську."
            imgr Dial_Citizen_9_3
            citizen9 "Как скажешь, дамочка."
            #подходит к монике сзади и хватает за грудь. так как на ней табличка, ей сложно сопротивляться.
            $ imagesArr = ["7110", "7111", "7112", "7113", "7114"]
            $ images = random.sample(set(imagesArr), 2)
            sound Jump2
            img images[0]
            w
            img images[1]
            w
            img scene_Hostel_Street
            imgl Dial_Monica_Sandwich_0
            imgr Dial_Citizen_9_3
            m "Идиот! Что ты делаешь?"
            imgr Dial_Citizen_9_3
            citizen9 "То, что ты мне сказала! Хе-хе-хе. Отличная грудь кстати!"
            m "Идиот! Я от Джека!"
            imgr Dial_Citizen_9_2
            citizen9 "Ууу, дамочка, с этого и надо было начинать. Что у тебя?"
            #citizen9 отходит
            menu:
                "Дать косяк.":
                    $ remove_inventory("joint", 1, True)
                    imgl Dial_Monica_Sandwich_0
                    $ add_corruption(1, "monica_give_joint_day_" + str(day))
                    m "Вот."
                    imgr Dial_Citizen_9_3
                    citizen9 "Отлично. Узнаю старину Джека. Отличная вещь. Хочешь?"
                    imgl Dial_Monica_Sandwich_1
                    call reduce_flyers() from _call_reduce_flyers_7
                    m "Нет, спасибо. Вот, возьми еще флаер."
                    imgr Dial_Citizen_9_2
                    citizen9 "Флаер? Ладно. Как насчет потрогать сиську еще раз?"
                    imgl Dial_Monica_Sandwich_2
                    m "Нет!"
                    mt "Идиот."
                    $ monicaGotJoint = False
                    $ citizen9_offered_last_day = day
                    $ kebabWorkHarassmentAmount +=1
                    return
                "Ничего":
                    imgl Dial_Monica_Sandwich_0
                    m "Ничего, я, кажется, ошиблась..."
                    return

        "Возьмите, пожалуйста, этот флаер..." if citizen9_offered_last_day != day:
            imgl Dial_Monica_Sandwich_1
            $ citizen9_offered_last_day = day
            #если нет косяка
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen9_refuse_probability) > 0:
                imgr Dial_Citizen_9_2
                citizen9 "А? Что?"
                "Флаер?"
                call reduce_flyers() from _call_reduce_flyers_8
                imgr Dial_Citizen_9_3
                "Хорошо..."
                citizen9 "Ооо, дамочка, а пойдемте к пилону! я потрогаю твою сиську еще разок!"
                menu:
                    "Да ни за что на свете!":
                        $ kebabWorkHarassmentAmount +=1
                        #img Моника злится
                        m "Мне ничего от тебя не нужно!"
                    "Ну точно не сейчас.":
                        m "Не в этот раз."
                        citizen9 "Ооо, ты не отказываешься... Хорошо. Тогда приходи, как будешь не так занята. Кстати, у Найджела есть деньги!"
            else:
                imgr Dial_Citizen_9_4
                citizen9 "Отстань, дамочка! Я пытаюсь кое-что вспомнить..."
                citizen9 "Вы меня отвлекаете!"
                $ kebabWorkMonicaRefusedAmount += 1
        "Уйти.":
            pass
#        "Уйти.":
#            pass
    return

label Citizen_9_use_joint:
    $ obj_name = "Citizen_9"
    call citizens_dialogue_process() from _call_citizens_dialogue_process_1
    $ restore_music()
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen9_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_9_1
    m "Привет! Ты ведь покупал кое что у Джека?"
    citizen9 "Не совсем понимаю к чему ты клонишь..."
    imgr Dial_Citizen_9_3
    citizen9 "Ууу, дамочке нужна наличка?"
    m "Ну, не совсем..."
    citizen9 "Ага, рассказывай... По твоей одежде мне все понятно..."
    imgl Dial_begin35_18
    mt "Ах ты деревеньщина! Ты даже не знаешь кто я такая!"
    citizen9 "Да ладно, дамочка, не злись."
    citizen9 "Знаешь подворотню с пилоном? Там часто появляются желающие заработать. Пойдем туда."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_213
    call pylonController(2, 1) from _call_pylonController_123
    with fadelong
    citizen9 "Ладно, дамочка, что там у тебя?"
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen9_dialogue_pilon_loop9:
    call pylonController(1, 1) from _call_pylonController_124
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_125
            citizen9 "Сиськи!"
            m "Что, это значит?"
            citizen9 "Дамочка, а что это может значить? Давай показывай!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1) from _call_pylonController_126
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(3, 3) from _call_pylonController_127
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_36
            call pylonController(3, 3) from _call_pylonController_128
            # img показывает сиськи
            citizen9 "Ну хоть что-то."
            call pylonController(3, 1) from _call_pylonController_129
            w
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_130
            citizen9 "Жопа!"
            m "Что 'Жопа!'?"
            call pylonController(4, 1) from _call_pylonController_131
            citizen9 "Повернись ко мне задом и показывай!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_132
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(4, 5) from _call_pylonController_133
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_37
            call pylonController(4, 5) from _call_pylonController_134
            # img показывает зад
            citizen9 "Мда, скучно как-то. Приходи сюда вечером, увидишь как можно реально заработать."
            call pylonController(2, 1) from _call_pylonController_135
            w
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_136
            citizen9 "Потанцуй! Для этого здесь пилон и поставили!"
            mt "Наркоман...Надеюсь скоро тебя поймают..."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_137
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_138
            with fade
            m "Хорошо, только не долго."
            call showRandomImages(pylonClothDanceImages8, 4) from _call_showRandomImages_38
#            call pylonController(4, 5)
            citizen9 "А у тебя неплохо выходит."
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_139
            with fade
            w
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen9BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen9BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen9BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen9BoobsNakesShowedCount == -1:
                call cit9_naked_boobs_1st() from _call_cit9_naked_boobs_1st
                if _return != False:
                    $ citizen9BoobsNakesShowedCount += 1
            else:
                if citizen9BoobsNakesShowedCount%2 == 0:
                    call cit9_naked_boobs_variant1() from _call_cit9_naked_boobs_variant1
                if citizen9BoobsNakesShowedCount%2 == 1:
                    call cit9_naked_boobs_variant2() from _call_cit9_naked_boobs_variant2
                $ citizen9BoobsNakesShowedCount += 1
            if _return == 2:
                $ scene_sound = "snd_runaway"
                $ autorun_to_object("citizen9_comment1", scene="hostel_edge_1_a")
                call refresh_scene_fade() from _call_refresh_scene_fade_154
                sound snd_runaway
                return False
            if _return != False:
                $ citizen9BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen9_dialogue_pilon_loop9




            call pylonController(4, 1) from _call_pylonController_140
            citizen9 "Голые сиськи! Я их люблю!"
            m "Что?"
            citizen9 "Да, дорогая, похоже, умом ты не отличаешься."
            "Покажи мне свои сисечки, только голыми!"
            mt "Когда нибудь я сдам тебя в полицию..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_141
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(4, 5) from _call_pylonController_142
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикаснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_39
            call pylonController(4, 5) from _call_pylonController_143
            citizen9 "Ууу... Так намного лучше! Ходи так всегда!"
            call pylonController(4, 1) from _call_pylonController_144
            mt "Размечтался..."
            citizen9 "Ты знаешь, тут не далеко продают кебабы, хотя ты конечно знаешь!"
            "Если ты сходишь мне вот так за кебабом, я дам тебе 100$. Что скажешь?"
            call pylonController(4, 1) from _call_pylonController_145
            m "Что значит Вот так?!"
            citizen9 "А что тут не понятно? Ну в одежде, которая на тебе сейчас."
            m "Да ни за что!"
            mt "Хотя 100$ - не маленькие деньги..."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen9_dialogue_pilon_loop9
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
                call pylonController(2, 1) from _call_pylonController_146
                citizen9 "Ну что-то ты заслужила..."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_147
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_148
            citizen9 "Дамочка, ни цента! Ничего не получишь!"
            return False
    return

# первый раз
label cit9_naked_boobs_1st:
    music Groove2_85
    img 12240
    with fade
    citizen9 "Эй дамочка, ты же хочешь еще доллар?"
    img 12241
    m "..."
    img 12242
    citizen9 "Дамочка, когда тебя спрашивают, нужно отвечать!"
    img 12243
    with diss
    mt "Проклятье, мне нужны деньги..."
    m "Да."
    img 12244
    citizen9 "А вот и славно! Давай посмотрим что ты прячешь под кофточкой!"
    img 12245
    m "Под ней ничего нет..."
    img 12246
    citizen9 "Да, кроме твоих сисечек! Покажи их мне!"
    img 12247
    with diss
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 12248
            m "Хватит и того, что ты уже видел!"
            return False
    img 12249
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12250
    citizen9 "Ох, какая ты скучная..."
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 12251
    with fadelong
    w
    img 12252
    with diss
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    music Loved_Up
    img 12253
    with diss
    w
    img 12255
    citizen9 "Ууу! Просто бомба!"
    citizen9 "Шикарно."
    # сиськи еще
    img 12256
    w
    img 12257
    w
    img 12258
    citizen9 "Слушай, а не найдется лу у тебя косячка?"
    citizen9 "Зрелище стало бы куда интереснее."
    # моника продолжает показывать
    img 12259
    with diss
    w
    img 12260
    w
    img 12261
    citizen9 "Ну ладно, можешь не отвечать..."
    # сиськи еще
    img 12262
    with diss
    w
    img 12263
    with diss
    w
    music Groove2_85
    img 12264
    with fade
    citizen9 "А ты ниче такая! Горячая штучка!"
    citizen9 "Я бы тебя каждый день..."
    img 12265
    with fade
    m "Ну ладно, хватит!"
    img 12266
    citizen9 "Ну что ты за обломщица?"
    img 12267
    with fade
    m "Хорошего понемногу."
    $ nakedBoobsFirstly_Cit9 = True
    return True

# вариант 1
label cit9_naked_boobs_variant1:
    music Groove2_85
    img 12268
    with fade
    citizen9 "Йо! Дамочка, давай заценим твои сисечки еще разок!"
    img 12269
    m "..."
    mt "Грязный наркоман... Но мне нужны деньги."
    img 12270
    citizen9 "Какая же ты некультурная. Нужно отвечать 'Давай!', а ты молчишь..."
    citizen9 "Ну дак что, глянем на твоих подружек еще разок?"
    img 12271
    with diss
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12272
            m "Хватит и того, что ты уже видел!"
            return False
    img 12273
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12274
    citizen9 "..."
    # отворачивается, моника переодевается... сиизен пытается схватить, но моника замечает
    sound snd_fabric1
    img 12275
    with fadelong
    w
    sound Jump1
    img 12276
    with diss
    w
    music Power_Bots_Loop
    sound Jump2
    img 12277
    with hpunch
    w
    img 12278
    m "Какого черта?!"
    img 12279
    with diss
    citizen9 "Эй, детка, все путем!"
    img 12280
    m "Ничего не путем! Я просила тебя отвернуться."
    img 12281
    with diss
    citizen9 "Эй, дамочка, все честно! Да, просила, но я же не ответил."
    img 12282
    with fade
    m "Все, я ухожу..."
    music Groove2_85
    img 12283
    citizen9 "Йо, дамочка, так дела не делаются."
    $ add_money(1.0)
    citizen9 "Ладно, вот твой доллар, все путем да?"
    img 12284
    with diss
    m "..."
    m "Да."
    mt "Проклятье, Моника, до чего ты дошла..."
    img 12285
    citizen9 "Я знал, что это решит наш маленький конфликт!"
    citizen9 "Продолжим?"
    return True

# вариант 2
label cit9_naked_boobs_variant2:
    music Groove2_85
    img 12286
    with fade
    citizen9 "Дамочка, покажи сиськи!"
    img 12287
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12288
            m "Хватит и того, что ты уже видел!"
            return False
    img 12289
    with fade
    m "Хорошо."
    m "Отвернись!"
    img 12290
    citizen9 "..."
    # отворачивается, моника переодевается...
    music Loved_Up
    sound snd_fabric1
    img 12291
    with fadelong
    w
    img 12292
    with diss
    w
    img 12293
    with diss
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    img 12294
    with diss
    w
    img 12295
    with diss
    w
    img 12296
    w
    img 12297
    citizen9 "Йо! Шик!"
    # сиськи
    img 12298
    with diss
    w
    img 12299
    w
    music Groove2_85
    img 12300
    with fade
    citizen9 "Классные дойки, дамочка! Я бы за них подергал!"
    img 12301
    citizen9 "Кстати, у меня идея!"
    citizen9 "Закрой глаза!"
    img 12302
    with diss
    m "Это еще зачем?"
    img 12303
    citizen9 "Да так, у меня для тебя сюрприз!"
    img 12304
    mt "Этот изврашенец что-то задумал?"
    menu:
        "Закрыть глаза.":
            # закывает глаза ситизен подходит сзади и хватает
            img 12305
            with fade
            w
            img 12306
            with diss
            w
            sound Jump1
            img 12307
            with diss
            citizen9 "Сюрприз!"
            music Power_Bots_Loop
            sound Jump2
            img 12308
            with hpunch
            w
            img 12309
            with fade
            m "Что?! Ах ты гад! Да я тебя!"
            img 12310
            with diss
            citizen9 "О! Они просто восхитительные! Ты знаешь, однажды я также схватил дамочку, которая раздавала флаеры..."
            # Сделать какую то привязку к тому событию или по простому: моника ему наваляет и он убегает?
            music stop
            sound snd_punch_face1
            img 12311
            with diss
            w
            sound snd_punch_face2
            img 12312
            with diss
            w
            sound snd_punch_face
            img 12313
            with diss
            w
            img black_screen
            with diss
            sound snd_down1
            pause 3.0
            return 2
            $ citizen9BoobsNakesEvent1 = True
        "Ну уж нет!":
            img 12314
            with fade
            m "Ну уж нет!"
            img 12315
            citizen9 "Дамочка, ты меня разочаровываешь..."
            pass
    # сиськи
    img 12316
    with diss
    w
    img 12317
    with diss
    w
    music Groove2_85
    img 12318
    with fade
    m "Ну все, хватит."
    img 12319
    citizen9 "Ну ты даешь! Я только представил как засовываю между них мой большой..."
    img 12320
    m "Я поняла!"
    img 12321
    citizen9 "Йо! Да неужели? И вероятно еще и представила! Ха-ха-ха!"
    img 12322
    with fade
    mt "Извращенец, когда я верну свое положение, я найду тебя..."
    return True

label citizen9_comment1:
    mt "Мерзавец!"
    return

# первый раз танцы с сиськами
label cit9_naked_boobs_dance_1st:
    img 13631
    citizen9 "Йо, дамочка! Давай посмотрим на твои сисечки!"
    img 13632
    mt "Как же ты меня бесишь, если бы мне не были так нужны деньги, то я..."
    img 13633
    citizen9 "И ты же уже знаешь, зачем нужен пилон..."
    citizen9 "Лезь на него!"
    img 13634
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13635
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13316
    mt "Я уже танцевала, мою прекрасную грудь он видел... Не так страшно, если все это будет вместе."
    mt "Хуже уже не будет..."
    img 13636
    m "Знаешь что, я тебе не верю. Деньги сразу!"
    img 13637
    citizen9 "Вот это ты придумала!"
    citizen9 "А если мне не понравится?"
    img 13638
    mt "Ах ты сволочь..."
    img 13639
    m "Тебе же нравилось все, что ты видел до этого..."
    img 13640
    citizen9 "Ладно, дамочка, держи! А теперь раздевайся!"
    img 13641
    m "Отвернись!"
    # отворачивается
    img 13642
    citizen9 "Так и быть!"
    img 12251
    # поворачиваются, моника стоит с голыми сиськами
    img 13643
    w
    img 13644
    citizen9 "Йо! Ну неужели сама не догадываешься, что пилон уже тебя заждался?!"
    # движение на пилоне
    img 13645
    w
    img 13646
    citizen9 "О да!"
    # движение на пилоне еще
    img 13648
    w
    img 13647
    citizen9 "Порадуй старину Найджела!"
    # движение на пилоне еще
    img 13649
    w
    img 13650
    citizen9 "Горяча!"
    # моника слезает с шеста
    img 13651
    m "Все, достаточно!"
    img 13652
    citizen9 "И правда хватит. Пора засунуть мой член меджу твоих сисек!"
    citizen9 "Я же уже заплатил..."
    img 13653
    m "?!"
    img 13654
    citizen9 "Шутка! Дамочка, в тебе ни капли чувства юмора."
    img 13655
    mt "Зато твое чувство юмора ужасно... Мерзавец!"
    $ nakedBoobsDanceFirstly_Cit9  = True
    return True

#  танцы с сиськами 1 вариант
label cit9_naked_boobs_dance_variant1:
    img 13663
    citizen9 "Йо, я соскучился по твоим танцам на пилоне!"
    citizen9 "Станцуй!"
    img 13634
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13635
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13664
    m "Знаешь что, почему ты так плохо со мной обращаешься?"
    img 13665
    citizen9 "Не, дамочка, с тобой я еще хорошо обращаюсь!"
    citizen9 "Здесь недалеко есть пара шлюх, вот с ними я..."
    img 13666
    m "Мне неинтересно!"
    img 13667
    citizen9 "Ну и ладно! Тогда пулей на пилон! И разденься!"
    img 13668
    m "А ты отвернись!"
    # отворачивается. достает тел и по тихому снимает как моника переодевается
    img 13669
    citizen9 "О да! Это видео непременно пойдет в мою коллекцию..."
    img 13670
    w
    img 13671
    # поворачивается моника стоит с сиськами
    img 13672
    citizen9 "Класс! Я доволен!"
    img 13673
    mt "Интересно чем..."
    img 13674
    citizen9 "Танцуй же уже!"
    # движение на пилоне
    img 13675
    w
    img 13676
    citizen9 "Да, дамочка, это твое призвание!"
    # движение на пилоне
    img 13677
    w
    img 13678
    citizen9 "Да ты просто бомба!"
    # моника слезает с шеста
    img 13651
    m "Все, достаточно!"
    img 13652
    citizen9 "Я бы так не сказал, но в любом случае, дома у меня будет еще неколько часов важных дел..."
    citizen9 "Я буду смотреть порно!"
    img 13653
    m "Я и без тебя это поняла..."
    img 13654
    citizen9 "А ты догадливая ... Иногда..."
    citizen9 "Но все равно, надеюсь, к следующему разу ты разучишь больше движений."
    return True

#  танцы с сиськами 2 вариант
label cit9_naked_boobs_dance_variant1:
    img 13663
    citizen9 "Расчехляй близняжек и на шест!"
    img 13634
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            img 13635
            m "Хватит с тебя того, что ты уже видел!"
            return False
    img 13637
    citizen9 "Я даже сам отвернусь..."
    img 13638
    mt "Что это с ним?"
    w
    img 1225
    # поворачивается, моника с сиськами
    img 13643
    citizen9 "Залезай пожалуйста на шест."
    img 13673
    mt "А где же Йо? Что с ним сегодня?"
    # движение на пилоне
    img 13680
    w
    img 13679
    citizen9 "Очень красиво!"
    # движение на пилоне
    img 13681
    w
    img 13682
    citizen9 "Очень, очень красиво!"
    # моника слезает с шеста
    img 13683
    m "Что с тобой сегодня?"
    img 13684
    citizen9 "Со мной все в порядке, просто я прочитал в гороскопе, что в течение дня мне лучше быть вежливым и, возможно, я добьюсь чего-то большего."
    img 13685
    mt "Возможно, но явно не со мной."
    img 13686
    citizen9 "Вот, возьми пожалуйста твои деньги."
    # моника берет дкньги
    img 13687
    citizen9 "И все?"
    img 13688
    m "А чего ты хотел?"
    img 13689
    citizen9 "Ну я же был вежлив..."
    img 13690
    m "Ну тебе же ясно в гороскопе сказали 'возможно добьетесь'. Со мной ничего не удалось."
    img 13691
    citizen9 "Йо, дамочка! Все гороскопы отстой, я знал это!"
    return True
