# После перехода уровня Барди и Бетти к тому, что Моника ходит дома без трусиков,
# появляется возможность придти к Барди вечером, когда он сидит в кабинете.
# до этого показывается сцена того, как Барди расслабляется перед журналом Моники и комментирует процесс
# Также делает замечание по поводу груди Моники на журнале и думает что упустил этот момент из виду.

label ep26_dialogues1_bardie1:
    # Моника случайно заходит к Барди (первый раз)

    # Сцена Барди с журналом
    # Старт, пара кадров
    #video
    bardie "Аххх! Ахххх!!!"
    bardie "Моника Бафетт..."
    bardie "Аххх! Ахххх!!!"
    bardie "Моя гувернантка..."
    bardie "Аххх!"
    bardie "Я молодец!"
    bardie "Я хороший хозяин, Аххх!"
    # video end
    # Барди кончает
    bardie "АХХХХХХ!!!"
    bardie "..."
    bardie "Ее сиськи..."
    bardie "Интересно, они настоящие или нет..."
    bardie "Как это я упустил их из виду..."
    bardie "У меня все еще недостаточный контроль над ней..."
    bardie "Мне нужно увидеть ее сиськи... И даже больше..."
    bardie "И мне нужна еще фотография, чтобы дрочить на нее."
    bardie "Этот журнал уже надоел мне..."
    # хитро прищуриваясь
    bardie "Может быть есть еще выпуски?"
    bardie "Надо будет спросить у гувернантки..."
    bardie "И, было бы неплохо не только дрочить на нее, но и делать нечто более..."
    bardie "Хотя я ее, пока, немного побаиваюсь..."
    bardie "Все-таки она Моника Бакфетт, но, почему-то боится штрафа..."
    bardie "Может быть она не настоящая Моника Бакфетт, потому и боится?"
    bardie "И Бетти..."
    bardie "Эта мачеха, хоть и соблюдает правила дома, но, все-же, действует мне на нервы."
    bardie "Я мечтаю не только смотреть ей под юбку, но и, когда-нибудь, трахнуть ее!"
    bardie "Вокруг ходит столько целей, а я все еще девственник!"
    bardie "Это ненормально! Я что, какой-то нудачник?!"


    # Моника заходит. Журнал весь в сперме

    m "Что... Что ты делаешь??"
    m "Это... Это Я?!"
    m "Это мой журнал! Мой!"
    m "Что делаешь с ним?!"
    bardie "Я дрочу на него, я же говорил тебе."
    m "Я... Не смей делать этого!"
    m "Верни его мне!"
    bardie "Я верну тебе его только если ты принесешь мне другой!"
    bardie "Новый выпуск!"
    m "Нет новых выпусков, я не работаю там!"
    m "Я торчу здесь! И меня это бесит!"
    bardie "Ты здесь работаешь! И я твой хозяин!"
    m "!!!"
    # Моника уходит
    return

label ep26_dialogues1_bardie1a:
    mt "Эта мелюзга достала меня!"
    mt "Как он смеет делать это... С моим журналом!"
    mt "На котором изображена Я!"
    mt "..."
    mt "У этого маленького засранца нет никакого стыда!"
    mt "И мозгов, кстати, тоже у него нет!"
    mt "Хм... Может быть мне как-то использовать его, раз уж приходится соблюдать его дурацкие капризы?"
    mt "Он шантажирует также и Бетти."
    mt "Может быть я могу использовать это, чтобы, хотя бы, питаться здесь?"
    return

label ep26_dialogues1_bardie2:
    # Моника прходит к Барди спросить о еде в доме (второй приход)
# Моника приходит к Барди и говорит что, учитывая то, что она ведет себя хорошо, может быть
# Барди скажет Бетти, чтобы та кормила прислугу в доме.
# Барди спрашивает хорошая-ли Моника гувернантка, что просит о таком?
# Моника отвечает что хорошая (либо не отвечает)
# Барди просит продемострировать что Моника соблюдает правила дома.
    m "Барди..."
    bardie "Да, гувернантка?"
    m "У меня разговор к тебе..."
    bardie "Я тебя слушаю."
    m "Барди, я ведь хорошо себя веду, так ведь?"
    bardie "Да, гувернантка... Обычно ты соблюдаешь правила дома..."
    m "Барди, если ты доволен мной, то..."
    m "То, может быть, Я заслуживаю того, чтобы меня кормили в этом доме."
    m "Может быть ты скажешь Бетти об этом?"
    # Щурится
    m "Ты ведь тут самый главный? Правда?"

    bardie "О таком может просить только хорошая гувернантка."
    bardie "Ты хорошая гувернантка, Моника?"
    menu:
        "Да, я хорошая гувернантка...":
            pass
        "Уйти.":
            return False

    m "Да, я хорошая гувернантка..."
    bardie "Хорошо, покажи, что ты соблюдаешь правила дома!"

# Моника соглашается либо нет.
# Если соглашается и у нее надеты трусики, то Барди злится и устраивает порку.
    if monicaUnder != "Nude":
        mt "Черт! У меня надеты трусики!"
        mt "Мне лучше не показывать их этому сопляку!"
    menu:
        "Задрать юбку.":
            pass
        "Попросить выйти.":
            m "Барди, конечно я соблюдаю правила."
            m "Я вспомнила об одном важном деле!"
            m "Мне надо отлучиться и я вернусь сюда!"
            return False

    # Моника показывает
    if monicaUnder != "Nude":
        # Моника показывает
        bardie "Нерадивая гувернантка!"
        bardie "Ты не соблюдаешь правила дома!"
        bardie "Следуй к себе в подвал для прохождения наказания!"
        m "!!!"
        # идет наказание
        return 1


# Тогда Барди говорит чтобы та показала свою грудь.
# Моника может это делать, либо нет. Если нет, то Барди злится и устраивает порку, но грудь Моника не показывает.
    bardie "Хорошо."
    bardie "Теперь покажи свои сиськи!"
    m "Мы так не договаривались!"
    m "Я не собираюсь этого делать!"
    bardie "Ты моя игрушка и принадлежишь мне!"
    m "Ах ты мелюзга!"
    m "Я не буду показывать тебе свою грудь!"
    bardie "Ты решила не подчиняться приказам хозяина дома? Я правильно понял?"
    menu:
        "Подчиниться и показать грудь.":
            pass
        "Не показывать грудь!":
            m "Я и так хожу с голой задницей по дому целыми днями!"
            m "Разве тебе этого мало?!"
            bardie "Нерадивая гувернантка!"
            bardie "Ты не слушаешься хозяина дома!"
            bardie "Следуй к себе в подвал для прохождения наказания!"
            return 2

    # Моника показывает грудь

    # Барди берет журнал и держит его рядом, сравнивая грудь
    bardie "Да, у тебя такая же грудь."
    bardie "Ты действительно похожа не нее."
    m "ЭТО И ЕСТЬ Я!"
    mt "Черт! Зачем я это сказала?!"

# Барди задумывается, улыбается и говорит что хозяин дома подумает, пусть Моника приходит завтра.
    bardie "Хорошо, хозяин дома подумает." # разглядывая грудь
    bardie "Гувернантка, приходи завтра."
    bardie "Хозяин скажет тебе о своем решении."
    # Моника закрывает грудь
    m "!!!"

#    bardie "Да, и еще!"
    return

label ep26_dialogues1_bardie3a:
    # Моника просто вышла и не хочет ничего показывать
    mt "Я не хочу ничего показывать этому сопляку."
    mt "Мне надоели эти его игры..."
    return
label ep26_dialogues1_bardie3:
    # Моника пытается зайти к Барди в этот же день, а также при выходе из комнаты Барди
    mt "Эта мелюзга сказала приходить завтра."
    mt "Он, видите-ли, подумает!"
    mt "Ненавижу!"
    mt "Мне в своем же доме надо выпрашивать еду! О УЖАС!!!"
    return

label ep26_dialogues1_bardie4:
# На след. день Моника приходит к Барди и спрашивает подумал-ли он?
# Барди отвечает что готов сделать величественный жест ради хорошей гувернантки, которая хорошо себя ведет.
# И сказать Бетти, чтобы она кормила Монику
# Переспрашивает хорошая-ли гувернантка Моника?
    m "Барди, ты подумал насчет того, чтобы я получала заслуженную еду в этом доме?!"
    bardie "Да, гувернантка."
    bardie "Я подумал и решил что готов сделать величественный жест ради хорошей гувернантки."
    bardie "Которая хорошо себя ведет..."
    mt "!!!"
    bardie "И я скажу Бетти, чтобы она кормила гувернантку."
    bardie "Но только хорошую гувернантку!"
    bardie "Ты ведь хорошая гувернантка, Моника?"

    menu:
        "Да...":
            pass
        "Я... Подумаю о том какая Я...":
            m "Я еще не решила..."
            bardie "Когда будешь уверена, приходи!"
            return False

# Моника отвечает что да.
    m "Да..."

# Барди говорит чтобы та сделала titjob. Моника в шоке и спрашивает не рановато-ли Барди думать о таких вещах.
# Барди отвечает что он уже достаточно большой. (мне уже 18, либо можно поменять число)
    bardie "Хорошо, я много раз кончал на твои сиськи на журнале."
    bardie "Теперь я хочу сделать это прямо на них."
    m "ЧТО?!"
    m "Барди, я понимаю, что ты уже интересуешься девушками."
    m "Придумываешь разные глупые игры. У тебя играют гормоны."
    m "Но тебе не кажется, что тебе рановато думать о чем-то большем?!"
    m "Тем более в отношении меня!"

    bardie "Я не маленький! Я большой!"
    bardie "Мне уже (введите число)"
    help "Внося изменения в игру, Вы берете на себя ответственность."
    help "Вы уверены в этом?"


# Барди ложится на кровать и достает член.
    bardie "..."
# Моника в шоке смотрит на это.
    m "!!!"
# Барди спрашивает чего гувернантка ждет? Она должна выполнять обязанности по дому, в число которых входит
# то, чтобы хозяин дома оставался доволен.
    bardie "Ну?!"
    bardie "И чего же гувернантка ждет?"
    bardie "Хорошая гувернантка должна выполнять обязанности по дому."
    bardie "Соблюдать везде чистоту."
    bardie "Это место надо протереть от пыли."
    bardie "И оно слишком чувствительное, поэтому это надо сделать твоими сиськами!"
    m "!!!"

# Моника злая, смотрит и думает.
    m "Я уверена в том, что это место протирается регулярно и без меня!"
# Барди говорит что если гувернантка будет хорошей, то ее в этом доме будут кормить.
    bardie "Хорошая гувернантка должна выполнять это работу."
    bardie "И, если гувернантка будет хорошей, то ее в этом доме будут кормить."

# Моника принимает решение
    mt "Что же мне делать?!"
    mt "Ведь я не буду трогать своей изысканной грудью член этого Барди?"
    mt "С другой стороны, я в шаге от того, чтобы нормально питаться."
    mt "В своем же доме!"
    bardie "А плохую гувернантку может ждать наказание..."
    mt "Что же мне делать?!"
    menu:
        "Сделать это...":
            pass
        "Я... Пока не готова для этого...":
            # Говорит что она пока не готова для этого (corruption)
            m "Я... Пока не готова для этого..."
            bardie "Тогда иди и готовься!"
            bardie "Иначе ты станешь плохой гувернанткой!"
            return False
# Либо соглашается и делает titjob
    m "Я не умею делать это..."
    bardie "Я тоже не умею делать это. Но не думаю что это сложно!"
    bardie "Вынь свои сиськи и положи их на мой член!"
    m "..."
    bardie "Вот так. А теперь начинай двигать ими вверх и вниз!"
# Барди говорит хорошая гувернантка и тд
    bardie "Хорошая гувернантка..."
    bardie "Хорошая..."
    bardie "Протирай как следует, это твоя работа..."
# Когда заканчивают, Барди говорит Монике придти завтра, когда он уладит обязанности хозяина дома и
# выдаст необходимые распоряжения Бетти

    # Барди кончает на грудь Монике
    bardie "Оооооох!!!"
    bardie "Хорошая гувернантка!"
    bardie "Приходи завтра."
    bardie "Я улажу обязанности хозяина дома и выдам необходимые распоряжения Бетти!"
    m "!!!"

# Моника уходит
    return

label ep26_dialogues1_bardie5:
# Приходит на след. день и спрашивает зло: ну что?! достаточно я сделала для того чтобы меня кормили в этом
#гребаном доме?!
#(мой дом!!!)
    m "Ну что, Барди!"
    m "Я достаточно сделала для того, чтобы меня кормили в этом гребаном доме?!"
    mt "В моем доме! В моем!"

# Барди отвечает что договорился с Бетии, но она поставила одно условие.
# Моника зло спрашивает какое еще условие? Разве недостаточно того что Моника убирается каждый день?!
    bardie "Да, гувернантка. Я договорился с Бетти."
    m "..." # Моника довольна
    bardie "Но она поставила одно условие."
    m "Какое еще условие?!"
    m "Разве недостаточно того, что я убираюсь здесь каждый день?!"
# Барди говорит что Моника может питаться на кухне когда захочет, но должна делать это.. с голой грудью.
# Моника в бешенстве, ЧТО?!?! И ТЫ ХОЧЕШЬ СКАЗАТЬ ЧТО ЭТО УСЛОВИЕ ПОСТАВИЛА БЕТТИ?!
# Я УВЕРЕНА ЧТО ЭТО СНОВА ТВОИ ПРОИСКИ, МАЛЯВКА!!!
# ТЫ НЕ МОЖЕШЬ ТРЕБОВАТЬ ОТ МЕНЯ ТАКОГО!!!
# ТЫ ВЕДЬ ЗНАЕШЬ КТО Я ТАКАЯ! МНЕ И ТАК ПРИХОДИТСЯ ХОДИТЬ ЗДЕСЬ В ЭТОЙ ДУРАЦКОЙ УНИФОРМЕ!
    bardie "Гувернантка может питаться когда захочет."
    bardie "Но должна делать это на кухне."
    bardie "И делать это... с голыми сиськами!"
    m "ЧТО?!?!"
    m "И ТЫ ХОЧЕШЬ СКАЗАТЬ ЧТО ЭТО УСЛОВИЕ ПОСТАВИЛА БЕТТИ?!"
    m "Я УВЕРЕНА ЧТО ЭТО СНОВА ТВОИ ПРОИСКИ, МАЛЯВКА!!!"
    m "ТЫ НЕ МОЖЕШЬ ТРЕБОВАТЬ ОТ МЕНЯ ТАКОГО!!!"
    m "ТЫ ВЕДЬ ЗНАЕШЬ КТО Я ТАКАЯ!"
    m "МНЕ И ТАК ПРИХОДИТСЯ ХОДИТЬ ЗДЕСЬ В ЭТОЙ ДУРАЦКОЙ УНИФОРМЕ!"

# Барди спрашивает что в униформе без трусиков?
    bardie "В униформе без трусиков."
# Моника переспрашивает: ЧТО?!
    m "ЧТО?!"
# Барди говорит что ты ведь соблюдаешь правила дома? В униформе без трусиков.
# ПРИЧЕМ ЗДЕСЬ ЭТО?! Я ГОВОРЮ ТЕБЕ ПРО ТО ЧТО ТЫ ЗНАЕШЬ КТО Я ТАКАЯ!
# КАК ТЫ СМЕЕШЬ, МАЛЯВКА, ТРЕБОВАТЬ ОТ МЕНЯ ЭТО?!
    bardie "Ты ведь соблюдаешь правила дома?"
    bardie "Ты ходишь в униформе без трусиков."
    m "ПРИЧЕМ ЗДЕСЬ ЭТО?!"
    m "Я ГОВОРЮ ТЕБЕ ПРО ТО ЧТО ТЫ ЗНАЕШЬ КТО Я ТАКАЯ!"
    m "КАК ТЫ СМЕЕШЬ, МАЛЯВКА, ТРЕБОВАТЬ ОТ МЕНЯ ЭТО?!"
# Барди говорит: что-то мне не нравится тон гувернантки.
# Покажи что ты соблюдаешь правила дома.
# Моника злится, и бесится!
    bardie "Что-то мне не нравится тон, на который перешла гувернантка."
    bardie "Гувернантка соблюдает правила дома?"
    m "!!!"
# ТЫ МЕНЯ СЛЫШИШЬ?!
# Барди отвечает чтобы она показала что соблюдает правила дома, иначе ее ждет наказание как плохую гувернантку.
# Моника зло смотрит на Барди
# Барди: Ну?!
    m "ТЫ МЕНЯ СЛЫШИШЬ?!"
    bardie "Немедленно покажи что соблюдаешь правила дома, иначе тебя ждет наказание как плохую гувернантку."
    m "!!!"
    bardie "Ну?!"
# Моника может показать, либо Барди наказывает ее
# Если Моника в трусиках, то Барди наказывает ее также
# Если Моника показывает:
    menu:
        "Задрать юбку.":
            pass

    # Моника показывает
    if monicaUnder != "Nude":
        # Моника показывает
        bardie "Нерадивая гувернантка!"
        bardie "Ты не соблюдаешь правила дома!"
        bardie "Следуй к себе в подвал для прохождения наказания!"
        m "!!!"
        # идет наказание
        return 1

# Я соблюдаю правила этого дома (злится!!)
# Барди отвечает: Хорошая гувернантка
    m "Я соблюдаю правила этого дома..."
    bardie "Хорошая гувернантка."
# Ты поняла правила питания в доме?
# Моника отвечает что да, я поняла. Но я не собираюсь питаться в доме на таких условиях.
# Барди отвечает что как гувернантка пожелает, но он бы советовал пользоваться благосклонностью
# хозяина дома, пока он добрый.
# Моника зло смотрит и спрашивает. Может-ли она идти?
# Барди говорит что да, она может идти, если только не хочет снова удовлетворить хозяина.
# Моника говорит что нет, спасибо!
    bardie "Ты поняла правила питания в доме?"
    m "Да, я поняла."
    m "Но я не собираюсь питаться в доме на таких условиях..."
    bardie "Как гувернантка пожелает..."
    bardie "Но я бы советовал ей пользоваться благосклонностью хозяина дома..."
    bardie "Пока он добрый..."
    m "Я могу идти?!"
    bardie  "Да, ты можешь идти."
    bardie "Если, конечно, не хочешь снова удовлетворить хозяина."
    m "Нет, спасибо!"
    return

label ep26_dialogues1_bardie5a:
    # Моника размышляет, выйдя из команаты Барди
    mt "Не могу поверить!"
    mt "Эта малявка из всего пытается сделать свою извращенную игру!"
    mt "Мелкий домогатель!"
    mt "Неужели он действительно считает что я буду есть на кухне, обнажив свою грудь?!"
    mt "Наивный дурачок!"
    return

# Моника теперь может заходить на кухню.
label ep26_dialogues1_bardie6:
    # Моника заходит на кухню первый раз (либо любой раз, пока Моника еще не показывала грудь)

# Если Моника заходит так, то прибегает Бетти и говорит Монике чтобы та убиралась с кухни!
# Что ей вообще не нужны проститутки в доме и что ей уже надоело присматривать за дурной гувернанткой
# Которая так и норовит нарушить дисциплину!
    betty "Моника, гувернантка!"
    betty "Что ты делаешь здесь!"
    betty "Я запретила тебе заходить на кухню!"
    betty "Быстро убирайся отсюда!"
    betty "И вообще... Мне не нужны проститутки в доме!"
    betty "И мне надоело присматривать за дурной гувернанткой, которая так и норовит нарушить дисциплину!"
# Моника спрашивает: есть-ли правила, которые позволяют ей питаться здесь?
# Бетти смущается и говорит что есть кое-какое правило и гувернантка сама про него знает. (злится)
# Говорит Монике чтобы та выметалась с кухни
    m "Миссис Робертс..."
    m "Есть-ли правила, которые позволяют мне питаться здесь?"
    betty "..."
    m "???"
    betty "!!!"
    betty "Есть кое-какое правило... И ты, гувернантка, сама знаешь про него..."
    betty "А сейчас, выметайся с кухни!"
# Моника делает выбор:
# Уйти или Оголить грудь (corruption)
    menu:
        "Оголить грудь...":
            pass
        "Уйти...":
            return False
# Если оголяет: А так?
# Если оголяет первый раз, то Моника про себя думает о том что же она творит, но, с другой стороны.
# Никто кроме Бетти этого не видит и это лучше, чем разносить флаеры за еду или что-то еще похуже.
    mt "Моника, что ты творишь?"
    mt "Неужели ты пойдешь на это?"
    mt "С другой стороны... Никто кроме Бетти этого не видит"
    mt "И это лучше, чем разносить флаеры за еду или делать что-то еще похуже..."
    #fade
    m "А так?"

# Бетти злится и говорит что у гувернантки нет никакого стыда.
# И чтобы та убиралась отсюда.
    betty "!!!"
    m "..." # Моника стервозно улыбается
    betty "Гувернантка, у тебя нет никакого стыда!"
    betty "Немедленно убирайся отсюда!"
# Моника спрашивает: Вы уверены, Миссис Робертс? Что я должна выйти отсюда?
# Бетти злится и говорит чтобы та садилась за стол.
    m "Вы уверены, Миссис Робертс!"
    m "Вы уверены что я должна выйти отсюда?"
    betty "!!!"
    betty "Садись за стол, сейчас подам тебе..."
# Моника садится.
# Бетти подает еду и говорит что если Ральф увидит ее в таком виде, то ей уже ничего не поможет.
# Даже мелкий засранец, с которым Моника спелась.
    betty "И не вздумай в таком виде шляться по дому!"
    betty "Если Ральф увидит тебя в таком виде, то я вышвырну тебя!"
    betty "И тебе никто не поможет!"
    betty "Даже мелкий засранец Барди, с которым ты спелась!"

    # Моника ест
    mt "Мммм... Наконец-то я ем вкусную еду..."
    mt "В своем доме..."

    #
    mt "Мой дом... Моя любимая кухня..."
    mt "Все не так уж плохо..."
    mt "Это только первые шаги..."
    mt "Скоро дом будет снова мой..."

    #
    mt "Ммм... Я кушаю на своей любимой кухне."
    mt "А Бетти прислуживает мне..."
    mt "Так мне нравится намного больше..."


    # Моника поела
    m "Благодарю Вас, Миссис Робертс."
    m "Я поела."
    betty "!!!"
    return

label ep26_dialogues1_bardie7:
    # Моника заходит на кухню регулярно
    # Моника делает выбор:
    # Уйти или Оголить грудь (corruption)
    menu:
        "Оголить грудь...":
            pass
        "Не оголять грудь...":
            betty "Моника, гувернантка!"
            betty "Что ты делаешь здесь!"
            betty "Я запретила тебе заходить на кухню!"
            betty "Быстро убирайся отсюда!"
            betty "И вообще... Мне не нужны проститутки в доме!"
            betty "И мне надоело присматривать за дурной гувернанткой, которая так и норовит нарушить дисциплину!"
            return 0


    betty "!!!"
    m "..." # Моника стервозно улыбается
    betty "Гувернантка, у тебя нет никакого стыда!"
    betty "Немедленно убирайся отсюда!"
    m "Вы уверены, Миссис Робертс!"
    m "Вы уверены что я должна выйти отсюда?"
    # На каждое 5-ое посещение дома, Бетти начинает козлить и идет переход на ep26_dialogues1_bardie8
    call ep26_dialogues1_bardie8()
    return 1

    betty "!!!"
    betty "Садись за стол, сейчас подам тебе..."

# Если Бетти ведет себя хорошо, то:

# Бетти подает еду и говорит приятного аппетита
# Моника язвительно смотрит и просит что-то из еды еще или типа того
# Моника думает про то, что наконец-то ест в собственном доме, что это уже прогресс и что она вернет его назад.
    betty "Приятного аппетита, гувернантка..."

    #
    m "Миссис Робертс. Пожалуйста, подайте мне другие приборы."
    m "Эти недостаточно хорошо вымыты."
    betty "!!!"

    #
    m "Миссис Робертс. Пожалуйста, подогрейте еду."
    m "Она недостаточно горячая."
    betty "!!!"

    #
    m "Миссис Робертс. Вы вкусно готовите."
    m "Это похвально."
    betty "!!!"
    #

# Если Бетти ведет себя плохо.
    betty "И не вздумай в таком виде шляться по дому!"
    betty "Если Ральф увидит тебя в таком виде, то я вышвырну тебя!"
    betty "И тебе никто не поможет!"
    betty "Даже мелкий засранец Барди, с которым ты спелась!"
    m "Вы уверены что так следует отзываться о хозяине дома?"
    betty "Это не твое дело, проститутка!"

#

    # Моника ест
    mt "Мммм... Наконец-то я ем вкусную еду..."
    mt "В своем доме..."

    #
    mt "Мой дом... Моя любимая кухня..."
    mt "Все не так уж плохо..."
    mt "Это только первые шаги..."
    mt "Скоро дом будет снова мой..."

    #
    mt "Ммм... Я кушаю на своей любимой кухне."
    mt "А Бетти прислуживает мне..."
    mt "Так мне нравится намного больше..."

    # Моника поела
    m "Благодарю Вас, Миссис Робертс."
    m "Я поела."
    betty "!!!"
    return 2

label ep26_dialogues1_bardie8:
# Через 5 посещений кухни, Бетти заявляет что правило не работает и чтобы нерадивая гувернантка убиралась отсюда.
    betty "Это дурацкое правило больше не работает!"
    betty "Я не собираюсь больше такое терпеть!"
    betty "Убирайся отсюда, нерадивая гувернантка!"
    betty "Пока я не вышвырнула тебя из дома на улицу!"

# Монике приходится уходить с голой грудью
    m "!!!"
    return

label ep26_dialogues1_bardie8a:
    mt "Бетти вконец обнаглела!"
    mt "Мне стоит пожаловаться на нее Барди!"
    return

label ep26_dialogues1_bardie9:

# Моника приходит к Барди и спрашивает почему Бетти ее больше не кормит?
    m "Барди!"
    m "Бетти не хочет меня кормить!"
    m "Мы договаривались с тобой!"
    bardie "Если ты хочешь обратиться к хозяину, то делай это как подобает хорошей гувернантке!"
    m "Что ты имеешь ввиду?!"
    bardie "Вынь свои сиськи и зайди ко мне снова!"
    return
label ep26_dialogues1_bardie9a:
    # Моника выходит
    mt "Эта мелюзга продолжает издеваться надо мной!"
    mt "Может к черту это все?"
    mt "Я найду где мне есть!"
    return
label ep26_dialogues1_bardie10:
    menu:
        "Оголить грудь.":
            pass
        "Не оголять грудь":
            call ep26_dialogues1_bardie9()
            return 0

    m "Барди!"
    bardie "Да, гувернантка. Твой хозяин слушает тебя."
    m "Бетти не хочет меня кормить!"
    m "Мы договаривались с тобой!"
    bardie "Тихо, гувернантка, не кричи."
    bardie "Ты хочешь сказать что кто-то не соблюдает правила дома?"
    m "Да! Бетти!"
    m "Она не соблюдает правила!"
    m "Я прихожу к ней как ты велел мне, но она не хочет кормить меня!"

# Барди ложится на кровать и достает член.
# Барди ехидно отвечает, что Моника забыла удовлетворить хозяина дома и, если она хочет и дальше продолжать
# бесплатно питаться, то должна это исправить.
    bardie "Бетти соблюдает правила."
    m "???"
    bardie "Гувернантка забыла удовлетворить хозяина дома."
    bardie "И, если гувернантка хочет и дальше продолжать бесплатно питаться."
    bardie "То она должна это исправить."

    m "!!!"
# Моника злится. У нее есть выбор:
# Сделать Барди titjob или уйти
    menu:
        "Удовлетворить Барди.":
            pass
        "Уйти.":
            m "Я... Подумаю..."
            return 1


    bardie "Хорошая гувернантка..."
    bardie "Хорошая..."
    bardie "Протирай как следует, это твоя работа..."

    # Кончает
    bardie "Оооооох!!!"
    bardie "Хорошая гувернантка!"
    bardie "Теперь ты снова можешь питаться в этом доме."
    m "!!!"
    menu:
        "Пожаловаться на Бетти.":
            pass
        "Уйти.":
            return 2

    m "Барди."
    m "Между прочим, Бетти часто зарывается."
    m "Она называет тебя засранцем."
    m "И, я думаю, не соблюдает правила дома."
    m "Я видела в прачечной, что кто-то трогает трусики."
    m "Уверена, это Бетти одевает их в доме."
    bardie "Ты уверена в этом, Моника?"
    m "Да, Барди."
    m "Я уверена в этом."

    bardie "Хорошо. Позови Бетти сюда."

    help "Позвать Бетти к Барди." # setobjective

    return

label ep26_dialogues1_bardie11:
    m "Миссис Робертс."
    m "Барди зовет Вас в свою комнату..."
    betty "..."
    betty "Хорошо, я скоро приду туда..."
    return

label ep26_dialogues1_bardie12:
    # Если в течении этого дня Моника заглядывает в комнату Барди

    # Идет сцена наказания Бетти
# Бетти шлепают по попе.
# Барди говорит что поняла-ли она что хозяина дома надо слушаться.
# Бетти отвечает что да.

    bardie "Поняла что хозяина дома надо слушаться?!"
    betty "Да!"
    bardie "Будешь еще нарушать правила дома?!"
    betty "Нет! Не буду!"

    # Бетти стоит с красным задом и зло смотрит на Монику
    return


# Если Бетти зарывалась, то Моника может сказать об этом Барди в его комнате.
# Барди говорит Монике позвать Бетти

# У Бетти появляется диалог о том что Барди зовет ее в свою комнату.
# Бетти напряженно смотрит и говорит что скоро придет туда.

# После этого, в течении времени суток, если зайти в комнату Барди, идет сцена наказания Бетти.
# Бетти шлепают по попе.
# Барди говорит что поняла-ли она что хозяина дома надо слушаться.
# Бетти отвечает что да.


































label ep26_dialogues1_bardie:
