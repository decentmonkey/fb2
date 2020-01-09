
label gallery_11566:
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
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 11495
    with fadelong
    m "Встань с моего стула, Стив!"
    # Моника садится на стул
    img 11496
    with fade
    steve "..."
    img 11497
    with diss
    m "Я хочу закрыть нашу сделку, Стив!"
    img black_screen
    with diss
    pause 1.0
    img 11498
    with fadelong
    w
    img 11499
    with fade
    m "Которую мы заключили у бассейна в моем доме..."
    img 11500
    with diss
    steve "Моника, это можно сделать прямо сейчас."
    img 11501
    with fade
    m "Стив, меня беспокоит возможность нежелательной беременности."
    img 11502
    with diss
    steve "О, Моника! С этим нет проблем!"
    steve "У меня есть специальная таблетка."
    # Стив кладет таблетку
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 11503
    with fadelong
    w
    img 11504
    with fade
    steve "Я всегда держу ее на всякий случай."
    # Стив улыбается
    img 11505
    with diss
    steve "..."
    img 11506
    w
    img 11507
    with diss
    m "!!!"
    img 11508
    with fade
    steve "..."
    music Power_Bots_Loop
    img 11509
    with diss
    m "Я знаю, что ты трахаешь всех налево и направо, Стив!"
    m "Ты мерзавец!"
    music Groove2_85
    img 11510
    with fade
    steve "Моника, я не мерзавец. Я честный бизнесмен."
    steve "Который заключает хорошие сделки!"
    music Power_Bots_Loop
    img 11511
    with diss
    m "!!!"
    img 11512
    with fade
    steve "Моника, будешь-ли ты пить таблетку?"
    img 11513
    with diss
    menu:
        "Я не собираюсь рисковать!":
# Выбор:
# Я не собираюсь рисковать!
# Уходит
            img 11514
            with fadelong
            m "Я не собираюсь рисковать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            return
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
    music Groove2_85
    mt "Не могу поверить что я соглашаюсь на это..."
    img 11515
    with diss
    m "Я выпью эту гребаную таблетку..."
    img 11516
    with fade
    steve "Хорошо, Моника."
    steve "Сейчас я попрошу Джейн принести стакан воды."
    steve "Ты ведь будешь запивать таблетку?"
    music Power_Bots_Loop
    img 11517
    with diss
    m "!!!"
    music Groove2_85
    img 11518
    with fade
    steve "..."
    img 11519
    with diss
    m "Буду..."
    # Бип телефон
    music stop
    img black_screen
    with diss
    sound snd_phone_short_beeps
    img 11519
    with fade
    steve "Джейн! Зайди, пожалуйста, сюда!"
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 11520
    with fadelong
    jane "..."
    img 11521
    with diss
    jane "Да, Мистер Стив."
    jane "Что Вам угодно?"
    img 11522
    with fade
    steve "Джейн, принести, пожалуйста, стакан воды."
    steve "У Миссис Бакфетт болит голова и ей надо запить таблетку."
    img 11523
    with diss
    jane "Хорошо, Мистер Стив, одну минуту."

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(_("Минуту спустя..."))
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    sound highheels_short_walk
    img 11524
    with fadelong

    # уходит, приходит
# Джейн приносит воду и ставит на стол перед Моникой. Говорит: пожалуйста, Миссис Бакфетт.
# Моника зло смотрит на Джейн
    w
    img 11525
    with fade
    jane "Вот, пожалуйста, Миссис Бакфетт."
    music Power_Bots_Loop
    img 11526
    with diss
    m "!!!"
# Джейн уходя подходит к Стиву и спрашивает: все хорошо, милый?
# Стив отвечает что да, малышка, все хорошо.
# Закрой, пожалуйста, дверь. Нам с Миссис Бакфетт надо закрыть сложный контракт и он бы не хотел чтобы кто-то мешал.
# Джейн отвечает: Да, Мистер Стив.
    music Groove2_85
    img 11527
    with fade
    jane "Все хорошо, Милый?"
    img 11528
    with diss
    steve "Да, малышка, все хорошо."
    steve "Закрой, пожалуйста, дверь."
    img 11529
    with diss
    steve "Нам с Миссис Бакфетт надо закрыть сложный контракт."
    steve "И я бы не хотел чтобы кто-то мешал."
    img 11530
    with fade
    jane "Да, Мистер Стив."


# Джейн уходит
# Моника смотрит на стакан с водой
# Стив говорит Монике что она может выпить таблетку
# Выбор:
# Выпить таблетку или уйти
    sound highheels_short_walk
    img 11531
    with fade
    w
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    img 11532
    with fadelong
    m "..."
    steve "..."
    img 11533
    with diss
    m "..."
    img 11534
    with fade
    steve "Моника, ты можешь выпить таблетку."
    img 11535
    with diss
    menu:
        "Выпить таблетку.":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 11536
            with fadelong
            m "Я не собираюсь рисковать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            return

# Если выпить:
# Моника пьет стакан.
# Стив говорит Монике: теперь ты можешь встать и задрать юбку. Мне требуется доступ к
# объекту аренды в соответствии с контрактом
# Моника зло смотрит:
# Уйти или задрать юбку
    music stop
    img 11537
    with fade
    w
    #глоток
    sound snd_gulp
    img 11538
    with diss
    w
    img 11539
    with diss
    w
    sound snd_drinking_water
    img 11540
    with diss
    w
    sound snd_glass_table
    img 11541
    with diss
    w
    music Groove2_85
    img 11542
    with fadelong
    steve "Моника, теперь ты можешь встать и задрать платье."
    img 11543
    with diss
    steve "Мне требуется доступ к объекту аренды в соответствии с контрактом."
    img 11544
    with fade
    menu:
        "Поднять платье.":
            pass
        "Уйти.":
            music Power_Bots_Loop
            img 11536
            with fadelong
            m "Я не собираюсь этого делать!"
            steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
            steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
            m "!!!"
            return

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
    with fade
    m "!!!"
    img 11548
    with diss
    w
    sound snd_fabric1
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
    with fade
    steve "О! Моника!"
    steve "Ты не одеваешь трусики?"
    img 11554
    with diss
    steve "Это похвально!"

#    steve "Какие интересные у тебя трусики..."
    # если была в них
#    steve "Не помню, в прошлый раз ты была в них же или была в других..."

    img 11555
    with fade
    steve "У тебя нет трусиков под это платье или тебе просто нравится ходить без них?"
    music Power_Bots_Loop
    img 11556
    with diss
    m "Это не твое дело, Стив!"
    img 11557
    with diss
    m "Быстро закрывай контракт и отсылай деньги!"
    music Groove2_85
    img 11558
    with fade
    steve "Моника, у тебя слишком длинные ноги!"
    img 11559
    with diss
    steve "Можешь, пожалуйста, присесть пониже?"
    steve "Мне нудобно вставать на цыпочки, как в прошлый раз, когда я брал в аренду твою..."
    music Power_Bots_Loop
    img 11560
    m "Заткнись, Стив!"
    img 11561
    with diss
    m "ТАК?!"
    music Groove2_85
    img 11562
    with fade
    steve "Да! Хе-хе!"


    music stop
    # video sex
    img 11563
    with diss
    w
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_1 = Movie(play="video/v_Steve_Monica_Sex_4_1.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_1
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_2 = Movie(play="video/v_Steve_Monica_Sex_4_2.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_2
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_3 = Movie(play="video/v_Steve_Monica_Sex_4_3.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_3
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_4 = Movie(play="video/v_Steve_Monica_Sex_4_4.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_4
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_5 = Movie(play="video/v_Steve_Monica_Sex_4_5.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_5
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_6 = Movie(play="video/v_Steve_Monica_Sex_4_6.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_6
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_7 = Movie(play="video/v_Steve_Monica_Sex_4_7.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_7
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_8 = Movie(play="video/v_Steve_Monica_Sex_4_8.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_8
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_9 = Movie(play="video/v_Steve_Monica_Sex_4_9.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_9
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Steve_Monica_Sex_4_11 = Movie(play="video/v_Steve_Monica_Sex_4_11.mkv", fps=30)
    show videov_Steve_Monica_Sex_4_11
    with fadelong
    wclean

    stop music
    music Loved_Up2
    img 11564
    with diss
    w
    img 11565
    with diss
    w
    img 11566
    with diss
    w
    img 11567
    with diss
    w
    img 11568
    with diss
    w
    img 11569
    with diss
    w


# Затем кончает.
    music Loved_Up2
    img 11570
    with fade
    sound bulk1
    steve "АААААХХХХ!!!"
# Моника говорит чтобы он скорее высунул его мерзкий отросток из ее тела!
# Стив говорит погоди, я еще не до конца кончил
# Кончает снова
# Моника зло говорит что теперь все?!
# Стив кончает еще и еще и еще
# Моника вскакивает и держится за киску, зло ругается на Стива что тот пожалеет о том что сделал!

    img 11571
    with diss
    m "Вытаскивай скорее свой мерзкий отросток из моего тела!"
    img 11572
    with fade
    steve "Погоди, я еще не до конца кончил."
    sound bulk1
    steve "АААААХХХХ!!!"
    img 11573
    with diss
    m "Ну что, теперь все?!"
    img 11574
    with fade
    sound bulk1
    steve "АААААХХХХ!!!"
    img 11575
    with diss
    sound bulk1
    steve "АААААХХХХ!!!"
    img 11576
    with diss
    sound bulk1
    steve "АААААХХХХ!!!"

    img 11741
    with fade
    w
    img 11742
    with diss
    w

    music Power_Bots_Loop
    img 11577
    with fadelong
    m "Мерзавец!"
    m "Ты пожалеешь о том что ты сделал!!!"
    img 11578
    with diss
    m "Быстро переводи деньги!"
    music Groove2_85
    img 11579
    with fade
    steve "Да, Моника, конечно!"
    steve "Наш контракт закрыт!"

# Стив перечисляет деньги
    img 11580
    with fadelong
    steve "Моника, если вдруг ты захочешь заключить еще сделку, то приходи!"
    steve "Я добропорядочный бизнесмен и всегда рад хорошей сделке!"
    m "!!!"
    return

label gallery_11629:
# Входит Джейн
# Сцена 1
# Джейн входит и говорит Стиву что ему пришел факс.
# Стив отвечает что положи, пожалуйста, его на стол.
# Джейн спрашивает все-ли хорошо? Миссис Бакфетт уже ушла?
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11625
    with fadelong
    jane "Стив, тебе пришел факс."
    img 11626
    with diss
    steve "Хорошо, Джейн."
    steve "Положи, пожалуйста, его на полку."
    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11627
    with diss
    w
    #
    music Groove2_85
    img 11628
    with fade
    w
    img 11629
    with diss
    w
    jane "Все-ли хорошо, Милый?"
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11630
    with diss
    jane "Миссис Бакфетт уже ушла?"
# Стив отвечает что она ушла Джейн просто не заметила ее.
# Стив знает что Джейн все время отлучается от рабочего места.
# И, если бы не ее хорошая попка, то он бы давно уволил ее за это.
# Джейн отвечает, что дело не только в этом и чтобы Стив не забывал.
# Джейн уходит
    music Groove2_85
    img 11631
    with fade
    steve "Да, Джейн."
    steve "Она уже ушла. Просто ты не заметила этого."

    music audio_Monica_Steve_Blowjob_IMG_1
    #blowjob
    img 11632
    with fade
    w
    #
    music Groove2_85
    img 11633
    with diss
    steve "Я знаю, что ты все время отлучаешься от рабочего места."
    steve "И, если бы не твоя хорошая попка, то я давно бы уволил тебя за это."
    img 11634
    with diss
    jane "Дело не только в моей попке, Стив."
    jane "Не забывай этого!"
    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
    call gallery_20385_1() # Стив кончает
    call gallery_20385_2() # Моника уходит
    return

label gallery_11664:
# Входит Тиффани
# Сцена 1
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив говорит чтобы она положила их на стол
# Джейн кладет сексуально и уходит
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11662
    with fadelong
    tiffany "Мистер Стив, можно войти?"
    img 11663
    with diss
    steve "Да, Тиффани, заходи!"
    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11627
    with diss
    w
    #
    sound highheels_short_walk
    music Groove2_85
    img 11664
    with fadelong
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    img 11665
    with diss
    steve "Да, Тиффани, можешь положить их на стол."
    sound snd_folder_drop
    img 11666
    with diss
    tiffany "..."

    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
    call gallery_20385_1() # Стив кончает
    call gallery_20385_2() # Моника уходит
    return

label gallery_11645:
# Сцена 2
# Джейн входит и спрашивает у Стива не забыл-ли он про свадьбу.
# Стив отвечает что не забыл.
# Джейн спрашивает когда будет дата свадьбы?
# Стив отвечает что это будет очень скоро, Стив работает над этим!
# Джейн отвечает: хорошо, милый и целует его в щечку
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11635
    with fadelong
    w
    img 11637
    with diss
    jane "Милый, ты не забыл про нашу свадьбу?"
    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11627
    with diss
    w
    #
    music Groove2_85
    img 11636
    with fade
    steve "Нет, милая, я не забыл."
    img 11638
    with diss
    steve "Я все помню!"
    img 11640
    with fade
    jane "Ты уже решил насчет даты, Милый?"

    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11641
    with fade
    w
    #

    music Groove2_85
    img 11642
    with fade
    steve "Еще нет, Милая, но это будет очень скоро."
    img 11639
    with diss
    steve "Я работаю над этим!"
    img 11643
    with fade
    jane "Хорошо, милый."
    music stop
    img 11644
    with diss
    w
    sound kiss2
    img 11645
    with diss
    jane "Чмок!"
    #уходит
    music Groove2_85
    sound highheels_short_walk
    img 11646
    with fadelong
    w
    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
    call gallery_20385_1() # Стив кончает
    call gallery_20385_2() # Моника уходит
    return

label gallery_11669:
# Сцена 2
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив просит Тиффани подойти поближе.
# Тиффани подходит и спрашивает что будет угодно ее Боссу?
# Стив говорит Тиффани что она такая красивая.
# Что Стив очень хочет оценить ее красоту.
# Стив кладет руку на ее ногу пониже попы
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11662
    with fadelong
    tiffany "Мистер Стив, можно войти?"
    img 11663
    with diss
    steve "Да, Тиффани, заходи!"

    music audio_Monica_Steve_Blowjob_IMG_1
    #blowjob
    img 11632
    with fade
    w

    sound highheels_short_walk
    music Groove2_85
    img 11664
    with fadelong
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    sound snd_folder_drop
    img 11667
    with diss
    steve "Тиффани, можешь подойти поближе?"
    sound highheels_short_walk
    img 11668
    with fadelong
    tiffany "Да, Босс, что Вам будет угодно?"
    music Loved_Up
    music2 audio_Monica_Steve_Blowjob_IMG_1
    img 11669
    with fade
    steve "Тиффани, малышка."
    steve "Ты такая красивая..."
    music2 stop
    img 11670
    with diss
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
    music Groove2_85
    img 11672
    with fade
    tiffany "Помнит-ли Мистер Стив мое условие?"
    img 11673
    with diss
    steve "Тиффани, твое условие трудно выполнимо."
    img 11674
    with diss
    steve "Но ведь это не помешает мне насладиться твоей красотой?"
    img 11675
    with fade
    tiffany "Уберите руку, Мистер Стив!"
    img 11676
    with diss
    tiffany "Иначе я заявлю о харрасменте!"
    img 11677
    with diss
    w
    music stop
    img 11678
    with diss
    w

# У Стива падает член.
    #звук вниз
    sound snd_down1
    img 11679
    with diss
    w
# Тиффани уходит
    music Groove2_85
    img 11680
    with fade
    w
    sound highheels_short_walk
    img 11681
    with fadelong
    tiffany "..."
    sound highheels_short_walk
    img 11682
    with diss
    w
    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
# Моника зло говорит из-под стола что у Стива упал член.
# И что теперь? Из-за этой дешевой шлюхи ей придется снова его поднимать?
# Стив отвечает что сложности бывают, но, Моника, что поделать, это твоя работа!
# Моника зло продолжает сосать член.
    music Groove2_85
    img 11683
    with fadelong
    w
    music Power_Bots_Loop
    img 11684
    with diss
    m "У тебя упал член, Стив!"
    img 11685
    with diss
    steve "..."
    img 11686
    with fade
    m "И что теперь?"
    m "Из-за этой дешевой шлюхи мне придется снова его поднимать?"
    music Groove2_85
    img 11687
    with diss
    steve "Моника, во время выполнения любого контракта бывают сложности."
    steve "Но что поделать? Это твоя работа."
    music Power_Bots_Loop
    img 11688
    with fade
    m "!!!"
    music Groove2_85
    img 11689
    with diss
    steve "Моника, ты можешь продолжать. Контракт еще не закрыт."
    img 11690
    with fade
    m "!!!"
    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11691
    with fade
    w
    stop music fadeout 1.0
    call textonblack(_("СПУСТЯ 15 МИНУТ..."))
    img black_screen
    with Dissolve(1)
# Моника зло продолжает сосать член.
    call gallery_20385_1() # Стив кончает
    call gallery_20385_2() # Моника уходит
    return

label gallery_11659:
# Сцена 3
# Джейн входит и говорит что соскучилась по любимому.
# А Стив? Стив отвечает что тоже соскучился.
# Джейн подходит ближе и спрашивает, любит-ли ее Стив?
# Стив отвечает что очень любит малышку Джейн.
# Джейн спрашивает: правда? Ты больше никого не любишь?
# У тебя больше никого нет кроме меня?
# Стив отвечает что любит только Джейн и она у него единственная.
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11635
    with fadelong
    w
    sound highheels_short_walk
    img 11647
    with fade
    jane "Милый, Я соскучилась по тебе."

    #blowjob
    music audio_Monica_Steve_Blowjob_IMG_1
    img 11648
    with diss
    w
    img 11649
    with diss
    w
    #
    music Groove2_85
    img 11650
    with diss
    steve "..."
    jane "А ты?"
    music Loved_Up
    img 11651
    with diss
    steve "..."
    music Groove2_85
    img 11652
    with diss
    jane "А, Стив?! Ты меня слышишь?"
    img 11653
    with fade
    steve "А?! Да, Джейн, я тоже соскучился по тебе."

    # Джейн подходит ближе
    sound highheels_short_walk
    img 11654
    with fade
    w
    img 11655
    with fade
    w
    img 11656
    with diss
    jane "Ты меня любишь, Стив?"

    img 11657
    with diss
    steve "Я очень люблю малышку Джейн!"
    img 11658
    with fade
    jane "Правда?"
    jane "Ты больше никого не любишь?"
    jane "У тебя больше никого нет кроме меня?"
    img 11659
    with diss
    jane "Я соблюдаю твой дурацкий дресс-код."
    jane "И я жду свадьбы, Стив!"
    img 11660
    with fade
    steve "Джейн, я люблю только тебя!"
#    #blowjob
#    music audio_Monica_Steve_Blowjob_IMG_1
#    img 11632
#    with fade
#    w
#    music Groove2_85
#    img 11660
#    with fade
    steve "И ты у меня единственная!"
    music stop
    sound kiss2
    img 11661
    with diss
    jane "Чмок!"
    #уходит
    music Groove2_85
    img 11646
    with fadelong
    w
    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
    call gallery_20385_1() # Стив кончает
    call gallery_20385_2() # Моника уходит
    return

label gallery_11699:
# Сцена 3
# Тиффани заходит и говорит Стиву что принесла отчеты
# Стив просит Тиффани подойти поближе
# Тиффани подходит и говорит что все уже сказала.
# Ее ответ нет и она догадывается что Стив хочет сейчас сделать.
# Стив подносит руку к Тиффани
    img black_screen
    with diss
    sound snd_door_open1
    pause 2.0
    music Groove2_85
    img 11662
    with fadelong
    tiffany "Мистер Стив, можно войти?"
    img 11663
    with diss
    steve "Да, Тиффани, заходи!"
    sound highheels_short_walk
    music Groove2_85
    img 11664
    with fadelong
    tiffany "Мистер Стив! Я принесла Вам отчеты."
    sound snd_folder_drop
    img 11667
    with diss
    steve "Тиффани, можешь подойти поближе?"
# Тиффани подходит и говорит что все уже сказала.

    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    img 11692
    with fadelong
    tiffany "Мистер Стив, я Вам все уже сказала."
    tiffany "Я догадываюсь что Вы сейчас хотите сделать."
    img 11693
    with diss
    tiffany "Мой ответ НЕТ!"

# Стив подносит руку к Тиффани
    sound Jump1
    img 11694
    with diss
    w
    img 11695
    with fade
# Тиффани говорит: только попробуйте, Мистер Стив...
# Стив говорит, что Тиффани так красива, так прекрасна
# Что Стив настолько сильно хочет ее, если бы она только знала...
# Что он.. он... Аааххх! Стив хватает Тиффани за попу под трусиками и кончает Монике в рот
    tiffany "Только попробуйте, Мистер Стив..."
    music Loved_Up
    img 11697
    with diss
    steve "О, Тиффани!"
    img 11696
    with diss
    steve "Ты так красива!"
    steve "Так прекрасна!"
    img 11698
    with diss
    steve "Если бы только знала как я хочу тебя!"
    music Loved_Up2
    sound Jump2
    img 11699
    with diss
    steve "Если бы ты только, Аааах!!"
# Что он.. он... Аааххх! Стив хватает Тиффани за попу под трусиками и кончает Монике в рот
    img 11700
    with diss
    tiffany "!!!"
    img 11701
    with diss
    steve "Аааах!"
    img 11702
    with diss
    steve "Аааах!"
    #звук кончания
    img 11703
    with diss
    sound bulk1
    steve "АААААААААААРГХХХХХ!!!"
    img 11704
    with diss
    w
    img 11705
    with diss
    sound bulk1
    steve "АААААААААААРГХХХХХ!!!"
    m "!!!"

# Тиффани смеется.
    music Groove2_85
    img 11706
    with fadelong
    tiffany "Ха!"
# Вы там что, кончили, Мистер Стив?
# Хи-хи-хи. Вы пополнили мою смешную коллекцию мужчин, которые кончают себе в штаны при моем виде.
# Моника зло смотрит из-под низа
# Хорошего рабочего дня, Мистер Стив...
# Уходит
    tiffany "Вы там что, кончили, Мистер Стив?"
    img 11707
    with diss
    steve "..."
    sound highheels_short_walk
    img 11708
    with fadelong
    tiffany "Хи-хи-хи."
    tiffany "Вы дополнили мою смешную коллекцию мужчин, которые при виде меня кончают в штаны."
    img 11709
    with diss
    w
    img 11710
    with diss
    m "!!!"
    sound highheels_short_walk
    img 11711
    with fadelong
    tiffany "Хорошего рабочего дня, Мистер Стив!"

    music stop
    img black_screen
    with diss
    sound snd_door_close1
    pause 2.0
#    call gallery_20385_1() # Стив кончает
    call gallery_20385_2() # Моника уходит
    return

label gallery_12633:
# Приходит к Джейн.
# Джейн с улыбкой смотрит на Монику.
# Моника говорит чтобы Джейн встала, когда перед ней стоит ее Босс!
# Джейн встает.
    music stop
    img black_screen
    with diss
    pause 1.5
    sound highheels_short_walk
    img 12578
    music Sneaky_Snitch
    with fadelong
    jane "Миссис Бакфетт?"
    music Pyro_Flow
    img 12579
    with fade
    m "!!!"
    img 12580
    jane "..."
    img 12581
    with diss
    m "Джейн!"
    m "Встань, когда перед тобой стоит твой Босс!"
    img 12582
    with fade
    w
# Моника надменно спрашивает что Джейн хочет узнать у Моники по поводу ее великолепной фигуры?
# Джейн спрашивает как Монике удалось достичь такой превосходной формы?
# Моника отвечает что все дело в правильном питании и регулярном занятии фитнессом.
# Джейн спрашивает, можно-ли ей рассмотреть Монику поближе.
# Моника надменно отвечает что не видит в этои необходимости, но так уж и быть.
# Джейн спрашивает у Моники чем она питается в данный момент? Какая сейчас лучшая диета?
    music Stealth_Groover
    img 12583
    with fadelong
    m "Итак..."
    m "Что ты хочешь узнать относительно моей великолепной фигуры?"
    img 12584
    jane "Миссис Бакфетт, скажите, как Вам удалось достичь такой превосходной формы?"
    img 12585
    with diss
    m "Все дело в правильном питании и регулярном занятии фитнесом."
    img 12586
    jane "Миссис Бакфетт, можно-ли мне рассмотреть Вашу фигуру поближе?"
    img 12587
    with fade
    m "Я не вижу в этом особой необходимости..."
    img 12588
    with diss
    jane "..."
    img 12589
    with fade
    m "Но, так уж и быть!"
    #Джейн подходит и осматривает Монику
    music stop
    img black_screen
    with diss
    pause 1.0
    sound highheels_short_walk
    music Sneaky_Snitch
    img 12590
    with fade
    w
    img 12591
    with diss
    sound highheels_short_walk
    w
    img 12592
    with fade
    jane "Миссис Бакфетт, скажите, чем Вы питаетесь в данный момент?"
    jane "Какая сейчас лучшая диета?"

# Моника сконфужена...
# Чем я питаюсь? Моя диета?
# Да уж! Я боюсь что эта толстая корова не сможет выжить на моей сегодняшней диете...
    music Hidden_Agenda
    img 12593
    with fade
    mt "Чем я питаюсь?"
    mt "Моя диета?"
    mt "Да уж!"
    mt "Я боюсь что эта толстая корова не сможет выжить на моей сегодняшней диете..."

# Моника отвечает что за ее рационом следит известный доктор, который скурпулезно составляет необходимые вещества.
# В общем, Джейн. Ты себе такого позволить не сможешь. Если есть другие вопросы, то задавай скорее и закончим.
    music Stealth_Groover
    img 12594
    with fade
    m "За моим рационом следит известный доктор!"
    m "Который скурпулезно составляет список блюд, содержащих необходимые вещества и витамины."
    img 12595
    with diss
    m "В общем, Джейн."
    img 12596
    jane "..."
    img 12597
    m "Ты себе такого позволить не сможешь."
    m "Если есть другие вопросы, то задавай скорее и закончим с этим."

# Джейн обсматривает Монику.
    music stop
    img black_screen
    with diss
    pause 1.0
    music Sneaky_Snitch
    img 12598
    with fadelong
    w
    img 12599
    with diss
    w
    img 12600
    with diss
    jane "..."
    img 12601
    with diss
    m "..."

# Миссик Бакфетт, Вы говорили что-то по поводу фитнесса.
# Да, Джейн. Фитнесс и йога - неотъемлемая часть построения изящной фигуры...
    img 12602
    with fadelong
    jane "Миссис Бакфетт."
    jane "Вы говорили по поводу фитнеса..."
    img 12603
    m "Да, Джейн."
    m "Фитнес и йога - неотъемлемая часть построения изящной фигуры..."

# Джейн спрашивает в какой фитнесс-центр сейчас ходит Моника и может-ли она помочь ей тоже устроиться туда на занятия.
# Моника отвечает что с ней занимается личный тренер, который внешне соответствует здоровому образу жизни.
# А также знает толк в упражнениях для достижения нужной цели.
    img 12604
    with fade
    jane "Миссис Бакфетт."
    jane "А в какой фитнес-центр Вы сейчас ходите заниматься?"
    img 12605
    jane "Могли-бы Вы мне помочь тоже устроиться туда на занятия?"
    music Stealth_Groover
    img 12606
    with fade
    m "Со мной занимается личный тренер, который даже внешне соответствует здоровому образу жизни."
    m "А также знает толк в упражнениях для достижения нужной цели!"

# Однако, к этому тренеру многие стараются попасть и у тебя, Джейн, нет никаких шансов на это.
    img 12607
    m "Однако, к этому тренеру многие стараются попасть."
    m "И у тебя, Джейн, нет никаких шансов на это!"

# Джейн спрашивает, можно-ли попасть в ее фитнесс-центр к другому тренеру?
# Моника отвечает что ее центр - только для элитных девушек, имеющих положение в обществе
# и туда можно попасть только по приглашению.
# Моника, естественно, не собирается это пришлашение Джейн давать!
    img 12608
    jane "Можно-ли попасть в Ваш фитнес-центр к другому тренеру?"
    img 12609
    with fade
    m "Фитнес-центр, куда я хожу - только для элитных девушек, имеющих положение в обществе!"
    m "И туда можно попасть только по приглашению."
    img 12610
    jane "..."
    img 12611
    with diss
    m "И, разумеется, я не собираюсь давать это приглашение для тебя, Джейн!"

# Моника думает про себя, что ей не хватало еще в фитнесс центре Джейн или этой проститутки Тиффани.
# Учитывая как Бетти обращается с Моникой там, не будет ничего хорошего если эти дуры станут свидетелями этого.
    music Hidden_Agenda
    img 12612
    with fade
    mt "Еще мне не хватало в фитнес-центре Джейн или этой проститутки..."
    mt "Как ее там..."
    mt "Тиффани..."
    img 12613
    with diss
    mt "!!!"
    mt "Учитывая, как Бетти обращается со мной там, не будет ничего хорошего если эти дуры станут свидетелями этого..."

# Джейн обиженно смотрит.
# Джейн говорит: Миссис Бакфетт.
    music Sneaky_Snitch
    img 12614
    with fade
    jane "..."
    jane "Миссис Бакфетт..."

# Моника прерывает. Джейн! Ты еще не закончила со своими дурацкими вопросами?!
# Я оказываю безмерную услугу Стиву тем, что согласилась ответить на несколько вопросов для его будущей супруги.
# Но ты начинаешь меня утомлять, Джейн!
# Давай заканчивай!
# Моника думает (я хочу побыстрее пообедать в дорогом ресторане!)
    music Power_Bots_Loop
    img 12615
    with fade
    m "Джейн! Ты еще не закончила со своими дурацкими вопросами?!"
    m "Я оказываю безмерную услугу Стиву тем, что согласилась ответить на несколько вопросов для его будущей супруги."
    img 12616
    m "Но ты начинаешь меня утомлять, Джейн!"
    m "Давай заканчивай!"
    img 12617
    with diss
    mt "Мне надоела эта Джейн!"
    mt "Я хочу побыстрее пообедать в дорогом ресторане!"

# Джейн говорит: Миссис Бакфетт. Мистер Стив сказал что Вы покажете мне свою грудь...
# Моника шипит. Джейн, ты не перегибаешь палку?!
# Джейн отвечает, Миссис Бакфетт, простите! Просто так сказал Мистер Стив!...
# Я не хотела как-то оскорбить Вас!
    music stop
    img black_screen
    with diss
    pause 1.0
    music Sneaky_Snitch
    img 12618
    with fadelong
    jane "Миссис Бакфетт..."
    jane "Мистер Стив сказал, что Вы покажете мне свою грудь..."
    music Power_Bots_Loop
    img 12619
    with diss
    mt "!!!"
    img 12620
    m "Джейн! Ты не перегибаешь палку?!"
    img 12621
    with fade
    jane "Миссис Бакфетт, простите! Просто так сказал Мистер Стив!..."
    jane "Я не хотела как-то оскорбить Вас!"

# выбор Моники:
# показать грудь
# не показывать грудь (нарушение контракта)
    img 12622
    with fade
    menu:
        "Показать грудь":
            pass
        "Не показывать грудь (нарушение контракта)":
# Моника не показывает грудь:
# Моника говорит что не собирается ничего показывать Джейн. Достаточно и так!
            img 12623
            with fade
            m "Я не собираюсь ничего показывать, Джейн!"
            m "Достаточно и так!"

# После этого, Моника возвращается к Стиву закрыть контракт.
# Моника говорит Стиву что сделала как они договорились и она ждет тикет на ланч в ресторане.
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.5
            music Hidden_Agenda
            img 12645
            with fadelong
            m "Стив!"
            m "Я достаточно рассказала твоей невесте, как мы договорились."
            img 12646
            m "Я жду сертификат на ланч в ресторане."

# Если Моника не показала грудь Джейн, то Стив заявляет что Моника нарушила контракт и не показала грудь.
# За это полагается неустойка, в виде одного бесплатного контракта на массаж его члена.
# Моника злится и говорит чтобы Стив пошел к черту со своими контрактами!
            music Groove2_85
            img 12647
            with fade
            steve "Моника, но ты не показала свою грудь Джейн!"
            steve "Ты нарушила контракт!"
            img 12648
            with diss
            steve "За это полагается неустойка в виде бесплатного контракта на массаж моего члена, хе-хе!"
            music Power_Bots_Loop
            img 12649
            with fadelong
            m "Иди ты к черту со своими контрактами!!!"
            return

# Моника говорит что Стив умолял Монику сделать это.
# К тому же, Монике есть чем гордится и она, так уж и быть, сделает это.
# Моника показывает грудь Джейн.
    img 12624
    with fade
    mt "!!!"
    img 12625
    with diss
    jane "..."
    music Hidden_Agenda
    img 12626
    with fade
    m "Ладно..."
    m "Стив умолял меня сделать это..."
    img 12627
    jane "..."
    img 12628
    m "К тому же, мне есть чем гордиться."
    m "И я, так уж и быть, сделаю это..."

# Моника показывает грудь.
    label gallery_12638:
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 12629
    with fadelong
    w
    img 12630
    with diss
    w
    img 12631
    with diss
    w
# Джейн спрашивает, а они настоящие? можно-ли потрогать?
# выбор Моники: Можно потрогать или не дать трогать грудь
    img 12632
    jane "Миссис Бакфетт, а они настоящие?"
    jane "Можно потрогать?"
    img 12633
    with diss
    menu:
        "Дать потрогать свою грудь.":
# Если дает потрогать, то:
# Моника шипит: Можно, только быстро, Джейн!
# Джейн трогает грудь
# Моника закрывается и говорит что довольно.
            img 12634
            with fade
            m "Можно, только быстро, Джейн!"
            music Loved_Up2
            img 12636
            with diss
            w
            img 12635
            with diss
            w
            img 12637
            with diss
            mt "Как же мне противно!"
            img 12638
            with diss
            jane "..."
            music Power_Bots_Loop
            img 12639
            with fade
            m "Довольно!"

        "Не дать потрогать свою грудь.":

# Моника говорит что нельзя потрогать грудь:
# Моника шипит и говорит Джейн что только попробуй!
# Джейн ошеломленно отвечает что просто хотела проверить, настоящие они или нет?
# Моника отвечает что они настоящие, как и сама Моника, в отличие от Джейн, которая является лишь тенью Стива.
            music Power_Bots_Loop
            img 12640
            with fade
            m "Только попробуй!"
            img 12641
            jane "Простите, Миссис Бакфетт."
            jane "Я только хотела проверить, настоящие они или нет..."
            img 12642
            with diss
            m "Они настоящие, как и я сама!"
            m "В отличие от тебя Джейн!"
            img 12643
            m "Ты являешься лишь тенью Стива!"
# Джейн обиженно смотрит.
            img 12644
            jane "!!!"


# Если Моника показала грудь Джейн, то Стив дает тикет на ланч в ресторане (предмет)
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    img 12650
    with fadelong
    m "Стив!"
    m "Я достаточно рассказала твоей невесте, как мы договорились."
    img 12651
    m "Я жду сертификат на ланч в ресторане."

    # Стив кладет сертивикат
    sound snd_folder_drop
    img 12652
    with fade
    steve "Моника!"
    steve "Ты жестокая женщина!"
    sound snd_take_paper
    img 12653
    with diss
    steve "Сначала ты оставила меня без денег, а теперь оставляешь и без еды!"
    # Моника уходит
    music Power_Bots_Loop
    img 12654
    with fadelong
    m "Не забывай при каких обстоятельствах это происходило!"
    m "Ты еще ответишь за все, что сделал!"
    return
