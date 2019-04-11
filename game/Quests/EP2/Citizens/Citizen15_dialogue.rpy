default pylonpart2startsCompleted = False
default pylonpart3startsCompleted = False

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
    call change_scene("hostel_edge_1_a", "Fade_long")
    call pylonController(2, 1)
    with fadelong
    citizen15 "Ну что, начинай, только не разочаруй меня."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen15_dialogue_pilon_loop15:
    call pylonController(1, 1)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1)
            citizen15 "Для начала сиськи, показывай!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                call pylonController(3, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15

            call pylonController(3, 3)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(5, 3)
            citizen15 "И это все?"
            call pylonController(2, 3)
            # img показывает сиськи
            citizen15 "Мда, ну и так сойдет..."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)

            # Разовое событие после которого появится еще 1 события у пилона -  голая грудь
            #Первый раз!!!
            if fallingPathServedCustomersTotal >= 20 and 1==1:
                img 10571
                citizen15 "Хотя... Ты красивая девочка. Хочу оценить их без одежды."
                "Я недавно провернул одно дельце и у меня есть лишние 50$. Что скажешь?"
                menu:
                    "Согласиться..." if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                        pass
                    "Согласиться... (low corruption, required: [monicaWhoringClothNakedBoobsCorruptionRequired]) (disabled)" if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                        pass
                    "Отказаться.":
#                        call pylonController(4, 1)
                        img 10572
                        m "Да за кого ты меня принимаешь?!"
                        m "Этого не будет никогда!"
                        img 10571
                        citizen15 "Тогда мои 50$ достанутся более сговорчивой девочке."
                        jump citizen15_dialogue_pilon_loop15
#                call pylonController(1, 1) #моника просто стоит у пилона
                img 10573
                mt "50$ были бы не лишними... Хорошо, что здесь никого нет."
                img 10574
                m "50$ ?"
                img 10575
                citizen15 "Все верно, девочка. Покажешь своих подружек и они твои."
                img 10576
                mt "Черт! Моника, ты уверена что станешь делать это???"
                mt "Станешь показывать свою грудь какому-то нищему за жалкие 50$?"
                img 10577
                mt "Но, с другой стороны, это же не я показываю грудь, а какая-то шлюха в трущобах."
                mt "Ведь никто даже представить себе не может что это делает Моника Бакфетт."
                mt "Это как какая-то виртуальная игра, в которой все не по настоящему..."
                mt "Но вот 50$, которые я получу, вполне реальны!"
#                call pylonController(3, 1)
                img 10578
                m "Ладно, только не трогать!"
                img 10579
                citizen15 "Об этом не волнуйся, детка. Я не хочу проблем с твоим сутенером."
                img 10580
                mt "Да за кого он меня принимает?"
#                call pylonController(3, 2)
                img 10581
                m "Хорошо, давай деньги."
                img 10582
                citizen15 "Только после того, как покажешь."
                citizen15 "Деньги вперед я могу дать только твоему сутенеру!"
                citizen15 "Извини, но таким девочкам как ты я на слово не верю..."
#                citizen15 "А ты не глупая девочка. Вот, держи."
#                $ add_money(50)
#                with fade
#                call showRandomImages(nakedboobsImages, 4)
#                call pylonController(3, 5) #моника показывет голые сиськи
                img 10583
                m "!!!"
                m "Отвернись!"
                img 10584
                with fade
                w
                img 10585
                with fade
                w
                #показывает
                img 10586
                with fade
                w
                img 10587
                with Dissolve(0.3)
                $ renpy.pause(1.5)
                img 10586
                with Dissolve(0.3)
                citizen15 "Эй! Куда ты их спрятала?!"
                img 10588
                m "Я показала тебе свою грудь! Давай деньги!"
                citizen15 "Ты что, пошутила?! Я ничего не успел рассмотреть!"
                m "Ты увидел достаточно! Давай деньги, скорее!"
                img 10589
                citizen15 "Я не дам тебе ничего, пока ты не покажешь мне грудь нормально!"
                citizen15 "Я хочу рассмотреть ее как следует! Иначе никаких денег!"
                img 10590
                m "!!!"
                menu:
                    "Согласиться...":
                        pass
                    "Отказаться.":
#                        call pylonController(4, 1)
                        img 10591
                        m "Да за кого ты меня принимаешь?!"
                        citizen15 "Тогда мои 50$ достанутся более сговорчивой девочке."
                        jump citizen15_dialogue_pilon_loop15
                #Моника снова показывает грудь быстро
                img 10592
                with Dissolve(0.3)
                $ renpy.pause(0.5)
                img 10590
                with Dissolve(0.3)
                citizen15 "Эй! Хватит кривляться! Покажи грудь нормально!"

                img 10593
                citizen15 "Покажи грудь, а я досчитаю до пяти!"
                citizen15 "Если ты уберешь грудь раньше, то не получишь никаких денег!"
                img 10594
                with fade
                m "..."
                citizen15 "..."
                m "..."
                citizen15 "50$!"
                menu:
                    "Согласиться...":
                        pass
                    "Отказаться.":
#                        call pylonController(4, 1)
                        img 10572
                        m "Да за кого ты меня принимаешь?!"
                        citizen15 "Тогда мои 50$ достанутся более сговорчивой девочке."
                        jump citizen15_dialogue_pilon_loop15

                #Моника показывает грудь, а citizen ее обсматривает
                img 10595
                with Dissolve(0.5)
                w
                img 10596
                with fade
                citizen15 "Один..."
                img 10597
                with fade
                citizen15 "Два..."
                img 10598
                with fade
                citizen15 "Три..."
                img 10599
                with fade
                w
                img 10600
                with fade
                w
                img 10601
                w
                img 10602
                with fade
                citizen15 "Четыре..."
                img 10603
                with fade
                w
                img 10604
                with fade
                w
                img 10605
                with fade
                citizen15 "Пять..."
                #Моника убирает грудь
                img 10606
                m "Доволен?"
                citizen15 "Более чем..."
                $ add_money(50)
                $ pylonpart3startsCompleted = True
                # Добавить сколько то corruption
                $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen15_dialogue_pilon_loop15
        "Покажи попу.":
            call pylonController(4, 1)
            citizen15 "А теперь повернсь и покажи свой зад!"
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            call pylonController(4, 5)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(assImages, 4)
            call pylonController(4, 5)
            # img показывает зад
            citizen15 "Зад, 10 долларовой шлюхи, но еще рабочий."
            call pylonController(4, 1)
            mt "Что за козел. Врезать может ему?"
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen15_dialogue_pilon_loop15
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1)
            citizen15 "Покрутись немного на шесте, который сзади тебя."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6)
            with fade
            m "Хорошо, только не долго."
            mt "Только потому, что ты заплатишь."
            call showRandomImages(pylonClothDanceImages2, 4)
#            call pylonController(4, 5)
            citizen15 "Мда, тебе далеко до совершенства..."
            $ restore_music()
            call pylonController(4, 1)
            with fade
            mt "Ну и урод..."
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen15_dialogue_pilon_loop15
        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
            pass
        "Голые сиськи." if pylonpart3startsCompleted == True:
            #если активно ограничение показа груди
            citizen15 "А теперь покажи своих малышек, похоже им там тесно."
            mt "Мне надо как-то получить больше денег с этого бродяги..."
            mt "Может быть показать ему снова мою грудь?"
            mt "Он ведь уже видел ее..."
            m "Если ты хочешь, я могу показать тебе свою грудь..."
            m "Снова..."
            citizen15 "Конечно! Я соскучился по твоим малышкам!"
            m "50$!"
            citizen15 "Что? Какие еще 50$?"
            citizen15 "Я уже видел твоих малышек!"
            citizen15 "Хочешь снова 50$ - покажи мне другие!"
            citizen15 "Ты можешь привести кого-нибудь и поделить с ней деньги."
            citizen15 "Но учти, я уже видел почти всех малышек в этом районе!"
            citizen15 "За малышек, которые я уже видел, я готов заплатить [monicaWhoringNakedBoobsMoney]$!"
            m "Мне некого приводить!"
            m "И моя грудь самая лучшая!"
            mt "Черт! Все мировые издания об этом писали!"
            citizen15 "Я готов заплатить тебе [monicaWhoringNakedBoobsMoney]$ и не более..."
            menu:
                "Согласиться...":
                    pass
                "Отказаться.":
                    call pylonController(4, 1)
                    m "Да за кого ты меня принимаешь?!"
                    jump citizen15_dialogue_pilon_loop15
            call pylonController(4, 5)
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикоснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4)
            call pylonController(4, 5)
            citizen15 "А ничего такие сиськи, но я видел и лучше."
            call pylonController(4, 1)
            mt "Очень сомневаюсь..."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen15_dialogue_pilon_loop15

            #Если не хочет смотреть на них
            mt "Мне надо как-то получить больше денег с этого бродяги..."
            mt "Может быть показать ему снова мою грудь?"
            mt "Он ведь уже видел ее..."
            m "Если ты хочешь, я могу показать тебе свою грудь..."
            m "Снова..."
            citizen15 "Сегодня я не хочу смотреть твоих малышек!"
            citizen15 "Покажи их кому-нибудь другому!"
            citizen15 "Уверен, ты сможешь заработать [monicaWhoringNakedBoobsMoney]$."
            jump citizen15_dialogue_pilon_loop15

            #регулярный показ
            call pylonController(4, 1)
            citizen15 "А теперь покажи своих малышек, похоже им там тесно."
            mt "Как он может так говорить о моей прекрасной груди?! Извращенец..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen15_dialogue_pilon_loop15
            call pylonController(4, 5)
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикоснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4)
            call pylonController(4, 5)
            citizen15 "А ничего такие сиськи, но я видел и лучше."
            call pylonController(4, 1)
            mt "Очень сомневаюсь..."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
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
                call pylonController(2, 1)
                citizen15 "Красивая шлюшка. Уверен, ты можешь больше, а пока так..."
                $ add_money(earnedMoney)
                call pylonController(1, 1)
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1)
            citizen15 "Сходи поищи себе кого-нибудь еще."
            return False
    return

label citizen15_dialogue_after_boobs_first_time:
    mt "Дьявол!"
    mt "Я не уверена что мне стоило делать это!"
    mt "Я думала это будет проще!"
    mt "Этот урод заставил меня пол дня стоять на улице, сверкая своей обнаженной бесценной, очаровательной грудью!"
    mt "Но за эти же деньги мне пришлось бы два месяца носить рекламу кебаба..."
    mt "Главное - это то что меня никто не видел."
    mt "И никто не знает кто я на самом деле, так что я могу делать все что потребуется."
    mt "Мне пришлось показать грудь - пускай!"
    mt "Это поможет мне сэкономить время на поиск еды, чтобы потратить его на решение моих главных проблем."
    mt "Моя цель - это вернуть назад мою роскошную жизнь."
    mt "И я не остановлюсь ни перед чем!"
    return


label citizen15_dialogue_after_boobs_second_time:
    mt "Вот мерзавец!"
    mt "Он отказался смотреть на мою грудь даже за [monicaWhoringNakedBoobsMoney]$ !"
    mt "Может быть показать мою грудь кому-нибудь еще?"
    mt "Это звучит дико, но мне нужны деньги..."
    mt "Похоже, в этом районе все относятся совершенно нормально к таким вещам..."
    mt "А я нахожусь здесь анонимно..."
    mt "То что здесь происходит никак не связано с жизнью Моники Бакфетт."
    mt "Так что мне нечего стесняться."
    mt "Мне это глубоко противно, но я отношусь к этому с хладнокровием."
    mt "В конце концов, это ненадолго."
    return

#
