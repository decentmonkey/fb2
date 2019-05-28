# Любой другой день (регулярное посещение)
label ep25_dialogues3_steve1:
    img 11488
    jane "Миссис Бакфетт?"
    img 11489
    m "Джейн! Мелкая подлиза!"
    m "Встать, когда с тобой говорит Босс!"
    # Джейн встает
    img 11490
    with fade
    w
    img 11491
    m "Стив у себя?!"
    img 11492
    jane "Да, Миссис Бакфетт. Мистер Стив у себя в кабинете."
    jane "Нет, Миссис Бакфетт, Мистер Стив будет только завтра."
    jane "Нет, Миссис Бакфетт, Мистер Стив будет только на следующей неделе."

    # заходит
    img 11493
    with fadelong
    steve "Моника, привет!"
    steve "Рад тебя видеть!"
    steve "Ты пришла заключить контракт?"
# В любой другой день Моника может придти и закрыть сделку со Стивом
# Выбор: закрыть сделку со Стивом
# Есть выбор сцен:
# Контракт со Стивом
# Контракт с Джейн
# Контракт с Тиффани
    img 11494
    menu:
        "Закрыть сделку со Стивом.":
            return 1
        "Контракт со Стивом.":
            return 2
        "Контракт со Стивом. (сначала надо закрыть сделку) (disabled)":
            pass
        "Контракт с Джейн. (в следующем обновлении) (disabled)":
            pass
        "Контракт с Тиффани (в следующем обновлении) (disabled)":
            pass
    return


label ep25_dialogues3_steve1a:
    # Закрыть сделку со Стивом

# Моника говорит Стиву чтобы встал с ее места и садится туда.
# Затем говорит что хочет закрыть их сделку.
# Стив отвечает что это можно сделать прямо сейчас.
# Моника говорит что ее только беспокоит возможность нежелательной беременности.
# Стив говорит что с этим нет проблем, у него есть специальная таблетка.
# Стив кладет таблетку перед Моникой
# Он всегда ее держит на всякий случай. Улыбается.
# Моника злится. Я знаю что ты трахаешь всех налево и направо, Стив!
# Ты мерзавец!
# Стив отвечает что он не мерзавец, он честный бизнесмен, который заключает хорошие сделки!
# Моника зло смотрит
# Стив спрашивает, будет-ли Моника пить таблетку?
    img 11495
    m "Встань с моего стула, Стив!"
    # Моника садится на стул
    img 11496
    steve "..."
    img 11497
    m "Я хочу закрыть нашу сделку, Стив!"
    img 11498
    with diss
    w
    img 11499
    m "Которую мы заключили у бассейна в моем доме..."
    img 11500
    steve "Моника, это можно сделать прямо сейчас."
    img 11501
    m "Стив, меня беспокоит возможность нежелательной беременности."
    img 11502
    steve "О, Моника! С этим нет проблем!"
    steve "У меня есть специальная таблетка."
    # Стив кладет таблетку
    img 11503
    with fadelong
    w
    img 11504
    steve "Я всегда держу ее на всякий случай."
    # Стив улыбается
    img 11505
    steve "..."
    img 11506
    w
    img 11507
    m "!!!"
    img 11508
    steve "..."
    img 11509
    m "Я знаю, что ты трахаешь всех налево и направо, Стив!"
    m "Ты мерзавец!"
    img 11510
    steve "Моника, я не мерзавец. Я честный бизнесмен."
    steve "Который заключает хорошие сделки!"
    img 11511
    m "!!!"
    img 11512
    steve "Моника, будешь-ли ты пить таблетку?"
    img 11513
    menu:
        "Я не собираюсь рисковать!":
# Выбор:
# Я не собираюсь рисковать!
# Уходит
            img 11514
            m "Я не собираюсь рисковать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            return False
        "Я выпью эту гребаную таблетку...":
            pass
# Я выпью эту гребаную таблетку...
# Стив отвечает. Хорошо, сейчас я попрошу Джейн принести стакан воды.
# Ты ведь будешь запивать таблетку?
# Моника зло смотрит и отвечает: буду...
# Стив зовет Джейн
# Джейн заходит и спрашивает что угодно Мистеру Стиву
# Стив просит Джейн принести стакан воды, у Миссис Бакфетт болит голова и ей надо запить таблетку.
# Джейн приносит воду и ставит на стол перед Моникой. Говорит: пожалуйста, Миссис Бакфетт.
# Моника зло смотрит на Джейн
    mt "Не могу поверить что я соглашаюсь на это..."
    img 11515
    m "Я выпью эту гребаную таблетку..."
    img 11516
    steve "Хорошо, Моника."
    steve "Сейчас я попрошу Джейн принести стакан воды."
    steve "Ты ведь будешь запивать таблетку?"
    img 11517
    m "!!!"
    img 11518
    steve "..."
    img 11519
    m "Буду..."
    # Бип телефон
    steve "Джейн! Зайди, пожалуйста, сюда!"
    img 11520
    jane "..."
    img 11521
    jane "Да, Мистер Стив."
    jane "Что Вам угодно?"
    img 11522
    steve "Джейн, принести, пожалуйста, стакан воды."
    steve "У Миссис Бакфетт болит голова и ей надо запить таблетку."
    img 11523
    jane "Хорошо, Мистер Стив, одну минуту."

    # уходит, приходит
# Джейн приносит воду и ставит на стол перед Моникой. Говорит: пожалуйста, Миссис Бакфетт.
# Моника зло смотрит на Джейн
    img 11524
    with fadelong
    w
    img 11525
    with fade
    jane "Вот, пожалуйста, Миссис Бакфетт."
    img 11526
    m "!!!"
# Джейн уходя подходит к Стиву и спрашивает: все хорошо, милый?
# Стив отвечает что да, малышка, все хорошо.
# Закрой, пожалуйста, дверь. Нам с Миссис Бакфетт надо закрыть сложный контракт и он бы не хотел чтобы кто-то мешал.
# Джейн отвечает: Да, Мистер Стив.
    img 11527
    jane "Все хорошо, Милый?"
    img 11528
    steve "Да, малышка, все хорошо."
    steve "Закрой, пожалуйста, дверь."
    img 11529
    steve "Нам с Миссис Бакфетт надо закрыть сложный контракт."
    steve "И я бы не хотел чтобы кто-то мешал."
    img 11530
    jane "Да, Мистер Стив."

# Джейн уходит
# Моника смотрит на стакан с водой
# Стив говорит Монике что она может выпить таблетку
# Выбор:
# Выпить таблетку или уйти
    img 11531
    with fade
    w
    img 11532
    m "..."
    steve "..."
    img 11533
    m "..."
    img 11534
    steve "Моника, ты можешь выпить таблетку."
    img 11535
    menu:
        "Выпить таблетку.":
            pass
        "Уйти.":
            img 11536
            m "Я не собираюсь рисковать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            return False

# Если выпить:
# Моника пьет стакан.
# Стив говорит Монике: теперь ты можешь встать и задрать юбку. Мне требуется доступ к
# объекту аренды в соответствии с контрактом
# Моника зло смотрит:
# Уйти или задрать юбку
    img 11537
    with fade
    w
    #глоток
    img 11538
    with diss
    w
    img 11539
    with diss
    w
    img 11540
    with diss
    w
    img 11541
    with diss
    w
    img 11542
    steve "Моника, теперь ты можешь встать и задрать платье."
    img 11543
    steve "Мне требуется доступ к объекту аренды в соответствии с контрактом."
    img 11544
    menu:
        "Поднять платье.":
            pass
        "Уйти.":
            img 11536
            m "Я не собираюсь этого делать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            return False

# Если задрать юбку:
# Моника встает и задирает юбку.
# Там трусики Юлии
# Стив говорит: какие интересные у тебя трусики
# В прошлый раз ты была в них-же, либо в прошлый раз ты была в других
# Моника зло отвечает что это не его дело, пусть быстро закрывает контракт и отсылает деньги!
# Стив входит в Монику и трахает ее.
    img 11545
    with diss
    w
    img 11546
    with diss
    w
    img 11547
    m "!!!"
    img 11548
    with diss
    w
    img 11549
    with diss
    w
    img 11550
    with diss
    w
    img 11551
    with diss
    w
    img 11552
    with diss
    w
    img 11553
    steve "О! Моника!"
    steve "Ты не одеваешь трусики?"
    img 11554
    steve "Это похвально!"

#    steve "Какие интересные у тебя трусики..."
    # если была в них
#    steve "Не помню, в прошлый раз ты была в них же или была в других..."
    img 11155
    steve "У тебя нет трусиков под это платье или тебе просто нравится ходить без них?"
    img 11556
    with diss
    m "Это не твое дело, Стив!"
    img 11557
    with diss
    m "Быстро закрывай контракт и отсылай деньги!"
    img 11558
    steve "Моника, у тебя слишком длинные ноги!"
    img 11559
    steve "Можешь, пожалуйста, присесть пониже?"
    steve "Мне нудобно вставать на цыпочки, как в прошлый раз, когда я брал в аренду твою..."
    img 11560
    m "Заткнись, Стив!"
    img 11561
    with diss
    m "ТАК?!"
    img 11562
    steve "Да! Хе-хе!"

    img 11563
    w
    img 11564
    w
    img 11565
    w
    img 11566
    w
    img 11567
    w
    img 11568
    w
    img 11569
    w


# Затем кончает.
    img 11570
    with fade
    steve "АААААХХХХ!!!"
# Моника говорит чтобы он скорее высунул его мерзкий отросток из ее тела!
# Стив говорит погоди, я еще не до конца кончил
# Кончает снова
# Моника зло говорит что теперь все?!
# Стив кончает еще и еще и еще
# Моника вскакивает и держится за киску, зло ругается на Стива что тот пожалеет о том что сделал!
    img 11571
    m "Вытаскивай скорее свой мерзкий отросток из моего тела!"
    img 11572
    steve "Погоди, я еще не до конца кончил."
    steve "АААААХХХХ!!!"
    img 11573
    m "Ну что, теперь все?!"
    img 11574
    steve "АААААХХХХ!!!"
    img 11575
    steve "АААААХХХХ!!!"
    img 11576
    steve "АААААХХХХ!!!"

    img 11741
    with fade
    w
    img 11742
    with diss
    w

    img 11577
    with fadelong
    m "Мерзавец!"
    m "Ты пожалеешь о том что ты сделал!!!"
    img 11578
    m "Быстро переводи деньги!"
    img 11579
    steve "Да, Моника, конечно!"
    steve "Наш контракт закрыт!"

# Стив перечисляет деньги
    img 11580
    steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
    steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
    m "!!!"
    return True





label ep25_dialogues3_steve2:
# Контракт со Стивом:
# первый раз:
# Стив, мне нужна какая-нибудь работа.
# Временно. Назначь меня на какую-нибудь руководящую должность.
# Только не слишком низко, ты ведь знаешь мой уровень!
# Стив отвечает Монике что руководящих должностей свободных нет.
# Моника спрашивает: хорошо, тогда назначь меня на какую-нибудь обычную должность, но с высокой зарплатой!
# Стив говорит что обычных должностей тоже свободных нет.

    # Моника не выгоняет Стива со стула
    img 11581
    m "Стив, мне нужна какая-нибудь работа."
    m "Временно."
    img 11582
    m "Назначь меня на какую-нибудь руководящую должность."
    m "Только не слишком низко, ты ведь знаешь мой уровень!"
    img 11583
    steve "Моника, прости, но руководящих должностей свободных нет."
    m "!!!"
    img 11584
    m "Хорошо, тогда назначь меня на какую-нибудь обычную должность, но с высокой зарплатой!"
    img 11585
    steve "Моника, прости, но обычных должностей вакантных тоже нет."

# Сейчас кризис и он и так собирается сокращать персонал.
# Моника говорит чтобы он уволил одну из тех дур, которые его окружают.
# Стив говорит что это невозможно, так как без них он как без рук.
# Моника злится и говорит Стиву что он пожалеет об этом!
# Стив говорит что у него есть контракт для Моники.
# Моника спрашивает какой контракт?
    steve "Сейчас кризис и я и так собираюсь сокращать персонал."
    img 11586
    m "Тогда уволь одну из тех дур, которые тебя окружают."
    img 11587
    steve "Моника, это невозможно, я без них как без рук!"
    img 11588
    m "Стив! Мерзавец!"
    m "Ты пожалеешь об этом!"
    img 11589
    steve "Моника, у меня есть контракт для тебя!"
    img 11590
    m "Какой еще контракт?"
# Стив говорит что сегодня был сложный рабочий день и что заплатит ей $5000 если она расслабит его и сделает ему массаж.
# Моника спрашивает что этот извращенец имеет ввиду под расслабить и какого рода массаж ему нужен?
# Стив говорит что Моника может забраться под стол и сделать массаж его члену.
# Его член целый день провел в неподвижности и очень затек. Ему требуется массаж.
# Моника зло смотрит на Стива.
    img 11591
    steve "Моника, сегодня был сложный рабочий день."
    steve "Я заплачу тебе $ 5000, если ты расслабишь меня и сделаешь мне массаж."
    img 11592
    m "Стив, извращенец, что ты имеешь ввиду под расслабить тебя?"
    m "И какого рода массаж тебе нужен?"
    #zip sound
    img 11593
    with fadelong
    steve "Моника, ты можешь забраться под стол и сделать массаж моему члену."
    img 11594
    steve "Мой член целый день провел в неподвижности и очень затек."
    steve "Ему требуется массаж."
    img 11595
    m "!!!"
# Я тебе что, дешевая проститутка, чтобы ты предлагал мне сосать твой член у тебя под столом?!
# А что будет если войдет твоя невеста Джейн, А?!
# Стив отвечает, что по условиям контракта Моника будет это делать инкогнито и не привлекать внимания.
# Никто про это не узнает. У Стива нет цели испортить деловую репутацию Моники.
# Это никак не связано с сексом за деньги, это просто контракт.
# Да в нем фигурирует член Стива и рот Моники, но, если абстрагироваться от всего, то это просто бизнес.
# А Моника - бизнес-леди и привыкла иметь дело с контрактами.
# В этом нет ничего особенного. Зато $5000 сразу отправятся на любимый адрес Моники.
    img 11596
    m "Я ТЕБЕ ЧТО, ДЕШЕВАЯ ПРОСТИТУТКА?!"
    m "ЧТОБЫ ТЫ ПРЕДЛАГАЛ МНЕ СОСАТЬ ТВОЙ ЧЛЕН У ТЕБЯ ПОД СТОЛОМ?!"
    img 11597
    m "А что будет, если войдет твоя невеста Джейн, А?!"
    img 11598
    steve "Моника, по условиям контракта ты будешь делать это инкогнито и не привлекать внимание."
    steve "Не волнуйся, Моника. Никто про это не узнает."
    steve "У меня нет цели портить твою деловую репутацию."
    img 11599
    steve "Это никак не связано с сексом за деньги."
    steve "Это просто контракт."
    img 11600
    steve "Да, в нем фигурирует мой член и твой ротик."
    steve "Но, если абстрагироваться от всего, то это просто бизнес."
    img 11601
    steve "А ты, Моника, бизнес-леди и привыкла иметь дело с контрактами."
    steve "В этом нет ничего особенного."
    steve "Зато $ 5000 сразу отправятся на твой любимый адрес!"
# Так что, Моника?
    img 11602
    m "!!!"
    img 11603
    steve "Так что, Моника?"
    img 11604
    menu:
        "Уйти.":
# Уйти
            img 11606
            m "Я не собираюсь делать этого!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            return False
        "Залезть под стол.":
            pass
# Залезть под стол.
# Мне надо больше денег, Стив!
# Хотя бы $5500!
# Моника, это невозможно! Даже $5000 для меня слишком большие деньги!
# Могу предложить тебе 5010$!
    img 11607
    mt "До сих пор не могу поверить в то что происходит..."
    mt "Но, по крайней мере, про это никто не узнает."
    mt "В отличии от фотосессий у Бифа, где на меня смотрит весь мир..."
    img 11608
    m "Мне надо больше денег, Стив!"
    m "Хотя бы $ 5500!"
    img 11609
    steve "Моника, это невозможно!"
    steve "Даже $ 5000 для меня слишком большие деньги!"
    img 11610
    steve "Могу предложить тебе $ 5050!"
    img 11611
    m "!!!"
    menu:
        "Согласиться на $ 5050":
# Согласиться на 5050
# Хорошо, Стив! 10$ Ты мне дашь наличными, понял?!
# Конечно, Моника, можешь приступать
            img 11612
            m "Хорошо, Стив!"
            m "$ 50 ты мне дашь наличными, понял?!"
            img 11613
            steve "Конечно, Моника. Можешь приступать."
        "Согласиться на $ 5000":

# Согласиться на 5000
# Мне не нужны твои жалкие подачки, Стив! Пусть будет $5000
# Конечно, Моника, можешь приступать
            img 11614
            m "Мне не нужны твои жалкие подачки, Стив!"
            m "Пусть будет $ 5000."
            img 11613
            steve "Конечно, Моника. Можешь приступать."

# Моника залезает под стол.
    img 11615
    with diss
    w
    img 11616
    with diss
    w
    img 11617
    w
    img 11618
    w
    img 11619
    w
    #blowjob
    img 11620
    with diss
    w
    img 11621
    with diss
    w
    img 11622
    with diss
    w
    img 11623
    with diss
    w
    img 11624
    with diss
    w

    return True
# Затем срабатывает одна из сцен:


label ep25_dialogues3_steve3a:
# Входит Джейн
# Сцена 1
# Джейн входит и говорит Стиву что ему пришел факс.
# Стив отвечает что положи, пожалуйста, его на стол.
# Джейн спрашивает все-ли хорошо? Миссис Бакфетт уже ушла?
    img 11625
    with fadelong
    jane "Стив, тебе пришел факс."
    img 11626
    steve "Хорошо, Джейн."
    steve "Положи, пожалуйста, его на полку."
    #blowjob
    img 11627
    with diss
    w
    #
    img 11628
    with fade
    w
    img 11629
    w
    jane "Все-ли хорошо, Милый?"
    img 11630
    jane "Миссис Бакфетт уже ушла?"
# Стив отвечает что она ушла Джейн просто не заметила ее.
# Стив знает что Джейн все время отлучается от рабочего места.
# И, если бы не ее хорошая попка, то он бы давно уволил ее за это.
# Джейн отвечает, что дело не только в этом и чтобы Стив не забывал.
# Джейн уходит
    img 11631
    steve "Да, Джейн."
    steve "Она уже ушла. Просто ты не заметила этого."

    #blowjob
    img 11632
    with fade
    w
    #
    img 11633
    steve "Я знаю, что ты все время отлучаешься от рабочего места."
    steve "И, если бы не твоя хорошая попка, то я давно бы уволил тебя за это."
    img 11634
    jane "Дело не только в моей попке, Стив."
    jane "Не забывай этого!"
    return

label ep25_dialogues3_steve3b:
# Сцена 2
# Джейн входит и спрашивает у Стива не забыл-ли он про свадьбу.
# Стив отвечает что не забыл.
# Джейн спрашивает когда будет дата свадьбы?
# Стив отвечает что это будет очень скоро, Стив работает над этим!
# Джейн отвечает: хорошо, милый и целует его в щечку
    img 11635
    with fadelong
    w
    img 11637
    jane "Милый, ты не забыл про нашу свадьбу?"
    img 11636
    steve "Нет, милая, я не забыл."
    img 11638
    steve "Я все помню!"
    img 11640
    with fade
    jane "Ты уже решил насчет даты, Милый?"
    #blowjob
    img 11641
    with fade
    w
    #

    img 11642
    steve "Еще нет, Милая, но это будет очень скоро."
    img 11639
    steve "Я работаю над этим!"
    img 11643
    with fade
    jane "Хорошо, милый."
    img 11644
    with diss
    w
    img 11645
    with diss
    jane "Чмок!"
    #уходит
    img 11646
    with fadelong
    w
    return

label ep25_dialogues3_steve3c:
# Сцена 3
# Джейн входит и говорит что соскучилась по любимому.
# А Стив? Стив отвечает что тоже соскучился.
# Джейн подходит ближе и спрашивает, любит-ли ее Стив?
# Стив отвечает что очень любит малышку Джейн.
# Джейн спрашивает: правда? Ты больше никого не любишь?
# У тебя больше никого нет кроме меня?
# Стив отвечает что любит только Джейн и она у него единственная.
    img 11635
    with fadelong
    w
    img 11647
    with fade
    jane "Милый, Я соскучилась по тебе."

    #blowjob
    img 11648
    with diss
    w
    img 11649
    with diss
    w
    #

    img 11650
    with diss
    steve "..."
    jane "А ты?"
    img 11651
    steve "..."
    img 11652
    jane "А, Стив?! Ты меня слышишь?"
    img 11653
    steve "А?! Да, Джейн, я тоже соскучился по тебе."

    # Джейн подходит ближе
    img 11654
    with fade
    w
    img 11655
    with fade
    w
    img 11656
    jane "Ты меня любишь, Стив?"

    img 11657
    steve "Я очень люблю малышку Джейн!"
    img 11658
    jane "Правда?"
    jane "Ты больше никого не любишь?"
    jane "У тебя больше никого нет кроме меня?"
    img 11659
    jane "Я соблюдаю твой дурацкий дресс-код."
    jane "И я жду свадьбы, Стив!"
    img 11660
    steve "Джейн, я люблю только тебя!"
    steve "И ты у меня единственная!"
    img 11661
    jane "Чмок!"
    #уходит
    img 11646
    with fadelong
    w
    return

label ep25_dialogues3_steve4a:
# Входит Тиффани
# Сцена 1
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив говорит чтобы она положила их на стол
# Джейн кладет сексуально и уходит
    img 11662
    tiffany "Мистер Стив, можно войти?"
    img 11663
    steve "Да, Тиффани, заходи!"
    img 11664
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    img 11665
    steve "Да, Тиффани, можешь положить их на стол."
    img 11666
    tiffany "..."
    return

label ep25_dialogues3_steve4b:
# Сцена 2
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив просит Тиффани подойти поближе.
# Тиффани подходит и спрашивает что будет угодно ее Боссу?
# Стив говорит Тиффани что она такая красивая.
# Что Стив очень хочет оценить ее красоту.
# Стив кладет руку на ее ногу пониже попы
    img 11662
    tiffany "Мистер Стив, можно войти?"
    img 11663
    steve "Да, Тиффани, заходи!"
    img 11664
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    img 11667
    steve "Тиффани, можешь подойти поближе?"
    img 11668
    tiffany "Да, Босс, что Вам будет угодно?"
    img 11669
    steve "Тиффани, малышка."
    steve "Ты такая красивая..."
    img 11670
    steve "Я так хочу оценить твою красоту!"
# Стив кладет руку на ее ногу пониже попы
    sound Jump2
    img 11671
    with diss
    w


# Тиффани спрашивает помнит-ли Мистер Стив ее условие?
# Стив отвечает что ее условие трудно выполнимо, но ведь это не помешает ему насладиться ее красотой?
# Тиффани жестко отвечает чтобы Стив убрал руку, иначе она заявит о харрасменте.
# Стив убирает руку.
    img 11672
    tiffany "Помнит-ли Мистер Стив мое условие?"
    img 11673
    steve "Тиффани, твое условие трудно выполнимо."
    img 11674
    steve "Но ведь это не помешает мне насладиться твоей красотой?"
    img 11675
    tiffany "Уберите руку, Мистер Стив!"
    img 11676
    tiffany "Иначе я заявлю о харрасменте!"
    img 11677
    with diss
    w
    img 11678
    with diss
    w

# У Стива падает член.
    #звук вниз
    img 11679
    with diss
    w
# Тиффани уходит
    img 11680
    w
    img 11681
    tiffany "..."
    img 11682
    with diss
    w
# Моника зло говорит из-под стола что у Стива упал член.
# И что теперь? Из-за этой дешевой шлюхи ей придется снова его поднимать?
# Стив отвечает что сложности бывают, но, Моника, что поделать, это твоя работа!
# Моника зло продолжает сосать член.
    img 11683
    with fade
    w
    img 11684
    m "У тебя упал член, Стив!"
    img 11685
    steve "..."
    img 11686
    m "И что теперь?"
    m "Из-за этой дешевой шлюхи мне придется снова его поднимать?"
    img 11687
    steve "Моника, во время выполнения любого контракта бывают сложности."
    steve "Но что поделать? Это твоя работа."
    img 11688
    m "!!!"
    img 11689
    steve "Моника, ты можешь продолжать. Контракт еще не закрыт."
    img 11690
    with fade
    m "!!!"
    #blowjob
    img 11691
    with fade
    w

# Моника зло продолжает сосать член.
    return


label ep25_dialogues3_steve4c:
# Сцена 3
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив просит Тиффани подойти поближе
# Тиффани подходит и говорит что все уже сказала.
# Ее ответ нет и она догадывается что Стив хочет сейчас сделать.
# Стив подносит руку к Тиффани
    img 11662
    tiffany "Мистер Стив, можно войти?"
    img 11663
    steve "Да, Тиффани, заходи!"
    img 11664
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    img 11667
    steve "Тиффани, можешь подойти поближе?"
# Тиффани подходит и говорит что все уже сказала.
    img 11692
    tiffany "Мистер Стив, я Вам все уже сказала."
    tiffany "Я догадываюсь что Вы сейчас хотите сделать."
    img 11693
    tiffany "Мой ответ НЕТ!"

# Стив подносит руку к Тиффани
    img 11694
    with diss
    w
    img 11695
# Тиффани говорит: только попробуйте, Мистер Стив...
# Стив говорит, что Тиффани так красива, так прекрасна
# Что Стив настолько сильно хочет ее, если бы она только знала...
# Что он.. он... Аааххх! Стив хватает Тиффани за попу под трусиками и кончает Монике в рот
    tiffany "Только попробуйте, Мистер Стив..."
    img 11697
    steve "О, Тиффани!"
    img 11696
    steve "Ты так красива!"
    steve "Так прекрасна!"
    img 11698
    steve "Если бы только знала как я хочу тебя!"
    img 11699
    with diss
    steve "Если бы ты только, Аааах!!"
# Что он.. он... Аааххх! Стив хватает Тиффани за попу под трусиками и кончает Монике в рот
    img 11700
    tiffany "!!!"
    img 11701
    steve "Аааах!"
    img 11702
    steve "Аааах!"
    #звук кончания
    img 11703
    with diss
    steve "АААААААААААРГХХХХХ!!!"
    img 11704
    with diss
    w
    img 11705
    with diss
    steve "АААААААААААРГХХХХХ!!!"
    m "!!!"

# Тиффани смеется.
    img 11706
    tiffany "Ха!"
# Вы там что, кончили, Мистер Стив?
# Хи-хи-хи. Вы пополнили мою смешную коллекцию мужчин, которые кончают себе в штаны при моем виде.
# Моника зло смотрит из-под низа
# Хорошего рабочего дня, Мистер Стив...
# Уходит
    tiffany "Вы там что, кончили, Мистер Стив?"
    img 11707
    steve "..."
    img 11708
    tiffany "Хи-хи-хи."
    tiffany "Вы дополнили мою смешную коллекцию мужчин, которые при виде меня кончают в штаны."
    img 11709
    with diss
    w
    img 11710
    m "!!!"
    img 11711
    tiffany "Хорошего рабочего дня, Мистер Стив!"
    return

label ep25_dialogues3_steve5a:
    # Стив кончает
    img 11712
    steve "АААААААААААРГХХХХХ!!!"
    img 11713
    w
    img 11714
    w
    return


label ep25_dialogues3_steve5:
    # Моника стоит перед Стивом после сцены blowjob
    img 11715
    m "Тьфу!"
    mt "Мерзость!"

    img 11716
    m "Доволен, Стив?!"
    img 11717
    m "Мы закрыли контракт!"
    img 11718
    steve "Да, Моника, деньги ушли."

    img 11719
    m "Стив, ты мерзавец и изменник!"
    img 11720
    steve "Моника, не будь так категорична!"
    steve "Давай это будет нашим маленьким секретом!"
    img 11721
    steve "Ты сохранишь его со своей стороны."
    steve "А я со своей..."
    img 11722
    m "!!!"
    m "Подонок! Только попробуй кому-нибудь рассказать про это!"

    img 11723
    steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
    steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
    m "!!!"
    return
#












#
