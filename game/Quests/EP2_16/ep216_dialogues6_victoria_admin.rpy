default victoriaMonicaAdmin1 = False  # у Виктории и админа была встреча в кафе
default victoriaMonicaAdmin2 = False  # админ пялил Монику, думая, что это Виктория




# при условии, что была сцена в апартаментах Виктории
# рабочий кабинет Моники
label ep216_dialogues6_victoria_admin_1:
    # Моника сидит за столом, Биг Босс
    # стук в дверь, заходит админ и неуверенно спрашивает
    w2 "Миссис Бакфетт, можно вопрос?"
    mt "Чего этому бездельнику от меня нужно?!"
    mt "Как тяжело быть важным Боссом!"
    mt "Все от меня чего-то хотят!"
    mt "Достали со своими глупостями!"
    mt "Жалкие, никчемные людишки!"
    mt "!!!"
    m "Что ты хотел?"
    m "Говори быстрее, у меня много работы!"
    w2 "Я тут это..."
    w2 "В общем, хотел отпроситься..."
    w2 "Мне... Кхм... Мне надо отлучиться по работе..."
    # Моника злобно на него смотрит
    m "Что значит 'по работе надо'?!"
    m "Твое рабочее место в этом отделе!"
    m "Куда ты собрался?! Рабочий день еще не окончен!"
    if monicaBitch == True:
        m "Весь этот отдел - одни никчемные бездельники!"
        m "И ты - самый главный бездельник здесь!"
    w2 "Но я... Я ненадолго..."
    m "Все! Иди отсюда!"
    m "У меня нет времени на тебя!"
    m "В отличие от всех вас, бездельников, Я работаю тут целыми днями!"
    m "!!!"
    w2 "Спасибо, Миссис Бакфетт..."
    w2_t "Черт! Пронесло! Она отпустила меня!"
    w2_t "Я думал она меня съест!"
    # админ уходит
    mt "Никчемные!"
    mt "Бесполезные!"
    mt "Все до единого!"
    mt "!!!"
    # смена кадра, спустя некоторое время
    # кафе, новая локация
    # Виктория и админ сидят в кафе за столиком
    # Виктория мило ему улыбается, он смущенный, ведет себя неловко, растерянно
    w2 "М-мисс Виктория..."
    w2 "Ваше предложение встретиться - это так... Такая неожиданность для меня..."
    w2 "Вы, наверное, хотели, чтобы я сделал какую-то работу?"
    victoria "Ну о чем ты говоришь?"
    victoria "Неужели я не могу просто так, без повода, встретиться с понравившимся мне мужчиной?"
    victoria "Кстати, как тебя зовут?"
    w2 "Я Эрик... То есть Йорик!"
    w2 "Эрик мой брат и... Я..."
    w2 "Эм..." # стесняется
    victoria "Какое интересное имя. Оно тебе очень идет!"
    w2 "Да? С-спасибо, Мисс Виктория."
    victoria "Ты можешь называть меня просто Виктория."
    w2 "Д-да... Х-хорошо, Ми... То есть, Виктория..."
    victoria "А чем ты увлекаешься, Йорик?"
    w2 "Я? О, я очень люблю все, что связано с репликациями многоуровневых реляционных баз данных!"
    victoria "Правда?! Как интересно!"
    w2 "Да!.."
    w2 "То есть... А вам и правда интересно, Ми... Виктория?.."
    victoria "Конечно! Я обожаю все, что связано с базовыми многоуровнями! Камеры, например..."
    w2 "О, это здорово! Девушки редко этим интересуются!"
    w2 "А многовложенными компьютерными сетями вы тоже интересуетесь, Виктория?"
    victoria "Да, но я боюсь, что не настолько умна, чтобы хорошо в них разбираться..."
    victoria "Во взламывании компьютеров..."
    w2 "Да чего там разбираться?"
    w2 "Любой компьютер можно легко взломать за считанные минуты!"
    victoria "Серьезно?! Не может быть!"
    victoria "Ты такой умный!"
    victoria "Неудивительно, что ты работаешь в таком престижном офисе!"
    victoria "Это, наверное, так сложно?"
    w2 "Неее... Это все ерунда... Работа элементарная, раз плюнуть..."
    # Виктория в притворном восхищении
    victoria "Ты очень талантливый, Йорик!"
    victoria "Твои таланты могли бы пригодиться абсолютно любому! Даже мне. Но об этом позже..."
    victoria "Расскажешь мне про свою девушку?"
    # админ в смущении
    w2 "Я... Кхм... У меня..."
    w2 "Я знаю все об отношениях с девушками, Виктория..."
    w2 "Я видел много фильмов про это..."
    w2 "Про то как... Девушки и мужчины... Это..."
    victoria "Ты так хорошо разбираешься в отношениях?"
    victoria "А что за фильмы? Ты их много посмотрел?"
    w2 "Все..."
    victoria "А девушка у тебя есть, Йорик?"
    w2 "Нет..."
    # она удивленно
    victoria "А почему? Ты такой красивый, умный! Так много всего умеешь..."
    # он удивленно
    w2 "Вы правда так считаете, Виктория?"
    victoria "Да, Йорик... Правда..."
    victoria "Хочешь встретиться со мной еще раз, Йорик?"
    $ victoriaMonicaAdmin1 = True # у Виктории и админа была встреча в кафе
    # кадр на его удивленное лицо
    # смена кадра
    # офис Моники, она сидит психует на админа
    mt "Вот так взять и уйти посреди рабочего дня!"
    mt "За что только он получает здесь деньги?!"
    mt "Жалкий неудачник!!!"
    mt "Самый жалкий из всех этих офисных бездельников!!!"
    mt "Никчемный!!!"
    mt "!!!"
    return


# след. приход Моники на работу в офис
# рабочий кабинет Моники
label ep216_dialogues6_victoria_admin_2:
    # Моника за своим рабочим столом
    # к ней подходит Юлия
    julia "Миссис Бакфетт..."
    mt "Чего она опять ко мне лезет?!"
    # если у Моники отношения с Юлией
    #
    $ notif(_("Моника состоит с Юлией в отношениях."))
    #
    mt "Сколько уже можно?!"
    mt "!!!"
    m "Да, милая. Ты что-то хотела?"
    #
    # если у Моники нет отношений с Юлией
    mt "Никчемная бывшая гувернантка! Фи!"
    m "Что?"
    #
    julia "Миссис Бакфетт, сейчас звонила Мисс Виктория..."
    julia "Она сказала, что ждет Вас у себя."
    mt "Черт!"
    mt "!!!"

    # если у Моники отношения с Юлией
    #
    $ notif(_("Моника состоит с Юлией в отношениях."))
    #
    julia "Миссис Бакфетт, вы говорили, что возьмете меня с собой в гости к Мисс Виктории..."
    julia "Я с большим удовольствием встретилась бы с ней!"
    mt "Дура!"
    m "Нет, Юлия. В другой раз..."
    # Юлия радостно
    julia "Обещаете?!"
    # Моника сквозь зубы
    m "Конечно, милая."
    # Юлия довольно чмокает Монику в губы и уходит на свое рабочее место
    mt "Боже!"
    mt "Надо же быть такой идиоткой!!!"
    mt "И как я только выношу ее присутствие?!"
    mt "!!!"
    #
    # если у Моники нет отношений с Юлией
    # Моника рявкает на нее раздраженно
    m "Я поняла!"
    m "Иди занимайся своими отчетами!!!"
    # Юлия испуганно
    julia "Д-да, Миссис Бакфетт..."
    # Юлия уходит на свое рабочее место
    #

    # Моника сидит злая как черт
    mt "Что этой больной извращенке нужно от меня?!"
    mt "Меня тошнит от одного ее вида!"
    mt "И теперь мне снова нужно ехать к ней!"
    mt "!!!"
    mt "Если бы я могла..."
    # ее мысли прерывает стук в дверь
    # заходит админ
    w2 "Миссис Бакфетт..."
    m "Чего тебе?!"
    m "Не видишь, я занята?!"
    m "Я ухожу на важную встречу!"
    m "!!!"
    w2 "Я просто хотел... Кхм.. Отпроситься не пару часов..."
    m "Что?! Снова?!"
    m "Это уже не в первый раз!"
    m "Причем в рабочее время!"
    m "Куда это ты все время ходишь?!"
    # он смущенно
    w2 "К девушке..."
    # Моника изображает удивление
    m "К девушке?! Ты серьезно?!"
    m "Не смеши меня!"
    m "Такой, как ты, не может нравится ни одной девушке на свете!"
    m "Ты хоть видел себя в зеркало?!"
    m "Никому не нужный неудачник!"
    m "!!!"
    w2 "Я..."
    # Моника его перебивает
    m "И вообще!.."
    m "У меня компьютер не работает уже сколько времени, а он отпрашивается!!!"
    w2 "Миссис Бакфетт, починить Ваш компьютер я могу быстро..."
    w2 "Там нужно всего лишь заменить жесткий диск."
    w2 "Это стоит всего тысячу долларов."
    m "Ты идиот?!"
    m "Какой еще диск?!"
    m "Он просто не включается!!!"
    m "Значит не работает кнопка, которая его включает!!!"
    m "!!!"
    w2 "..."
    m "И откуда такая сумма?!"
    w2 "Я позвонил в компанию, которая занимается поставкой комплектующих."
    w2 "Они сказали, что Ваша организация оплачивает именно такую сумму."
    w2 "Нужна только Ваша подпись, Миссис Бакфетт..."
    # Моника недовольно смотрит на него
    mt "Подпись?!"
    mt "Твою мать!"
    mt "Что на это скажет Биф?!"
    mt "Он подумает, что я решила украсть эти деньги!"
    # орет на админа
    m "Конечно, я знаю про подпись!"
    m "Я тут начальник, я знаю ВСЕ!"
    m "Я должна была бы уволить тебя прямо сейчас!"
    m "Но мне сейчас не до этого!"
    m "У меня есть более важные дела!"
    m "Не отвлекай меня!"
    m "Я без тебя поменяю эту кнопку!!"
    m "ИДИ ОТСЮДА!!!"
    w2 "Спасибо, Миссис Бакфетт..."
    # админ уходит
    mt "Никчемный жалкий неудачник!"
    mt "!!!"
    mt "Так, Моника, соберись!"
    mt "Тебе надо ехать к сучке Виктории!"
    mt "Ненавижу эту мелкую дрянь!"
    mt "!!!"
    # если у Моники отношения с Юлией
    mt "Еще эта Юлия лезет со своей дружбой с Викторией!"
    mt "Дура!!!"
    $ log1 = _("Поехать к Виктории.")
    return

# Моника возле дома Виктории, глазик
label ep216_dialogues6_victoria_admin_3:
    # не рендерить!!
    mt "Настанет тот день, Моника, когда ты избавишься от сучки Виктории!"
    mt "Это будет один из самых счастливых дней!"
    mt "Не могу дождаться этого момента!"
    mt "А пока я вынуждена терпеть ее присутствие в своей жизни..."
    return

# при клике на дом Виктории
# апартаменты Виктории
label ep216_dialogues6_victoria_admin_4:
    # включется сцена, где Виктория разговаривет с Йориком в своей спальне
    # она с ним флиртует
    victoria "Йорик, я так рада, что смог отпроситься с работы!"
    victoria "Я так переживала, что ты не сможешь прийти!"

    w2 "Ваша подруга, Миссис Бакфетт, была весьма добра ко мне..."
    w2 "И без проблем отпустила меня..."
    w2 "Вообще, мне повезло, что у меня такая начальница..."
    w2 "Понимющая, отзывчивая..."
    # Виктория ехидно
    victoria "Да, моя подружка Моника очень хорошая."
    w2 "Да... Очень..."
    # Виктория подходит к админу ближе, флиртует

    victoria "Йорик..."
    victoria "Ты такой милый..."
    victoria "Такой умный, талантливый..."
    victoria "И такой благородный..."

    w2 "Виктория, я..."
    w2 "Я подумал о том что ты попросила меня сделать..."
    w2 "Это... Довольно опасно и я..."
    # админ смущается
    victoria "Тссссс..."
    victoria "Я считаю, что ты заслуживаешь внимания такой девушки, как я, Йорик..."
    victoria "Ты ведь такой умный и красивый..."
    victoria "И смелый..."
    victoria "Докажешь мне что ты смелый?"
    w2 "Я... Я правда не знаю..."
    victoria "Тссссс..." # Виктория соблазняет админа
    victoria "Ты ведь хочешь попробовать что такое встреча с настоящей девушкой, правда?" # кладет руку ему на член
    w2 "Я..."
    victoria "Ты ведь достаточно храбрый?"
    w2 "Да! Да! Да!"
    w2 "Я хочу! Я очень хочу!"
    victoria "Ты достаточно смелый, чтобы помочь мне и сделать что я прошу?"
    w2 "Да! Я все сделаю!"

    # звонок в дверь
    # админ испуганно
    w2 "Ой, кто это?"
    w2 "Вы кого-то ждете, Виктория?"
    victoria "Подожди минутку."
    # уходя, говорит ему, улыбается и посылает воздушный поцелуй
    victoria "Можешь пока раздеваться, Йорик, я сейчас вернусь..."
    # Виктория выходит, админ растерянно смотрит ей вслед
    # смена кадра, звук отворяющейся двери (или лифта-?)
    # холл апартаметов Виктории, в дверях стоит Моника
    mt "Я снова в этой отвратной розовой квартире! Фи!"
    mt "Лицемерная мелкая дрянь!"
    mt "Притворяется невинной овечкой, а сама - демон в юбке!"
    mt "Ненавижу ее!!!"
    mt "Что ей снова нужно от меня?!"
    mt "!!!"
    # Виктория встречает Монику с улыбочкой
    victoria "Тссс, подружка!"
    victoria "Мне очень нужна твоя помощь..."
    victoria "Ты же не откажешь мне?"
    victoria "Ты ведь хорошая подружка?"
    # Моника подозрительно
    m "Какая помощь?"
    victoria "Ой, подружка, для тебя это сущий пустяк!"
    victoria "Там есть один человек, он кое-что может для меня сделать..."
    victroai "Для этого мне надо его соблазнить."
    m "Соблазнить?"
    victoria "Да, подружка Моника. Но я ведь не могу изменять Мистеру Дику!"
    victoria "Поэтому ты меня подменишь, подружка."
    m "Что?!"
    m "Что все это значит?"
    victoria "Это значит, что подружка выручит меня..."
    victoria "Ты ведь хочешь быть для меня хорошей подружкой?"
    m "..."
    menu:
        "Да...":
            pass
    m "Да, я хорошая подружка..."
    victoria "Я тебе сейчас расскажу, что надо делать, хорошая подружка Моника..."
    # затемнение
    # смена кадра на спальню Виктории
    # Виктория заходит в комнату к админу, он уже голый, стеснительно прикрывается
    w2 "Кто это был, Виктория?"
    # она проходит мимо него, берет в руки повязку на глаза
    victoria "Ошиблись дверью, Йорик..."
    victoria "А теперь расслабься... Давай немного поиграем..."
    # подходит к нему, завязывает ему глаза
    w2 "Что? Зачем? Я хочу видеть вас..."
    victoria "Возможно, в следующий раз, а сейчас..."
    victoria "Я хочу чтобы эта встреча была особенной..."
    victoria "Просто отдайся своим ощущениям..."
    victoria "Только не снимай повязку, иначе ты меня расстроишь и я не буду больше играть с тобой."
    w2 "Д-да, В-виктория... Х-хорошо..."
    victoria "Расслабься, Йорик... Не нервничай..."
    # прикасается к нему, проводит рукой по его груди, прижимается к нему
    victoria "Почувствуй мои прикосновения, мое тело..."
    victoria "Я так хочу, чтобы ты ласкал меня, Йорик."
    victoria "Секунду, я сейчас сниму платье..."
    # отстраняется от него и смотрит в сторону двери, подзывает к себе пальцем Монику
    # Моника заходит уже голая, останавливается и в шоке смотрит на админа
    mt "ЧТООООО?!"
    mt "Этот никчемный бездельник?!"
    mt "Какого черта ОН ТУТ ДЕЛАЕТ?!"
    mt "?!?!?!"
    mt "Он для ЭТОГО отпрашивался?!"
    mt "Сволочь!!!"
    mt "!!!"
    mt "!!!!!"
    mt "А эта дрянь?! Зачем он ей нужен?!"
    mt "Что вообще тут происходит?!"
    mt "???"
    # админ нетерпеливо тянет руки в сторну Виктории
    w2 "Виктория, иди ко мне скорее!"
    w2 "Я так хочу этого!"
    # Виктория жестом указывает Монике подойти к админу
    victoria "О, да Йорик!"
    victoria "Прикоснись к моей груди, я так этого хочу!"
    # Моника с отвращением на лице подходит к нему, Виктория стоит сбоку рядом
    mt "О Боже!"
    mt "Какой кошмар!"
    mt "Какой же он мерзкий и жалкий!"
    # он тянет руки и хватается за ее грудь, начинает мять
    mt "Фуууу!!!"
    mt "!!!"
    w2 "О, Виктория!!!"
    w2 "Твоя грудь! Она потрясающая!#it"
    w2 "Такая упругая, такая..."
    victoria "О, Йорик... Поцелуй же ее скорее!#it" # Виктория говорит из-за плеча Моники, будто это она
    # админ тянется губами к ее груди и целует
    # Моника смотрит с отвращением, потом зло на Викторию
    # та ехидно смотрит на нее и снова обращается к админу
    victoria "О, да!!!"
    victoria "Это потрясающе!"
    victoria "Еще разочек!"
    victoria "А теперь потрогай мою киску, Йорик..."
    victoria "Хочешь почеловать ее?#it"
    w2 "Да... Сейчас..."
    # админ тянет руку между ног Монике и трогает ее киску пальцами
    mt "Он прикасается ко МНЕ, Монике Бакфетт! Своими грязными руками!"
    mt "Мой подчиненный!"
    mt "Лапает МЕНЯ!"
    mt "Своего Босса!!!"
    mt "ААААААА!!!"
    # потом опускается на колени и лижет
    victoria "Ооооо! Даааа!!!"
    victoria "Еще! Ещееее!!!"
    w2 "О, ваша киска такая горячая!"
    w2 "Хочу скорее попробовать ее!#it"
    victoria "Да, Йорик! Мне не терпится почувствовать твой член внутри себя!"
    victoria "Ох, пойдем скорее на кровать!"
    victoria "Я уже вся влажная, я так хочу тебя!"
    mt "Сучка!"
    mt "Я убью эту тварь!"
    mt "!!!"
    # админ поднимается
    w2 "Пошли скорее, Виктория!"
    w2 "Куда идти? Я ничего не вижу!"
    victoria "Я отведу тебя."
    # Моника зло на нее смотрит
    mt "!!!"
    victoria "Давай руку, Йорик..." # Виктория протягивает руку Моники
    # админ тянет руку, Моника берет его ладонь и идут к кровати # Моника ведет админа к кровати
    # Моника и админ стоят у кровати, Виктория садится с краю кровати, она остается одетой
    # указывает Монике пальцем, что ей нужно залезть на кровать
    # Моника встает коленями на кровать, лицом к Виктории, злобно на нее смотрит
    w2 "Виктория, а можно я сниму повязку?"
    mt "НЕТ!"
    mt "!!!"
    w2 "Мы ведь уже поиграли немного?"
    w2 "Я так хочу увидеть твое обнаженное тело!"
    victoria "Нет, милый Йорик..."
    victoria "Мы еще играем..."
    victoria "В своих фильмах ты уже все видел."
    victoria "Я хочу подарить тебе ощущения!"
    victoria "Я скажу, когда можно будет снять повязку."
    victoria "Идем ко мне на кровать, я уже жду тебя..."
    # админ трогает кровать рукой, натыкается на ногу Моники, потом лезет к ней на кровать
    w2 "О, я не верю, что сейчас я буду делать ЭТО!"
    w2 "Чувствую себя героем одного из тех фильмов, которые я смотрел..."
    w2 "Там как раз было про такие игры..."
    victoria "Хи-хи-хи! Да, я люблю поиграть..."
    victoria "Пойдем ко мне скорее!"
    victoria "Войди в меня!"
    # Моника встает на четвереньки (догги стайл)
    # админ лапает ее, Моника психует
    mt "Я ему оторву яйца!!!"
    mt "УВОЛЮ!!!"
    mt "УБЬЮ СУЧКУ ВИКТОРИЮ!!!"
    mt "УНИЧТОЖУ ЭТОГО НЕУДАЧНИКА!!!"
    mt "МЕРЗКАЯ СКОТИНА!!!"
    mt "НЕНАВИЖУ ВСЕХ!!!"
    mt "!!!"
    victoria "А теперь попробуй найти мою киску! Хи-хи-хи!"
    w2 "Я совсем ничего не вижу..."
    w2 "Это ваша ножка... Так..."
    victoria "А теперь выше..."
    w2 "О, какая у вас упругая попа, Виктория. Она такая клевая!#it"
    # гладит и мнет руками ягодицы Моники
    w2 "Вы были правы, с закрытыми глазами такие интересные ощущения!"
    w2 "Я представлял вас совсем другой, Виктория!"
    w2 "А на самом еле вы оказались в тысячу раз круче, чем я мог предположить!"
    w2 "Это так офигенно!!!"
    # Виктория зло смотрит на Монику
    victoria "..."
    # Затем, снова натягивает улыбочку
    victoria "Да, я такая!"
    victoria "Входи же в мою киску скорее, Йорик!"
    victoria "Я больше не могу ждать!"
    # админ рукой находит киску Моники и пытается ткунться в нее членом
    # промазывает и тыкается куда-нибудь в ягодицу или ногу, член сгибается
    victoria "Хи-хи-хи! Мимо!"
    w2 "Ох, черт!"
    # снова тыкается не туда
    victoria "Снова мимо!"
    victoria "Ну найди же мою влажную киску скорее!"
    victoria "Она так хочет твой огромный член!"
    w2 "Сейчас... Я сейчас..."
    # снова тыкается и снова мимо
    victoria "Ох, Йорик, я не могу больше терпеть!"
    victoria "Давай я тебе помогу, милый!"
    w2 "Да... Я совсем ничего не вижу..."
    victoria "Я направлю твой огромный член в мою киску своей рукой..."
    # Моника вопросительно смотрит на Викторию
    mt "Какого хрена?!"
    mt "Я еще должна ему помогать?!"
    # Виктория пристально на Монику и указывает рукой на член админа
    mt "!!!"
    menu:
        "Взять член админа и засунуть его в свою киску.":
            pass
    mt "Я что, должна прикасаться к его отростку?!"
    mt "?!?!?!"
    mt "ФУУУУ!!!"
    mt "Не могу поверить, что все это происходит на самом деле!"
    mt "Какой-то нелепый кошмарный сон!"
    mt "Моим прекрасным телом сейчас овладеет какое-то ничтожество!"
    mt "Которое работает в моем подчинении!!!"
    mt "Он даже мечтать не мог о подобном!!!"
    mt "Мерзкое животное! Плебей!!!"
    mt "!!!"
    # Моника тянется рукой к члену админа и направляет в свою киску
    w2 "Ооооох!!!"
    w2 "Ооооо!!!"
    w2 "Мне кажется, я сейчас кончу от одних твоих прикосновений, Виктория!"
    w2 "Какая ты офигенная!!!"
    # Моника вставляет его член в себя
    # Виктория притворно стонет
    # Моника, заткнув себе рот рукой (как в камере), молчит
    w2 "ООООООО!!!"
    w2 "Ох, я не могу поверить! Я наконец-то трахаюсь!!!"
    w2 "Как тепло внутри твоей киски!!! Так влажно!!!"
    victoria "ДААААА!!!"
    w2 "ООООО!!!"
    victoria "Ооооох как круууутоооо!"
    w2 "Охренительно!!! ДААА!!!"
    victoria "Ты настоящий зверь! Да!!!"
    victoria "ЕЩЕЕЕ!!! ДАААА!!!"
    w2 "Оооо, я больше не могууу!!! Ааааа!!!"
    w2 "Я кажется сейчас кончуууу!!!"
    # Виктория издевательски смотрит на Монику

    victoria "Кончай в меня, Йорик! Давай!"
    victoria "Давай же! Сделай это для меня!"
    # возможно кончать куда-то еще + сделать разветвление в зависимости от поступка с Мелани. (кончание, либо еще какое-то действие, небольшое, но противное)
    menu:
        "Кончить внутрь Моники.":
            w2 "КОНЧААААЮЮЮЮ!!!"
            victoria "ААА!!!"
            w2 "ООО!!!"
            victoria "ДАААА!!!"
            w2 "ОООООО!!!!"
            pass
    # админ кончает
    # Моника в бешенстве, но молчит
    mt "!!!"
    mt "!!!!!"
    mt "!!!!!!!"
    # затемнение
    # смена кадра, холл в апартаментах Виктории
    # Виктория с админом стоят у двери, Моника голая прячется за углом
    # Виктрия провожает админа, он в восторге
    w2 "Виктория, это такой кайф!"
    w2 "Я не ожидал, что будет настолько круто!"
    w2 "Я в восторге!!!"
    victoria "Мне тоже очень понравилось, милый Йорик!"
    victoria "Мы обязательно с тобой повторим!"
    w2 "Ооо, да!"
    w2 "Я с большим удовольствием!!!"
    w2 "Один ваш звонок, Виктория, и я приеду, несмотря ни на что!"
    # Виктория строит глазки
    victoria "Даже если это будет рабочий день? Как сегодня?"
    w2 "Скажу начальнице, что у меня важные дела по работе!"
    w2 "Она все равно не узнает, где я был на самом деле!"
    w2 "Вы же ей ничего не расскажете, Виктория?"
    victoria "Ну что ты, Йорик? Конечно же, нет!"
    victoria "Это будет наш с тобой маленький секретик! Хи-хи!"
    w2 "Да, прикольно!"
    w2 "Тогда до встречи!"
    victoria "До встречи, Йорик..."
    # админ наклоняется к Виктории, чмокает ее в щеку и уходит
    # он уходит
    # Виктория подходит к Монике, та в шоке
    victoria "Подружка Моника хорошая."
    victoria "Она мне помогла."
    victoria "Тебе понравилось помогать мне, подружка?"
    mt "Может, долбануть ее чем-нибудь потяжелее?"
    mt "И убежать..."
    mt "Все равно все подумают на админа..."
    mt "Черт... Уверена у этой сучки здесь спрятаны камеры..."
    mt "Слишком рискованно..."
    menu:
        "Понравилось.":
            pass
    m "Да..."
    victoria "Что 'да'? Понравилось?"
    m "Да! Очень!"
    # Виктория ехидно хихикает
    victoria "Хи-хи-хи!"
    victoria "Я знала, подружка, что тебе понравится помогать мне."
    victoria "И поэтому ты не откажешь мне в помощи в следующий раз, когда я тебя позову."
    m "Этот... Он мой подчиненный..."
    m "А если он узнает о том, что это была Я?"
    victoria "Уверена, что ради нашей с тобой хорошей дружбы ты сможешь потерпеть небольшие неудобства, подружка."
    mt "!!!"
    $ victoriaMonicaAdmin2 = True # админ пялил Монику, думая, что это Виктория
    return

# после сцены с админом у Виктории дома, Моника возле дома Виктории, мысли
label ep216_dialogues6_victoria_admin_5:
    # не рендерить!!
    mt "В МЕНЯ!"
    mt "МИССИС МОНИКУ БАКФЕТТ!"
    mt "ГЛАВУ ЖУРНАЛА!"
    mt "БОССА!!!"
    mt "ТЫКАЛСЯ СВОИМ ГРЯЗНЫМ ОТРОСТКОМ КАКОЙ-ТО ЖАЛКИЙ!.."
    mt "ЖАЛКИЙ! НИКЧЕМНЫЙ! БЕСПОЛЕЗНЫЙ!"
    mt "ПЛЕБЕЙ!!!"
    mt "Я УБЬЮ ВИКТОРИЮ!!!"
    mt "НЕНАВИЖУ ЭТУ МРАЗЬ!!!"
    mt "!!!"
    return

# Моника приходит на работу на др. рабочий день
# отдел отчетов
label ep216_dialogues6_victoria_admin_6:
    w2 "Здравствуйте, Миссис Бакфетт!"
    # она молча просто зло на него смотрит
    m "!!!"
    # он непонимающе смотрит на нее
    w2 "Что-то не так, Миссис Бакфетт?"
    # она продолжает сверлить его взглядом
    mt "ЖАЛКИЙ! НИКЧЕМНЫЙ! БЕСПОЛЕЗНЫЙ!"
    mt "ПЛЕБЕЙ!!!"
    m "НИЧЕГО!"
    m "!!!"
    # и проходит просто мимо
    # он смотрит ей вслед мечтательно
    w2_t "Виктория, конечно, клевая..."
    w2_t "Но вот добраться бы до задницы Бакфетт..."
    w2_t "О ней мечтают все!"
    w2_t "Эх... Жаль что это абсолютно невозможно..."
    return


# офис Дика
# Моника приносит Виктории деньги, одета в красное платье
# регулярный диалог
#label ep216_dialogues6_victoria_admin_7:
#    # Виктория сидит на своем рабочем месте, ехидно смотрит на Монику
#    # убрать про деньги
#    victoria "О, подружка Моника!"
#    victoria "Я так рада тебя видеть!"
#    victoria "А ты? Ты рада меня видеть, подружка Моника?"
#    m "Да... Рада..."
#    victoria "Подружка хочет меня чем-то порадовать?"
#    m "Я принесла деньги..."
#    victoria "Хорошо, подружка. Я как раз собиралась на шоппинг завтра..."
#    victoria "Хочешь составить мне компанию?"
#    m "..."
#    victoria "Ах, я совсем забыла, что у тебя совсем нет времени на это."
#    victoria "Тебе ведь нужно до следующей пятницы заработать еще $ 5 000 для меня..."
#    victoria "Хи-хи-хи!"
#    victoria "Положи деньги на стол, подружка Моника."
#    victoria "Можешь идти."
#    victoria "Жду [$ 5 000 в следующую пятницу], подружка."
#    mt "Мерзкая лицемерная тварь!"
#    mt "Ненавижу тебя!!"
#    mt "!!!"
    # Виктория скажет, что ей нравится платье подружки, но она просит ее не приходить в этот офис в таком виде (после сцены с Мелани)
    # Скажет что мне нравится твое платье и я бы хотела дальше тебя видеть в нем в моих апартаментах, так как здесь приличный район, хи-хи
    # Но в Мистеру Дику, пожалуйста, приходи в той забавной одежде. Я бы не хотела чтобы Мистер Дик видел тебя какой-то другой.

    # коммент Моники, когда пытается войти не в одежде шлюхи
    return
