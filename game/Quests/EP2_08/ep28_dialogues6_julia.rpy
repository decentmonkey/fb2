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
    img 21911
    mt "Какой же этот Фред мерзавец!"
    mt "Скорее бы вернуть себе все, что у меня отняли!"
    mt "Первым делом я уволю этого 'профессионала'!"
    img 21912
    mt "!!!"
    mt "Как мне узнать цвет трусиков Юлии?"
    mt "Не могу же я у нее просто взять и спросить! Что она обо мне подумает?"
    mt "Как тогда мне это сделать?"
    mt "И чтобы Юлия ничего не заподозрила..."
    img 21913
    mt "Хм..." # с улыбочкой
    # Моника подходит к своему столу, незаметно кладет на свой стол флешку. куда-нибудь за монитор. Потом тоном босса подзывает Юлию.
    img 21914
    w
    img 21915
    m "Юлия! Подойди ко мне!"
    # Юлия подходит к Монике
    img 21916
    julia "Да, Миссис Бакфетт?"
    img 21917
    m "Юлия! Я потеряла свою флешку. А она мне срочно нужна!"
    m "Найди ее! Я ее, наверное, выронила где-то в кабинете."
    img 21918
    julia "Хорошо, Миссис Бакфетт... Только... Где ее искать?"
    img 21919
    m "Откуда я знаю?! Поищи под столом!" # раздраженно
    img 21920
    julia "Да, Миссис Бакфетт. Сейчас посмотрю."
    # Юлия наклоняется и заглядывает под стол Моники
    img 21921
    m "..."
    img 21922
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return 1
    # Моника в это время пытается заглянуть ей под платье, но ей ничего не видно
    img 21923
    w
    img 21924
    mt "Черт! Еще немного!"
    # Юлия выпрямляется, Моника делает вид, что тоже ищет флешку
    img 21925
    julia "Миссис Бакфетт, под вашим столом нет флешки..."
    m "..."
    mt "Конечно, ее там нет!.."
    img 21926
    m "Юлия, ты уверена, что внимательно посмотрела?" # строго
    # Юлия неуверенно
    img 21927
    julia "М-м-миссис Бакфетт, я сейчас посмотрю еще раз..."
    # Юлия встает на колени и заглядывает под стол, Моника в это время пытается посмотреть ей под платье
    img 21928
    w
    img 21929
    w
    img 21930
    w
    img 21931
    mt "Все равно мне ничего не видно!"
    img 21932
    w
    img 21933
    mt "!!!"
    # Юлия выпрямляется, но все еще стоит на коленях и тут замечает на столе флешку
    img 21934
    julia "???" # удивленно
    img 21935
    # Юлия поворачивается к Монике и замечает, что та пристально смотрит на ее зад
    img 21936
    w
    img 21937
    w
    img 21938
    w
    img 21939
    julia "Миссис Бакфетт... Что в-в-вы д-делаете?"  # вопросительно смотрит на Монику
    img 21940
    m "..." # растерянно
    img 21941
    m "Ничего!"
    m "..."
    m "Ты нашла флешку?!" # строго
    # Юлия встает, с непонимающим видом
    img 21942
    julia "Да, Миссис Бакфетт... Она лежит у вас на столе." # на полке
    img 21943
    m "..."
    img 21944
    julia "..."
    # Моника с покер-фейсом протягивает руку
    img 21945
    m "Давай ее мне!"
    # Юлия подходит, отдает флешку, смотрит на Монику вопросительно
    img 21946
    julia "???"
    # Моника делает вид, что ничего не произошло
    img 21947
    m "А теперь иди работай! Не отвлекайся!"
    # садится за свой стол и прячется за монитором
    img 21948
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
    img 21949
    mt "Не могу поверить! Мне приходится выяснять, какие трусики носит моя секретарша!!!"
    mt "И все из-за этого мерзавца Фреда!"
    mt "Как-будто без этого у меня мало забот!"
    mt "Я здесь начальник! Мне нужно думать о работе целого отдела и о том, как вернуть назад мою компанию, а не о трусиках секретарши!"
    img 21950
    mt "..."
    mt "Как мне посмотреть на трусики Юлии?"
    mt "И чтобы она ничего не заподозрила..."
    img 21951
    w
    img 21952
    mt "Хм..." # с улыбочкой
    # Моника садится за свой стол. Потом тоном босса подзывает Юлию.
    img 21953
    m "Юлия! Подойди ко мне!"
    # Юлия подходит к Монике
    img 21954
    julia "Да, Миссис Бакфетт?"
    img 21955
    m "Юлия! Мне срочно для работы нужна папка с отчетами за прошлый год!"
    m "Достань мне ее!" # строго
    img 21956
    julia "Хорошо, Миссис Бакфетт. А где эта папка?"
    img 21957
    m "Эта папка стоит в шкафу на верхней полке."
    # Юлия смотрит на шкаф, никаких документов там нет, смотрит на Монику
    img 21958
    julia "М-м-Миссис Бакфетт... Там на полках... Там нет никаких папок и документов..."
    img 21959
    mt "..."
    img 21960
    m "Юлия! Я тебе говорю, что эта папка там есть! Достань мне ее!" # раздраженно
    m "Срочно!!!"
    # Юлия растерянно
    img 21961
    julia "Да, Миссис Бакфетт... Я сейчас принесу стул..."
    # Юлия ставит стул, встает на него и тянется к верхней полке, где нет документов. Ее платье немного приподнимается
    img 21962
    w
    img 21963
    w
    img 21964
    m "..."
    img 21965
    menu:
        "Заглянуть Юлии под платье.": #corruption
            pass
        "Не заглядывать.":
            mt "Нет, я не буду этого делать!" # сердито
            mt "Мне надоело играть по правилам этого мерзавца!"
            mt "Он здесь никто, чтобы приказывать МНЕ, Монике Бакфетт!!!"
            return 1
    # Моника пытается заглянуть ей под платье, но ей ничего не видно
    img 21966
    mt "Черт! Еще чуть-чуть и я увижу ее трусики!"
    img 21967
    julia "Миссис Бакфетт, здесь нет никаких документов..."
    img 21968
    w
    img 21969
    m "..."
    img 21970
    m "Посмотри внимательнее, Юлия!" # строго
    # Юлия пытается найти папку, а Моника пытается заглянуть ей под платье
    img 21971
    w
    img 21972
    w
    img 21973
    julia "Все равно мне ничего не видно!"
    img 21974
    julia "???"
    img 21975
    w
    img 21976
    w

    # Юлия поворачивает голову и видит, что Моника заглядывает ей под платье
    img 21977
    julia "!!!" # удивленно
    img 21978
    m "Ну же!"
    img 21979
    julia "Миссис Бакфетт... Что в-в-вы д-делаете?"  # вопросительно смотрит на Монику
    # Моника делает вид, что ничего не произошло
    img 21980
    m "..." # растерянно
    m "Ничего!"
    img 21981
    julia "???"
    img 21982
    m "..."
    m "Ты нашла папку с отчетами, Юлия?!" # строго
    # Юлия с непонимающим видом спускается со стула
    img 21983
    julia "Нет, Миссис Бакфетт... На полке нет ничего."
    julia "..."
    img 21984
    m "..."
    # Моника с серьезной миной
    m "Ты плохо искала, Юлия! Тебе ничего нельзя доверить!"
    img 21985
    julia "???"
    julia "Н-но..."
    img 21986
    m "А теперь иди работай! И не отвлекайся!"
    # Юлия возвращается за свой стол, Моника прячется за монитором
    img 21987
    mt "Вот черт! Ничего не получилось!"
    img 21988
    mt "Более того, она увидела, как я пыталась заглянуть ей под платье!!!"
    mt "Какой кошмар!!!"
    img 21989
    mt "!!!"
    mt "Мне нужно будет придумать еще что-нибудь..."
    mt "Иначе мерзавец Фред не оставит меня в покое..."
    return

# Работа в офисе. Гримерка.
# Моника сталкивается с Фредом. Разговор Фреда и Моники.
label ep28_dialogues6_julia_4:
    # Моника возмущенно
    img 21884
    m "Это снова ты?!"
    # Фред ей отвечает спокойно
    img 21885
    fred "Миссис Бакфетт... Это непрофессионально с вашей стороны не выполнять условия нашей договоренности..."
    img 21886
    m "!!!" # зло смотрит на него
    menu:
        "Отказаться выполнять дурацкие приказы этого мерзавца!": # если отказалась заглядывать под юбку Юлии
            # Моника орет на Фреда
            img 21882
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
    img 21887
    fred "Вы так и не сделали, что я вам сказал, Миссис Бакфетт?"
    # Моника убийственно смотрит на него, но молчит
    img 21886
    m "..."
    # Фред с улыбочкой
    img 21887
    fred "Так уж и быть, Миссис Бакфетт. Я готов подождать еще немного..."
    img 21888
    m "..."
    fred "Я не сомневаюсь, что у вас все получится, Миссис Бакфетт."
    fred "Я с нетерпением буду ждать вашего ответа."
    fred "До скорой встречи, Миссис Бакфетт."
    return


# Кабинет Моники. Следующий день.
label ep28_dialogues6_julia_5:
    # Моника стоит у себя в кабинете, Юлия сидит за своим столом
    img 21990
    mt "Не могу поверить! Мне приходится выяснять, какие трусики носит моя секретарша!!!"
    mt "Я здесь начальник! Мне нужно думать о работе целого отдела, а не о трусиках секретарши!"
    img 21991
    mt "..."
    mt "Как мне посмотреть на трусики Юлии?"
    mt "И чтобы она ничего не заподозрила..."
    img 21992
    mt "Хм..." # с улыбочкой
    mt "Собственно, какая мне разница, что она подумает?"
    mt "Она же просто секретарша!"
    mt "А мне надо скорее заканчивать с этими дурацкими заданиями Фреда!"
    img 21993
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
    img 21994
    w
    img 21995
    w
    img 21996
    w
    img 21997
    w
    img 21998
    julia "Миссис Бакфетт! Что вы делаете?!"
    img 21999
    m "Ничего!"
    m "Сиди и работай!"
    m "И не отвлекайся!"
    img 22000
    julia "М-м-Миссис Бакфетт... Вы что-то потеряли? Вам помочь?" # растерянно
    img 22001
    mt "Да!!! Раздвинь ноги и покажи свои трусики!"
    img 22002
    m "Нет!!! Я сама! Сиди и работай!"
    # Моника все это время пытается посмотреть, в каких трусиках Юлия, но ей ничего не видно
    img 22003
    mt "Еще чуть-чуть и я увижу ее трусики!"
    mt "!!!"
    img 22004
    m "Отодвинь ногу, Юлия! Она мне мешает!"
    # Юлия вскакивает со своего стула
    img 22005
    julia "Миссис Бакфетт! Мне кажется или вы пытаетесь... Вы..."
    img 22006
    m "!!!"
    # Юлия смущается, Моника поднимается с пола
    img 22007
    m "Тебе кажется, Юлия!!!" # строго
    m "Я..."
    m "Я просто потеряла кое-что! Иди работай!"
    # Юлия возвращается за свой стол, Моника садится за свой стол и прячется за монитором
    img 22008
    mt "Вот черт! Снова ничего не получилось!"
    mt "Более того, эта Юлия поняла, что я пыталась заглянуть ей под платье!!!"
    mt "Какой кошмар!!!"
    img 22009
    mt "!!!"
    mt "Что же мне еще придумать?.."
    mt "Пора уже заканчивать с этим! Сколько можно заниматься этими глупостями?!"
    return

# В конце рабочего дня, когда Моника лезла к Юлии под стол.
# Гримерка. Моника сталкивается с Фредом. Разговор Фреда и Моники.
label ep28_dialogues6_julia_6:
### Нет понятия "последний день". Фред говорит просто поторопиться. (не привязываемся к таймингу) +
    # Моника возмущенно
    img 21889
    m "ФРЕД!!!"
    m "Перестань меня преследовать!!!"
    # Фред ей отвечает спокойно
    fred "Миссис Бакфетт... Вы выяснили то, о чем я вас просил?"
    img 21890
    m "!!!" # зло смотрит на него
    mt "Ненавижу этого мерзавца!"
    menu:
        "Отказаться выполнять дурацкие приказы этого мерзавца!": # если отказалась заглядывать под юбку Юлии
            # Моника орет на Фреда
            img 21891
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
    img 21892
    fred "Миссис Бакфетт, я все понимаю. Но прошу вас поторопиться."
    fred "С вашей стороны непрофессионально заставлять меня ждать так долго."
    img 21893
    m "..." # сердито
    m "Я не знаю, как сделать это!"
    m "Может, ты, как профессионал, подскажешь мне?"
    img 21894
    fred "Не вижу в этом проблемы, Миссис Бакфетт."
    fred "Просто наденьте трусики Юлии..."
    img 21895
    m "???" # как на идиота
    img 21896
    fred "Вы же любите их носить, Миссис Бакфетт?"
    img 21897
    m "Нет, конечно!!! Что за глупости?!" # возмущается
    img 21898
    fred "И покажите ей, что вы носите ее трусики..."
    fred "А она покажет вам свои трусики в ответ."
    img 21899
    mt "Что за чушь он говорит?!"
    img 21892
    fred "Я не сомневаюсь, что у вас все получится, Миссис Бакфетт."
    fred "Я с нетерпением буду ждать вашего ответа."
    fred "До скорой встречи, Миссис Бакфетт."
    img 21900
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
    img 22009
    mt "Не могу поверить!"
    mt "Я собираюсь показывать своей секретарше, в каких я трусиках!!!"
    img 22010
    mt "А вдруг она узнает свои трусики?!"
    mt "Не могу же я признаться ей в том, что я ношу ЕЕ трусики!"
    mt "Я, Моника Бакфетт, ношу трусики своей бывшей гувернантки!"
    img 22011
    mt "Хотя... Я сама в это с трудом верю, а Юлия тем более не поверит..."
    img 22012
    mt "..."
    m "Юлия!"
    img 22013
    julia "Да, Миссис Бакфетт?" # вопросительно
    img 22014
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
    img 22015
    m "Хм... Юлия, ты знаешь..."
    m "..."
    m "Несмотря на то, что я иногда была немного строга с тобой..."
    m "Мне нравилось, как ты работала у меня гувернанткой."
    # Юлия крайне удивлена, смотрит на Монику
    img 22016
    julia "Это правда, Миссис Бакфетт?.."
    img 22017
    m "Да, Юлия..."
    img 22018
    julia "А я думала, что... Вы... В общем..."
    m "Мне правда все нравилось. Думаю, весьма непросто найти гувернантку лучше, чем ты."
    img 22019
    mt "Черт!!! Я не могу этого сказать!"
    img 22020
    m "После того, как ты перестала работать, я увидела в твоей комнате твои трусики..." # выдавливает из себя
    m "И мне они очень понравились..."
    img 22021
    m "..."
    m "И я себе купила такие же..."
    img 22022
    julia "!!!"
    img 22023
    mt "Я не верю, что я говорю это! Я говорю это своей секретарше!!!"
    # Юлия смотрит с недоверием
    img 22024
    julia "Купили себе трусики, как у меня?!"
    img 22025
    m "Да, Юлия. Ты мне не веришь?"
    # Юлия, смутившись
    img 22026
    julia "Если быть честной, Миссис Бакфетт, то я... Я сомневаюсь, что Вы говорите правду..."
    img 22027
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
    img 22028
    m "Вот смотри! Они сейчас на мне!"
    # Юлия смотрит на трусики, она в шоке
    img 22029
    w
    img 22030
    julia "Это не такие же трусики как у меня... Это..."
    img 22031
    julia "Миссис Бакфетт... Это мои трусики..."
    img 22032
    julia "Я узнаю их!"
    # Моника стыдится
    img 22033
    mt "Боже! Какая глупая ситуация!"
    mt "И как мне теперь выкрутиться из нее?"
    img 22034
    mt "..."
    m "Но ведь правда они красивые?" # сквозь зубы
    img 22035
    julia "Вообще-то, Миссис Бакфетт, они ужасные. Я ненавидела носить их."
    # Моника молча смотрит на нее, опускает платье
    img 22036
    mt "!!!"
    img 22037
    mt "Пора заканчивать весь этот цирк!"
    img 22038
    m "Юлия, я тебе показала свои трусики. Теперь я хочу увидеть твои!"
    # Юлия офигевает
    img 22039
    julia "Что???"
    julia "Нет! Я не буду вам ничего показывать, Миссис Бакфетт!"
    # Моника требовательно
    sound down9
    img 22040 # падает стул
    w
    img 22041
    m "Юлия, просто покажи мне их и все. Я просто хочу посмотреть."
    julia "Нет, Миссис Бакфетт! Я вам ничего не покажу!"
    img 22042
    julia "Нет!"
    julia "Извините, но нет!"
    img 22043
    julia "Мне надо идти работать..."
    # Юлия продолжила работу, сидит за своим столом и косо посматривает на Монику
    # Моника садится за свой стол и прячется за монитором
    img 22044
    mt "Вот черт! Это было так ужасно!"
    mt "Такая глупая ситуация!!!"
    mt "!!!"
    img 22045
    mt "И снова ничего не получилось!"
    mt "Эта Юлия теперь думает, что я пристаю к ней!"
    mt "Я, Моника Бакфетт, пристаю к какой-то секретарше!!!"
    img 22046
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
    img 21901
    m "Фред!"
    m "Сколько можно за мной ходить?!"
    img 21902
    mt "Я сегодня так и не узнала цвет трусиков Юлии. Что же делать?"
    # Фред ей отвечает спокойно
    img 21903
    fred "Миссис Бакфетт... Вы выяснили то, о чем я вас просил?"
    img 21904
    m "!!!" # зло смотрит на него
    mt "Ненавижу этого мерзавца!"
    menu:
        "Отказаться выполнять дурацкие приказы этого мерзавца!": # если поднимала платье перед Юлией
            # Моника орет на Фреда
            img 21910
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
            img 21905
            m "Да, я выяснила!!!"
            m "Она носит трусики белого цвета!"
            m "..."
        "Юлия носит трусики красного цвета!":
            img 21905
            m "Да, я выяснила!!!"
            m "Она носит трусики красного цвета!"
            m "..."
        "Юлия носит трусики синего цвета!":
            img 21905
            # Моника сердито, сложив руки
            m "Да, я выяснила!!!"
            m "Она носит трусики синего цвета!"
            m "..."
    # Фред с улыбочкой
    img 21906
    fred "Миссис Бакфетт, обман - это непрофессионально."
    fred "Но я вас прощаю на первый раз..."
    # Моника зло смотрит на него
    img 21907
    m "..."
    mt "Я уже несколько дней потратила на выяснение цвета трусиков секретарши..."
    mt "Мне все это надоело уже!!!"
    img 21908
    fred "Я не сомневаюсь, что у вас все получится, Миссис Бакфетт."
    fred "Я с нетерпением буду ждать вашего ответа."
    fred "До скорой встречи, Миссис Бакфетт."
    # Фред уходит
    img 21909
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
