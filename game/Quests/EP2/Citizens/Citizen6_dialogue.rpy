default citizen6BoobsNakesShowedLastDay = 0
default citizen6BoobsNakesShowedCount = -1
default questOffendMonicaFlyersCitizen6ThanksGiven = False
default questWhorePlaceSearchingStage = 0

label citizen6_dialogue:
    if questOffendMonicaFlyersCitizen12Completed == True and questOffendMonicaFlyersCitizen6ThanksGiven == False:
        mt "Надо бы поблагодарить его, но я не хочу делать это одетой в рекламу кебеба..."
        return
    imgl Dial_Monica_Sandwich_0
#    menu:
#    "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_6_1
    if citizen6_offered_last_day == day:
        imgr Dial_Citizen_6_4
        citizen6 "Нельзя! Я тороплюсь!"
        return
    citizen6 "Да, Леди? Что Вы хотели?"
    menu:
        # этот пункт появляется единождыпосле выполнения события нападения(проверка на переменную диалога 12)

        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen6_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen6_refuse_probability) > 0:
                imgr Dial_Citizen_6_2
                call reduce_flyers() from _call_reduce_flyers_1
                citizen6 "Взять флаер? Хорошо..."
                imgr Dial_Citizen_6_3
                citizen6 "Какой красивый флаер! Прямо такой-же как Вы!"
                imgl Dial_Monica_Sandwich_2
                m "Спасибо конечно, но меня не нужно сравнивать с флаером."
                citizen6 "Как насчет того чтобы сходить со мной в одно интересное место?"
                menu:
                    "Я никуда с тобой не пойду":
                        $ kebabWorkHarassmentAmount +=1
                        #img Моника злится
                        m "Я ничего не предлагаю! Просто возьмите флаер!"
                    "В какое это место?" if fallingPathStarted == True:
                        m "Куда это?"
                        citizen6 "Да тут не далеко, тем более мы уже там были с тобой. Ха-ха!"
                        m "Хватит с меня этого места..."
                        citizen6 "Ну если тебе не нужны деньги..."
                        m "Ты это о чем?"
                        citizen6 "Как это о чем? Как будто ты ничего не понимаешь. За это обычно платят."
                        m "У меня есть деньги!"
                        mt "Точнее были..."
            else:
                imgr Dial_Citizen_6_4
                citizen6 "Я тороплюсь! Давайте в другой раз!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

label citizen6_dialogue_after_offend_hook:
    if kebabWorkInProgress == True:
        return
    if act=="l":
        mt "Этот парень не выглядит злым. Надеюсь, так оно и есть."
        return False
#    if day_time == "evening":
#        mt "Надо бы поблагодарить его, но я боюсь подходить к людям вечером..."
#        mt "Лучше сделаю это завтра днем..."
#        return False

    if questWhorePlaceSearchingStage == 0:
        call citizen6_dialogue_after_offend() from _call_citizen6_dialogue_after_offend
        return False
    if questWhorePlaceSearchingStage == 1:
        call citizen6_dialogue_after_offend2() from _call_citizen6_dialogue_after_offend2
        return False
    if questWhorePlaceSearchingStage == 2:
        call citizen6_dialogue_after_offend3() from _call_citizen6_dialogue_after_offend3
        return False
    return

# диалог доступен только когда моника не работает на раздаче флаеров
label citizen6_dialogue_after_offend:
    music Groove2_85
    imgr Dial_Citizen_6_3
    imgl Dial_Monica_Whore_1
    m "Спасибо за помощь."
    citizen6 "Не за что, милочка. Ну что, приступим?"
    m "Приступим... К чему?"
    citizen6 "Ну как же, к моей награде."
    m "Награде?"
    citizen6 "Ага. Ты же догадываешься, какую?"
    m "Понимаешь, я сейчас не в самом лучшем финансовом положении..."
    citizen6 "Не, не... Не нужны мне твои 10 долларов!"
    imgl Dial_Monica_Whore_2
    m "Да как ты?!..."
    if money < 10:
        mt "Черт, у меня нет даже 10 долларов..."
    m "Что же ты хочешь?"
    citizen6 "Ты красивая, хочу на тебя посмотреть."
    m "Что?"
    citizen6 "Да! Не прикидывайся, что не понимаешь о чем я."
    imgl Dial_Monica_Whore_1
    m "Я не стану раздеваться!"
    citizen6 "Ха-ха! А ты не простая штучка..."
    "Не бойся, я не буду раздевать тебя! Я просто хочу на тебя посмотреть!"
    "Притом я дам тебе доллар сверху! Несмотря на то что ты мне и так должна!"
    "Давай, показывай себя!"
    imgl Dial_Monica_Whore_1
    mt "Целый доллар?"
    "Просто за то чтобы показать себя не раздеваясь..."
    "С одной стороны, я могу за 5 минут заработать на этот чертов кебаб..."
    "А не ходить в этой рекламе по району целый день..."
    "С другой стороны... Моника, ты готова к этому?"
    "Но, ведь меня все-равно никто не узнает в этой жуткой одежде..."
    "И у этого ничтожества нет ни одного шанса притронуться к моей красоте..."
    "Так что же мне делать?"
    menu:
        "Согласиться..." if corruption >= monicaWhoringStartCorruptionRequired:
            pass
        "Согласиться... (low corruption, required: [monicaWhoringStartCorruptionRequired]) (disabled)" if corruption < monicaWhoringStartCorruptionRequired:
            pass
        "Отказаться.":
            imgl Dial_Monica_Whore_2
            m "Я не собираюсь ничего показывать тебе!"
            "Ты не за ту принял меня!"
            imgr Dial_Citizen_6_4
            citizen6 "Эй! Я спас тебя!"
            "Не забывай что ты мне должна!"
            m "Не забуду!"
            return
    imgl Dial_Monica_Whore_2
    m "Но я не буду делать это здесь, на виду у всей улицы!"
    citizen6 "Ну так давай сделаем это где-то еще!"
    imgl Dial_Monica_Whore_1
    m "Где?"
    citizen6 "Я не знаю где! Ты же шлюха, ты знаешь такие места!"
    m "Я не шлюха! Я уже говорила тебе это!!!"
    mt "Мерзавец! Как он смеет говорить такое?!"
    "Ну и что что я так одета, но неужели не видно что я Леди?!"
    m "..."
    m "Хорошо, поищу такое место..."
    m "Но ты помнишь что обещал мне доллар?"
    citizen6 "Милочка, не затягивай с этим!"
    $ questWhorePlaceSearchingStage = 1
    $ autorun_to_object("needToFindWhorePlace", scene="hostel_street2")
    $ autorun_to_object("citizen6_dialogue_after_offend_place_found", scene="hostel_edge_1_a")
    $ add_objective("find_place", _("Найти тихое место для обслуживания 'Клиентов'"), c_orange, 50)
    call refresh_scene_fade() from _call_refresh_scene_fade_41
    return

label citizen6_dialogue_after_offend_place_found:
    mt "Какжется, это место вполне подходит для того чтобы здесь показать то что меня попросили..."
    mt "Оно жуткое, но здесь никого нет..."
    mt "И этот пилон... Что он делает здесь?"
    $ remove_objective("find_place")
    $ questWhorePlaceSearchingStage = 2
    return

label citizen6_dialogue_after_offend2: #Моника еще не нашла место
    music Groove2_85
    imgr Dial_Citizen_6_3
    imgl Dial_Monica_Whore_1
    citizen6 "Ну что, ты нашла место?!"
    "Пойдем!"
    m "Еще нет..."
    citizen6 "Давай быстрее! Я теряю терпение!"
    $ autorun_to_object("needToFindWhorePlace", scene="hostel_street2")
    return

label citizen6_dialogue_after_offend3: #Моника нашла место

    #Ладно, пошли со мной, тут не далеко."
#    m "Куда?"
#    citizen6 "Не бойся, тут не далеко..."
#    m "Я не собираюсь никуда с тобой идти!"

    imgr Dial_Citizen_6_3
    imgl Dial_Monica_Whore_1
    citizen6 "Ну что, ты нашла место?!"
    m "Я нашла одно место, но я не уверена и..."
    imgr Dial_Citizen_6_4
    citizen6 "Послушай, хочу тебе напомнить: я тебя спас, ты мне обещала 'Все, что угодно'. А теперь шевели своим красивым задом, пока я добрый."
#    mt "А ведь он прав...Возможно, он не такой уж и плохой."
    m "Ну хорошо, только я сказала, что не буду раздеваться."
    imgr Dial_Citizen_6_1
    citizen6 "Я это уже слышал... Пошли уже."

    sound highheels_short_walk
    # переход на локацию с пилоном
    call change_scene("hostel_edge_1_a") from _call_change_scene_167
    $ pylonPreset = rand(1,2)
    $ citizenId = 6
    call pylonController(2, 1) from _call_pylonController
    with fadelong
    m "..."
#    mt "Я уже была в этой грязной подворотне..."
    citizen6 "А теперь покажи сиськи!"
    if corruption < monicaWhoringClothBoobsCorruptionRequired:
        mt "Я не могу себе этого позволить!"
        "Я еще не настолько опустилась!"
        "И, надеюсь, этого не произойдет НИКОГДА!"
        call pylonController(1, 2) from _call_pylonController_1
        m "Да как ты можешь такое просить!?"
        call pylonController(5, 1) from _call_pylonController_2
        citizen6 "Дорогуша, ты же обещала Все, что угодно. Дак вот, я хочу твои сиськи!"
        m "Я не могу!"
        help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
        return
    call pylonController(1, 2) from _call_pylonController_3
    m "Что? А что если нас кто-то увидит?"
    m "И ты не забыл про доллар?"
    call pylonController(3, 1) from _call_pylonController_4
    citizen6 "Расслабься, тут никого нет. Давай уже, показывай. Чем быстрее ты это сделаешь, тем быстрее будешь мне не должна!"
    mt "Что за извращенец..."
    m "Ладно..."
    # моника кажет сиськи
    call pylonController(3, 3) from _call_pylonController_5
    with fade
    w
    call showRandomImages(boobsImages, 4) from _call_showRandomImages
    call pylonController(3, 3) from _call_pylonController_6
    citizen6 "О да, какие сочные!"
    call pylonController(3, 3) from _call_pylonController_7
    citizen6 "Да, у тебя шикарные сиськи! А теперь повернись и нагнись немного."
    $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))

    if corruption < monicaWhoringClothAssCorruptionRequired:
        call pylonController(3, 1) from _call_pylonController_8
        mt "Я не могу себе этого позволить!"
        "Я еще не настолько опустилась!"
        "И, надеюсь, этого не произойдет НИКОГДА!"
        m "Ну уж нет, это слишком!"
        call pylonController(3, 1) from _call_pylonController_9
        citizen6 "Ну ладно, я сегодня добрый. Можешь идти. Тем более твои сиськи это нечто!"
        citizen6 "Детка, ты можешь неплохо зарабатывать этим!"
        $ add_money(1.0)
        help "Для активации этого события требовалось [monicaWhoringClothAssCorruptionRequired] corruption, но не переживайте, Моника еще покажет себя."
        $ questOffendMonicaFlyersCitizen6ThanksGiven = True
        $ fallingPathStarted = True
        call ep22_quests_falling_path5() from _call_ep22_quests_falling_path5
        return
    # моника кажет жопу
    call pylonController(4, 5) from _call_pylonController_10
    with fade
    w
    call showRandomImages(assImages, 4) from _call_showRandomImages_1
    call pylonController(4, 5) from _call_pylonController_11
    $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
    citizen6 "Да, детка, ты великолепна! Ты можешь неплохо зарабатывать этим!"
    "Ох, у меня кажется встал... Нужно срочно отойти..."
    call pylonController(2, 1) from _call_pylonController_12
    citizen6 "Можешь идти, считай, ты мне ничего не должна."
    $ add_money(1.0)
    # переменная отвечающая за А что бы ты хотел в диалогах с кебабом = 1
    $ fallingPathStarted = True
    $ questOffendMonicaFlyersCitizen6ThanksGiven = True
    call ep22_quests_falling_path5() from _call_ep22_quests_falling_path5_1
    return

label citizen6_dialogue_after_offend4: #Моника думает после встречи с citizen6
    $ hudDaySkipToEveningEnabled = True

    mt "Боже! Какой ужас!"
    "Как я могла опуститься до такого..."
    "..."
    "С другой стороны, я в таком положении, когда любая девушка согласилась бы на такое гораздо раньше чем Я!"
    "Я еще очень долго держусь и сохраняю гордость!"
    "И меня ничто не сломит, клянусь!"
    "Я верну назад все что потеряла и отомщу им всем!"
    "И даже этому ничтожеству, которое уговорило меня показать мое тело... пусть и в одежде..."
    "..."
    "С другой стороны, меня никто не узнает..."
    "Просто дать на себя посмотреть..."
    "Это ведь лучше, чем ходить в рекламе кебаба по району..."
    "Но нет! Моника Бакфетт выше этого!"
    "Пусть даже меня никто и не узнает, это ничего не меняет!"
    "У меня полно других возможностей добыть еду!"
    "Или нет?.."
    return

label citizen6_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_6_1
    m "Привет! Помнишь, ты говорил, что я могу заработать..."
    imgr Dial_Citizen_6_3
    citizen6 "Конечно помню, у тебя все для этого есть!"
    m "..."
    citizen6 "В общем, я понимаю о чем ты. Давай не будем тратить время и пойдем уже в наше место"
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_168
    call pylonController(2, 1) from _call_pylonController_13
    with fadelong
    citizen6 "Начнем."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen6_dialogue_pilon_loop6:
    call pylonController(1, 1) from _call_pylonController_14
    menu:
        "Покажи сиськи.":
            call pylonController(2, 1) from _call_pylonController_15
            citizen6 "Покажи сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen6_dialogue_pilon_loop6

            call pylonController(3, 3) from _call_pylonController_16
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_2
            call pylonController(3, 3) from _call_pylonController_17
            # img показывает сиськи
            citizen6 "Корошее начало!"
            call pylonController(3, 3) from _call_pylonController_18
            citizen6 "Ух, мне достаточно только взгляда и у меня встает..."
            call pylonController(3, 3) from _call_pylonController_19
            citizen6 "Ооо... Как хорошо..."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen6_dialogue_pilon_loop6
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_20
            citizen6 "Покажи жопу!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen6_dialogue_pilon_loop6
            call pylonController(4, 5) from _call_pylonController_21
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4) from _call_showRandomImages_3
            call pylonController(4, 5) from _call_pylonController_22
            citizen6 "Вау, вот это да!"
            call pylonController(4, 5) from _call_pylonController_23
            citizen3 "Никогда не видел такой шикарной жопы!"
            $ showedButt = True
            # img показывает зад
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen6_dialogue_pilon_loop6
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_24
            citizen6 "Танцуй! Шест рядом."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_25
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen6_dialogue_pilon_loop6
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_26
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages5, 4) from _call_showRandomImages_4
#            call pylonController(4, 5)
            citizen6 "Блестяще, давно такого не видел!"
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_27
            with fade
            w
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen6_dialogue_pilon_loop6
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen6BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen6BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen6BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen6BoobsNakesShowedCount == -1:
                call cit6_naked_boobs_1st() from _call_cit6_naked_boobs_1st
                if _return != False:
                    $ citizen6BoobsNakesShowedCount += 1
            else:
                if citizen6BoobsNakesShowedCount%2 == 0:
                    call cit6_naked_boobs_variant1() from _call_cit6_naked_boobs_variant1
                if citizen6BoobsNakesShowedCount%2 == 1:
                    call cit6_naked_boobs_variant2() from _call_cit6_naked_boobs_variant2
                $ citizen6BoobsNakesShowedCount += 1
            if _return != False:
                $ citizen6BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen6_dialogue_pilon_loop6



            call pylonController(4, 1) from _call_pylonController_28
            citizen6 "Покажи мне грудь, только теперь без одежды."
            mt "Он и вправду говорит как бизнесмен, заключающий сделку..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_29
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen6_dialogue_pilon_loop6
            call pylonController(4, 5) from _call_pylonController_30
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_5
            call pylonController(4, 5) from _call_pylonController_31
            citizen6 "Очень хорошо. Отличный старт."
            call pylonController(4, 1) from _call_pylonController_32
            mt "Что значит старт?"
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen6_dialogue_pilon_loop6
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
                call pylonController(2, 1) from _call_pylonController_33
                citizen6 "Какая ты сочная! Вот держи, а я пойду займусь очень важным делом."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_34
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_35
            citizen6 "Похоже, я зря потратил свое время, пойду найду другую шлюху."
            return False
    return

# первый раз
label cit6_naked_boobs_1st:
    music Groove2_85
    img 11961
    with fade
    citizen6 "Я никак не могу забыть нашу первую встречу..."
    img 11962
    mt "А вот я бы ее с радостью забыла..."
    img 11963
    citizen6 "Как насчет того, чтобы показать мне свои сиськи? Но уже без этой ненужной курточки?"
    img 11964
    m "И почему я должны согласиться?"
    img 11965
    citizen6 "Если ты не помнишь, я тебя спас! А вообще район тут опасный, если ты понимаешь о чем я..."
    img 11966
    mt "К чему это он?"
    img 11967
    citizen6 "Ну дак что, как насчет сисек?"
    img 11968
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит и того, что ты уже видел!":
            img 11969
            m "Хватит и того, что ты уже видел!"
            return False
    img 11970
    with fade
    mt "Думаю, лучше это сделать, а то мало ли что..."
    img 11971
    m "Отвернись!"
    img 11972
    citizen6 "Вот это другой разговор."
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 11973
    with fade
    w
    music Loved_Up
    img 11974
    with diss
    m "Можешь повернуться."
    m "Но руками не трогать!"
    # сиськи
    img 11975
    with diss
    w
    img 11976
    w
    img 11977
    w
    img 11978
    citizen6 "Ха! Вот это класс!"
    citizen6 "Я был бы готов каждый день давать тебе по 100 баксов, если бы ты так ходила!"
    img 11979
    with diss
    mt "Не в этой жизни..."
    # сиськи еще
    img 11980
    w
    img 11981
    w
    img 11982
    citizen6 "Шикарные сиськи!"
    # моника продолжает показывать
    img 11983
    w
    img 11984
    w
    img 11985
    w
    music Groove2_85
#    img 11986
    img 11988
    with fade
    m "Ну ладно, хватит с тебя."
    img 11987
    citizen6 "Слабовато, но ничего, хватит для первого раза."
    img 11988
    mt "Может даже и последнего..."
    $ nakedBoobsFirstly_Cit6 = True
    return True

# вариант 1
label cit6_naked_boobs_variant1:
    music Groove2_85
    img 11989
    with fade
    citizen6 "Я уже успел соскучиться по твоим сиськам!"
    img 11990
    mt "Да неужели..."
    img 11991
    citizen6 "Покажи мне их еще раз!"
    img 11992
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 11993
            m "Хватит и того, что ты уже видел!"
            return False

    # отворачивается, моника переодевается...
    img 11994
    with fade
    m "Хорошо"
    sound snd_fabric1
    music Loved_Up
    img 11995
    with fade
    m "Только руками не трогать!"
    img 11996
    citizen6 "Ладно, ладно! Можно и не говорить об этом каждый раз!"
    # сиськи
    img 11997
    w
    img 11998
    w
    img 11999
    w
    img 12000
    citizen6 "О да! Как же ты меня заводишь!"
    # сиськи еще
    img 12001
    w
    img 12002
    w
    img 12003
    citizen6 "Черт, это просто супер!"
    # сиськи еще
    img 12004
    w
    img 12005
    w
    img 12006
    citizen6 "Ну все, теперь мне надо к шлюхам. Хотя..."
    # сиськи еще
    img 12007
    w
    img 12008
    w
    music Groove2_85
    img 12009
    with fade
    citizen6 "Детка, ты готова отсосать за 20 баксов?"
    img 12010
    menu:
        "Только за 20 тысяч баксов.":
            m "Только за 20 тысяч баксов."
            img 12011
            citizen6 "А ты шутница! Да за такие деньги я трахну кого захочу!"
            img 12012
            mt "Господи, что я говорю? Неужели я готова сделать такое..."
            pass
        "Я тебе сейчас нос сломаю!":
            music Power_Bots_Loop
            img 12013
            with fade
            m "Я тебе сейчас нос сломаю!"
            img 12014
            citizen6 "Да ладно тебе, хочешь больше?"
            citizen6 "Хорошо, 23 бакса! Хорошая цена!"
            img 12015
            with diss
            m "Еще слово и тебе конец!"
            img 12016
            citizen6 "Ладно, не кипятись! Так бы и сказала, что не хочешь..."
            pass
    img 12017
    with fade
    m "Хватит с тебя."
    img 12018
    citizen6 "Да и пожалуйста, я и получше сиськи видел!"
    return True

# вариант 2
label cit6_naked_boobs_variant2:
    music Groove2_85
    img 12019
    with fade
    citizen6 "Давай глянем на твои сиськи!"
    img 12020
    menu:
        "Хорошо.":
            pass
        "Хватит и того, что ты уже видел!":
            img 12021
            m "Хватит и того, что ты уже видел!"
            return False
    img 12022
    with fade
    m "Отвернись!"
    # отворачивается, моника переодевается...
    sound snd_fabric1
    img 12023
    w
    img 12024
    with diss
    w
    music Loved_Up
    img 12025
    with diss
    m "Можешь повернуться."
    m "Только руками не трогать!"
    img 12026
    citizen6 "Да сколько уже можно об этом?"
    # сиськи
    img 12027
    w
    img 12028
    w
    img 12029
    citizen6 "Класс! Сногсшибательные сиськи!"
    # сиськи еще
    img 12030
    w
    img 12031
    w
    img 12032
    citizen6 "Да, еще немного!"
    # сиськи еще
    img 12033
    w
    img 12034
    w
    img 12035
    citizen6 "Шикарно!"
    # сиськи еще
    img 12036
    w
    img 12037
    w
    music Groove2_85
    img 12038
    citizen6 "Знаешь, я хочу, чтобы ты прошлась немного."
    img 12039
    m "Не поняла..."
    img 12040
    citizen6 "А что не понятно то? Пилон стоит у стены, пройдись до другой стены и обратно."
    img 12041
    with diss
    m "Зачем это вообще?"
    img 12042
    citizen6 "Что за вопросы? Я плачу, ты делаешь."
    img 12043
    mt "Какого черта? Возможно стоит согласиться, ведь ничего в этом такого нет..."
    img 12044
    menu:
        "Хорошо.":
            music Loved_Up
            img 12045
            with fade
            m "Хорошо."
            # моника идет от стенки до стенки с голой грудью
            sound man_steps
            img 12046
            with diss
            w
            sound man_steps
            img 12047
            with diss
            w
            sound man_steps
            img 12048
            with diss
            w
            sound man_steps
            img 12049
            with diss
            w
            img 12050
            with fade
            w
        "Не хочу.":
            img 12051
            with fade
            m "Не хочу! Я не собираюсь этого делать!"
            img 12052
            citizen6 "Ну и черт с тобой!"
            pass
    img 12053
    with fade
    m "Ладно, хватит с тебя того, что ты уже видел."
    img 12054
    citizen6 "Да и пожалуйста, я и получше сиськи видел!"
    return True

# первый раз танцы с сиськами
label cit6_naked_boobs_dance_1st:
    citizen6 "Эй, как насчеет танцев?"
    m "Можно, но только если ты заплатишь."
    citizen6 "Да, я заплачу, а ты снимешь кофточку."
    m "Что?!"
    menu:
        "Почему бы и нет.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            m "Хватит с тебя того, что ты уже видел!"
            return False
    mt "Я уже танцевала, мою прекрасную грудь он видел... Не так страшно, если все это будет вместе."
    m "Сколько ты заплатишь?"
    citizen6 "Танцы-доллар, сиськи-по пол доллара каждая. Итого 2 доллара."
    menu:
        "Хорошо.":
            pass
        "Ну уж нет!":
            m "Ну уж нет!"
            citizen6 "Ладно, тут можно и по дешевле найти!"
            return False
    mt "Сиськи по пол доллара каждая?! Да моя грудь стоит миллион!"
    m "Хорошо. Только отвернись!"
    # отворачиваются
    citizen6 "Хорошо, отвернусь!"
    # поворачиваются, моника стоит с голыми сиськами
    citizen6 "Давай, не тормози, начинай!"
    # движение на пилоне
    citizen6 "Хе-хе! Прекрасно!"
    # движение на пилоне еще
    citizen6 "Давай еще! И если мне понравится, то я, возможно, дам тебе еще доллар!"
    # движение на пилоне еще
    citizen6 "Ну не знаю, такое чувство, что ты халтуришь..."
    # моника слезает с шеста
    m "С тебя хватит!"
    citizen6 "Вот смотрю я на тебя и думаю, что нет в теби искры, но свои 2 бакса ты заработала."
    citizen6 "Тренируйся! И получишь 2.5 доллара, а может и 3!"
    m "Когда я верну себе все то, чем я владела, я затолкаю эти 2 доллара тебе в рот!"
    $ nakedBoobsDanceFirstly_Cit6  = True
    return True

# танцы с сиськами var 1
label cit6_naked_boobs_dance_variant1:
    citizen6 "Детка, потанцуй еще, мне нравится, как ты крутишься на пилоне."
    citizen6 "Особенно без кофточки."
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            m "Хватит с тебя того, что ты уже видел!"
            citizen6 "Ладно, если ты не хочешь денег..."
            return False
    m "Хорошо. Только отвернись!"
    # отворачиваются
    citizen6 "Хорошо."
    # поворачиваются, моника стоит с голыми сиськами
    citizen6 "Давай, не тормози, начинай!"
    # движение на пилоне
    citizen6 "Хе-хе! Прекрасно!"
    # движение на пилоне еще
    citizen6 "Давай еще! И если мне понравится, то я, возможно, дам тебе еще доллар!"
    # движение на пилоне еще
    citizen6 "Ну не знаю, такое чувство, что ты халтуришь..."
    # моника слезает с шеста
    m "С тебя хватит!"
    citizen6 "Вот смотрю я на тебя и думаю, что нет в теби искры, но свои 2 бакса ты заработала."
    citizen6 "Тренируйся! И получишь 2.5 доллара, а может и 3!"
    m "Когда я верну себе все то, чем я владела, я затолкаю эти 2 доллара тебе в рот!"
    return True

# вариант 2
label cit6_naked_boobs_dance_variant2:
    citizen6 "Детка, потанцуй еще, я устал от стрип клуба, там плохое освещение..."
    citizen6 "И сними кофточку. Без нее тебе лучше."
    menu:
        "Хорошо.":
            pass
        "Хватит с тебя того, что ты уже видел!":
            m "Хватит с тебя того, что ты уже видел!"
            citizen6 "Ладно, если ты не хочешь денег..."
            return False
    m "Хорошо. Только отвернись!"
    # отворачиваются
    citizen6 "Ладно."
    # поворачиваются, моника стоит с голыми сиськами
    citizen6 "Ну давай уже! Мне долго ждатть?"
    # движение на пилоне
    citizen6 "Вот, другое дело!"
    # движение на пилоне еще
    citizen6 "Давай еще! И если мне понравится, то я, возможно, дам тебе еще доллар!"
    # движение на пилоне еще
    citizen6 "А сегодня ты получше! Тренировалась?"
    # моника слезает с шеста
    m "С тебя хватит!"
    citizen6 "Я тут придумал, как ты можешь заработать еще доллар."
    citizen6 "Я тут был в стрип клубе и там некоторые из твоих коллег наклоняются перед лицами посетителей, а между сисек у них бутылка..."
    citizen6 "Дак вот, они наклоняются, а из бутылки льется пиво прямо в рот!"
    citizen6 "Я тут прикупил пивка...Ну дак что? Сделаешь это? Я дам тебе доллар!"
    citizen6 "Ради такого я даже присяду, ведь тут нет сцены..."
    citizen6 "Ну дак что, хочешь доллар?"
    menu:
        "Я хочу больше.":
            m "Я хочу больше."
            citizen6 "Серьезно? Я и так плачу тебе доллар! На это можно купить целый кебаб!"
            citizen6 "Сколько же ты хочешь?"
            mt "Черт, мне нужны деньги и я уже решила, что могу пойти на такое... Как бы сделать так, чтобы он согласился заплатить как можно больше."
            m "Я хочу 50 долларов! Один человек мне заплатил столько только за то, что я показала ему грудь."
            citizen6 "Ха-ха-ха! Я даже знаю его! Его тут все знают! Он помешан на новых сиськах! Думаю в другой раз он столько не заплатит."
            citizen6 "Хорошо. В стрип клубе я за это плачу 10 долларов, но девочке из этого идет не все. Я дам тебе на 1 доллар, а 3!"
            m "Ладно."
            mt "Козел..."
            # сцена.
            citizen6 "Вот кстати мое любимое пивко."
            # дает бутылку, продолжение сцены
            citizen6 "О да, детка!"
            citizen6 "Дааа!"
            citizen6 "Даже лучше стрип клуба! Нет этих лампочек..."
            # звук питья ...
            citizen6 "Ух! Зашибись! Вот твои деньги! Я доволен!"
            pass
        "Это слишком!":
            m "Думаю, тебе стоит вернуться в стрип клуб. Я не готова на такое."
            citizen6 "Ладно, приду, когда ты будешь работать."
            mt "Козел, я не сприптизерша."
            pass
    citizen6 "Да, кстати, вот 2 доллара за танец."
    return True
