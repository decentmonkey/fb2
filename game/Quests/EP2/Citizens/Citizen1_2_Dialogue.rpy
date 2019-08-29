default citizen1BoobsNakesShowedLastDay = 0
default citizen1BoobsNakedDancedLastDay = 0
default citizen1BoobsNakesShowedCount = -1
default citizen1BoobsNakedDancedCount = -1

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
    $ showedNakedBoobsDance = False

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
        "Голые сиськи. (disabled)" if pylonpart4startsCompleted == False or citizen1BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen1BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsVisitsRequired:
            pass
        "Голые сиськи." if (pylonpart4startsCompleted == True and citizen1BoobsNakesShowedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsVisitsRequired:
            $ store_music()
            if citizen1BoobsNakesShowedCount == -1:
                call cit1_2_naked_boobs_1st() from _call_cit1_2_naked_boobs_1st
                if _return != False:
                    $ citizen1BoobsNakesShowedCount += 1
            else:
                if citizen1BoobsNakesShowedCount%2 == 0:
                    call cit1_2_naked_boobs_variant1() from _call_cit1_2_naked_boobs_variant1
                if citizen1BoobsNakesShowedCount%2 == 1:
                    call cit1_2_naked_boobs_variant2() from _call_cit1_2_naked_boobs_variant2
                $ citizen1BoobsNakesShowedCount += 1
            if _return != False:
                $ citizen1BoobsNakesShowedLastDay = day
                $ showedNakedBoobs = True
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen1_dialogue_pilon_loop1


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
        "Станцуй с голыми сиськами. (disabled)" if pylonpart4startsCompleted == False or citizen1BoobsNakedDancedLastDay == day:
            pass
        "Станцуй с голыми сиськами. (мало свиданий) (disabled)" if (pylonpart4startsCompleted == True and citizen1BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") < monicaWhoringNakedBoobsDanceVisitsRequired:
            pass
        "Станцуй с голыми сиськами." if (pylonpart4startsCompleted == True and citizen1BoobsNakedDancedLastDay != day) and fallingPathGetCitizenData("visits") >= monicaWhoringNakedBoobsDanceVisitsRequired and citizen1BoobsNakesShowedCount>=0:
            $ store_music()
            if citizen1BoobsNakedDancedCount == -1:
                call cit1_2_naked_boobs_dance_1st()
                if _return != False:
                    $ citizen1BoobsNakedDancedCount += 1
            else:
                if citizen1BoobsNakedDancedCount%2 == 0:
                    call cit1_2_naked_boobs_dance_variant1()
                if citizen1BoobsNakedDancedCount%2 == 1:
                    call cit1_2_naked_boobs_dance_variant2()
                $ citizen1BoobsNakedDancedCount += 1
            if _return != False:
                $ citizen1BoobsNakedDancedLastDay = day
                $ showedNakedBoobsDance = True
                $ add_corruption(monicaWhoringClothNakedBoobsDanceCorruptionProgress, "monicaWhoringClothNakedBoobsDanceCorruptionProgress_day_" + str(day) + "_citizen" + str(citizenId))
            $ restore_music()
            jump citizen1_dialogue_pilon_loop1


        "Достаточно на сегодня.":
            $ earnedMoney = 0
            if showedBoobs == True or showedButt == True or showedDance == True or showedNakedBoobs == True or showedNakedBoobsDance == True:
                if showedBoobs == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedButt == True:
                    $ earnedMoney += monicaWhoringClothBoobsOrButtMoney
                if showedDance == True:
                    $ earnedMoney += monicaWhoringClothDanceMoney
                if showedNakedBoobs == True:
                    $ earnedMoney += monicaWhoringNakedBoobsMoney
                if showedNakedBoobsDance == True:
                    $ earnedMoney += monicaWhoringNakedBoobsMoneyDance
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
    with fade
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
        "Мне нужны деньги...":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11750

            m "Хватит с вас и того, что вы уже видели!"
            return False
    music Groove2_85
    img 11751
    with fade
    m "Ну а мне это зачем?"
    img 11752
    citizen1 "Ну как зачем? А зачем ты нам их в одежде показываешь?"
    citizen1 "Мы заплатим!"
    music Hidden_Agenda
    img 11753
    with diss
    m "Хорошо, смотрите, только руками не трогать!"
    m "И отвернитесь!"
    # отворачиваются
    sound snd_fabric1
    img 11755
    with fade
    w
    img 11754
    citizen1 "О чем речь, тетя! Разве мы когда нибудь тебя обманывали?"
    m "Можете поворачиваться.."
    img 11756
    w
    img 11757
    w
    # поворачиваются, моника показывает сиськи
    music Loved_Up
    img 11758
    with diss
    citizen1 "Ого! Прямо как у моей бывшей!"
    # показывает сиськи еще
    img 11759
    with diss
    w
    img 11760
    with diss
    citizen1 "Вот это класс, тетя! Так они смотрятся гораздо лучше."
    img 11761
    with diss
    w
    img 11762
    with diss
    w
    img 11763
    with diss
    w
    img 11764
    with diss
    # показывает сиськи еще
    w
    music Groove2_85
    img 11765
    with diss
    citizen1 "Да, сегодня день прошел не зря!"
    $ nakedBoobsFirstly_Cit1_2 = True
    return True

# вариант 1
label cit1_2_naked_boobs_variant1:
    music Groove2_85
    img 11766
    with fade
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
    m "Хорошо. Если заплатите..."
    music Loved_Up
    img 11772
    with fadelong
    w
    img 11773
    with diss
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
    with diss
    m "..."
    img 11787
    citizen1 "У меня идея! Нас как раз двое, как и твоих подружек. Давай обнимемся!"
    music Groove2_85
    img 11788
    with diss
    m "Даже не надейся!!!"
    img 11789
    citizen1 "Кто-то сегодня не в духе? Ладно, и так все очень хорошо!"
    return True

# вариант 2
label cit1_2_naked_boobs_variant2:
    music Groove2_85
    img 11790
    with fade
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
    with fade
    m "Отвернитесь!"
    # отворачиваютяс, моника переодевается...
    music Loved_Up
    sound snd_fabric1
    img 11796
    with fade
    w
    img 11797
    with diss
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
    music Groove2_85
    img 11805
    citizen1 "Ты же не против заработать чуть больше... Сожми ка свои аппетитные соски!"
    img 11806
    m "Ну...Я не знаю..."
    img 11807
    citizen1 "Давай! И прямо сейчас получишь часть денег!"
    img 11808
    menu:
        "Хорошо.":
            $ add_money(0.5)
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11809
            m "Хватит с вас и того, что вы уже видели!"
            return True

    # смена картинки - моника сжимает соски
    music Loved_Up
    img 12487
    with fade
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
    music Groove2_85
    img 12493
    with fade
    citizen1 "Ух, тетя, снова нас порадовала!"
    # ?? может есть смысл сделать картинку: если было сжатие сосков - моника наклоняется и поднимает монетку
    return True

# первый раз танцы с сиськами
label cit1_2_naked_boobs_dance_1st:
    music Groove2_85
    img 13188
    with fade
    citizen1 "Тетя, нам скучно!"
    citizen1 "Как насчет еще одного танца на пилоне?"
    img 13189
    m "Вы уже видели меня танцующей там.."
    img 13190
    citizen1 "Эм...Ну да..."
    citizen1 "Короче потанцуй для нас без кофты."
    img 13191
    with fade
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 13192
            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 13193
    with fade
    mt "Я уже танцевала, мою прекрасную грудь они видели... Не так страшно, если все это будет вместе."
    mt "Хуже уже не будет... А мне нужны деньги..."
    img 13194
    m "Сколько вы заплатите?"
    img 13195
    citizen1 "Тетя, тариф стандартный!"
    citizen1 "Но если ты готова станцевать с бутылкой в заднице, это можно обсудить!"
    music Power_Bots_Loop
    img 13196
    m "Что?! Да как ты смеешь такое говорить?!"
    img 13197
    citizen1 "Ой, тетя! Не кипятись, я пошутил..."
    music Groove2_85
    img 13198
    with fade
    m "Только вздумайте еще раз так пошутить! Отвернитесь!"

    # отворачиваются
    img 13199
    with diss
    w
    sound snd_fabric1
    img 13200
    with diss
    citizen1 "Конечно, тетя, не вопрос."
    music Loved_Up
    img 13201
    with fade
    m "Можете поворачиваться..."
    # поворачиваются, моника стоит с голыми сиськами
    img 13202
    citizen1 "Да, они шикарны. Можешь начинать."
    # движение на пилоне
    music Molten_Alloy
    img 13203
    with diss
    w
    img 13204
    with diss
    w
    img 13205
    citizen1 "Отлично, тетя!"
    # движение на пилоне еще
    img 13206
    with diss
    w
    img 13207
    with diss
    citizen1 "Черт, как глупо было просить тебя крутиться в одежде!"
    # движение на пилоне еще
    img 13208
    with diss
    w
    img 13209
    with diss
    w
    img 13210
    with diss
    citizen1 "Вау, тетя! Тебе нужно этим зарабатывать! Хотя стоп, этим ты и занимаешься!"
    citizen1 "Ха-ха-ха!"
    music Groove2_85
    img 13211
    with fade
    mt "Грязные панки..."
    mt "Мерзавцы..."
    $ nakedBoobsDanceFirstly_Cit1_2 = True
    return True

# первый выриант
label cit1_2_naked_boobs_dance_variant1:
    music Groove2_85
    img 13212
    with fade
    citizen1 "Тетя, мы снова хотим ощутить себя в стрип клубе!"
    citizen1 "Как насчет еще одного танца на пилоне?"
    img 13213
    m "В стрип клубе платят больше, да и вход туда бывает платный."
    img 13214
    citizen1 "Но мы ведь не в стрип клубе!"
    citizen1 "Станцуй для нас, и сиськи не забудь оголить."
    img 13215
    with fade
    menu:
        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 13216
            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 13217
    with fade
    m "Сколько вы заплатите?"
    img 13218
    citizen1 "Снова ты за свое!"
    citizen1 "Можно подумать о том, как ты можешь заработать больше, но в другой раз."
    citizen1 "И вообще, ты нас утомляешь своей болтовней, раздевайся уже!"
    img 13219
    with diss
    menu:
        "Хорошо.":
            pass
        "Я передумала.":
            img 13220
            m "Нет, не будет вам танцев!"
            m "Вы и так уже видели достаточно!"
            return False
    img 13221
    with fade
    m "Хорошо. Отвернитесь!"
    # отворачиваются
    img 13222
    citizen1 "Конечно, тетя, не вопрос."
    sound snd_fabric1
    music Loved_Up
    img 13223
    with fade
    w
    img 13224
    with fadelong
    m "Можете поворачиваться.."
    # поворачиваются, моника стоит с голыми сиськами
    img 13225
    citizen1 "Тетя, тебе особое приглашение нужно? Начинай уже!"
    # движение на пилоне
    music Molten_Alloy
    img 13226
    with diss
    w
    img 13227
    with diss
    citizen1 "Отлично, тетя!"
    # движение на пилоне еще
    img 13228
    with diss
    w
    img 13229
    with diss
    citizen1 "Черт, как глупо было просить тебя крутиться в одежде!"
    # движение на пилоне еще
    img 13230
    with diss
    w
    img 13231
    with diss
    citizen1 "И зачем мы ходим в стрип клуб?"
    # моника слезает  спилона, панк достает бутылку
    img 13234
    w
    img 13232
    with fade
    citizen1 "Тетя, ты помнишь про наше предложение насчет бутылки?"
    # моника злая
    music Power_Bots_Loop
    img 13233
    with fade
    m "Еще слово, и я засуну бутылку тебе в зад!"
    img 13235
    citizen1 "Ха-ха-ха! Два раза одна и та же шутка прошла!"
    music Groove2_85
    img 13236
    with fade
    mt "Грязные панки..."
    img 13237
    citizen1 "Ладно, молодец, тетя, нам понравилось!"
    return True

# второй выриант
label cit1_2_naked_boobs_dance_variant2:
    music Groove2_85
    img 13238
    with fade
    citizen1 "Тетя, станцуй! И не забуть снять кофту!"
    img 13239
    with fade
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 13240
            m "Хватит с вас и того, что вы уже видели!"
            return False
    img 13241
    with fade
    m "Хорошо. Отвернитесь!"
    # отворачиваются
    music Loved_Up
    img 13242
    with diss
    citizen1 "..."
    sound snd_fabric1
    img 13223
    with fade
    w
    img 13224
    with fadelong
    m "Можете поворачиваться.."
    # поворачиваются, моника стоит с голыми сиськами
    img 13225
    citizen1 "Начинай!"
    img 13243
    mt "Что-то они какие-то молчаливые... Это подозрительно..."
    # движение на пилоне
    music Molten_Alloy
    img 13244
    with diss
    w
    img 13245
    with diss
    citizen1 "Отлично!"
    # движение на пилоне еще
    img 13246
    with diss
    w
    img 13247
    with diss
    citizen1 "Не плохо!"
    img 13248
    with diss
    mt "Что это с ними сегодня? Они ведут себя не как обычно..."
    # движение на пилоне еще
    # когда моника крутится на пилоне спиной к панкам, один из них достает
    # телефон, и фоткает другого на фоне моники когда она не видит
    # звук фотографировния
    # моника слезает с шеста
    img 13249
    with diss
    w
    img 13250
    with diss
    call photoshop_flash()
    w
    music Groove2_85
    img 13251
    with diss
    m "Что это был за звук?"
    img 13252
    mt "Как будто меня сфотографировали..."
    img 13253
    citizen1 "Какой звук, тетя? Мы ничего не слышали."
    img 13254
    m "Вы меня сфотографировали?"
    img 13255
    citizen1 "Нет, тетя! Да и откуда у нас фотоаппарат?"
    img 13256
    with fade
    mt "И правда, откуда... Хотя... Нет, у них нет фотоаппарата..."
    img 13257
    with diss
    citizen1 "Кстати, отличный танец!"
    return True
