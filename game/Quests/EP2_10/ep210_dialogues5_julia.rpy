# Офис. Кабинет Моники.
# Моника заходит в свой кабинет, Юлия сидит за своим столом
# при клике на Юлию вместо обычного меню отношений вызывыется эта сцена
label ep210_dialogues5_julia_1:
    # Юлия встает со стула и, волнуясь, говорит
    img 16456
    julia "Миссис Бакфетт... Я..."
    # Моника раздраженно
    img 16457
    m "Что?!"
    img 16458
    julia "Я хотела сказать Вам, что Ваши сотрудники, Джон и Гретта..."
    julia "Они... Они ворвались в этот кабинет и пытались задрать мое платье!"
    img 16459
    m "И что, им это удалось?"
    img 20880
    julia "Миссис Бакфетт, конечно я не позволила им сделать это!"
    img 16460
    mt "Никчемные и безполезные сотрудники..."
    img 20878
    julia "Миссис Бакфетт, они нарушают рабочую атмосферу своим поведением!"
    img 22025
    m "Я ничего не знаю!"
    m "Просто так они не стали бы это делать."
    m "Значит, они выполняют какое-то важное распоряжение начальства!"
    img 22026
    julia "???"
    julia "Какое важное распоржение, Миссис Бакфетт?"
    julia "Посмотрет мои трусики?!"
    img 22027
    m "А я тут причем? Они просто выполняют свою работу..."
    img 22024
    julia "Как Вы ни причем?"
    julia "..."
    julia "Это же по Вашему приказу они это делают..."
    # Моника с безразличным видом
    img 22015
    m "Я не помню такого..."
    m "Мне до этого вообще нет дела... До каких-то низкоуровневых сотрудников."
    # Юлия удивленно
    img 22022
    julia "Но, Миссис Бакфетт... Как же так?"
    julia "Вы совсем недавно пытались ущипнуть меня... И поцеловать..."
    julia "Я пытаюсь понять причину, почему Вы так делаете..."
    img 22016
    julia "Вы..."
    julia "Вы пытаетесь сблизиться со мной?"
    julia "Вы ко мне неравнодушны?"
    # Моника удивлена
    img 16461
    m "!!!"
    m "С чего ты это взяла?!"
    # Юлия смущенно
    img 16462
    julia "Вы мне тоже очень... Нравитесь..."
    julia "Но я всегда боялась Вам сказать об этом..."
    # Моника смотрит на нее удивленно
    img 16463
    mt "Я ей нравлюсь?"
    mt "???"
    menu:
        "Подыграть Юлии.":
            pass
        "Как она могла про такое подумать?! (завершение сюжета с Юлией)":
            img 16464
            m "Юлия!!!"
            m "Ты о чем вообще говоришь?!"
            img 22017
            m "Как ты могла подумать, что такой как Я!"
            m "Может понравится девушка твоего уровня?!"
            m "Ты совсем глупая?!"
            img 16465
            mt "!!!"
            img 22350
            m "Перестань отвлекать меня от работы этой чушью!"
            m "И сама иди займись работой!!!"
            img 22883
            mt "Никчемная глупая помощница!!!"
            mt "!!!"
            return False
    img 21913
    mt "Хммм..."
    mt "Это отличный способ выяснить то, что мне нужно..."
    mt "По-другому никак - она слишком быстро прыгает."
    mt "Сейчас мне просто нужно подыграть ей!"
    mt "Притворюсь, что она тоже мне нравится."
    mt "..."
    img 21952
    mt "Я же не могу рассказать ей про настоящую причину своего поведения..."
    mt "Про мерзавца Фреда. Иначе она узнает правду про меня. А мне этого не нужно."
    mt "..."
    img 16466
    mt "Я эту глупую Юлию могу легко обмануть..."
    mt "Скажу, что она мне нравится..."
    mt "И она мне все расскажет и все покажет!"
    mt "Это гениально, Моника!"
    # Моника смотрит на Юлию
    img 16467
    m "Я думала, что скажу об этом тебе позже..."
    m "Но ты и правда мне нравишься."
    img 16468
    julia "!!!"
    img 16469
    m "Именно поэтому я щипала тебя за попу..."
    img 16470
    julia "Это правда?!"
    julia "Я Вам нравлюсь?!"
    julia "Поэтому Вы... Хотите залезть ко мне в трусики?"
    img 16471
    m "Да, Юлия..."
    julia "Я просто не могу поверить, что я вам и правда нравлюсь..."
    julia "Вы такая красивая и умная. Как я могу вам нравиться?"
    img 16472
    mt "Черт! Мне ей еще и доказывать это придется?!"
    mt "И уговаривать?!"
    mt "!!!"
    img 16473
    mt "С другой стороны..."
    mt "Думаю, этот способ сработает с точностью в тысячу процентов."
    mt "Так что я попробую."
    # Моника подходит к Юлии и обнимает ее, при этом пытается поднять ее платье.
    # платье чуть приподнимается сбоку, но так что трусиков не видно, либо это место закрыто рукой!
    img 16474
    w
    img 16475
    w
    img 16477
    m "Да, я мечтаю залезть к тебе в трусики, Юлия..."
    # Юлия придерживает платье рукой и отстраняется
    # Юлия, смущаясь
    img 16476
    w
    img 16478
    w
    img 16479
    julia "Миссис Бакфетт... Сначала нам нужно узнать друг друга лучше."
    img 16480
    m "И что ты хочешь от меня?"
    img 20930
    julia "Ну не знаю..."
    julia "Сначала люди ходят на свидания... Можно сходить в кафе и попить кофе."
    img 16481
    mt "Кафе?"
    mt "..."
    img 16482
    m "Ну хорошо. Куда ты хочешь?"
    m "Я не могу тебя вести в те пафосные места, куда хожу обычно..."
    m "Боюсь, ты будешь чувствовать себя неудобно."
    img 16483
    m "Выбирай то место, которое нравится тебе."
    m "Например, рядом с твоим домом. Кстати, где ты живешь?"
    img 16484
    julia "Я живу рядом с трущобами..."

    #
    img 16485
    mt "Надеюсь, не рядом с Shiny Hole..."
    $ notif(_("Моника работает в пабе Shiny Hole"))
    #
    img 16486
    m "Я хочу доказать тебе, что ты мне и правда нравишься..."
    m "Поэтому с удовольствием пойду с тобой в то кафе, где ты обычно бываешь."
    m "Хочу узнать тебя получше..."
    mt "Боже. Моника, что за чушь ты несешь?"
    # Юлия радостно
    img 16487
    julia "Правда?!"
    julia "У меня рядом с домом есть кафе!"
    julia "Мы можем пойти туда. А когда?"
    img 1648
    m "Думаю, завтра... Сегодня у меня много дел."
    img 16489
    mt "Уверена в том, что мне удастся улучить момент и подсмотреть ей под юбку..."
    img 16490
    julia "Хорошо, Миссис Бакфетт!"
    julia "Завтра встретимся с Вами в кафе."
    img 16491
    mt "Фи... На какие жертвы приходится идти из-за этой глупой просьбы Фреда..."
    # далее обычный рабочий день.
    $ log1 = _("Я решила подыграть этой никчемной Юлии. Отличный способ узнать цвет ее трусиков.") # квест лог
    return

# при клике на Юлию после назначения 1-го свидания
label ep210_dialogues5_julia_1_2:
    julia "Миссис Бакфетт, я не могу дождаться нашего свидания в кафе!"
    julia "Скорее бы наступил завтрашний день!"
    return

# Моника на следующий день приходит на работу
# становится доступным кафе в трущобах
label ep210_dialogues5_julia_2:
    # Юлии нет на рабочем месте
    mt "А где эта никчемная помощница?!"
    mt "Вот черт! Я совсем забыла..."
    mt "Я же договорилась с ней сегодня сходить в кафе."
    mt "Оно находится где-то рядом с трущобами."
    mt "Мне нужно сейчас идти на свидание с Юлией."
    $ log1 = _("Пойти на свидание с Юлией.")
    return

# ранее:
# Моника призналась, что она сама испачкала ковер и Юлия добровольно оттирала пятно
# Моника призналась, что испачкала ковер и заставила Юлию оттирать пятно
# Моника обвинила Юлию в порче ковра и заставила оттирать пятно, а потом ее уволила
# Моника обвинила Юлию в порче ковра и заставила оттирать пятно, потом простила и оставила на работе
# в зависимости от того, как Моника относилась к Юлии, у них будет развиваться разговор в баре

# Моника стоит перед кафе, мысли при клике на кафе
label ep210_dialogues5_julia_3_1:
    mt "Фи. Какая-то дешевая забегаловка."
    return

# Моника стоит перед кафе (глазик)
label ep210_dialogues5_julia_3_2:
    mt "Мне придется притвориться, что эта никчемная Юлия мне нравится."
    mt "Поверить не могу. Это же моя бывшая гувернантка..."
    mt "Как такая, как она, может понравиться такой леди, как Я?!"
    return

# Моника заходит в кафе в трущобах
label ep210_dialogues5_julia_3:
    # Юлия сидит за столиком, на столике две чашки. одна для Юлии, вторая для Моники
    # Моника садится к ней за столик
    mt "Надо же, какая она радостная..."
    mt "Ну что ж, не буду портить ей настроение..."
    julia "Миссис Бакфетт, я так рада, что Вы пришли!"
    julia "Я заказала Вам чай."
    m "Хорошо, Юлия. Спасибо."
    julia "Я всю ночь не могла уснуть..."
    julia "Неужели, я Вам и правда нравлюсь?"
    m "Это правда, Юлия."
    m "Я хочу узнать тебя поближе и..."
    mt "Узнать цвет твоих трусиков!"
    m "И проводить с тобой больше времени."
    julia "Не могу поверить в это..."
    julia "Вы такая красивая и успешная женщина, настоящая леди..."
    julia "Что Вы могли найти в такой как я?"
    mt "Я что, должна сейчас ей делать комплименты какие-то?"
    mt "И как это делать?!"
    # Моника перечисляет
    m "..."
    m "Ты очень милая и добрая."
    m "В моем окружении редко можно встретить таких людей..."
    m "..."
    m "Ты очень ответственная и старательно выполняешь все поручения..."
    m "И еще..."
    m "Ты очень красивая..."

    # если Моника заставляла Юлию оттирать пятно на ковре
    #
    julia "Почему тогда Вы так со мной обращались, Миссис Бакфетт?"
    $ notif(_("Моника заставляла Юлию оттирать пятно на ковре"))
    mt "Черт!"
    mt "Надо что-то придумать..."
    mt "..."
    #

    m "Я не могла понять, что меня в тебе так притягивает..."
    m "..."
    m "И злилась на это. Поэтому так вела себя."
    julia "А сейчас что изменилось?"
    m "Я решила, что мне нужно сделат каминг аут, несмотря на то, что скажут остальные..."
    m "Я устала притворяться и выдавать себя не за ту, какая я есть настоящая."
    m "При этом скрывать свои чувства к другой девушке..."
    m "Хоть она и совершенно другого, несравнимого с моим, социального статуса... Гувернантка."
    julia "Это очень смелый поступок, Миссис Бакфетт."
    julia "И я готова поддержать Вас."
    #

    mt "Что за чушь мне приходится говорить?!"
    mt "!!!"
    mt "Как бы подсмотреть ей под платье?"
    mt "???"
    julia "Мне нужно время, чтобы привыкнуть к этому..."
    # Моника роняет ложку на пол
    mt "Возможно, сейчас у меня получится заглянуть ей под платье..."
    mt "..."
    # наклоняется под стол за ней
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть в эту глупую игру мерзавца Фреда!"
            mt "Да еще и притворяться перед никчемной Юлией!"
            mt "!!!"
            # садится за столик прямо
            m "Юлия, забудь о том, что я тебе тут наговорила."
            m "У меня сегодня полно других, более важных дел."
            julia "Но... Миссис Бакфетт!"
            m "Просто забудь!"
            m "!!!"
            # встает и уходит
            return False
    # но Юлия снова закрывается и Моника ничего не видит
    mt "Черт!!!"
    mt "Как обычно!"
    mt "!!!"
    # Моника поднимает ложечку и садится прямо за стол
    # Юлия смущенно
    julia "Миссис Бакфетт, зачем Вы подглядываете мне под платье?"
    # Моника без особо энтузиазма
    m "Потому что ты мне нравишься..."
    # Юлия смущается
    m "Юлия, а ты вообще носишь трусики?"
    julia "Да, Миссис Бакфетт..."
    m "А какого они цвета?"
    julia "Миссис Бакфетт, это слишком личное..."
    julia "И еще слишком рано обсуждать такие вещи..."
    m "А сколько должно пройти времени?"
    julia "Я читала в одной книжке... О похожих отношениях... Таких как у нас с Вами..."
    julia "Это все... плохо закончилось там..."
    m "Юлия, не бери в голову разные дурацкие книжки."
    m "Все будет хорошо, если мы захотим этого... Доверься мне..."
    julia "Возможно Вы правы, Миссис Бакфетт..."
    julia "В той книжке начальница каждый день целовала свою подчиненную... Говорила ей комплименты."
    # еще больше смущаясь
    julia "И я хочу также..."
    # Моника психует
    mt "Кто написал такую дурацкую книжку?!"
    mt "!!!"
    mt "Теперь мне придется заниматься этими глупостями!"
    mt "Только для того, чтобы втереться этой никчемной Юлии в доверие!"
    m "..."
    m "Если я буду делать также, ты мне поверишь?"
    julia "Да, Миссис Бакфетт..."
    mt "Хорошо было бы попасть к ней в гости и там посмотреть, какого цвета у нее белье..."
    m "Юлия, а ты живешь где-то рядом?"
    m "Может быть, пригласишь меня к себе в гости?"
    m "Я хочу посмотреть, как ты живешь..."
    julia "Миссис Бакфетт, после одного свидания в гости я Вас не могу пригласить..."
    julia "Мне нужно время, чтобы привыкнуть к этому..."
    julia "И вообще поверить, что я действително нравлюсь Вам."
    julia "..."
    mt "!!!"
    m "Хорошо, я не буду торопить тебя."
    m "Сейчас мне нужно идти по делам."
    m "Встретимся в офисе..."
    # они встают
    # Юлия вопросительно на нее смотрит
    mt "Она что, ждет чего-то от меня?!"
    mt "Что она там говорила про свою дурацкую книжку?"
    mt "Каждый день ее нужно целовать и говорить комплименты?"
    menu:
        "Поцеловать Юлию.": #corruption
            pass
        "Не целовать.":
            mt "Нет, я не хочу этого делать!" # сердито
            mt "Не хочу и не буду!"
            mt "Что за глупости?!"
            mt "!!!"
            return False
    # Моника наклоняется к Юлии и целует ее в щечку
    $ log1 = _("Мне нужно каждый день целовать Юлию и говорить ей комплименты.") # квест лог
    return

# если Моника все делает правильно, то уровень Юлии повышается
# 2-е свидание становится доступно, когда Юлия достигает определенного уровня
# для 2-го свидания у Моники должны быть деньги, чтобы угостить Юлию

# Офис. Кабинет Моники. Моника, придя на работу
label ep210_dialogues5_julia_4_1:
    img 16495
    mt "Мне нужно просто чмокнуть ее в щечку..."
    mt "В это же нет ничего такого?"
    mt "Так я смогу втереться к ней в доверие."
    img 16496
    m "..."
    # подходит к Юлии и целует ее в щечку
    img 16497
    m "Я так соскучилась по тебе..."
    m "Милая..."
    m "Ты прекрасно выглядишь сегодня."
    img 16498
    # Юлия смущенно
    img 16499
    julia "Миссис Бакфетт... Спасибо. Мне так приятно..."
    return

# Офис. Кабинет Моники.
label ep210_dialogues5_julia_4_2:
    img 21954
    julia "Миссис Бакфетт?"
    img 22294
    mt "Ну что еще ей от меня нужно?!"
    mt "!!!"
    img 16492
    m "Да, милая?"
    # Юлия встает и подходит к Монике
    img 16493
    julia "Вы, наверное, устали?"
    julia "Хотите, я Вам помассирую плечи?"
    menu:
        "Да, Юлия. Хорошая идея.":
            pass
        "Нет, не отвлекай меня от работы.":
            img 20889
            m "Нет, Юлия!" # сердито
            m "Мне сейчас не до этого!"
            img 16494
            mt "Что за глупости?!"
            mt "!!!"
            img 16500
            m "Иди работай. И не отвлекай меня."
            img 22341
            julia "..." # садится на свое место
            return False
    # Юлия делает Монике массаж на плечи, Моника закрывает глаза и расслабляется
    img 16501
    w
    img 16502
    w
    img 16503
    mt "Боже. Как же приятно!"
    mt "Я так давно не была на массаже..."
    mt "Пожалуй, в этом нелепом притворстве есть свои плюсы."
    img 16504
    m "Ммммм..."
    img 16505
    # Юлия закончила массировать плечи
    img 16506
    julia "Вам понравилось, Миссис Бакфетт?"
    img 16507
    m "Да, очень..."
    m "Спасибо, милая."
    # Юлия наклоняется к Монике и чмокает ее в щеку
    img 16508
    w
    img 16509
    mt "Ого! Даже так?!"
    mt "Чувствую, я на верном пути..."
    # Юлия садится на свое место
    return

# Офис. Кабинет Моники. Моника, уходя с работы
label ep210_dialogues5_julia_4_3:
    img 16495
    mt "Теперь мне нужно поцеловать ее, прощаясь..."
    img 16496
    m "..."
    # подходит к Юлии и целует ее в щечку
    img 16497
    m "Мне пора идти по делам."
    m "До встречи..."
    m "Милая..."
    m "Буду скучать по тебе."
    # Юлия смущенно
    img 16499
    julia "Миссис Бакфетт... Я тоже по Вам буду скучать..."
    return

# Моника приходит утром на работу
label ep210_dialogues5_julia_5_1:
    img 20277
    menu:
        "Сделать Юлии массаж.":
            pass
        "Пригласить Юлию на второе свидание. (в следующем обновлении)":
            return False
    return

# если выбран пункт меню "Сделать Юлии массаж"
# Офис. Кабинет Моники.
label ep210_dialogues5_julia_5:
    mt "Что бы мне такого еще сделать для Юлии?"
    mt "Я должна как-то расположить ее к себе."
    mt "..."
    mt "Хммм..."
    mt "Массаж - это хорошая идея."
    # Моника подходит к столу Юлии
    m "Юлия, милая, ты так много работаешь..."
    m "Тебе нужно отдохнуть немного."
    m "Пойдем в комнату отдыха, посидим там немного? Отдохнем."
    julia "Спасибо, Миссис Бакфетт."
    julia "Я и правда устала. А еще так много работы..."
    # она садится на диванчик в комнате отдыха
    # Моника подходит к ней и кладет Юлию на диван
    m "Не переживай, я не буду делать ничего такого..."
    m "Просто помогу тебе немного расслабиться. Сделаю массаж."
    m "Ты можешь довериться мне..."
    m "Милая."
    # делает массаж ног, все выше и выше, пытаясь подсмотреть
    # Юлия лежит, балдеет
    menu:
        "Заглянуть Юлии под платье.":
            pass
        "Не заглядывать.":
            mt "Нет, я не буду этого делать!"
            mt "Мне надоело играть в эту глупую игру мерзавца Фреда!"
            mt "Да еще и притворяться перед никчемной Юлией!"
            mt "!!!"
            m "Все, Юлия!"
            julia "Да, Миссис Бакфетт..."
            julia "Спасибо за массаж. Мне очень понравилось."
            m "Иди работай!" # сердито
            # уходит и садится на свое место
            return False
    # Юлия снова закрывается и Моника ничего не видит
    mt "Черт!!!"
    mt "Как обычно!"
    mt "!!!"
    mt "Ну сколько можно?!"
    julia "Миссис Бакфетт, я еще к этому не готова."
    m "Конечно... Милая..."
    m "..."
    m "Я тебя не тороплю..." # выдавливает из себя улыбку
    julia "Спасибо за массаж. Мне очень понравилось."
    # чмокает Монику в щечку и уходит за свой стол. Моника сидит на диване сердитая
    mt "Я была почти у цели!!!"
    mt "!!!"
    mt "Еще бы чуть-чуть и я смогла бы закончить весь этот цирк!"
    mt "Как же меня это бесит!"
    mt "Никчемная бесполезная Юлия!!!"
    mt "!!!"
    return




########################## в v0.11 #############

# Моника заходит в кафе в трущобах
label ep210_dialogues5_julia_6:
    # садятся за столик, заказывают ужин
    # Моника - расскажи о себе. я тут поняла, что совсем ничего о тебе не знаю
    # Юлия говорит, что она с состоятельной семьи из другой страны, но она не хочет к ним возвращаться
    # они никогда ее не понимали и не поддерживали, поэтому она уехала и пытается жить самостоятельно
    # Моника - почему ты не хочешь возвращаться, а работаешь здесь
    # Юлия - должно произойти нечто экстраординарное, чтобы я вернулась к ним.
    # Моник про себя - странно. дома у нее богатая семья и не будет никакой нужды, а она здесь работает за копейки
    # Моника про себя - никогда не понимала логику неудачников...
    # Моника - а сейчас ты живешь здесь, в трущобах?
    # Юлия - да, я арендую тут квартиру.
    # Моника про себя - хмм.. арендовать квартиру в трущобах - это наверное недорого?
    # Моника - но жить в трущобах!! фи!
    # Моника - с другой стороны... не будет деревенщины Бетти и озабоченного сопляка Барди...
    # сколько уже можно работать за еду на эту семейку идиотов.
    # мне нужно будет подумать об этом...
    # Юлия - Миссис Бакфетт, спасибо за ужин. и я хотела бы... в знак благодарности за вечер...
    # стесняюсь что такая леди как вы в такой конуре как у меня
    # пригласить Вас к себе домой.
    # Моника говорит что да, это, конечно, будет шокирующе для меня и непривычно, но ради моих чувств к тебе я готова пойти бла бла бла
    # Моника - отлично! я почти у цели! действительно, замечательный вечер!
    # Моника - да, я с радостью
    # уходят с кафе
    return

# мысли Моники перед домом Юлии
label ep210_dialogues5_julia_7:
    # какой кошмарный дом! и как люди тут живут?!
    # наверняка, одни неудачники и... извращенцы!
    # и тут небезопасно вечером...
    # нет. вряд ли я смогу жить в таких условиях
    # такая леди, как я, никогда не сможет привыкнуть к таким условиям
    # Хотя для меня и это место сейчас бы подошло
    return

# Моника в квартире у Юлии
label ep210_dialogues5_julia_8:
    # Моника говорит, что здесь очень уютно
    # Юлия смущается
    # Моника подходит к ней и обнимает, поцелуй
    # кладет руку ей на талию, потом смещает руку на попу, пытаясь поднять платье
    # Юлия отстраняется, говорит, что еще не готова
    # Моника говорит - дай, я тебя просто потрогаю и не более
    # Юлия смущается, но соглашается
    # снова поцелуй, Моника трогает ее попу и нащупывает трусики
    # Моника про себя - я почти у цели. осталось уговорить ее задрать платье
    # Моника опускает руку немного ниже и пытается залезть под платье
    # но Юлия снова отстраняется и говорит, что на сегодня этого будет достаточно
    # Моника - черт! может, попроситься в туалет? ванная со стиральной машинкой будет наверное там же
    # спрашивает у Юлии и идет в туалет
    # в ванной открывает шкафчик или машинку и ищет трусики, находят а там несколько штук и все разные
    # Моника злится, что снова не удалось ничего выяснить
    # поцелуй, до завтра, милая
    return
