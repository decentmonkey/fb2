# Если на фитнесе было достаточно посещений (в идеале посмотрены все девочки), то появляется Фред в конце занятия.
# Фред говорит Монике что ей идет эта униформа. Моника злится и спрашивает что Фреду надо от нее.
# Фред говорит что нужен совет в выборе попы. Какой попы?
# Одной из тех что там занимается.
# Какую бы Вы предпочли, Миссис Бакфетт?
# Бетти, Стефани или Ребекку?
label ep23_dialogues3_1:
    fred "..."
    m "Фред!?"
    "Что ты здесь делаешь?! Нерадивый водитель!"
    "Твое место у машины!"
    fred "О! Миссис Бакфетт!"
    "Все забываю сказать что Вам очень идет эта униформа..."
    m "!!!"
    m "Что тебе здесь надо, Фред?!"
    fred "О! Миссис Бакфетт!"
    "Мне нужен Ваш совет..."
    m "Какой еще совет?!"
    fred "Совет в выборе попы..."
    m "Какой еще попы?! Что ты несешь?!"
    "Иди на свое рабочее место, немедленно!"
    fred "Одной попы из тех, которые там занимаются сейчас."
    fred "Какую попы Вы бы предпочли, Миссис Бакфетт?"
    fred "Бетти..."
    fred "Стефани..."
    fred "или Ребекку?"
    mt "Вот мерзававец!!!"
    "Как он смеет разговаривать со мной о таких вещах!"
    mt "..."
    mt "Хотя..."
    # Моника говорит что бери Бетти, эта дура как раз заслуживает такого болвана как ты.
    # Фред говорит что это будет непрофессионально, т.к. он у нее работает.
    # Моника говорит что добраться до других у него шансов есть.
    # Фред говорит что Моника поможет ему в этом. Моника спрашивает с какой стати.
    # Фред отвечает что Моника что-нибудь придумает, потому что иначе ей придется пожертвовать своей попой.
    # Хватает ее за зад.
    m "Бери Бетти, эта дура как раз заслуживает такого болвана как ты!"
    fred "Миссис Бакфетт, это будет непрофесионально, так как я работаю у нее."
    "А Вы знаете, я профессионал!"
    m "В любом случае, добраться до остальных у тебя шансов нет!"
    fred "У меня есть шансы, Мэм..."
    fred  "Ведь Вы поможете мне в этом..."
    m "С какой стати я тебе будут помогать в твоих похотливых фантазиях, Фред?!"
    m "Тебе мало что ты уже натворил, подлец?!"
    fred "Вы обязательно что-нибудь придумаете, Миссис Бакфетт..."
    m "Я не собираюсь разговаривать с тобой об этом!"
    fred "Вы обязательно что-нибудь придумаете, Миссис Бакфетт..."
    fred "В противном случае, Вам придется пожертвовать своей попой для этого..."
    # Хватает ее за зад.

    # Моника поворачивается и, в зависимости от bitchness дает пощечину, либо дает по яйцам ногой.
    menu:
        "Ударить Фреда между ног!" if monicaBitch == True:
            m "ЧТО?!?!"
            "ТЫ МЕНЯ РЕШИЛ ЛАПАТЬ?!?"
            "НИЧТОЖЕСТВО!!!"
            "ПОЛУЧАЙ!!!"
            "НА!!!"
            fred "АААААххххх!!!"
            fred "Что Вы сделали, Миссис Бакфетт..."
            "Это же..."
            "Это же... Больно..."
            # Фред падает, если ударили.
            # В это время заходят Стефани и Ребекка
            # Видят Фреда. Моника делает комментарий в его сторону, чтобы он убирался отсюда, болван.
            m "Сейчас я воткну каблук в твой глаз, мерзавец!"
            "Если ты сейчас же не уберешься отсюда!!!"
            "Ты забыл с кем связался! Ничтожество!"
        "Ударить Фреда между ног! (Моника слишком приличная) (disabled)" if monicaBitch == False:
            pass

        "Дать пощечину Фреду." if monicaBitch == False:
            m "ЧТО?!?!"
            "ТЫ МЕНЯ РЕШИЛ ЛАПАТЬ?!?"
            "НИЧТОЖЕСТВО!!!"
            fred "Айй!!"
            fred "Вы применили насилие!"
            # В это время заходят Стефани и Ребекка
            # Видят Фреда. Моника делает комментарий в его сторону, чтобы он убирался отсюда, болван.
            m "Следующий удар будет гораздо больнее, мерзавец!"
            "Если ты сейчас же не уберешься отсюда!!!"
            "Ты забыл с кем связался! Ничтожество!"

        "Дать пощечину Фреду. (Моника недостаточно приличная) (disabled)" if monicaBitch == True:
            pass
    # Стефани и Ребекки нравятся слова Моники и они разговаривают с ней о том наконец-то увидели прежнюю Монику.
    # А то они уже стали сомневаться по поводу ее слов.
    # Моника говорит чтобы не сомневались.
    # После этого несколько меняется диалог при встрече подруг на фитнесе.
    stephanie "Вау! Моника!"
    rebecca "Моника! Вот это да!"
    stephanie "Наконец-то мы узнаем нашу Монику!"
    rebecca "Да, Моника, а то мы уже начали сомневаться в тебе!"
    m "Я хочу предупредить Вас, девочки!"
    "Если кто-то будет сомневаться во мне, то последует за тем болваном!"
    stephanie "Нет, Моника! Пожалуйста не надо!"
    rebecca "Мы твои верные подруги, Хи-хи!"
    stephanie "Скорее завершай свое приключение."
    "Нам не терпится все узнать!"
    rebecca "Да, Моника!"
    "Про тебя можно снимать кино!"
    mt "Да уж, про меня уже можно снимать кино, это точно..."
    stephanie "Пока, Моника!"
    "Чмок!"
    rebecca "Пока, Моника!"
    "Чмок!"
    m "Пока, девочки!"
    return


label ep23_dialogues3_2:
    stephanie "Привет, Моника!"
    m "Привет, девочки!"
    rebecca "Моника, мы скучаем по тебе!"
    stephanie "Скажи нам сразу как только соберешься на наш девичник!"
    "Мы тебя ждем!"
    m "Хорошо, девочки!"
    return

label ep23_dialogues3_3:
    # Фред, если к нему подойти у дома, смотрит на Монику.
    # Моника спрашивает хочет-ли он еще получить?
    # Фред делает вид что боится и что не хочет. Моника говорит чтобы тогда помалкивал.
    m "Фред, ты на меня все-время смотришь..."
    m "Тебе показалось мало в прошлый раз?"
    "Ты хочешь получить еще?"
    fred "Нет, Мэм!"
    "Никак нет!"
    m "Вот и помалкивай! Болван!"
    return

    # Когда Моника трет пятно, периодически вместо Бетти появляется Фред, который смотрит на нее.
    # Если Моника кликнет на Фреда, то оборачивается и говорит чтобы он проваливал, если не хочет получить еще.
    # Фред говорит что просто гуляет и ищет надо-ли где-то применить его профессионализм.
label ep23_dialogues3_4:
    m "Фред! Что ты шляешься здесь?!"
    "Проваливай отсюда, пока не получил по зубам!"
    fred "Мэм! Я просто прогуливаюсь!"
    "Вы знаете, Я профессионал."
    "И ищу вдруг где-то надо применить мой профессионализм!"
    m "Это точно не здесь, Фред!"
    return

label ep23_dialogues3_5:
    # В один из дней Бетти находится в спальне. Заходит Фред.
    # Бетти в белье (заранее определяется какое белье, запуск когда в определенном)
    # Бетти зло спрашивает что он тут делает?
    # Фред говорит что его послал Мистер Робертс, чтобы позвать Бетти, потому что он уезжает с Фредом по делам
    # и хочет поцеловать супругу перед отъездом.
    # Бетти спрашивает и что, ради этого он послал прислугу водителя в ее спальню?
    # Фред отвечает что вообще-то нет, просто кое-кто еще хочет ее поцелуя.
    # И снимает штаны.
    img 8536
    w
    img 8537
    w
    img 8538
    w
    img 8539
    betty "Фред?!"
    img 8540
    betty "Фред! Что ты делаешь здесь?! В спальне хозяев!"
    img 8541
    fred "Миссис Робертс! Меня послал Мистер Робертс, чтобы я позвал Вас спуститься вниз к нему!"
    fred "Мистер Робертся собирается уезжать по делам, до вечера, и хочет поцеловать супругу перед отъездом!"
    img 8542
    betty "И что, ради этого от прислал прислугу водителя в нашу спальню?"
    img 8543
    fred "Мэм, вообще-то нет..."
    sound snd_fabric1
    #fade
    img 8544
    "Просто кое-кто еще хочет Ваш поцелуй..."
    # И снимает штаны.

    # Бетти говорит что он сошел с ума? Здесь ходит Барди, не хватало чтобы он это увидел.
    # И что он вообще себе позволяет в ее спальне?
    # Фред отвечает что закрыл дверь и ведет себя профессионально, так как хозяйка богатого дома хочет поцеловать его член.
    # Бетти смотрит на Фреда, спускается и целует.
    # Фред говорит что хозяйка дома хочет взять член в рот поглубже. Бетти делает минет.
    # Фред кончает и говорит что спасибо, теперь можно идти к Мистеру Робертсу.
    img 8545
    w
    img 8546
    w
    img 8547
    betty "Фред?! Ты сошел с ума?!"
    "Здесь ходит Барди! Не хватало чтобы он это увидел!"
    img 8548
    betty "И что ты вообще себе позволяешь?!"
    img 8549
    "Прямо в спальне хозяев дома!"
    img 8550
    fred "Мэм, я профессионал и поэтому предусмотрительно закрыл дверь."
    fred "Я веду себя профессионально, так как знаю что хозяйка богатого дома хочет этот член..."
    betty "!!!"
    img 8551
    betty "..."
    fred "..."
    img 8552
    betty "..."
    img 8553
    w
    img 8554
    w
    img 8555
    w
    img 8556
    w
    img 8557
    driver "Ну-же..."
    img 8558
    w
    #dissolve
    img 8559
    w
    img 8560
    w
    img 8561
    w
    img 8562
    w
    img 8563
    w
    img 8564
    w
    img 8565
    w

    # Бетти смотрит на Фреда, спускается и целует.
    img 8566
    fred "Хозяйка богатого дома хочет взять член в рот поглубже..."
    img 8567
    betty "..."
    img 8568
    w
    img 8569
    w
    img 8570
    w
    img 8571
    w
    img 8572
    w
    img 8573
    fred "ААААаааааххх!"
    #longfade
    img 8574
    fred "Спасибо, Мэм."
    "Теперь можно идти к Мистеру Робертсу."
    img 8575
    w
    img 8576
    w

    # Бетти говорит что куда это он собрался, давай быстрее и тд. Повторяется сцена секса (можно взять из прошлой версии)
    # Фред кончает. Бетти говорит что не вздумай снова кончить на лицо, раздается крик Ральфа: Бетти, ты где?
    # Фред снова кончает на лицо, Бетти зло смотрит и вытирает его.
    img 8577
    betty "Куда это ты собрался?!"
    betty "А как же я?!"
    img 8578
    #звук падающих предметов
    w
    img 8579
    betty "Давай быстрее!"
    img 8580
    fred "Как скажете, Мэм!"
    "Вы мой Босс!"
    img 8581
    betty "И не забудь вытереть свой член от спермы, прежде чем начнешь!"
    #fade
    img 8582
    fred "Да, Мэм! Конечно!"
    img 8583
    betty "Вовсе необязательно делать это о мою занавеску!"
    #fade
    img 8584
    fred "Простите, Мэм!"
    img 8585
    fred "Я приношу свои извинения."
    img 8586
    fred "Как профессионал!"
    #sex
    img 8587
    w
    img 8588
    w
    img 8589
    w
    img 8590
    w
    img 8592
    fred "ААААаааааххх!"
    img 8593
    betty "Фред! Не вздумай кончить в меня!"
    img 8594
    betty "..."
    #fade
    img 8595
    ralph "Бетти!"
    img 8596
    betty "И не вздумай кончить мне на лицо, как в прошлый раз!"
    img 8597
    ralph "Бетти! Ты где?"
    img 8598
    fred "ААААаааааххх!"
    #fade
    img 8599
    betty "!!!"
    img 8600
    fred "..."
    img 8601
    betty "..."
    img 8602
    w
    #fade
    img 8603
    w
    ralph "Бетти! Ты где?"
    # Кричит в ответ: Ральф, я иду, хватит орать на весь дом!
    # Они спускаются вниз. Фред говорит Ральфу что дверь в комнату Бетти была закрыта и он ждал, пока она закончит макияж.
    # Бетти спрашивает Ральфа зачем он ее звал.
    # Ральф отвечает что едет на важную встречу и хотел чтобы Бетти поцеловала его (Бетти только что была вся в сперме)
    # Бетти решает целовать его или нет. Если целовать, то в губы или в щеку.
    img 8604
    betty "Ральф, я иду!"
    "Хватит орать на весь дом!"

    img 8605
    fred "Мистер Робертс, дверь в комнату Миссис Робертс была закрыта."
    "Поэтому я ждал, пока она закончит наносить макияж."
    img 8606
    betty "Ральф, зачем ты звал меня?"
    img 8607
    ralph "Бетти, я еду на важную встречу и хочу чтобы ты поцеловала меня, любимая!"
    "Мне осталось надеть костюм и я выезжаю!"
    img 8608
    betty "..."
    img 8609
    fred "..."
    menu:
        "Не целовать Ральфа.":
            img 8610
            betty "Ральф! Ты не заслужил моего поцелуя!"
            "Ты плохо ведешь себя, кушаешь не вовремя и не помогаешь мне ни в чем!"
            img 8611
            ralph "..."
            betty "Когда ты заслужишь, я поцелую тебя!"
        "Поцеловать Ральфа в щеку.":
            img 8612
            betty "Да, любимый, иди я тебя поцелую!"
            img 8613
            betty "Чмок!"
            img 8614
            ralph "..."
        "Поцеловать Ральфа в губы.":
            img 8612
            betty "Да, любимый, иди я тебя поцелую!"
            img 8615
            betty "Чмок!"
            img 8617
            ralph "..."
            img 8616
            w


    return

label ep23_dialogues3:
    return
