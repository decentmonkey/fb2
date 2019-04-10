label ep24_dialogues5_betty1:
# На следующий день, при попытке войти в любую локацию дома, происходит сцена разговора Бетти и Моники
# (Барди подглядывает)
# Бетти окликает Монику.
# Бетти напряжена и недовольна.
# Бетти говорит Монике что узнала кое-что о Монике.
    if cloth != "Governess":
        return False
    img 10331
    betty "Эй! Моника, гувернантка!"
    img 10332
    m "???"
    img 10333
    betty "Подойди-ка сюда..."
    img 10334
    m "..."
    m "Да, Миссис Робертс. Чем могу быть полезна?"
    betty "..."
    img 10335
    betty "Гувернантка, я кое-что узнала о тебе..."

# Моника напряжена (неужели она узнала кто я?)
# Бетти говорит что узнала что Моника носит ее трусики!
# Моника в шоке.
    img 10336
    mt "?!?!?!"
    mt "НЕУЖЕЛИ?!?!"
    mt "НЕУЖЕЛИ ОНА УЗНАЛА КТО Я?!?"
    img 10337
    mt "ЧТО ЖЕ ТЕПЕРЬ БУДЕТ?! МНЕ КОНЕЦ!!!"

    img 10338
    betty "Я знаю..."
    img 10339
    betty "Я знаю, что ты носишь мои трусики..."

    #betty
    img 10340
    img 10341
    img 10342
    img 10343
    img 10344
    #
    img 10345
    mt "!!!"

# Бетти шипит: знаешь что я с тобой сделаю за это... нерадивая служанка...
# Барди смотрит на Бетти
# Бетти смотрит на Барди и смущается, напряженно (Бетти под шантажом)
# Я... Я разрешаю тебе носить мои трусики
    img 10346
    betty "Знаешь... Что я с тобой сделаю за это..."
    img 10347
    betty "... нерадивая служанка..."
    img 10348
    betty "..."
    img 10349
    bardie "..."
    img 10350
    mt "!!!"
    img 10351
    betty "..."
    img 10352
    bardie "..."
    img 10353
    betty "Я... Я разрешаю тебе носить мои трусики..."
    img 10354
    mt "!!!"

# Дальше шипит... Но только попробуй одеть те, которые я постирала и собираюсь одеть!
# Моника кривится...
# Бетти смотрит на Барди снова. Барди улыбается.
# Бетти с трудом говорит.
# Моника должна носить те трусики, которые Бетти одевала в предыдущий день.
    img 10355
    betty "..."
    betty "Но..."
    img 10356
    betty "Только попробуй надеть те, которые я постирала и собираюсь одеть!"
    img 10357
    mt "!!!"
    img 10358
    with fade
    betty "..."
    img 10359
    bardie "..."
    img 10360
    betty "..."
    img 10361
    bardie "..."
    img 10362
    betty "И..."
    img 10363
    betty "И... Ты..."
    img 10364
    betty "И... Ты должна носить только те трусики, которые я одевала в предыдущий день..."

# И...
# Бетти зло смотрит на Барди. Барди улыбается.
# Если тебе понадобится узнать какие трусики я ношу сегодня, то...
# Бетти снова зло смотрит на Барди, тот улыбается.
# То ты можешь спросить у меня и я покажу тебе... (Бетти злая и надменная)
    img 10365
    betty "..."
    img 10366
    bardie "..."
    img 10367
    betty "И..."
    img 10368
    mt "?!?!?!"
    img 10369
    betty "И... Если тебе понадобится узнать какие трусики я ношу сегодня, то..."
    img 10370
    with fade
    betty "..."
    img 10371
    bardie "..."
    img 10372
    mt "???"
    img 10373
    betty "То ты можешь спросить у меня и я покажу тебе..."
    img 10374
    betty "!!!"

# Моника в шоке и немного морщится.
    img 10375
    mt "..."
# Выбор что ответить
# Говорит спасибо, Миссис Робертс. Это будет намного удобнее.
# Тогда Бетти зло смотрит на Монику.
# Либо промолчать.
    menu:
        "Спасибо, Миссис Робертс. Это будет намного удобнее.":
            #bitchiness
            img 10376
            m "Спасибо, Миссис Робертс. Это будет намного удобнее."
            img 10377
            betty "!!!"
            img 10378
            m "..." # Моника злорадствует
            return True
        "Промолчать...":
            return False

    return



label ep24_dialogues5_betty2:
# Теперь, когда Бетти находится в спальне, там периодически находится Барди, который проверяет ее трусики.
# Моника может подойти к Бетти в спальне и проверить ее трусики.
# Также Моника может подойти к Бетти у зеркала на floor2 и проверить трусики тоже.


    # Бетти в спальне, Барди проверяет ее трусики
    img 10402
    with fadelong
    w
    img 10403
    w
    img 10404
    bardie "Бетти! Можешь не отвлекаться!"
    img 10420
    w
    #betty
    img 10405
    img 10406
    #
    img 10407
    img 10408
    #
    img 10409
    img 10410
    #
    img 10411
    img 10412
    #
    img 10413
    img 10414
    #
    #nude
    img 10415
        #random
    img 10416
    img 10417
    img 10418
    img 10419

    w
    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"

    betty "!!!"

    return
label ep24_dialogues5_betty2:
    # Бетти у зеркала, Барди проверяет ее трусики
    img 10421
    with fadelong
    w
    img 10422
    bardie "Бетти! Можешь не отвлекаться!"

    #betty
    img 10423
    img 10424
    #
    img 10426
    img 10425
    #
    img 10427
    img 10428
    #
    img 10430
    img 10429
    #
    img 10431
    img 10432
    #nude
    img 10433
        #random
        img 10434
        img 10435 #rare
        img 10436
        img 10437
        img 10438

    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
    img 10439
    betty "!!!"

    return


label ep24_dialogues5_betty3:
    # Моника в спальне проверяет трусики Бетти
    menu:
        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
            pass
        "Уйти.":
            return False
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    betty "!!!"
    m "..."
    betty "На, гувернантка, смотри. И не вздумай надеть другие!"
    return

label ep24_dialogues5_betty4:
    # Моника у зеркала проверяет трусики Бетти
    menu:
        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
            pass
        "Уйти.":
            return False
    img 10440
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    img 10441
    betty "!!!"
    img 10442
    with fade
    m "..."
    #betty
    img 10443
    betty "На, гувернантка, смотри."
    img 10444
    w
    betty "И не вздумай одеть другие!"
    #
    img 10446
    img 10445
    #
    img 10447
    img 10448
    #
    img 10450
    img 10449
    #
    img 10451
    img 10452

    betty "На, гувернантка, смотри. И не вздумай одеть другие!"
    return



# Все это происходит пока прогресс Барди не достигнет след. уровня
# После этого, Моника, при входе в любую локацию дома из подвала, натыкается на Бетти.
# Снова цена Бетти, Моника и подглядывающий Барди.
# Бетти говорит Монике что теперь в доме новые правила.
# Моника спрашивает подозрительно какие новые правила, Миссис Робертс?
# Бетти говорит что теперь в доме Моника должна ходить и убираться без трусиков.
# Моника в шоке!
# Но почему, Миссис Робертс?!
# Ведь она просто наемный работник и Бетти не имеет права требовать этого!
# Бетти злится и кричит что если еще раз увидит гувернантку в трусиках, та вылетит из дома в тот же миг!
# Моника оборачивается на Барди и шипит: мелкий гаденышь! я знаю, это все ты!!!
# Барди улыбается.

label ep24_dialogues5_betty5:
    img 10379
    betty "Моника, гувернантка."
    img 10380
    betty "Подойди ко мне!"

    img 10381
    m "Да, Миссис Робертс. Чем могу быть полезна?"
    img 10382
    betty "Гувернантка, я хочу сказать тебе."
    betty "В этом доме теперь новые правила..."
    img 10383
    m "Какие новые правила, Миссис Робертс?" #подозрительно
    img 10384
    betty "..."
    img 10385
    bardie "..."
    img 10386
    betty "..."
    img 10387
    m "..."
    img 10388
    bardie "..."
    img 10389
    betty "..."
    img 10390
    betty "В общем Моника..."
    img 10391
    betty "С этого дня ты должна ходить по дому и убираться без трусиков..."
    img 10392
    m "!!!"
    img 10393
    m "Но почему, Миссис Робертс?!?!"
    img 10394
    m "Ведь я просто наемные работник!"
    img 10395
    m "И Вы не имеете права требовать этого!"
    img 10396
    betty "Нерадивая гувернантка!"
    betty "Если я еще раз увижу тебя в трусиках, то ты вылетишь из дома в тот же миг!"
    img 10397
    betty "Поняла меня?!"
    img 10398
    m "!!!" #смотрит на Барди
    img 10399
    bardie "..."
    img 10400
    mt "Мелкий гаденыш!"
    mt "Я знаю, это все Ты!!!"
    img 1001
    bardie "..."

    return


# После этого, когда Моника проверяет у Бетти трусики в спальне, либо у зеркала и у Моники что-то надето,
# то она комментирует что не будет проверять у Бетти трусики, потому что сама сейчас носит их.
# И Бетти может попросить проверить в ответ и Моника рискует потерять крышу над головой.

label ep24_dialogues5_betty6:
    # Моника проверяет без трусиков Бетти в спальне
    menu:
        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
            pass
        "Уйти.":
            return False

    # Если есть какие-то трусики
    mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
    mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
    return False
    #


    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    # Бетти показывает попу
    betty "Я соблюдаю правила этого дома..."
    betty "Покажи, что ты тоже!"
    m "Да, Миссис Робертс, конечно..."
    # Моника показывает попу
    m "Я тоже соблюдаю правила этого дома..."

    return

label ep24_dialogues5_betty7:
    # Моника проверяет без трусиков Бетти у зеркала
    menu:
        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
            pass
        "Уйти.":
            return False

    # Если есть какие-то трусики
    mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
    mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
    return False
    #

    img 10453
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    img 10454
    w
    # Бетти показывает попу
    img 10455
    with fade
    w
    #random
    img 10456
    img 10457
    img 10458
    w

    img 10459
    w
    betty "Я соблюдаю правила этого дома..."
    img 10460
    betty "Покажи, что ты тоже!"
    m "Да, Миссис Робертс, конечно..."

    # Моника показывает попу
    img 10461
    with fade
    w
    img 10462
    w
    #random
    img 10463
    img 10464
    img 10465
    img 10466
    img 10467
    img 10468


    img 10462
    m "Я тоже соблюдаю правила этого дома..."

    return


















#
