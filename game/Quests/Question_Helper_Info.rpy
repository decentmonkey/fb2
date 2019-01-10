default questLogDataEnabled = {}

label question_helper_hairdye:
    menu:
        "Посмотреть подсказку":
            img help1_1
            with fadelong
            help "Подойти к зеркалам и взять краску для волос."
            img help1_2
            with fade
            help "Разлить краску на ковер."
        "Продолжить игру.":
            pass

    call refresh_scene_fade() from _call_refresh_scene_fade_30
#    help "Help!"
    return

label question_helper_hairdye_find_julia:
    menu:
        "Посмотреть подсказку":
            help "Юлия в подвале. Вход в подвал у лестницы на нижнем этаже."
        "Продолжить игру.":
            pass

    return


label question_helper_laundry:
    menu:
        "Посмотреть подсказку":
            img help1_3
            with fadelong
            w
            help "Взять платье в нижнем ящике."
            w
            img help1_4
            with fade
            w
            help "Взять утюг из нижней коробки."
            w
            img help1_5
            with fade
            help "Убрать мусор. Затем применить поочереди платье и утюг, чтобы погладить."
        "Продолжить игру.":
            pass
    call refresh_scene_fade() from _call_refresh_scene_fade_31
    return

label question_gas_trader1:
    menu:
        "Посмотреть подсказку":
            img help1_6
            with fadelong
            help "Кассир за дверью."
        "Продолжить игру.":
            pass
    call refresh_scene_fade() from _call_refresh_scene_fade_32
    return

label question_gas_trader2:
    menu:
        "Посмотреть подсказку":
            img help1_7
            with fadelong
            help "Идти сюда."
            img help1_8
            with fade
            help "Затем идти сюда."
            img help1_9
            with fade
            help "Разбить дорогую бутылку вина."
        "Продолжить игру.":
            pass
    call refresh_scene_fade() from _call_refresh_scene_fade_33
    return

label question_cloth_shop_dick_buy_dress:
    menu:
        "Посмотреть подсказку":
            img help1_10
            with fadelong
            help "Проверить места."
            w
            img help1_11
            with fade
            w
            img help1_12
            with fade
            help "После каждого места идти примерять платье в примерочную."
            img help1_13
            with fade
            help "Повесить свое платье на вешалку."
            img help1_14
            help "Нажать сюда чтобы примерить новое платье."
        "Продолжить игру.":
            pass
    call refresh_scene_fade() from _call_refresh_scene_fade_34
    return

label question_hostel_perry_dress:
    img help1_15
    with fadelong
    w
    return

label question_office_tea_lost_phone:
    img help1_16
    with fadelong
    help "Телефон на полу при входе в офис..."
    w
    return

label questLog_init:
    $ questLogData = [
    [0, _("Барди постоянно пытается заглянуть мне под юбку."), True, _("Барди")], #+
    [1, _("Барди в при любом удобном случае заглядывает мне под юбку. И я ничего не могу с этим поделать..."), True, _("Барди")],
    [2, _("Барди хочет чтобы я одевала трусики Бетти, которые она носила в прошлый раз. Интересно, как я узнаю какие именно трусики она носит сегодня?"), True, _("Барди")],
    [3, _("Бетти ждет от меня, что я буду регулярно убираться в доме."), True, _("Бетти")], #+
    [4, _("Бетти ждет от меня, что я буду регулярно убираться в доме и тереть это проклятое пятно."), True, _("Бетти")],
    [5, _("Бетти хочет чтобы я носила ее сумку с вещами, пока она занимается фитнесом. Фитнес у Бетти по вторникам и четвергам."), True, _("Бетти")],
    [6, _("Мне надо проверить что происходит в моем офисе."), True, _("Офис")], #+
    [7, _("Биф хочет чтобы я ходила к нему на кастинги. Если я хочу убедить его взять меня в офис, мне надо завоевать его доверие. Но смогу-ли я на это пойти?"), True, _("Офис")],
    [8, _("Похоже я нашла возможность зарабатывать деньги, делая фотосессии у Бифа. Но эти фотосессии все более развратные. Долго-ли я смогу себе это позволять?"), True, _("Офис")],
    [9, _("Я отказалась от того что хочет Биф. Но найду-ли я другой способ достать деньги? Возможно, мне придется, все-таки, передумать?"), True, _("Офис")],
    [10, _("Мне надо как-то найти $ 5000 до пятницы. Где мне их взять? Может быть спросить Бифа о работе?"), True, _("Дик")],
    [11, _("Мне надо найти еще $ 1000, иначе конец!"), True, _("Дик")],
    [12, _("Теперь я должна приносить Виктории раз в неделю $ 5000 до пятницы. Я даже не представляла насколько она опасна."), True, _("Дик")],
    [13, _("Так продолжаться не может. Виктория не даст мне нормально жить. Надо как-то воздействовать на Дика. Его единственное слабое место - это женщины. У меня не получается, как я ни пыталась. Может быть попробовать попросить помощи у Мелани?"), True, _("Дик")],
    [14, _("В фитнес-зале я встретила Стефани и Ребекку. Я, кажется, убедила их что все это игра. Но долго-ли они будут в это верить?"), True, _("Fitness Gym")],
    [15, _("В доме для меня еды нет. По крайней мере пока. Мне надо где-то питаться!"), True, _("Жизнь")], #+
    [16, _("В доме для меня еды нет. По крайней мере пока. Мне надо где-то питаться. Есть эта дурацкая разноска флаеров. Но, может быть, проще воровать еду где-нибудь? Но готова-ли я на это пойти? Или, может быть, проще занять у кого-то деньги?"), True, _("Жизнь")],
    [17, _("Я разношу гребаные флаеры за жалкий кебаб. Может быть есть способы заработать на еду проще?"), True, _("Жизнь")],
    [18, _("Мне надо как-то вернуть мою прошлую жизнь. Я не смогу долго прожить в этом кошмаре!"), True, _("Жизнь")],
    [19, _("Любой ценой избегать встречи с Маркусом!"), True, _("Маркус")] #+
    ]

    #еда
    #флаеры, фаллинг
    #по дефолту 2-ая часть: 0, 3, 7, 15, 18, 19,
    #monicaKnowAboutKebabWork. Если знает, то 15-, 16+
    return

label show_questlog:
    $ inText = ""
    python:
        lastCategory = False
        for questLogLine in questLogData:
            if str(questLogLine[0]) in questLogDataEnabled and questLogDataEnabled[str(questLogLine[0])] == True and questLogLine[2] == True:
                if __(questLogLine[3]) != lastCategory:
                    lastCategory = __(questLogLine[3])
                    inText = inText + "{=questlog_text_category_style}{u}" + lastCategory + "{/u}{/=questlog_text_category_style}\n{vspace=5}"
                inText = inText + __(questLogLine[1]) + "\n\n"
    sound open_map
    call screen questlog_screen(inText)
    sound open_map
    return
