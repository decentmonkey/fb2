label citizen1_dialogue:
    imgl Dial_Monica_Sandwich_0
#    "Можно к Вам обратиться?"
    m "Эй, ребята... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_1_1
    if citizen1_offered_last_day == day:
        imgr Dial_Citizen_1_4
        citizen1 "Эй! Тетя!"
        "Ты уже подходила к нам!"
        "Хватит с нас твоих флаеров!"
        return
    citizen1 "Да, тетя? Что тебе надо?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            $ citizen1_offered_last_day = day
            imgl Dial_Monica_Sandwich_1
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen1_refuse_probability) > 0:
                imgr Dial_Citizen_1_2
                citizen1 "Тетя, не видишь, мы заняты, нам сейчас не до тебя."
                imgr Dial_Citizen_2_3
                citizen2 "Погоди, Том, разве ты не видишь? Она работает."
                imgr Dial_Citizen_1_3
                citizen1 "С такой внешностью тебе бы не флаеры раздавать!"
                imgl Dial_Monica_Sandwich_0
                mt "(Вот козел...)"
                imgr Dial_Citizen_2_2
                imgl Dial_Monica_Sandwich_1
                call reduce_flyers() from _call_reduce_flyers_9
                citizen2 "А я возьму, давай свой флаер."
                # на 3 раз будут они давать какие то задания ей
                imgr Dial_Citizen_1_3
                citizen1 "Тетя! А больше ты ничего мне не можешь дать?"
                menu:
                    "Больше ничего!":
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "Больше ничего!"
                        $ kebabWorkHarassmentAmount +=1
                    "А что бы вы хотели?":
                        m "А что бы вы хотели?"
                        imgr Dial_Citizen_1_3
                        citizen1 "А то ты не знаешь, тетя! Конечно тебя!"
                        imgr Dial_Citizen_2_3
                        citizen2 "Мой брат слишком груб, но в целом он прав."
                        imgl Dial_Monica_Sandwich_2
                        menu:
                            "Что?! Да как вы можете просить такое?":
                                m "Что?! Да как вы можете просить такое?"
                                return
                            "Я подумаю, но сейчас я занята..." if fallingPathStarted == True:
                                m "Я подумаю, но сейчас я занята..."
                                mt "В любом случае я не могу ничего поделать в этом жутком наряде..."
                                return

            else:
                imgr Dial_Citizen_1_4
                citizen1 "Нам не нужны твои флаеры, тетя!"
                $ kebabWorkMonicaRefusedAmount += 1

    return
# диалог доступен только когда моника не работает на раздаче флаеров
label citizen1_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_1_1
    m "Эй, парни! Скажите, у вас есть деньги?"
    citizen1 "Смотря для чего, тетя. А тебе зачем?"
    m "Вы помнится хотели на меня посмотреть..."
    imgr Dial_Citizen_1_3
    citizen1 "Да, тетя, и до сих пор хотим!"
    m "Ну, я могу Вам кое-что показать, только нам лучше уйти отсюда."
    citizen1 "Конечно, тетя, без проблем."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long") from _call_change_scene_214
    call pylonController(2, 1) from _call_pylonController_149
    with fade
    citizen1 "Ну что, тетя..."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False

    label citizen1_dialogue_pilon_loop1:
    call pylonController(1, 1) from _call_pylonController_150
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1) from _call_pylonController_151 #
            citizen1 "Покажи нам свои классные сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1

            call pylonController(3, 3) from _call_pylonController_152
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4) from _call_showRandomImages_40
            call pylonController(3, 3) from _call_pylonController_153
            # img показывает сиськи
            citizen1 "Отличные сиськи, но как насчет того, чтобы снять все лишнее?"
            call pylonController(3, 2) from _call_pylonController_154
            m "Ну уж нет."
            call pylonController(3, 1) from _call_pylonController_155
            citizen1 "Ну и так не плохо."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)
            jump citizen1_dialogue_pilon_loop1
        "Покажи попу.":
            call pylonController(4, 1) from _call_pylonController_156
            citizen1 "Покажи нам свои красивый зад!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            call pylonController(4, 5) from _call_pylonController_157
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4) from _call_showRandomImages_41
            call pylonController(4, 5) from _call_pylonController_158
            citizen1 "Шикарная жопа, тетя!"
            call pylonController(4, 5) from _call_pylonController_159
            citizen1 "Почти как у моей бывшей."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen1_dialogue_pilon_loop1
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1) from _call_pylonController_160
            citizen1 "Покрутись на пилоне, тетя."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_161
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6) from _call_pylonController_162
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages1, 4) from _call_showRandomImages_42
#            call pylonController(4, 5)
            citizen1 "А ты крутишься как профессионал. Мне нравится!"
            $ restore_music()
            call pylonController(4, 1) from _call_pylonController_163
            with fade
            mt "Не думаю, что буду это делать часто..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen1_dialogue_pilon_loop1
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart4startsCompleted == True:
            call pylonController(4, 1) from _call_pylonController_164
            citizen1 "Мы хотим поглядеть на твои классные сиськи еще раз. Снимай все!"
            mt "Грязные панки..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1) from _call_pylonController_165
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen1_dialogue_pilon_loop1
            call pylonController(4, 5) from _call_pylonController_166
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4) from _call_showRandomImages_43
            call pylonController(4, 5) from _call_pylonController_167
            citizen1 "Черт, тетя! Они шикарны! И что же ты их раньше от нас прятала?"
            call pylonController(4, 1) from _call_pylonController_168

            citizen1 "Эй, тетя! Как насчет того, чтобы получить немного больше?"
            m "..."
            citizen1 "У меня идея! Нас как раз двое, как и твоих подружек. Давай обнимемся!"
            m "Даже не надейся!"
            citizen1 "Ладно, не горячись, тетя! Ты же не против заработать чуть больше... Сожми ка свои аппетитные соски!"
            label citizen1_dialogue_pilon_loop1_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothNakedBoobsNippleSquizeCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothNakedBoobsNippleSquizeCorruptionRequired] corruption"
                        jump citizen1_dialogue_pilon_loop1_1
                    m "Ладно."
                    call pylonController(3, 4) from _call_pylonController_169
                    with fade
                    w
                    call showRandomImages(nakedboobssquizenipplesImages, 1) from _call_showRandomImages_44
                    call pylonController(3, 4) from _call_pylonController_170
                    citizen1 "Уф...А ты горячая!"
                "Ну уж нет!":
                    call pylonController(3, 1) from _call_pylonController_171
                    m "Не собираюсь, и так достаточно."
                    citizen1 "Не ожидал я такого тетя. Думаю, ты скоро передумаешь."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen1_dialogue_pilon_loop1
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
                call pylonController(2, 1) from _call_pylonController_172
                citizen1 "Ну все, тетя, хватит. До следующего раза. Вот, держи."
                $ add_money(earnedMoney)
                call pylonController(1, 1) from _call_pylonController_173
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1) from _call_pylonController_174
            citizen1 "Тетя, и за что тебе платить? Ничего не получишь."
            return False
    return

# первый раз
label cit1_2_naked_boobs_1st:
    img 11745
    citizen1 "Тетя, у нас с братом возникла шикарная идея!"
    img 11746
    citizen1 "Мы ведь с тобой не первый раз видимся и уже не чужие люди.."
    img 11747
    m "Ты это к чему?"
    img 11748
    citizen1 "Мда, не умею я говорить намеками..."
    citizen1 "Короче мы хотим посмотреть на твои сиськи, но уже так сказать без всего!"
    img 11749
    menu:
        "Почему бы и нет.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11750

            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 11751
    m "Ну а мне это зачем?"
    img 11752
    citizen1 "Ну как зачем? А зачем ты нам их в одежде показываешь?"
    citizen1 "Мы заплатим!"
    img 11753
    m "Хорошо, смотрите, только руками не трогать!"
    m "И отвернитесь!"
    # отворачиваются
    img 11755
    w
    img 11754
    citizen1 "О чем речь, тетя! Разве мы когда нибудь тебя обманывали?"
    m "Можете поворачиваться.."
    img 11756
    w
    img 11757
    w
    # поворачиваются, моника показывает сиськи
    img 11758
    citizen1 "Ого! Прямо как у моей бывшей!"
    # показывает сиськи еще
    img 11759
    w
    img 11760
    citizen1 "Вот это класс, тетя! Так они смотрятся гораздо лучше."
    img 11761
    w
    img 11762
    w
    img 11763
    w
    img 11764
    # показывает сиськи еще
    w
    img 11765
    citizen1 "Да, сегодня день прошел не зря!"
    $ nakedBoobsFirstly_Cit1_2 = True
    return True

# вариант 1
label cit1_2_naked_boobs_variant1:
    img 11766
    citizen1 "Тетя, покажи нам свои сиськи!"
    img 11767
    m "Как именно?"
    img 11768
    citizen1 "А ты шутница. Конечно голыми, так интереснее!"
    img 11769
    menu:

        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11770

            m "Хватит с вас и того, что вы уже видели!"
            return False

    #m "Отвернитесь!"
    # отворачиваютяс, моника переодевается...
    #m "Можете повернуться."
    img 11771
    m "Хорошо."
    img 11772
    w
    img 11773
    m "Только руками не трогать!"
    img 11774
    citizen1 "Какие вопросы, тетя!"
    # показывает
    img 11775
    citizen1 "Не могу наглядеться, красота!"
    # смена картинки, под другим углом
    img 11776
    w
    img 11777
    w
    img 11778
    w
    img 11779
    citizen1 "Тетя, а че ты молчишь?"
    img 11780
    m "Мне нечего вам сказать..."
    img 11781
    citizen1 "Ого! Ну ладно, глядя на такие сиськи можно и ничего не говорить!"
    # смена картинки, под другим углом
    img 11782
    w
    img 11783
    w
    img 11784
    w
    img 11785
    citizen1 "Эй, тетя! Как насчет того, чтобы получить немного больше?"
    img 11786
    m "..."
    img 11787
    citizen1 "У меня идея! Нас как раз двое, как и твоих подружек. Давай обнимемся!"
    img 11788
    m "Даже не надейся!!!"
    img 11789
    citizen1 "Кто-то сегодня не в духе? Ладно, и так все очень хорошо!"
    return True

# вариант 2
label cit1_2_naked_boobs_variant2:
    img 11790
    citizen1 "Тетя, покажи нам свои сиськи!"
    img 11791
    m "Как именно?"
    img 11792
    citizen1 "Серьезно?! Давай снимай уже все!"
    img 11793
    menu:
        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11794
            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 11795
    m "Отвернитесь!"
    # отворачиваютяс, моника переодевается...
    img 11796
    w
    img 11797
    m "Можете повернуться."
    m "Только руками не трогать!"
    img 11798
    citizen1 "Конечно, тетя!"
    # показывает
    img 11799
    w
    img 11800
    w
    img 11801
    citizen1 "Вау! Как в первый раз!"
    img 11802
    w
    img 11803
    w
    img 11804
    # смена картинки
    img 11805
    citizen1 "Ты же не против заработать чуть больше... Сожми ка свои аппетитные соски!"
    img 11806
    m "Ну...Я не знаю..."
    img 11807
    citizen1 "Давай! И прямо сейчас получишь часть денег!"
    img 11808
    menu:
        "Хорошо.":
            $ add_money(0,5)
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11809
            m "Хватит с вас и того, что вы уже видели!"
            pass

    # смена картинки - моника сжимает соски
    img 12487
    w
    img 12488
    w
    img 12489
    citizen1 "Уф...А ты горячая!"
    citizen1 "И так заводит!"
    img 12490
    m "Ай!"
    mt "Это немного больно и даже немного приятно... Странно..."
    # смена картинки - моника сжимает соски
    img 12491
    w
    img 12492
    w
    img 12493
    citizen1 "Ух, тетя, снова нас порадовала!"
    # ?? может есть смысл сделать картинку: если было сжатие сосков - моника наклоняется и поднимает монетку
    return True
