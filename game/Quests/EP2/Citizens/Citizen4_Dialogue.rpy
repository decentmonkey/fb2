default citizen4BoobsShowedFirstTime = False
default citizen4BoobsShowedSecondTimeCount = 0
default citizen4BoobsNakesShowingActive = False
default citizen4BoobsNakesShowedLastDay = 0

label citizen4_dialogue:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_4_1
    if citizen4_offered_last_day == day:
        imgr Dial_Citizen_4_4
        citizen4 "Нельзя!"
        return
    citizen4 "Да?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            $ citizen4_offered_last_day = day
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen4_refuse_probability) > 0:
                imgr Dial_Citizen_4_2
                call reduce_flyers() from _call_reduce_flyers_2
                citizen4 "Хорошо."
                citizen4 "А что на нем?"
                m "Это реклама вкусного кебаба... Там же написано!"
                imgr Dial_Citizen_4_3
                citizen4 "А я подумал Вы решили познакомиться со мной!"
                menu:
                    "У меня нет желания знакомиться с Вами!":
                        $ kebabWorkHarassmentAmount +=1
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "У меня нет желания знакомиться с Вами!"
                    "Что Вы подразумеваете под знакомством?":
                        m "Что вы имеете ввиду?"
                        citizen4 "Я бы хотел узнать по ближе такую красотку. Думаю, мы бы договорились."
                        m "Договорились о чем?"
                        citizen4 "Что за вопросы? Обычно девушки вашей профессии это понимают."
                        mt "Да что за люди здесь живут?! Всем надо одно и то же..."
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."
            else:
                imgr Dial_Citizen_4_4
                citizen4 "Давайте в другой раз!"
                $ kebabWorkMonicaRefusedAmount += 1
#        "Уйти.":
#            pass
    return

    # диалог доступен только когда моника не работает на раздаче флаеров
label citizen4_dialogue_pilon:
    imgl Dial_begin35_17
    imgr Dial_Citizen_4_1
    m "Привет! Помню, ты хотел познакомиться поближе?"
    imgr Dial_Citizen_4_3
    citizen4 "Конечно, давай познакомимся."
    m "Ну я не о близком знакомстве...Немного о другом."
    citizen4 "Да не вопрос, я понимаю о чем речь. Любой из нашего района тебя поймет с полуслова."
    # уходят к пилону.
    call change_scene("hostel_edge_1_a", "Fade_long")
    call pylonController(2, 1)
    with fade
    citizen4 "Ну что, давай начнем."
    $ showedBoobs = False
    $ showedButt = False
    $ showedDance = False
    $ showedNakedBoobs = False
    label citizen4_dialogue_pilon_loop4:
    call pylonController(1, 1)
    menu:
        "Покажи сиськи.":
            call pylonController(3, 1)
            citizen4 "Покажи мне свои сиськи!"
            if corruption < monicaWhoringClothBoobsCorruptionRequired:
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothBoobsCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(3, 3)
            with fade
            m "Я не собираюсь раздеваться, только так."
            call showRandomImages(boobsImages, 4)
            call pylonController(5, 3)
            # img показывает сиськи
            citizen4 "Да, очень хорошо, но я видел сиськи и получше!"
            call pylonController(5, 1)
            mt "Козел!"
            call pylonController(3, 1)
            citizen4 "Хотя весьма не плохо."
            $ showedBoobs = True
            $ add_corruption(monicaWhoringClothBoobsCorruptionProgress, "monicaWhoringClothBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("BoobsCloth", 1)


            # Разовое событие после которого появится еще 1 события у пилона -  голая грудь
            #Первый раз!!!
            # Ситизен предлагает Монике показать грудь за $ 50
            $ store_music()
            call citizen4_show_boobs_first_time()
            $ restore_music()
            if _return == True:
                $ citizen4BoobsShowedFirstTime = True
            jump citizen4_dialogue_pilon_loop4
        "Покажи попу.":
            call pylonController(4, 1)
            citizen4 "Покажи свой задницу."
            if corruption < monicaWhoringClothAssCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothAssCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(4, 5)
            with fade
            m "Я не собираюсь раздеваться, только так."
            # img показывает зад
            call showRandomImages(assImages, 4)
            call pylonController(4, 5)
            citizen4 "Красивая задница, но я люблю побольше!"
            call pylonController(4, 5)
            citizen4 "Но ее можно увеличить, подумай об этом."
            $ showedButt = True
            $ add_corruption(monicaWhoringClothAssCorruptionProgress, "monicaWhoringClothAssCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("AssCloth", 1)
            jump citizen4_dialogue_pilon_loop4
        "Станцуй. (мало свиданий) (disabled)" if fallingPathGetCitizenData("visits") < monicaWhoringClothPylonDanceVisitsRequired:
            pass
        "Станцуй." if fallingPathGetCitizenData("visits") >= monicaWhoringClothPylonDanceVisitsRequired:
            call pylonController(4, 1)
            citizen4 "Покрутись на шесте немного. Надеюсь, ты хорошо двигаешься."
            if corruption < monicaWhoringClothPylonDanceCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothPylonDanceCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            $ store_music()
            music Molten_Alloy
            call pylonController(4, 6)
            with fade
            m "Хорошо, только не долго."
            call showRandomImages(pylonClothDanceImages3, 4)
#            call pylonController(4, 5)
            citizen4 "Сойдет. У меня есть знакомая стриптизерша. Если хочешь, могу вас познакомить."
            "Уж она то научит тебя всему."
            $ restore_music()
            call pylonController(4, 1)
            with fade
            mt "И что ты за козел?!"
            $ showedDance = True
            $ add_corruption(monicaWhoringClothPylonDanceCorruptionProgress, "monicaWhoringClothPylonDanceCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            $ store_citizen_action("PylonDanceCloth", 1)
            jump citizen4_dialogue_pilon_loop4
#        "Голые сиськи. (disabled)" if pylonpart3startsCompleted == False and 1==2:
        "Голые сиськи. (disabled)" if citizen4BoobsNakesShowingActive == True and citizen4BoobsNakesShowedLastDay == day:
            pass
        "Голые сиськи." if citizen4BoobsNakesShowingActive == True and citizen4BoobsNakesShowedLastDay != day:
            $ citizen4BoobsNakesShowedLastDay = day
            $ store_music()
            call citizen4_show_boobs_regular_time()
            $ restore_music()
            jump citizen4_dialogue_pilon_loop4

            #регулярный показ (активировать позже!)
            call pylonController(4, 1)
            citizen4 "А теперь покажи своих малышек, похоже им там тесно."
            mt "Как он может так говорить о моей прекрасной груди?! Извращенец..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop15
            call pylonController(4, 5)
            with fade
            m "Так и быть, только руками не трогать."
            mt "Только попробуй к ним прикоснуться и я сломаю тебе пальцы."
            call showRandomImages(nakedboobsImages, 4)
            call pylonController(4, 5)
            citizen4 "А ничего такие сиськи, но я видел и лучше."
            call pylonController(4, 1)
            mt "Очень сомневаюсь..."
            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen4_dialogue_pilon_loop4

            # DEPRECATED (старый диалог, замененный из citizen4!)
            call pylonController(4, 1)
            citizen4 "Показывай сиськи, только не забудь все снять."
            mt "Урод..."
            if corruption < monicaWhoringClothNakedBoobsCorruptionRequired:
                call pylonController(4, 1)
                mt "Я не могу себе этого позволить!"
                "Я еще не настолько опустилась!"
                "И, надеюсь, этого не произойдет НИКОГДА!"
                help "Требуется [monicaWhoringClothNakedBoobsCorruptionRequired] corruption"
                jump citizen4_dialogue_pilon_loop4
            call pylonController(4, 5)
            with fade
            m "Так и быть, только руками не трогать."
            call showRandomImages(nakedboobsImages, 4)
            call pylonController(4, 5)
            citizen4 "Должен признать, твои сиськи хороши."
            mt "Ну еще бы!"
            citizen4 "Хотя страшно подумать, что с ними станет лет через 10..."
            mt "Что?"
            citizen4 "Знаешь, мой знакоый может тебе помочь кое в чем... За каких нибудь 500$ твои подруги наберут вес."
            citizen4 "Тебе дать его номер?"
            call pylonController(4, 1)
            m "Меня это не интересует! С тебя хватит!"

            citizen4 "Погоди минутку. Потряси ка своими сочными сиськами!"
            label citizen4_dialogue_pilon_loop4_1:
            menu:
                "Хорошо.":
                    if corruption < monicaWhoringClothNakedBoobsShakeCorruptionRequired:
                        mt "Уже достаточно, что он вот так глазеет на меня"
                        "Хватит с него и того, что он видит."
                        help "Требуется [monicaWhoringClothNakedBoobsShakeCorruptionRequired] corruption"
                        jump citizen4_dialogue_pilon_loop4_1
                    m "Ладно."
                    call pylonController(3, 4)
                    with fade
                    w
                    call showRandomImages(nakedboobsshakeImages, 1)
                    call pylonController(3, 4)
                    citizen4 "О да! Теперь мне еще больше хочется их потрогать!"
                    m "Даже не думай!"
                "Ну уж нет!":
                    call pylonController(3, 1)
                    m "Не собираюсь, и так достаточно."
                    citizen4 "Как хочешь. Похоже, мне придется найти другую шлюху."

            $ showedNakedBoobs = True
            $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
            jump citizen4_dialogue_pilon_loop4
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
                citizen4 "А ты ничего такая, надо будет вернуться к нашему знакомству. Держи, заслужила."
                $ add_money(earnedMoney)
                call pylonController(1, 1)
                m "Что?! Так мало? Мог бы дать и больше!"
                mt "Ну ничего, скоро я стану богатой и верну свою жизнь..."
                return
            #если не было ничего
            call pylonController(5, 1)
            citizen4 "Какое то не продуктивное вышло знакомство. Надеюсь, в другой раз будет лучше."
            return False
    return





label citizen4_show_boobs_first_time:
    # Ситизен предлагает Монике показать грудь за $ 50
    music Groove2_85
    img 10571
    with fade
    citizen4 "Хотя... Ты красивая девочка. Хочу оценить их без одежды."
    "Я недавно провернул одно дельце и у меня есть лишние 50$. Что скажешь?"
    menu:
        "Согласиться..." if corruption >= monicaWhoringClothNakedBoobsCorruptionRequired and fallingPathServedCustomersTotal >= 20:
            pass
        "Согласиться... (low corruption, required: [monicaWhoringClothNakedBoobsCorruptionRequired], required: 20 customers) (disabled)" if corruption < monicaWhoringClothNakedBoobsCorruptionRequired or fallingPathServedCustomersTotal < 20:
            pass
#        if fallingPathServedCustomersTotal >= 20 and citizen4BoobsShowedFirstTime == False:
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10572
            with fade
            m "Да за кого ты меня принимаешь?!"
            m "Этого не будет никогда!"
            img 10571
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return False
#                call pylonController(1, 1) #моника просто стоит у пилона
    img 10573
    with fade
    mt "50$ были бы не лишними... Хорошо, что здесь никого нет."
    img 10574
    with diss
    m "50$ ?"
    img 10575
    citizen4 "Все верно, девочка. Покажешь своих подружек и они твои."
    img 10576
    with fade
    mt "Черт! Моника, ты уверена что станешь делать это???"
    mt "Станешь показывать свою грудь какому-то нищему за жалкие 50$?"
    img 10577
    with diss
    mt "Но, с другой стороны, это же не я показываю грудь, а какая-то шлюха в трущобах."
    mt "Ведь никто даже представить себе не может что это делает Моника Бакфетт."
    mt "Это как какая-то виртуальная игра, в которой все не по настоящему..."
    mt "Но вот 50$, которые я получу, вполне реальны!"
#                call pylonController(3, 1)
    img 10578
    with fade
    m "Ладно, только не трогать!"
    img 10579
    citizen4 "Об этом не волнуйся, детка. Я не хочу проблем с твоим сутенером."
    music Power_Bots_Looop
    img 10580
    mt "Да за кого он меня принимает?"
#                call pylonController(3, 2)
    img 10581
    m "Хорошо, давай деньги."
    music Groove2_85
    img 10582
    with diss
    citizen4 "Только после того, как покажешь."
    citizen4 "Деньги вперед я могу дать только твоему сутенеру!"
    citizen4 "Извини, но таким девочкам как ты я на слово не верю..."
#                citizen4 "А ты не глупая девочка. Вот, держи."
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
    music Loved_Up
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
    music stop
    sound plastinka2
    img 10586
    with Dissolve(0.3)
    music Groove2_85
    citizen4 "Эй! Куда ты их спрятала?!"
    img 10588
    with diss
    m "Я показала тебе свою грудь! Давай деньги!"
    citizen4 "Ты что, пошутила?! Я ничего не успел рассмотреть!"
    m "Ты увидел достаточно! Давай деньги, скорее!"
    img 10589
    with fade
    citizen4 "Я не дам тебе ничего, пока ты не покажешь мне грудь нормально!"
    citizen4 "Я хочу рассмотреть ее как следует! Иначе никаких денег!"
    img 10590
    with fadelong
    m "!!!"
    menu:
        "Согласиться...":
            pass
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10591
            with fade
            m "Да за кого ты меня принимаешь?!"
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return False
    #Моника снова показывает грудь быстро
    music Loved_Up
    img 10592
    with Dissolve(0.3)
    $ renpy.pause(0.5)
    music stop
    sound plastinka2
    img 10590
    with Dissolve(0.3)
    music Groove2_85
    citizen4 "Эй! Хватит кривляться! Покажи грудь нормально!"

    img 10593
    citizen4 "Покажи грудь, а я досчитаю до пяти!"
    citizen4 "Если ты уберешь грудь раньше, то не получишь никаких денег!"
    img 10594
    with fade
    m "..."
    citizen4 "..."
    m "..."
    citizen4 "50$!"
    menu:
        "Согласиться...":
            pass
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10572
            with fade
            m "Да за кого ты меня принимаешь?!"
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return False

    #Моника показывает грудь, а citizen ее обсматривает
    music Loved_Up
    img 10595
    with Dissolve(1.0)
    w
    img 10596
    with fade
    citizen4 "Один..."
    img 10597
    with fade
    citizen4 "Два..."
    img 10598
    with fade
    citizen4 "Три..."
    img 10599
    with fade
    w
    img 10600
    with fade
    w
    img 10601
    with diss
    w
    img 10602
    with fade
    citizen4 "Четыре..."
    img 10603
    with fade
    w
    img 10604
    with fade
    w
    citizen4 "Пять..."
    #Моника убирает грудь
    music Groove2_85
    img 10606
    with diss
    m "Доволен?"
    citizen4 "Более чем..."
    $ add_money(50)
    $ pylonpart3startsCompleted = True
    # Добавить сколько то corruption
    $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))
    $ citizen4BoobsShowedFirstTime = True
    $ citizen4BoobsNakesShowingActive = True
    $ add_hook("enter_scene", "citizen4_dialogue_after_boobs_first_time", scene="hostel_edge_1_a")
    return True


label citizen4_show_boobs_regular_time:
    if (citizen4BoobsShowedSecondTimeCount < 2 or rand(1,2) == 1) and citizen4BoobsShowedSecondTimeCount != 1: #Показываем первые 1 раз точно, затем по рандому, кроме 2-го раза!
        #если активно ограничение показа груди
        img 10571
        with fade
        citizen4 "А теперь покажи своих малышек, похоже им там тесно."
        img 10573
        with fade
        mt "Мне надо как-то получить больше денег с этого бродяги..."
        mt "Может быть показать ему снова мою грудь?"
        mt "Он ведь уже видел ее..."
        img 10583
        with fade
        m "Если ты хочешь, я могу показать тебе свою грудь..."
        m "Снова..."
        img 10589
        citizen4 "Конечно! Я соскучился по твоим малышкам!"
        img 10581
        m "50$!"
        img 10593
        citizen4 "Что? Какие еще 50$?"
        citizen4 "Я уже видел твоих малышек!"
        citizen4 "Хочешь снова 50$ - покажи мне другие!"
        citizen4 "Ты можешь привести кого-нибудь и поделить с ней деньги."
        citizen4 "Но учти, я уже видел почти всех малышек в этом районе!"
        citizen4 "За малышек, которые я уже видел, я готов заплатить [monicaWhoringNakedBoobsMoney]$!"

        music Pyro_Flow
        img 10572
        with fade
        m "Мне некого приводить!"
        m "И моя грудь самая лучшая!"
        mt "Черт! Все мировые издания об этом писали!"
        music Groove2_85
        img 10571
        citizen4 "Я готов заплатить тебе [monicaWhoringNakedBoobsMoney]$ и не более..."
        menu:
            "Согласиться...":
                pass
            "Отказаться.":
    #            call pylonController(4, 1)
                m "Да за кого ты меня принимаешь?!"
                return False
        music Hidden_Agenda
        sound snd_fabric1
        img 10585
        with fadelong
        w
        img 10586
        with fade
        w
        img 10592
        with diss
        m "Так и быть, только руками не трогать."
        img 10596
        with diss
        mt "Только попробуй к ним прикоснуться и я сломаю тебе пальцы."
        img 10603
        with diss
        citizen4 "А ничего такие сиськи, но я видел и лучше."
        img 10606
        with fade
        mt "Очень сомневаюсь..."
        $ showedNakedBoobs = True
        $ add_corruption(monicaWhoringClothNakedBoobsCorruptionProgress, "monicaWhoringClothNakedBoobsCorruption_day_" + str(day) + "_citizen" + str(citizenId))

        $ citizen4BoobsShowedSecondTimeCount += 1
        return True

    #Если не хочет смотреть на них
    img 10573
    with fade
    mt "Мне надо как-то получить больше денег с этого бродяги..."
    mt "Может быть показать ему снова мою грудь?"
    mt "Он ведь уже видел ее..."
    img 10583
    with fade
    m "Если ты хочешь, я могу показать тебе свою грудь..."
    m "Снова..."
    img 10593
    citizen4 "Сегодня я не хочу смотреть твоих малышек!"
    citizen4 "Покажи их кому-нибудь другому!"
    citizen4 "Уверен, ты сможешь заработать [monicaWhoringNakedBoobsMoney]$."
    $ add_hook("enter_scene", "citizen4_dialogue_after_boobs_second_time", scene="hostel_edge_1_a")

    return

label citizen4_dialogue_after_boobs_first_time:
    $ remove_hook()
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


label citizen4_dialogue_after_boobs_second_time:
    $ remove_hook()
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
    help "Будет доступно в следующем обновлении игры. Следите за новостями!"
    return
