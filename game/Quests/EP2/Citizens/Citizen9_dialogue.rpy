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
                        citizen7 "Ооо, ты не отказываешься... Хорошо. Тогда приходи, как будешь не так занята. Кстати, у Найджела есть деньги!"
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
    call change_scene("hostel_edge_1_a", "Fade_long")
    call pylonController(2, 1)
    with fadelong
    citizen9 "Ладно, дамочка, что там у тебя?"
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen9_dialogue_pilon_loop9:
    call pylonController(1, 1)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1)
            citizen9 "Сиськи!"
            m "Что, это значит?"
            citizen9 "Дамочка, а что это может значить? Давай показывай!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(3, 3)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(3, 3)
            # img показывает сиськи
            citizen9 "Ну хоть что-то."
            call pylonController(3, 1)
            w
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Покажи попу.":
            call pylonController(4, 1)
            citizen9 "Жопа!"
            m "Что 'Жопа!'?"
            call pylonController(4, 1)
            citizen9 "Повернись ко мне задом и показывай!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(4, 5)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4)
            call pylonController(4, 5)
            # img показывает зад
            citizen9 "Мда, скучно как-то. Приходи сюда вечером, увидишь как можно реально заработать."
            call pylonController(2, 1)
            w
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1)
            citizen9 "Потанцуй! Для этого здесь пилон и поставили!"
            mt "Наркоман...Надеюсь скоро тебя поймают..."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6)
            with fade
            m "Хорошо, только не долго."
            call showRandomImages(pylonClothDanceImages8, 4)
#            call pylonController(4, 5)
            citizen9 "А у тебя неплохо выходит."
            $ restore_music()
            call pylonController(4, 1)
            with fade
            w
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen9_dialogue_pilon_loop9
        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart3startsCompleted == True:
            call pylonController(4, 1)
            citizen9 "Голые сиськи! Я их люблю!"
            m "Что?"
            citizen9 "Да, дорогая, похоже, умом ты не отличаешься."
            "Покажи мне свои сисечки, только голыми!"
            mt "Когда нибудь я сдам тебя в полицию..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen9_dialogue_pilon_loop9
            call pylonController(4, 5)
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикаснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4)
            call pylonController(4, 5)
            citizen9 "Ууу... Так намного лучше! Ходи так всегда!"
            call pylonController(4, 1)
            mt "Размечтался..."
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
                call pylonController(2, 1)
                citizen9 "Ну что-то ты заслужила..."
                $ add_money(earnedMoney)
                call pylonController(1, 1)
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1)
            citizen9 "Дамочка, ни цента! Ничего не получишь!"
            return False
    return
