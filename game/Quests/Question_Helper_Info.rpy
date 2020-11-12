default questLogDataEnabled = {}
default questLogLinesUpdated = []

#call question_helper_enable("question_helper_hairdye_find_julia")
#call question_helper_disable()
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

label question_clothing_shop_sell_dress:
    img help1_17
    with fadelong
    help "Подходить к клиентам и пытаться продать платье."
    help "Этот клиент, в итоге, должен купить его."
    return

label question_steve_ask_ralph:
    img 5806
    with fadelong
    help "Спросить у Ральфа по поводу Стива."
    return

label questLog_init:
    $ questLogData = [
    [55, t_("Барди совсем обнаглел и заставляет меня быть мамой для своего одноклассника. Такого же неудачника как он сам!"), True, t_("Барди")],
    [0, t_("Барди постоянно пытается заглянуть мне под юбку."), True, t_("Барди")], #+
    [44,t_("Барди шантажирует Бетти. Может быть я могу использовать это?"), True, t_("Барди")],
    [45, t_("Я могу питаться в доме. Если буду соблюдать условие..."), True, t_("Барди")],
    [1, t_("Барди в при любом удобном случае заглядывает мне под юбку. И я ничего не могу с этим поделать..."), True, t_("Барди")],
    [2, t_("Барди хочет чтобы я одевала трусики Бетти, которые она носила в прошлый раз. Интересно, как я узнаю какие именно трусики она носит сегодня?"), True, t_("Барди")],
    [20, t_("Барди хочет чтобы я одевала трусики Бетти, которые она носила в прошлый раз. Бетти валяется в них своей толстой задницей на моей кровати по вечерам."), True, t_("Барди")],
    [34, t_("Барди снова требует от меня каких-то извращений! Похоже, удалось переключить его на Бетти. Давно стоит проучить ее за то как она обращается со мной! Итак, надо сообщать Барди когда мы собираемся идти на фитнесс..."), True, t_("Барди")],
    [35, t_("Барди удалось найти компромат на Бетти. Надеюсь теперь он оставит меня в покое!"), True, t_("Барди")],
    [36, t_("Барди хочет чтобы я одевала трусики Бетти, которые она носила в прошлый раз. Бетти обязана показать мне их, если я спрошу."), True, t_("Барди")],
    [38, t_("Я теперь должна ходить без трусиков в доме. Иначе Барди накажет меня. Мерзавец!"), True, t_("Барди")],
    [72, t_("Барди хочет, чтобы я соблазнила Ральфа и сделала для него материалы... Но, может быть, это мой шанс вернуть назад свой дом?"), True, t_("Барди")],
    [3, t_("Бетти ждет от меня, что я буду регулярно убираться в доме."), True, t_("Бетти")], #+
    [4, t_("Бетти ждет от меня, что я буду регулярно убираться в доме и тереть это проклятое пятно."), True, t_("Бетти")],
    [5, t_("Бетти хочет чтобы я носила ее сумку с вещами, пока она занимается фитнесом. Фитнес у Бетти по вторникам и четвергам."), True, t_("Бетти")],
    [23, t_("Кажется, Бетти не так строго следит за тем, чтобы я убиралась все время."), True, t_("Бетти")],
    [37, t_("Бетти знает что я ношу ее трусики. Более того, она должна показать трусики, которые носит сегодня, если я спрошу ее об этом."), True, t_("Бетти")],
    [39, t_("Бетти теперь должна ходить без трусиков в доме. Она сказала что я могу проверять это. Это все проделки Барди!"), True, t_("Бетти")],
    [6, t_("Мне надо проверить что происходит в моем офисе."), True, t_("Офис")], #+
    [43, t_("Теперь я могу работать в офисе. Денег это не добавило, но я могу чувствовать себя Боссом снова..."), True, t_("Офис")],
    [46, t_("Биф требует, чтобы я собирала отчеты у своих сотрудников и приносила ему. За кого он меня держит?!"), True, t_("Офис")],
    [7, t_("Биф хочет чтобы я ходила к нему на кастинги. Если я хочу убедить его взять меня в офис, мне надо завоевать его доверие. Но смогу-ли я на это пойти?"), True, t_("Офис")],
    [8, t_("Похоже я нашла возможность зарабатывать деньги, делая фотосессии у Бифа. Но эти фотосессии все более развратные. Долго-ли я смогу себе это позволять?"), True, t_("Офис")],
    [9, t_("Я отказалась от того что хочет Биф. Но найду-ли я другой способ достать деньги? Возможно, мне придется, все-таки, передумать?"), True, t_("Офис")],
    [67, t_("Биф требует, чтобы я убедила этих глупых инвесторов инвестировать деньги в мой журнал. Как он предполагает я смогу это сделать?"), True, t_("Офис")],
    [68, t_("Я не собираюсь быть позорищем для всего мира! Я верну себе мою компанию, но не таким путем!"), True, t_("Офис")],

    [64, t_("Мне нужно каждый день целовать Юлию и говорить ей комплименты."), True, t_("Офис")],
    [63, t_("Я решила подыграть этой никчемной Юлии. Отличный способ узнать цвет ее трусиков."), True, t_("Офис")],
    [47, t_("Фред просит говорить Юлии какие-то непонятные слова и делать странные вещи. Не понимаю зачем это, но мне придется выполнять его просьбы, потому что он шантажирует меня. Но, возможно, я могу потянуть время..."), True, t_("Офис")],
    [73, t_("У меня появилась возможность сбежать из страны. Для этого мне всего лишь нужно притворяться влюбленной дурочкой перед никчемной Юлией."), True, t_("Офис")],
    [74, t_("Теперь я могу жить у этой дурацкой гувернантки. И мне не нужно платить за жилье и еду. Но на что мне придется идти взамен?"), True, t_("Офис")],

    [10, t_("Мне надо как-то найти $ 5000 до пятницы. Где мне их взять? Может быть спросить Бифа о работе?"), True, t_("Дик")],
    [11, t_("Мне надо найти еще $ 1000, иначе конец!"), True, t_("Дик")],
    [21, t_("Теперь Дик имеет свой галстук! Мой кошмар закончился. Надо проведать его."), True, t_("Дик")],
    [12, t_("Теперь я должна приносить Виктории раз в неделю $ 5000 до пятницы. Я даже не представляла насколько она опасна."), True, t_("Дик")],
    [13, t_("Так продолжаться не может. Виктория не даст мне нормально жить. Надо как-то воздействовать на Дика. Его единственное слабое место - это женщины. У меня не получается, как я ни пыталась. Может быть попробовать попросить помощи у Мелани?"), True, t_("Дик")],
    [24, t_("Мелани обещала узнать всю правду про Дика. За это я согласилась поучаствовать с ней в какой-то фотосессии. Надеюсь я не пожалею об этом..."), True, t_("Дик")],
    [25, t_("Это был жуткий кошмар, но я надеюсь оно того стоило! Ну держись, Виктория! Я нашла кое-кого кто тебе не по зубам!"), True, t_("Дик")],
    [26, t_("У меня появился шанс вернуть прежнюю жизнь! ШАНС!!! Неужели Мелани сможет мне помочь? Но что она захочет попросить взамен?.."), True, t_("Дик")],
    [27, t_("От Мелани нет новостей... Я даже боюсь представить что с ней..."), True, t_("Дик")],
    [28, t_("Я жду новостей от Мелани..."), True, t_("Дик")],
    [29, t_("Мелани решила унизить меня в обмен на свою помощь... Пойду-ли я на то что она предложила мне?"), True, t_("Дик")],
    [14, t_("В фитнес-зале я встретила Стефани и Ребекку. Я, кажется, убедила их что все это игра. Но долго-ли они будут в это верить?"), True, t_("Fitness Gym")],

    [79, t_("Мне удалось соблазнить Ральфа! Если я продолжу встречаться с ним, то смогу вытрясти с него какие-то деньги. А еще лучше было бы занять место Бетти и вернуть себе свой дом!"), True, t_("Жизнь")],
    [80, t_("Подкаблучник Ральф готов платить мне $ 200 за секс с ним по вторникам и четвергам. Жадный старикашка!"), True, t_("Жизнь")],
    [81, t_("Я притворяюсь перед Ральфом что люблю его. Уверена, что я смогу занять место Бетти и вернуть себе свой дом!"), True, t_("Жизнь")],

    [71, t_("У меня теперь есть место, где я могу жить. Апартаменты в трущобах... Но это лучше, чем подвал в доме, где живет семейка идиотов."), True, t_("Жизнь")],
    [62, t_("Мне предложили работу в эскорте! Неужели я решусь на такое?! Хотя... Там можно неплохо заработать."), True, t_("Жизнь")],
    [61, t_("У меня появилась возможность дополнительного заработка по субботам. У Филиппа. Но смогу ли я?"), True, t_("Жизнь")],
    [31, t_("Стив приходил в гости к Ральфу. Мне надо избегать встречи с ним!"), True, t_("Жизнь")],
    [32, t_("Не могу поверить что я согласилась на секс со Стивом! Мне надо проверить перевел-ли он деньги Виктории."), True, t_("Жизнь")],
    [33, t_("Стив обманул меня! Он что, думает что можно иметь со мной секс за бесплатно?!"), True, t_("Жизнь")],
    [40, t_("Мне надо поймать Стива, этого слизняка! Он не уйдет от меня!"), True, t_("Жизнь")],
    [41, t_("Стив хочет трахнуть меня снова, чтобы закрыть эту чертову сделку! Мне нужны деньги, но цена..."), True, t_("Жизнь")],
    [42, t_("Стив слизняк и негодяй! Но, может быть, через него можно найти какую-то работу или просто деньги?"), True, t_("Жизнь")],
    [15, t_("В доме для меня еды нет. По крайней мере пока. Мне надо где-то питаться!"), True, t_("Жизнь")], #+
    [16, t_("В доме для меня еды нет. По крайней мере пока. Мне надо где-то питаться. Есть эта дурацкая разноска флаеров. Но, может быть, проще воровать еду где-нибудь? Но готова-ли я на это пойти? Или, может быть, проще занять у кого-то деньги?"), True, t_("Жизнь")],
    [17, t_("Я разношу гребаные флаеры за жалкий кебаб. Может быть есть способы заработать на еду проще?"), True, t_("Жизнь")],

    [22, t_("Вместо разноски флаеров я нашла более быстрый способ заработать. Он немного... неудобный, но ведь это ненадолго..."), True, t_("Жизнь")],
    [83, t_("Старая карга застукала меня! Она сказала что заниматься проституцией в этом районе нельзя без ее разрешения! Какого черта?! Ложь! Я бы никогда не стала заниматься этим! Но что мне теперь делать? Если я хочу хоть что-то заработать, мне придется найти укромное место, где старая карга не найдет меня..."), True, t_("Жизнь")],
    [82, t_("Теперь мне нужно каждую неделю приносить гребаной Перри деньги в счет оплаты долга. Черт!"), True, t_("Жизнь")],

    [30, t_("Я нашла способ зарабатывать на еду, моя посуду в Баре. Я не в восторге, но ведь это временно?"), True, t_("Жизнь")],
    [18, t_("Мне надо как-то вернуть мою прошлую жизнь. Я не смогу долго прожить в этом кошмаре!"), True, t_("Жизнь")],


    [84, t_("Теперь корона Shiny Hole принадлежит МНЕ! Я буду пользоваться королевскими привилегиями! А эта сучка Молли теперь никто!"), True, t_("Shiny Hole")],
    [69, t_("Я не собираюсь вилять голой попой перед посетителями этой дыры!!!"), True, t_("Shiny Hole")],
    [76, t_("Я пригласила Клэр в свой офис, чтобы она убедилась, что я не какая-то [monica_pub_name]. Она же не сможет отказать в просьбе самой Монике Бакфетт!"), True, t_("Shiny Hole")],
    [77, t_("Мерзавец Биф! Он при Клэр сказал, что я работаю заменой Моники Бакфетт! Теперь единственный адекватный человек будет считать меня лгуньей!"), True, t_("Shiny Hole")],
    [78, t_("Клэр ко мне хорошо относится и готова мне помочь при необходимости. Она говорит, что ей без разницы, настоящая ли я Моника Бакфетт или нет."), True, t_("Shiny Hole")],

    [66, t_("Из-за это рыжей сучки я теперь должна отдавать все свои чаевые Эшли! Ненавижу ее!!!"), True, t_("Shiny Hole")],
    [52, t_("Я устроилась работать официанткой в Shiny Hole. У меня нет зарплаты и почти все чаевые надо отдавать хозяевам, но это шанс заработать хоть какие-то деньги. Я не могу выносить этих жутких клиентов, но у меня нет выбора. Тем более, это ненадолго..."), True, t_("Shiny Hole")],
    [48, t_("Кажется, Джо пытается меня лапать, когда я мою посуду... Ненавижу эту работу!"), True, t_("Shiny Hole")],
    [49, t_("Кажется, Эшли пытается меня лапать. Я не понимаю с какой целью. Ведь у нее есть муж!"), True, t_("Shiny Hole")],
    [50, t_("Мне удалось договориться с Джо, чтобы снова работать официанткой. Для этого мне пришлось позволить ему лапать меня, пока его жена не видит. Моника, ты уверена что это правильный путь?"), True, t_("Shiny Hole")],
    [51, t_("Я танцевала голой перед Джо, пока он дрочил на меня. А потом пряталась за диваном от его жены! Моника, ты точно помнишь кто ты?! Ты не [monica_pub_name]! Одумайся!"), True, t_("Shiny Hole")],
    [53, t_("Мне удалось договориться с Эшли, чтобы снова работать официанткой. Эта грязная Эшли - гребаная лесбиянка! Неужели я способна на такое?!"), True, t_("Shiny Hole")],
    [57, t_("Мне нужно отработать долг $500, выступая на сцене в пабе."), True, t_("Shiny Hole")],
    [60, t_("Эшли простила мне долг. Теперь я могу зарабатывать, выступая на сцене в пабе Shiny Hole. Неужели для меня это теперь нормально?"), True, t_("Shiny Hole")],
    [75, t_("Я полностью разделать на сцене перед толпой пьяных посетителей. Мне не верится, что это случилось наяву, а не в кошмарном сне! Но, с другой стороны, я делала это в маске и меня никто не знает здесь..."), True, t_("Shiny Hole")],
    [58, t_("Эта рыжая стриптизерша слишком многое себе позволяет. Как она смеет так общаться со мной?!"), True, t_("Shiny Hole")],
    [70, t_("Эшли хочет чтобы я помирилась с этой сучкой Молли. Не представляю как это возможно!"), True, t_("Shiny Hole")],
    [59, t_("Похоже, Клэр единственная в этой дыре, с кем можно нормально общаться."), True, t_("Shiny Hole")],
    [19, t_("Любой ценой избегать встречи с Маркусом!"), True, t_("Маркус")], #+
    [54, t_("Мелани советует мне самой придти к Маркусу. Якобы это может помочь... Готова-ли Я на это пойти и что меня ждет?"), True, t_("Маркус")],
    [56, t_("Маркус ждет меня снова... Смогу-ли я решиться снова навестить его?"), True, t_("Маркус")],

    [65, t_("Фред обычно во дворе у машины..."), True, t_("Жизнь")]
    ]

    #еда
    #флаеры, фаллинг
    #по дефолту 2-ая часть: 0, 3, 7, 15, 18, 19,
    #monicaKnowAboutKebabWork. Если знает, то 15-, 16+
    return

label questHelp_init:
    # вначале игры
    # house1, house2, fitness1

    $ questHelpDataQuests = {
        # ДОМ
        "house1" : [t_("ДОМ"), t_("Хорошая гувернантка"), t_("Убираться в доме для роста уровня отношений с Бетти. Уровень начинает расти после 3-х уборок подряд.")],



        "house2" : [t_("ДОМ"), t_("Хорошая гувернантка"), t_("Убираться в доме для роста уровня у Бетти. Уровень начинает расти после 3-х уборок подряд.")],
        "house3" : [t_("ДОМ"), t_("Хорошая гувернантка"), t_("Убираться в доме для роста уровня у Бетти. Уровень начинает расти после 3-х уборок подряд.")],




        # ДОМ
        "house1" : [t_("ДОМ"), t_("Хорошая гувернантка"), t_("Убираться в доме для роста уровня у Бетти. Уровень начинает расти после 3-х уборок подряд.")],
        "house2" : [t_("ДОМ"), t_("Барди постоянно пытается заглянуть мне под юбку.")],

        # ФИТНЕСС
        "fitness1" : [t_("ФИТНЕСС"), t_("Бетти подумывает взять Монику на фитнесс"), t_("Убираться в доме, пока уровень Бетти не достигнет 3.")]
    }

    $ questHelpDataCategoriesDescriptions = [
        ["house_desc1", t_("ДОМ"), t_("Барди постоянно пытается заглянуть мне под юбку.")]
    ]
    return

label show_questlog:
    $ questLogJustUpdated = False
    call questLog_init() from __rcall_questLog_inita1
    $ inText = ""
    python:
        lastCategory = False
        for questLogLine in questLogData:
            if str(questLogLine[0]) in questLogDataEnabled and questLogDataEnabled[str(questLogLine[0])] == True and questLogLine[2] == True:
                if t__(questLogLine[3]) != lastCategory:
                    lastCategory = t__(questLogLine[3])
                    inText = inText + "{=questlog_text_category_style}{u}" + t__(lastCategory) + "{/u}{/=questlog_text_category_style}\n{vspace=5}"
                if str(questLogLine[0]) in questLogLinesUpdated:
                    inText = inText + "{b}{color=#002810}" + t__(questLogLine[1]) + "{/color}{/b}\n\n"
                else:
                    inText = inText + t__(questLogLine[1]) + "\n\n"
    sound open_map
    call screen questlog_screen(inText)
    $ questLogLinesUpdated = []
    sound open_map
    return

label show_questhelp:
    $ questHelpJustUpdated = False
    call questHelp_init()

    python:
        questHelpDataLastCategoryMemory = {}
        questHelpDataLastQuestsBold = {}
        questHelpDataCategoriesBold = {}
        for questCategoryName in questHelpData:
            for idx1 in range(0, len(questHelpData[questCategoryName])):
                tempVar1 = questHelpData[questCategoryName][idx1]
                if questHelpDataLastMemory.has_key(tempVar1[0]) == False:
                    questHelpDataLastMemory[tempVar1[0]] = tempVar1[1]
                    questHelpDataLastQuestsBold[tempVar1[0]] = True
                    questHelpDataCategoriesBold[questCategoryName] = True
                else:
                    if questHelpDataLastMemory[tempVar1[0]] != tempVar1[1]:
                        questHelpDataLastQuestsBold[tempVar1[0]] = True
                        questHelpDataCategoriesBold[questCategoryName] = True

                if questHelpDataLastCategoryMemory.has_key(questCategoryName) == False:
                    questHelpDataLastCategoryMemory[questCategoryName] = -100
                if questHelpDataLastCategoryMemory[questCategoryName] == -100:
                    questHelpDataLastCategoryMemory[questCategoryName] = tempVar1[1]
                else:
                    if questHelpDataLastCategoryMemory[questCategoryName] == -1:
                        questHelpDataLastCategoryMemory[questCategoryName] = tempVar1[1]
                    else:
                        if questHelpDataLastCategoryMemory[questCategoryName] == 1:
                            questHelpDataLastCategoryMemory[questCategoryName] = tempVar1[1]
                        else:
                            if questHelpDataLastCategoryMemory[questCategoryName] == -100:
                                questHelpDataLastCategoryMemory[questCategoryName] = tempVar1[1]

    sound keyboard_click
label show_questhelp_loop:
    call screen questhelp_screen()
    if _return != False:
        if _return[0] == "category_click":
            if questHelpCurrentCategory != _return[1]:
                $ questHelpCurrentQuest = False
            $ questHelpCurrentCategory = _return[1]
            sound keyboard
            jump show_questhelp_loop

        if _return[0] == "quest_click":
            $ questHelpCurrentQuest = _return[1]
            sound keyboard
            jump show_questhelp_loop


    sound snd_ui_not_working

    python:
        for questCategoryName in questHelpData:
            for idx1 in range(0, len(questHelpData[questCategoryName])):
                tempVar1 = questHelpData[questCategoryName][idx1]
                questHelpDataLastMemory[tempVar1[0]] = tempVar1[1]

    return


label show_achievements:
    sound open_map
    call screen achievements_screen()
    sound open_map
    return
