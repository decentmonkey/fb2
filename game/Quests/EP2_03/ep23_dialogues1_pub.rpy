# сюжетка бара
# Бармен постоянно смотрит на других женщин, поставил пилон и тд
# Жена сварливая, ревнует его, говорит он извращенец и что пилон и тд только из-за денег
# На Монику жена смотрит как на проститутку и не хочет брать.
# Сначала берут посудомойкой (без документов), за что Моника может бесплатно есть в баре нормальную еду. (если уже сегодня ела, то не хочет работать)
# Когда Моника моет посуду, игрок может кликать на бармена, который лапает ее за зад
# Иногда появляется также около мужа жена.
# Если Моника кликнула на жену, то та тоже лапает Монику за зад (на что Моника очень удивляется, а жена в ответ сварливо ворчит чтобы та лучше мыла посуду, везде грязь! Моника думает о своем положении)
# Жена на самом деле любит девочек тоже, поэтому в том числе и согласилась на пилон. При лапании Моника может ругаться, либо терпеть.
# Если Моника терпит, то повышает левел у бармена, либо у жены. Если у жены lvl2, то она начинает говорить что такой красивый белый зад никогда не лапала (и улыбается, Моника понимает что та любит девочек).
# Моника комментирует что это реально сверкающая дыра с извращенцами
# Бармен lvl2 - уговаривает жену, чтобы Моника работала без документов официанткой. Жена соглашается, но чтобы Моника отдавала почти все чаевые (ее доход 5-10%), т.к. та отбирает у жены работу и приносит риск, так как работает без документов.
# Моника работает официанткой, позволяя или нет лапать себя (corruption и progress).
# Внчале работы выбор кем работает сегодня (официантка, посудомойка)
# Каждую смену Моника должна сдавать чаевые, с которых ей дают маленький процент.
# Если Моника не сдает чаевые, а пытается уйти, то ее ловят и вешают на нее долг (гораздо больше чем было чаевых, около 300-1000$).
# Чтобы погасить долг, Моника начинает танцевать на пилоне (все более и более развратно, а также одевать более вызывающую и открытую униформу официантки) - линейный прогресс постепенно.
# Если Моника 2 раза подряд пытается уйти с выручкой, то ее не пускают на работу (Моника остается без нормальной еды).
# Чтобы снова попасть, она должна отдать сумму, либо уговорить снова дать работать отрабатывать эту сумму
# Но за это она сделает минет бармену, либо поцелует грудь жене. (тогда бармен становится lvl.3, жена также lvl.3)
# Моника может также погасить долг, занявшись сексом с барменом (пока жена не видит), либо полизав жене попу или киску (прогресс), условие с женой, либо мужем lvl.3, т.е. уже должна сделать минет, либо целовать грудь
# Постепенно, по мере прогресса долгов, клиенты начнут делать комментарии о том что им не терпится сегодня увидеть эту попку в деле у пилона.
# Также, со временем, Моника ходит официанткой с shiny затычкой в заднице, говоря что скоро будет танцевать и вы ее увидите (все просят показать?)


label ep23_dialogues1_1:
    # Моника увидела вход в бар autorun
    mt "А это что?"
    "Какой-то Бар?"
    "Раньше я не замечала его."
    return

label ep23_dialogues1_1a:
    # Моника нажала на вход в бар
    mt "А это что?"
    "Какой-то Бар?"
    "Раньше я не замечала его."
    "..."
    "Черт! Ну еще бы я замечала какие-то жуткие бары в трущобах!"
    "Моника, кажется ты начинаешь привыкать к этому месту, да?"
    "Замечать какие-то бары..."
    "Интересно, что ты станешь замечать еще позже?"
    "Мне надо скорее кончать со всем этим!"
    "Но, все-же... Может заглянуть туда?"
    menu:
        "Зайти в бар.":
            if cloth == "Kebab":
                mt "Я не могу зайти туда одетой в рекламу кебеба..."
                mt "Я просто застряну в проходе!"
                return False
            $ remove_hook()
            return True
        "Уйти.":
            return False
    return

label ep23_dialogues1_2:
    # Моника первый раз зашла в бар
    mt "О БОЖЕ!"
    "ЧТО ЭТО ЗА ДЫРА?!?"
    img 9662
    with fade
    "???"
    "SHINY HOLE?!?"
    "ЭТО МЕСТО ТАК И НАЗЫВАЕТСЯ!"

    "Пожалуй, мне лучше уйти отсюда!"
    return

label ep23_dialogues1_2a:
    #при клике на бармена или барменшу
    music2 stop
    music Groove2_85
    img 9585
    with fade
    ashley "Эй! Джо!"
    "К тебе пришла очередная шлюха!"
    "Сколько раз я тебе говорила не звать сюда работать шлюх!"
    img 9586
    mt "???"
    "Я... Я не собираюсь работать здесь!"
    img 9584
    ashley "Да как же не собираешься!"
    "Это Джо подговорил тебя, чтобы ты так сказала мне?!"
    "Он вечно таскает сюда шлюх, а потом оправдывается передо мной!"
    img 9587
    with fadelong
    joe "Эшли! Что ты кричишь здесь?!"
    sound Jump2
    img 9588
    joe "О! Какая детка!"
    music Pyro_Flow
    img 9589
    with fade
    m "Я тебе не детка!"
    img 9590
    ashley "Джо, посмотри! Это не детка!"
    "Это шлюха!!!"
    mt "!!!"
    img 9591
    with fade
    m "Хватит называть меня шлюхой!"
    "Я не заслуживаю такого обращения!"
    "Я зашла сюда, потому что увидела вывеску!"
    "Я клиент!!!"
    music Groove2_85
    img 9592
    with fade
    ashley "Ты?? Клиент?!"
    img 9593
    with Dissolve(0.5)
    "Джо! Мало того что ты устроил здесь стриптиз!"
    "Хорошо, я терплю это, потому что это приносит деньги."
    img 9594
    with fade
    "Но ты решил маскировать шлюх под клиентов?!"
    "Ты хочешь чтобы эта шлюха сидела здесь под видом посетителя и строила глазки всем вокруг?!"
    "А потом уводила их с собой до того как они заплатили?!"
    "Я не потерплю этого, Джо!"

label ep23_dialogues1_2b:
    joe "Эшли! Я первый раз ее вижу!"
    joe "Если она и шлюха, то я ее точно не знаю."
    "Она не из нашего района."
    img 9595
    with fade
    ashley "О, Да! Джо! Ты-то знаешь всех шлюх в этом районе!"
    joe "Я не это имел ввиду, Эшли..."
    img 9596
    with fade
    menu:
        "Слушать их болтовню.":
            jump ep23_dialogues1_2b
        "Уйти.":
            pass
    music Pyro_Flow
    img 9597
    with fade
    m "Знаете что!"
    "Вы позволяете себе обсуждать человека, при его присутствии, в третьем лице!"
    "Я не знаю кто Вас воспитывал Вашим манерам..."
    "Но я не собираюсь дальше это слушать!"
    "До свидания!"

    #fade
    music Groove2_85
    img 9598
    with fadelong
    joe "Послушайте, я не знаю как к Вам обращаться?"
    "Как Вас зовут?"
    img 9599
    m "Меня зовут Мо..."
    music Hidden_Agenda
    mt "Черт! Лучше не называть свое настоящее имя здесь..."
    m "Меня зовут..."
    img 9600
    with fade
    $ monica_pub_name = t__("Мэрилин")
    if renpy.android == True:
        call screen input_softkeyboard
        $ monica_pub_name = _return
    else:
        $ monica_pub_name = renpy.input(t__("Меня зовут... (enter для ввода)"), monica_pub_name)
    with fadelong
    if monica_pub_name == False:
        $ monica_pub_name = t__("Мэрилин")
    m "Меня зовут... [monica_pub_name]..."
    $ pubLocationInitializedForced = True
    img 9601
    with fade
    joe "[monica_pub_name], слушай..."
    "Не обращай внимания на Эшли."
    "Просто ты действительно так одета, что она подумала..."
    img 9602
    m "Я все знаю..."
    "Можно не комментировать."
    "Но я не шлюха!"
    img 9603
    joe "Конечно нет! Я не имел это ввиду!"
    "Ты просто любишь носить такую одежду..."
    music Power_Bots_Loop
    img 9604
    with fade
    m "!!!"
    music Groove2_85
    img 9605
    with Dissolve(0.5)
    m "Я... не очень люблю носить такую одежду..."
    "И хватит комментариев об этом!"
    img 9606
    with fade
    joe "Да, [monica_pub_name], конечно."
    "Слушай, ты неплохо выглядишь!"
    "Ты бы могла работать у нас."
    "Здесь у нас гибкий график, перспективы карьерного роста и..."
    music Pyro_Flow
    img 9607
    with fade
    m "Хватит меня дурить!"
    "Ты хочешь чтобы я виляла задницей у того пилона!?"
    img 9608
    joe "..."
    img 9609
    with Dissolve(0.5)
    mt "Еще бы! Моника Бакфетт! С обложки Модного Журнала!"
    "Самая красивая девушка в городе!"
    "Конечно он хотел бы чтобы такая как я работала здесь, виляя задницей!"
    "Но этого не будет никогда!"
    "Я никогда не опущусь до того, чтобы делать это... У всех на виду..."
    music Groove2_85
    img 9610
    with fade
    joe "Ну почему-же сразу у пилона..."
    "У нас есть работа посудомойкой или официанткой."
    "Хорошие чаевые и бесплатная еда для персонала."
    music Hidden_Agenda
    img 9611
    with Dissolve(0.5)
    m "Бесплатная еда?"
    img 9612
    joe "Да! И очень вкусная!"
    "Для персонала у нас те же блюда, что и для гостей!"
    music Pyro_Flow
    img 9613
    with fade
    m "Я сомневаюсь в том что меня это заинтересует!"
    img 9614
    joe "Приходи, если надумаешь!"

    return

label ep23_dialogues1_2c:
    # autorun на улице
    mt "Черт!"
    "Горячая и вкусная еда..."
    "..."
    "И для этого не надо разносить флаеры в рекламе кебаба или делать что еще похуже..."
    "Может быть..."
    "Пока я не решила то небольшое недоразумение, которое со мной произошло..."
    "Мне попробовать поработать здесь?"
    "..."
    "РАБОТАТЬ В ТАКОЙ ДЫРЕ???"
    "МНЕ???"
    "МОНИКЕ БАКФЕТТ?!?"
    "..."
    "(хмык)"
    "Но что мне делать? Мне же надо где-то есть!"
    "Притом, меня в этом районе никто не узнает."
    "Да и там я назвалась другим именем... [monica_pub_name]..."

#Marilyn

    return


label ep23_dialogues1_3:
    # Моника снова приходит в бар, устраиваться на работу
    # Клик на бармена
    if act=="l":
        mt "Как зовут этого бармена?"
        "Кажется, Джо?"
        return False
    music2 stop
    music Groove2_85
    img 9616
    with fade
    joe "О! [monica_pub_name]! Привет!"
    "Ты надумала работать у нас?"
    music Hidden_Agenda
    menu:
        "Да, я хочу устроиться на работу.":
            pass
        "Уйти.":
            return False
    m "Да, я хочу устроиться на работу."
    joe "Отлично!"
    music Groove2_85
    img 9617
    with fade
    "Эшли! Иди сюда! Она пришла!"
    # fade
    img 9618
    with fadelong
    ashley "А! Это ты?!"
    "Джо уговорил меня взять тебя."
    "У тебя действительно хорошая задница и ты принесешь много денег, если будет танцевать у нас."
    music Pyro_Flow
    img 9619
    m "ЧТО?! Я НЕ СОБИРАЮСЬ ТАНЦЕВАТЬ ЗДЕСЬ!!!"
    music Groove2_85
    img 9620
    with fade
    ashley "А зачем же ты пришла тогда?"
    m "Джо сказал что у Вас есть нормальная работа здесь."
    "Я могу работать официанткой."
    img 9621
    with Dissolve(0.5)
    ashley "Джо! Мало того что ты набрал шлюх для танцев!"
    "Ты еще решил лишить меня работы?!"
    "Может быть ты меня тоже хочешь заменить на какую-нибудь шлюху, А?!"
    joe "Эшли! Она не хочет танцевать, пока..."
    "Это значит что она не шлюха."
    "Она хорошая девушка, Эшли!"
    "И она может помочь тебе."
    "В конце концов, я думаю она будет не против если ты будешь мало платить ей."
    joe "Она обрадовалась даже тому что здесь есть бесплатная горячая еда для персонала!"
    music Hidden_Agenda
    img 9622
    with fade
    m "!!!"
    mt "Я?! Обрадовалась?!"
    "Неужели это было написано у меня на лице?!"
    "О БОЖЕ!!!"
    music Groove2_85
    img 9623
    with fade
    ashley "Это правда? Тебя устроит если тебе будут платить очень мало?"
    img 9624
    with Dissolve(0.5)
    m "..."
    m "По правде говоря... Я бы хотела заработать здесь..."
    img 9625
    ashley "Ладно, мы посмотрим как ты будешь работать."
    "Если с тобой не будет проблем, то мы поговорим о повышении."
    "Давай сюда свои документы, я оформлю тебя на испытательный срок..."
    m "..."
    m "Я... Эммм..."
    "У меня нет документов сейчас."
    music Power_Bots_Loop
    img 9626
    with fade
    ashley "ЧТО?!?!"
    m "Но они будут позже! Я обещаю!"
    ashley "Вот позже и приходи!"
    "Я не позволю работать с клиентами нелегалу!"
    "Любая проверка нас оштрафует!"
    "У нашего заведения и так плохая репутация! Я не хочу ее портить еще сильнее!"
    img 9627
    with fade
    menu:
        "Пожалуйста! Дайте хоть какую-то работу!":
            pass
        "Уйти.":
            return False

    img 9628
    with fade
    m "Пожалуйста! Дайте хоть какую-то работу!"
    "Я слышала у Вас есть вакансия посудомойки!"
    ashley "Я не собираюсь платить нелегальному работнику!"
    menu:
        "Я буду работать за еду...":
            pass
        "Уйти.":
            return False
    music Hidden_Agenda
    img 9629
    with fade
    m "Я буду работать за еду..."
    m "Я слышала что у Вас есть бесплатная еда для персонала..."
    "Если Вы не будете мне платить, то Вы ничем не рискуете..."
    music Power_Bots_Loop
    img 9630
    with Dissolve(0.5)
    ashley "Бесплатно? Почему ты на это согласна?!"
    "Может быть ты какая-то заразная! Или грязная!"
    "Если нет документов, значит нет медицинских справок!"
    "Я не пущу тебя мыть посуду за нашими клиентами!"
    "И вообще, ты умеешь мыть посуду?!"
    "По твоему виду этого не скажешь!"
    img 9631
    mt "АААААААА!!!"
    "ДА Я ЧИЩЕ ЧЕМ ВЫ ВСЕ ВМЕСТЕ ВЗЯТЫЕ ЗДЕСЬ!!!"
    "ЖАЛКИЕ НИЧТОЖЕСТВА!!!"
    music Hidden_Agenda
    img 9632
    with fade
    mt "..."
    m "Эшли, я умею мыть посуду..."
    "Я долгое время работала гувернанткой в богатых домах..."
    "Сейчас у меня небольшие проблемы с миграционными бумагами..."
    "Поэтому я и не могу предоставить документы."
    "Но Вы можете посмотреть на меня и убедиться что я очень чистоплотная."
    "Вы можете рассчитывать на меня..."
    img 9633
    with Dissolve(0.5)
    ashley "..."
    ashley "Хорошо. Можешь приходить и мыть посуду."
    "Я пока не буду брать тебя на постоянную работу."
    "Я хочу к тебе присмотреться."
    "За эту работу ты будешь получать бесплатную еду, которую ест персонал."
    "Это вкусная еда! Я сама готовлю ее!"
    music Groove2_85
    img 9634
    with Dissolve(0.5)
    mt "Не думаю что ты готовишь лучше, чем мне готовила Юлия!"
    "!!!"
    music Hidden_Agenda
    img 9635
    with fade
    m "Да, Эшли. Спасибо Вам за доверие!"
    img 9636
    with fadelong
    joe "Добро пожаловать, [monica_pub_name]!"
    return


# Если Моника кликнула на жену, то та тоже лапает Монику за зад (на что Моника очень удивляется, а жена в ответ сварливо ворчит чтобы та лучше мыла посуду, везде грязь! Моника думает о своем положении)
# Жена на самом деле любит девочек тоже, поэтому в том числе и согласилась на пилон. При лапании Моника может ругаться, либо терпеть.
# Если Моника терпит, то повышает левел у бармена, либо у жены. Если у жены lvl2, то она начинает говорить что такой красивый белый зад никогда не лапала (и улыбается, Моника понимает что та любит девочек).
# Моника комментирует что это реально сверкающая дыра с извращенцами


label ep23_dialogues1_4:
    # Моника работает

    # Если уже ела
    mt "Я сегодня уже ела..."
    "Я не собираюсь лишний раз быть жалкой посудомойкой!"
    "Я - Королева, а не посудомойка!"
    #
    return

label ep23_dialogues1_4a:
    # Моника работает
    menu:
        "Танцевать на сцене в Shiny Hole." if monicaDancingWillingly == True:
            return 5
        "Работать официанткой в Shiny Hole." if pubMonicaWorkingWaitress == True:
            return 4
        "Спросить о повышении." if monicaPubWashingDishesCount>0 and pubMonicaWorkingWaitress == False:
            return 3
        "Мыть посуду.":
            return 1
        "Заказать еду.":
            return 2
        "Меня зовут...": # сменить имя
            return 6
        "Уйти.":
            return False

label ep23_dialogues1_4a2:
    # Моника моет посуду
    music2 stop

    music stop
    sound snd_washing_dishes
    $ monicaWashingDishesImages = [9637, 9638, 9639]
    call showRandomImagesFirstFade(monicaWashingDishesImages, 1) from _call_showRandomImagesFirstFade
    $ monicaWashingDishesImages2 = [9640, 9641, 9642]
    call showRandomImagesFirstFade(monicaWashingDishesImages2, 1) from _call_showRandomImagesFirstFade_1
    $ rand1 = rand(1,4)
    if rand1 == 1:
        mt "Никогда бы не подумала что буду мыть посуду в подобной дыре..."
    if rand1 == 2:
        mt "Не могу поверить что я делаю это..."
    if rand1 == 3:
        mt "У меня ощущение что все это сон..."
    if rand1 == 4:
        mt "Мне надо определенно что-то менять в этой ситуации... И как можно быстрее!"

    $ monicaPubWashingDishesCount += 1
    return

label ep23_dialogues1_4b: # Бармен

    # Клик на бармена
    # Бармен лапает Монику
    music Hidden_Agenda
    img 9643
    with fade
    w
    img 9644
    with Dissolve(0.3)
    w
    sound Jump2
    img 9645
    with Dissolve(0.3)
    w
    mt "Черт! Кажется, этот извращенец Джо пытается меня незаметно лапать!"
    $ menu_corruption = [monicaWashHoldJoeCorruption]
    menu:
        "Не обращать внимание...":
            sound snd_washing_dishes
            music Loved_Up
            img 9646
            with Dissolve(0.3)
            w
            img 9647
            with Dissolve(0.3)
            w
            img 9648
            with Dissolve(0.3)
            w
            if char_info["Bartender"]["level"] == 1:
                $ add_char_progress("Bartender", monicaWashMolestJoeProgress, "PS1_JoeProgressMolest_day" + str(day))
            music Groove2_85
            $ questLog(48, True)

#        "Не обращать внимание... (low corruption, required [monicaWashHoldJoeCorruption]) (disabled)" if corruption < monicaWashHoldJoeCorruption:
#            pass
        "Прекратить это!":
            music Power_Bots_Loop
            img 9649
            with fade
            m "Джо! Ты что-то хотел взять здесь?"
            joe "Да, [monica_pub_name]!"
            "Я хочу взять чистую пивную кружку!"

    img 9650
    with fadelong
    mt "Это место - действительно Shiny Hole с извращенцами!"
    return

label ep23_dialogues1_4c: # Барменша
    # Клик на барменшу
    # Барменша лапает Монику
    music Hidden_Agenda
    img 9651
    with fade
    w
    img 9652
    with Dissolve(0.3)
    w
    img 9653
    with Dissolve(0.3)
    w
    sound Jump2
    img 9654
    with Dissolve(0.3)
    w

    mt "Черт! Эшли меня трогает за зад?!"
    $ menu_corruption = [monicaWashHoldAshleyCorruption]
    menu:
        "Не обращать внимание...":
            sound snd_washing_dishes
            music Loved_Up
            img 9655
            with Dissolve(0.3)
            w
            img 9656
            with Dissolve(0.3)
            w
            img 9657
            with Dissolve(0.3)
            w

            if char_info["Bartender_Waitress"]["level"] == 1:
                $ add_char_progress("Bartender_Waitress", monicaWashMolestAshleyProgress, "PS1_AshleyProgressMolest_day" + str(day))
            music Groove2_85
            $ questLog(49, True)

#        "Не обращать внимание... (low corruption, required [monicaWashHoldAshleyCorruption]) (disabled)" if corruption < monicaWashHoldAshleyCorruption:
#            pass
        "Прекратить это!":
            music Power_Bots_Loop
            img 9658
            with fade
            m "Эшли! Ты что-то хотела взять здесь?"
            ashley "Я слежу чтобы ты лучше мыла посуду!"
            "Везде грязь!"

    img 9650
    with fadelong
    mt "О БОЖЕ!!!"
    "ЗА ЧТО МНЕ ЭТО?!"
    mt "Это место - действительно Shiny Hole с извращенцами!"
    return

label ep23_dialogues1_5:
    # Моника помыла посуду
    music Groove2_85
    mt "Все! Хватит! Я не собираюсь дальше портить руки моющими средствами!"
    img 9659
    with fade
    m "Эшли, я помыла посуду... Где моя еда?"
    ashley "Я видела, ты помыла не все и не очень хорошо."
    "Но, так уж и быть, иди поешь..."
    if char_info["Bartender_Waitress"]["level"] >= 2:
    # если lvl2, то уходящую Монику лапает за попу
        sound Jump2
        img 9660
        with Dissolve(0.5)
        w

    # fade
    img 9661
    with fade
    mt "По крайней мере это действительно вкусная еда... По сравнению с кебабом..."
    mt "И я честно заработала ее..."
    sound snd_gulp
    img black_screen
    with fade
    return



label ep23_dialogues1_6:
    if monicaEatedLastDay == day:
        mt "Я уже ела сегодня."
        mt "Ни к чему тратить деньги..."
        return False
    music2 stop
    music Groove2_85
    img 20462
    with fadelong
    ashley "Привет, [monica_pub_name]!"
    img 20461
    with diss
    ashley "Ты пришла, чтобы мыть посуду?"
    img 20463
    with diss
    m "Нет, я хочу заказать еду!"
    img 20464
    with fade
    ashley "Правда?"
    ashley "И что же ты хочешь заказать?"
    img 20465
    with diss
    m "Я хочу заказать..."
    $ menu_price = [pubShinyBurger, pubSphagettiPrice, pubSoupPrice]
    $ menu_price2 = [pubShinyBurger, pubSphagettiPrice, pubSoupPrice]
    $ choose_var = 0
    menu:
        "Shiny Бургер.":
            $ choose_var = 1
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Shiny Бургер."
            $ images_list = [20473, 20478, 20483]
        "Спагетти.":
            $ choose_var = 2
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Спагетти."
            $ images_list = [20474, 20479, 20482]
        "Суп харчо.":
            $ choose_var = 3
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Суп харчо."
            $ images_list = [20475, 20477, 20484]
        "Уйти.":
            img 20470
            with fade
            m "Я передумала."
            img 20471
            with diss
            ashley "Ах, [monica_pub_name], у тебя нет денег!"
            ashley "Но ведь ты посудомойка. Ты всегда можешь помыть посуду!"
            img 20472
            with diss
            mt "!!!"

            # на улице
            $ autorun_to_object("ep23_dialogues1_6a", scene="hostel_street")
            return False
    img 20467
    with diss
    joe "А выпивку?"
    img 20468
    m "Спасибо, не надо!"
    img 20469
    with fade
    ashley "Хорошо, присаживайся за стол."
    ashley "Я сейчас принесу."
    $ add_money(-menu_price2[choose_var-1])

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_plates2
    $ pubFoodHistory.append(choose_var)
    music Groove2_85
    img images_list[0]
    with fadelong
    #Shiny Бургер.
#    img 20473
    #Спагетти.
#    img 20474
    #Суп харчо.
#    img 20475
    ashley "Но ты могла бы не тратить деньги."
    ashley "Эту еду легко заработать посудомойкой."

    img 20476
    with diss
    mt "!!!"

    if monicaPubWashingDishesCount > 5:
        $ notif(t_("Моника часто мыла посуду."))
        # если часто мыла
        img images_list[1]
        #Shiny Бургер.
#        img 20478
        #Спагетти.
#        img 20479
        #Суп харчо.
#        img 20477
        with fade
        ashley "К тому же, я уже привыкла что ты моешь посуду."
        ashley "Мне стало как-то лень заниматься этим."
        img 20480
        with diss
        m "Спасибо, Эшли."
        m "Сегодня я не хочу... мыть посуду..."

        img 20481
        with diss
        ashley "Хорошо, [monica_pub_name], если надумаешь, приходи..."
        #


    img images_list[2]
    with fade
    #Shiny Бургер.
#    img 20483
    #Спагетти.
#    img 20482
    #Суп харчо.
#    img 20484
    #
    mt "Эшли готовит отвратительно."
    mt "Это место - действительно дыра."
    music stop
    sound snd_gulp
    img black_screen
    with diss
    mt "Но это нормальная еда, а не пирожные с заправки..."
    $ autorun_to_object("ep23_dialogues1_6b", scene="hostel_street")
    return True

label ep23_dialogues1_6a:
    # Говорит на улице
    mt "Ненавижу!"
    mt "Я не посудомойка! Я - Моника Бакфетт, королева!"
    return

label ep23_dialogues1_6b:
    mt "Хотя пирожные, пожалуй, повкуснее, чем помои в этой блестящей дыре!"
    return

label ep23_dialogues1_7: # Смена имени

    m "Меня зовут..."
    if renpy.android == True:
        call screen input_softkeyboard
        $ monica_pub_name = _return
    else:
        $ monica_pub_name = renpy.input(t__("Меня зовут... (enter для ввода)"), monica_pub_name)
    m "Меня зовут... [monica_pub_name]..."
    return

    #
