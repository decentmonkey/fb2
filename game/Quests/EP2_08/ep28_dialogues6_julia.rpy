# Продолжение линии отношений с Юлией

### В холле у лифта может быть разная одежда. Красивое платье, либо одежда шлюхи. Нужна какая-то локация, где офисная униформа. +
### Текстов делаем как можно меньше (евенты минималистичные) +
### Везде перед действием даем выбор: Подсмотреть то-то, либо отказаться (corruption) +


# Работа в офисе. Гримерка.
# Моника сталкивается с Фредом. Разговор Фреда и Моники.
label ep28_dialogues6_julia_1:
    # Моника сталкивается с Фредом.
    img 21873
    mt "Он опять здесь ошивается!"
    mt "И что ему в этот раз нужно?!." # возмущенно
    # Моника говорит сердито
    img 21872
    m "Фред! Ты так часто бываешь в офисе..."
    m "Я подумала, может, тебе уже устроиться сюда на работу кем-нибудь?"
    m "Уборщиком, например?.."
    # Фред ей с серьезным видом
    img 21874
    fred "С моей стороны было бы непрофессионально совмещать две работы, Миссис Бакфетт."
    fred "Тем более, такие не схожие по должностным обязанностям."
    # Фред делает паузу и добавляет с улыбочкой
    img 20865
    fred "Чего я не могу сказать о вас, Миссис Бакфетт..."
    # Моника злится
    img 21873
    mt "!!!"
    mt "Я готова придушить эту сволочь Фреда!!!"
    mt "Чего он ко мне пристал со своими нелепым шантажом?!"
    mt "Не понимаю, чего он добивается? Какая ему выгода от этого?"
    fred "Мне очень понравилось, Миссис Бакфетт, как вы справились с моей небольшой просьбой в прошлый раз."
    fred "И до этого у вас все отлично получалось."
    img 21875
    m "Фред, я не собираюсь больше заниматься подобными вещами!"
    m "Я здесь начальник и нечего мною командовать!" # зло
    img 21876
    fred "Если вы, Миссис Бакфетт, откажетесь играть в мою небольшую профессиональную игру..."
    fred "То вы быстро перестанете быть боссом..."
    # Моника зло смотрит на Фреда и молчит
    img 21877
    m "!!!"
    img 21878
    fred "Миссис Бакфетт, Я бы хотел, чтобы Вы выяснили, какого цвета трусики носит Юлия."
### Какого цвета трусики носит Юлия (т.е. вообще, не именно сегодня, т.к. она носит одни и те же в игре) +
    # Моника в шоке от такого задания
    img 21879
    m "Что-о-о?!"
    m "Фред!!! Ты ненормальный?! Как ты себе это представляешь?!"
    m "???"
    img 21880
    fred "Я не сомневаюсь, Миссис Бакфетт, что у вас все получится."
    fred "Я с нетерпением буду ждать вашего ответа."
    img 21881
    m "..."
    menu:
        "Отказаться выполнять дурацкие приказы этого мерзавца!":
            # Моника орет на Фреда
            img 21882
            m "Ты не смеешь мне указывать, что мне делать!"
            m "И мне плевать на то, что ты кому-то расскажешь!"
            m "Ты просто какой-то ничегонезначащий водитель!!! Тебе никто не поверит!"
            m "А я всем скажу, что ты шантажируешь меня, подделав фото!"
            m "Пошел вон отсюда!!!"
            m "Еще раз здесь тебя увижу - вызову охрану!!!"
            m "Жалкий водитель!"
            fred "..." # Фред уходит
            return False
        "Продолжить играть в 'профессиональную' игру Фреда.":
            pass
    # Моника смотрит на Фреда с негодованием
    mt "Ненавижу этого мерзавца!"
    mt "..."
    mt "Но если он покажет мою фотографию, где я оттираю это чертово пятно..."
    mt "Еще и в форме гувернантки!.."
    mt "!!!"
    mt "Боюсь даже преставить, какие будут последствия!"
    # Фред ухмыляется
    img 21883
    fred "До скорой встречи, Миссис Бакфетт."
    m "..." # зло
    # Фред уходит
    $ log1 = _("Узнать, какие трусики носит Юлия.")
    return

# в меню выбора в офисе + новый пункт в отношениях с Юлией "Выяснить, какого цвета трусики на Юлии сегодня"

# Кабинет Моники. Если игрок, кликая на Юлию, выбирает пункт "Выяснить, какого цвета трусики на Юлии сегодня"
#### Тут можно укоротить. Евенты должны быть маленькими. + Подбрасывание флешки сложно показать. +
label ep28_dialogues6_julia_2:
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    mt "Какой же этот Фред мерзавец!"
    mt "Скорее бы вернуть себе все, что у меня отняли!"
    mt "Первым делом я уволю этого 'профессионала'!"
    mt "!!!"
    mt "Как мне узнать цвет трусиков Юлии?"
    mt "Не могу же я у нее просто взять и спросить! Что она обо мне подумает?"
    mt "Как тогда мне это сделать?"
    mt "И чтобы Юлия ничего не заподозрила..."
    mt "Хм..." # с улыбочкой
    # Моника подходит к своему столу, незаметно кладет на свой стол флешку. куда-нибудь за монитор. Потом тоном босса подзывает Юлию.
    m "Юлия! Подойди ко мне!"
    # Юлия подходит к Монике
    julia "Да, Миссис Бакфетт?"
    m "Юлия! Я потеряла свою флешку. А она мне срочно нужна!"
    m "Найди ее! Я ее, наверное, выронила где-то в кабинете."
    julia "Хорошо, Миссис Бакфетт... Только... Где ее искать?"
    m "Откуда я знаю?! Поищи под столом!" # раздраженно
    julia "Да, Миссис Бакфетт. Сейчас посмотрю."
    # Юлия наклоняется и заглядывает под стол Моники
    m "..."
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return 1
    # Моника в это время пытается заглянуть ей под платье, но ей ничего не видно
    mt "Черт! Еще немного!"
    # Юлия выпрямляется, Моника делает вид, что тоже ищет флешку
    julia "Миссис Бакфетт, под вашим столом нет флешки..."
    m "..."
    mt "Конечно, ее там нет!.."
    m "Юлия, ты уверена, что внимательно посмотрела?" # строго
    # Юлия неуверенно
    julia "М-м-миссис Бакфетт, я сейчас посмотрю еще раз..."
    # Юлия встает на колени и заглядывает под стол, Моника в это время пытается посмотреть ей под платье
    mt "Все равно мне ничего не видно!"
    mt "!!!"
    # Юлия выпрямляется, но все еще стоит на коленях и тут замечает на столе флешку
    julia "???" # удивленно
    # Юлия поворачивается к Монике и замечает, что та пристально смотрит на ее зад
    julia "Миссис Бакфетт... Что в-в-вы д-делаете?"  # вопросительно смотрит на Монику
    m "..." # растерянно
    m "Ничего!"
    m "..."
    m "Ты нашла флешку?!" # строго
    # Юлия встает, с непонимающим видом
    julia "Да, Миссис Бакфетт... Она лежит у вас на столе."
    julia "..."
    m "..."
    # Моника с покер-фейсом протягивает руку
    m "Давай ее мне!"
    # Юлия подходит, отдает флешку, смотрит на Монику вопросительно
    julia "???"
    # Моника делает вид, что ничего не произошло
    m "А теперь иди работай! Не отвлекайся!"
    # садится за свой стол и прячется за монитором
    mt "Вот черт! Ничего не получилось!"
    mt "Более того, мне кажется, что она заметила, как я пыталась заглянуть ей под платье!!!"
    mt "Какой кошмар!!!"
    mt "!!!"
    mt "Мне нужно будет придумать еще что-нибудь..."
    return


# Кабинет Моники. Другой день.
label ep28_dialogues6_julia_3:
### На полках документов нет. Моника говорит достань. Юлия отвечает что там нет документов на тех полках. +
### Моника говорит они там есть (ей надо чтобы она туда полезла) +
### В итоге, Юлия ничего не находит +
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    mt "Не могу поверить! Мне приходится выяснять, какие трусики носит моя секретарша!!!"
    mt "И все из-за этого мерзавца Фреда!"
    mt "Как-будто без этого у меня мало забот!"
    mt "Я здесь начальник! Мне нужно думать о работе целого отдела и о том, как вернуть назад мою компанию, а не о трусиках секретарши!"
    mt "..."
    mt "Как мне посмотреть на трусики Юлии?"
    mt "И чтобы она ничего не заподозрила..."
    mt "Хм..." # с улыбочкой
    # Моника садится за свой стол. Потом тоном босса подзывает Юлию.
    m "Юлия! Подойди ко мне!"
    # Юлия подходит к Монике
    julia "Да, Миссис Бакфетт?"
    m "Юлия! Мне срочно для работы нужна папка с отчетами за прошлый год!"
    m "Достань мне ее!" # строго
    julia "Хорошо, Миссис Бакфетт. А где эта папка?"
    m "Эта папка стоит в шкафу на верхней полке."
    # Юлия смотрит на шкаф, никаких документов там нет, смотрит на Монику
    julia "М-м-Миссис Бакфетт... Там на полках... Там нет никаких папок и документов..."
    mt "..."
    m "Юлия! Я тебе говорю, что эта папка там есть! Достань мне ее!" # раздраженно
    m "Срочно!!!"
    # Юлия растерянно
    julia "Да, Миссис Бакфетт... Я сейчас принесу стул..."
    # Юлия ставит стул, встает на него и тянется к верхней полке, где нет документов. Ее платье немного приподнимается
    m "..."
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return 1
    # Моника пытается заглянуть ей под платье, но ей ничего не видно
    mt "Черт! Еще чуть-чуть и я увижу ее трусики!"
    julia "Миссис Бакфетт, здесь нет никаких документов..."
    m "..."
    m "Посмотри внимательнее, Юлия!" # строго
    # Юлия пытается найти папку, а Моника пытается заглянуть ей под платье
    mt "Все равно мне ничего не видно!"
    mt "!!!"
    # Юлия поворачивает голову и видит, что Моника заглядывает ей под платье
    julia "???" # удивленно
    julia "Миссис Бакфетт... Что в-в-вы д-делаете?"  # вопросительно смотрит на Монику
    # Моника делает вид, что ничего не произошло
    m "..." # растерянно
    m "Ничего!"
    m "..."
    m "Ты нашла папку с отчетами, Юлия?!" # строго
    # Юлия с непонимающим видом спускается со стула
    julia "Нет, Миссис Бакфетт... На полке нет ничего."
    julia "..."
    m "..."
    # Моника с серьезной миной
    m "Ты плохо искала, Юлия! Тебе ничего нельзя доверить!"
    julia "???"
    julia "Н-но..."
    m "А теперь иди работай! И не отвлекайся!"
    # Юлия возвращается за свой стол, Моника прячется за монитором
    mt "Вот черт! Ничего не получилось!"
    mt "Более того, она увидела, как я пыталась заглянуть ей под платье!!!"
    mt "Какой кошмар!!!"
    mt "!!!"
    mt "Мне нужно будет придумать еще что-нибудь..."
    mt "Иначе мерзавец Фред не оставит меня в покое..."
    return

# Работа в офисе. Гримерка.
# Моника сталкивается с Фредом. Разговор Фреда и Моники.
label ep28_dialogues6_julia_4:
    # Моника возмущенно
    m "Это снова ты?!"
    # Фред ей отвечает спокойно
    fred "Миссис Бакфетт... Это непрофессионально с вашей стороны не выполнять условия нашей договоренности..."
    m "!!!" # зло смотрит на него
    menu:
        "Отказаться выполнять дурацкие приказы этого мерзавца!": # если отказалась заглядывать под юбку Юлии
            # Моника орет на Фреда
            m "ФРЕД!!!"
            m "Ты не смеешь мне указывать, что мне делать!"
            m "И мне плевать на то, что ты кому-то расскажешь!"
            m "Ты просто какой-то ничегонезначащий водитель!!! Тебе никто не поверит!"
            m "А я всем скажу, что ты шантажируешь меня, подделав фото!"
            m "Пошел вон отсюда!!!"
            m "Еще раз здесь тебя увижу - вызову охрану!!!"
            m "Жалкий водитель!"
            fred "..." # Фред уходит
            return False
        "Продолжить играть в 'профессиональную' игру Фреда.": # если заглядывала под юбку Юлии
            pass
    # Моника смотрит на Фреда с негодованием
    mt "Ненавижу этого мерзавца!"
    fred "Вы так и не сделали, что я вам сказал, Миссис Бакфетт?"
    # Моника убийственно смотрит на него, но молчит
    m "..."
    # Фред с улыбочкой
    fred "Так уж и быть, Миссис Бакфетт. Я готов подождать еще немного..."
    m "..."
    fred "Я не сомневаюсь, что у вас все получится, Миссис Бакфетт."
    fred "Я с нетерпением буду ждать вашего ответа."
    fred "До скорой встречи, Миссис Бакфетт."
    return


# Кабинет Моники. Следующий день.
label ep28_dialogues6_julia_5:
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    mt "Не могу поверить! Мне приходится выяснять, какие трусики носит моя секретарша!!!"
    mt "Я здесь начальник! Мне нужно думать о работе целого отдела, а не о трусиках секретарши!"
    mt "..."
    mt "Как мне посмотреть на трусики Юлии?"
    mt "И чтобы она ничего не заподозрила..."
    mt "Хм..." # с улыбочкой
    mt "Собственно, какая мне разница, что она подумает?"
    mt "Она же просто секретарша!"
    mt "А мне надо скорее заканчивать с этими дурацкими заданиями Фреда!"
    mt "..."
    menu:
        "Заглянуть под стол Юлии.": #corruption
            pass
        "Не заглядывать.":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return 1
    # Моника лезет под стол Юлии, Юлия удивленно и испуганно смотрит вниз
    julia "Миссис Бакфетт! Что вы делаете?!"
    m "Ничего!"
    m "Сиди и работай!"
    m "И не отвлекайся!"
    julia "М-м-Миссис Бакфетт... Вы что-то потеряли? Вам помочь?" # растерянно
    mt "Да!!! Раздвинь ноги и покажи свои трусики!"
    m "Нет!!! Я сама! Сиди и работай!"
    # Моника все это время пытается посмотреть, в каких трусиках Юлия, но ей ничего не видно
    mt "Еще чуть-чуть и я увижу ее трусики!"
    mt "!!!"
    m "Отодвинь ногу, Юлия! Она мне мешает!"
    # Юлия вскакивает со своего стула
    julia "Миссис Бакфетт! Мне кажется или вы пытаетесь... Вы..."
    julia "!!!"
    # Юлия смущается, Моника поднимается с пола
    m "Тебе кажется, Юлия!!!" # строго
    m "Я..."
    m "Я просто потеряла кое-что! Иди работай!"
    # Юлия возвращается за свой стол, Моника садится за свой стол и прячется за монитором
    mt "Вот черт! Снова ничего не получилось!"
    mt "Более того, эта Юлия поняла, что я пыталась заглянуть ей под платье!!!"
    mt "Какой кошмар!!!"
    mt "!!!"
    mt "Что же мне еще придумать?.."
    mt "Пора уже заканчивать с этим! Сколько можно заниматься этими глупостями?!"
    return

# В конце рабочего дня, когда Моника лезла к Юлии под стол.
# Гримерка. Моника сталкивается с Фредом. Разговор Фреда и Моники.
label ep28_dialogues6_julia_6:
### Нет понятия "последний день". Фред говорит просто поторопиться. (не привязываемся к таймингу) +
    # Моника возмущенно
    m "ФРЕД!!!"
    m "Перестань меня преследовать!!!"
    # Фред ей отвечает спокойно
    fred "Миссис Бакфетт... Вы выяснили то, о чем я вас просил?"
    m "!!!" # зло смотрит на него
    mt "Ненавижу этого мерзавца!"
    menu:
        "Отказаться выполнять дурацкие приказы этого мерзавца!": # если отказалась заглядывать под юбку Юлии
            # Моника орет на Фреда
            m "ФРЕД!!!"
            m "Ты не смеешь мне указывать, что мне делать!"
            m "И мне плевать на то, что ты кому-то расскажешь!"
            m "Ты просто какой-то ничегонезначащий водитель!!! Тебе никто не поверит!"
            m "А я всем скажу, что ты шантажируешь меня, подделав фото!"
            m "Пошел вон отсюда!!!"
            m "Еще раз здесь тебя увижу - вызову охрану!!!"
            m "Жалкий водитель!"
            fred "..." # Фред уходит
            return False
        "Продолжить играть в 'профессиональную' игру Фреда.": # если заглядывала под юбку Юлии
            pass
    # Моника убийственно смотрит на него
    m "Нет, Фред! Это не так легко, как ты думаешь!!!"
    m "Я не какая-то лесбиянка, чтобы просто взять и залезть к ней под юбку!"
    # Фред с улыбочкой
    fred "Миссис Бакфетт, я все понимаю. Но прошу вас поторопиться."
    fred "С вашей стороны непрофессионально заставлять меня ждать так долго."
    m "..." # сердито
    m "Я не знаю, как сделать это!"
    m "Может, ты, как профессионал, подскажешь мне?"
    fred "Не вижу в этом проблемы, Миссис Бакфетт."
    fred "Просто наденьте трусики Юлии..."
    m "???" # как на идиота
    fred "Вы же любите их носить, Миссис Бакфетт?"
    m "Нет, конечно!!! Что за глупости?!" # возмущается
    fred "И покажите ей, что вы носите ее трусики..."
    fred "А она покажет вам свои трусики в ответ."
    mt "Что за чушь он говорит?!"
    fred "Я не сомневаюсь, что у вас все получится, Миссис Бакфетт."
    fred "Я с нетерпением буду ждать вашего ответа."
    fred "До скорой встречи, Миссис Бакфетт."
    m "..." # сердито
    # Фред уходит
    mt "Я уже несколько дней потратила на выяснение цвета трусиков секретарши..."
    mt "..."
    mt "Может, и правда сделать, как сказал этот мерзавец Фред?.."
    mt "Я уже не знаю, что еще можно придумать..."
#    $ log1 = _("Надеть трусики Юлии на работу в офис.")
    return

### Какая логика в том что Моника решила одеть трусики Юлии? +
### Думаю надо чтобы Моника ответила Фреду что не знает как это сделать. А Фред ей советует одеть трусики Юлии и показать ей. А та покажет в ответ. +
### Вы же любите их носить... +
### Моника говорит еще чего! +
### А сама потом думает может и правда так сделать? Других идей у нее нет. +

### Это не такие же трусики как у меня... Это... Это мои трусики... +
### Я узнаю их...+
### Моника стыдится, думает про себя что глупая ситуация, но сквозь зубы спрашивает: Но ведь правда они красивые? +
### Юлия отвечает: Вообще-то они ужасные, Миссис Бакфетт. Я ненавидела носить их. +


# Кабинет Моники. Следующий день.
label ep28_dialogues6_julia_7:
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    mt "Не могу поверить!"
    mt "Я собираюсь показывать своей секретарше, в каких я трусиках!!!"
    mt "А вдруг она узнает свои трусики?!"
    mt "Не могу же я признаться ей в том, что я ношу ЕЕ трусики!"
    mt "Я, Моника Бакфетт, ношу трусики своей бывшей гувернантки!"
    mt "Хотя... Я сама в это с трудом верю, а Юлия тем более не поверит..."
    mt "..."
    m "Юлия!"
    julia "Да, Миссис Бакфетт?" # вопросительно
    m "..."
    menu:
        "Ты очень хорошо работала гувернанткой, поэтому я...": #corruption
            pass
        "Ничего! Сиди и работай! Не отвлекайся!":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return 1
    # Моника обращается к Юлии неуверенно
    m "Хм... Юлия, ты знаешь..."
    m "..."
    m "Несмотря на то, что я иногда была немного строга с тобой..."
    m "Мне нравилось, как ты работала у меня гувернанткой."
    # Юлия крайне удивлена, смотрит на Монику
    julia "Это правда, Миссис Бакфетт?.."
    m "Да, Юлия..."
    julia "А я думала, что... Вы... В общем..."
    m "Мне правда все нравилось. Думаю, весьма непросто найти гувернантку лучше, чем ты."
    mt "Черт!!! Я не могу этого сказать!"
    m "После того, как ты перестала работать, я увидела в твоей комнате твои трусики..." # выдавливает из себя
    m "И мне они очень понравились..."
    m "..."
    m "И я себе купила такие же..."
    julia "!!!"
    mt "Я не верю, что я говорю это! Я говорю это своей секретарше!!!"
    # Юлия смотрит с недоверием
    julia "Купили себе трусики, как у меня?!"
    m "Да, Юлия. Ты мне не веришь?"
    # Юлия, смутившись
    julia "Если быть честной, Миссис Бакфетт, то я... Я сомневаюсь, что Вы говорите правду..."
    m "..."
    menu:
        "Поднять платье и показать Юлии трусики.": #corruption
            pass
        "Я не собираюсь ставить себя в такую глупую ситуацию!":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return 1
    # Моника задирает свое платье
    m "Вот смотри! Они сейчас на мне!"
    # Юлия смотрит на трусики, она в шоке
    julia "Это не такие же трусики как у меня... Это..."
    julia "Миссис Бакфетт... Это мои трусики..."
    julia "Я узнаю их!"
    # Моника стыдится
    mt "Боже! Какая глупая ситуация!"
    mt "И как мне теперь выкрутиться из нее?"
    mt "..."
    m "Но ведь правда они красивые?" # сквозь зубы
    julia "Вообще-то, Миссис Бакфетт, они ужасные. Я ненавидела носить их."
    # Моника молча смотрит на нее, опускает платье
    mt "Пора заканчивать весь этот цирк!"
    m "Юлия, я тебе показала свои трусики. Теперь я хочу увидеть твои!"
    # Юлия офигевает
    julia "Что???"
    julia "Нет! Я не буду вам ничего показывать, Миссис Бакфетт!"
    # Моника требовательно
    m "Юлия, просто покажи мне их и все. Я просто хочу посмотреть."
    julia "Нет, Миссис Бакфетт! Я вам ничего не покажу!"
    julia "Извините, но нет!"
    julia "Мне надо идти работать..."
    # Юлия продолжила работу, сидит за своим столом и косо посматривает на Монику
    # Моника садится за свой стол и прячется за монитором
    mt "Вот черт! Это было так ужасно!"
    mt "Такая глупая ситуация!!!"
    mt "!!!"
    mt "И снова ничего не получилось!"
    mt "Эта Юлия теперь думает, что я пристаю к ней!"
    mt "Я, Моника Бакфетт, пристаю к какой-то секретарше!!!"
    mt "!!!"
    mt "Пусть что хочет, то и думает! Какое мне дело до этого?!"
    mt "Только что я теперь скажу этому мерзавцу Фреду?"
    mt "???"
    return


# В конце рабочего дня, когда Моника показывала свои трусики Юлии.
# Кабинет секретарши (перед кабинетом Бифа), когда Моника приносит флешку секретарю.
# Моника сталкивается с Фредом. Разговор Фреда и Моники.
label ep28_dialogues6_julia_8:
    # Моника возмущенно
    m "Фред!"
    m "Сколько можно за мной ходить?!"
    mt "Я сегодня так и не узнала цвет трусиков Юлии. Что же делать?"
    # Фред ей отвечает спокойно
    fred "Миссис Бакфетт... Вы выяснили то, о чем я вас просил?"
    m "!!!" # зло смотрит на него
    mt "Ненавижу этого мерзавца!"
    menu:
        "Отказаться выполнять дурацкие приказы этого мерзавца!": # если поднимала платье перед Юлией
            # Моника орет на Фреда
            m "ФРЕД!!!"
            m "Ты не смеешь мне указывать, что мне делать!"
            m "И мне плевать на то, что ты кому-то расскажешь!"
            m "Ты просто какой-то ничегонезначащий водитель!!! Тебе никто не поверит!"
            m "А я всем скажу, что ты шантажируешь меня, подделав фото!"
            m "Пошел вон отсюда!!!"
            m "Еще раз здесь тебя увижу - вызову охрану!!!"
            m "Жалкий водитель!"
            fred "..." # Фред уходит
            return False
#        "Продолжить играть в 'профессиональную' игру Фреда.": # если отказалась поднимать платье перед Юлией
        "Юлия носит трусики белого цвета!":
            m "Да, я выяснила!!!"
            m "Она носит трусики белого цвета!"
            m "..."
        "Юлия носит трусики красного цвета!":
            m "Да, я выяснила!!!"
            m "Она носит трусики красного цвета!"
            m "..."
        "Юлия носит трусики синего цвета!":
            # Моника сердито, сложив руки
            m "Да, я выяснила!!!"
            m "Она носит трусики синего цвета!"
            m "..."
    # Фред с улыбочкой
    fred "Миссис Бакфетт, обман - это непрофессионально."
    fred "Но я вас прощаю на первый раз..."
    # Моника зло смотрит на него
    m "..."
    mt "Я уже несколько дней потратила на выяснение цвета трусиков секретарши..."
    mt "Мне все это надоело уже!!!"
    fred "Я не сомневаюсь, что у вас все получится, Миссис Бакфетт."
    fred "Я с нетерпением буду ждать вашего ответа."
    fred "До скорой встречи, Миссис Бакфетт."
    # Фред уходит
    mt "..."
    mt "Я уже не знаю, что еще можно придумать..."
    return


# Новый пункт в меню "Отношения с Юлией"
label ep28_dialogues6_julia_9:
    menu:
        "Выяснить, какого цвета трусики на Юлии сегодня":
            menu:
                "Заставить Юлию искать флешку.":
                    return 1
                "Заставить Юлию достать с полки папку с отчетами.":
                    return 2
                "Заглянуть под стол Юлии.":
                    return 3
                "Показать Юлии свои трусики.":
                    return 4
