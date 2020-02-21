default monicaBiffPhotoshootInvestor1 = False  # Моника с 1-го раза согласилась фотографироваться в платье Королева сердец
default monicaBiffPhotoshootInvestor2 = False  # Моника со 2-го раза согласилась фотографироваться в платье Королева сердец

# другой день после паблик ивента, Моника приходит на работу в офис
label ep211_dialogues3_photoshoot_1:
    # не рендерить!
    mt "Сегодня у меня фотосессия в каком-то наряде от инвестора."
    mt "Надеюсь, это будет приличный наряд..."
    return

# офис, кабинет Бифа
label ep211_dialogues3_photoshoot_2:
    # Моника заходит в кабинет, там сидит инвестор на стуле перед проектором
    # Биф показывает ему фотки с ее фотосессии в костюме черного лебедя
    img 16867
    w
    img 16868
    w
    img 16869
    w
    img 16870
    mt "!!!"
    img 16872
    biff "В скором времени, Я планирую опубликовать эти кадры в широкий доступ."
    img 16873
    mt "ЧТО-О-О?!"
    mt "!!!!!"
    # инвестор говорит, внимательно рассматривая кадры
    img 16874
    campbell "Опубликуйте их после фотосессии в моем платье 'Королева сердец'."
    campbell "Если вы их опубликуете до этой фотосессии..."
    campbell "То снимки в моем платье будут публике неинтересны."
    img 16875
    biff "Конечно, Мистер Кэмпбелл!"
    biff "Кстати, Миссис Бакфетт уже пришла на фотосессию."
    img 16876
    biff "Можете проходить в фотостудию, Мистер Кэмпбелл."
    campbell "Да, спасибо."
    img 16877
    w
    img 16878
    # инвестор уходит в фотостудию
    # Моника орет на Бифа
    img 16879
    m "Биф!"
    m "Зачем ты показал эти фотографии инвестору?!"
    m "!!!"
    img 16880
    biff "Я тебя забыл спросить, кукла безмозглая, что мне делать!"
    biff "Ты не задаешь вопросы, когда сосешь на улице члены за $ 20!.."
    biff "Но пытаешься спорить, когда я показываю твою задницу, даже без члена в ней, состоятельному инвестору!"
    biff "Не забывай, какае деньги я плачу тебе, кукла!"
    m "!!!"
    img 16881
    biff "Хватит орать тут и быстро иди переодевайся!"
    biff "Тебя ждет Мистер Кэмпбелл. И только попробуй сорвать эту фотосессию!!!"
    biff "Я тебя в один миг вышвырну отсюда на улицу!!!"
    img 16882
    mt "ААААААА!"
    mt "НЕНАВИЖУ!!!"
    mt "УБЬЮ!!!"
    $ log1 = _("Идти в фотостудию и переодеться.")
    return


# фотостудия
label ep211_dialogues3_photoshoot_3:
    # Моника заходит в фотостудию, разговор с Алексом, как обычно
    # в меню выбора новый костюм. Моника переодевается и выходит к Алексу, прикрывшись руками
    # начинает возмущаться
    img 23193
    m "Алекс!!!"
    m "Это разве платье?!?!?!"
    m "Эта тряпка на мне совсем не закрывает мою грудь!!!"
    m "Алекс, как я буду сниматься в этом?! Да еще и при этом инвесторе?!"
    # Алекс пускает слюни и пялится на Монику
    img 23194
    alex_photograph "Миссис Бакфетт, не переживайте."
    alex_photograph "Это платье очень Вам идет! Вы в нем настоящая королева!"
    alex_photograph "Я буду делать кадры, на которых ничего не будет видно."
    # Моника смотрит на него недоверчиво
    img 23195
    mt "Этот фотограф-извращенец всегда так говорит, а в итоге..."
    mt "Нужно сходить к Бифу и послать его к черту!"
    mt "Или пусть предоставит другое платье!"
    mt "Или фотосессия отменяется!"
    $ log1 = _("Пойти к Бифу.")
    return

# офис, кабинет Бифа
label ep211_dialogues3_photoshoot_4:
    # Моника, прикрывшись руками, заходит в кабинет Бифа и орет
    img 16856
    w
    img 16857
    m "Биф, я не буду фотографироваться в ЭТОМ!!!"
    m "Это не платье!"
    m "У меня вся грудь открыта в нем!!!"
    m "!!!"
    img 16858
    biff "У тебя, кукла, никто не спрашивал!"
    img 16859
    m "Биф, я предупреждаю, что я не буду делать никаких откровенных кадров!"
    m "Я соглашусь на кадры только с прикрытой грудью!"
    img 15902
    biff "А я тебя предупреждаю, что если Кэмпбелл откажется инвестировать..."
    biff "То виновата в этом будешь ты, кукла безмозглая!"
    biff "У тебя не хватает мозгов понять, что от этой фотосессии многое зависит?"
    img 16860
    biff "Проведи ее и чтобы никаких глупостей!"
    biff "Это твоя работа! Ты получаешь за это немаленькие деньги!"
    biff "Иди в фотостудию!"
    # Моника зло
    img 16861
    mt "Мерзавец!"
    mt "!!!"
    menu:
        "Идти в фотостудию и провести фотосессию в платье 'Королева сердец'.": #corruption
            $ monicaBiffPhotoshootInvestor1 = True # Моника с 1-го раза согласилась фотографироваться в платье Королева сердец
            pass
        "Я не буду участвовать в этом!!!":
            img 16863
            m "Биф, я не буду фотографироваться в этом платье!"
            m "Да еще в присутствии этого инвестора!"
            img 16864
            m "Я не хочу, чтобы он на меня пялился!"
            m "Почему я?! Почему не Мелани?"
            img 15870
            biff "Потому что Мистер Кэмпбелл так хочет!"
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            img 16865
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя фотографироваться с членом во рту!"
            img 16862
            mt "!!!"
            mt "Чертов Мистер Кэмпбелл! Чертов Биф! Ненавижу их всех!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return
    img 16862
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "А мне нужны деньги."
    mt "Где я смогу заработать 5 тысяч в месяц для сучки Виктории?"
    img 16866
    m "Я проведу эту фотосессию..."
    img 16865
    biff "Иди в фотостудию."
    img 16861
    mt "Чертов Биф!"
    mt "На публичном вечере я всем сказала, что публика никогда не увидит мою грудь!"
    mt "Что я всем им скажу теперь?! О ужас!!!"
    mt "!!!"
    $ log1 = _("Идти в фотостудию и провести фотосессию.")
    return

# если Моника отказалась фотографироваться в этом платье и оказалась на улице, но потом передумала и пришла к Бифу
# офис, кабинет Бифа
label ep211_dialogues3_photoshoot_5:
    img 13891
    m "Биф..."
    m "Мне нужна работа."
    img 13892
    biff "Если цыпочка хочет работать, она сделает фотосессию."
    biff "В платье от инвестора и в его присутствии."
    img 13900
    m "..."
    img 13906
    biff "Ты согласна?"
    mt "!!!"
    menu:
        "Идти в фотостудию и провести фотосессию в платье 'Королева сердец'.": #corruption
            $ monicaBiffPhotoshootInvestor2 = True # Моника со 2-го раза согласилась фотографироваться в платье Королева сердец
            pass
        "Я не буду участвовать в этом!!!":
            img 15896
            m "Нет! Я не буду фотографироваться в этом платье!"
            m "Да еще в присутствии этого инвестора!"
            m "Я не хочу, чтобы он на меня пялился!"
            img 15906
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            img 15902
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя фотографироваться с членом во рту!"
            img 12792
            mt "!!!"
            mt "Чертов Мистер Кэмпбелл! Чертов Биф! Ненавижу их всех!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return
    img 12810
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "А мне нужны деньги."
    mt "Где я смогу заработать 5 тысяч в месяц для сучки Виктории?"
    img 12792
    mt "..."
    mt "На публичном вечере я всем сказала, что публика никогда не увидит мою грудь!"
    mt "Что я всем им скажу теперь?! О ужас!!!"
    mt "..."
    img 12799
    m "Я проведу эту фотосессию..."
    img 12815
    biff "Иди переодевайся."
    biff "Я пока позвоню Мистеру Кэмпбеллу, чтобы приехал на съемку."
    img 12809
    mt "..."
    $ log1 = _("Идти в фотостудию и провести фотосессию.")
    return


# фотостудия, Моника в платье Кролева сердец
label ep211_dialogues3_photoshoot_6:
    # Моника с угрозой обращается к Алексу
    img 23196
    m "Алекс!"
    m "Только попробуй взять ракурс, где будет видна моя... моя..."
    # Моника замолкает, так как в фотостудию заходит инвестор
    img 23197
    campbell "Миссис Бакфетт, Вам нравится платье, которое я Вам подбрал?"
    # Моника сердито смотрит на него, продолжая прикрывать грудь руками
    img 23198
    mt "Биф сказал, что от этой фотосессии зависит решение этого неудачника..."
    mt "Если я сделаю что-то не так, он откажется от инвестирования в журнал..."
    mt "Тогда Биф выгонит меня с этой работы..."
    mt "А мне нужны деньги для этой сучки Виктории."
    mt "Черт!!!"
    # Моника сквозь зубы
    menu:
        "Платье мне нравится, Мистер Кэмпбелл...":
            pass
    img 23199
    m "Платье мне нравится, Мистер Кэмпбелл..."
    m "Только мне кажется, что оно несколько откровенное..."
    img 23200
    campbell "Вы сами мне сказали, что поддерживаете новый курс журнала."
    campbell "Я подобрал платье в соответствии с курсом Вашего журнала."
    img 23201
    campbell "И нахожу его весьма подходящим для Вас, Миссис Бакфетт."
    # инвестор садится на стул напротив съемочной площадки и с надменным видом смотрит на Монику
    img 23202
    campbell "Приступайте!"
    # Моника
    img 23203
    mt "Мерзкий тип!"
    mt "Скорее надо провести эту долбанную фотосессию..."
    mt "И пусть он убирается отсюда!"
    img 23204
    alex_photograph "Приступим, Миссис Бакфетт."
    return

# фотосессия
label ep211_dialogues3_photoshoot_7:
    # во время фотосессии периодически показывается лицо инвестора, который пристально смотрит на Монику, рассматривает ее
    # каждый раз, когда Моника отказывается принимать какую-либо позу, она смотрит на инвестора
    img 23205
    alex_photograph "Миссис бакфетт. Пожалуйста, уберите руки от груди, мне надо сделать кадр."
    m "Алекс, сделай кадр как есть, затем я уберу руки..."
    mt "Дьявол!"
    mt "Это все слишком далеко зашло..."
    #up
    img 23206
    #left
    img 23207
    #down
    img 23208

    alex_photograph "А теперь уберите руки, миссис бакфетт, пожалуйтса."
    alex_photograph "Иначе я не смогу сделать работу, которую мне поручил мой босс и мне будет выговор."
    menu:
        "Обнажить грудь.":
            pass
        "Уйти.":
            m "С меня хватит!"
            m "Я не собираюсь завершать эту пошлую фотосессию!"
            return False
    img 23209
    mt "Боже мой! не могу поверить что я это делаю!"
    mt "Я, моника бакфетт..."
    mt "Обнажить грудь, перед камерой..."
    mt "В своем же собственном журнале..."
    mt "Как же до этого могло дойти?!"
    mt "Ведь это увидит весь мир! Абсолютно весь!"
    mt "О Боже!!!"

    #photo
    img 23210
    alex_photograph "Не переживайте, миссис бакфетт!"
    alex_photograph "Я буду фотографировать так, чтобы ничего не было видно!"
    m "Точно?"
    alex_photograph "Конечно, миссис бакфетт!"
    #up
    img 23211
    #left
    img 23212
    #down
    img 23213

    #photo
    img 23214
    #up
    img 23215
    #left
    img 23216
    #down
    img 23217


    #4
    #photo
    img 23218
    alex_photograph "Миссис Бакфетт! Пожалуйста, сядьте пораскованнее."
    alex_photograph "Не зажимайтесь!"
    m "Но так будет все очень хорошо видно!"
    alex_photograph "Миссис Бакфетт, не волнуйтесь!"
    alex_photograph "Свет от софитов засвечивает снимок и видно только ваше лицо!"
    #up
    img 23219
    #left
    img 23220
    #down
    img 23221
    m "Алекс, не фотографируй так, чтобы были видны мои ноги или... что-нибудь выше..."
    alex_photograph "Не переживайте, миссис бакфетт!"
    alex_photograph "Я ни в коем случае не возьму такой кадр!"

    #5
    #photo
    img 23222
    alex_photograph "Миссис Бакфетт, встаньте, пожалуйста, на трон."
    alex_photograph "Так будет лучше видно вашу королевскую фигуру!"
    m "Алекс, только фотографируй так, чтобы ничего не было видно!"
    #up
    img 23223
    #left
    img 23224
    #down
    img 23225

    #6
    #photo
    img 23226
    #up
    img 23229
    #left
    img 23228
    #down
    img 23227

    #7
    #photo
    img 23230
    #up
    img 23231
    #left
    img 23232
    #down
    img 23233

    #8
    #photo
    img 23234
    m "Алекс, не бери близко кадр!"
    m "Будет все видно!"
    alex_photograph "Не волнуйтесь, Миссис Бакфетт!"
    alex_photograph "Я снимаю под таким углом, что форму груди будет не видно!"
    #up
    img 23235
    #left
    img 23236
    #down
    img 23237

    #photo
    img 23238
    #up
    img 23239
    #left
    img 23240
    #down
    img 23241

    #photo
    img 23242
    alex_photograph "Миссис Бакфетт!"
    alex_photograph "Пожалуйста, оставьте ножки раздвинутыми, а сами откиньтесь на спинку трона."
    alex_photograph "И примите расслабленное положение!"
    alex_photograph "Это будет великолепный кадр!"
    m "Алекс, ни за что!"
    m "Ты ведь знаешь что там у меня ничего нет!"
    m "Даже на рассчитывай на это!"
    alex_photograph "Но Миссис Бакфетт, Мистер Биф сказал, что..."
    m "Мне плевать что он сказал!"
    m "Я не собираюсь брать такие пошлые кадры!"
    m "Фотографируй как есть, иначе я вообще сейчас уйду!"
    #up
    img 23243
    #left
    img 23244
    #down
    img 23245
    w
    img 23246
    biff "Как проходит фотосессия, Мистер Кэмпбелл?"
    biff "Довольны-ли Вы всем?"
    biff "Вы уже приняли окончательное решение по поводу инвестирования в журнал?"
    img 23247
    campbell "Вы знаете, у меня сомнения по этому поводу."
    campbell "Вы, как личный менеджер Миссис Бакфетт, дали мне гарантию по поводу курса журнала и его содержания."
    campbell "Однако, я вижу что Миссис Бакфетт вовсе не поддерживаю ею же задекларированный курс."
    img 23248
    biff "???"
    campbell "Вместо этого, она стесняется и отказывается принимать некоторые позы, которые очень бы подошли моему наряду."
    img 23249
    biff "О, Мистер Кэмпбелл, не волнуйтесь!"
    biff "Миссис Бакфетт, действительно, немного стесняется при посторонних."
    biff "Это эмоции, вы же знаете женщин, Мистер Кэмпбелл."
    biff "Но я сейчас ее успокою и сделаю убеждение расслабиться перед камерой."
    img 23250
    biff "Ведь Миссис Бакфетт также как и я понимает всю важность вашего решения касаемо инвестиций в журнал..."
    m "!!!"
    img 23251
    biff "Как Вы хотите продолжить фотосессию?"
    biff "Хотите, Миссис Бакфетт обнажится полностью и примет любую позу, которые Вы пожелаете..."
    biff "Или, если хотите, можно пригласить мужскую модель и сделать фотосессию совокупления."
    biff "Это может сразу повысить рейтинги нашего с Вами журнала!"
    img 23252
    m "ЧТО?!!!"
    img 23253
    campbell "Нет, Мистер Биф. Давайте не будем торопиться."
    campbell "Я бы не хотел портить впечатление зрителей от закрытой фотосессии, которую Вы вскоре собираетесь опубликовать."
    campbell "И я бы не хотел, чтобы Миссис Бакфетт снимала платье, я не хочу лишаться рекламы моего бренда."
    campbell "Будет достаточно лишь немного приоткрыть его."
    campbell "В другой раз, я предоставлю соответствующий наряд и мы значительно продвинемся в направлении нового курса журнала."
    biff "Да, Мистер Кэмпбелл, конечно!"

    img 23254
    biff "Кукла, у тебя что, совсем закончились твои куриные мозги?!"
    biff "Ты вообще понимаешь перед кем ты здесь ломаешься?!"
    biff "Это Мистер Кэмпбелл, один из самых богатых людей этого города!"
    biff "Будь рада что он вообще пока еще не раскусил то, что ты поддельная резиновая кукла!"
    biff "Потому, встань в ту позу, которую он пожелал."
    img 23255
    biff "Отвлеки его взгляд от своей глупой кукольной модрашки, чтобы продолжить оставаться неузнанной."
    biff "Пока он думает, что ты Моника Бакфетт, он готов инвестировать в наш журнал!"
    img 23256
    m "Биф, но я..."
    m "Это ведь публичная фотосессия!"
    biff "Если ты сейчас же не сделаешь что я тебе говорю, ты вылетишь отсюда и никогда больше не попадешь в этот шикарный офис!"
    biff "Я считаю до трех!"
    biff "Раз..."
    img 23257
    mt "О Боже! Что мне делать?!"
    biff "Два..."
    img 23258
    mt "Кэмпбелл сказал, что надо лишь немного приоткрыть платье..."
    mt "Может быть не будет ничего видно?"
    img 23259
    biff "Три!"
    menu:
        "Сделать как требует Биф.":
            pass
        "Уйти (конец квестов, связанных с офисом).":
            img 23278
            m "Я не собираюсь участвовать в этом фарсе!"
            m "Прощайте, мерзавцы!!!"
            return False
    mt "У меня нет выбора!"
    mt "Если у меня не будет денег от этих фотосессий, то Виктория скажет Дику бросить мое дело!"
    mt "И я окажусь в руках Маркуса и тех, кто стоит за ним!"
    mt "А там меня ждет... О Ужас!!!"
    mt "У меня нет выбора!"

    #photo
    img 23260
    biff "Мистер Кэмпбелл. я убедил Миссис Бакфетт."
    campbell "Вы отличный личный менеджер, Биф! вы знаете подход к своему Боссу!"
    biff "Спасибо, Мистер Кэмпбелл!"
    biff "Вас устраивает поза Миссис Бакфетт?"
    biff "Хотите мы снимем это платье и повесим рядом, чтобы был виден Ваш бренд?"
    campbell "Нет, Мистер Биф. Все в порядке."
    campbell "Так вполне достаточно. Для этого раза..."

    #up
    img 23261
    img 23262

    #left
    img 23263
    img 23264
    img 23265
    #down
    img 23266
    img 23267
    img 23268
    img 23269
    img 23270
    img 23271
    img 23272
    img 23273
    img 23274
    img 23275
    mt "Мне нужно, чтобы он согласился вложить деньги в журнал..."
    mt "Если я сорву эту фотосессию, то этот неудачник просто откажется."
    mt "Биф сказал, что выгонит меня с работы, если хоть одни из инвесторов откажется..."

    # фразы Моники во время позирования для Алекса:
    m "Алекс, ты помнишь, что ты мне обещал перед началом съемки?"
    alex_photograph "Да, конечно, Миссис Бакфетт."
    alex_photograph "Я все сделаю, как надо, не переживайте."
    m "Алекс, эта поза не будет хорошо смотреться в кадре..."
    alex_photograph "Что вы, Миссис Бакфетт, это будет просто великолепный кадр!"
    m "Алекс! Снимай меня с другого ракурса!!"
    alex_photograph "Да, конечно. Сейчас еще один снимок и я возьму другой ракурс."
    m "Алекс, ты уверен, что в таком ракурсе не будет видно ничего лишнего?"
    alex_photograph "Конечно, Миссис Бакфетт! Вы можете мне довериться."
    m "Алекс, не снимай меня крупным планом! Ты забыл, что ты мне обещал?"
    alex_photograph "Я помню, Миссис Бакфетт. Кадры получаются отличные!"
    alex_photograph "Вам очень идет это платье! Настоящая королева!"
    m "Алекс, я не буду вставать в такую позу!"
    # инвестор
    campbell "Кхм... Эта поза как нельзя лучше демонстрирует платье..."
    campbell "И характеризует новый курс вашего журнала, Миссис Бакфетт..."
    mt "!!!"
    alex_photograph "Согласен. Миссис Бакфетт, это очень интересный ракурс."
    alex_photograph "Ничего лишнего в кадре не будет видно, не переживайте."
    m "Ты уверен в этом, Алекс?"
    alex_photograph "Конечно. Я Вам обещаю, Миссис Бакфетт!"


    # после фотосессии инвестор смортит на Монику, она прикрывает грудь руками
    img 23276
    campbell "Благодарю. Мне было любопытно поприсутствовать."
    # инвестор встает со стула и уходит
    img 23277
    mt "Куда этот неудачник пошел?"
#    mt "А если он пошел к Бифу и сейчас скажет ему, что отказывается?!"
#    mt "Тогда я не смогу больше здесь работать!!!"
    mt "Мне нужно переодеться и идти к Бифу."
    mt "Нужно узнать, что решил этот мерзкий Мистер Кэмпбелл..."
    $ log1 = _("Пойти кв кабиент к Бифу и узнать, что решил инвестор.")
    return

# кабинет Бифа
label ep211_dialogues3_photoshoot_8:
    # заходит к Бифу, тот стоит вместе с инвестором
    # жмут друг другу руки
    img 16883
    w
    img 16884
    biff "Мистер Кэмпбелл, я уверен, что вы сделали правильный выбор!"
    img 16885
    campbell "Посмотрим."
    campbell "Будем надеяться, что это будет выгодная сделка для нас обоих..."
    img 16886
    biff "Конечно, Мистер Кэмпбелл!"
    biff "С Вами приятно сотрудничать."
    # инвестор смотрит на часы
    campbell "Я уже опаздываю на важную встречу."
    biff "Как я Вам уже говорил, мы будем рады видеть Вас снова в нашем офисе!"
    # инвестор проходит мимо Моники
    img 16887
    campbell "Миссис Бакфетт, надеюсь, это была не последняя фотосессия..."
    campbell "На которую я был приглашен..."
    mt "???"
    # Моника грозно смотрит на Бифа, тот стоит довольный
    img 16888
    m "До свидания, Мистер Кэмпбелл."
    # инвестор уходит
    # Биф довольный, садится на свой стул
    img 12785
    biff "Папочка доволен, что цыпочка смогла убедить первого инвестора."
    biff "Но папочка недоволен тем, что осталось еще пять колеблющихся инвесторов..."
    biff "Цыпочка должна проявить свои таланты убеждения..."
    img 12865
    biff "Полученные ею в прошлой жизни на грязной улице."
    biff "Иначе цыпочка рискует вернуться к ней!"
    # Моника
    img 12792
    mt "!!!"
    mt "Вот сволочь!!!"
    return
