# Появляется диалог поговорить о повышении
# Только если Эшли или Джо уровень 2
label ep27_dialogues7_pub1:
    menu:
        "Спросить о повышении.":
            pass
# Моника спрашивает, можно-ли ее повысить, чтобы она зарабатывала какие-то деньги?
    img 20953
    m "Эшли..."
    m "Можно-ли попросить дать мне еще другую работу, чтобы я..."
    m "Что я зарабатывала какие-то деньги здесь?"
# Далее:
# Если ур у Эшли и Джо < 1
    img 20954
    ashley "Хммм..."
    ashley "Если честно, я не уверена в тебе [monica_pub_name]."
    ashley "Поработай пока посудомойкой!"
    img 20955
    m "!!!"
    help "Требуется отношение с Джо, либо Эшли выше 1."

# Если у Эшли ур.1, то она говорит что не уверена в ней, но Джо отзывается о ней хорошо (показан хитрый Джо)
    img 20956
    ashley "Хммм..."
    ashley "Если честно, я не уверена в тебе [monica_pub_name]."
    ashley "Но Джо отзывается хорошо о тебе."
    joe "..." # хитрый

# Если у Эшли ур.2, то она говорит что уже успела разглядеть ее попку
    img 20957
    ashley "Хммм..."
    ashley "Если честно, то я уже успела разглядеть твою попку, [monica_pub_name]."

# И, пока она работает, никто не пришел проверять ее из миграционной полиции или санитарного контроля.
# Также после ее мытья посуды не отравился ни один клиент.
# И Эшли было бы интересно посмотреть на ее голую попку, которая будет крутиться на пилоне.
# Поэтому она разрешает ей танцевать здесь, но трахаться с клиентами пока нельзя, хотя я знаю что ты за этим пришла сюда.
    img 20958
    ashley "И, пока ты работаешь, никто не пришел проверять тебя из миграционной полиции или санитарного контроля."
    img 20959
    m "..."
    img 20960
    ashley "Также, после твоего мытья посуды не отравился ни один клиент."
    img 20961
    ashley "Так что мне было бы интересно посмотреть на твою голую попку, которая будет крутиться на пилоне."
    ashley "Поэтому, так уж и быть."
    ashley "Я разрешаю тебе танцевать здесь..."
    img 20962
    ashley "Но трахаться с клиентами пока нельзя!"
    ashley "Хотя я знаю что ты за этим пришла сюда."
# Моника в шоке. Отвечает что не собирается танцевать здесь в голом виде!
# Эшли удивленно спрашивает а что же она тогда хочет? О каком повышении говорит?
# Джо говорит что видишь Эшли, она приличная девушка, пусть она работает у нас официанткой!
# Эшли спрашивает у Джо что ты решил отдать мою работу Мэрилин?
    img 20963
    m "!!!"
    m "Я не собираюсь танцевать здесь в голом виде!"
    img 20964
    ashley "А что же ты тогда хочешь?"
    ashley "О каком повышении ты говоришь?"
    joe "Видишь, Эшли? [monica_pub_name] приличная девушка."
    joe "Пусть она работает у нас официанткой!"
    img 20965
    ashley "Джо, ты что, решил отдать мою работу [monica_pub_name]?!"
# Может быть ты на ней женишься вместо меня, Джо?!
# И будешь сам платить кредиты за это заведение?!
# Джо улыбается. Нет, Эшли, я не это имел ввиду.
# У нее нет документов, но ей нужно зарабатывать хотя бы пару долларов, правда, Мерилин?
    img 20966
    ashley "Может быть ты на ней женишься вместо меня, Джо?!"
    ashley "И будешь сам платить кредиты за это заведение?!"
    img 20967
    joe "Нет, Эшли! Я не это имел ввиду!"
    joe "У нее нет документов, но ей нужно зарабатывать хотя бы пару долларов."
    img 20968
    joe "Правда, [monica_pub_name]?"

# Моника кривится
# Уверен, что обладательнице такой попки будут платить хорошие чаевые, которые мы можем забирать себе, Эшли!
# Она ведь работает у нас неофициально! Скажем, отдавать ей 10 процентов от того что ей дадут клиенты.
# И ей необязательно платить основную зарплату, ей вполне хватит остатка от чаевых.
# Ведь так, Мэрилин?
    img 20969
    mt "!!!" # Моника кривится
    img 20970
    joe "Уверен, что обладательнице такой фигуры будут платить хорошие чаевые, которые мы можем забирать себе, Эшли!"
    img 20971
    mt "ЧТО?!"
    img 20972
    joe "Она ведь работает у нас неофициально!"
    joe "Можно, скажем, отдавать ей 10 процентов от того, что ей дадут клиенты."
    joe "И нам необязательно платить ей основную зарплату."
    joe "Ей вполне хватит остатка от чаевых."
    img 20973
    joe "Ведь так, [monica_pub_name]?"
# Моника кривится
# А ты, Эшли, будешь получать чаевых даже больше чем раньше и при этом уделять больше времени бару.
# Эшли задумалась. Т.е., Джо, ты предлагаешь отправить Мэрилин к этим пьяницам и не платить ей деньги?
# Платить, но только 10 процентов от чаевых. Мы ничем не рискуем, Эшли! Нет зарплаты - не нужны документы!
# Эшли спрашивает: а если она нагрубит клиенту? Или заберет чаевые себе?
# Джо говорит что Мэрилин выглядит как порядочная девушка и не будет брать себе лишнего!
# Эшли спрашивает у Моники: Мэрилин, и ты согласна на такую работу?
    img 20974
    m "!!!" # Моника кривится
    img 20975
    joe "А ты, Эшли, будешь получать чаевых даже больше чем раньше и при этом уделять больше времени бару."
    img 20976
    ashley "..."
    ashley "То есть, Джо, ты предлагаешь отправить [monica_pub_name] к этим пьяницам и не платить ей деньги?"
    img 20977
    joe "Платить, но только 10 процентов от чаевых. Мы ничем не рискуем, Эшли!"
    joe "Нет зарплаты - не нужны документы! Не страшны никакие проверки!"
    img 20978
    ashley "А если [monica_pub_name] нагрубит клиенту?"
    ashley "Или заберет чаевые себе?"
    img 20979
    m "!!!"
    img 20980
    joe "[monica_pub_name] выглядит как порядочная девушка и не будет брать себе лишнего."
    img 20981
    ashley "..."
    ashley "Ну, не знаю..."
    img 20982
    ashley "[monica_pub_name], и ты согласна на такую работу?"

# Выбор:
# Я не согласна работать за такие копейки!
# Моника говорит что не согласна работать за такие копейки. (уходя)
# Джо говорит что если надумает, то пусть приходит
    menu:
        "Я не согласна работать за такие копейки!":
            img 20983
            m "Я не согласна работать за такие копейки!"
            img 20984
            joe "[monica_pub_name], если надумаешь, то приходи." # подмигивает
            return -1
        "Согласиться.":
            pass
# Согласиться.
# Моника говорит что согласна работать, ей нужна хоть какая-то работа.
# Что не будет грубить клиентам, будет общаться с ними вежливо.
# И что будет отдавать чаевые им.
    img 20985
    m "Я..."
    m "Я согласна работать. Мне нужна хоть какая-то работа."
    m "Я обещаю что не буду грубить клиентам, а буду обращаться с ними вежливо."
    img 20986
    ashley "..."
    img 20987
    m "И буду отдавать чаевые Вам..."
# Эшли говорит что хорошо, ты можешь вилять своей попкой, но не вздумай заигрывать с посетителями!
# Здесь не бордель! И она не потерпит официантку, которая будет вести себя как шлюха!
# Моника отвечает что Эшли может не беспокоиться, она не будет выходить за рамки рабочих обязанностей.
    img 20988
    ashley "Ну хорошо. Ты можешь вилять своей попкой, но не вздумай заигрывать с посетителями!"
    ashley "Здесь не бордель!"
    ashley "И я не потерплю официантку, которая будет вести себя как шлюха!"
    img 20989
    m "Эшли, Вы можете не беспокоиться."
    m "Я не буду выходить за рамки рабочих обязанностей."
# Моника думает что ей с трудом вериться что она вообще ведет такой диалог!
# Она, Моника Бакфетт! И говорит такие слова!
# Утешает только то, что ее считают здесь Мерилин, а это значит она в этом месте не имеет ничего общего с Моникой Бакфетт.
# Иначе, она не смогла бы согласиться на такое.
    img 20990
    mt "О БОЖЕ!"
    mt "Мне с трудом вериться в то что я вообще такое говорю!"
    mt "Я! Моника Бакфетт!"
    mt "И говорю такие слова!"
    img 20991
    with diss
    mt "..."
    mt "Утешает только то, что меня здесь считают [monica_pub_name]."
    mt "А это значит, что в этом месте я не имею ничего общего с Моникой Бакфетт."
    mt "Но мне не стоит забывать кто Я!"
    mt "В конце концов, мне еще предстоит долгая жизнь, когда я верну свое положение назад..."
#
# Эшли говорит Мэрилин, чтобы та одевала рабочую униформу и шла работать.
#
    ashley "[monica_pub_name], ты меня слышишь?!"
    img 20992
    m "А?" # оборачивается
    img 20993
    ashley "[monica_pub_name], ты можешь одевать рабочую униформу и идти работать."
    return

label ep27_dialogues7_pub2:
# Появляется опция меню Работать официанткой.
    menu:
        "Работать официанткой в Shiny Hole.":
            pass

label ep27_dialogues7_pub3:
# Если уже работала
# Моника говорит что уже работала сегодня и больше не может терпеть эти пьяные лица.
    mt "Я уже работала сегодня и больше не могу смотреть на эти пьяные лица!"
    return

label ep27_dialogues7_pub4:
#
# Если не работала сегодня, то подходит и говорит что пришла работать официанткой.
# Эшли говорит чтобы Моника шла и переодевалась в униформу и шла работать.
# Эшли уже надоело работать самой. Для этого есть Мерилин.
# Моника злится
    img 20994
    m "Эшли..."
    ashley "..."
    m "Я пришла работать официанткой."
    ashley "Хорошо, [monica_pub_name]."
    ashley "Иди переодевайся в униформу и иди работать."
    ashley "Мне уже надоело работать самой."
    ashley "Для этого есть ты, [monica_pub_name]!"
    mt "Меня бесит эта женщина..."
    return

label ep27_dialogues7_pub5:
# Моника закончила работать
# Моника говорит что хватит с нее. Она больше не может терпеть эти пьяные лица.
    mt "Все, с меня хватит!"
    mt "Я больше не могу терпеть эти пьяные лица!"
    return

label ep27_dialogues7_pub6:
# Моника может уйти. Тогда идет выбор уйти без того что отдала чаевые. Если да, то уходит.
# Если нет, то остается.
    menu:
        "Уйти и не отдавать чаевые хозяевам бара.":
            return False
        "Остаться.":
            return True
    return

label ep27_dialogues7_pub7:
# При клике на барменов, Моника говорит что закончила работу и вот чаевые.
# Эшли дает ей 10 процентов и говорит приходить работать еще.
    img 20995
    m "Эшли, я закончила работу."
    m "Вот чаевые, которые я смогла получить..."

    # если есть чаевые
    img 20996
    ashley "Хорошо. Вот твои десять процентов."
    ashley "Завтра приходит работать еще."

    # если нет чаевых
#    img 20995
    m "Мне никто не дал чевых сегодня..."
    return


label ep27_dialogues7_pub8:
# Если Моника не отдала чаевые, то при клике на барменов, идет диалог:
# Эшли ругается на Монику за то что та не отдала чаевые.
# Эшли говорит Джо что она так и знала. Она с самого начала говорила что Мэрилин шлюха, которая ворует деньги.
# Эшли говорит Монике чтобы та убиралась и что у нее больше нет работы для нее.
    img 20997
    ashley "[monica_pub_name], я так и знала что ты воровка и шлюха!"
    img 20998
    m "!!!"
    img 20999
    ashley "Джо! Я тебе говорила!"
    ashley "Я тебя предупреждала!"
    ashley "Она украла наши деньги, Джо!"
    img 21000
    m "!!!"
    ashley "Что смотришь? Убирайся отсюда!"
    ashley "Здесь больше нет для тебя работы!"
    ashley "И я не буду тебя обслуживать даже за деньги!"

# Выбор
# Уйти
# Попросить снова взять работать
    menu:
        "Попросить снова взять работать в Shiny Hole.":
            pass
        "Уйти.":
            return False
# Моника говорит что извиняется, что просто забыла в конце смены отдать деньги.
# Она готова это сделать и продолжить работать.
# Эшли спрашивает, сколько чаевых было в тот день.
# Моника отвечает сколько
# Эшли говорит что не верит ей. Чаевых было как минимум $ 500, раз она решила не отдавать эти деньги.
# Моника оправдывается что нет.
# Эшли говорит что ничего не знает. Либо Моника отдает $ 500, либо пусть идет отрабатывать деньги виляя задницей.
# А до этого пусть убирается отсюда!
    img 21001
    m "Эшли, Джо, я прошу извинить меня."
    m "Я просто очень устала за рабочий день и забыла в конце отдать деньги."
    m "Я готова сделать это сейчас и продолжить работать здесь."
    img 21002
    ashley "Сколько чаевых было в тот день?"
    img 21003
    if pub_tips_amount_day > 0:
        m "В тот день было $ [pub_tips_amount_day]."
    else:
    # либо
        m "В тот день не было чаевых."
    img 21004
    ashley "Я не верю тебе, [monica_pub_name]!"
    ashley "Чаевых было как минимум $ 500, раз ты решила не отдавать их."
    img 21005
    m "Нет, столько не было!"
    m "Клянусь!"
    m "Такой суммы просто не могло быть..."
    mt "В этой дыре!!!"
    img 21006
    ashley "Меня не волнуют твои оправдания, [monica_pub_name]."
    ashley "Либо ты отдаешь эти $ 500 наличными, либо иди отрабатывать эти деньги, виляя своей задницей на сцене."
    img 21007
    m "!!!"
    img 21008
    w
    img 21000
    ashley "А иначе убирайся отсюда!"


# После этого появляется выбор при клике на барменов
# -Отдать $ 500
# Моника отдает деньги Эшли
# Эшли говорит что так уж и быть, теперь ты можешь снова работать, но не испытывай моего терпения!
# -Идти танцевать на сцену (в следующей версии игры)
# -Попросить прощения по другому...
    menu:
        "Отдать $ 500.":
            img 21009
            m "Эшли..."
            m "Вот $ 500..."
            img 21010
            ashley "Я так и знала, ха-ха!"
            ashley "Ладно, так уж и быть. Теперь ты можешь снова работать здесь."
            ashley "Но не испытывай моего терпения!"
            return 1
        "Идти танцевать на сцену (в следующем обновлении) (disabled)":
            pass
        "Попросить прощения по другому...":
            return 2
    return


label ep27_dialogues7_pub9:
# Если подходит к Джо:
# Моника говорит что у нее нет таких денег и она бы не хотела танцевать голой у всех на виду.
# Может быть есть еще какие-то варианты.
# Джо отвечает, что есть один вариант попросить прощения. Джо подмигивает
# Моника напряженно смотрит
# Джо говорит Мэрилин, чтобы она дождалась пока Эшли отвернется и шла в подсобку за Джо
    
    m "Джо... У меня нет таких денег."
    m "И я бы..."
    m "Я бы не хотела танцевать голой у всех на виду..."
    m "Может быть есть еще какие-то варианты?"
    joe "Вообще-то, [monica_pub_name], есть один вариант попросить прощения."  # Джо подмигивает
    m "..." # Моника напряженно смотрит
    joe "[monica_pub_name], если хочешь, чтобы тебя простили, дождись пока Эшли отвернется"
    joe "И иди в служебную комнату за мной."

# Выбор:
# Подождать пока Эшли отвернется и идти в подсобку за Джо
# Уйти
    menu:
        "Подождать пока Эшли отвернется и идти в подсобку за Джо.": #corruption
            pass
        "Подождать пока Эшли отвернется и идти в подсобку за Джо. (в следующем обновлении) (diabled)":
            pass
        "Уйти.":
            return False

    return True

label ep27_dialogues7_pub10:
# Если идет, вызывается меню со сценами с Джо (открываются последовательно)
# Сцена1:
# Трогает зад
# Джо
    joe "О, [monica_pub_name], ты пришла!"
    m "Да, Джо, я пришла."
    joe "Тебя точно не видела Эшли?"
    joe "Не видела как ты сюда заходила?"
    m "Нет, Джо."
    m "Меня не видела Эшли."
    m "Но она может придти сюда в любой момент."
    joe "Нет, [monica_pub_name], она не придет."
    joe "Пока меня нет, она не оставит бар без присмотра."
    joe "У нас здесь, знаешь-ли, такие клиенты... хе-хе."
    m "Я знаю какие здесь клиенты, Джо..."
    joe "..."
    m "Джо, я готова еще раз извиниться за то что не отдала деньги."
    m "Я правда забыла и..."
    joe "[monica_pub_name], хватит про эти деньги."
    joe "Мне не нужны эти деньги, я хочу тебя, [monica_pub_name]!"
    joe "Я хочу твою попку, [monica_pub_name]!"
    m "Джо, это исключено!"
    m "У тебя есть жена, которая прямо за стенкой!"
    m "Да, я хочу работать здесь, но я не собираюсь за это спать с таким жирным толстяком, как ты, Джо!"
    joe "[monica_pub_name], очень жаль."
    joe "Но повернись, хотя бы, своей попой."
    joe "Покажи ее мне!"
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            m "Нет, Джо!"
            return False
    m "И на этом все, ты сделаешь так, чтобы Эшли простила меня!"
    joe "Хорошо, [monica_pub_name]."
    joe "Повернись своей попой, скорее!"
    m "..."
    mt "Дьявол, мне не хочется делать этого!"
    mt "С другой стороны, в этом нет ничего страшного и это позволит мне снова работать здесь..."
    mt "Мне нужны деньги..."
    # Моника показывает зад

    joe "!!!"
    m "Все? Достаточно?"
    joe "[monica_pub_name], я должен потрогать твою попу!"
    joe "Она такая сладкая! Я хочу этого, [monica_pub_name]!"
    m "Нет!"
    joe "Я потрогаю ее и обещаю что Эшли простит тебя!"
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            m "Нет, Джо!"
            return False

    m "Ладно, но только в одежде!"
    m "И я не буду отдавать те чаевые, которые взяла себе!"
    joe "Хорошо, [monica_pub_name]!"
    joe "Можешь оставить эти деньги себе!"
    # трогает
    joe "Ахххх!"
    joe "Как я мечтал об этом!"
    joe "Я стал мечтать об этом с первой минуты, когда увидел тебя здесь, [monica_pub_name]!"
    mt "Очередной озабоченный мерзавец!"
    joe "Ах, твоя попка!"
    joe "Она такая упругая!"
    joe "Ах!"
    m "Ну все, хватит!"
    m "Идет к Эшли!"
    return

label ep27_dialogues7_pub11:
# Трогает голую грудь
    joe "[monica_pub_name], ты пришла!"
    joe "Я хочу посмотреть твою грудь!"
    joe "Я хочу увидеть ее!"
    m "Нет!"
    joe "Мне жаль, [monica_pub_name], но Эшли начнет что-то подозревать."
    joe "Это большой риск для меня."
    menu:
        "Согласиться показать грудь.": #corruption
            pass
        "Отказаться.":
            m "Нет, Джо!"
            return False
    m "Ладно..."
    # Моника снимает верх
    joe "Ах! Какие сиськи!"
    joe "Тебе определенно надо танцевать на сцене, [monica_pub_name]!"
    mt "!!!"
    joe "Можно я потрогаю их?"
    m "Нет, Джо! Мы договорились!"
    joe "Я не могу так, не могу, [monica_pub_name]!"
    joe "Дай я только прикоснусь к ним и Эшли простит тебя, я обещаю!"
    menu:
        "Согласиться.": #corruption
            pass
        "Отказаться.":
            m "Нет, Джо!"
            return False
    m "Ты прикоснешься к моей груди буквально на секунду."
    joe "Да, [monica_pub_name], я обещаю!"
    m "И больше никаких условий после этого."
    m "Обещаешь?!"
    joe "Да, [monica_pub_name], я обещаю!"
    mt "Дьявол!"
    mt "Мое изысканное тело создано для того, чтобы быть на обложке модного журнала..."
    mt "До чего я докатилась, О БОЖЕ!"
    mt "Хотя... Это не Я... Это [monica_pub_name]..."
    # джо трогает грудь
    m "Все, Джо!"
    m "Хватит!"
    return

label ep27_dialogues7_pub12:
# Просит посмотреть на ее обалденную попку
    joe "[monica_pub_name], я хочу увидеть твою попку!"
    m "!!!"
    m "Ладно..."
    # Моника поворачивается задом
    joe "Нет, [monica_pub_name], я хочу увидеть твою попку голой!"
    joe "Покажи ее мне и я сделаю так, чтобы Эшли снова простила тебя!"
    m "Джо, может быть, можно как-то без этого?"
    joe "Нет, [monica_pub_name], я действительно хочу увидеть твою попку."
    joe "Это мое самое большое желание сейчас!"
    joe "И, пока оно не исполнится, я не смогу ничего сделать с Эшли."
    menu:
        "Показать Джо свою голую попу.": #corruption
            pass
        "Отказаться.":
            m "Нет, Джо!"
    m "Джо, но только никаких прикосновений, тебе ясно?!"
    joe "Конечно, [monica_pub_name], я только посмотрю!"
    m "И никаких дополнительных условий, ясно?!"
    joe "Да, [monica_pub_name], я обещаю!"
    mt "Дьявол!"
    mt "Мне так стыдно делать это..."
    mt "Показывать свой голый зад в какой-то shiny hole посреди трущоб..."
    mt "Это какой-то сон..."
    joe "[monica_pub_name], я жду!"
    joe "Скорее, показывай свою попку!"
    m "!!!"
    # Моника показывает голую попу
    joe "[monica_pub_name], можно потрогать?!"
    # Моника одевается
    m "Только попробуй, Джо!"
    m "И я сломаю тебе пальцы!"
    return

label ep27_dialogues7_pub13:
# Просит раздеться и забраться на стол
    joe "[monica_pub_name], ты уже украла столько денег..."
    joe "И Эшли уже начинает что-то подозревать."
    joe "Обычно... Знаешь..."
    joe "Больше денег я люблю только шлюх..."
    joe "И Эшли знает об этом и очень ревнует."
    mt "Я не шлюха!!!"
    joe "Если честно, она так следит за мной, что уже очень давно я не видел другой голой женщины."
    m "И что же ты хочешь на этот раз, Джо?"
    joe "Я хочу чтобы ты разделась, [monica_pub_name]."
    joe "Полностью."
    m "Это исключено, Джо!"
    joe "Тогда извини, для меня это слишком большой риск."
    joe "Ты можешь идти. Если Эшли догадается, она прибьет меня."
    menu:
        "Уйти.":
            m "Твоя жена тоже может быть голой женщиной, Джо!"
            m "Смотри лучше на нее!"
            return False
        "Предложить компромисс.":
            pass
    m "Джо..."
    m "Мне действительно надо снова работать здесь."
    m "Может быть мне не надо раздеваться полностью?"
    joe "Хорошо, [monica_pub_name]."
    joe "Ты можешь раздеться наполовину и встать на этот стол."
    joe "И принять пару сексуальных поз."
    joe "Это будет как приватный танец."
    m "Ладно, Джо..."
    m "Сейчас я сниму верх..."
    joe "Нет, [monica_pub_name]!"
    joe "Я хочу чтобы ты сняла низ!"
    m "ЧТОООО?!"
    joe "[monica_pub_name], твоя грудь прекрасна!"
    joe "Но от твоей попки я просто без ума!"
    joe "Это мое условие!"
    joe "Если ты не согласна, то можешь идти и искать $ 500!"
    m "!!!"
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            m "Нет, Джо!"
            return False
    mt "Дьявол!"
    mt "До чего ты докатилась, Моника!"
    mt "..."
    mt "Мне не стоит даже в мыслях называть себя Моникой..."
    mt "Вдруг я проговорюсь..."
    mt "Ведь меня здесь знают под именем [monica_pub_name]..."
    mt "Черт! Мо... [monica_pub_name]!"
    mt "Закрой глаза и сделай это..."

    # Моника снимает низ и залезает на стол
    joe "О да, [monica_pub_name]!"
    joe "Покажи мне свою попу, Да!"
    # достает член
    joe "Да, выгнись посильнее, да!"
    joe "Аааааххх!"
    m "ЧТО?!"
    m "Ты там что, дрочишь на меня, Джо?!"
    joe "Ааааххх! Ааааааааххх!"
    m "Дьявол!!!"
    m "Все, шоу закончено!"
    m "Иди к Эшли, немедленно!"
    mt "Извращенец!!!"
    return


label ep27_dialogues7_pub14:
# Затем Джо говорит Эшли что та самая красивая и любимая и что он поговорил с Мэрилин и ей кажется надо дать ей еще шанс.
# Что он ручается за нее. Эшли тает и говорит что так уж и быть.
# Говорит Монике что та снова может работать, но чтобы не испытывала ее терпения.
    joe "Эшли, ты моя самая красивая и любимая жена!"
    ashley "И, Джо? Что тебе снова понадобилось от меня?"
    joe "Я поговорил с [monica_pub_name] и, мне кажется, надо дать ей еще шанс."
    joe "Я ручаюсь за нее, Эшли."
    joe "И..."
    joe "И я тебя очень сильно люблю..."
    # обнимает
    ashley "Ох, Джо..."
    ashley "Ну ладно... Хорошо..."
    # поворачивается к Монике
    ashley "[monica_pub_name], ты можешь снова работать."
    ashley "Но не испытывай моего терпения!"
    return

label ep27_dialogues7_pub14a:
# Если подходит к Эшли:
# Моника говорит что у нее нет таких денег и она бы не хотела танцевать голой у всех на виду.
# Может быть есть еще какие-то варианты.
# Эшли отвечает, что для такой аппетитной попки у нее есть один вариант.
# Моника напряженно смотрит
# Эшли говорит Мэрилин, чтобы она дождалась пока Джо отвернется и шла в подсобку за Эшли
    m "Эшли... У меня нет таких денег."
    m "И я бы..."
    m "Я бы не хотела танцевать голой у всех на виду..."
    m "Может быть есть еще какие-то варианты?"
    ashley "Вообще-то, [monica_pub_name], у обладательницы такой раскошной попки есть один вариант попросить прощения у меня."  # подмигивает
    m "..." # Моника напряженно смотрит
    ashley "[monica_pub_name], если хочешь, чтобы тебя простили, дождись пока Джо будет занят"
    ashley "И иди в служебную комнату за мной."

# Выбор:
# Подождать пока Джо отвернется и идти в подсобку за Эшли
# Уйти
# Если идет, вызывается меню со сценами с Эшли (открываются последовательно)
    menu:
        "Подождать пока Джо будет занят и идти в подсобку за Эшли.":
            pass
        "Подождать пока Джо будет занят и идти в подсобку за Эшли. (в следующем обновлении) (diabled)":
            pass
        "Уйти.":
            return False
    return

label ep27_dialogues7_pub15:
# Эшли
# Просит поцеловаться (хватает Монику за зад, под джинсы)
    m "Я пришла, Эшли..."
    ashley "О, [monica_pub_name]!"
    ashley "Иди ко мне!"
    ashley "Я ждала когда ты что-нибудь натворишь..."
    ashley "Иди ко мне! Иди я поцелую тебя!"
    menu:
        "Позволить Эшли поцеловать себя.": #corruption
            pass
        "Отказать.":
            m "Нет, Эшли! Я не способна на такое!"
            return False
    # Эшли целует Монику
    ashley "Ммммм..."
    mt "!!!"
    ashley "Ммммм... Моя конфетка... Мммммм..."
    # Эшли пропускает руку Монике под джинсы сзади
    #sound
    mt "!!!"
    ashley "Ах, эта сладкая попка... Мммммм..."
    ashley "Какая она упругая... Мммммм...."
    # Моника отстраняется
    m "Эшли, пожалуйста, хватит!"
    ashley "[monica_pub_name], ты получила прощение на этот раз..."
    ashley "Я подожду, пока ты снова что-нибудь не напроказничаешь..."
    mt "!!!"
    return

label ep27_dialogues7_pub16:
    m "Я пришла, Эшли..."
    ashley "О, [monica_pub_name]!"
    ashley "Иди ко мне!"
    ashley "Дай я потрогаю твою киску!"
    menu:
        "Позволить Эшли потрогать свою киску.": #corruption
            pass
        "Отказать.":
            m "Нет, Эшли! Я не способна на такое!"
            return False
    mt "О Боже!"
    mt "Что эта Эшли собралась делать?!"
    # Эшли запускает руку Монике в джинсы и трогает киску
    ashley "Да, [monica_pub_name]!"
    ashley "Чувствуешь меня?"
    m "Ахххх!"
    ashley "Наслаждаешься этим?"
    m "Ахххх!"
    ashley "Почуствуй меня, [monica_pub_name]!"
    ashley "Если захочешь, это можно сделать по другому."
    m "ААА! Ааааахх!"
    ashley "Ах, какая ты вкусная, [monica_pub_name]!"

    # Моника отстраняется
    m "Погоди, Эшли!"
    m "Я..."
    m "На меня что-то начинает накатывать..."
    m "Погоди, я боюсь этого..."
    ashley "Это оргазм, моя [monica_pub_name]."
    ashley "Ты разве не любишь это?"
    m "Я... Я не совсем знаю что это такое и..."
    ashley "Ах, иди ко мне, [monica_pub_name], я тебе покажу!"
    m "Нет, Эшли! Мне..."
    m "Мне надо идти!"
    return

# Засовывает руку Монике спереди в джинсы, и трогает там, что-то говоря, какая Мерилин вкусная. Моника ахает и еле сдерживается.
# Просит Мэрилин спустить ее джинсы, чтобы посмотреть на ее попку, затем задирает юбку и просит потереться своей попой о Мэрилин

label ep27_dialogues7_pub17:
    m "Эшли, я пришла."
    m "Только пожалуйста, давай ты не будешь трогать мою киску..."
    m "По крайней мере не в этот раз..."
    ashley "Хорошо, [monica_pub_name]."
    ashley "Снимай свой низ, я хочу потереться о твою сладкую попку!"
    menu:
        "Сделать то о чем просит Эшли.":
            pass
        "Отказаться.":
            m "Нет, Эшли! Я не способна на такое!"
            return False

    m "Эшли, и что будет дальше?"
    ashley "Не бойся, [monica_pub_name], снимай!"
    m "Ладно..."
    # Моника снимает низ
    # Эшли поднимает юбку
    ashley "Потрись о мою попку своей и я прощу тебя!"
    m "ЧТО??!"
    ashley "Давай, [monica_pub_name]!"
    ashley "Я хочу почувствовать твою сладкую попку!"
    ashley "Иначе я тебя не прощу!"
    menu:
        "Сделать то о чем просит Эшли.":
            pass
        "Отказаться.":
            m "Нет, Эшли! Я не способна на такое!"
            return False

    # Моника трется своей попой о попу Эшли.
    ashley "Да, [monica_pub_name]!"
    ashley "Какая у тебя упругая и приятная попка!"
    ashley "Это просто персик!"
    ashley "Ах! Как здорово!"
    ashley "Ах! Ах! Да!"
    ashley "Дааааааа!!!" # Эшли кончает
    return

label ep27_dialogues7_pub18:
# Эшли говорит Джо что подумала и решила дать Мэрилин еще один шанс
# Говорит Монике что та может снова работать, но чтобы не испытывала ее терпения.
    ashley "Джо, я подумала и решила дать [monica_pub_name] еще один шанс."
    joe "Правда, Эшли? Рад это слышать!"
    ashley "[monica_pub_name], ты можешь снова работать."
    ashley "Но не испытывай моего терпения, иначе ты снова будешь наказана." # Подмигивает
    mt "!!!"
    return



























#
