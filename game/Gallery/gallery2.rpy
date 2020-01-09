
label gallery_15521:
    music stop
    scene black_screen
    with Dissolve(1)
    # Виктория смотрит на Монику с ухмылкой
    music Groove2_85
    img 15517
    with fade
    victoria "Подружка Моника, ты скучала по мне?"
    # Виктория поворачивается к Мелани
    img 15518
    with diss
    victoria "Эта подружка по мне скучала, она всегда так рада меня видеть..."
    victoria "Правда, рада?"
    img 15519
    with fade
    victoria "Что ты делаешь при встрече, подружка Мелани?"
    # пристально с высока смотрит на Мелани и показыват пальцем на свою щеку
    music Master_Disorder
    img 15520
    with diss
    melanie "..."
    img 15521
    with diss
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
    # Мелани немного медлит, потом подходит к ней и чмокает ее в щеку
    # Моника смотрит на это в полнейшем изумлении
    music Groove2_85
    img 15522
    with fade
    sound highheels_short_walk
    w
    music Loved_Up
    img 15523
    with diss
    sound snd_kiss2
    w
    music Master_Disorder
    img 15524
    with fade
    mt "???"
    mt "Виктория указывает Мелани?"
    mt "Я ничего не понимаю..."
    # Мелани садится за столик, берет бокал в руку
    # Виктория говорит Мелани
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 15525
    with fadelong
    victoria "Молодец, ты хорошая подружка."
    # поворачивается к Монике
    img 15526
    with fade
    victoria "А ты?"
    victoria "Ты моя подружка?"
    # Моника нерешительно
    music Master_Disorder
    img 15527
    with diss
    m "Д-да..."
    # Виктория пристально смотрит на Монику
    img 15528
    with fade
    victoria "Скажи это!"
    img 15529
    with diss
    m "Я... Я твоя... Подружка."
    music Power_Bots_Loop
    img 15530
    with fade
    victoria "Скажи это еще раз! Я не расслышала!"
    music Master_Disorder
    img 15531
    with diss
    m "Я твоя подружка!"
    # Виктория продолжает сверлить Монику взглядом
    img 15532
    with fade
    victoria "Ты моя ХОРОШАЯ подружка? Скажи мне!"
    img 15533
    with diss
    m "Да, я хорошая подружка..."
    music Power_Bots_Loop
    img 15534
    with fade
    mt "Какого черта она тут делает?"
    mt "Что ей нужно?"
    img 15535
    with diss
    mt "Может, она хочет, чтобы я платила ей еще больше денег?"
    mt "???"
    # Виктория говорит Монике
    music Groove2_85
    img 15536
    with fade
    victoria "Если ты хорошая подружка, то должна была скучать по мне..."
    victoria "И радоваться нашей встрече."
    victoria "Ты рада видеть меня, подружка Моника?"
    m "..."
    # Моника непонимающе смотрит на Мелани, та сидит за столиком с бокалом в руке и наблюдает за сценой
    # Моника поворачивается снова к Виктории, та вопросительно поднимает брови
    img 15537
    with diss
    victoria "Ты настолько рада, что не можешь найти слов?"
    img 15538
    with fade
    m "Я так рада нашей встрече, что не могу найти подходящих слов..."
    img 15539
    with diss
    victoria "Странно, что ты не можешь сказать мне ничего приятного при встрече."
    victoria "Ты точно скучала по мне?"
    img 15540
    with fade
    m "Да... Скучала..."
    music Power_Bots_Loop
    img 15541
    with diss
    mt "Ненавижу эту маленькую дрянь!!!"
    mt "!!!"
    # Виктория продолжает смотреть на Монику
    music Groove2_85
    img 15542
    with fade
    victoria "Мелани хорошая подружка. Она целует меня при встрече..."
    victoria "А ты? Ты же скучала?"
    victoria "Почему ты не хочешь поцеловать меня?"
    # Моника медлит
    music Master_Disorder
    img 15543
    with diss
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
        "Не делать этого! (пропуск сцены)":
            img 15545
            with fade
            mt "Фу! Мне к ней не то что прикасаться, мне на нее смотреть противно!"
            music Power_Bots_Loop
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            music stop
            img black_screen
            with diss
            sound highheels_run2
            ##### арт Моника убегает
            return
    mt "Просто надо чмокнуть эту стерву в щеку, как сделала Мелани..."
    mt "Тогда она отвяжется от меня."
    img 15544
    with fade
    mt "Фу! Мне к ней не то что прикасаться, мне на нее смотреть противно!"
    mt "!!!"
    # Моника подходит к Виктории и чмокает ее в щеку, та довольно хихикает
    # Виктория подходит к столику, ставит сумочку на него, берет бокал
    img 15545
    with fade
    w
    img 15546
    with diss
    sound highheels_short_walk
    w
    music Loved_Up
    img 15547
    with diss
    w
    img 15548
    with diss
    sound snd_kiss2
    w
    img 15549
    with diss
    sound snd_woman_laugh3
    victoria "Подружка Моника, садись за столик. Девичник начинается!" # хихикает
    # Моника садится напротив Мелани, берет бокал в руку
    # Виктория протягивает свой бокал к ним
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 15550
    with fadelong
    victoria "Подружки, наконец-то мы с вами все вместе встретились..."
    # чокаются со звоном бокалов
    # Виктория с интересом оглядывает квартиру Мелани, та вместе с Моникой смотрят на нее
    img 15551
    with fade
    victoria "Мне нравится квартира моей подружки Мелани..."
    img 15552
    with diss
    victoria "Особенно ее фотографии..."
    victoria "Хочу поближе их рассмотреть. Ты же не против, подружка?"
    # Мелани отвечает равнодушно, не глядя на нее
    img 15553
    with fade
    melanie "Я не против..."
    # Виктория подходит к портретам Мелани на стене и рассматривает их
    sound highheels_short_walk
    img 15554
    with diss
    victoria "Фотографии мне нравятся, но чего-то все равно не хватает..."
    img 15555
    with diss
    victoria "Хмм..." # делает вид, что задумалась
    # Виктория подходит к столику с косметикой, берет помаду Мелани (или достает ее из своей сумочки, если нет столика)
    # потом идет к фотографиям на стене
    # помадой рисует на портрете Мелани ей улыбку
    # Мелани молча бесится, убийственным взглядом наблюдая за этим действием
    sound highheels_short_walk
    img 15556
    with fade
    w
    img 15557
    with diss
    sound swish
    w
    img 15558
    with diss
    sound Jump1
    w
    music Power_Bots_Loop
    img 15559
    with diss
    melanie "!!!"
    # Виктория поворачивается к ней
    label gallery_15565:
    music Groove2_85
    img 15560
    with fade
    sound vjuh3
    w
    img 15561
    with diss
    sound vjuh4
    w
    img 15562
    with fade
    victoria "Так портрет смотрится намного гармоничнее."
    victoria "Ты согласна со мной, подружка Моника?"
    # Моника вопросительно смотрит на Мелани, та зло молчит
    music Power_Bots_Loop
    img 15563
    with diss
    melanie "!!!"
    # Моника снова смотрит на Викторию
    img 15564
    with diss
    m "Да... Так стало еще лучше..."
    # Виктория смеется, потом смотрит на Мелани
    music Groove2_85
    img 15565
    with fade
    sound snd_woman_laugh3
    victoria "А ты что скажешь, подружка Мелани?"
    # Мелани зло на нее смотрит
    music Power_Bots_Loop
    img 15566
    with diss
    melanie "!!!"
    # потом делает глоток из бокала, берет себя в руки и говорит спокойно
    music ZigZag
    img 15567
    with fade
    sound snd_beer_table
    melanie "Я согласна с Миссис Бакфетт."
    music Groove2_85
    img 15568
    with diss
    victoria "В чем именно ты согласна с моей подружкой Моникой?"
    victoria "Скажи мне это!"
    music ZigZag
    img 15569
    with fade
    melanie "Мои портреты стали еще лучше..."
    music Groove2_85
    img 15570
    with diss
    victoria "И кого ты должна поблагодарить за это?"
    music ZigZag
    img 15571
    with fade
    melanie "Тебя... Подружка."
    music Groove2_85
    img 15572
    with diss
    sound highheels_short_walk
    victoria "А как ты меня будешь благодарить, подружка Мелани?"
    # Мелани вопросительно смотрит на нее
    img 15573
    with fade
    melanie "..."
    melanie "Скажу тебе спасибо."
    # Виктория смеется
    img 15574
    with diss
    sound snd_woman_laugh3
    victoria "Этого недостаточно!"
    # Мелани вопросительно поднимает бровь
    # Виктория делает серьезную мину
    music Power_Bots_Loop
    img 15575
    with fade
    melanie "!!!"
    melanie "!!!!!!"
    melanie "!!!!!!!!!"
    w
    music Groove2_85
    img 15576
    with diss
    victoria "Во-первых, не вздумай стирать это со своих фотографий!"
    victoria "Тебе же нравится моя работа?"
    # Мелани напряжанно отвечает
    music Power_Bots_Loop
    img 15577
    with fade
    melanie "Да..."
    music Groove2_85
    img 15578
    with diss
    sound highheels_short_walk
    victoria "Я не слышу!"
    music Power_Bots_Loop
    img 15579
    with fade
    melanie "Да. Мне нравится твоя работа."
    music Groove2_85
    img 15580
    with diss
    victoria "Во-вторых..."
    # делает многозначительную паузу, подходит к столику, за которым сидят Мелани с Моникой
    img 15581
    with fade
    victoria "Во-вторых, я, как и обещала, принесла вам, мои подружки, подарок..."
    # смотрит с улыбкой на Мелани, потом на Монику
    img 15582
    with diss
    victoria "Подружки ведь хотят узнать, какой подарок я для них приготовила?"
    victoria "Это подарок только для хороших подружек..."
    victoria "Вы же хорошие подружки?"
    # Мелани с Моникой переглядываются напряженно
    music Master_Disorder
    img 15583
    with fade
    melanie "..."
    img 15584
    with diss
    m "..."
    img 15585
    with diss
    melanie "Мы хорошие подружки..."
    music Groove2_85
    img 15586
    with fade
    victoria "Чьи вы хорошие подружки?"
    img 15587
    with diss
    m "Твои хорошие подружки..."
    img 15588
    with fade
    victoria "Мои хорошие подружки хотят получить подарок от меня?"
    music Master_Disorder
    img 15589
    with diss
    melanie "Да..."
    # Виктория самодовольно хихикает, ставит одну ногу на столик, смотрит на Монику с Мелани сверху вниз
    # проводит пальцами вверх по своему бедру и немного приподнимает свое платье, становится видно, что она без трусиков
    music Groove2_85
    img 15549
    with diss
    sound snd_woman_laugh3
    w
    img 15590
    with fade
    sound Jump1
    victoria "Тогда подружки должны заслужить свой подарок!"
    img 15591
    with diss
    sound plastinka1b
    w
    img 15592
    with diss
    w
    # Моника с Мелани в шоке смотрят на нее, но ничего не предпринимают
    music Power_Bots_Loop
    img 15594
    with fade
    melanie "..."
    img 15593
    with diss
    m "!!!"
    music Groove2_85
    img 15595
    with fade
    victoria "Подружки, скажите, я красивая? Вам нравится на меня смотреть?"
    img 15596
    with diss
    m "..."
    img 15597
    with fade
    melanie "Ты красивая и нам нравится на тебя смотреть..."
    img 15598
    with diss
    victoria "Раз я вам так нравлюсь, подружки, то я разрешаю вам поцеловать меня..."
    victoria "Кто из подружек хочет сделать это первой, м?"
    # Мелани с Моникой молча переглядываются, лицо Мелани остается безэмоциональным, у Моники отвращение на лице
    music Power_Bots_Loop
    img 15599
    with fade
    melanie "..."
    img 15600
    with diss
    m "!!!"
    music Groove2_85
    img 15601
    with fade
    victoria "Вижу, что вы никак не можете решить, кто из вас будет первой..."
    victoria "Я помогу вам, вы ведь мои хорошие подружки."
    victoria "Вы что, хотите, чтобы я вам помогла?"
    # молчание
    music Master_Disorder
    img 15604
    with diss
    mt "Черт! Она сейчас разозлится..."
    mt "Потом еще и увеличит сумму еженедельных выплат..."
    mt "Где я найду столько денег для нее?!"
    img 15605
    with fade
    mt "Одного слова этой дряни достаточно, чтобы Дик сдал меня Маркусу и его людям..."
    mt "Этот тюфяк полностью в ее власти!"
    mt "!!!"
    music Power_Bots_Loop
    img 15606
    with hpunch
    mt "Неужели мне придется сделать ЭТО?!"
    mt "ФУУУУ! Какая мерзость!!!"
    mt "!!!"
    # Мелани задумчиво смотрит на сумочку Виктории
    music Master_Disorder
    img 15603
    with fade
    melanie_t "Эта мелкая дрянь принесла что-то в сумочке и не хочет это давать просто так..."
    melanie_t "Возможно, это какая-то важная информация."
    melanie_t "Маленькая дрянь хочет сначала поиграться..."
    img 15602
    with diss
    melanie_t "Самый простой выход - притвориться, что я не против."
    melanie_t "Все равно, я скоро найду способ наказать ее за все это..."
    music Power_Bots_Loop
    img 15607
    with vpunch
    victoria "Я НЕ СЛЫШУ ОТВЕТА!"
    victoria "Подружки нехорошие?!"
    victoria "Они хотят меня расстроить?!"
    # Моника с Мелани вздрагивают, смотрят друг на друга, молчание
    music Master_Disorder
    img 15608
    with fade
    melanie "..."
    img 15609
    with diss
    m "..."
    img 15610
    with fade
    menu:
        "Подыграть Виктории":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15604
            with fade
            mt "Я не собираюсь заниматься этими извращенскими мерзостями!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            return
    # Моника, глядя на Мелани
    img 15611
    with diss
    m "Мы не хотим тебя расстраивать... Подружка..."
    # Мелани, глядя на Монику
    img 15612
    with diss
    melanie "Мы хотим, чтобы ты помогла нам... Подружка."
    # поворачиваются к ней
    music Groove2_85
    img 15613
    with fade
    victoria "Так-то лучше!"
    victoria "А то я в какой-то момент стала подозревать..."
    victoria "Что вы только притворяетесь моими подружками..."
    # молчание, Виктория с нехорошей ухмылкой смотрит на них
    music Power_Bots_Loop
    img 15602
    with diss
    melanie "..."
    img 15531
    with diss
    m "..."
    # перемещая палец в сторону Моники
    music Groove2_85
    img 15614
    with fade
    victoria "Итак! Я придумала!"
    victoria "Ты, подружка Моника, помнишь, что тебе нельзя трогать мою киску?"
    victoria "Ты пока допущена только до моей попы!"
    victoria "Ты еще не достаточно хорошая подружка для моей киски."
    # Мелани удивленно приподнимает брови и смотрит на Монику
    img 15615
    with diss
    m "..."
    # Виктория указывает пальцем на Мелани
    img 15616
    with fade
    victoria "Ты, подружка Мелани, трогаешь только мою киску."
    victoria "Попу тебе трогать нельзя. Она только для подружки Моники."
    music Hidden_Agenda
    img 15617
    with diss
    victoria "Я разрешу тебе это делать, потом..."
    victoria "Уверена, ты меня сама попросишь об этом..."
    # обе подружки не торопятся исполнять указание Виктории
    music Power_Bots_Loop
    img 15618
    with fade
    melanie "..."
    m "..."
    music Groove2_85
    img 15619
    with diss
    victoria "Можете начинать! Давайте, я жду!"
    # Виктория поднимает свое платье выше
    # Мелани ставит бокал на стол, бросает еще один взгляд на Монику, поднимается с дивана и подходит к Виктории
    # смотрит на нее в упор
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    img 15620
    with fadelong
    w
    music Groove2_85
    img 15621
    with diss
    victoria "Я вижу, подружка Мелани, что тебе не терпится поцеловать мою киску. Скажи мне это."
    music Power_Bots_Loop
    img 15622
    with fade
    melanie "..."
    img 15623
    with diss
    menu:
        "Сказать, что приказывает Виктория":
            pass
    img 15624
    with fade
    melanie "Мне... Мне не терпится поцеловать тебя..."
    # Моника все еще на диване и смотрит с отвращением
    music Groove2_85
    img 15625
    with diss
    victoria "Нет, не так! Скажи это еще раз!"
    music Power_Bots_Loop
    img 15626
    with fade
    melanie "Мисс Виктория, мне не терпится поцеловать вашу... Вашу киску..."
    # Виктория, улыбаясь
    music Groove2_85
    img 15627
    with diss
    victoria "Хорошая подружка Мелани."
    victoria "Моей киске тоже не терпится... Она уже вся влажная."
    victoria "На колени!"
    # Мелани медлит, смотрит в глаза Виктории
    music Power_Bots_Loop
    img 15628
    with fade
    melanie "..."
    img 15629
    with diss
    menu:
        "Встать на колени и поцеловать киску Виктории":
            pass
    # Мелани опускается на колени, киска Виктории прямо у нее перед глазами
    # смотрит, потом приближает лицо и прикасается губами к ней
    music stop
    img black_screen
    with diss
    sound snd_paper1
    pause 1.0
    music Loved_Up
    img 15630
    with fadelong
    sound lick10
    victoria "М-м-м-м-м..."
    victoria "Какая хорошая подружка Мелани!"
    img 15631
    with fade
    victoria "Давай еще разочек!"
    # Мелани целует еще раз, потом немного отстраняется
    # Виктория немного разворачивается, киска раскрывается, она кладет руку на голову Мелани
    # потом поворачивается к Монике
    img 15632
    with diss
    victoria "А подружка Моника хорошая?"
    victoria "Или она хочет отказаться от моего подарка и расстроить меня?"
    # Моника молчит
    music Power_Bots_Loop
    img 15606
    with fade
    mt "Фу!!! Я не представляю, как я буду делать это!"
    mt "Какая мерзость!!!"
    mt "!!!"
    # Виктория смотрит на нее в упор, Моника ставит бокал на стол, бросает взгляд на Мелани
    # Моника поднимается с дивана и подходит к Виктории сзади, медлит
    music Master_Disorder
    img 15633
    with diss
    mt "!!!"
    menu:
        "Поцеловать попу Виктории":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15633
            with fade
            mt "Нет! Я, Моника Бакфетт! Я леди!"
            mt "Я не собираюсь целовать тощую задницу этой мелкой стервы!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            return
    # встает на колени
    music stop
    img black_screen
    with diss
    sound snd_paper1
    pause 1.0
    music Groove2_85
    img 15635
    with fade
    victoria "Давай, подружка Моника, целуй меня!"
    victoria "Тебе же нравится моя попа?"
    music Power_Bots_Loop
    img 15636
    with diss
    mt "Твоя попа отвратительна!!! Также как и ты!!!"
    img 15637
    with diss
    m "Да... Нравится..."
    music Groove2_85
    img 15638
    with fade
    victoria "Прикоснись к ней губами."
    # Моника прикасается губами к ягодицам, сначала к одной
    music stop
    stop music
    music2 Loved_Up
    img 15634
    with diss
    sound lick10
    victoria "Да, подружка хорошая! Поцелуй еще!"

    # причесать
    music stop
    img black_screen
    with diss
    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    play music "<from " + str(float(rand(1,4))*1.66666667) + " loop 0.0>Sounds/v_Victoria_Monica_Melanie_Licking1_1.ogg"
    scene black
    image videov_Victoria_Monica_Melanie_Licking1_1 = Movie(play="video/v_Victoria_Monica_Melanie_Licking1_1.mkv", fps=30)
    show videov_Victoria_Monica_Melanie_Licking1_1
    with fadelong
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    music2 Loved_Up
    # Моника прикасается ко второй ягодице губами
    #victoria "А теперь подружка Моника потрогает руками мою попу..."
    #victoria "Раздвинет ее половинки в стороны и поцелует мою дырочку..."
    # Моника кладет ладони, разводит ягодицы, смотрит, на лице отвращение
    #mt "!!!"
    # Виктория переключается на Мелани
    img 15639
    with fade
    victoria "Хорошая подружка Мелани сейчас поцелует мою киску еще раз."
    victoria "Тебе ведь нравится целовать мою киску, м?"
    music2 Power_Bots_Loop
    img 15640
    with diss
    melanie "Да. Нравится."
    music2 Groove2_85
    img 15641
    with fade
    victoria "Что тебе нравится?"
    music2 Power_Bots_Loop
    img 15642
    with diss
    melanie "Мне нравится целовать твою киску..."
    music2 Loved_Up
    img 15643
    with fade
    victoria "Я разрешаю тебе поцеловать мою киску еще, раз тебе это так нравится."
    # Мелани снова прикасается губами к киске Виктории
    img 15644
    with diss
    victoria "А теперь я разрешаю подружке Мелани потрогать мою киску язычком." # клитор
    victoria "М-м-м-м. Да, хорошая подружка!"
    victoria "И еще раз... Да, так!"

    img 15645
    with fade
    victoria "А теперь подружка Мелани найдет мою дырочку и полижет ее." # влагалище
    victoria "Давай, да!"
    sound lick10
    victoria "А подружка Моника чего ждет?"
    #mt "!!!"
#    victoria "Я ей уже разрешила целовать мою вторую дырочку!"
    # Моника с отвращением прикасается губами к анусу, отстраняется
    # причесать

    img 15646
    with diss
#    victoria "А теперь я разрешаю полизать подружке Монике мою вторую дырочку."
    # Моника проводит кончиком языка
    #mt "Фуууу!!!"
    victoria "А теперь еще раз, подружка Моника! И посмелее!"
    # Моника снова проводит языком по анусу

    $ renpy.music.set_volume(0.5, 0.5, channel="music2")
    music stop
    img black_screen
    with diss
    stop music
    play music "<from " + str(float(rand(1,4))*1.66666667) + " loop 0.0>Sounds/v_Victoria_Monica_Melanie_Licking1_1.ogg"
    scene black
    image videov_Victoria_Monica_Melanie_Licking1_2 = Movie(play="video/v_Victoria_Monica_Melanie_Licking1_2.mkv", fps=30)
    show videov_Victoria_Monica_Melanie_Licking1_2
    with fadelong
    wclean
    stop music
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
#    music Loved_Up

    img 15647
    with fade
    victoria "Да, так! Давай! М-м-м-м..."
#    victoria "Подружка Мелани, теперь засунь свой язычок в мою дырочку."
    # Мелани выполняет, начинает двигать языком внутрь-наружу. Моника продолжает лизать.
    # Виктория приспускает лямки на своем платье, обнажает грудь
    # сжимает обеими руками свои соски, откидывает голову назад, глаза закрыты
    sound lick10
    img 15648
    with diss
    sound ahhh1
    w
    img 15649
    with diss
    victoria "Да-а-а... М-м-м-м..."
    img 15650
    with fade
    victoria "Какие подружки хорошие... Как они стараются получить мой подарок..."
    # Виктория наклоняется немного, дотягивается рукой до сумочки, достает из нее телефон
    label gallery_15651:
    music stop
    music2 stop
    img black_screen
    with diss
    sound vjuh3
    pause 1.0
    music Loved_Up
    img 15651
    with fadelong
    victoria "Хорошие подружки не останавляваются!"
    victoria "Они продолжают лизать своим язычками мои обе дырочки!"
    w
    sound camera_lens1
    img 15719
    with Dissolve(0.2)
    w
    call photoshop_flash()
    w
    img 15652
    with fade
    sound lick10
    victoria "Подружки знают, что мне это нравится..."
    w
    call photoshop_flash()
    w
    # Виктория делает селфи, держа телефон над собой на вытянутой руке, на фото видно головы Моники и Мелани
    victoria "Подружки не должны останавляваться, иначе я огорчусь."
    # Виктория делает еще селфи сбоку, теперь на фото видно лица Моники и Мелани
    # убирает телефон обратно в сумочку, выпрямляется и говорит
    img 15653
    with diss
    victoria "Думаю, что время подарка уже пришло..."
    victoria "Хорошие подружки заслужили подарок!"
    victoria "СТОП!!!"
    # Мелани и Моника отстраняются от Виктории
    # Моника с отвращением вытирает рот рукой, Мелани тоже вытирает рот, при этом заинтересованно смотрит на сумочку Виктории
    # Виктория снимает ногу со стола
    music Groove2_85
    img 15654
    with fade
    victoria "Подружки хорошо постарались..."
    victoria "Пришло время подарка. Кто хочет первый его получить?"
    # молчание
    music Master_Disorder
    img 15655
    with diss
    melanie "..."
    img 15656
    with diss
    m "..."
    music Groove2_85
    img 15657
    with fade
    victoria "Мне кажется, что подружка Мелани будет первой..."
    victoria "Потому что ей так хотелось поласкать язычком мою дырочку... Что ее не пришлось заставлять..."
    img 15658
    with diss
    victoria "Да, подружка?"
    victoria "Чтобы получить подарок от меня, тебе нужно снять одежду... И трусики тоже..."
    # Мелани удивленно смотрит на Викторию, продолжая сидеть на коленях
    music Power_Bots_Loop
    img 15659
    with fade
    melanie "Снять одежду и трусики? Зачем?"
    # Виктория смотрит на нее сверху вниз
    music Groove2_85
    img 15660
    with diss
    victoria "Потому что Я тебе так сказала сделать!"
    victoria "Снимай все с себя!"
    img 15661
    with diss
    victoria "И подружка Моника сделает сейчас тоже самое!"
    victoria "Мне же не придется просить ее об этом дважды?!"
    # поворачивает голову и смотрит на Монику
    music Power_Bots_Loop
    img 15543
    with fade
    mt "!!!"
    mt "Какого черта эта стерва здесь устроила?!"
    img 15534
    with diss
    mt "Недостаточно было всех этих извращений?!"
    mt "Что ей еще нужно?!"
    # Мелани смотрит на Монику, та на нее
    music Master_Disorder
    img 15662
    with fade
    melanie_t "Нужно сделать, как эта мелкая дрянь требует. Чтобы она не сомневалась в моем послушании..."
    melanie_t "После этого вечера нужно будет срочно предпринимать меры против нее."
    melanie_t "Она слишком многое себе позволяет..."
    img 15663
    with diss
    menu:
        "Снять одежду":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15604
            with fade
            mt "Это все зашло слишком далеко!"
            mt "Я, Моника Бакфетт, не собираюсь играть по ее правилам!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            return

    # Мелани встает, снимает платье, бросает его на пол
    # Моника смотрит на Мелани, тоже встает и начинает раздеваться
    # Виктория внимательно наблюдает за ними, осматривая их прелести, самодовольно улыбается
    img 15664
    with fade
    w
    img 15665
    with diss
    w
    img 15666
    with diss
    w
    img 15667
    with diss
    w
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15668
    with fadelong
    w
    img 15669
    with fade
    sound snd_woman_laugh3
    victoria "Я уверена, что вам понравится мой подарок."
    victoria "Я его выбирала специально для вас, мои подружки!"
    # Виктория снимает с себя платье, подходит к столику, берет сумочку и обходит диван с другой стороны
    # стоит спиной к Мелани и Монике
    # те заинтересованно на нее смотрят, переглядываются между собой, им не видно, что там делает Виктория
    # через несколько минут
    # камера на Викторию, она стоит спиной, на ней надеты стринги, голову в полоборота
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    music Master_Disorder
    img 15670
    with fadelong
    sound swish
    w
    img 15671
    with fade
    w
    music Groove2_85
    img 15672
    with diss
    victoria "Подружка Моника садится на диван и смотрит!"
    victoria "Подружка Мелани, ты готова увидеть подарок?"
    # Моника садится на диван
    img 15673
    with fade
    melanie "Да..."
    img 15674
    with diss
    victoria "Что 'да'?"
    victoria "Ты хочешь сказать, что ты хорошая подружка... И будешь рада получить от меня подарок?"
    victoria "Скажи мне это. Я хочу это услышать..."
    img 15675
    with fade
    melanie "Я хорошая подружка и буду рада получить подарок от мисс Виктории."
    # Виктория довольно ухмыляется и поворачивается к Мелани и Монике
    # на ней надет страпон какого-нибудь нелепого цвета (н-р, ярко-розовый)
    # у ее подружек шок !!! даже у Мелани
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    img 15676
    with diss
    w
    sound vjuh4
    img 15700
    with diss
    sound plastinka1b
    w
    music Power_Bots_Loop
    img 15677
    with hpunch
    melanie "!!!"
    img 15678
    with fade
    melanie_t "Страпон?!"
    melanie_t "Она решила подарить мне СТРАПОН?!"
    melanie_t "Мерзкая сучка! Она заставила нас думать, что у нее есть какой-то компромат!"
    img 15679
    with hpunch
    m "!!!"
    img 15680
    with fade
    mt "ЧТО?!"
    mt "Мне пришлось вылизывать ее зад, чтобы она подарила эту ужасную штуку!!!"
    img 15681
    with diss
    mt "!!!"
    mt "Ненавижу!!!"
    # Виктория довольна произведенным эффектом
    music Groove2_85
    img 15682
    with fade
    victoria "Мои хорошие подружки рады подарку?"
    victoria "Подружка Мелани, тебе нравится?"
    # Мелани молчит и смотрит на нее, как на сумасшедшую
    music Power_Bots_Loop
    img 15683
    with diss
    melanie "..."
    music Groove2_85
    img 15684
    with fade
    victoria "Я вижу, что тебе нравится мой подарок, подружка Мелани."
    victoria "Тебе не терпится ощутить его внутри себя. Но ты стесняешься признаться в этом..."
    victoria "Не стоит стесняться, подружка. Скажи мне это!"
    # смотрит на Мелани пристально
    music Power_Bots_Loop
    img 15685
    with diss
    melanie "..."
    img 15686
    with diss
    menu:
        "Сказать, как приказывает Виктория":
            pass
        "Отказаться!":
            music Master_Disorder
            img 15687
            with fade
            melanie_t "Я не позволю это мелкой дряни так унижать меня..."
            melanie_t "Да еще и в присутствии Миссис Бакфетт."
            # Мелани смотрит на Викторию пристально
            img 15688
            with diss
            melanie "Я думаю, Мисс Виктория, что подружки не дарят друг другу такие подарки..."
            # Виктория строго смотрит на нее, подходит к ней, говорит с угрозой
            music Power_Bots_Loop
            img 15689
            with fade
            victoria "ХОРОШИЕ подружки дарят, Мисс Мелани!!!"
            victoria "Хотя... Мы можем перестать быть хорошими подружками прямо сейчас."
            img 15690
            with diss
            victoria "У меня есть другой подарок... Для нашего общего друга...."
            victoria "Он им очень заинтересуется... Мисс Мелани..."
            img 15691
            with diss
            melanie "..."
            # Мелани смотрит на Викторию высокомерно
            music Master_Disorder
            img 15692
            with fade
            melanie_t "Я не просто избавлюсь от нее."
            melanie_t "Сначала я ей отомщу. Заставлю пожалеть о том, что она сейчас делает."
            music Groove2_85
            img 15693
            with diss
            victoria "Итак! Что хорошая подружка сейчас должна мне сказать?"
            pass
    music Master_Disorder
    img 15694
    with fade
    melanie "Мне... Не терпится... Получить от вас подарок, мисс Виктория..."
    img 15695
    with diss
    victoria "Точно не терпится? Ты уверена?"
    img 15696
    with fade
    melanie "Да, мне не терпится..."
    img 15697
    with diss
    victoria "Что именно тебе хочется, м? Скажи мне!"
    music Power_Bots_Loop
    img 15698
    with fade
    melanie "Мне не терпится ощутить ваш подарок внутри меня... мисс Виктория."
    # Виктория смотрит Мелани в глаза и ухмыляется

#label v_Victoria_Melanie_Sex_test:
    label gallery_15703:
    music Groove2_85
    img 15699
    with diss
    victoria "На колени!"
    victoria "Оближи его как следует! Покажи мне, как ты хочешь его!"
    # Мелани медлит, потом опускается на колени, облизывает дилдо
#    sound vjuh3
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 15701
    with fadelong
    w
    img 15702
    with diss
    w

    img 15703
    with diss
    w
    img 15704
    with fade
    victoria "Вот так, да!"
    victoria "Теперь возьми его в рот!"
    victoria "Я хочу, чтобы ты отсосала у меня, мисс Мелани!"
    music Power_Bots_Loop
    img 15705
    with hpunch
    mt "О боже! Какой кошмар!"
    mt "Я не смогу этого сделать!"
    mt "!!!"
    music Loved_Up
    img 15706
    with fade
    w
    ################################
    img black_screen
    with diss
    scene black
    image videov_Victoria_Monica_Melanie_Blowjob1_1 = Movie(play="video/v_Victoria_Monica_Melanie_Blowjob1_1.mkv", fps=30)
    show videov_Victoria_Monica_Melanie_Blowjob1_1
    with fadelong
    wclean
    ################################
    if game.extra == True:
        ################################
        img black_screen
        with diss
        scene black
        image videov_Victoria_Monica_Melanie_Blowjob1_2 = Movie(play="video/v_Victoria_Monica_Melanie_Blowjob1_2.mkv", fps=30)
        show videov_Victoria_Monica_Melanie_Blowjob1_2
        with fadelong
        wclean
        ################################
    # запихивает дилдо ей в рот, Мелани давится, отстраняется, дилдо становится мокрым, с него тянется слюна
    # Моника с ужасом наблюдает
    # Виктория строго говорит Мелани
    ################################
    ################################
    img 15707
    with diss
    w


    img black_screen
    with diss
    scene black
    image videov_Victoria_Monica_Melanie_Blowjob1_4 = Movie(play="video/v_Victoria_Monica_Melanie_Blowjob1_4.mkv", fps=30)
    show videov_Victoria_Monica_Melanie_Blowjob1_4
    with fadelong
    wclean
    ################################
    if game.extra == True:
        img black_screen
        with diss
        scene black
        image videov_Victoria_Monica_Melanie_Blowjob1_3 = Movie(play="video/v_Victoria_Monica_Melanie_Blowjob1_3.mkv", fps=30)
        show videov_Victoria_Monica_Melanie_Blowjob1_3
        with fadelong
        wclean
    img 15708
    with fade
    w
    ################################
    img 15709
    with diss
    w

    music Groove2_85
    img 15710
    with fade
    victoria "Теперь на диван! Встань на колени и покажи мне свой фирменный зад!"
    # та поднимается, убивает Викторию взглядом, но исполняет
    # Виктория встает сзади нее (доги-стайл), шлепает ее по ягодице
    music Power_Bots_Loop
    img 15711
    with diss
    w
    music Master_Disorder
    img 15712
    with fade
    sound highheels_short_walk
    w
    img 15720
    with diss
    w
#    img 15721
#    sound vjuh4
#    pause 0.5
#    sound snd_slap1
#    img 15722
#    with vpunch
#    melanie "Ах!"
#    img 15723
#    with diss
#    w
    ################################
    img v_Victoria_Melanie_Spanking1_1_start
    with fade
    w
    scene black
    sound v_Victoria_Melanie_Spanking1_1
    image videov_Victoria_Melanie_Spanking1_1 = Movie(play="video/v_Victoria_Melanie_Spanking1_1.mkv", fps=30, loop=False, image="/images/Slides/v_Victoria_Melanie_Spanking1_1_end.jpg")
    show videov_Victoria_Melanie_Spanking1_1
#    sound2 vjuh4
    pause 0.5
#    sound2 snd_slap1
    melanie "Ах!"
    music Master_Disorder
    wclean
    #################################

    # у Мелани остается красный отпечаток на попе
    music Master_Disorder
    img 15724
    with fade
    victoria "Какая отличная задница у вас, Мисс Мелани!"
    # шлепает еще раз

    ################################
    if game.extra == True:
        img v_Victoria_Melanie_Spanking1_2_start
        with fade
        w
        scene black
        sound v_Victoria_Melanie_Spanking1_2
        image videov_Victoria_Melanie_Spanking1_2 = Movie(play="video/v_Victoria_Melanie_Spanking1_2.mkv", fps=30, loop=False, image="/images/Slides/v_Victoria_Melanie_Spanking1_2_end.jpg")
        show videov_Victoria_Melanie_Spanking1_2
    #    sound2 vjuh4
        pause 0.5
    #    sound2 snd_slap1
        melanie "Ах!"
        music Master_Disorder
        wclean
        #################################

    music stop
    img black_screen
    with diss
    pause 1.5
#    music Master_Disorder
    sound chpok6
    img 15725
    with hpunch
    w
    label gallery_15728:
    music Loved_Up2
    img black_screen
    with diss
#    music stop
#    stop music
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_2.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_1 = Movie(play="video/v_Victoria_Melanie_Sex1_1.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_1
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    img 15726
    sound vjuh4
    pause 0.5
    sound snd_slap1
    img 15727
    with vpunch
    melanie "Ах!"




    img 15728
    with fade
    victoria "Тебе ведь нравится, подружка Мелани?"
    victoria "Скажи, что хочешь еще! Говори!!!"
    music Power_Bots_Loop
    img 15729
    with diss
    melanie "Мне... Мне нравится..."
########################################
    music Loved_Up2
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_2.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_4 = Movie(play="video/v_Victoria_Melanie_Sex1_4.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_4
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")



########################################
    # Виктория снова шлепает ее, ягодицы у Мелани становятся красными
#    music Master_Disorder
    img 15730
    with diss
    sound vjuh4
    pause 0.5
    sound snd_slap1
    img 15731
    with vpunch
    melanie "Ах!"
    # Виктория направляет дилдо в киску Мелани и вводит его
    # Моника продолжает с ужасом смотреть на эту картину
#    music Power_Bots_Loop
    img 15732
    with fade
    mt "!!!"
    # Виктория поворачивается к Монике, при этом двигается в Мелани, схватив ту за волосы
########################################
    music Loved_Up2
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_2.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_2 = Movie(play="video/v_Victoria_Melanie_Sex1_2.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_2
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
########################################

    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 15733
    with fadelong
    victoria "Подружка Моника, тебе нравится смотреть на нас?"
    victoria "Скажи, что тебе нравится!"
    music Power_Bots_Loop
    img 15734
    with fade
    mt "!!!"
    menu:
        "Сказать Виктории, что мне нравится":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15735
            with fade
            mt "Это отвратительно!"
            mt "Эта Виктория - спятившая извращенка!!!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            return
    m "Д-да... Нравится..."
    img 15735
    with diss
    mt "Это отвратительно!"
    mt "Эта Виктория - спятившая извращенка!!!"
    mt "!!!"
    music Loved_Up
    img 15736
    with fade
    victoria "Что именно тебе нравится?"
    victoria "Ты хочешь оказаться на месте нашей подружки? Скажи мне!"
    music Power_Bots_Loop
    img 15738
    with diss
    mt "Нет-нет! Это так мерзко!!!"
    music Loved_Up
    img 15737
    with fadelong
    m "Д-да..."
    img 15739
    with fade
    victoria "Тогда раздвинь ноги и подготовь свою киску для меня."
    victoria "Покажи мне, как тебе нравится смотреть на меня."
    music Power_Bots_Loop
    img 15681
    with diss
    mt "!!!"
    menu:
        "Раздвинуть ноги":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15738
            with fade
            mt "Это отвратительно!"
            mt "Пошла она к черту!!!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            return
    # Моника подчиняется, раздвигает ноги, смотрит на Викторию
    music Loved_Up
    img 15740
    with fadelong
    victoria "Теперь ласкай свою киску!"
    victoria "Я хочу посмотреть, как ты это делаешь!"
    img 15741
    with diss
    mt "ЧТО!?"
    # Моника опускает руку и прикасается к себе там, начинает водить пальцами по киске
    # Виктория самодовольно ухмыляется
    music Loved_Up2
    img 15742
    with diss
    w

########################################
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_2.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_3 = Movie(play="video/v_Victoria_Melanie_Sex1_3.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_3
    with fadelong
    wclean
    stop music2

    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_7 = Movie(play="video/v_Victoria_Melanie_Sex1_7.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_7
    with fadelong
    wclean
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    stop music2
########################################

#    music Loved_Up
    img 15743
    with diss
    w
    img 15744
    with fade
    victoria "Нравится тебе?"
#    music Power_Bots_Loop
    img 15745
    with diss
    m "Да..."
    # Виктория снова шлепает Мелани по ягодицам и продолжает натягивать ее на свой страпон

########################################
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_5 = Movie(play="video/v_Victoria_Melanie_Sex1_5.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_5
    with fadelong
    wclean
    stop music2
    if game.extra == True:
        stop music2
        play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
        scene black
        image videov_Victoria_Melanie_Sex1_6 = Movie(play="video/v_Victoria_Melanie_Sex1_6.mkv", fps=30)
        show videov_Victoria_Melanie_Sex1_6
        with fadelong
        wclean
        stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
########################################
#    music Loved_Up
    img 15746
    with diss
    sound vjuh3
    w
    img 15747
    with diss
    sound snd_slap1
    pause 0.5
    img 15748
    with hpunch
    melanie "Ах!"
    # Виктория спрашивает у Мелани
    img 15749
    with fade
    victoria "Тебе нравится, подружка Мелани?"
    victoria "У тебя такая киска! Она вся влажная!"
    img 15750
    with diss
    victoria "Я вижу, что тебе нравится..."
    victoria "Подружка Моника, тебе нравится киска нашей подружки Мелани?"
#    music Power_Bots_Loop
    img 15751
    with fade
    m "Нравится..."

########################################
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
    scene black
    image videov_Victoria_Melanie_Sex1_8 = Movie(play="video/v_Victoria_Melanie_Sex1_8.mkv", fps=30)
    show videov_Victoria_Melanie_Sex1_8
    with fadelong
    wclean
    stop music2

    if game.extra == True:
        play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Melanie_Sex1_1.ogg"
        scene black
        image videov_Victoria_Melanie_Sex1_9 = Movie(play="video/v_Victoria_Melanie_Sex1_9.mkv", fps=30)
        show videov_Victoria_Melanie_Sex1_9
        with fadelong
        wclean
        stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

##########################################
    music Loved_Up
    img 15752
    with diss
    victoria "А твоя киска уже стала влажной?"
    victoria "Она готова к тому, чтобы я вошла в нее?"
    music Power_Bots_Loop
    img 15753
    with fade
    mt "!!!"
    mt "Боже! Какой кошмар!!!"
    img 15754
    with diss
    mt "Я не хочу говорить ей это! Какая пошлость!!!"
    mt "!!!"
    music Groove2_85
    img 15755
    with fade
    victoria "Подружка Моника, я не слышу... Скажи мне это!"
    # сама в это время продолжает натягивать Мелани, делает это жестко, держа ее за волосы
    img 15756
    with diss
    m "Да... Готова..."
    img 15757
    with fade
    victoria "К чему ты готова, подружка Моника?"
    music Power_Bots_Loop
    img 15758
    with diss
    m "Готова к тому, чтобы ты... Вошла в меня..."
    music Loved_Up
    img 15759
    with fade
    victoria "Хорошая подружка! Мне нравится, что ты такая послушная."
    # Виктория еще раз шлепает Мелани по попе, у нее она вся красная от шлепков
    sound vjuh3
    img 15726
    with diss
    pause 0.5
    sound snd_slap1
    img 15727
    with hpunch
    melanie "Ах!"
    img 15760
    with diss
    sound chpok6
    victoria "Подружка Мелани тоже хорошая!"
    victoria "Можешь теперь посмотреть на то, как я дарю подарок подружке Монике!"
    # вытаскивает из нее дилдо с хлюпом, отпускает ее волосы
    # Мелани встает, волосы растрепаны, смотрит ненавидящим взглядом на Викторию, но молчит
    music Power_Bots_Loop
    img 15761
    with fade
    melanie "..."
    label gallery_15766:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Master_Disorder
    # садится на диван, берет бокал вина и делает несколько глотков
    # Виктория смотрит на Монику, с ухмылкой подзывает ее к себе пальчиком
    img 15762
    with fade
    w
    img 15763
    with diss
    menu:
        "Встать коленями на диван и нагнуться":
            pass
        "Не делать этого! (пропуск сцены)":
            music Power_Bots_Loop
            img 15681
            with fade
            mt "Это отвратительно!"
            mt "Пошла она к черту!!!"
            mt "!!!"
            m "Я хорошая подружка, но я не буду делать этого!!!"
            # Моника убегает
            music stop
            img black_screen
            with diss
            sound highheels_run2
            return
    mt "У Мелани все получилось... И я смогу. Я сильная."
    mt "!!!"
    mt "Скорее бы эта извращенка ушла отсюда!"
    # Моника подходит к дивану, нерешительно смотрит на Викторию. та пальцем ей показывает на диван
    # Моника встает в ту же позу, что и Мелани. Виктория смотрит на нее сзади, шлепает ее по ягодице
    sound Jump1
    img 15764
    with fade
    w
#    img 15765
#    with diss
#    sound vjuh3
#    pause 0.5
#    sound snd_slap1
#    img 15766
#    with hpunch
    img v_Victoria_Monica_Spanking1_2_start
    with fade
    w
    scene black
    sound v_Victoria_Monica_Spanking1_2
    image videov_Victoria_Monica_Spanking1_2 = Movie(play="video/v_Victoria_Monica_Spanking1_2.mkv", fps=30, loop=False, image="/images/Slides/v_Victoria_Monica_Spanking1_2_end.jpg")
    show videov_Victoria_Monica_Spanking1_2
#    sound2 vjuh4
    pause 0.5
#    sound2 snd_slap1
    m "Ах!"
    music Master_Disorder
    wclean
    img 15767
    with diss
    w
    img 15768
    with diss
    victoria "Нет, подружка Моника!"
    victoria "Я хочу видеть твое лицо!"
    victoria "На спину!"
    # Моника ложится на спину, Виктория задирает ее ноги вверх, открывая себе доступ к ее киске и грубо входит в нее
    # Моника ойкает, гримаса боли
    music stop
    img black_screen
    with diss
    sound vjuh3
    pause 1.0
    music Groove2_85
    img 15769
    with fadelong
    w
    img 15770
    with diss
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    img 15771
    sound chpok6
    with hpunch
    m "Аааа!"


    img 15772
    with fade
    victoria "М-м-м... Как же мне нравится ваша киска, Миссис Бакфетт."
    victoria "Вы ее хорошо подготовили для меня. Вы хорошая подружка, Миссис Бакфетт..."
    # выходит из нее полностью, снова направляет дилдо в киску и опять грубо входит
    # у Моники снова гримаса боли, Виктория смотрит на нее и довольно улыбается

    img 15773
    with diss
    victoria "Тебе нравится чувствовать в себе мой подарок? Скажи, что тебе нравится!"
    music Power_Bots_Loop
    img 15774
    with diss
    m "М-мне... Н-нравится чувствовать в себе... Это..."
    # Виктория снова выходит и входит, Моника ахает
    music Loved_Up2
    img 15775
    with hpunch
    m "Ай!"


    img 15776
    with diss
    victoria "Что именно тебе нравится, подружка Моника?"
    victoria "Я хочу услышать это!"
    img 15777
    with fade
    m "М-мне... Н-нравится как ты... Делаешь это..."

    img 15778
    with diss
    victoria "Что 'ЭТО'?"
    victoria "Монике Бакфетт нравится, что я трахаю ее искусственным членом?"
#    img 15779
#=======================================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_1 = Movie(play="video/v_Victoria_Monica_Sex1_1.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_1
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #=======================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_2 = Movie(play="video/v_Victoria_Monica_Sex1_2.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_2
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #=======================

    music Power_Bots_Loop
    img 15780
    with fade
    m "Д-да-а..."
    mt "Когда же этот кошмар уже закончится?!"
    mt "!!!"
    # Виктория начинает двигаться туда-обратно, удерживая ноги Моники, смотрит на ее лицо
    # Мелани пьет вино и смотрит с каменным лицом на разыгрывающуюся перед ней сцену
    # Виктория поворачивается к Мелани и ухмыляется
    music Loved_Up2
    #========================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_3 = Movie(play="video/v_Victoria_Monica_Sex1_3.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_3
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #======================
    #========================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_4 = Movie(play="video/v_Victoria_Monica_Sex1_4.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_4
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #======================

    if game.extra == True:
        #========================
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        img black_screen
        with diss
        play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
        scene black
        image videov_Victoria_Monica_Sex1_5 = Movie(play="video/v_Victoria_Monica_Sex1_5.mkv", fps=30)
        show videov_Victoria_Monica_Sex1_5
        with fadelong
        wclean
        stop music2
        $ renpy.music.set_volume(1.0, 0.5, channel="music")
        #======================

    img 15781
    with diss
    victoria "Хотелось бы тебе оказаться на моем месте, подружка Мелани?"
    # Мелани вопросительно поднимает бровь, но молчит
    img 15782
    with fade
    melanie "..."

    #========================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_6 = Movie(play="video/v_Victoria_Monica_Sex1_6.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_6
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #======================
    label gallery_15785:
    img 15783
    with diss
    victoria "Возможно, в следующий наш девичник... Я разрешу тебе побыть на моем месте, подружка..."
    victoria "Скажи, что хочешь этого!"
    music Power_Bots_Loop
    img 15784
    with fade
    melanie "..."
    melanie "Да, я хочу этого..." # равнодушно
    # Виктория самодовольно улыбается, смотрит на Мелани, продолжая двигаться в Монике
    # потом поворачивается к Монике, ускоряет движения
    music Loved_up2
    if game.extra == True:
        #========================
        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        img black_screen
        with diss
        play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
        scene black
        image videov_Victoria_Monica_Sex1_7 = Movie(play="video/v_Victoria_Monica_Sex1_7.mkv", fps=30)
        show videov_Victoria_Monica_Sex1_7
        with fadelong
        wclean
        stop music2
        $ renpy.music.set_volume(1.0, 0.5, channel="music")
        #======================

    img 15785
    with diss
    victoria "М-м-м-м... Да-а-а!"
    victoria "Как же охренительно трахать саму Монику Бакфетт!"

    #========================
    $ renpy.music.set_volume(0.5, 0.5, channel="music")
    img black_screen
    with diss
    play music2 "<from " + str(float(rand(1,7))*1.16666667) + " loop 0.0>Sounds/v_Victoria_Monica_Sex1_1.ogg"
    scene black
    image videov_Victoria_Monica_Sex1_8 = Movie(play="video/v_Victoria_Monica_Sex1_8.mkv", fps=30)
    show videov_Victoria_Monica_Sex1_8
    with fadelong
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    #======================

    img 15786
    with fade
    victoria "А-а-а-а"
    victoria "Да-а!!!"
    # еще несколько резких движений и Виктория кончает
    img 15787
    sound woman_moan14
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    victoria "ААААА!!!"
    victoria "Чертовски здорово!!! Да-а-а-а!!!"
    # Виктория отпускает ноги Моники, с хлюпом вытаскивает из нее дилдо
    # садится на диван в расслабленной позе, страпон торчит вверх, весь мокрый
    music stop
    img black_screen
    with diss
    sound chpok6
    pause 2.0
    music Groove2_85
    img 15788
    with fadelong
    w
    img 15789
    with fade
    victoria "М-м-м-м..."
    # Моника садится в закрытую позу, стараясь быть подальше от Виктории
    # Моника и Мелани смотрят на страпон, Виктория ухмыляется, видя это
    img 15790
    with diss
    victoria "Ну что, подружки, вам понравился наш девичник?"
    music Master_Disorder
    img 15791
    with fade
    melanie "Да..."
    music Groove2_85
    img 15792
    with diss
    victoria "Что 'да'? Вам понравилось?"
    victoria "Вы хотели бы повторить наш девичник? Подружки."
    music Master_Disorder
    img 15793
    with fade
    m "Нам понравился девичник..."
    music Power_Bots_Loop
    img 15763
    with diss
    mt "!!!"
    mt "Ни за что!!!"
    mt "НЕНАВИЖУ!!!"
    img 15794
    with diss
    melanie "И мы хотели бы повторить..."
    # Виктория самодовольно смеется
    music Groove2_85
    img 15795
    with fade
    sound snd_woman_laugh3
    victoria "Я оставлю мой подарок здесь..."
    victoria "В следующий наш девичник он мне пригодится..."
    victoria "Хотя, возможно, я принесу своим хорошим подружкам еще какой-нибудь подарок."
    # хихикает
    # спустя несколько минут
    # Виктория стоит возле входной двери, смотрит на своих подружек, ухмыляется, подмигивает им и уходит
    # дверь за Викторией закрывается
    # камера на Монику с Мелани. они сидят одетые, держат в руке бокалы, смотрят друг на друга
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 15800
    with fadelong
    w
    img 15796
    with diss
    w
    music stop
    img black_screen
    with diss
    sound snd_door_open1
    pause 1.0
    sound snd_door_locked1
    pause 1.0
    music Power_Bots_Loop
    img 15797
    with fadelong
    m "Я! НЕНАВИЖУ! ЭТУ СУЧКУ!"
    music Master_Disorder
    img 15798
    with fade
    melanie "Миссис Бакфетт. Думаю, наши интересы относительно Мисс Виктории совпадают."
    melanie "У меня есть идея, как избавиться от нее..."
    melanie "Я могу расчитывать на Вашу помощь?"
    img 15799
    with diss
    m "Да, Мелани... Я готова на все ради этого..."
    # они обе преисполнены мести и готовы "дружить" против Виктории, бокалы сближаются, звук чокающихся бокалов
    # и мокрый страпон на диване
    music stop
    img black_screen
    with diss
    pause 3.0
    return


############ Fitness 1############

label gallery_7739:
    # в раздевалки издалека Стефани и Ребекка обнаженные
    # render
    # Повтор, раздевалка. Стефани, Ребекка, Бетти
    music Groove2_85
    img 7727
    with fade
    w
    img 7729
    w
    img 7728
    w
    img 7730
    with fade
    betty "Гуверантка! Где моя сумка с униформой?"
    img 7731
    betty "Быстро неси ее сюда!"

    img 7732
    betty "Что ты там копаешься?!"
    img 7733
    with fade
    m "Вот Ваша сумка, Миссис Робертс."

    # Бетти уходит в спортивном
    img 7734
    with fade
    betty "Можешь посидеть здесь или понаблюдать за мной."
    img 7735
    m "Спасибо, Миссис Робертс... Я посижу здесь..."
    img 7736
    w
    #fade
    # Девочки обнаженные
    music BossaBossa
    img 7737
    with fadelong
    rebecca "Привет, Моника!"
    img 7738
    stephanie "Моника, когда ты закончишь свое приключение?"
    img 7739
    with fade
    "Ты знаешь..."
    img 7740
    with Dissolve(0.5)
    "Это смешно выглядит со стороны..."
    sound snd_fabric1
    img 7742
    with Dissolve(0.5)
    "Хи-хи!"

    img 7741
    with fade
    rebecca "И когда ты будешь снова заниматься с нами?"
    sound snd_fabric1
    img 7744
    with fade
    w
    img 7745
    with Dissolve(0.5)
    w
    img 7746
    with Dissolve(0.5)
    w
    img 7747
    "Почему ты всю тренировку сидишь здесь?"
    img 7748
    with fade
    m "Привет, девочки!"
    "Я уже скоро закончу свое приключение."
    img 7749
    "Осталось совсем немного!"
    img 7750
    "Скоро я снова буду заниматься с Вами!"
    music Groove2_85
    img 7751
    with fade
    stephanie "Ну хорошо... Как-то это все странно..."
    img 7752
    with fade
    rebecca "Хи-хи"
    img 7753
    with fade
    w
    img 7754
    mt "СУЧКИ!!!"
    return

label gallery_7793:
    #render
    #Сцена занятия йогой.
    #Стефани, Ребекка, Бетти


    #выбор
#    img 7755
    label gallery_7909:
    $ imagesListIdx = 0

    if obj_name == "Stephanie":
        menu:
            "Смотреть на Стефани.":
                pass
            "Нет.":
                return

        music Ready_and_Waiting
        #Stephanie - 7756, 7757, 7765, 7766, 7767, 7768, 7780, 7781, 7782, 7783, 7798, 7799, 7800, 7801, 7802, 7803, 7816, 7817, 7818, 7819, 7824, 7825, 7826, 7827, 7828, 7829,
        # 7842, 7843, 7844, 7845, 7846, 7861, 7862, 7863, 7864, 7875, 7876, 7877, 7878, 7879, 7880, 7892, 7893, 7894, 7895, 7896, 7908, 7909, 7910, 7911
        $ images = [7756, 7757, 7765, 7766, 7767, 7768, 7780, 7781, 7782, 7783, 7798, 7799, 7800, 7801, 7802, 7803, 7816, 7817, 7818, 7819, 7824, 7825, 7826, 7827, 7828, 7829, 7842, 7843, 7844, 7845, 7846, 7861, 7862, 7863, 7864, 7875, 7876, 7877, 7878, 7879, 7880, 7892, 7893, 7894, 7895, 7896, 7908, 7909, 7910, 7911]
        $ imagesAmount = 25
        $ imagesList = random.sample(set(images), imagesAmount)
        $ imagesList.sort()
        label gallery_7909_1:
            if imagesListIdx < imagesAmount:
                $ imageName = str(imagesList[imagesListIdx])
                img imageName
                if imagesListIdx == 0:
                    with fadelong
                w
                $ imagesListIdx += 1
                jump gallery_7909_1

        $ videoList = [1, 2, 3, 4, 5]
        $ videosAmount = 3
        $ videoList = random.sample(set(videoList), videosAmount)
        if 1 in videoList:
            scene black
            image videov_Fitness_Stephanie_1_1 = Movie(play="video/v_Fitness_Stephanie_1_1.mkv", fps=30)
            show videov_Fitness_Stephanie_1_1
            wclean
        if 2 in videoList:
            scene black
            image videov_Fitness_Stephanie_1_2 = Movie(play="video/v_Fitness_Stephanie_1_2.mkv", fps=30)
            show videov_Fitness_Stephanie_1_2
            wclean
        if 3 in videoList:
            scene black
            image videov_Fitness_Stephanie_1_3 = Movie(play="video/v_Fitness_Stephanie_1_3.mkv", fps=30)
            show videov_Fitness_Stephanie_1_3
            wclean
        if 4 in videoList:
            scene black
            image videov_Fitness_Stephanie_1_4 = Movie(play="video/v_Fitness_Stephanie_1_4.mkv", fps=30)
            show videov_Fitness_Stephanie_1_4
            wclean
        if 5 in videoList:
            scene black
            image videov_Fitness_Stephanie_1_5 = Movie(play="video/v_Fitness_Stephanie_1_5.mkv", fps=30)
            show videov_Fitness_Stephanie_1_5
            wclean

        music Loved_Up
        #Инструктор подходит к Стефани
        img 7933
        with fadelong
        fitness_instructor "Стефани, давай я помогу тебе..."
        #Если был секс
        if stephanieFitnessJustSex == True:
            img 7934
            with fade
            stephanie "Муррр..."
            stephanie "Мой тигр хочет помочь мне?..."
            img 7935
            fitness_instructor "Стефани, твой тигр всегда готов придти на помощь!"
            img 7936
            with fade
            stephanie "Муррр..."
            img 7937
            with fade
            w
            img 7938
            with fade
            w

        else:
            #Если секса не было
            music Groove2_85
            img 7933
            with fadelong
            stephanie "Я предпочитаю помощь от кого-то более сообразительного чем ты..."
            fitness_instructor "Стефани, что я могу сделать?"
            img 7939
            with fade
            stephanie "Продолжай быть настойчивым..."
            "Хи-хи..."

    if obj_name == "Rebecca":
        menu:
            "Смотреть на Ребекку.":
                pass
            "Нет.":
                return

        music Ready_and_Waiting
        #Rebecca - 7760, 7761, 7762, 7763, 7764, 7784, 7785, 7786, 7787, 7788, 7789, 7790, 7791, 7792, 7793, 7794, 7795, 7796, 7797, 7820, 7821, 7822, 7823, 7830, 7831, 7832,
        # 7833, 7834, 7847, 7848, 7849, 7850, 7851, 7852, 7858, 7859, 7860, 7881, 7882, 7883, 7884, 7885, 7897, 7898, 7899, 7900, 7901, 7902, 7903, 7904, 7912, 7913, 7914, 7915, 7916
        $ images = [7760, 7761, 7762, 7763, 7764, 7784, 7785, 7786, 7787, 7788, 7789, 7790, 7791, 7792, 7793, 7794, 7795, 7796, 7797, 7820, 7821, 7822, 7823, 7830, 7831, 7832, 7833, 7834, 7847, 7848, 7849, 7850, 7851, 7852, 7858, 7859, 7860, 7881, 7882, 7883, 7884, 7885, 7897, 7898, 7899, 7900, 7901, 7902, 7903, 7904, 7912, 7913, 7914, 7915, 7916]
        $ imagesAmount = 27
        $ imagesList = random.sample(set(images), imagesAmount)
        $ imagesList.sort()
        $ videoFlag = False
        label gallery_7909_2:
            if imagesListIdx < imagesAmount:
                $ imageName = str(imagesList[imagesListIdx])
                if imagesList[imagesListIdx] >= 7832 and videoFlag == False:
                    $ videoFlag = True
                    $ videoList = [1, 3, 4]
                    $ videosAmount = 2
                    $ videoList = random.sample(set(videoList), videosAmount)
                    if 1 in videoList:
                        scene black
                        image videov_Fitness_Rebecca_1_1 = Movie(play="video/v_Fitness_Rebecca_1_1.mkv", fps=30)
                        show videov_Fitness_Rebecca_1_1
                        wclean
                    if 3 in videoList:
                        scene black
                        image videov_Fitness_Rebecca_1_3 = Movie(play="video/v_Fitness_Rebecca_1_3.mkv", fps=30)
                        show videov_Fitness_Rebecca_1_3
                        wclean
                    if 4 in videoList:
                        scene black
                        image videov_Fitness_Rebecca_1_4 = Movie(play="video/v_Fitness_Rebecca_1_4.mkv", fps=30)
                        show videov_Fitness_Rebecca_1_4
                        wclean

                img imageName
                if imagesListIdx == 0:
                    with fadelong
                w
                $ imagesListIdx += 1
                jump gallery_7909_2

        #Инструктор подходит к Ребекке
        music Loved_Up
        img 7931
        with fadelong
        fitness_instructor "Ребекка, давай я помогу тебе..."
        img 7932
        rebecca "Спасибо, не надо..."
    label gallery_7926:
    if obj_name == "Betty":
        menu:
            "Смотреть на Бетти.":
                pass
            "Нет.":
                return
        music Ready_and_Waiting
        #Betty - 7758, 7759, 7769, 7770, 7771, 7772, 7773, 7774, 7775, 7776, 7777, 7778, 7779, 7804, 7805, 7806, 7807, 7808, 7809, 7810, 7811, 7812, 7813, 7814, 7815,
        # 7835, 7836, 7837, 7838, 7839, 7840, 7841, 7853, 7854, 7855, 7856, 7857, 7865, 7866, 7867, 7868, 7869, 7870, 7871, 7872, 7873, 7874, 7886, 7887, 7888, 7889, 7890, 7891,
        # 7905, 7906, 7907, 7917, 7918, 7919, 7920, 7921, 7922, 7923, 7924, 7925, 7926, 7927, 7928, 7929, 7930
        $ images = [7758, 7759, 7769, 7770, 7771, 7772, 7773, 7774, 7775, 7776, 7777, 7778, 7779, 7804, 7805, 7806, 7807, 7808, 7809, 7810, 7811, 7812, 7813, 7814, 7815, 7835, 7836, 7837, 7838, 7839, 7840, 7841, 7853, 7854, 7855, 7856, 7857, 7865, 7866, 7867, 7868, 7869, 7870, 7871, 7872, 7873, 7874, 7886, 7887, 7888, 7889, 7890, 7891, 7905, 7906, 7907, 7917, 7918, 7919, 7920, 7921, 7922, 7923, 7924, 7925, 7926, 7927, 7928, 7929, 7930]
        $ imagesAmount = 35
        $ imagesList = random.sample(set(images), imagesAmount)
        $ imagesList.sort()
        $ videoFlag1 = False
        $ videoFlag2 = False
        label gallery_7926_1:
            if imagesListIdx < imagesAmount:
                $ imageName = str(imagesList[imagesListIdx])
                if imagesList[imagesListIdx] >= 7808 and videoFlag1 == False:
                    $ videoList = [1, 2, 3, 4]
                    $ videosAmount = 2
                    $ videoList = random.sample(set(videoList), videosAmount)
                    $ videoFlag1 = True
                    if 1 in videoList:
                        scene black
                        image videov_Fitness_Betty_1_1 = Movie(play="video/v_Fitness_Betty_1_1.mkv", fps=30)
                        show videov_Fitness_Betty_1_1
                        wclean
                    if 2 in videoList:
                        scene black
                        image videov_Fitness_Betty_1_2 = Movie(play="video/v_Fitness_Betty_1_2.mkv", fps=30)
                        show videov_Fitness_Betty_1_2
                        wclean
                    if 3 in videoList:
                        scene black
                        image videov_Fitness_Betty_1_3 = Movie(play="video/v_Fitness_Betty_1_3.mkv", fps=30)
                        show videov_Fitness_Betty_1_3
                        wclean
                    if 4 in videoList:
                        scene black
                        image videov_Fitness_Betty_1_4 = Movie(play="video/v_Fitness_Betty_1_4.mkv", fps=30)
                        show videov_Fitness_Betty_1_4
                        wclean



                img imageName
                if imagesListIdx == 0:
                    with fadelong
                w
                $ imagesListIdx += 1
                jump gallery_7926_1


        #Инструктор подходит к Бетти
        music Loved_Up
        img 7940
        with fadelong
        fitness_instructor "Бетти, давай я помогу тебе..."
        betty "Конечно!"
        "С удовольствием!"
        img 7941
        with fade
        fitness_instructor "Сосредоточься на себе..."
        img 7942
        betty "Хорошо..."
        img 7943
        fitness_instructor "Давай попробуем еще одно упражнение..."
        betty "Хорошо..."
        #fade
        #если первый раз
        if fitness_gym_betty_first_time_interact_with_trainer == True:
            img 7944
            with fade
            betty "Ой! Мне больно!"
            img 7945
            fitness_instructor "Надо немножечко потерпеть..."
            betty "У меня не получается..."
            img 7946
            fitness_instructor "Бетти, ты прекрасна!"
            "У тебя все получится!"
            img 7947
            betty "Правда?"
            img 7948
            fitness_instructor "Хочешь остаться на частный урок?"
            img 7949
            "У меня есть методики, которые дадут потрясающе быстрый результат..."
            img 7950
            betty "Хочу..."
            music Groove2_85
            img 7951
            with fade
            stephanie "Эй! Прошу прощения!"
            img 7952
            "Мне тут нужна небольшая помощь в упражнениях!"
            img 7953
            with fade
            fitness_instructor "Тогда до встречи после занятий, Бетти..."
            img 7954
            betty "До встречи!"
        else:
            #если последующие разы
            img 7944
            with fade
            fitness_instructor "У тебя уже лучше получается, Бетти!"
            img 7950
            betty "Спасибо!"
            img 7948
            with fade
            fitness_instructor "Останешься сегодня снова на частный урок?"
            img 7949
            fitness_instructor "Тебе надо еще позаниматься..."
            img 7954
            betty "Да, я останусь..."
            img 7953
            with fade
            fitness_instructor "Тогда до встречи после занятий, Бетти..."
            img 7954
            betty "До встречи!"
            #


        if fitness_gym_betty_first_time_interact_with_trainer == False:
            music Ready_and_Waiting
#            if imagesList[imagesListIdx] >= 7808 and videoFlag2 == False:
#                $ videoFlag2 = True
            $ videoList = [5, 6, 7, 8, 9]
            $ videosAmount = 3
            $ videoList = random.sample(set(videoList), videosAmount)
            if 5 in videoList:
                scene black
                image videov_Fitness_Betty_1_5 = Movie(play="video/v_Fitness_Betty_1_5.mkv", fps=30)
                show videov_Fitness_Betty_1_5
                wclean
            if 6 in videoList:
                scene black
                image videov_Fitness_Betty_1_6 = Movie(play="video/v_Fitness_Betty_1_6.mkv", fps=30)
                show videov_Fitness_Betty_1_6
                wclean
            if 7 in videoList:
                scene black
                image videov_Fitness_Betty_1_7 = Movie(play="video/v_Fitness_Betty_1_7.mkv", fps=30)
                show videov_Fitness_Betty_1_7
                wclean
            if 8 in videoList:
                scene black
                image videov_Fitness_Betty_1_8 = Movie(play="video/v_Fitness_Betty_1_8.mkv", fps=30)
                show videov_Fitness_Betty_1_8
                wclean
            if 9 in videoList:
                scene black
                image videov_Fitness_Betty_1_9 = Movie(play="video/v_Fitness_Betty_1_9.mkv", fps=30)
                show videov_Fitness_Betty_1_9
                wclean
            img v_Fitness_Betty_1_5_23
            with fade
            w
            img v_Fitness_Betty_1_6_20
            with fade
            w
    return

label gallery_8649:
    music Groove2_85
    img 8618
    with fade
    w
    img 8619
    with fade
    w
    img 8620
    with fade
    fred "..."
    img 8621
    m "Фред!?"
    "Что ты здесь делаешь?! Нерадивый водитель!"
    "Твое место у машины!"
    img 8622
    fred "О! Миссис Бакфетт!"
    "Все забываю сказать что Вам очень идет эта униформа..."
    img 8623
    m "!!!"
    img 8624
    m "Что тебе здесь надо, Фред?!"
    img 8625
    fred "О! Миссис Бакфетт!"
    "Мне нужен Ваш совет..."
    m "Какой еще совет?!"
    fred "Совет в выборе попы..."
    music Pyro_Flow
    img 8626
    m "Какой еще попы?! Что ты несешь?!"
    "Иди на свое рабочее место, немедленно!"
    music Groove2_85
    img 8627
    with fade
    fred "Одной попы из тех, которые там занимаются сейчас."
    img 8628
    fred "Какую попу Вы бы предпочли, Миссис Бакфетт?"
    music Loved_Up
    img 8629
    with fade
    fred "Бетти..."
    img 8630
    with fade
    fred "Стефани..."
    img 8631
    with fade
    fred "или Ребекку?"
    music Groove2_85
    img 8632
    with fade
    mt "Вот мерзавец!!!"
    "Как он смеет разговаривать со мной о таких вещах!"
    mt "..."
    mt "Хотя..."
    # Моника говорит что бери Бетти, эта дура как раз заслуживает такого болвана как ты.
    # Фред говорит что это будет непрофессионально, т.к. он у нее работает.
    # Моника говорит что добраться до других у него шансов есть.
    # Фред говорит что Моника поможет ему в этом. Моника спрашивает с какой стати.
    # Фред отвечает что Моника что-нибудь придумает, потому что иначе ей придется пожертвовать своей попой.
    # Хватает ее за зад.
    img 8633
    m "Бери Бетти, эта дура как раз заслуживает такого болвана как ты!"
    img 8634
    fred "Миссис Бакфетт, это будет непрофесионально, так как я работаю у нее."
    "А Вы знаете, я профессионал!"
    img 8635
    m "В любом случае, добраться до остальных у тебя шансов нет!"
    img 8636
    fred "У меня есть шансы, Мэм..."
    fred  "Ведь Вы поможете мне в этом..."
    music Pyro_Flow
    img 8637
    with fade
    m "С какой стати я тебе будут помогать в твоих похотливых фантазиях, Фред?!"
    m "Тебе мало что ты уже натворил, подлец?!"
    img 8636
    fred "Вы обязательно что-нибудь придумаете, Миссис Бакфетт..."
    img 8638
    with fade
    m "Я не собираюсь разговаривать с тобой об этом!"
    music Groove2_85
    img 8639
    with fade
    fred "Вы обязательно что-нибудь придумаете, Миссис Бакфетт..."
    img 8640
    fred "Обязательно..."
    img 8641
    fred "В противном случае, Вам придется пожертвовать своей попой для этого..."
    sound Jump2
    img 8642
    with Dissolve(0.5)
    # Хватает ее за зад.
    w
    img 8643
    w
    if monicaBettyPanties == False:
        img 8668
    else:
        if monicaBettyPantiesId == 1:
            img 8669
        if monicaBettyPantiesId == 2:
            img 8670
        if monicaBettyPantiesId == 3:
            #before subd
            img 8671
        if monicaBettyPantiesId == 4:
            img 8672
        if monicaBettyPantiesId == 5:
            img 8673
    with fade
    w
    img 8644
    with fade
    w
    img 8645
    music Power_Bots_Loop
    # Моника поворачивается и, в зависимости от bitchness дает пощечину, либо дает по яйцам ногой.
    menu:
        "Ударить Фреда между ног!" if monicaBitch == True:
            label gallery_8659:
            img 8654
            with Dissolve(0.5)
            m "ЧТО?!?!"
            "ТЫ МЕНЯ РЕШИЛ ЛАПАТЬ?!?"
            "НИЧТОЖЕСТВО!!!"
            sound snd_kick_fred1
            img 8655
            with Dissolve(0.5)
            "ПОЛУЧАЙ!!!"
            img 8656
            with Dissolve(0.5)
            "НА!!!"
            #bodyfall
            #fade
            sound snd_bodyfall
            img 8657
            with fade
            fred "АААААххххх!!!"
            fred "Что Вы сделали, Миссис Бакфетт..."
            fred "Вы применили насилие!"
            img 8658
            "Это же..."
            "Это же... Больно..."
            # Фред падает, если ударили.
            # В это время заходят Стефани и Ребекка
            # Видят Фреда. Моника делает комментарий в его сторону, чтобы он убирался отсюда, болван.
            img 8659
            with fade
            m "Сейчас я воткну каблук в твой рот, мерзавец!"
            img 8660
            with fade
            w
            img 8661
            "Если ты сейчас же не уберешься отсюда!!!"
            if monicaBettyPanties == False:
                img 8662
            else:
                if monicaBettyPantiesId == 1:
                    img 8663
                if monicaBettyPantiesId == 2:
                    img 8664
                if monicaBettyPantiesId == 3:
                    #before subd
                    img 8665
                if monicaBettyPantiesId == 4:
                    img 8666
                if monicaBettyPantiesId == 5:
                    img 8667
            with fade
            "Ты забыл с кем связался! Ничтожество!"
            return

        "Ударить Фреда между ног! (Моника слишком приличная) (disabled)" if monicaBitch == False:
            pass

        "Дать пощечину Фреду." if monicaBitch == False:
            img 8646
            with Dissolve(0.5)
            sound snd_punch_face1
            m "ЧТО?!?!"
            "ТЫ МЕНЯ РЕШИЛ ЛАПАТЬ?!?"
            img 8647
            with Dissolve(0.5)
            sound snd_punch_face2
            #звук пощечины
            "НИЧТОЖЕСТВО!!!"
            #fade
            sound snd_bodyfall
            img 8648
            with fade
            fred "Айй!!"
            fred "Мои очки!"
            fred "Вы применили насилие!"

            # В это время заходят Стефани и Ребекка
            # Видят Фреда. Моника делает комментарий в его сторону, чтобы он убирался отсюда, болван.
            img 8650
            with fade
            w
            img 8649
            m "Следующий удар будет гораздо больнее, мерзавец!"
            img 8651
            "Если ты сейчас же не уберешься отсюда!!!"
            img 8652
            with fade
            "Ты забыл с кем связался! Ничтожество!"

        "Дать пощечину Фреду. (Моника недостаточно приличная) (disabled)" if monicaBitch == True:
            pass
    # Стефани и Ребекки нравятся слова Моники и они разговаривают с ней о том наконец-то увидели прежнюю Монику.
    # А то они уже стали сомневаться по поводу ее слов.
    # Моника говорит чтобы не сомневались.
    # После этого несколько меняется диалог при встрече подруг на фитнесе.

    #Фред убегает
    music stop
    img 8653
    with fade
    sound man_steps
    w
    #fade
    music BossaBossa
    img 8674
    with fade
    stephanie "Вау! Моника!"
    rebecca "Моника! Вот это да!"
    stephanie "Наконец-то мы узнаем нашу Монику!"
    rebecca "Да, Моника, а то мы уже начали сомневаться в тебе!"
    img 8675
    m "Я хочу предупредить Вас, девочки!"
    "Если кто-то будет сомневаться во мне, то последует за тем болваном!"
    img 8676
    stephanie "Нет, Моника! Пожалуйста не надо!"
    rebecca "Мы твои верные подруги, Хи-хи!"
    stephanie "Скорее завершай свое приключение."
    "Нам не терпится все узнать!"
    rebecca "Да, Моника!"
    "Про тебя можно снимать кино!"
    img 8677
    with fade
    mt "Да уж, про меня уже можно снимать кино, это точно..."
    img 8678
    with fade
    stephanie "Пока, Моника!"
    "Чмок!"
    rebecca "Пока, Моника!"
    "Чмок!"
    m "Пока, девочки!"
    return

############ GasStation 1############

label gallery_7074:
    menu:
        "Купить продукты.":
            if money <= 0:
                mt "У меня нет денег на это..."
                return
            call gallery_7074_1()
            return
        "Украсть еду.":
            pass
        "Не делать этого.":
            mt "Я не стану рисковать..."
            return

    #Моника ворует еду
    if monicaEatedLastDay == day:
        mt "Я не так уж голодна."
        "Не стоит лишний раз рисковать..."
        return
    $ store_music()
    music Hidden_Agenda
    #render
    img 7072
    with fade
    w
    img 7073
    w
    img 7074
    mt "Думаю не будет ничего страшного если я украду одно пирожное..."
    img 7075
    w

    #вариации (случайно)
    $ gasStationThiefImages = ["7076", "7077", "7078"]
    $ images = random.sample(set(gasStationThiefImages), 1)
    img images[0]
    "Я заслужила его за все то что пережила..."

    $ restore_music()
    return

label gallery_7074_1:
    if gasStationFoodInited == False:
        $ add_location("gas_station_buy_food", caption=_("Gas Station"), label="gas_station_buy_food", init_label="gas_station_buy_food_init", parent="street_gas_station")
        $ gasStationFoodInited = True
    # Моника заходит
    $ gasStationFoodBought = False
    if cloth == "CasualDress1":
        music Groove2_85
        img 11743
        with fade
        m "Я хочу купить продукты!"
        m "И только попробуй сказать мне что у тебя не работает касса, детка!"
        img 11744
        saleswoman "Мэм, касса работает."
        saleswoman "Пожалуйста, скажите, если я смогу чем-то помочь Вам!"
        music Hidden_Agenda
        return

############ HotelLeGrand 1############

label gallery_20424:
# Моника входит в ресторан:

# Если Моника обещала уволить официантку:
# waitress: Здравствуйте, Мэм! Это... Это ВЫ?!
# Моника отвечает: Да, это я!
# Удивительно что ты все еще работаешь здесь!
# waitress: Мэм... Что Вам будет угодно?! (злое лицо)
    img 20418
    with fadelong
    waitress "Здравствуйте, Мэм!"
    music Groove2_85
    img 20419
    waitress "Это... Это ВЫ?!"
    img 20420
    with fade
    m "Да, это Я!"
    m "Удивительно, что ты все еще работаешь здесь!"
    img 20421
    with diss
    waitress "Мэм... Что Вам будет угодно?!"
# Моника говорит что их ресторан не дотягивает до ее требований, но она, так уж и быть,
# соблаговолит откушать здесь
# waitress: Да, Мэм... Присаживайтесь, пожалуйста, за свободный столик (злое лицо)
    img 20422
    with fade
    m "Этот ресторан не дотягивает до моих требований."
    m "Но я, так уж и быть, соблаговолю откушать здесь."
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Poppers_and_Prosecco
    img 20423
    with fadelong
    waitress "Да, Мэм..."
    waitress "Присаживайтесь, пожалуйста, за свободный столик."
# Моника садится
# waitress: Мэм, Что Вам будет угодно?
    img 20424
    with diss
    waitress "Мэм, Что Вам будет угодно?"
# меню выбора блюд (если нет тикета, то указаны цены, большие):
# блюдо1
# блюдо2
# блодо3
    if check_inventory("legrand_certificate",1) != True:
        $ menu_price = [restaurantForelPrice, restaurantSeaFoodPrice, restaurantLasaniaPrice, restaurantSushiPrice]
        $ menu_price_money = [restaurantForelPrice, restaurantSeaFoodPrice, restaurantLasaniaPrice, restaurantSushiPrice]
    $ choose_var = 0
    menu:
        "Стейк из форели, греческий салат и шампанское.":
            label gallery_20434:
            $ choose_var = 1
            img 20425
            with fade
            m "Стейк из форели, греческий салат и шампанское."
            $ images_list = [20432, 20433, 20434, 20435]
        "Морепродукты и коктейль.":
            label gallery_20438:
            $ choose_var = 2
            img 20425
            with fade
            m "Морепродукты и коктейль."
            $ images_list = [20436, 20437, 20438, 20435]
        "Лазанья с кофе.":
            $ choose_var = 3
            img 20425
            with fade
            m "Лазанья с кофе."
            $ images_list = [20439, 20440, 20441, 20435]
        "Суши и сок.":
            label gallery_20444:
            $ choose_var = 4
            img 20425
            with fade
            m "Суши и сок."
            $ images_list = [20442, 20443, 20444, 20435]
        "Уйти.":
            # Моника уходит
            music Groove2_85
            img 20426
            with fade
            m "В этом дурацком ресторане нет нормальной еды для такой леди как Я!"
            m "Я ухожу!"
            img 20427
            with diss
            waitress "!!!"
            return
# Моника говорит какие блюда выбрала
# Если есть тикет, то она добавляет что оплатит тикетом.
    if check_inventory("legrand_certificate",1) == True:
        sound snd_folder_drop
        img 20428
        with diss
        m "Я оплачу этим сертификатом"
        sound snd_take_paper

# waitress: Да, Мэм. Несколько минут и все будет готово.
# Моника надменно говорит чтобы официантка поторопилась, если не хочет вылететь с работы прямо сейчас.
# waitress морщится в злобе
    img 20429
    with fade
    waitress "Да, Мэм. Несколько минут и все будет готово."
    music Groove2_85
    img 20430
    with diss
    m "Я советую тебе поторопиться, деточка."
    m "Если ты не хочешь вылететь с работы прямо сейчас!"
    img 20431
    with diss
    waitress "!!!"

#    $ restaurantFoodHistory.append(choose_var)
# waitress: Пожалуйста, Мэм.
# Моника кушает и говорит как же вкусно.
# Она отвыкла от такой вкусной пищи, а зря!
# Надо скорее возвращать назад ее прежнюю жизнь.
    #Стейк из форели, греческий салат и шампанское.
    #Морепродукты и коктейль.
    #Лазанья с кофе.
    #Суши и сок.

    #1
    music stop
    img black_screen
    with diss
    pause 1.5
    music Poppers_and_Prosecco
    sound snd_plates
    img images_list[0]
    with fadelong
    waitress "Пожалуйста, Мэм."

    #2
    img images_list[1]
    with diss
    mt "Ммммм... Как вкусно..."
    #3
    img images_list[2]
    with diss
    mt "Я уже отвылка от такой вкусной пищи."
    #4
    img images_list[3]
    with fade
    mt "А зря!"
    mt "Надо скорее возвращать назад мою прежнюю жизнь!"
    music stop
    sound snd_eating
    img black_screen
    with diss
    pause 2.0

    # смотрят
    music Hidden_Agenda
    img 20445
    with fadelong
    w
    #
    $ images_list = random.sample(set([20446, 20447, 20448, 20449]), 1)
    img images_list[0]
    with diss
    mt "Интересно, почему та девушка так смотрит на меня?"



# Моника говорит официантке. Я закончила. Было невкусно!
# waitress: Мэм, прошу прощения, в следующий раз мы постараемся угодить Вам... (злое лицо)
    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 20450
    with fadelong
    m "Я закончила."
    m "Было невкусно!"
    img 20451
    with diss
    waitress "Мэм, прошу прощения."
    waitress "В следующий раз мы постараемся угодить Вам..." # (злое лицо)
    return

############ House 1############

label gallery_5999:
    #Дик, Моника и водитель в машине. День. Моника в платье AfterJail
    #белый экран
    music dream
    img white_screen
    with fade
    dick "Моника..."
    dick "Моника?"
    dick "Моника!"

    #Моника просыпается в машине
    music Power_Bots_Loop
    img 5905
    with Dissolve(1.0)
    m "А? ЧТО?"
    "ГДЕ Я???"

    img 5906
    m "ДИК???"
    "Что ты здесь делаешь?"

    img 5907
    dick "Моника, что значит что я здесь делаю?"
    "Я еду с тобой в ресторан."
    img 5908
    m "В какой ресторан?"

    img 5909
    dick "В самый лучший! В отеле Le Grand!"
    img 5910
    dick "Моника, ты себя хорошо чувствуешь?"
    img 5911
    m "Я... Я не знаю..."

    img 5912
    dick "Моника, мне показалось что ты заснула."
    "Ты не выспалась сегодня?"

    img 5913
    m "Я... Заснула?..."
    "Это был сон???"

    img 5914
    dick "Сон? Дорогая, тебе что-то приснилось?"

    music RnB4_100
    img 5915
    with fade
    m "Мне... Да...."
    img 5916
    with Dissolve(0.5)
    "ЭТО БЫЛ СОН!!!"

    img 5917
    with fade
    fred "Мэм. С вами все в порядке?"

    music Stealth_Groover
    img 5918
    m "Фрэд?!?!"
    "ТЫ?!?!"

    img 5919
    fred "Да, мэм?"

    img 5920
    m "Ты уволен, Фред!!!"
    "Едь скорее на место и вон из машины!"

    img 5921
    dick "Дорогая???"
    img 5922
    fred "Миссис Бакфетт, но за что вы хотите уволить меня?"
    "В чем причина? Что за проступок я совершил?"

    img 5923
    m "Что за проступок, ты спрашиваешь?!?!"
    img 5924
    "Ты..."
    "Ты... Я не скажу что ты сделал..."
    img 5923
    "Но этого более чем достаточно для увольнения!"

    img 5925
    fred "Мэм, но я не понимаю..."

    music Hidden_Agenda
    img 5926
    with fade
    m "Значит это все-таки был сон!"
    "Получается Фред этого не делал?"
    img 5927
    "Но нет! Я не смогу находиться рядом с ним после того что я пережила, даже во сне!"

    music RnB4_100
    img 5928
    with fade
    "Сон!"
    "Ура! Сон!"

    music Stealth_Groover
    img 5929
    with fadelong
    m "Ты уволен, Фред!"

    dick "Дорогая???"

    img 5930
    m "Дик, не надоедай мне!"
    "Ты тоже хорош!"
    "Что ты здесь делаешь? Иди к своей секретарше!"

    img 5931
    "Ходи с ней по ресторанам! Ты не достоин меня!"

    img 5932
    dick "С какой секретаршей, Моника?!"
    "Мне нравишься ТЫ!"

    img 5933
    m "Так, Фред! Быстро останови машину!"
    img 5934
    with fade
    "Мистеру Дику надо выйти!"

    img 5935
    with Dissolve(0.5)
    "А мне надо позвонить!"

    img 5936
    dick "..."

    img 5937
    with fade
    m "Так, черт, где мой телефон?!"
    img 5938
    with Dissolve(0.5)
    "Дик, ты не видел его?"

    img 5939
    music Master_Disorder
    with fadelong
    dick "У тебя его не было, Моника."
    "Я не знаю почему, но ты не взяла его..."

    img 5940
    m "???"

    img 5941
    dick "Более того, ты почему-то не носишь свои украшения."
    img 5942
    music Villainous_Treachery
    with Dissolve(0.5)
    "А где твой браслет? Ты всегда одевала его..."
    img 5942
    show screen vignette_screen
    with Dissolve(1.5)
    w
    img 5943
    with Dissolve(0.5)
    m "..."

    img 5944
    with fade
    dick "И трусики, зачем-то ты их тоже не носишь."
    "Почему, Моника?"

    img 5945
    with fade
    m "..."
    img 5946
    with Dissolve(0.5)
    w
    img 5947
    with Dissolve(0.5)
    w
    img 5948
    with Dissolve(0.5)
    m "!!!"

    img 5949
    with fade
    m "Дик... Я..."
    img 5950
    with Dissolve(0.5)
    "Погоди, я не понимаю..."

    img 5951
    dick "Моника, дорогая!"
    "Не переживай!"
    "Все будет хорошо!"
    img 5952
    "Главное не забудь!"

    img 5953
    with fade
    m "Про что я не должна забыть, Дик?"

    img 5954
    with fadelong
    dick "Про галстук..."

    img 5955
    with Dissolve(0.5)
    m "!!!"

    img 5956
    with fade
    dick "У тебя все будет хорошо, Моника!"
    img 5957
    with Dissolve(0.5)
    "Главное помни про галстук и не разбей мое сердце..."

    img 5958
    with Dissolve(0.5)
    m "!!!"
    hide screen vignette_screen

    #Моника просыпается
    music Power_Bots_Loop
    sound snd_woman_scream1a
    if cloth != "Nude":
        img 5959
    else:
        img 7109
    with fade
    mt "АААААХХХ!!!!"

    mt "ГДЕ Я???"

    img 5960
    mt "Что это... что это за дыра?!?!"
    img 5961
    with fade
    mt "Где Юлия?!"

    mt "..."

    img 5962
    with fade
    mt "Черт! Я все вспомнила!"

    mt "Этого не может быть!!!"

    if cloth != "Nude":
        img 5963
    else:
        img 5964
    "НЕТ!!!"
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    #пауза
    #моника сидит думает на кровати, встает
    music Stealth_Groover
    if cloth != "Nude":
        img 5965
        with fade
    else:
        img 5966
        with fade
    mt "Стоп. Моника, не унывай!"

    "Давай подумаем что у нас есть на данный момент."

    if cloth != "Nude":
        img 5967
    else:
        img 5968
    with fade
    "У меня нет денег, нет документов."
    "Любой полицейский, который меня остановит, {c}может забрать меня к Маркусу{/c} и..."
    img 5969
    "Никаких И! Я не попаду к нему!"

    img 5970
    with fade
    "На самом деле, не все так плохо."
    "У меня есть крыша над головой, правда я не могу забыть какой ценой она досталась мне..."
    img 5971
    with Dissolve(0.5)
    "Этот Фред... Я убью его!"
    "Но это потом... Моника, давай подумаем про то что делать сейчас..."

    if cloth != "Nude":
        img 5972
    else:
        img 5973
    with fade
    "Итак... Меня пустили в свой же дом при условии что {c}я буду убираться в нем{/c}..."

    if cloth != "Nude":
        img 5974
    else:
        img 5975
    "ЗА БЕСПЛАТНО!!!"
    img 5976
    "..." #злой взгляд

    if cloth != "Nude":
        img 5977
    else:
        img 5978
    with fade
    "Но хорошо... Если мне надо пройти через это, то я пройду..."
    "Они не знают кто я такая, поэтому моя гордость не сильно пострадает..."
    "Мне надо всего-лишь притвориться... Ненадолго..."
    "Сделать вид что я убираюсь."
    "В конце концов, эта семейка идиотов что здесь живет - она недалекого ума."
    "Притвориться перед ними и обхитрить их будет пустяковой задачей..."

    img 5979
    "Они глазом не успеют моргнуть, как вылетят отсюда, из этого дома."
    "А я займу свое достойное место здесь..."
    img 5980
    with Dissolve(0.5)
    "Потому что Я - Моника Бакфетт!"
    "А они - никто!"

    img 5981
    with fade
    "Эта Бетти..."
    "Черт... Хоть она и дура, но она следит за мной."
    "Куда бы я здесь ни пошла, она следует за мной по пятам..."
    "Так что крыша у меня над головой есть, но {c}еду мне придется доставать где-то еще...{/c}"

    if cloth != "Nude":
        img 5982
    else:
        img 5983
    with fade
    "Интересно где?..."

    "Может украсть еду у той {c}дуры на заправке{/c}?"
    "Но хочу-ли я воровать?..."

    if cloth != "Nude":
        img 5984
    else:
        img 5985
    with fade
    "Или может спросить еду у того {c}продавца кебабов{/c}?"
    "Я видела как он смотрит на меня..."

    img 5986
    if shawarmaTraderOffended1 == True:
        #
        "Животное, фу!"
    else:
        #
        "Маленькое ничтожество..."

    "Конечно, ему никогда не светит прикоснуться к такой красоте как Я..."

    img 5987
    "Но... это можно использовать, чтобы достать хоть какую-то пищу..."
    "Я никогда в жизни не пробовала такой еды, но сейчас выбирать не приходится."

    if cloth != "Nude":
        img 5988
    else:
        img 5989
    with fade
    "Даже она мне кажется вкусной сейчас, учитывая что я толком ничего не ела уже давно..."
    "И уж тем более не сравнится с теми помоями, что мне пришлось выпрашивать, когда я была в подвале у Маркуса..."

    if cloth != "Nude":
        img 5990
    else:
        img 5991
    with fade
    "И мне надо как-то придумать как вернуть назад свое положение..."

    img 5992
    with Dissolve(0.5)
    "Дик... Да уж, помощник!"
    "Этот подкаблучник теперь влюблен в свою новую секретаршу."

    if cloth != "Nude":
        img 5993
    else:
        img 5994
    "Эту сучку!"
    "Это ее происки по поводу галстука!"
    "Мне надо сходить к нему еще раз, может получится {c}отбить Дика у нее{/c}?"

    if cloth != "Nude":
        img 5996
    else:
        img 5997
    with fade
    "В конце концов, чтобы вернуть назад свои деньги, мне надо сначала отделаться от Маркуса!"
    "А в этом мне может помочь только Дик!"
    "Еще эти его дурацкие слова про галстук!"
    img 5995
    with Dissolve(0.5)
    "Уверена что Дик просто шутил!"
    "Не думаю что мне стоит всерьез воспринимать его слова об этом!"

    if cloth != "Nude":
        img 5998
    else:
        img 5999
    "..."
    "Мне интересно что там происходит в {c}моем офисе{/c}?"
    "Кто-то сменил код на лифте, но может я найду способ попасть туда?"

    if cloth != "Nude":
        img 6000
    else:
        img 6001
    with fade
    "Я хочу посмотреть на того смельчака, который посмел занять мое место!"
    "Да и как это вообще возможно?!"

    img 6002
    with Dissolve(0.5)
    "Я - Моника Бакфетт!"
    "Я - лицо модного журнала!"
    "Невозможно представить журнал без меня!"
    img 6003
    "Это невозможно! И, думаю, они это прекрасно понимают!"
    "Поэтому им не обойтись без меня!"
    "Это шанс для меня вернуть все назад..."

    img 6004
    with fade
    "Стив?..."
    "Нет, к этому слизняку в таком виде идти точно не стоит."
    "Этот мешок с дерьмом сделает все чтобы использовать это небольшое недоразумение в своих целях..."
    "Я его слишком хорошо знаю..."
    if janeTiffanyFirePlanned == True:
        #если была угроза увольнения Джейн и Тиффани
        "Плюс вокруг него вьются эти две проститутки..."
        "Тиффани и Джейн..."
        "После того как я угрожала уволить их, они могут быть пострашнее той секретарши у Дика..."
        "Жалкие ничтожества..."

    img 6005
    with fade
    "И мне вообще стоит поменьше показываться в таком виде перед людьми, которые мне знакомы."
    "Это касается и моих подружек Стефани и Ребекки..."
    "В конце концов, мне придется общаться со всеми ними когда я верну положение в обществе."
    "И вообще, надо бы найти одежду получше чем те тряпки, которые я схватила у той шлюхи..."

    if cloth != "Nude":
        img 6006
    else:
        img 6007
    "Не могу поверить что мне приходится ходить в этом по городу..."
    "Может лучше ходить в униформе Юлии?"
    "Как хорошо что меня никто не узнает в этом!"
    if cloth != "Nude":
        img 6008
    else:
        img 6009
    "Никто даже подумать не может что Моника Бакфетт может ходить по улице в униформе горничной..."
    "Или в одежде проститутки..."
    "Это мне на руку!"

    img 6010
    with Dissolve(0.5)
    "..."
    "Ральф..."
    "Его было бы очень просто отбить у этой провинциальной дуры."
    "После этого выкинуть того маленького недоноска и эту Бетти из дома."
    "А потом выкинуть и Ральфа..."

    img 6011
    "Но Бетти не дает возможности даже взять бутерброд на кухне, что уж говорить о том что она не даст даже близко приблизиться к Ральфу..."

    "..."

    img 6012
    "Барди..."
    "Этот мелкий неудачник даже не заслуживает внимания."
    "Он вертится вокруг как назойливая муха!"
    "Считает что я ему обязана тем что нахожусь здесь!"
    "Наивный дурачок!"
    "Надо как-то избавиться от него..."

    #играет музыка kill bill
    img 6013
    with fadelong
    m "Да, это все небольшое недоразумение..."
    "И, когда я решу его, я поквитаюсь со всеми вами!"
    "Клянусь!"

    #музка гаснет
    music stop
    img 6014
    with fade
    mt "..."
    music Stealth_Groover
    "Итак..."
    "Сейчас, думаю, надо {c}притвориться горничной{/c}."
    "Затем {c}пойти поискать еду{/c}..."
    img 6015
    with fade
    "Думаю мне необязательно все время убираться здесь..."
    "Эта семейка не привыкла к тем стандартам чистоты, которые требовала я от гувернанток."
    img 6016
    with Dissolve(0.5)
    "Но иногда убираться все-же стоит. Это может вызвать доверие у Бетти."
    "Хотя зачем мне ее доверие?"
    "Мне, почему-то, кажется что еду брать она все-равно не разрешит."
    return

label gallery_7079:
    if monicaLastPissedDay == day and monicaLastPissedDayTime == day_time:
        mt "Я уже писала недавно. Я пока не хочу."
        return
    $ store_music()
    music stop
    #Моника писает
    #звук
    #whore
    #вариации (случайно)
    if cloth == "Whore":
        $ toilet_images = ["7079", "7080", "7081", "7082", "7083", "7084", "7085", "7086", "7087"]
        $ images = random.sample(set(toilet_images), 4)

    if cloth == "CasualDress1":
        $ images = ["11724", "11725", "11726"]
        $ images = random.sample(set(images), 3)

    if cloth == "SchoolOutfit1":
        $ images = ["22274", "22275", "22276"]
        $ images = random.sample(set(images), 3)


    #governess
    if cloth == "Governess":
        if monicaUnder != "Nude":
            $ toilet_images = ["7088", "7089", "7090", "7091", "7092", "7093", "7094"]
            $ images = random.sample(set(toilet_images), 3)
        else:
            $ images = ["10568", "10569", "10570"]
            $ images = random.sample(set(images), 3)

    if monicaBettyPanties == True:
        if monicaBettyPantiesId == 1:
            $ images = [7163, 7164, 7165]
        if monicaBettyPantiesId == 2:
            $ images = [7166, 7167, 7168]
        if monicaBettyPantiesId == 3:
            $ images = [7169, 7170, 7171]
        if monicaBettyPantiesId == 4:
            $ images = [7172, 7173, 7174]
        if monicaBettyPantiesId == 5:
            $ images = [7175, 7176, 7177]


    img images[0]
    with fade
    w
    sound snd_piss
    $ rnd = rand(1,4)
    if rnd == 1:
        img images[1]
        mt "Эх... мне надо придумать как вернуть все назад..."
        img images[2]
        mt "Я такая красивая... Как со мной могло случиться такое?"
    if rnd == 2:
    #
        img images[1]
        mt "Этот дом такой большой, а мне приходится прятаться чтобы пописать..."
        img images[2]
        "Но, по крайней мере я здесь, а не на улице..."
    #
    if rnd == 3:
        img images[1]
        w
        img images[2]
        mt "Надеюсь Бетти не заметит как я делаю это..."

    #
    if rnd == 4:
        img images[1]
        w
        img images[2]
        mt "Девушка с такой красотой как у меня не заслуживает того что со мной случилось..."
    $ restore_music()
    return

label gallery_7102:
    if monicaLastShowerDay == day and monicaLastShowerDayTime == day_time:
        mt "Я уже принимала душ недавно..."
        return

    $ store_music()
    music stop
    #Моника принимает душ
    #вариации (случайно)
    #звук душа
    music snd_shower2
    img 7095
    with fade
    w
    if monicaPussyShaved == False:
        $ shower_images = ["7096", "7097", "7098", "7099", "7100", "7101", "7102", "7103", "7104", "7105", "7106", "7107"]
    else:
        $ shower_images = ["7096", "7097", "7098", "10564", "10565", "10566", "7102", "7103", "10567", "7105", "7106", "7107"]

    $ images = random.sample(set(shower_images), 3)

    img images[0]
    w
    img images[1]
    w
    img images[2]
    $ rnd = rand(1,3)
    if rnd == 1:
        mt "Как же хорошо принять душ!"
    if rnd == 2:
        mt "Мне приятно ощущать капельки воды, стекающей по моему телу..."
    if rnd == 3:
        mt "Мое тело божественно!"

    $ restore_music()
    return

label gallery_7159:
    sound snd_fabric1
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10612
            with fade
            $ images = [10613, 10614, 10615, 10616]
            mt "Я... Не привыкла..."
            call showRandomImages(images, 2)
            mt "Ходить без трусиков..."
        else:
            $ images = [7121, 7122]
            img 7120
            with fade
            mt "Это трусики Юлии..."
            "Я уже к ним привыкла..."
            w
            call showRandomImages(images, 2)
    else:
        if monicaBettyPantiesId == 1:
            $ images = [7124, 7125, 7126, 7127, 7128, 7129, 7130]
            img 7123
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4)
        if monicaBettyPantiesId == 2:
            $ images = [7132, 7133, 7134, 7135, 7136]
            img 7131
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 3)
        if monicaBettyPantiesId == 3:
            $ images = [7138, 7139, 7140, 7141, 7142, 7143, 7144]
            img 7137
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4)
        if monicaBettyPantiesId == 4:
            $ images = [7146, 7147, 7148, 7149, 7150, 7151, 7152]
            img 7145
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4)
        if monicaBettyPantiesId == 5:
            $ images = [7154, 7155, 7156, 7157, 7158, 7159, 7160, 7161, 7162]
            img 7153
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 5)
    return

#??
label gallery_7433:
    $ images = [7420, 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431]
    $ imagesList = random.sample(set(images), 4)
    $ amount = 4
    $ bettyHere = False
    if get_active_objects("Betty", scene="floor2") != False:
        $ bettyHere = True
    if cloth == "Governess":
        if monicaBettyPanties == False:
            if monicaUnder == "Nude":
                if bettyHere == True:
                    img 10609
                    w
                img 10610
                call showRandomImages(images, 4, True)
                img 10611
                w

            else:
                if bettyHere == True:
                    img 7419
                    w
                img 7421
                call showRandomImages(images, 4, True)
                img 7432
                w
        else:
            if monicaBettyPantiesId == 1:
                if bettyHere == True:
                    img 7436
                    w
                img 7437
                call showRandomImages(images, 4)
                img 7437
                w
            if monicaBettyPantiesId == 2:
                if bettyHere == True:
                    img 7440
                    w
                img 7441
                call showRandomImages(images, 4)
                img 7441
                w
            if monicaBettyPantiesId == 3:
                if bettyHere == True:
                    img 7444
                    w
                img 7445
                w
                img 7446
                w
                call showRandomImages(images, 4)
                img 7447
                w
            if monicaBettyPantiesId == 4:
                if bettyHere == True:
                    img 7448
                    w
                img 7449
                call showRandomImages(images, 4)
                img 7449
                w
            if monicaBettyPantiesId == 5:
                if bettyHere == True:
                    img 7452
                    w
                img 7453
                w
                img 7454
                w
                call showRandomImages(images, 4)
                img 7455
                w
    call gallery_7433_1()
    return

label gallery_7433_1:
    # Моника закончила тереть пятно
    # Пикчи того как Моника трет пятно
    # Общие 7420, 7422, 7423, 7424, 7425, 7426, 7427, 7428, 7429, 7430, 7431

    # Если Governess Pants (Betty 7419), 7421, 7432, 7433, 7434, 7435
    # Если Governess Pants Betty_1 (Betty 7436) 7437, 7438, 7439
    # Если Governess Pants Betty_2 (Betty 7440) 7441, 7442, 7443
    # Если Governess Pants Betty_3 (Betty 7444) 7445, 7446, 7447
    # Если Governess Pants Betty_4 (Betty 7448) 7449, 7450, 7451
    # Если Governess Pants Betty_5 (Betty 7452) 7453, 7454, 7455


    mt "Все! Я устала тереть это пятно!"
    return

label gallery_7578:
    #render
    #Барди сидит с журналом на кровати Моники в спальне в подвале
    #Возвращение в спальню на следующий день
    #Если Моника одета в гувернантку, иначе Барди нет
    sound highheels_short_walk
    $ store_music()
    music Power_Bots_Loop high
    img 7516
    with fadelong
    m "Что это у тебя в руках???"
    img 7517
    bardie "Смотри что я нашел у тебя!"
    "Это правда ты???"
    "Ты Моника Бакфетт???"
    menu:
        "Да, это Я. Я - миссис Бакфетт!":
            pass
    music Groove2_85 high
    img 7518
    with fade
    "Да, это Я. Я - миссис Бакфетт!"
    "Но это не твое дело!"
    img 7519
    bardie "Но ведь Моника Бакфетт - это глава компании где работает мой отец!"
    bardie "Как это можешь быть ты?"
    "Гувернантка???"
    music Hidden_Agenda high
    img 7520
    m "У меня небольшие сложности... Временные..."
    "Это не твое дело..."
    img 7521
    bardie "Насколько я знаю, этот дом тоже принадлежал тебе?"
    m "Да, это мой дом!"
    music Groove2_85 high
    "Вы поселились в нем незаконно! И я восстановлю справедливость!"
    img 7522
    m "Можешь не сомневаться, Барди..." #смотрит прищурившись
    img 7523
    bardie "Ой! Я боюсь тебя!"
    img 7524
    m "Да, тебе стоило бы меня бояться, учитывая мои возможности!"
    img 7525
    bardie "Почему ты сразу не сказала кто ты?"
    img 7526
    m "Вашей семье пока не стоит про это знать..."
    "И я бы тебе советовала держать рот на замке!"
    img 7527
    with fade
    "Ты ведь послушный мальчик?"
    img 7528
    bardie "..." #Испуганно смотрит
    music Pyro_Flow high
    img 7529
    m "Отвечай!" #Надменно
    img 7530
    bardie "Да, Миссис Бакфетт..."
    "Я никому не скажу про вас..."
    music Groove2_85 high
    img 7531
    m "И не называй меня по фамилии, еще не время..."
    bardie "Хорошо, Ми... Миссис Моника..."
    img 7532
    m "Можешь пока просто Моника, но только пока...!!!"
    img 7533
    bardie "Хорошо, Моника. Я никому не скажу кто ты."
    img 7534
    with fade
    m "Вот и отлично!"
    m "Я надеюсь наше маленькое недоразумение закончено?"
    "Этот дурацкий разговор в полиции и твои глупые просьбы..."
    img 7535
    "Ты можешь быть свободен, я хочу отдохнуть!"
    "ИДИ!"
    music Marty_Gots_a_Plan high
    img 7536
    with fade
    bardie "Хм... Моника!"
    m "Чего тебе еще? Ты разве не понял?"
    "Ты можешь идти!"
    img 7537
    bardie "Моника, но ты так и не показала трусики мне!"
    music Pyro_Flow high
    img 7538
    with fade
    m "ЧТО?!?! ТЫ СНОВА ЗА СВОЕ?!?"
    m "Ты разве не понял кто я такая?!"
    "Я - Моника Бакфетт!"
    "И ты не имеешь права говорить мне подобное!!!"
    img 7539
    bardie "Но ты обещала!"
    "Ты дала слово!"
    img 7540
    m "Я не считаю словом то что сказала такому малявке как ты!"
    music Power_Bots_Loop high
    bardie "ЧТО?!?!"
    "ТЫ СНОВА ОБЗЫВАЕШЬ МЕНЯ МАЛЯВКОЙ?!?"
    img 7541
    bardie "Сейчас же покажи свои трусики, иначе я иду к Мистеру Маркусу!"
    img 7542
    with fade
    m "Ты что, правда не понял кто Я?!"
    "Как ты смеешь от меня требовать это?!"
    img 7543
    bardie "Ну и что! Так даже интереснее!"
    "Моя игрушка - это девушка с обложки журнала!"
    "У меня даже захватывает дух! Я даже представить не мог!"
    img 7544
    "Я заберу этот журнал к себе и буду дрочить на него по вечерам!"
    img 7545
    m "ЧТО?!?! Дрочить на него?!"
    "Это мой журнал! Мой!"
    img 7546
    with fade
    bardie "Это теперь мой журнал, как и ты теперь моя!"
    "Ты моя игрушка!"
    img 7547
    "Быстро поворачивайся задом и нагнись!"
    img 7548
    "Я собираюсь, наконец-то, рассмотреть твои трусики как следует!"
    img 7549
    with fade
    m "Я не буду делать этого!!!" #Моника переживает
    img 7550
    bardie "Тогда я иду к Мистеру Маркусу! Прямо сейчас!"
    music Hidden_Agenda high
    img 7551
    with fadelong
    mt "Дьявол!!! Этот Барди!!!"
    "Это очень рискованно! Если он сообщит Маркусу обо мне, то мне конец!"
    img 7552
    "..."
    "Может быть правда проще показать ему мои трусики, чтобы он, наконец-то, отстал от меня?"
    "Все-равно он и так уже их видел!"
    "Он использует каждую возможность, чтобы заглянуть мне под юбку!"
    menu:
        "Хорошо, я покажу тебе, но только один раз!":
            pass
    img 7553
    with fade
    m "Хорошо, я покажу тебе, но только один раз!"
    img 7554
    bardie "Ты будешь показывать мне трусики каждый раз, когда я захочу этого!"
    music Pyro_Flow high
    img 7555
    with fade
    mt "!!!" #Моника злая
    music Groove2_85 high
    img 7556
    bardie "Теперь нагибайся, я теряю терпение!"
    menu:
        "Повернуться спиной и нагнуться...":
            pass
    music Loved_up high
    img 7557
    with fade
    w
    img 7558
    w
    img 7559
    w
    img 7560
    with fade
    w
    img 7561
    w
    img 7562
    w
    img 7563
    w
    img 7564
    w
    img 7565
    with fade
    w
    img 7566 #нагнулась
    with fade
    w
    img 7567
    with fade
    w
    img 7568
    w
    img 7569
    w
    img 7570
    w
    img 7571
    w
    img 7572
    w
    img 7573
    w
    img 7574
    with fade
    w
    img 7575
    w
    img 7576
    w
    img 7584
    w
    img 7577
    w
    img 7578
    with fade
    bardie "Отличный вид, хе-хе!"
    img 7579
    w
    img 7580
    w

    # Моника нагибается, Барди подымает юбку и рассматривает трусики
    img 7581
    w
    img 7582
    "Пожалуй, я оставлю эту гувернантку себе!"
    img 7583
    mt "Маленький ублюдок!"
    music Groove2_85 high
    img 7585
    with fade
    bardie "Пока достаточно! Ты можешь идти работать!"
    img 7586
    with fade
    bardie "Я буду регулярно проверять у тебя под юбкой"
    img 7587
    "Беду следить чтобы там был порядок!"
    img 7588
    w
    img 7589
    mt "!!!"
    # Барди исчезает
    $ restore_music()
    return

label gallery_7635:
    #render+
    #когда Моника убирает у Барди в комнате
    $ store_music()
    music Marty_Gots_a_Plan high
    img 6038
    w
    img 6040
    w
    img 7618
    sound Jump2
    bardie "Моника! Убирайся в комнате хозяина как следует!"
    img 7617
    mt "!!!"
    m "Да, Барди... Я стараюсь убираться хорошо..."
#    bardie "И подними юбку! Я хочу проверить твои трусики!"
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10555
            w
            img 10556
            w
            img 10557
            w
        else:
            #Governess Pants - 7619, 7620, 7621
            img 7619
            w
            img 7620
            w
            img 7621
            w
    else:
        if monicaBettyPantiesId == 1:
            #Betty1
            img 7622
            w
            img 7623
            w
            img 7624
            w
        if monicaBettyPantiesId == 2:
            #Betty2
            img 7625
            w
            img 7626
            w
            img 7627
            w
        if monicaBettyPantiesId == 3:
            #Betty3
            img 7628
            w
            img 7629
            w
            img 7630
            w
        if monicaBettyPantiesId == 4:
            #Betty4
            img 7631
            w
            img 7632
            w
            img 7633
            w
        if monicaBettyPantiesId == 5:
            #Betty5
            img 7634
            w
            img 7635
            w
            img 7636
            w
    if monicaMustWearBettyPanties == True and (monicaBettyPantiesId != bettyPantiesLog[1] or monicaBettyPanties == False):
        music Groove2_85 high
        bardie "Ты одела не те трусики! Бетти была вчера в других!"
        mt "!!!"
    else:
        if monicaMustWearBettyPanties == True:
            bardie "Ты одела правильные трусики! Хорошая гувернантка!"
            mt "!!!"
        if monicaMustNotWearPanties == True:
            if monicaUnder != "Nude":
                call gallery_7635_1()# замечание
            else:
                bardie "Молодец, гувернантка. Ты соблюдаешь правила дома."
#    music Pyro_Flow
#    music Marty_Gots_a_Plan high
    $ restore_music()
#    call EP22_Quests_Bardie4_check_progress()
    return

label gallery_7635_1:
# Барди делает замечания когда видит что Моника в трусиках.
    bardie "Моника, ты знаешь правила дома!"
    bardie "Почему на тебе надеты трусики?!"
    mt "!!!"
    bardie "Если ты будешь нарушать правила, то тебя будет ждать наказание!"
    return

label gallery_7655:
    #render+
    #когда Моника убирает в bedroom_second
    $ store_music()
    music Marty_Gots_a_Plan high
    img 6045
    w
    img 6046
    w
    img 6047
    w
    img 7637
    sound Jump2
    w
    img 7638
    bardie "Моника! Покажи трусики!"
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            #Nude
            img 10558
            w
            img 10559
            w
            img 10560
            w
        else:
            #Governess Pants
            img 7639
            w
            img 7640
            w
            img 7641
            w
    else:
        if monicaBettyPantiesId == 1:
            #Betty1
            img 7642
            w
            img 7643
            w
            img 7644
            w
        if monicaBettyPantiesId == 2:
            #Betty2
            img 7645
            w
            img 7646
            w
            img 7647
            w
        if monicaBettyPantiesId == 3:
            #Betty3
            img 7648
            w
            img 7649
            w
            img 7650
            w
        if monicaBettyPantiesId == 4:
            #Betty4
            img 7651
            w
            img 7652
            w
            img 7653
            w
        if monicaBettyPantiesId == 5:
            #Betty5
            img 7654
            w
            img 7655
            w
            img 7656
            w


    if monicaMustWearBettyPanties == True and (monicaBettyPantiesId != bettyPantiesLog[1] or monicaBettyPanties == False):
        music Groove2_85 high
        img 7657
        bardie "Ты одела не те трусики! Бетти была вчера в других!"
        mt "!!!"
    else:
        if monicaMustWearBettyPanties == True:
            bardie "Ты одела правильные трусики! Хорошая гувернантка!"
            mt "!!!"
        if monicaMustNotWearPanties == True:
            if monicaUnder != "Nude":
                call gallery_7635_1() # замечание
            else:
                bardie "Молодец, гувернантка. Ты соблюдаешь правила дома."
#    music Pyro_Flow high
#    $ add_corruption(bardieCleaning2UpskirtCorruption, "bardie_monica_upskirt_corruption_day_" + str(day))
    $ restore_music()
#    call EP22_Quests_Bardie4_check_progress()
    return

label gallery_7675:
    #render+
    #иногда Барди появляется в комнате, где убирается Моника
    #комнаты floor1 (если нет Ральфа)
    $ store_music()
    music Marty_Gots_a_Plan high
#    $ add_corruption(bardieCleaningUpskirtTryCorruption, "bardie_monica_upskirt_corruption_day_" + str(day))
    img 6030
    w
    img 6031
    w
    img 6032
    w
    #Governess Pants
#    bardie "Моника! Покажи трусики!"
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10561
            sound Jump2
            w
            img 10562
            w
            img 10563
            w
        else:
            img 7659
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7660
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7661
            w
    else:
        if monicaBettyPantiesId == 1:
            #Betty1
            img 7662
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7663
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7664
        if monicaBettyPantiesId == 2:
            #Betty2
            img 7665
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7666
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7667
            w
        if monicaBettyPantiesId == 3:
            #Betty3
            img 7668
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7669
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7670
            w
        if monicaBettyPantiesId == 4:
            #Betty4
            img 7671
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7672
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7673
            w
        if monicaBettyPantiesId == 5:
            #Betty5
            img 7674
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7675
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7676
            w
            img 7677
            w

    img 7658
    mt "!!!"
    if monicaMustWearBettyPanties == True and (monicaBettyPantiesId != bettyPantiesLog[1] or monicaBettyPanties == False):
        # Если Моника одела не те трусики
        music Groove2_85 high
        bardie "Ты одела не те трусики! Бетти была вчера в других!"
        mt "!!!"
    else:
        if monicaMustWearBettyPanties == True:
            bardie "Ты одела правильные трусики! Хорошая гувернантка!"
            mt "!!!"
        if monicaMustNotWearPanties == True:
            if monicaUnder != "Nude":
                call gallery_7635_1() # замечание
            else:
                bardie "Молодец, гувернантка. Ты соблюдаешь правила дома."
#    music Pyro_Flow high
    # Моника
    $ restore_music()
#    call EP22_Quests_Bardie4_check_progress()
    return

label gallery_8683:
    $ store_music()
    music Groove2_85 high
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10554
        else:
            img 8683
    else:
        if monicaBettyPantiesId == 1:
            img 8684
        if monicaBettyPantiesId == 2:
            img 8685
        if monicaBettyPantiesId == 3:
            img 8686
        if monicaBettyPantiesId == 4:
            img 8687
        if monicaBettyPantiesId == 5:
            img 8688
    with fade
    w
    if monicaUnder == "Nude":
        fred "Вау! Какой вид, Миссис Бакфетт!"

    img 8689
    m "Фред! Что ты шляешься здесь?!"
    "Проваливай отсюда, пока не получил по зубам!"
    fred "Мэм! Я просто прогуливаюсь!"
    "Вы знаете, Я профессионал."
    img 8690
    with fade
    "И ищу вдруг где-то надо применить мой профессионализм!"
    img 8691
    m "Это точно не здесь, Фред!"
    if monicaUnder == "Nude":
        m "И не вздумай приближаться ко мне, мерзавец!"
    $ restore_music()
    return

label gallery_10322:
    # Спальня в подвале
# Барди говорит что Моника нерадивая гувернантка и заслужила наказание.
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Groove2_85
    img 10270
    with fadelong
    m "Что тебе снова надо, Барди?!"
    music Power_Bots_Loop
    img 10271
    bardie "Моника, ты нерадивая гувернантка."
    #governess
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            img 10272
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 10273
        if monicaBettyPantiesId == 2:
            img 10274
        if monicaBettyPantiesId == 3:
            img 10275
        if monicaBettyPantiesId == 4:
            img 10276
        if monicaBettyPantiesId == 5:
            img 10277
    #
    sound Jump1
    with diss
    bardie "Ты не соблюдаешь правила дома."
    img 10278
    bardie "И ты заслужила наказание!"
# Первый раз:
# Моника кривится и говорит какое еще наказание?!
    img 10279
    with fade
    m "Какое еще наказание?!"

# Барди садится на кровать и говорит чтобы сняла запрещенные трусики,
#подняла попу вверх и легла к нему на колени.
    img 10280
    with fade
    bardie "Сними запрещенные в этом доме трусики!"
    img 10281
    with diss
    bardie "Ложись ко мне на коленки и подними попу вверх!"
# Выбор:
# Моника говорит что не собирается этого делать! С нее хватит!
# Она уйдет из этого дурацкого дома!
# Моника не собирается терпеть такие унижения из-за какой-то крыши над головой!
# Барди говорит что пусть только попробует уйти! Тогда он сразу пожалуется Мистеру Маркусу на нее!
# Моника в ярости!
# Вот малявка! Он продолжает шантажировать меня!
# Барди говорит чтобы не испытывала его терпения и быстро легла для получения наказания!
    img 10282
    with fade
    menu:
        "Я не собираюсь этого делать! С меня хватит!":
            music Pyro_Flow
            img 10283
            with fade
            m "Я не собираюсь этого делать! С меня хватит!"
            img 10284
            with fade
            m "Я уйду из этого дурацкого дома!"
            m "Я не буду терпеть такие унижения из-за какой-то крыши над головой!"
            music Power_Bots_Loop
            img 10285
            with diss
            bardie "Только попробуй уйти!"
            bardie "Я сразу пожалуюсь Мистеру Маркусу на тебя!"
            mt "!!!"
            img 10286
            with fade
            mt "Вот малявка! Он продолжает шантажировать меня!"
            img 10287
            bardie "Не испытывай моего терпения и быстро ложись для получения наказания!"
            img 10288
            menu:
                "Послушаться хозяина дома...":
                    pass
                "Убежать...":
                    return
        "Послушаться хозяина дома...":
            pass

# Моника снимает трусики и ложится к Барди на коленки
    music Groove2_85
    img 10289
    with fade
    w
    img 10290
    with fade
    w
    img 10291
    with fade
    w
    sound snd_fabric1
    if monicaBettyPanties == False:
        if monicaUnder != "Nude":
            #governess
            img 10292
            with diss
            w
            img 10293
            with diss
            w
    else:
        if monicaBettyPantiesId == 1:
            #betty
            img 10295
            with diss
            w
            img 10294
            with diss
            w
            img 10305
            with diss
            w
    #
        if monicaBettyPantiesId == 2:
            img 10296
            with diss
            w
            img 10297
            with diss
            w
            img 10306
            with diss
            w
    #
        if monicaBettyPantiesId == 3:
            img 10299
            with diss
            w
            img 10298
            with diss
            w
            img 10307
            with diss
            w
    #
        if monicaBettyPantiesId == 4:
            img 10300
            with diss
            w
            img 10301
            with diss
            w
            img 10308
            with diss
            w
    #
        if monicaBettyPantiesId == 5:
            img 10303
            with diss
            w
            img 10302
            with diss
            w
            img 10304
            with diss
            w

    #
    img 10309
    with fade
    w
    img 10310
    with fade
    w
    img 10311
    with fade
    w
    img 10312
    with fade
    w
    img 10313
    with fade
    w
    img 10314
    with fade
    w
    img 10315
    with fade
    w
    img 10316
    with fade
    w
    img 10317
    with fade
    w
    img 10318
    with fade
    w
    img 10319
    with fade
    w


# Барди шлепает Монику по попе, со следами.

label gallery_10322_1:
    # Барди шлепает Монику

    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_1 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_1.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_1
    wclean
    stop music

    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_2 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_2.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_2
    bardie "Получай!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_3 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_3.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_3
    bardie "Получай!"
    bardie "Нерадивая гувернантка!"
    bardie "Я научу тебя соблюдать правила дома!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_4 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_4.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_5 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_5.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_6 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_6.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_6
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_7 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_7.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_7
    bardie "Ну что, ты поняла? Ты будешь слушаться хозяина?"
    wclean
    stop music

    music Power_Bots_Loop
    menu:
        "Отпусти меня немедленно, малявка!":
            img 10320
            with fade
            m "Отпусти меня немедленно, малявка!"
            jump gallery_10322_1
        "Я поняла! Я буду слушаться хозяина!":
            pass


    music Groove2_85
    img 10321
    with fade
    m "Я поняла! Я буду слушаться хозяина!"
    img 10322
    with fade
    m "Я обещаю! Я буду себя хорошо вести!"
    img 10323
    with fade
    bardie "Так-то лучше!"
    img 10324
    with diss
    bardie "Если будешь себя снова плохо вести, получишь еще!"
    img 10325
    with fade
    bardie "Гувернантка, можешь продолжать работать..."
    bardie "Ты мне пока не нужна."

    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Pyro_Flow
    img 10326
    with fadelong
    mt "Не могу поверить!"
    mt "Этот малявка отшлепал меня словно я маленький ребенок!"

    #Если повтор
    if bardieMonicaPunishmentCount > 1:
        img 10327
        with fade
        mt "И уже не первый раз!!!"
        #
        img 10327
        mt "В моем же доме!"
        mt "Отшлепали! Меня!!!"
        mt "Монику Бакфетт!!!"
        #

    img 10328
    with fade
    mt "У меня попа горит!"
    img 10329
    with diss
    mt "Что этот Барди себе позволяет?!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 10330
    with fadelong
    mt "Как унизительно!"
    mt "Мне надо как-то избавиться от него!"

    return

label gallery_10615:
    sound snd_fabric1
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10612
            with fade
            $ images = [10613, 10614, 10615, 10616]
            mt "Я... Не привыкла..."
            call showRandomImages(images, 2)
            mt "Ходить без трусиков..."
        else:
            $ images = [7121, 7122]
            img 7120
            with fade
            mt "Это трусики Юлии..."
            "Я уже к ним привыкла..."
            w
            call showRandomImages(images, 2)
    else:
        if monicaBettyPantiesId == 1:
            $ images = [7124, 7125, 7126, 7127, 7128, 7129, 7130]
            img 7123
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4)
        if monicaBettyPantiesId == 2:
            $ images = [7132, 7133, 7134, 7135, 7136]
            img 7131
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 3)
        if monicaBettyPantiesId == 3:
            $ images = [7138, 7139, 7140, 7141, 7142, 7143, 7144]
            img 7137
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4)
        if monicaBettyPantiesId == 4:
            $ images = [7146, 7147, 7148, 7149, 7150, 7151, 7152]
            img 7145
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 4)
        if monicaBettyPantiesId == 5:
            $ images = [7154, 7155, 7156, 7157, 7158, 7159, 7160, 7161, 7162]
            img 7153
            with fade
            mt "Это трусики Бетти..."
            call showRandomImages(images, 5)

    return

label gallery_10555:
    #render+
    #когда Моника убирает у Барди в комнате
    $ store_music()
    music Marty_Gots_a_Plan high
    img 6038
    w
    img 6040
    w
    img 7618
    sound Jump2
    bardie "Моника! Убирайся в комнате хозяина как следует!"
    img 7617
    mt "!!!"
    m "Да, Барди... Я стараюсь убираться хорошо..."
#    bardie "И подними юбку! Я хочу проверить твои трусики!"
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10555
            w
            img 10556
            w
            img 10557
            w
        else:
            #Governess Pants - 7619, 7620, 7621
            img 7619
            w
            img 7620
            w
            img 7621
            w
    else:
        if monicaBettyPantiesId == 1:
            #Betty1
            img 7622
            w
            img 7623
            w
            img 7624
            w
        if monicaBettyPantiesId == 2:
            #Betty2
            img 7625
            w
            img 7626
            w
            img 7627
            w
        if monicaBettyPantiesId == 3:
            #Betty3
            img 7628
            w
            img 7629
            w
            img 7630
            w
        if monicaBettyPantiesId == 4:
            #Betty4
            img 7631
            w
            img 7632
            w
            img 7633
            w
        if monicaBettyPantiesId == 5:
            #Betty5
            img 7634
            w
            img 7635
            w
            img 7636
            w
    if monicaMustWearBettyPanties == True and (monicaBettyPantiesId != bettyPantiesLog[1] or monicaBettyPanties == False):
        music Groove2_85 high
        bardie "Ты одела не те трусики! Бетти была вчера в других!"
        mt "!!!"
    else:
        if monicaMustWearBettyPanties == True:
            bardie "Ты одела правильные трусики! Хорошая гувернантка!"
            mt "!!!"
        if monicaMustNotWearPanties == True:
            if monicaUnder != "Nude":
                call gallery_7635_1() # замечание
            else:
                bardie "Молодец, гувернантка. Ты соблюдаешь правила дома."
#    music Pyro_Flow
#    music Marty_Gots_a_Plan high
    $ restore_music()
#    call EP22_Quests_Bardie4_check_progress()
    return

label gallery_10559:
    #render+
    #когда Моника убирает в bedroom_second
    $ store_music()
    music Marty_Gots_a_Plan high
    img 6045
    w
    img 6046
    w
    img 6047
    w
    img 7637
    sound Jump2
    w
    img 7638
    bardie "Моника! Покажи трусики!"
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            #Nude
            img 10558
            w
            img 10559
            w
            img 10560
            w
        else:
            #Governess Pants
            img 7639
            w
            img 7640
            w
            img 7641
            w
    else:
        if monicaBettyPantiesId == 1:
            #Betty1
            img 7642
            w
            img 7643
            w
            img 7644
            w
        if monicaBettyPantiesId == 2:
            #Betty2
            img 7645
            w
            img 7646
            w
            img 7647
            w
        if monicaBettyPantiesId == 3:
            #Betty3
            img 7648
            w
            img 7649
            w
            img 7650
            w
        if monicaBettyPantiesId == 4:
            #Betty4
            img 7651
            w
            img 7652
            w
            img 7653
            w
        if monicaBettyPantiesId == 5:
            #Betty5
            img 7654
            w
            img 7655
            w
            img 7656
            w


    if monicaMustWearBettyPanties == True and (monicaBettyPantiesId != bettyPantiesLog[1] or monicaBettyPanties == False):
        music Groove2_85 high
        img 7657
        bardie "Ты одела не те трусики! Бетти была вчера в других!"
        mt "!!!"
    else:
        if monicaMustWearBettyPanties == True:
            bardie "Ты одела правильные трусики! Хорошая гувернантка!"
            mt "!!!"
        if monicaMustNotWearPanties == True:
            if monicaUnder != "Nude":
                call gallery_7635_1() # замечание
            else:
                bardie "Молодец, гувернантка. Ты соблюдаешь правила дома."
#    music Pyro_Flow high
#    $ add_corruption(bardieCleaning2UpskirtCorruption, "bardie_monica_upskirt_corruption_day_" + str(day))
    $ restore_music()
#    call EP22_Quests_Bardie4_check_progress()
    return

label gallery_10563:
    #render+
    #иногда Барди появляется в комнате, где убирается Моника
    #комнаты floor1 (если нет Ральфа)
    $ store_music()
    music Marty_Gots_a_Plan high
#    $ add_corruption(bardieCleaningUpskirtTryCorruption, "bardie_monica_upskirt_corruption_day_" + str(day))
    img 6030
    w
    img 6031
    w
    img 6032
    w
    #Governess Pants
#    bardie "Моника! Покажи трусики!"
    if monicaBettyPanties == False:
        if monicaUnder == "Nude":
            img 10561
            sound Jump2
            w
            img 10562
            w
            img 10563
            w
        else:
            img 7659
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7660
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7661
            w
    else:
        if monicaBettyPantiesId == 1:
            #Betty1
            img 7662
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7663
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7664
        if monicaBettyPantiesId == 2:
            #Betty2
            img 7665
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7666
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7667
            w
        if monicaBettyPantiesId == 3:
            #Betty3
            img 7668
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7669
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7670
            w
        if monicaBettyPantiesId == 4:
            #Betty4
            img 7671
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7672
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7673
            w
        if monicaBettyPantiesId == 5:
            #Betty5
            img 7674
            sound Jump2
            bardie "Моника! Можешь не отвлекаться!"
            img 7675
            "Я лишь проверю что у тебя все в порядке с твоими трусиками!"
            img 7676
            w
            img 7677
            w

    img 7658
    mt "!!!"
    if monicaMustWearBettyPanties == True and (monicaBettyPantiesId != bettyPantiesLog[1] or monicaBettyPanties == False):
        # Если Моника одела не те трусики
        music Groove2_85 high
        bardie "Ты одела не те трусики! Бетти была вчера в других!"
        mt "!!!"
    else:
        if monicaMustWearBettyPanties == True:
            bardie "Ты одела правильные трусики! Хорошая гувернантка!"
            mt "!!!"
        if monicaMustNotWearPanties == True:
            if monicaUnder != "Nude":
                call gallery_7635_1() # замечание
            else:
                bardie "Молодец, гувернантка. Ты соблюдаешь правила дома."
#    music Pyro_Flow high
    # Моника
    $ restore_music()
#    call EP22_Quests_Bardie4_check_progress()
    return

label gallery_10414:
# Теперь, когда Бетти находится в спальне, там периодически находится Барди, который проверяет ее трусики.
# Моника может подойти к Бетти в спальне и проверить ее трусики.
# Также Моника может подойти к Бетти у зеркала на floor2 и проверить трусики тоже.


    # Бетти в спальне, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10402
    with fadelong
    w
    img 10403
    w
    img 10404
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"
    img 10420
    with fade
    sound Jump2
    if bettyPantiesCurrent >= 1:
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    else:
        w

    #betty
    if bettyPantiesCurrent == 1:
        img 10405
        with fade
        w
        img 10406
        with diss
        w
    #
    if bettyPantiesCurrent == 2:
        img 10407
        with fade
        w
        img 10408
        with diss
        w
    #
    if bettyPantiesCurrent == 3:
        img 10409
        with fade
        w
        img 10410
        with diss
        w
    #
    if bettyPantiesCurrent == 4:
        img 10411
        with fade
        w
        img 10412
        with diss
        w
    #
    if bettyPantiesCurrent == 5:
        img 10413
        with fade
        w
        img 10414
        with diss
        w
    #
    if bettyPantiesCurrent == 0:
        #nude
        img 10415
        with fade
        bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
            #random
        call showRandomImagesDiss([10416, 10417, 10418, 10419], 2)
#        w
#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"

    betty "!!!"

    $ restore_music()
    music Sneaky_Snitch
    return

label gallery_10416:
# Теперь, когда Бетти находится в спальне, там периодически находится Барди, который проверяет ее трусики.
# Моника может подойти к Бетти в спальне и проверить ее трусики.
# Также Моника может подойти к Бетти у зеркала на floor2 и проверить трусики тоже.


    # Бетти в спальне, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10402
    with fadelong
    w
    img 10403
    w
    img 10404
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"
    img 10420
    with fade
    sound Jump2
    if bettyPantiesCurrent >= 1:
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    else:
        w

    #betty
    if bettyPantiesCurrent == 1:
        img 10405
        with fade
        w
        img 10406
        with diss
        w
    #
    if bettyPantiesCurrent == 2:
        img 10407
        with fade
        w
        img 10408
        with diss
        w
    #
    if bettyPantiesCurrent == 3:
        img 10409
        with fade
        w
        img 10410
        with diss
        w
    #
    if bettyPantiesCurrent == 4:
        img 10411
        with fade
        w
        img 10412
        with diss
        w
    #
    if bettyPantiesCurrent == 5:
        img 10413
        with fade
        w
        img 10414
        with diss
        w
    #
    if bettyPantiesCurrent == 0:
        #nude
        img 10415
        with fade
        bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
            #random
        call showRandomImagesDiss([10416, 10417, 10418, 10419], 2)
#        w
#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"

    betty "!!!"

    $ restore_music()
    music Sneaky_Snitch
    return

label gallery_10432:
    # Бетти у зеркала, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10421
    with fadelong
    w
    img 10422
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"

    #betty
    if bettyPantiesCurrent == 1:
        img 10423
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10424
        with diss
        w
    #
    if bettyPantiesCurrent == 2:
        img 10426
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10425
        with diss
        w
    #
    if bettyPantiesCurrent == 3:
        img 10427
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10428
        with diss
        w
    #
    if bettyPantiesCurrent == 4:
        img 10430
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10429
        with diss
        w
    #
    if bettyPantiesCurrent == 5:
        img 10431
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10432
        with diss
        w
    #nude
    if bettyPantiesCurrent == 0:
        img 10433
        with diss
        sound Jump2
        bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
        #random
        img 10434
        with diss
        w
        call showRandomImagesDiss([10435, 10436, 10437, 10438], 2)

#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
    img 10439
    betty "!!!"

    $ restore_music()

    return

label gallery_10435:
    # Бетти у зеркала, Барди проверяет ее трусики
    $ store_music()
    music Sneaky_Snitch high
    img 10421
    with fadelong
    w
    img 10422
    with diss
    sound Jump1
    bardie "Бетти! Можешь не отвлекаться!"

    #betty
    if bettyPantiesCurrent == 1:
        img 10423
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10424
        with diss
        w
    #
    if bettyPantiesCurrent == 2:
        img 10426
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10425
        with diss
        w
    #
    if bettyPantiesCurrent == 3:
        img 10427
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10428
        with diss
        w
    #
    if bettyPantiesCurrent == 4:
        img 10430
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10429
        with diss
        w
    #
    if bettyPantiesCurrent == 5:
        img 10431
        with diss
        sound Jump2
        w
        bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
        img 10432
        with diss
        w
    #nude
    if bettyPantiesCurrent == 0:
        img 10433
        with diss
        sound Jump2
        bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
        #random
        img 10434
        with diss
        w
        call showRandomImagesDiss([10435, 10436, 10437, 10438], 2)

#    bardie "Я лишь проверю, что у тебя все в порядке с твоими трусиками!"
    #
#    bardie "Я лишь проверю, что ты соблюдаешь правила этого дома!"
    img 10439
    betty "!!!"

    $ restore_music()

    return

label gallery_10452:
    # Моника у зеркала проверяет трусики Бетти
    $ store_music()
    music Hidden_Agenda high
    img 10440
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10441
    betty "!!!"
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return
    img 10442
    with fade
    m "..."
    #betty
    sound snd_fabric1
    if bettyPantiesCurrent == 1:
        img 10443
        with fade
        betty "На, гувернантка, смотри."
        img 10444
        with fade
        w
        betty "И не вздумай одеть другие!"
    #
    if bettyPantiesCurrent == 2:
        img 10446
        with fade
        betty "На, гувернантка, смотри."
        img 10445
        with fade
        w
        betty "И не вздумай одеть другие!"
    #
    if bettyPantiesCurrent == 3:
        img 10447
        with fade
        betty "На, гувернантка, смотри."
        img 10448
        with fade
        w
        betty "И не вздумай одеть другие!"
    #
    if bettyPantiesCurrent == 4:
        img 10450
        with fade
        betty "На, гувернантка, смотри."
        img 10449
        with fade
        w
        betty "И не вздумай одеть другие!"
    #
    if bettyPantiesCurrent == 5:
        img 10451
        with fade
        betty "На, гувернантка, смотри."
        img 10452
        with fade
        w
        betty "И не вздумай одеть другие!"

#    betty "На, гувернантка, смотри. И не вздумай одеть другие!"
    $ restore_music()
    return

label gallery_10459:
    # Моника проверяет без трусиков Бетти у зеркала
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики
    if monicaUnder != "Nude":
        mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
        mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
        return
    #

    $ store_music()
    music Hidden_Agenda high
    img 10453
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10454
    betty "..."
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return
    w
    # Бетти показывает попу
    sound snd_fabric1
    img 10455
    with fade
    w
    #random
    call showRandomImagesDiss([10456, 10457, 10458], 1)
#    img 10456
#    img 10457
#    img 10458
#    w

    img 10459
    with diss
    w
    betty "Я соблюдаю правила этого дома..."
    img 10460
    with fade
    betty "Покажи, что ты тоже!"
    m "Да, Миссис Робертс, конечно..."

    # Моника показывает попу
    sound snd_fabric1
    img 10461
    with fade
    w
    img 10462
    with diss
    w
    #random
    call showRandomImagesDiss([10463, 10464, 10465, 10466, 10467, 10468], 3)
#    img 10463
#    img 10464
#    img 10465
#    img 10466
#    img 10467
#    img 10468


    img 10462
    with fade
    m "Я тоже соблюдаю правила этого дома..."
    $ restore_music()

    return

label gallery_10463:
    # Моника проверяет без трусиков Бетти у зеркала
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики
    if monicaUnder != "Nude":
        mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
        mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
        return
    #

    $ store_music()
    music Hidden_Agenda high
    img 10453
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10454
    betty "..."
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return
    w
    # Бетти показывает попу
    sound snd_fabric1
    img 10455
    with fade
    w
    #random
    call showRandomImagesDiss([10456, 10457, 10458], 1)
#    img 10456
#    img 10457
#    img 10458
#    w

    img 10459
    with diss
    w
    betty "Я соблюдаю правила этого дома..."
    img 10460
    with fade
    betty "Покажи, что ты тоже!"
    m "Да, Миссис Робертс, конечно..."

    # Моника показывает попу
    sound snd_fabric1
    img 10461
    with fade
    w
    img 10462
    with diss
    w
    #random
    call showRandomImagesDiss([10463, 10464, 10465, 10466, 10467, 10468], 3)
#    img 10463
#    img 10464
#    img 10465
#    img 10466
#    img 10467
#    img 10468


    img 10462
    with fade
    m "Я тоже соблюдаю правила этого дома..."
    $ restore_music()

    return

label gallery_10482:
    # Моника в спальне проверяет трусики Бетти
    $ store_music()
    music Hidden_Agenda high
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False
    img 10469
    with fade
    w
    img 10470
    with fade
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10471
    betty "!!!"
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return
    img 10472
    with diss
    m "..."
    img 10473
    with fade
    betty "Ладно..."
    sound snd_fabric1
    img 10474
    with fade
    w

    #betty
    if bettyPantiesCurrent == 1:
        img 10475
        with fade
        w
        img 10476
        with diss
        betty "На, гувернантка, смотри."
        w
        img 10477 #общий
        with diss
        w
        img 10478
        with diss
        w
    #
    if bettyPantiesCurrent == 2:
        img 10479
        with fade
        w
        img 10480
        with diss
        betty "На, гувернантка, смотри."
        w
        img 10477 #общий
        with diss
        w
        img 10481
        with diss
        w
    #
    if bettyPantiesCurrent == 3:
        img 10482
        with fade
        w
        img 10483
        with diss
        betty "На, гувернантка, смотри."
        w
        img 10477 #общий
        with diss
        w
        img 10484
        with diss
        w
    #
    if bettyPantiesCurrent == 4:
        img 10485
        with fade
        w
        img 10486
        with diss
        betty "На, гувернантка, смотри."
        w
        img 10477 #общий
        with diss
        w
        img 10487
        with diss
        w
    #
    if bettyPantiesCurrent == 5:
        img 10488
        with fade
        w
        img 10489
        with diss
        w
        img 10477 #общий
        with diss
        w
        img 10490
        with diss
        w
    #

    betty "И не вздумай одеть другие!"

#    betty "На, гувернантка, смотри. И не вздумай надеть другие!"
    img 10491
    with fade
    mt "..."

    $ restore_music()
    return

label gallery_10498:
    # Моника проверяет без трусиков Бетти в спальне
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики
    if monicaUnder != "Nude":
        mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
        mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
        return
    #

    $ store_music()
    music Hidden_Agenda high
    img 10492
    with fade
    w
    img 10493
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10494
    with fade
    betty "!!!"
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return

    if char_info["Betty"]["level"] < 6:
        #обычный
        # Бетти показывает попу
        img 10495
        with fade
        w

        img 10496
        with fade
        w
        sound snd_fabric1
        img 10497
        with fade
        w

        #random
        call showRandomImagesDiss([10498, 10499, 10500, 10501, 10502, 10503, 10504, 10505], rand(3,4))
        #

        img 10506
        with diss
        betty "Я соблюдаю правила этого дома..."
        img 10507
        with fade
        betty "Покажи, что ты тоже!"
        img 10508
        w
        img 10509
        with fade
        m "Да, Миссис Робертс, конечно..."

        sound snd_fabric1
        img 10510
        with fade
        w
        img 10511
        with diss
        w
        img 10512
        with diss
        w
        img 10513
        with diss
        w

        #random
        call showRandomImagesDiss([10514, 10515, 10516, 10517, 10518, 10519, 10520, 10521], rand(3,4))
#        img 10514
#        img 10515
#        img 10516
#        img 10517
#        img 10518
#        img 10519
#        img 10520
#        img 10521
        #
        img 10522
        with diss
        w
        img 10523
        with diss
        w
        img 10524
        with fade
        m "Я тоже соблюдаю правила этого дома..."
        $ restore_music()
        return

    else:
        #бонус
        music Loved_Up high
        sound snd_fabric1
        img 10525
        with fade
        w
        img 10526
        with fade
        w
        img 10527
        with diss
        w
        img 10528
        with diss
        w
        img 10529
        with diss
        w
        #random
        call showRandomImagesDiss([10530, 10531, 10532, 10533, 10534, 10535], 3)
#        img 10530
#        img 10531
#        img 10532
#        img 10533
#        img 10534
#        img 10535
        #

        img 10536
        with fade
        betty "Я соблюдаю правила этого дома..."
        betty "Покажи, что ты тоже!"

        img 10537
        with fade
        m "Да, Миссис Робертс, конечно..."
        sound snd_fabric1
        img 10538
        with fade
        w
        img 10539
        with diss
        w
        #random
        call showRandomImagesDiss([10540, 10541, 10542, 10543, 10544, 10545], 3)
#        img 10540
#        img 10541
#        img 10542
#        img 10543
#        img 10544
#        img 10545
        #
        img 10546
        with diss
        w
        img 10547
        with diss
        w
        img 10548
        with diss
        w
        img 10549
        with diss
        w
        img 10550
        with diss
        w
        img 10551
        with diss
        w
        img 10552
        with diss
        w
        img 10553
        with fade
        m "Я тоже соблюдаю правила этого дома..."

    $ restore_music()
    return

label gallery_10515:
    # Моника проверяет без трусиков Бетти в спальне
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики
    if monicaUnder != "Nude":
        mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
        mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
        return
    #

    $ store_music()
    music Hidden_Agenda high
    img 10492
    with fade
    w
    img 10493
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10494
    with fade
    betty "!!!"
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return

    if char_info["Betty"]["level"] < 6:
        #обычный
        # Бетти показывает попу
        img 10495
        with fade
        w

        img 10496
        with fade
        w
        sound snd_fabric1
        img 10497
        with fade
        w

        #random
        call showRandomImagesDiss([10498, 10499, 10500, 10501, 10502, 10503, 10504, 10505], rand(3,4))
        #

        img 10506
        with diss
        betty "Я соблюдаю правила этого дома..."
        img 10507
        with fade
        betty "Покажи, что ты тоже!"
        img 10508
        w
        img 10509
        with fade
        m "Да, Миссис Робертс, конечно..."

        sound snd_fabric1
        img 10510
        with fade
        w
        img 10511
        with diss
        w
        img 10512
        with diss
        w
        img 10513
        with diss
        w

        #random
        call showRandomImagesDiss([10514, 10515, 10516, 10517, 10518, 10519, 10520, 10521], rand(3,4))
#        img 10514
#        img 10515
#        img 10516
#        img 10517
#        img 10518
#        img 10519
#        img 10520
#        img 10521
        #
        img 10522
        with diss
        w
        img 10523
        with diss
        w
        img 10524
        with fade
        m "Я тоже соблюдаю правила этого дома..."
        $ restore_music()
        return

    else:
        #бонус
        music Loved_Up high
        sound snd_fabric1
        img 10525
        with fade
        w
        img 10526
        with fade
        w
        img 10527
        with diss
        w
        img 10528
        with diss
        w
        img 10529
        with diss
        w
        #random
        call showRandomImagesDiss([10530, 10531, 10532, 10533, 10534, 10535], 3)
#        img 10530
#        img 10531
#        img 10532
#        img 10533
#        img 10534
#        img 10535
        #

        img 10536
        with fade
        betty "Я соблюдаю правила этого дома..."
        betty "Покажи, что ты тоже!"

        img 10537
        with fade
        m "Да, Миссис Робертс, конечно..."
        sound snd_fabric1
        img 10538
        with fade
        w
        img 10539
        with diss
        w
        #random
        call showRandomImagesDiss([10540, 10541, 10542, 10543, 10544, 10545], 3)
#        img 10540
#        img 10541
#        img 10542
#        img 10543
#        img 10544
#        img 10545
        #
        img 10546
        with diss
        w
        img 10547
        with diss
        w
        img 10548
        with diss
        w
        img 10549
        with diss
        w
        img 10550
        with diss
        w
        img 10551
        with diss
        w
        img 10552
        with diss
        w
        img 10553
        with fade
        m "Я тоже соблюдаю правила этого дома..."

    $ restore_music()
    return

label gallery_10539:
    # Моника проверяет без трусиков Бетти в спальне
#    menu:
#        "Миссис Робертс, я бы хотела проверить Ваши трусики...":
#            pass
#        "Уйти.":
#            return False

    # Если есть какие-то трусики
    if monicaUnder != "Nude":
        mt "Мне не следует проверять трусики у Бетти, потому что я сама сейчас в трусиках..."
        mt "Бетти может проверить в ответ и я рискую потерять крышу над головой..."
        return
    #

    $ store_music()
    music Hidden_Agenda high
    img 10492
    with fade
    w
    img 10493
    m "Миссис Робертс, я бы хотела проверить Ваши трусики..."
    music Groove2_85 high
    img 10494
    with fade
    betty "!!!"
    if bettyShowedPantiesLastDay == day:
        betty "Гувернантка, Я уже показывала тебе сегодня!"
        $ restore_music()
        return

    if char_info["Betty"]["level"] < 6:
        #обычный
        # Бетти показывает попу
        img 10495
        with fade
        w

        img 10496
        with fade
        w
        sound snd_fabric1
        img 10497
        with fade
        w

        #random
        call showRandomImagesDiss([10498, 10499, 10500, 10501, 10502, 10503, 10504, 10505], rand(3,4))
        #

        img 10506
        with diss
        betty "Я соблюдаю правила этого дома..."
        img 10507
        with fade
        betty "Покажи, что ты тоже!"
        img 10508
        w
        img 10509
        with fade
        m "Да, Миссис Робертс, конечно..."

        sound snd_fabric1
        img 10510
        with fade
        w
        img 10511
        with diss
        w
        img 10512
        with diss
        w
        img 10513
        with diss
        w

        #random
        call showRandomImagesDiss([10514, 10515, 10516, 10517, 10518, 10519, 10520, 10521], rand(3,4))
#        img 10514
#        img 10515
#        img 10516
#        img 10517
#        img 10518
#        img 10519
#        img 10520
#        img 10521
        #
        img 10522
        with diss
        w
        img 10523
        with diss
        w
        img 10524
        with fade
        m "Я тоже соблюдаю правила этого дома..."
        $ restore_music()
        return

    else:
        #бонус
        music Loved_Up high
        sound snd_fabric1
        img 10525
        with fade
        w
        img 10526
        with fade
        w
        img 10527
        with diss
        w
        img 10528
        with diss
        w
        img 10529
        with diss
        w
        #random
        call showRandomImagesDiss([10530, 10531, 10532, 10533, 10534, 10535], 3)
#        img 10530
#        img 10531
#        img 10532
#        img 10533
#        img 10534
#        img 10535
        #

        img 10536
        with fade
        betty "Я соблюдаю правила этого дома..."
        betty "Покажи, что ты тоже!"

        img 10537
        with fade
        m "Да, Миссис Робертс, конечно..."
        sound snd_fabric1
        img 10538
        with fade
        w
        img 10539
        with diss
        w
        #random
        call showRandomImagesDiss([10540, 10541, 10542, 10543, 10544, 10545], 3)
#        img 10540
#        img 10541
#        img 10542
#        img 10543
#        img 10544
#        img 10545
        #
        img 10546
        with diss
        w
        img 10547
        with diss
        w
        img 10548
        with diss
        w
        img 10549
        with diss
        w
        img 10550
        with diss
        w
        img 10551
        with diss
        w
        img 10552
        with diss
        w
        img 10553
        with fade
        m "Я тоже соблюдаю правила этого дома..."

    $ restore_music()
    return

label gallery_12962:
    # Моника случайно заходит к Барди (первый раз)

    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up
    # Сцена Барди с журналом
    # Старт, пара кадров
    #video
    img 12959
    with fadelong
    bardie "Аххх! Ахххх!!!"
    bardie "Моника Бакфетт..."
    img black_screen
    with diss
#    stop music
#    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Bardie_Masturbation_1_1 = Movie(play="video/v_Bardie_Masturbation_1_1.mkv", fps=30)
    show videov_Bardie_Masturbation_1_1
    with fade
    wclean
    img 12960
    with fade
    bardie "Аххх! Ахххх!!!"
    img black_screen
    with diss
#    stop music
#    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Bardie_Masturbation_1_2 = Movie(play="video/v_Bardie_Masturbation_1_2.mkv", fps=30)
    show videov_Bardie_Masturbation_1_2
    with fade
    wclean
    img 12961
    with fade
    bardie "Моя гувернантка..."
    bardie "Аххх!"
    img black_screen
    with diss
#    stop music
#    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Bardie_Masturbation_1_3 = Movie(play="video/v_Bardie_Masturbation_1_3.mkv", fps=30)
    show videov_Bardie_Masturbation_1_3
    with fade
    wclean
    img 12962
    with fade
    bardie "Я молодец!"
    bardie "Я хороший хозяин, Аххх!"
    # video end
    # Барди кончает
    img black_screen
    with diss
#    stop music
#    play music "<from " + str((rand(1,5)*1.1666)) + " loop 0.0>Sounds/audio_Steve_Monica_Sex_4.mp3"
    scene black
    image videov_Bardie_Masturbation_1_4 = Movie(play="video/v_Bardie_Masturbation_1_4.mkv", fps=30)
    show videov_Bardie_Masturbation_1_4
    with fade
    wclean
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    sound hlup10
    img 12963
    with diss
    bardie "АХХХХХХ!!!"
    bardie "..."
    sound hlup10
    img 12965
    with diss
    bardie "Ее сиськи..."
    sound hlup10
    img 12964
    with diss
    w
    music stop
    sound hlup19
    img 13183
    with diss
    w
    music Sneaky_Snitch
    img 12966
    with fadelong
    bardie "Интересно, они настоящие или нет..."
    bardie "Как это я упустил их из виду..."
    img 12967
    bardie "У меня все еще недостаточный контроль над ней..."
    bardie "Мне нужно увидеть ее сиськи... И даже больше..."
    img 12968
    with diss
    bardie "И мне нужна еще фотография, чтобы дрочить на нее."
    bardie "Этот журнал уже надоел мне..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    # хитро прищуриваясь
    music Sneaky_Snitch
    img 12969
    with fadelong
    bardie "Может быть есть еще выпуски?"
    bardie "Надо будет спросить у гувернантки..."
    img 12970
    bardie "И, было бы неплохо не только дрочить на нее, но и делать нечто более..."
    bardie "Хотя я ее, пока, немного побаиваюсь..."
    img 12971
    with diss
    bardie "Все-таки она Моника Бакфетт, но, почему-то боится штрафа..."
    bardie "Может быть она не настоящая Моника Бакфетт, потому и боится?"
    bardie "И Бетти..."
    img 12972
    with fade
    bardie "Эта мачеха, хоть и соблюдает правила дома, но, все-же, действует мне на нервы."
    bardie "Я мечтаю не только смотреть ей под юбку, но и, когда-нибудь, трахнуть ее!"
    img 12973
    with diss
    bardie "Вокруг ходит столько целей, а я все еще девственник!"
    bardie "Это ненормально! Я что, какой-то нудачник?!"


    # Моника заходит. Журнал весь в сперме
    music Power_Bots_Loop
    sound highheels_run2
    img 12974
    with fadelong
    m "Что... Что ты делаешь??"
    img 13183
    with diss
    w
    img 13184
    with diss
    m "Это... Это Я?!"
    img 12975
    with diss
    m "Это мой журнал! Мой!"
    m "Что ты делаешь с ним?!"
    music Groove2_85
    img 12976
    bardie "Я дрочу на него, я же говорил тебе."
    img 12977
    with fade
    m "Я... Не смей делать этого!"
    m "Верни его мне!"
    img 12978
    bardie "Я верну тебе его только если ты принесешь мне другой!"
    bardie "Новый выпуск!"
    img 12979
    with diss
    m "Нет новых выпусков, я не работаю там!"
    m "Я торчу здесь! И меня это бесит!"
    img 12980
    with fade
    bardie "Ты здесь работаешь! И я твой хозяин!"
    music Power_Bots_Loop
    img 12981
    m "!!!"
    # Моника уходит
    sound highheels_short_walk
    img 12982
    with fadelong
    w
    return

label gallery_13001:
    # Моника прходит к Барди спросить о еде в доме (второй приход)
# Моника приходит к Барди и говорит что, учитывая то, что она ведет себя хорошо, может быть
# Барди скажет Бетти, чтобы та кормила прислугу в доме.
# Барди спрашивает хорошая-ли Моника гувернантка, что просит о таком?
# Моника отвечает что хорошая (либо не отвечает)
# Барди просит продемострировать что Моника соблюдает правила дома.
    music Hidden_Agenda
    img 12983
    with fadelong
    m "Барди..."
    img 12984
    bardie "Да, гувернантка?"
    img 12985
    with diss
    m "У меня разговор к тебе..."
    sound snd_cardboard2
    img 12986
    with fade
    bardie "Я тебя слушаю."
    img 12987
    with diss
    m "Барди, я ведь хорошо себя веду, так ведь?"
    img 12988
    bardie "Да, гувернантка... Обычно ты соблюдаешь правила дома..."
    img 12989
    with diss
    m "Барди, если ты доволен мной, то..."
    m "То, может быть, Я заслуживаю того, чтобы меня кормили в этом доме."
    m "Может быть ты скажешь Бетти об этом?"
    # Щурится
    img 12990
    with diss
    m "Ты ведь тут самый главный? Правда?"
    music Groove2_85
    img 12991
    with fade
    bardie "О таком может просить только хорошая гувернантка."
    bardie "Ты хорошая гувернантка, Моника?"
    img 12992
    with diss
    menu:
        "Да, я хорошая гувернантка...":
            pass
        "Уйти.":
            sound highheels_run2
            img 12982
            with fade
            w
            return
    img 12993
    with fade
    m "Да, я хорошая гувернантка..."
    img 12994
    with diss
    bardie "Хорошо, покажи, что ты соблюдаешь правила дома!"

# Моника соглашается либо нет.
# Если соглашается и у нее надеты трусики, то Барди злится и устраивает порку.
    if monicaUnder != "Nude":
        music Hidden_Agenda
        img 12995
        with fade
        mt "Черт! У меня надеты трусики!"
        mt "Мне лучше не показывать их этому сопляку!"
    music Groove2_85
    img 13078
    with fade
    menu:
        "Задрать юбку.":
            pass
        "Попросить выйти.":
            music Hidden_Agenda
            img 12996
            with fade
            m "Барди, конечно я соблюдаю правила."
            m "Я вспомнила об одном важном деле!"
            img 12997
            with diss
            m "Мне надо отлучиться и я вернусь сюда!"
            sound highheels_run2
            img 12982
            with fade
            w
            return

    # Моника показывает
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Loved_Up
    img 13185
    with fadelong
    w
    if monicaUnder != "Nude":
        # Моника показывает
        #governess
        if monicaBettyPanties == False:
            img 20508
        else:
            #betty
            if monicaBettyPantiesId == 1:
                img 13002
            if monicaBettyPantiesId == 2:
                img 13003
            if monicaBettyPantiesId == 3:
                img 13004
            if monicaBettyPantiesId == 4:
                img 13005
            if monicaBettyPantiesId == 5:
                img 13006
        with diss
        w
        music Groove2_85
        img 12998
        with fade
        bardie "Нерадивая гувернантка!"
        bardie "Ты не соблюдаешь правила дома!"
#        img 12999
        bardie "Следуй к себе в подвал для прохождения наказания!"
        img 13000
        m "!!!"
        # идет наказание
        return
    img 13001
    with diss
    w



# Тогда Барди говорит чтобы та показала свою грудь.
# Моника может это делать, либо нет. Если нет, то Барди злится и устраивает порку, но грудь Моника не показывает.
#    img 13007
    img 12999
    with fade
    bardie "Хорошо."
    bardie "Теперь покажи свои сиськи!"
    music Power_Bots_Loop
    img 13008
    with diss
    m "Мы так не договаривались!"
    m "Я не собираюсь этого делать!"
    img 13009
    bardie "Ты моя игрушка и принадлежишь мне!"
    img 13010
    with diss
    m "Ах ты мелюзга!"
    m "Я не буду показывать тебе свою грудь!"
    music Groove2_85
    img 13011
    with fade
    bardie "Ты решила не подчиняться приказам хозяина дома? Я правильно понял?"
    img 13012
    with diss
    menu:
        "Подчиниться и показать грудь.":
            pass
        "Не показывать грудь!":
            music Power_Bots_Loop
            img 13013
            with fade
            m "Я и так хожу с голой задницей по дому целыми днями!"
            m "Разве тебе этого мало?!"
            music Groove2_85
            img 12998
            with diss
            bardie "Нерадивая гувернантка!"
            bardie "Ты не слушаешься хозяина дома!"
            bardie "Следуй к себе в подвал для прохождения наказания!"
            return

    # Моника показывает грудь
    label gallery_13051:
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 13014
    with fadelong
    w
    img 13049
    with diss
    w
    img 13050
    with diss
    w
    # Барди берет журнал и держит его рядом, сравнивая грудь
    sound snd_take_paper
    img 13051
    with diss
    w
    img 13052
    with diss
    bardie "Да, у тебя такая же грудь."
    bardie "Ты действительно похожа не нее."
    music Power_Bots_Loop
    img 13053
    with fade
    m "ЭТО И ЕСТЬ Я!"
    music Loved_Up
    img 13054
    with diss
    mt "Черт! Зачем я это сказала?!"

# Барди задумывается, улыбается и говорит что хозяин дома подумает, пусть Моника приходит завтра.

    img 13055
    with fade
    w
    img 13056
    with diss
    w
    music Groove2_85
    img 13057
    with fade
    bardie "Хорошо, хозяин дома подумает." # разглядывая грудь
    bardie "Гувернантка, приходи завтра."
    bardie "Хозяин скажет тебе о своем решении."
    # Моника закрывает грудь
    sound snd_fabric1
    img 13058
    with fadelong
    m "!!!"

#    bardie "Да, и еще!"
    return

label gallery_13045:
# На след. день Моника приходит к Барди и спрашивает подумал-ли он?
# Барди отвечает что готов сделать величественный жест ради хорошей гувернантки, которая хорошо себя ведет.
# И сказать Бетти, чтобы она кормила Монику
# Переспрашивает хорошая-ли гувернантка Моника?
    music Hidden_Agenda
    img 13015
    with fadelong
    m "Барди, ты подумал насчет того, чтобы я получала заслуженную еду в этом доме?!"
#    music Groove2_85
    img 13016
    with diss
    bardie "Да, гувернантка."
    bardie "Я подумал и решил что готов сделать величественный жест ради хорошей гувернантки."
    bardie "Которая хорошо себя ведет..."
    img 13017
    mt "!!!"
    img 13018
    with diss
    bardie "И я скажу Бетти, чтобы она кормила гувернантку."
    bardie "Но только хорошую гувернантку!"
    bardie "Ты ведь хорошая гувернантка, Моника?"
    img 13019
    menu:
        "Да...":
            pass
        "Я... Подумаю о том какая Я...":
            music Groove2_85
            img 13020
            with fade
            m "Я еще не решила..."
            img 13021
            with diss
            bardie "Когда будешь уверена, приходи!"
            return

# Моника отвечает что да.
    m "Да..."
#    img 13021
# Барди говорит чтобы та сделала titjob. Моника в шоке и спрашивает не рановато-ли Барди думать о таких вещах.
# Барди отвечает что он уже достаточно большой. (мне уже 18, либо можно поменять число)
    img 13023
    with fade
    bardie "Хорошо, я много раз кончал на твои сиськи на журнале."
    bardie "Теперь я хочу сделать это прямо на них."
    music Groove2_85
    img 13024
    with diss
    m "ЧТО?!"
    m "Барди, я понимаю, что ты уже интересуешься девушками."
    m "Придумываешь разные глупые игры. У тебя играют гормоны."
    img 13025
    with diss
    m "Но тебе не кажется, что тебе рановато думать о чем-то большем?!"
    m "Тем более в отношении меня!"
    img 13026
    with fadelong
    bardie "Я не маленький! Я большой!"
    bardie "Мне уже 21!"
#    help "Внося изменения в игру, Вы берете на себя ответственность."
#    help "Вы уверены в этом?"


# Барди ложится на кровать и достает член.
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 13027
    with fadelong
    bardie "..."
# Моника в шоке смотрит на это.
    sound Jump2
    img 13186
    w
    img 13028
    with diss
    m "!!!"
# Барди спрашивает чего гувернантка ждет? Она должна выполнять обязанности по дому, в число которых входит
# то, чтобы хозяин дома оставался доволен.
    img 13029
    with fade
    bardie "Ну?!"
    bardie "И чего же гувернантка ждет?"
    bardie "Хорошая гувернантка должна выполнять обязанности по дому."
    bardie "Соблюдать везде чистоту."
    img 13030
    bardie "Это место надо протереть от пыли."
    bardie "И оно слишком чувствительное, поэтому это надо сделать твоими сиськами!"
    music Groove2_85
    img 13031
    m "!!!"

# Моника злая, смотрит и думает.
    img 13032
    with diss
    m "Я уверена в том, что это место протирается регулярно и без меня!"
# Барди говорит что если гувернантка будет хорошей, то ее в этом доме будут кормить.
    img 13033
    with fade
    bardie "Хорошая гувернантка должна выполнять эту работу."
    bardie "И, если гувернантка будет хорошей, то ее в этом доме будут кормить."

# Моника принимает решение
    music Hidden_Agenda
    img 13034
    with fade
    mt "Что же мне делать?!"
    mt "Ведь я не буду трогать своей изысканной грудью член этого Барди?"
    img 13035
    with diss
    mt "С другой стороны, я в шаге от того, чтобы нормально питаться."
    mt "В своем же доме!"
    music Groove2_85
    img 13036
    with fade
    bardie "А плохую гувернантку может ждать наказание..."
    img 13037
    with diss
    mt "Что же мне делать?!"
    img 13038
    with diss
    menu:
        "Сделать это...":
            pass
        "Я... Пока не готова для этого...":
            # Говорит что она пока не готова для этого (corruption)
            music Hidden_Agenda
            img 13039
            with fade
            m "Я... Пока не готова для этого..."
            music Groove2_85
            img 13040
            with diss
            bardie "Тогда иди и готовься!"
            bardie "Иначе ты станешь плохой гувернанткой!"
            return
# Либо соглашается и делает titjob
    music Hidden_Agenda
    img 13041
    with fadelong
    m "Я не умею делать это..."
    music Groove2_85
    img 13042
    bardie "Я тоже не умею делать это. Но не думаю что это сложно!"
    bardie "Вынь свои сиськи и положи их на мой член!"

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 13043
    with fadelong
    m "..."
    img 13044
    with diss
    bardie "Вот так. А теперь начинай двигать ими вверх и вниз!"
# Барди говорит хорошая гувернантка и тд
    # video
    music stop
    img black_screen
    with diss
    pause 1.5
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_1 = Movie(play="video/v_Monica_Bardie_Titjob_1_1.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_2 = Movie(play="video/v_Monica_Bardie_Titjob_1_2.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_2
    with fadelong
    wclean
    music Loved_Up
    img 13045
    with fade
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_3 = Movie(play="video/v_Monica_Bardie_Titjob_1_3.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_3
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_4 = Movie(play="video/v_Monica_Bardie_Titjob_1_4.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_4
    with fadelong
    wclean
    music Loved_Up
    img 13046
    with fade
    bardie "Хорошая гувернантка..."
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_5 = Movie(play="video/v_Monica_Bardie_Titjob_1_5.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_5
    with fadelong
    wclean
    music Loved_Up
    img 13047
    with fade
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_6 = Movie(play="video/v_Monica_Bardie_Titjob_1_6.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_6
    with fadelong
    wclean
    music Loved_Up
    img 13048
    with fade
    bardie "Хорошая..."
    bardie "Протирай как следует, это твоя работа..."
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_7 = Movie(play="video/v_Monica_Bardie_Titjob_1_7.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_7
    with fadelong
    wclean
    img black_screen
    with diss
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/audio_Monica_Bardie_Titjob_1.mp3"
    scene black
    image videov_Monica_Bardie_Titjob_1_8 = Movie(play="video/v_Monica_Bardie_Titjob_1_8.mkv", fps=30)
    show videov_Monica_Bardie_Titjob_1_8
    with fadelong
    wclean
# Когда заканчивают, Барди говорит Монике придти завтра, когда он уладит обязанности хозяина дома и
# выдаст необходимые распоряжения Бетти
    # end video

    # Барди кончает на грудь Монике
    music stop
    stop music
    img black_screen
    with diss
    bardie "Оооооох!!!"
    sound bulk1
    img 13123
    with fade
    w
    img 13125
    with diss
    w
    sound bulk1
    img 13124
    with fade
    bardie "Оооооох!!!"
    sound hlup19
    img 13126
    with diss
    w
    music Groove2_85
    img 13127
    with fade
    mt "!!!"
    img 13128
    with diss
    w
    img 13129
    bardie "Хорошая гувернантка!"
    bardie "Приходи завтра."
    bardie "Я улажу обязанности хозяина дома и выдам необходимые распоряжения Бетти!"
    sound snd_fabric1
    img 13130
    with fadelong
    m "!!!"
    img black_screen
    with diss

# Моника уходит
    return

label gallery_13115:
    # Если в течении этого дня Моника заглядывает в комнату Барди

    # Идет сцена наказания Бетти
# Бетти стоит в углу.
# Барди говорит что поняла-ли она что хозяина дома надо слушаться.
# Бетти отвечает что да.
    # кадр смотрит
    # обращается
    music Hidden_Agenda
    img 13109
    with fadelong
    w
    img 13110
    with diss
    m "Мистер Робертс, от меня еще что-нибудь требуется?"
    # Бетти смотрит на Монику
    img 13111
    with diss
    # Моника смотрит на Бетти
    m "..."
    img 13112
    with diss
    betty "!!!"
    # Барди отвечает
    img 13113
    with fade
    bardie "Нет, гувернантка. Ты можешь отдыхать."
    # поворачивается в Бетти
    music stop
    img black_screen
    with diss
    sound snd_cardboard2
    pause 1.5
    music Groove2_85
    img 13114
    with fade
    bardie "Поняла что хозяина дома надо слушаться?!"
    img 13115
    with diss
    betty "Да!"
    img 13116
    with fade
    bardie "Поняла что бывает с непослушными девочками?"
    img 13117
    with diss
    betty "Да, поняла. Их ставят в угол..."
    img 13118
    with fade
    bardie "Будешь еще нарушать правила дома?!"
    img 13119
    with diss
    betty "Нет! Не буду!"
    if bettyCollegeDay1JobFinished == False and bettyCollegeTeacherRefused == True:
        img 13118
        bardie "И ты еще не закончила решать мои проблемы в колледже..."
        bardie "Ты не забыла про них?"
        menu:
            "Я завтра пойду в колледж...":
                img 13117
                betty "Я завтра пойду в колледж..."
                return
            "Промолчать...":
                betty "..."
    else:
        img 13120
        with fade
        bardie "И не только в угол! Есть еще другие наказания, хе-хе!"
        bardie "А теперь можешь идти! Заниматься делами по дому!"
        bardie "Завтра на обед я хочу вкусный бургер!"
    img 13121
    with diss
    betty "!!!" # зло смотрит, тянется к платью
    sound snd_fabric1
    img 13122
    with diss
    mt "..." # язвительно улыбается

    # Бетти стоит с красным задом и зло смотрит на Монику
    return

label gallery_13155:
    # Моника заходит на кухню первый раз (либо любой раз, пока Моника еще не показывала грудь)

# Если Моника заходит так, то прибегает Бетти и говорит Монике чтобы та убиралась с кухни!
# Что ей вообще не нужны проститутки в доме и что ей уже надоело присматривать за дурной гувернанткой
# Которая так и норовит нарушить дисциплину!
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    music Groove2_85
    img 13131
    with fadelong
    betty "Моника, гувернантка!"
    betty "Что ты делаешь здесь!"
    img 13132
    betty "Я запретила тебе заходить на кухню!"
    betty "Быстро убирайся отсюда!"
    img 13133
    with diss
    betty "И вообще... Мне не нужны проститутки в доме!"
    betty "И мне надоело присматривать за дурной гувернанткой, которая так и норовит нарушить дисциплину!"
# Моника спрашивает: есть-ли правила, которые позволяют ей питаться здесь?
# Бетти смущается и говорит что есть кое-какое правило и гувернантка сама про него знает. (злится)
# Говорит Монике чтобы та выметалась с кухни
    music Hidden_Agenda
    img 13134
    with fade
    m "Миссис Робертс..."
    m "Есть-ли правила, которые позволяют мне питаться здесь?"
    img 13135
    with diss
    betty "..."
    img 13136
    m "???"
    img 13137
    betty "!!!"
    music Groove2_85
    img 13138
    with fade
    betty "Есть кое-какое правило... И ты, гувернантка, сама знаешь про него..."
    betty "А сейчас, выметайся с кухни!"
# Моника делает выбор:
# Уйти или Оголить грудь (corruption)
    img 13139
    with diss
    menu:
        "Оголить грудь...":
            pass
        "Уйти...":
            sound highheels_run2
            img 13140
            with fade
            w
            return
# Если оголяет: А так?
# Если оголяет первый раз, то Моника про себя думает о том что же она творит, но, с другой стороны.
# Никто кроме Бетти этого не видит и это лучше, чем разносить флаеры за еду или что-то еще похуже.
    music Hidden_Agenda
    img 13142
    with fade
    mt "Моника, что ты творишь?"
    mt "Неужели ты пойдешь на это?"
    img 13141
    with diss
    mt "С другой стороны... Никто кроме Бетти этого не видит"
    mt "И это лучше, чем разносить флаеры за еду или делать что-то еще похуже..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    #fade
    music Loved_Up
    img 13143
    with fadelong
    m "А так?"

# Бетти злится и говорит что у гувернантки нет никакого стыда.
# И чтобы та убиралась отсюда.
    img 13144
    with diss
    betty "!!!"
    img 13145
    with diss
    m "..." # Моника стервозно улыбается
    music Groove2_85
    img 13146
    with fade
    betty "Гувернантка, у тебя нет никакого стыда!"
    betty "Немедленно убирайся отсюда!"
# Моника спрашивает: Вы уверены, Миссис Робертс? Что я должна выйти отсюда?
# Бетти злится и говорит чтобы та садилась за стол.
    music Loved_Up
    img 13147
    with fade
    m "Вы уверены, Миссис Робертс!"
    m "Вы уверены что я должна выйти отсюда?"
    img 13148
    with diss
    betty "!!!"
    music Groove2_85
    img 13149
    with fade
    betty "Садись за стол, сейчас подам тебе..."
# Моника садится.
# Бетти подает еду и говорит что если Ральф увидит ее в таком виде, то ей уже ничего не поможет.
# Даже мелкий засранец, с которым Моника спелась.
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 13150
    with fadelong
    betty "И не вздумай в таком виде шляться по дому!"
    betty "Если Ральф увидит тебя в таком виде, то я вышвырну тебя!"
    img 13151
    betty "И тебе никто не поможет!"
    betty "Даже мелкий засранец Барди, с которым ты спелась!"

    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5

    $ rnd = rand(1,3)

    #
    music RnB3_65
    if rnd == 1:
        img 13167
        with fadelong
        mt "Мммм... Наконец-то я ем вкусную еду..."
        img 13168
        with diss
        mt "В своем доме..."

    if rnd == 2:
        img 13167
        with fadelong
        mt "Мой дом... Моя любимая кухня..."
        mt "Все не так уж плохо..."
        img 13168
        with diss
        mt "Это только первые шаги..."
        mt "Скоро дом будет снова мой..."

    if rnd == 3:
        #
        img 13169
        with fadelong
        mt "Ммм... Я кушаю на своей любимой кухне."
        img 13170
        with diss
        mt "А Бетти прислуживает мне..."
        mt "Так мне нравится намного больше..."

    music stop
    img black_screen
    with diss
    pause 1.0
    sound snd_plates
    music RnB3_65

#    $ images = random.sample(set(images_set1, images_set2, images_set3), 1)

    $ rnd = rand(1,3)
    if rnd == 1:
        img 13152
        with fadelong
        w
        $ images_set1 = [13153, 13154, 13155, 13156]
        $ images = random.sample(set(images_set1), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда1
        music Groove2_85
        img 13174
        with fade
        m "Миссис Робертс. Пожалуйста, подайте мне другие приборы."
        m "Эти недостаточно хорошо вымыты."
        img 13177
        betty "!!!"

    if rnd == 2:
        img 13157
        with fadelong
        w
        $ images_set2 = [13158, 13159, 13160, 13161]
        $ images = random.sample(set(images_set2), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда2
        music Groove2_85
        img 13176
        with fade
        m "Миссис Робертс. Пожалуйста, подогрейте еду."
        m "Она недостаточно горячая."
        img 13177
        betty "!!!"

    if rnd == 3:
        img 13162
        with fadelong
        w
        $ images_set3 = [13163, 13164, 13165, 13166]
        $ images = random.sample(set(images_set3), 2)
        img 13173
        with diss
        betty "Приятного аппетита, гувернантка..."
        img images[0]
        with diss
        w
        img images[1]
        with diss
        w
        # еда3
        music Groove2_85
        img 13175
        with fade
        m "Миссис Робертс. Вы вкусно готовите."
        m "Это похвально."
        img 13177
        betty "!!!"




    # Моника поела
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 13171
    with fadelong
    m "Благодарю Вас, Миссис Робертс."
    m "Я поела."
    img 13172
    betty "!!!"
    return

label gallery_14600:
    # Бетти стоит в комнате Барди и недовольно
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(_("Вечер..."))
    img black_screen
    with Dissolve(2.0)
    music Groove2_85
    img 14566
    with fadelong
    betty "Чего тебе надо? Зачем ты меня звал?"
    # Барди лежит на кровати и смотрит на Бетти с улыбочкой
    music Sneaky_Snitch
    img 14567
    with diss
    bardie "Мне нужно проверить, соблюдаешь ли ты правила этого дома..."
    img 14568
    with fade
    betty_t "Как же меня этот сопляк достал со своими глупостями! Пусть проверяет... и отстанет уже от меня."
    # подходит к Бетти и задирает ей юбку, заглядывает под нее. Бетти без трусиков. Барди довольно
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14569
    with fadelong
    w
    img 14570
    with diss
    w
    img 14571
    with diss
    w
    music Sneaky_Snitch
    img 14572
    with fade
    bardie "Хорошо. Я вижу, что ты соблюдаешь правила. Позови гувернантку. Я давно не проверял ее."
    # Бетти недовольно
    music Power_Bots_Loop
    img 14573
    with diss
    betty "Тебе надо - ты и зови. Мне нет дела до твоих глупостей."
    img 14574
    with fade
    bardie "Я сказал тебе, чтобы ты позвала гувернантку..."
    bardie "Или ты решила, что меня не надо слушаться? Ты забыла, что у меня есть парочка очень интересных фото с тобой и тренером?"
    # Бетти поворачивается к Барди, зло смотрит на него
    music Groove2_85
    img 14575
    with diss
    betty_t "Когда же ты уже отстанешь от меня?!"
    betty_t "!!!"
    # Барди с серьезной миной
    img 14576
    with fade
    bardie "Ну? Я жду!"
    img 14577
    with diss
    betty "!!!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Power_Bots_Loop
    img 14578
    with fadelong
    with hpunch
    betty "Гувернантка! Гувернантка!!!"
    # спустя несколько минут появляется Моника, Барди возле Моники
    # с лица
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Power_Bots_Loop
    img 14579
    with fadelong
    mt "Эта деревенщина не знает, что так орать на весь дом - неприлично..."
    mt "Что на этот раз?.. Эта Бетти с этим малявкой. Я уже даже не знаю, чего ожидать от них."
    mt "Когда же они все уже исчезнут из моего дома?.."
    # со спины
    music Hidden_Agenda
    img 14580
    with fade
    m "Да, миссис Робертс..."
    # Бетти, не поворачиваясь к Монике
    # Барди идет к кровата
    music Groove2_85
    img 14582
    with diss
    betty "Гувернантка, я тебя позвала, чтобы..."
    img 14583
    with diss
    betty "..."
    # Барди прыгает на кровать
    sound Jump1
    img 14581
    with diss
    w
    img 14584
    with fade
    betty "Хм. Барди, что ты там хотел? Давай, быстрее.!"
    music Sneaky_Snitch
    img 14585
    with diss
    bardie "Мне нужно проверить, насколько хорошо вы соблюдаете правила этого дома и..."
    img 14586
    with diss
    betty "И?"
    img 14587
    with diss
    bardie "... и запечатлеть это на свой телефон!"
    # Барди поворачивается к Монике и говорит
    img 14588
    with fade
    bardie "Начнем с тебя. Ты же хорошая гувернантка? Ты соблюдаешь правила?"
    # Моника в шоке, смотрит на него, как на больного
    music Power_Bots_Loop
    img 14589
    mt "Он совсем обнаглел!!!"
    mt "Эта малявка требует от меня, Моники Бакфетт, чтобы я согласилась задрать юбку!"
    mt "Задрать юбку перед каким-то малявкой, который будет снимать это на телефон! Который поселился в МОЕМ доме!!!"
    mt "!!!"
    img 14590
    with fade
    m "Я не буду делать этого! Да как ты смеешь?! В обязанности гувернантки не входит позировать в голом виде перед камерой!"
    music Groove2_85
    img 14591
    with diss
    bardie "А в обязанности хорошей гувернантки - входит. Ты же хорошая гувернантка?"
    # Моника смотрит зло
    img 14592
    m "!!!"
    img 14593
    with fade
    bardie "Или ты не соблюдаешь правила этого дома и хочешь получить штраф?"
    bardie "???"
    # Моника думает
    if monicaUnder != "Nude":
        music Hidden_Agenda
        img 14594
        with fade
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        # Моника убегает
        sound highheels_run2
        music Groove2_85
        img 14595
        with diss
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        return
    img 14594
    with diss
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            # Моника убегает
            sound highheels_run2
            music Groove2_85
            img 14595
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return
    img 14596
    with diss
    m "!!!"
    # Моника, срипя зубами соглашается, поднимает юбку, Барди фото не делает и смотрит на Бетти
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 14597
    with fadelong
    w
    img 14598
    with diss
    w
    img 14599
    with fade
    bardie "Бетти, а ты чего ждешь? Я хочу запечатлеть на фото вас вдвоем. Поднимай юбку!"
    # Бетти офигевает и начинает ор-р-р-рать
    music Power_Bots_Loop
    img 14600
    with hpunch
    betty "Если эта шлюха готова поднять юбку перед любым, даже перед моим приемным сыном..."
    betty "То я на такое никогда не соглашусь!"
    music Groove2_85
    img 14601
    with diss
    betty "!!!"
    # Бетти уходит, Моника продолжает держать юбку и смотрит ей вслед
    sound highheels_run2
    img 14602
    with fade
    betty "Я порядочная замужняя женщина и ты не смеешь требовать от меня такого!" #высокомерно
    bardie "Стой! Я с тобой еще не договорил! Ты куда?" # в этом же арте
    # кадр меняется на Барди
    music Sneaky_Snitch
    img 14603
    with diss
    bardie_t "Значит вот так?.. Значит, она у меня еще недостаточно под контролем."
    bardie_t "Окей... Я придумаю что-нибудь еще, помимо фоток с тренером."
    return

label gallery_14612:
    # Барди разговаривает нагло, отдает приказ
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(_("Утро..."))
    scene black_screen
    with Dissolve(1)
    music Sneaky_Snitch
    img 14604
    with fadelong
    w
    img 14605
    with diss
    bardie "Сегодня мой преподаватель вызывает к себе родителей..."
    # Бетти вопросительно
    img 14606
    with diss
    betty "???"
    # Поворачивается
    music Groove2_85
    img 14607
    with fade
    betty "А я здесь причем?"
    betty "Иди к Ральфу, скажи ему об этом."
    img 14608
    with diss
    bardie "Ты же моя приемная мать. Ты и сходишь в колледж. Отцу не обязательно об этом знать."
    bardie "У меня там небольшие проблемы: меня могут отчислить. Я хочу, чтобы ты уладила этот вопрос."
    img 14609
    with fade
    betty "В смысле, 'ты хочешь'?! Почему я должна идти в колледж и вообще тратить свое время на это?"
    img 14610
    with diss
    bardie "Потому что отцу не обязательно знать не только о том, что у меня проблемы в колледже, но и еще кое о чем..."
    bardie "О чем мы оба с тобой знаем."
    # Бетти зло смотрит
    img 14611
    betty "!!!"
    img 14612
    with fade
    bardie "Вот поэтому сегодня именно ТЫ пойдешь в колледж и сделаешь так, чтобы меня не отчислили!"
    # Бетти раздражена назойливостью Барди
    img 14613
    with diss
    betty_t "Чего эта малявка пристала ко мне?! Как бы поскорее отвязаться от него?"
    img 14614
    with diss
    betty "Это твои проблемы, разбирайся с этим сам!"
    img 14615
    with fade
    bardie "Это наша общая проблема! Так же, как и проблема того, что ты трахаешься со всеми подряд!"
    # Бетти, кипя от злости
    img 14616
    betty "!!!"
    img 14617
    with diss
    betty "Вообще-то, я верная жена! Не смей говорить обо мне такое!"
    # Барди в ответ смеется
    img 14618
    with fade
    bardie "Если хочешь, чтобы отец и дальше думал, что ты верная жена, делай, что я тебе говорю."
    bardie "И только попробуй не уладить вопрос моего отчисления. Тебе же хуже будет!"
    # Бетти убийственным взглядом смотрит на него и уходит
    img 14619
    betty "!!!"
    img 14620
    with fade
    bardie_t "Мне нужно будет убедиться, что она все сделает правильно. Надо за ней проследить!"
    return

label gallery_15076:
    # Барди стоит возле своего стола и улыбается, Бетти заходит к нему в комнату, возмущается
    music Groove2_85
    img 15072
    with fadelong
    betty "Ты, наверное, не понял, о чем я тебе говорила! Ты почему со мной так разговариваешь?!"
    betty "!!!"
    # Барди с улыбочкой указывает рукой на свой ноут
    music Sneaky_Snitch
    img 15073
    with fade
    bardie "Я позвал тебя, чтобы ты посмотрела мою коллекцию фотографий. За последние дни я сделал несколько очень интересных фоток."
    img 15074
    with diss
    betty "???"
    betty "Что за глупости?! Какое мне дело до твоих дурацких коллекций?"
    img 15075
    with fade
    bardie "Я уверен, что тебе понравится... Посмотри."
    # Бетти подходит к его столу и заглядывает в ноут, видит на фото себя с учителем и офигевает
    #sound звук клавиши
    sound keyboard
    img 15076
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15077
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15078
    with diss
    betty "!!!"
    #sound звук клавиши
    sound keyboard
    img 15079
    with diss
    w
    #sound звук клавиши
    sound keyboard
    img 15114
    with diss
    betty "ЧТО! ЭТО! ТАКОЕ?!"
    # Бетти бомбит
    music Power_Bots_Loop
    img 15080
    with fade
    betty "Ты что делаешь, сволочь!!!"
    betty "Я порядочная женщина! Что это за фотографии?!"
    betty "Как ты смеешь, мерзкий сопляк?! Я это сделала для тебя, а ты!.. Ты!!!"
    # Барди спокойно отвечает
    music Groove2_85
    img 15081
    with diss
    bardie "Я не просил тебя трахаться с ним. Ты даже в моем колледже нашла член, за который можно подержаться."
    bardie "На этих фото доказательство очередной измены моему отцу. Попробуй только сделать что-нибудь не так..."
    img 15082
    with diss
    bardie "..."
    bardie "Нууу, например, не слушаться меня... Эти фото сразу же увидит твой муж. И с того момента он станет уже твоим 'бывшем мужем'."
    # Бетти кипит от злости
    music Power_Bots_Loop
    img 15083
    betty_t "!!!"
    betty_t "Ненавижу! Да как он смеет?!"
    # Бетти смотрит на Барди убийственным взглядом
    img 15084
    with diss
    betty_t "Этот сопляк шпионил за мной! Он это все специально подстроил!"
    betty_t "!!!"
    music Hidden_Agenda
    img 15085
    with fade
    betty_t "Но я не могу позволить, чтобы Ральф увидел эти фотографии! Даже несмотря на то, что я это делала для его сына!"
    betty_t "..."
    # Бетти, злая, складывает руки на груди и спрашивает Барди
    music Groove2_85
    img 15086
    with diss
    betty "Чего тебе надо от меня?"
    img 15087
    with diss
    betty_t "Ненавижу этого сопляка!"
    img 15088
    with fade
    bardie "Так-то лучше."
    bardie "Помнишь, я хотел тебя сфотографировать с задранной юбкой? Ты мне отказала тогда..."
    bardie "Так вот..."
    # Бетти снова начинает орать
    music Power_Bots_Loop
    img 15089
    with fade
    betty "Да ты совсем охренел!"
    betty "НЕТ!"
    img 15090
    with diss
    betty "Ни за что!!! Я не буду фотографироваться так!"
    betty "!!!"
    # Барди с мерзкой улыбочкой
    music Groove2_85
    img 15091
    bardie "???"
    img 15092
    with diss
    bardie "Ты хорошо подумала?"
    img  15093
    with fade
    betty "..."
    # Барди показывает свой смартфон
    img 15094
    with diss
    bardie "Копии твоих фотографий с учителем есть у меня в телефоне. Отправить их отцу - вопрос нескольких секунд."
    img 15095
    betty "Ты не сделаешь этого!"
#    img 15096
    img 15097
    with diss
    bardie "Я уже делаю это."
    betty "!!!"
    # делает вид, что отправляет фотки, Бетти не выдерживает
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 15098
    with fade
    betty "Хорошо, твоя взяла... Я согласна... Но только одно фото и ты обещаешь, что никому его не покажешь!"
    betty "..."
    img 15099
    bardie "Естественно, не покажу. Это только для меня..."
    img 15100
    with diss
    bardie_t "... и моего одноклассника."
    bardie_t "Теперь он мне точно поверит!"
    # Бетти фыркает, психует, но подчиняется и задирает юбку, она в трусиках
    img 15101
    betty "Давай, быстрее!"
    # Барди ничего не делает и смотрит на нее вопросительно
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15102
    with fadelong
    w
    img 15103
    with diss
    bardie "..."
    music Groove2_85
    img 15104
    with fade
    bardie "Во-первых, почему ты в трусах?"
    # Бетти опускает юбку, смотрит возмущенно и зло, но молчит
    img 15105
    with diss
    bardie "Ты забыла, что должна соблюдать правила этого дома? Снимай их, быстро!"
    bardie "Во-вторых, позови гувернантку. Я хочу сфотографировать вас вдвоем."
    # Бетти опять бомбит
    music Power_Bots_Loop
    img 15106
    betty "Я не собираюсь фотографироваться с этой шлюхой!"
    betty "!!!"
    music Groove2_85
    img 15107
    with diss
    bardie "Ты сейчас снимешь свои трусы и позовешь гувернантку! Я жду!"
    # Барди садится на свою кровать и демонстративно показывает Бетти свой телефон. Бетти кипит от злости, но подчиняется
    img 15108
    with diss
    w
    sound Jump1
    img 14581
    with diss
    w
    img 15109
    with diss
    w
    img 15110
    with fade
    betty_t "Ненавижу этого сопляка!"
    # Бетти отворачивается от Барди, со злостью снимает трусики
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 15111
    with fadelong
    w
    img 15112
    with diss
    betty "!!!"
    # Бетти с напряженным лицом зовет Монику
    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 15113
    with hpunch
    betty "Гувернантка!!! Иди сюда!"
    # Барди самодовольно ухмыляется
    return

label gallery_15130:
    # Барди с телефоном в руках сидит на своей кровати, Бетти стоит в комнате Барди и недовольно кричит
    music Power_Bots_Loop
    img 15113
    with hpunch
    betty "Гувернантка!!!"
    # спустя несколько минут появляется Моникаg
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Groove2_85
    img 14579
    with fade
    mt "Она опять орет на весь дом..."
    mt "Что этой деревенщине снова от меня нужно?"
    img 14582
    with diss
    m "Да, миссис Робертс..."
    # Бетти и Моника стоят перед Барди, он сидит на кровати
    img 15115
    with fade
    betty "Гувернантка, я..."
    img 15116
    with diss
    betty "..."
    img 15117
    with fade
    bardie "Мне нужно проверить, насколько хорошо ты соблюдаешь правила этого дома и..."
    bardie "...сделать фото!"
    img 14589
    with diss
    mt "Он опять хочет фото?! Когда он уже отстанет от меня?!"
    img 15118
    with fade
    bardie "Давай, без лишних разговоров. Поднимай юбку!"
    # Моника зло смотрит на него
    music Power_Bots_Loop
    img 14592
    with diss
    m "Я не собираюсь фотографироваться с задранной юбкой!"
    m "Достаточно того, что ты при каждом удобном случае заглядываешь мне под юбку!"
    img 15119
    with diss
    mt "Мелкий озабоченный извращенец!"
    music Groove2_85
    img 15120
    with fade
    bardie "Гувернантка слишком много разговаривает!"
    bardie "Если ты хорошая гувернантка и соблюдаешь правила, то делай, что тебе говорят!"
    img 14592
    with diss
    m "..."
    # Барди с угрозой
    img 15121
    with fade
    bardie "Или ты отказываешься и хочешь, чтобы я тебя наказал?"
    img 14594
    with diss
    mt "!!!"
    mt "Ненавижу эту малявку! И эту чокнутую деревенщину Бетти!"
    mt "Когда этот дом снова станет моим, я возьму ее к себе гувернанткой. Будет работать у меня за еду."
    mt "!!!"
    # Моника смотрит зло, Бетти все это время стоит с каменным лицом
    img 14588
    with fade
    m "Зачем тебе нужна эта фотография?"
    img 15122
    with diss
    bardie "Гувернантку это не касается! Поднимай юбку!"
    # Барди поднимает руку с телефоном, чтобы сделать фото
    mt "..."
    if monicaUnder != "Nude":
        img 14594
        with diss
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        sound highheels_run2
        img 14595
        with fade
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        return
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            sound highheels_run2
            img 14595
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return
    # Моника, срипя зубами соглашается, поднимает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14598
    with fadelong
    w
    img 15123
    with diss
    w
    music Groove2_85
    img 15124
    with fade
    bardie "Хорошая гувернантка."
    # Барди фото не делает и смотрит на Бетти
    img 15125
    with diss
    bardie "Бетти?.."
    img 15126
    betty "!!!"
    # Бетти фыркает, психует, но подчиняется и задирает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15127
    with fadelong
    w
    img 15128
    with diss
    w
    img 15129
    with diss
    betty "Давай, быстрее!"
    betty "Только одно фото!"
    w
    call photoshop_flash()
    w
    # Барди с довольным видом делает фотку
    img 15130
    with diss
    betty "Все?"
    bardie "Подождите, что-то не получилось фото. Ну-ка еще раз."
    w
    call photoshop_flash()
    w
    # Барди делет еще несколько кадров
    img 15131
    with diss
    w
    call photoshop_flash()
    w
    img 15132
    with diss
    w
    call photoshop_flash()
    w
    img 15133
    with diss
    betty "Все! Хватит!"
    w
    call photoshop_flash()
    w
    # Бетти опускает юбку, Моника следом за ней
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 14584
    with fadelong
    betty "Надеюсь, ты доволен?"
    img 14585
    with diss
    bardie "Очень! Вы обе доказали мне, что соблюдаете правила этого дома."
    bardie "..."
    img 14587
    with diss
    bardie "Моему однокласснику точно понравится!"
    # Бетти с Моникой офигевают
    music Power_Bots_Loop
    img 15134
    with hpunch
    mt "!!!"
    betty "!!!"
    # Бетти начинает орать, Моника зло смотрит
    img 15135
    with fade
    betty "ЧТООООО?!!"
    betty "Какому еще однокласснику?!"
    # Барди нагло
    music Groove2_85
    img 15136
    with diss
#    if ep28_monica_eric_meeting_completed == False:
    bardie "Ах да... Вы же еще не знакомы... Я скоро приглашу его в гости."
#    else:
#        bardie "Ах да... Ты еще с ним не знакома... В отличие от гувернантки."
    img 15119
    with diss
    mt "Он совсем обнаглел! Ненавижу эту малявку!"
    mt "И почему у этой деревенщины не хватает мозгов, чтобы приструнить его?!"
    music Power_Bots_Loop
    img 15137
    with fade
    betty "Нет!!! Не смей! Ты говорил, что это фото никто не увидит!"
    betty "!!!"
    music Groove2_85
    img 14587
    with diss
    bardie "Я так сказал?! Хм... Никто, кроме моего одноклассника."
    bardie "Аха-ха!"
    music Power_Bots_Loop
    img 15138
    with fade
    betty "Да как ты смеешь так обращаться со мной, порядочной женщиной?! Сопляк!"
    betty "Я - жена твоего отца! А ты собираешься показываеть фото, где я голая, да еще и с этой шлюхой, своему однокласснику!!!"
    img 15139
    with diss
    mt "Ненавижу эту семейку! Когда она будет моей гувернанткой, я ее уволю!"
    mt "!!!"
    music Groove2_85
    img 15140
    with fade
    bardie "Если ты и дальше будешь со мной так разговаривать, то женой моего отца ты будешь недолго..."
    bardie "Ты забыла, что у меня есть много фото, интересных фото...?"
    img 15141
    with diss
    bardie "И в интересной компании..."
    bardie "???"
    # Бетти смотрит испепеляющим взглядом, но молчит
    img 15142
    betty "!!!"
    img 15143
    with diss
    mt "Хм. Кто из нас после этого шлюха?"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 15144
    with fade
    bardie "Вы на сегодня свободны. Можете идти."
    return

label gallery_15147: # если ушла от учителя
    # Моника заходит в комнату Барди, тот сидит на кровати, залипнув в телефон
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 15145
    with fadelong
    w
    img 15146
    with diss
    mt "Ненавижу эту малявку! Он меня достал уже со своими глупостями!"
    # Барди вопросительно смотрит на нее
    img 15147
    with fade
    bardie "Ну как сходила, гувернантка? Надеюсь, у тебя все получилось уладить?"
    # Моника недовольно
    img 15148
    with diss
    m "Если бы твой друг включил мозг, когда надумал залезть в шкафчик мисс Мэнсфилд. То проблем бы никаких не было."
    # Барди смотрит на Монику
    img 15149
    with fade
    bardie "И? Проблема решена?"
    # Моника орет
    music Power_Bots_Loop
    img 15150
    m "Нет! И я не собираюсь заниматься этими глупостями!"
    m "Я не пойду больше в этот твой чертов колледж! Разбирайтесь сами!"
    # Барди угрожающе
    music Groove2_85
    img 15151
    with fade
    bardie "Гувернантка забыла, что Эрик делает хозяину домашку?"
    music Power_Bots_Loop
    img 15152
    m "Да какое мне дело до этого?!" #возмущенно
    m "Пусть сам решает свои проблемы!!!"
    music Groove2_85
    img 15153
    with fade
    bardie "Гувернантка плохая! Ее надо наказать!"

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(_("5 минут спустя..."))
    img black_screen
    with Dissolve(2.0)
    music Groove2_85

    if monicaUnder != "Nude":
        sound snd_fabric1
        if monicaBettyPanties == False:
            if monicaUnder != "Nude":
                img 10272
        else:
            if monicaBettyPantiesId == 1:
                #betty
                img 10273
            if monicaBettyPantiesId == 2:
                img 10274
            if monicaBettyPantiesId == 3:
                img 10275
            if monicaBettyPantiesId == 4:
                img 10276
            if monicaBettyPantiesId == 5:
                img 10277
        with fadelong
        bardie "Покажи мне, как хорошо ты соблюдаешь правила этого дома!"
        sound snd_fabric1
        if monicaBettyPanties == False:
            if monicaUnder != "Nude":
                #governess
                img 10292
                with diss
                w
                img 10293
                with diss
                w
        else:
            if monicaBettyPantiesId == 1:
                #betty
                img 10295
                with diss
                w
                img 10294
                with diss
                w
                img 10305
                with diss
                w
        #
            if monicaBettyPantiesId == 2:
                img 10296
                with diss
                w
                img 10297
                with diss
                w
                img 10306
                with diss
                w
        #
            if monicaBettyPantiesId == 3:
                img 10299
                with diss
                w
                img 10298
                with diss
                w
                img 10307
                with diss
                w
        #
            if monicaBettyPantiesId == 4:
                img 10300
                with diss
                w
                img 10301
                with diss
                w
                img 10308
                with diss
                w
        #
            if monicaBettyPantiesId == 5:
                img 10303
                with diss
                w
                img 10302
                with diss
                w
                img 10304
                with diss
                w
    else:
        img 10281
        with fadelong
        bardie "Покажи мне, как хорошо ты соблюдаешь правила этого дома!"
    img 10309
    with fade
    w
    img 10310
    with fade
    w
    img 10311
    with fade
    mt "Ненавижу его!"
    img 10312
    with fade
    w
    img 10313
    with fade
    mt "Он меня этим не напугает и не заставит идти к учителю!"
    img 10314
    with fade
    w
    img 10315
    with fade
    mt "Он все равно не добьется своего!"
    img 10316
    with fade
    w
    img 10317
    with fade
    mt "Я не пойду в этот чертов колледж! Я не хочу!!!"
    img 10318
    with fade
    w
    img 10319
    with fade
    w


label gallery_15147_1:
    # Барди шлепает Монику

    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_1 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_1.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_1
    wclean
    stop music

    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_2 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_2.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_2
    bardie "Гувернантка ослушалась приказа хозяина!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_3 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_3.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_3

    bardie "Получай!"
    bardie "Плохая гувернантка!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_4 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_4.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_5 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_5.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_5
    bardie "Гувернантка поняла, что вела себя плохо?"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_6 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_6.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_6
    bardie "Гувернантка больше не будет так делать и выполнит все, что скажет хозяин?"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_7 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_7.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_7
    bardie "Гувернантка должна пойти в колледж и решить проблему Эрика!"
    wclean
    stop music

    music Power_Bots_Loop
    mt "Черт! Как больно! Когда он уже остановится?!"
    menu:
        "Отпусти меня немедленно, малявка!":
            img 10320
            with fade
#            m "!!!"
            m "Я хорошая гувернантка!"
            m "Но я не пойду в колледж!"
            m "Отпусти меня немедленно, малявка!"
#            mt "Нет! Я не пойду туда больше!"
            jump gallery_15147_1
        "Я поняла! Я буду слушаться хозяина!":
            pass


    music Groove2_85
    img 10321
    with fade
    m "Я поняла! Я буду слушаться хозяина!"
    img 10322
    with fade
    m "Я хорошая гувернантка! Я поговорю с учителем еще раз!"
    img 10323
    with fade
    bardie "Так-то лучше!"
    img 10324
    with diss
    bardie "Если будешь себя снова плохо вести, получишь еще!"
    img 10325
    with fade
    bardie "Гувернантка, можешь продолжать работать..."
    bardie "Ты мне пока не нужна."

    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Pyro_Flow
    img 10326
    with fadelong
    mt "Не могу поверить!"
    mt "Этот малявка отшлепал меня словно я маленький ребенок!"

    #Если повтор
    if bardieMonicaPunishmentCount > 1:
        img 10327
        with fade
        mt "И уже не первый раз!!!"
        #
        img 10327
        mt "В моем же доме!"
        mt "Отшлепали! Меня!!!"
        mt "Монику Бакфетт!!!"
        #

    img 10328
    with fade
    mt "У меня попа горит!"
    img 10329
    with diss
    mt "Что этот Барди себе позволяет?!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 10330
    with fadelong
    mt "Как унизительно!"
    mt "Мне надо как-то избавиться от него!"


#    img 14596
#    m "!!!" # зло смотрит на него
#    img 15154
#    mt "Надеюсь, после этого он, наконец, отстанет от меня."
    # поднимает юбку БАРДИ НАКАЗЫВАЕТ МОНИКУ - ШЛЕПАЕТ ПО ПОПЕ
#    bardie "Гувернантка ослушалась приказа хозяина!"
#    bardie "Плохая гувернантка!"
#    bardie "Гувернантка поняла, что вела себя плохо?"
#    bardie "Гувернантка больше не будет так делать и выполнит все, что скажет хозяин?"
#    bardie "Гувернантка должна пойти в колледж и решить проблему Эрика!"


    return

label gallery_22069:
    music stop
    img black_screen
    with diss
    pause 2.0
    # через несколько минут Моника заходит к нему в комнату, смотрит на Эрика, тот заинтересованно смотрит на нее
    music Groove2_85
    img 15254
    with fadelong
    mt "Этот малявка привел в дом еще одного такого же озабоченного мелкого извращенца, как он сам."
    # переводит взгляд на Барди
    img 15255
    with diss
    m "Да? Ты звал меня?"
    # Барди с серьезным лицом говорит Монике
    img 15256
    bardie "Гувернантка, мне надо проверить, соблюдаешь ли ты правила этого дома!"
    music Power_Bots_Loop
    img 15257
    with hpunch
    m "Что, прямо сейчас? При твоем друге?!" # удивленно
    m "???"
    # Барди все с такой же серьезной миной
    music Groove2_85
    img 15258
    with fade
    bardie "Да, мне нужно проверить прямо сейчас, гувернантка."
    # Моника зло
    img 15259
    with diss
    m "В мои обязанности это не входит! Я не собираюсь проходить эту проверку при твоем друге!"
    m "!!!"
    # Барди с угрозой
    img 15260
    with fade
    bardie "Если ты хорошая гувернантка и соблюдаешь правила, то делай, что тебе говорят!"
    img 15261
    with diss
    m "..."
    img 15262
    with fade
    bardie "Или ты отказываешься и хочешь, чтобы я тебя наказал?"
    # Моника злится, но молчит
    img 15263
    with diss
    mt "!!!"
    mt "Ненавижу эту малявку!"
    img 15264
    with fade
    bardie "Ну? Я долго должен ждать?"
    if monicaUnder != "Nude":
        img 15265
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        img 15266
        with fade
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        music stop
        img black_screen
        with diss
        sound highheels_run2
        pause 2.0
        return
    img 15267
    with diss
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            img 15266
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 2.0
            return
    # Моника с недовольным лицом задирает юбку, Эрик сидит офигевший и пялится на нее, Барди самодовольно ему говорит
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15268
    with fadelong
    w
    img 15270
    with diss
    bardie "Ну что? Теперь ты убедился, что я не врал?"
    img 15269
    with diss
    eric "..."
    music Groove2_85
    img 15271
    with fade
    bardie "Я выиграл спор! С тебя домашка на месяц вперед!"
    # Моника опускает юбку, недовольно смотрит на Барди
    img 15272
    with diss
    mt "Они спорили на домашку? Детский сад!"
    mt "Теперь он, наконец, отвяжется от меня?"
    # Эрик продолжает пялиться на Монику
    img 15273
    with fade
    eric "Н-нет..."
    # Барди и Моника вопросительно смотрят на Эрика
    img 15274
    with diss
    bardie "Что 'нет'? Мы с тобой договаривались!"
    img 15275
    with fade
    eric "Я... Хм... Спор не выигран."
    eric "Потому что я... Я не рассмотрел..."
    img 15276
    with diss
    m "Что значит 'не рассмотрел'?! Я все сделала, как сказал Барди."
    # Эрик смотрит на юбку Моники, но обращается к Барди
    img 15277
    with fade
    eric "Если твоя гувернантка задерет юбку еще раз и... даст посмотреть поближе, тогда я буду делать тебе домашку 2 месяца."
    # Моника офигевает
    music Power_Bots_Loop
    img 15278
    with hpunch
    mt "!!!"
    mt "Эти две малявки спорят на какую-то глупость! А я должна тут стоять перед ними полуголая!!!"
    # Барди поворачивается к Монике и смотрит вопросительно, Моника смотрит на него зло, но ничего не делает
    music Groove2_85
    img 15279
    with fade
    bardie "Чего ты ждешь, гувернантка? Ты не слышала что-ли? Подойди поближе к нам и подними юбку еще раз!"
    img 15272
    with diss
    mt "Ненавижу эту малявку! И его озабоченного друга!"
    mt "Если я этого не сделаю, он не отвяжется от меня."
    img 15280
    with fade
    bardie "Я жду."
    # Моника подходит ближе к  Эрику, и снова задирает юбку, Эрик с тупым выражением лица пялится на ее киску
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15281
    with fadelong
    w
    img 15282
    with diss
    w
    img 15283
    with diss
    eric "Я... Я вообще ничего не могу рассмотреть."
    # Барди смотрит на Монику, Моника взглядом готова убить Эрика
    img 15284
    with fade
    bardie "Гувернантка, расставь ноги шире!"
    # Моника зло смотрит на него, но подчиняется и ставит ноги шире
    img 15285
    mt "!!!"
    # Моника снова испепеляет взглядом Эрика, а он пристально разглядывает
    img 15286
    with fade
    w
    img 15287
    with diss
    w
    img 15288
    with diss
    w
    music Groove2_85
    img 15289
    with fade
    eric "Я хочу увидеть еще ближе. Пусть твоя гувернантка сядет на кровать. Тогда я смогу все рассмотреть."
    # Моника злится
    img 15291
    m "!!!"
    img 15290
    with diss
    menu:
        "Сесть на кровать.":
            pass
        "Отказаться. Эти малявки совсем обнаглели!":
            music Power_Bots_Loop
            img 15292
            with fade
            m "Я не буду этого делать! Все итак слишком далеко зашло!!!"
            # Барди угрожающе
            img 15293
            with diss
            bardie "Гувернантка не хочет быть хорошей? Она забыла, что может сделать хозяин, если она не будет слушаться его?"
            img 15272
            with diss
            mt "Черт!"
            img 15294
            with diss
            m "..."
            music Groove2_85
#            return 1
    # Моника садится на край кровати, а Барди и Эрик смотрят на нее
#    img 15295
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22048
    with fadelong
    w
    img 22049
    with diss
#    img 15296
    bardie "Подними юбку."
    # Моника слушается
#    img 15297
    img 22050
    with diss
    m "!!!"
#    img 15298
    sound snd_fabric1
    img 22051
    with diss
    w
    img 22052
    with diss
    w
    img 22053
    with diss
    bardie "Раздвинь ноги."
    img 22054
    w
    # Моника раздвигает их, совсем немного
    img 22055
    with fade
    w
    img 22056
    with diss
    w
    img 22057
    with diss
    w
    img 22058
    with fade
    w
    img 22059
    with diss
    bardie "Eще шире! Ему же ничего не видно так."
    # Барди с Эриком внимательно смотрят, Моника подчиняется
    img 22060
    mt "Я когда-нибудь задушу эту мерзкую малявку! И почему он прицепился именно ко мне, а не к Бетти?!"
    img 22061
    with diss
    mt "!!!"
    img 22062
    with fade
    w
    img 22063
    with diss
    w
    # Эрик наклоняется над кроватью близко от киски Моники и разглядывает ее в упор
    sound Jump1
    img 22064
    with diss
    w
    img 22065
    with diss
    w
    m "!!!"
    music Loved_Up
    img 22066
    with fade
    eric "Чувак, я видел в порно, как лижут киски и всегда хотел попробовать. Ты же не против?"
    # Барди удивленно смотрит на него
    img 22067
    with diss
    bardie "???"
    music Groove2_85
    img 22068
    with fade
    bardie "Окей."
    # Моника возмущается
    img 22069
    with diss
    m "Какого черта?! А меня ты не хочешь спросить? Я не хочу, чтобы ты ко мне прикасался!"
    # Барди, смотря не на нее, а на киску
    img 22070
    with fade
    bardie "Он только потрогает языком и не будет больше ничего делать."
    bardie "Зато за хозяина будут делать домашние задания целых два месяца."
    img 22071
    with diss
    bardie "Хорошая гувернантка должна быть рада пойти на такие маленькие жертвы ради своего хозяина."
    img 22072
    with fade
    mt "Какой ужас! Мне что, приходится раздвигать ноги перед кем-то ради домашних заданий этого сопляка?"
    mt "Мне?! Монике Бакфетт! Самой богатой и влиятельной женщине этого города!"

    # Моника негодует, но продолжает сидеть с развинутыми ногами
    label gallery_22079:
    music Power_Bots_Loop
    img 22073
    with hpunch
    m "Только попробуй коснуться меня там пальцами или чем-либо еще!"
    m "!!!"
    music Groove2_85
    img 22074
    with fade
    bardie "Да, Эрик! Не трогай ее там пальцами или чем-то еще. Это МОЯ гувернантка."
    bardie "Не забывай это!"
    # Эрик все это время глаз не отводит от ее киски
    music Loved_Up
    img 22075
    with diss
    eric "..."
    # лицо Эрика все ближе к киске Моники, на лице Моники отвращение
    music Groove2_85
    img 22076
    with fade
    mt "Фу, как это мерзко! Но если я не послушаюсь Барди..."
    mt "Я тогда остановила его прямо в полиции. Еще несколько минут и он был бы у Маркуса."
    mt "Боже! Даже боюсь думать о последствиях."
    mt "У меня сейчас нет другого выхода, кроме того, как перетерпеть эту мерзость."
    # Эрик высовывает свой язык и касается им киски Моники
#    music Loved_Up
    #видео erick licking monica
    music v_Monica_Eric_Licking_1_1
    img 22079
    with diss
    w
    img 22077
    with diss
    w
    img 22078
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Licking_1_1 = Movie(play="video/v_Monica_Eric_Licking_1_1.mkv", fps=30)
    show videov_Monica_Eric_Licking_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Licking_1_2 = Movie(play="video/v_Monica_Eric_Licking_1_2.mkv", fps=30)
    show videov_Monica_Eric_Licking_1_2
    with fadelong
    wclean
#    music v_Monica_Eric_Licking_1_1
    img 22080
    with diss
    w
    img 22082
    with diss
    w
    img 22081
    with diss
    mt "По крайней мере, это не так неприятно как я думала."
    mt "Но это все-равно отвратительно!"
    mt "Когда же он уже закончит все это?!"
    music Groove2_85
    img 22083
    with fade
    bardie "Эй, чувак! У нас точно все в силе? Ты мне будешь делать домашку?"
    music Turbo_Tornado
    img 22084
    with diss
    eric "Да буду, буду!"
    # тут Эрик присасывается к Монике, Барди в шоке смотрит на это
    sound Jump2
    #sound звук эрик присосался к Монике
    img 22085 # присосался
    with hpunch
    w
    img 22086
    with diss
    m "!!!"
    img 22087
    with diss
    bardie "Эй-эй, чувак. Полегче..."
    # Эрик делает еще несколько движений языком и поворачивается к Барди
    img 22088
    with fade
    eric "Лизать самому намного прикольнее, чем просто смотреть на это!"
    eric "А ты пробовал?"
    img 22089
    with diss
    bardie "Не, даже не думал об этом."
    img 22090
    with fade
    eric "Давай, чувак, попробуй."
    img 22091
    with diss
    bardie "Прямо сейчас?"
    eric "Ага. Это правда прикольно."
    # Барди смотрит на Монику, та на него смотрит испепеляющим взглядом, но молчит
    img 22092
    with diss
    bardie "..."
    img 22093
    with diss
    m "!!!"
    img 22095
    with diss
    w
    sound plastinka1b
    music stop
    img 22094
    with diss
    m "!!!"
    # Эрик отстраняется от Моники, Барди наклоняется к ней
    music Sneaky_Snitch
    img 22096
    with fade
    bardie_t "Хм. Надо хотя бы разочек попробовать, каково это лизать киску."
    img 22097
    with diss
    bardie_t "..."
    # наклоняется еще ближе и проводит языком, лицо Эрика совсем близко и когда Барди останавливается и поднимает голову, то тоже проводит языком
    label gallery_22113:
    music Groove2_85
    img 22098
    with fade
    bardie "Хорошая гувернантка поднимает юбку!"
    sound Jump1
    img 22099
    with diss
    w
    img 22100
    with diss
    w
    img 22101
    m "!!!"
    img 22102
    with fade
    bardie "Плохая гувернантка будет наказана штрафом..."
    menu:
        "Сделать что говорит Барди.":
            pass
    img 22103
    with diss
    mt "Какой кошмар! Что эти озабоченные малявки творят?!"
    sound snd_fabric1
    img 22104
    with fade
    mt "Что вообще у них в голове творится? Как можно было до такого додуматься?"
    img 22105
    with diss
    w
    mt "!!!"
    img 22106
    with diss
    w
    mt "Почему я должна это терпеть?!"
    music stop
    img black_screen
    with diss
    pause 1.5
#    music Loved_Up
    music v_Monica_Eric_Bardie_Licking_1_1
    img 22107
    with fadelong
    w
    #видео monica eric bardie licking
    img 22108
    with diss
    mt "Черт! Как же щекотно..."
    img 22109
    with diss
    w
    img 22110
    with diss
    w
    img 22111
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Bardie_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Bardie_Licking_1_1 = Movie(play="video/v_Monica_Eric_Bardie_Licking_1_1.mkv", fps=30)
    show videov_Monica_Eric_Bardie_Licking_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Bardie_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Bardie_Licking_1_2 = Movie(play="video/v_Monica_Eric_Bardie_Licking_1_2.mkv", fps=30)
    show videov_Monica_Eric_Bardie_Licking_1_2
    with fadelong
    wclean
    music v_Monica_Eric_Bardie_Licking_1_1
    img 22112
    with diss
    mt "..."
    img 22113
    with diss
    w
    img 22114
    with diss
    sound ahhh11
    mt "Странные ощущения какие-то..."
    img 22115
    with diss
    w

    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    img 22116
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    eric "Ааааааа..."

    sound bulk1
    img 22117
    sound man_moan6
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    eric "Ааааааахххх!!!"
    # парни в это время продолжают лизать, сначала один, потом его сменяет другой. Эрик достает свой член из штанов
    # Эрик смотрит, как лижет Барди, проводит по своему члену рукой пару раз и кончает
    # Барди видит это и делает то же самое со своим членом, и кончает на живот Моники
    img 22118
    with diss
    m "Эй, что ты делаешь?! Фуууу!!!"
    img 22120
    with diss
    m "Не смей!"
    sound bulk1
    img 22119 # звук кончания
    sound man_moan1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    #sound звук спермы на живот
    sound hlup2
    img 22121 # прилетает сперма Монике на живот
    with diss
    w
    img 22122
    with diss
    mt "!!!"
    # Моника сдвигает ноги и опускает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 22123
    with fadelong
    mt "Наконец-то, это закончилось!"
    # вопросительно смотрит на Барди, тот расслаблен и доволен
    img 22124
    with diss
    bardie "Гувернантка хорошая. Гувернантка помогла хозяину выиграть спор."
    img 22125
    mt "!!!"
    # смотрит на Эрика
    img 22126
    with fade
    bardie "Эй, чувак, что там с домашкой?"
    # Эрик тоже расслаблен и доволен
    eric "Окей. Ты выиграл два месяца домашки."
    # Барди радостный, поворачивается к Монике
    sound highheels_run2
    img 22127
    with diss
    bardie "Можешь идти, гувернантка. На сегодня ты свободна."
    music stop
    img black_screen
    with diss
    pause 1.5
    return

label gallery_22180:
    # Барди на кровати, Бетти стоит напротив него и недовольно на него смотрит
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 22128
    with fadelong
    betty "Зачем ты меня звал? У меня нет времени на твои глупости!"
    img 22129
    with diss
    betty "Давай быстрее!"
    # Барди с мерзкой улыбочкой
    img 22130
    with fade
    bardie "Зови гувернантку. Я хочу проверить, как вы соблюдаете правила этого дома."
    img 22131
    betty "!!!"
    img 22132
    with diss
    betty "А сам проверить не можешь?!"
    betty "Я не хочу звать ее! А тем более при ней показывать, что я соблюдаю правила!"
    # Барди с фейсом а-ля хозяин дома
    img 22133
    with fade
    bardie "Ты, наверное, забыла, что я тут хозяин?!"
    bardie "Ты должна меня слушаться! Зови гувернантку!!!"
    # Бетти с недовольным лицом орет
    img 22131
    betty "!!!"
    music stop
    img black_screen
    with diss
    pause 1.0
    music Power_Bots_Loop
    img 22134
    with hpunch
    betty "Гувернантка! Иди сюда!"
    # через несколько минут в комнату заходит Моника, они вдвоем стоят перед кроватью Барди
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Hidden_Agenda
    img 22135
    with fadelong
    m "Да, миссис Робертс?" #недовольно
    music Power_Bots_Loop
    img 22136
    with diss
    mt "Эта деревенщина с малявкой уже меня достали!"
    mt "Что бы такого придумать, чтобы они от меня отстали?"
    music Hidden_Agenda
    img 22137
    with fade
    mt "???"
    # Бетти смотрит на Монику высокомерно
    betty "Гувернантка, я тебя позвала, чтобы..."
    betty "Чтобы..."
    # поворачивается к Барди
    img 22138
    with diss
    betty "..."
    music Groove2_85
    img 22139
    with fade
    bardie "Гувернантка, я хочу проверить, насколько хорошо вы соблюдаете правила этого дома."
    img 22140
    with diss
    bardie "И как хорошо слушаетесь хозяина."
    # Моника зло смотрит на Бетти
    img 22141
    with diss
    mt "Эта провинциальная шлюха могла бы поставить сопляка на место..."
    mt "Если бы была в состоянии говорить 'нет' мужчинам..."
    # Моника поворачивается к Барди
    img 22142
    with fade
    m "Что мне надо сделать? Задрать юбку?"
    img 22143
    with diss
    bardie "Ага. Но не прямо сейчас. Сначала я хочу проверить Бетти."
    img 22144
    with diss
    mt "???"
    betty "!!!"
    # Барди встает с кровати, улыбаясь многозначительно, говорит Бетти
    music stop
    img black_screen
    with diss
    pause 1.5
    sound Jump1
    music Groove2_85
    img 22145
    with diss
    bardie "Сядь на мою кровать."
    # Бетти офигевает
    music Power_Bots_Loop
    img 22146
    with fade
    betty "А это еще зачем?! Что ты еще придумал, сопляк?"
    img 22147
    with diss
    # Барди угрожающе
    bardie "Ты не хочешь слушать то, что говорю тебе я?"
    # Бетти психует, злится
    music Groove2_85
    img 22148
    with fade
    betty "..."
    betty_t "Ненавижу этого сопляка!!!"
    # но выполняет его приказ и садится на край его кровати
    img 22149 # садится
    with diss
    w
    img 22150
    betty "!!!"
    img 22151
    with fade
    bardie "А теперь я проверю, как ты соблюдаешь правила. Покажи мне. Разведи ноги в стороны и подними юбку."
    # Бетти зло на него смотрит
    img 22152
    with diss
    w
    music Power_Bots_Loop
    img 22153
    betty "Я не хочу делать этого при гувернантке! Вообще-то, на мне нет трусиков!"
    img 22154
    with diss
    betty "!!!"
    img 22155
    with diss
    betty "Я не собираюсь сидеть тут перед вами с раздвинутыми ногами!"
    # Барди ей показывает рукой на свой ноут
    music Groove2_85
    sound Jump1
    img 22156
    with fade
    bardie "Давай, еще раз посмотрим на твои фото?"
    img 22157
    with diss
    bardie "Возможно, ты забыла, что там отлично видно, как ты мастерски ведешь переговоры, с раздвинутыми ногами?"
    music Power_Bots_Loop
    img 22158
    with hpunch
    betty "Не смей такое говорить про меня! Я порядочная женщина!"
    music Groove2_85
    img 22159
    with fade
    bardie "Тогда делай, как я говорю! Порядочные женщины должны слушаться хозяина дома!"
    img 22160
    with diss
    bardie "Я жду!"
    # Бетти зло смотрит, но подчиняется, поднимает юбку, раздвигает ноги (далее она их раздвинет еще шире, см.ниже)
    img 22161
    with diss
    betty "!!!"
    # Барди смотрит на нее
    music stop
    img black_screen
    with diss
    pause 1.5
    sound snd_fabric1
    music Groove2_85
    img 22162
    with fade
    w
    img 22163
    with diss
    w
    img 22164
    with fade
    bardie "Хорошо. Так и сиди, не опускай юбку."
    img 22165
    with hpunch
    bardie "Сейчас я буду проверять гувернантку."
    # Барди поворачивается к Монике
    img 22166
    with fade
    bardie "Гувернантка, встань на пол на колени между ног Бетти!"
    # Моника офигевает
    music Power_Bots_Loop
    img 22167
    with diss
    m "ЧТО?!"
    m "Я не буду этого делать!!!"
    m "Проверяй как обычно!"
    # Барди недовольно
    music Groove2_85
    img 22168
    with fade
#    bardie "Ты плохая гувернантка. Ты отказалась принять благодарность моего друга."
    bardie "Ты плохая гувернантка."
    bardie "Плохую гувернантку хозяин должен наказать!"
    # Барди угрожающе
    img 22169
    with diss
    bardie "Если не сделаешь, как я говорю, то тебе будет только хуже!"
    # Моника зло на него смотрит
    music Power_Bots_Loop
    img 22170
    with fade
    mt "Он снова угрожает мне Маркусом..."
    mt "Ему же ничего не стоит пойти в полицию и сказать, что я живу здесь!"
    img 22171
    with diss
    mt "..."
    mt "Он расскажет..."
    mt "Полицейские будут здесь в тот же день..."
    mt "Возможно, даже завтра..."
    img 22172
    with diss
    mt "Нет! Я не должна допустить этого!!!"
    music Groove2_85
    img 22173
    with fade
    mt "!!!"
    # Моника с недовольным видом встает на колени перед Бетти
    # Барди самодовольно улыбается
    sound Jump1
    img 22174
    with diss
    w
    img 22175
    with diss
    w
    img 22176
    with diss
    w
    img 22177
    with fade
    bardie "Бетти, откинься назад, на кровать."
    img 22178
    with diss
    bardie "Гувернантка, наклонись и дотронься языком до киски Бетти."
    # Моника смотрит на него уничтожающим взглядом, а Бетти возмущается
    music Power_Bots_Loop
    img 22179
    with hpunch
    betty "Я не хочу, чтобы эта шлюха прикасалась своими губами ко мне!" #говорит она Барди
    img 22180
    with diss
    betty "Гувернантка, не смей прикасаться ко мне!" #говорит Монике
    # Моника зло
    img 22181
    with fade
    mt "Они издеваются?! Меня тошнит от того, что он просит сделать!"
    mt "И кому?! Этой деревенщине! Я, Моника Бакфетт!"
    img 22182
    with diss
    w
    img 22183
    with diss
    w
    music Groove2_85
    img 22184
    with fade
    w
    img 22185
    with diss
    w
    # Моника с ненавистью смотрит на Бетти, потом с отвращением приближается к ее киске и проводит языком
    img 22186
    with diss
    w
    img 22187
    with diss
    w
    img 22188
    with diss
    w
    img 22189
    with diss
    w
    img 22190
    with diss
    w
    img 22191
    with diss
    w
    img 22192
    with diss
    w
    #sound Моника прикасается языком к киске Бетти
    sound lick3
    img 22193
    with diss
    w
    img 22194
    with diss
    betty "Фууу!"
    # Моника отстраняется все с тем же отвращением, смотрит на Барди
    sound Jump1
    music Power_Bots_Loop
    img 22195
    with fade
    m "!!!"
    img 22196
    with diss
    m "Надеюсь, это все?! Я могу идти?"
    bardie "Нет, гувернантка! Я тобой очень недоволен!"
    bardie "Сделай так еще несколько раз, а я подумаю, достаточно или нет."
    # Моника снова с отвращением прикасается к Бетти и лижет ей там, Бетти злится, смотрит на Барди
    label gallery_22199:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22197
    with fadelong
    w
    img 22198
    with diss
    w
    #sound Моника прикасается языком к киске Бетти
    sound lick3
    img 22199
    with diss
    w
    img 22200
    with diss
    betty "Когда весь этот цирк прекратится?!"
    img 22201
    with diss
    betty_t "Фу! Эта шлюха согласилась лизать меня ТАМ!"
    betty_t "Как же это противно, что она ко мне прикасается!"
    img 22202
    with fade
    bardie "Гувернантка, еще не все."
    bardie "Продолжай. Я еще думаю, простить тебя или нет..."
    #sound Моника прикасается языком к киске Бетти
    sound lick3
    img 22203
    with diss
    w
    music Loved_Up
    img 22204
    with diss
    betty_t "Как же это противно... М-м-м-мне совсем это не нравится... Мммм..."
    #sound Бетти произносит Аааааааххх
    sound ahhh1
    img 22205
    with diss
    betty "Ааааааххх..."
    # Бетти раздвигает ноги еще шире, сама смотрит на Барди
    img 22206
    with diss
    betty "Все, хватит, достаточно! Мне неприятно, что она трогает меня там-м-м..."
    #sound Моника лижет киску Бетти обычно
    sound lick10
    img 22207
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.66666667)) + " loop 0.0>Sounds/v_Monica_Betty_Licking_1_1.ogg"
    scene black
    image videov_Monica_Betty_Licking_1_1 = Movie(play="video/v_Monica_Betty_Licking_1_1.mkv", fps=30)
    show videov_Monica_Betty_Licking_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.66666667)) + " loop 0.0>Sounds/v_Monica_Betty_Licking_1_1.ogg"
    scene black
    image videov_Monica_Betty_Licking_1_2 = Movie(play="video/v_Monica_Betty_Licking_1_2.mkv", fps=30)
    show videov_Monica_Betty_Licking_1_2
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.66666667)) + " loop 0.0>Sounds/v_Monica_Betty_Licking_1_1.ogg"
    scene black
    image videov_Monica_Betty_Licking_1_3 = Movie(play="video/v_Monica_Betty_Licking_1_3.mkv", fps=30)
    show videov_Monica_Betty_Licking_1_3
    with fadelong
    wclean

    #sound Бетти произносит ММмммммм...
    sound woman_moan8a
    music Loved_Up
    img 22208
    with diss
    betty "Мммм..."
    # Бетти закрывает глаза и приподнимает свои ноги, раскрываясь полностью (см. позу)
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    #sound падает мяч
    img 22209 # падает мяч
    with fadelong
    sound ball3
    w
    #sound Бетти произносит Ммммммм в экстазе
    sound woman_moan6
    #sound Моника лижет сильно
    sound lick13
    img 22210
    with diss
    betty "Мммм..."
    img 22211
    with diss
    w
    img 22212
    with diss
    w
    img 22213
    with diss
    betty "Сколько я могу терпеть эту мерзость..."
    img 22214
    with diss
    betty "Мммм..."
    img 22215
    with diss
    w
    img 22216
    with diss
    betty "Я... Порядочная женщина..."
    img 22217
    with diss
    w
    img 22218
    with diss
    w
    img 22219
    with diss
    betty "Аааах, прикажи ей остановится... Оооо..."
    # в итоге Бетти кончает со стонами
    #sound Бетти почти кончает (ахи рывками)
    sound woman_moan7a
    img 22220
    with diss
    w
    #sound Бетти почти кончает (ахи рывками)
    sound woman_moan12
    img 22221
    with diss
    w
    #sound Бетти почти кончает (ахи рывками)
    sound woman_moan11
    img 22222
    with diss
    w
    #sound Бетти почти кончает (ахи рывками)
    sound woman_moan12
    img 22223
    with diss
    betty "Ты... Ты!... Ты...."
    #sound Бетти кончает
    sound woman_moan14
    img 22224
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    betty "АААААААА!!!"
    #sound Бетти кончает
    sound woman_moan15
    img 22225
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    betty "ААААА!!! АААААА!!!"
    # Моника отстраняется от нее, смотрит с отвращением на нее, потом на Барди вопросительно и зло
    # Барди с довольной ухмылкой
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    sound snd_bodyfall
    img 22226 #Бетти кончила
    with fadelong
    w
    img 22227
    with diss
    w
    img 22228
    with diss
    w
    img 22229
    with fade
    bardie "Достаточно, гувернантка."
    sound highheels_short_walk
    img 22230
    with diss
    bardie "Теперь хозяин доволен своей гувернанткой и она может идти."
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    # Барди поворачивается к Бетти, та после оргазма лежит на кровати
    music Groove2_85
    img 22231
    with fadelong
    bardie "Я вижу, что ты соблюдаешь правила этого дома. Ты тоже свободна на сегодня."
    img 22232
    with Dissolve(2.0)
    w
    music stop
    img black_screen
    with diss
    pause 2.0
    music Mandeville
    return

############ College 1############

label gallery_14747:
    # Бетти садится напротив учителя, который сидит за учительским столом. Бетти с улыбкой
    music Groove2_85
    img 14735
    with fadelong
    w
    img 14741
    with diss
    w
    img 14742
    with fade
    w
    img 14736
    with diss
    w
    sound highheels_short_walk
    img 14743
    with fade
    w

    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14737
    with fadelong
    betty "Добрый день, мистер..."
    # учитель с серьезным лицом
    img 14738
    with diss
    teacher "...Эдвардс. Добрый день. Я так понимаю, вы - мать Барди?"
    img 14739
    with fade
    betty "Да, мистер Эдвардс. Барди сказал, что у него какие-то проблемы..."
    img 14740
    with diss
    teacher "У Барди серьезные проблемы с успеваемостью. У него много прогулов и много не сданных зачетов."
    teacher "Я неоднократно пытался проводить с ним разъяснительные беседы, но безуспешно."
    teacher "К сожалению, я вынужден вам сообщить, что я сейчас готовлю документы на отчисление Барди для передачи директору."
    img 14744
    with fade
    betty "Мистер Эдвардс, документы еще находятся у вас? Я могу их посмотреть?"
    img 14745
    with diss
    teacher "Да, конечно. Я вас пригласил сегодня именно для этого. Вот личный файл Барди, можете ознакомиться."
    # Учитель дает Бетти папку с документами, та их просматривает, сосредоточенно думая. Учитель в это время пялится на ее грудь
    img 14746
    with vpunch
    betty_t "Этот мелкий сопляк совсем не бывает в колледже!"
    betty_t "Если мне удастся уговорить учителя притормозить это дело, у меня появится отличная возможность приструнить его..."
    img 14747
    with diss
    w
    img 14748
    with diss
    betty_t "В противном случае, Барди мне вообще никакой жизни не даст. Я итак его уже видеть не могу."
    betty_t "Интересно, как мне уговорить этого мистера Эдвардса? Может, попросить денег у Ральфа? Скажу, что для колледжа..."
    # Бетти поднимает взгляд на учителя, тот продолжает пялиться на нее. Бетти уже без улыбки, с серьезным выражением лица
    img 14749
    with fade
    betty "Мистер Эдвардс, я вижу, что у Барди совсем все плохо с учебой. Этот сорванец и правда в последнее время совсем отбился от рук."
    betty "Возможно, мы с вами как-то сможем уладить этот вопрос? Я могла бы оказать спонсорскую помощь колледжу. Купить мел для доски, например."
    betty "Я обещаю, что поговорю с Барди. Этот сопл... Барди больше не будет прогуливать занятия и сдаст все зачеты."
    sound Jump2
    img 14750
    teacher "..."
    img 14751
    with fade
    betty "Мистер Эдвардс?"
    # учитель, наконец, отрывает взгляд от ее груди.
    img 14752
    with diss
    teacher "А? Что?"
    img 14753
    with fade
    betty "Я говорю, что готова поговорить с Барди и он будет себя хорошо вести..."
    img 14754
    with diss
    teacher "..."
    img 14755
    with fade
    teacher "Ну... Я даже не знаю... Документы уже подготовлены."
    teacher "Боюсь, что ничего уже нельзя изменить."
    # Барди подглядывает через приоткрытую дверь, переживает
    music Sneaky_Snitch
    img 14756
    with fade
    bardie_t "Черт!"
    bardie_t "..."
    bardie_t "Эта деревенщина не сможет договориться с преподом. Надо было гувернантку посылать к нему."
    # Бетти продолжает уговаривать учителя
    music Groove2_85
    img 14757
    with diss
    betty "Личный файл Барди все еще находится у вас. Значит, именно от вас зависит, дойдут ли документы до директора."
    betty "Что я могу сделать для того, чтобы Барди остался в колледже?"
    # препод снова залипает на груди Бетти, задумчиво
    img 14758
    with diss
    teacher "Хм. Я вижу, что вы искренне переживаете за сына, Миссис Робертс."
    # Бетти расплывается в улыбке
    img 14759
    with diss
    betty_t "Ненавижу этого сопляка!"
    img 14760
    with fade
    teacher "Возможно, я смогу что-нибудь придумать. Это будет непросто... Ведь, помимо меня, и другие учителя в курсе ситуации с Барди."
    teacher "Мне придется как-то аргументировать то, что я изменил свое решение..."
    img 14761
    with diss
    betty "Мистер Эдвардс, я понимаю, что это сложный процесс. Если я смогу чем-то вам помочь, то я буду только рада."
    # тут Бетти случайно роняет паку Барди на пол
    img 14762
    with vpunch
    #sound папка падает на пол
    sound down7
    betty "Oй!"
    img 14763
    with diss
    w
    # наклоняется за ней, поворачивает голову и видит, что учитель сидит с внушительным стояком
    img 14764
    with diss
    w
    sound Jump1
    img 14765
    with diss
    betty "!!!"
    # Бетти зависает на этом зрелище, но тут же берет себя в руки, выпрямляется. Глаза у нее заблестели, но она делает вид, что ничего не видела
    #video teacher dick up
    img black_screen
    with diss
    sound erection1
    scene black
    image videov_Teacher_Betty_DickUp_1 = Movie(play="video/v_Teacher_Betty_DickUp_1.mkv", fps=30, loop=False, image="/images/Slides/v_Teacher_Betty_DickUp_1_stop.jpg")
    show videov_Teacher_Betty_DickUp_1
#        with fadelong
    wclean

#       img 14766
#        with diss
    betty "..."

    music stop
    img black_screen
    with diss
    pause 2.0
    music Hidden_Agenda
    img 14767
    with fade
    betty "Так на чем мы остановились, мистер Эдвардс?.."
    # учитель догадался, что она его спалила, и принимает решение развести Бетти на "помощь"
    img 14768
    with diss
    teacher "На том, что вы могли бы мне помочь в этом непростом деле."
    # Бетти воодушевленно
    img 14769
    with fade
    betty "Да, конечно. Я буду рада помочь вам. Что мне нужно будет сделать?"
    img 14770
    with diss
    teacher "..."
    # учитель встает со стула, поправляет ширинку и пристально смотрит на Бетти. Бетти сидит на стуле и не может оторвать взгляд от его стояка, который прямо перед ее лицом
    music Loved_Up
    img 14771
    with fadelong
    w
    img 14772
    with diss
    betty "М-м-мистер Эд-д-двардс... Я н-не совсем вас п-п-понимаю..."
    img 14773
    with fade
    betty_t "Вот черт. Что же мне делать?"
    betty_t "Так, стоп! Я же замужняя женщина и верная жена."
    betty_t "Тем более, я разговариваю с учителем Барди! Я не должна так смотреть на то, что у него в штанах!"
    # Бетти поднимает взгляд от ширинки препода и смотрит ему в глаза. Говорит возмущенно
    label gallery_14785:
    music Groove2_85
    img 14774
    with fade
    betty "Мистер Эдвардс! Я замужем! Как вы можете предлагать мне подобное?!"
    img 14775
    with diss
    teacher "Вы же сами предложили мне помощь, миссис Робертс... Это очень помогло бы мне..."
    # Бетти снова уставилась на его стояк
    img 14776
    with diss
    teacher "Тем более, я не прошу о многом. Вы могли бы просто приласкать его рукой. У меня так давно не было никого."
    teacher "А вы такая красивая, миссис Робертс, что я просто не в силах держать себя в руках."
    # учитель медленно начинает расстегивать ремень
    sound snd_zip
    img 14777
    with fade
    betty_t "..."
    betty_t "Я не должна этого делать! Что вообще себе позволяет этот мистер Эдвардс?!"
    # учитель расстегивает молнию на брюках, Бетти не в силах отвести взгляд
    img 14781
    with diss
    betty_t "С другой стороны..."
    betty_t "Хм... Если я просто потрогаю его, это же не будет считаться изменой?"
    img 14782
    with fade
    betty "М-мистер Эд-двардс, если об этом кто-нибудь узнает..."
    img 14783
    with diss
    teacher "Миссис Робертс, это не в моих интересах, чтобы кто-либо узнал о нашей с вами договоренности."
    teacher "Я в виде исключения предлагаю вам единственный из всех возможных способов решить эту проблему с вашим сыном."
    teacher "Для этого вам достаточно просто протянуть руку..."
    # препод достает свой стояк
    music Loved_Up
    sound Jump1
    img 14784
    with diss
    teacher "... и немного погладить его."
    img 14785
    with diss
    betty "!!!"
    img 14786
    with diss
    menu:
        "Убежать.":
            music Groove2_85
            betty "Я не буду этого делать!!!"
            return
        "Постараться убедить учителя не делать этого":
            music Hidden_Agenda
            img 14787
            with fade
            betty "Мистер Эдвардс, я никогда себе не позволяю такого с другими мужчинами. Только с мужем..."
        "Поддаться давлению со стороны учителя":
            music Hidden_Agenda
            img 14788
            with fade
            betty "Мистер Эдвардс, я, конечно, не совсем уверена. Это единственный способ?"
            betty_t "У него просто каменный стояк. Если я к нему притронусь... Так интересно ощутить его."
    music Loved_Up
    img 14789
    with fade
    teacher "Это единственный способ, миссис Робертс. Просто прикоснитесь ко мне."
    # Бетти протягивает руку и замирает буквально в сантиметре от члена
    label gallery_14799:
    music Hidden_Agenda
    img 14790
    with diss
    betty_t "Что я делаю? Это так неправильно..."
    betty_t "Я просто потрогаю его и вопрос с Барди будет решен. Я делаю это не ради своего удовольствия!"
    # препод берет ее за запястье и притягивает ее руку к своему члену, Бетти прикасается к нему пальцами
    img 14791
    with diss
    w
    img 14792
    with diss
    betty_t "Ммм... Он и правда каменный. И такой горячий..."
    img 14793
    with fade
    betty "Мистер Эдвардс, я... мне... это так неправильно..."
    music Loved_Up
    img 14794
    with diss
    teacher "Вы уже делаете это, миссис Робертс. Еще совсем немного. Сожмите его своей ручкой."
    # препод убирает свою руку, Бетти обхватывает его член рукой
    img 14795
    with fade
    betty_t "Ооо! У этого мистера Эдвардса просто отличный член. Интересно, какой он на вкус?"
    betty_t "!!!"
    betty_t "О боже! О чем я думаю?!"
    # Бетти медленно начинает дрочить ему
    img 14796
    with diss
    sound drkanje5
    teacher "Да, так! У вас отлично получается, миссис Робертс! Быстрее!"
    # Бетти пристально смотрит на член и старается с удвоенной силой
    # Барди все видит и слышит. Волнение на его лице сменяется злорадной ухмылкой. Он достает свой смартфон и делает фото.
    music Sneaky_Snitch
    img 14797
    with fadelong
    bardie_t "Офигеть! Бетти даже в колледже умудрилась подержать чужой член в руке!"
    bardie_t "!!!"
    bardie_t "Может, будет какое-то продолжение?"

    # Бетти продолжает усердно работать рукой, не отрывая глаз от члена учителя
    img 14798
    with diss
    sound drkanje5
    w
    music Loved_Up2
    img 14799
    with fade
    sound drkanje5
    teacher "Ооо, миссис Робертс... Да, так! Еще..."
    teacher "Ммм... Еще быстрее!"
    #видео teacher_betty_handjob
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_1 = Movie(play="video/v_Teacher_Betty_HandJob_1_1.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_1
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
        scene black
        image videov_Teacher_Betty_HandJob_1_2 = Movie(play="video/v_Teacher_Betty_HandJob_1_2.mkv", fps=30)
        show videov_Teacher_Betty_HandJob_1_2
        wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_3 = Movie(play="video/v_Teacher_Betty_HandJob_1_3.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
    scene black
    image videov_Teacher_Betty_HandJob_1_4 = Movie(play="video/v_Teacher_Betty_HandJob_1_4.mkv", fps=30)
    show videov_Teacher_Betty_HandJob_1_4
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.0)) + " loop 0.0>Sounds/Betty_handjob_teacher.ogg"
        scene black
        image videov_Teacher_Betty_HandJob_1_5 = Movie(play="video/v_Teacher_Betty_HandJob_1_5.mkv", fps=30)
        show videov_Teacher_Betty_HandJob_1_5
        wclean

    #препод со стоном кончает на личный файл Барди, который на столе, попадает и Бетти на руку
    stop music
    music stop
    music Loved_Up2
    sound bulk1
    img 14800
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "ООООООООО!!!"
    sound man_moan18
#    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w

    # препод крайне доволен, надевает обратно брюки и садится за стол, а Бетти, изображая из себя оскорбленную невинность, вытирает руку

    # sound звук падающей спермы на папку (вввиухх...)
    sound hlup2
    music Groove2_85
    img 14801
    betty "Вы испачкали документы Барди, мистер Эдвардс."
    img 14802
    with fade
    teacher "Ничего страшного, миссис Робертс. Директор все равно этого не заметит."
    # Бетти в шоке, учитель с улыбочкой
    img 14803
    with diss
    betty "В смысле?! Мы же с вами договорились, что эти документы не дойдут до директора!"
    img 14804
    with fade
    teacher "Миссис Робертс, в моих силах пока только притормозить это дело."
    img 14805
    with diss
    betty "???"
    img 14807
    with fade
    teacher "Но если вы еще раз посетите меня на днях, то, возможно, я смогу закрыть этот вопрос."
    # Бетти удивленно
    img 14808
    betty "Еще раз?!"
    img 14809
    with diss
    teacher "Именно. Мне может снова потребоваться ваша помощь."
    # Барди злорадно ухмыляется за дверью
    music Sneaky_Snitch
    img 14806
    with fade
    bardie_t "!!!"
    bardie_t "Отлично! Нужно будет дождаться продолжения!"
    # Барди убегает, Бетти, сидя напротив учителя, пристально смотрит на него
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14810
    with fadelong
    betty_t "Из-за этого сопляка мне придется тащиться сюда снова. Он теперь в долгу передо мной. Нужно только окончательно уговорить учителя."
    img 14811
    with diss
    betty "Хорошо, мистер Эдвардс. Я загляну к вам на днях. И, надеюсь, мы с вами закроем этот вопрос."
    img 14812
    with fade
    teacher "Конечно, миссис Робертс. С нетерпением буду ждать встречи с вами."
    return

label gallery_14648:
    sound ball4
    # Барди снова делает вид, что не замечает ее. Бетти стоит, руки в боки и зовет его
    music Groove2_85
    img 14643
    with fadelong
    betty "Эй, ты! Иди сюда!"
    # Барди к ней подходит и, делая вид, что ничего не знает, вопросительно смотрит на нее
    # Барди держит мяч
    sound Jump1
    img 14644
    with fade
    bardie "???"
    bardie "Что?"
    # Бетти ему высокомерно
    img 14645
    with diss
    betty "Я договорилась с твоим преподавателем. Это было непросто, но я смогла его убедить не отчислять тебя из колледжа."
    betty "Он очень не хотел оставлять тебя. Мне пришлось три раза посетить его и, в итоге, я смогла его уговорить."
    # Барди продолжает молча смотреть на нее, но уже едва сдерживает улыбку
    img 14646
    with diss
    bardie "..."
    img 14647
    with fade
    betty "Я сделала то, о чем ты меня попросил. Но хочу сразу тебя предупредить, что я в любой момент могу позвонить мистеру Эдвардсу..."
    # Бетти с угрозой
    img 14648
    with diss
    betty "... и он выкинет твою задницу из колледжа!"
    betty "!!!"
    betty "Поэтому с этого дня ты перестаешь строить из себя здесь хозяина и командовать мною! Если будешь хорошо себя вести, то с твоей учебой все будет в порядке."
    # Бетти с торжествующей улыбкой на лице
    img 14649
    with fade
    betty_t "Вот ты и попался, мелкий сопляк! Попробуй теперь покомандовать в моем доме!"
    img 14650
    with diss
    bardie "..."
    # На это Барди, не выдерживая, злорадно хохочет
    img 14651
    with fade
    bardie "Аха-ха!!! Ты это серьезно сейчас?!"
    bardie "!!!"
    bardie "Жду тебя через пять минут в своей комнате! И не задерживайся!"
    bardie "Аха-ха!!!"
    # Барди уходит, Бетти в недоумении
    img 14652
    with diss
    betty_t "???"
    sound snd_runaway
    img 14653
    with fade
    betty_t "Что еще этому мерзкому мальчишке нужно от меня?"
    betty_t "Почему я, такая порядочная и умная женщина, должна терпеть такое в своем же доме?!"
    betty_t "!!!"
    betty_t "Он, наверное, не понял, что он больше здесь не хозяин. Хм, что ж... Пойду к нему, объясню ему еще раз, более доходчиво!"
    # Бетти с уверенным видом уходит
    sound highheels_run2
    img 14654
    with diss
    w
    return

label gallery_14821:
    # Бетти сидит напротив учителя, как в прошлый раз. Говорит с улыбкой
    music Groove2_85
    img 14778
    with fadelong
    w
    sound highheels_short_walk
    img 14779
    with diss
    w
    img 14780
    with fade
    betty "Мистер Эдвардс, я пришла, как мы с вами и договаривались."
    # учитель тоже улыбается
#    img 14813
    img 14815
    with diss
    teacher "Рад вас видеть снова, миссис Робертс. Документы Барди все еще у меня."
    img 14814
    with fade
    betty "Спасибо. Я надеюсь, что мы с вами закроем сегодня этот вопрос?"
    img 14815
    with diss
    teacher "Возможно, миссис Робертс. Все зависит от того, насколько вы готовы помочь мне в этом..."
    img 14816
    betty "..."
    # учитель, как и в прошлый раз, пялится на ее грудь
    img 14817
    with diss
    betty_t "Почему мне, порядочной женщине, приходится заниматься подобными вещами из-за какого-то малявки?!"
    betty_t "Мне снова придется работать рукой? Что ж, в прошлый раз это помогло..."
    betty_t "Но только рукой! На большее я не соглашусь, это уже будет изменой! А я замужняя женщина!"
    img 14818
    with diss
    teacher "..."
    img 14819
    with diss
    betty "Мистер Эдвардс?"
    img 14820
    with fade
    teacher "Миссис Робертс, вы же не будете против, если я прикоснусь к вашей прекрасной груди?"
    # Бетти растерянно
    music Hidden_Agenda
    img 14821
    with diss
    betty "???"
    betty "Я... Я думала, что мы просто повторим нашу прошлую встречу..."
    music Loved_Up
    img 14822
    with fade
    teacher "Я просто потрогаю ее и все. У вас такая красивая грудь!"
    img 14823
    with diss
    betty "..."
    img 14824
    with diss
    menu:
        "Не делать этого. Я порядочная замужняя женщина. Я же пришла сюда, чтобы удовлетворить его только рукой...":
            music Groove2_85
            img 14825
            with fade
            betty "Мистер Эдвардс, я порядочная замужняя женщина. Как вы себе это представляете?"
        "Почему нет? Он же просто потрогает мою грудь.":
            img 14826
            with fade
            betty "Мистер Эдвардс, я не против, если вы только потрогаете ее. Не более того!"
    img 14827
    with diss
    teacher "Миссис Робертс, я просто теряю голову от вашей красоты! Позвольте мне прикоснуться к вам. Хотя бы один раз."
    # Бетти встает со стула, приспускает платье и оголяет грудь. Учитель встает, обходит свой стол и подходит к ней
    # Барди подглядывает через приоткрытую дверь, делает фото
    music Sneaky_Snitch
    img 14828
    with fadelong
    bardie_t "!!!"
    bardie_t "Сегодня в моей коллекции прибавятся отличные фотки с Бетти! Жаль, отец пока не может оценить их."
    # учитель берет в ладонь грудь Бетти, приподнимает ее, сжимает
    label gallery_14831:
    music Loved_Up
    img 14829
    with fade
    w
    img 14830
    with diss
    w
    #видео teacher_betty_titsgrooping
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_v.ogg"
    scene black
    image videov_Teacher_Betty_TitsGrooping_1_1 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_1.mkv", fps=30)
    show videov_Teacher_Betty_TitsGrooping_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_2.ogg"
    scene black
    image videov_Teacher_Betty_TitsGrooping_1_2 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_2.mkv", fps=30)
    show videov_Teacher_Betty_TitsGrooping_1_2
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_3.ogg"
        scene black
        image videov_Teacher_Betty_TitsGrooping_1_3 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_3.mkv", fps=30)
        show videov_Teacher_Betty_TitsGrooping_1_3
        wclean
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/Betty_tits_4.ogg"
        scene black
        image videov_Teacher_Betty_TitsGrooping_1_4 = Movie(play="video/v_Teacher_Betty_TitsGrooping_1_4.mkv", fps=30)
        show videov_Teacher_Betty_TitsGrooping_1_4
        wclean

    img 14831
    with diss
    w
    img 14832
    with diss
    betty "Ох. Мистер Эдвардс. Достаточно." # ахххх
    img 14833
    with diss
    betty_t "Ммм, это так приятно..."
    img 14834
    with fade
    teacher "Миссис Робертс, я хочу поцеловать ее."
    img 14835
    with diss
    betty "Нет, нет. Мы об этом не договаривались." # возмущенно (но ахх)
    # учитель не слушает ее, целует ее соски
    img 14836
    with fade
    betty "Ох! Ооо!"
    #sound поцелуй груди
    sound kiss1
    img 14839
    with diss
    w
    img 14840
    with diss
    w
    #sound поцелуй груди
    label gallery_14856:
    music Loved_Up
    sound kiss1
    img 14838
    with diss
    betty_t "Мне нужно остановить это немедленно. Ммм... Иначе одной рукой я не обойдусь сегодня."
    betty_t "Я порядочная и замужняя женщина! Я не могу себе позволить большего!"
    # Бетти отталкивает препода, неуверенно
    img 14841
    with fade
    betty "Мистер Эдвардс! Давайте, сделаем все, как в прошлый раз и я пойду. У меня мало времени."
    sound snd_zip
    img 14842
    with diss
    teacher "Как скажете. Но вам же это нравится, миссис Робертс. Зачем вы сопротивляетесь?"
    # учитель расстегивает ремень и ширинку, достает член, Бетти смотрит на его стояк
    sound Jump1
    img 14843
    with diss
    teacher "Возьмите его в руку, миссис Робертс."
    img 14844
    with diss
    betty "..."
    # Бетти подходит к преподу ближе и гладит его член
    img 14845
    with fade
    betty_t "Ммм... Какой же он... Ммм..."
    betty_t "Так! Мне надо держать себя в руках и не забывать о том, что я замужем."
    img 14846
    with diss
    teacher "Давайте, миссис Робертс, смелее. Прикоснитесь к нему губами."
    img 14847
    with diss
    betty "Губами?!"
    img 14848
    with diss
    menu:
        "Как он мог предложить мне такое?! Я порядочная женщина!":
            img 14849
            with fade
            betty "Мистер Эдвардс, я не могу на такое согласиться. Я порядочная женщина."
        "Мне совсем неинтересно, какой он на вкус!!!":
            img 14850
            with fade
            betty "Мистер Эдвардс, вам не достаточно нравится, как я делаю это рукой и вы хотите большего?"
    img 14851
    with diss
    teacher "Миссис Робертс, просто поцелуйте его. Неужели он вам не нравится?"
    img 14852
    with diss
    betty_t "Черт!!! Мне неинтересно... Мне неинтересно..."
    img 14853
    with diss
    teacher "Всего один поцелуй..."
    img 14854
    with diss
    betty "Только один!"
    # Бетти опускается на колени перед преподом, смотрит на член
    img 14855
    with fade
    betty_t "Что я творю?"
    betty_t "..."
    betty_t "Я просто прикоснусь к нему губами... и языком. Я делаю это не ради себя!"
    # Бетти прикасается к члену учителя губами, потом проводит языком по головке
    img 14858
    with diss
    w
    img 14856
    with diss
    w
    img 14859
    with diss
    betty_t "Ммм... Ну и что, что он оказался таким вкусным..."
    # и еще раз языком по стволу и по головке
    # видео betty teacher licking
    img black_screen
    with diss
    pause 1.5
    music stop
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_1 = Movie(play="video/v_Teacher_Betty_DickLicking_1_1.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_2 = Movie(play="video/v_Teacher_Betty_DickLicking_1_2.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
    scene black
    image videov_Teacher_Betty_DickLicking_1_3 = Movie(play="video/v_Teacher_Betty_DickLicking_1_3.mkv", fps=30)
    show videov_Teacher_Betty_DickLicking_1_3
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
        scene black
        image videov_Teacher_Betty_DickLicking_1_4 = Movie(play="video/v_Teacher_Betty_DickLicking_1_4.mkv", fps=30)
        show videov_Teacher_Betty_DickLicking_1_4
        wclean
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str(float((rand(1,4))*1.83333333)) + " loop 0.0>Sounds/v_Teacher_Betty_DickLicking_1_1.ogg"
        scene black
        image videov_Teacher_Betty_DickLicking_1_5 = Movie(play="video/v_Teacher_Betty_DickLicking_1_5.mkv", fps=30)
        show videov_Teacher_Betty_DickLicking_1_5
        wclean

    img 14860
    with diss
    w
    img 14861
    with diss
    w
    img 14862
    with diss
    betty "Мистер Эдвардс, я... думаю, что... достаточно..."
    # а сама облизывает его
    img 14863
    with diss
    teacher "Еще немного, миссис Робертс. Обхватите его губами."
    # Бетти обхватывает губами головку и насаживается головой на член
    stop music
    music Loved_Up2
    img 14865
    with diss
    w
    sound Jump2
    img 14864
    show screen photoshot_screen()
#    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "Ооо, да!"
    img 14866
    with diss
    betty_t "!!!"
    # Бетти запускает свою руку под платье, в трусики (платье поднимает, трусики красные)
    # audio из видео
    img 14867
    with diss
    betty "Ммммфмммффф..."
    # Бетти старательно делает минет преподу, а Барди делает фото
    img 14868
    with diss
    w
    # видео betty teacher blowjob
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_1 = Movie(play="video/v_Teacher_Betty_Blowjob_1_1.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_1
    wclean
    if game.extra == True:
        img black_screen
        with diss
        music stop
        stop music
        play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
        scene black
        image videov_Teacher_Betty_Blowjob_1_2 = Movie(play="video/v_Teacher_Betty_Blowjob_1_2.mkv", fps=30)
        show videov_Teacher_Betty_Blowjob_1_2
        wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_3 = Movie(play="video/v_Teacher_Betty_Blowjob_1_3.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Blowjob_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Blowjob_1_4 = Movie(play="video/v_Teacher_Betty_Blowjob_1_4.mkv", fps=30)
    show videov_Teacher_Betty_Blowjob_1_4
    wclean
    music Sneaky_Snitch
    img 14857
    with fadelong
    bardie_t "В прошлый раз подрочила, сегодня отсосала... Как она старается, чтобы меня не отчислили!"
    bardie_t "Аха-ха!"
    bardie_t "!!!"
    # Бетти продолжает работать ртом
    music Loved_Up2
    img 14869
    with fade
    teacher "Ммм... Как же чертовски хорошо! Еще, быстрее!"
    img 14870
    with diss
    betty "Ммммфмммффф..."
    # препод со стоном кончает на ее лицо
    img 14871
    with diss
    w
    img 14872
    with diss
    w
    img 14873
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    sound bulk1
    img 14874
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    teacher "Ооо, дааааааа!"
    sound man_moan18
    # Бетти делает еще несколько движений своей рукой у себя в трусиках и кончает следом за ним
    img 14875
    with diss
    w
    img 14876
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound woman_moan14
    betty "ООООООООО!!!"
    # препод крайне доволен (уже одет)
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14877
    with fadelong
    teacher "Миссис Робертс, это было великолепно. Думаю, нам с вами нужно будет еще раз встретиться, чтобы закрепить нашу договоренность."
    # смотрит на него снизу вверх, вся в сперме
    img 14878
    with diss
    betty "Еще раз?"
    img 14879
    with fade
    teacher "Именно. Еще раз и я закрою этот вопрос с отчислением Барди."
    # Барди злорадно ухмыляется за дверью
    music Sneaky_Snitch
    img 14880
    with fade
    bardie_t "!!!"
    bardie_t "Отлично!"

    # Барди убегает, Бетти, сидя на полу перед учителем
    sound snd_runaway
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 14881
    with fadelong
    betty_t "Еще один визит к преподавателю и этот сопляк у меня в руках! Не могу дождаться, чтобы, наконец, поставить его на место."
    img 14882
    with diss
    betty "Хорошо, мистер Эдвардс. Я загляну к вам на днях. И мы закрепим с вами нашу договоренность."
    img 14883
    with fade
    teacher "Конечно, миссис Робертс. С нетерпением буду ждать встречи с вами."
    return

label gallery_14638:
    # Барди делает вид, что ничего не знает, спрашивает Бетти
    music Groove2_85
    img 14625
    with fadelong
    bardie "Ну как? Надеюсь, ты все уладила?"
    # Бетти смотрит возмущенно
    img 14638
    with diss
    betty "Ты хоть видел свои оценки?! Ты думаешь так просто решить этот вопрос, если ты вообще не бываешь в колледже?!"
    # Барди строго
    img 14629
    with fade
    bardie "То есть у тебя не получилось договориться с учителем?"
    bardie "..."
    bardie "Я так и знал, что тебе ничего нельзя поручить..."
    # Бетти орет
    music Power_Bots_Loop
    img 14634
    with fade
    betty "Ты как со мной разговариваешь, сопляк!"
    betty "Я не буду решать твои проблемы в колледже!"
    betty "Разбирайся с этим сам!"
    img 14636
    with diss
    betty "А теперь отойди! У меня нет времени на тебя!"
    betty "!!!"
    # Бетти уходит, Барди ей вслед
    img 14640
    with diss
    bardie "Стой! Я с тобой еще не договорил! Ты куда?"
    # кадр меняется на Барди
    music Sneaky_Snitch
    img 14641
    with fade
    bardie_t "Значит вот так?.. Значит, она у меня еще недостаточно под контролем."
    bardie_t "Окей... Я придумаю что-нибудь еще, помимо фоток с тренером."
    return

label gallery_14891:
    # Бетти сидит напротив учителя, как в прошлый раз. Бетти с улыбкой
    music Groove2_85
    img 14884
    with fadelong
    w
    img 14885
    with diss
    w
    sound highheels_short_walk
    img 14886
    with diss
    w
    img 14737
    with fade
    betty "Мистер Эдвардс, я пришла, как мы с вами и договаривались."
    img 14887
    with diss
    teacher "Рад вас видеть снова, миссис Робертс."
    img 14739
    with fade
    betty "Я надеюсь, что мы с вами закроем сегодня вопрос отчисления Барди с колледжа?"
    img 14888
    with diss
    teacher "Возможно, миссис Робертс. Все зависит от того, насколько вы готовы помочь мне в этом..."
    img 14816
    with diss
    betty "..."
    # учитель, как и в прошлый раз, пялится на ее грудь
    img 14817
    with diss
    betty_t "Сегодня нельзя соглашаться на большее! Достаточно было прошлого раза..."
    betty_t "Я не собираюсь изменять своему мужу!"
    img 14818
    with fade
    teacher "Миссис Робертс, вы же не будете против, если я прикоснусь к вашей прекрасной груди, как в прошлый раз?"
    img 14890
    with diss
    betty "???"
    img 14889
    with fade
    betty "Я... Да. Только как в прошлый раз, не более того!"
    img 14758
    with diss
    teacher "Миссис Робертс, ну конечно! Вам не о чем переживать!"
    # Бетти встает, приспускает платье и оголяет грудь. Учитель подходит к ней, берет в ладонь грудь Бетти, целует соски
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 14830
    with fadelong
    w
    img 14832
    with diss
    w
    #sound целует грудь Бетти
    sound kiss1
    img 14891
    with diss
    sound ahhh1
    betty_t "Ммм, как же хорошо..."
    img 14892
    with diss
    betty "Ох. Мистер Эдвардс."
    img 14893
    with fade
    teacher "Миссис Робертс, я сниму с вас платье? Оно мешает мне рассмотреть вашу красоту."
    # Бетти растерянно
    img 14894
    betty "Вы хотите снять с меня платье?!"
    img 14895
    with diss
    menu:
        "Это все закончится сексом. Я не должна делать этого! Я порядочная женщина...":
            img 14896
            with fade
            betty "Мистер Эдвардс, вы забыли, что я порядочная женщина? Достаточно моей голой груди."
        "Он хочет приласкать меня. Это же просто ласки, а не измена? Я же порядочная женщина...":
            img 14897
            with fade
            betty "Мистер Эдвардс, вам не достаточно моей голой груди и вы хотите большего?"
    img 14898
    with diss
    teacher "Миссис Робертс, я ничего такого не собираюсь делать. Просто приласкаю вас немного."
    teacher "Вы же в прошлый раз сделали мне приятно, теперь я хочу сделать так, чтобы и вам было хорошо."
    # Бетти возмущенно
    music Power_Bots_Loop
    img 14899
    with hpunch
    betty "Нет, Мистер Эдвардс! Вы - преподаватель. Как вы вообще можете предлагать мне такое?!"
    betty "Мне, замужней женщине!"
    music Groove2_85
    img 14900
    with fade
    teacher "Миссис Робертс, вы такая заботливая мать, так искренне переживаете за вашего сына..."
    teacher "Я предлагаю вам единственный из всех возможных способов окончательно решить вопрос об учебе Барди."
    teacher "Если вы сейчас откажетесь, то я буду вынужден передать документы Барди директору."
    teacher "И тогда ничего нельзя уже будет исправить. Подумайте хорошо, прежде чем отказывать мне."
    # Бетти пристально смотрит на препода, сомневается
    img 14901
    with diss
    betty "..."
    # принимает решение
    img 14902
    with fade
    betty "Ну ладно, мистер Эдвардс... Только быстро!"
    # Бетти раздевается до трусиков, учитель гладит ее рукой через трусики
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 14903
    with fadelong
    sound Jump1
    w
    img 14904
    with diss
    sound chpok3
    w
    #sound ах
    sound ahhh12
    img 14905
    with diss
    betty "Ах!"
    betty_t "О, как же приятно!"
    img 14906
    with diss
    w
    img 14907
    with diss
    sound chpok3
    w
    # учитель подводит ее к столу, нагибает над ним и снимает с нее трусики, второй рукой расстегивает свою ширинку
    label gallery_14919:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up
    img 14917
    with fadelong
    sound Jump1
    w
    img 14918
    with diss
    betty "Ммм..."
    # продолжает рукой ласкать ее киску, а потом входит в нее пальцами
    #sound чавк
    sound chmok2
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w
    img 14919
    with diss
    w
    img 14920
    with diss
    w


    img 14921
    with diss
    w
    img 14924
    with diss
    sound ahhh12
    betty "Ооо... М-мистер Эд-двардс... Ммм..."
    img 14922
    with diss
    betty_t "Ох, черт! Как же хорошо! Но я должна остановить его!"
    img 14923
    with diss
    betty "М-мистер Эд-двардс, я... дум-маю, что... д-достаточно..."
    # учитель продолжает водить рукой туда-сюда
    img 14925
    with diss
    teacher "Еще немного, миссис Робертс. Раздвиньте ножки пошире."
    # учитель убирает пальцы, берет в руки свой член, нацеливается в киску Бетти и входит в нее
    label gallery_14910:
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up2
    img 14910
    with fadelong
    sound chmok2
    w
    #видео teacher betty sex 1
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_1 = Movie(play="video/v_Teacher_Betty_Sex_1_1.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_2 = Movie(play="video/v_Teacher_Betty_Sex_1_2.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_3 = Movie(play="video/v_Teacher_Betty_Sex_1_3.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_4 = Movie(play="video/v_Teacher_Betty_Sex_1_4.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_4
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_5 = Movie(play="video/v_Teacher_Betty_Sex_1_5.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_5
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.16666667)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_1_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_1_6 = Movie(play="video/v_Teacher_Betty_Sex_1_6.mkv", fps=30)
    show videov_Teacher_Betty_Sex_1_6
    wclean

    img 14911
    with diss
    w
    img 14912
    with diss
    w
    img 14913
    with diss
    betty "Ааааах!"
    img 14914
    with diss
    w
    img 14915
    with diss
    teacher "Ооооо..."
    img 14916
    with diss
    w
    call photoshop_flash()
    w
    call photoshop_flash()
    w
    # Барди злорадно ухмыляется за дверью и делает несколько кадров
    img 14908
    with diss
    w
    call photoshop_flash()
    w
    bardie_t "!!!"
    bardie_t "Отлично! Теперь она от меня никуда не денется!"
    img 14909
    with fade
    # препод "любит" Бетти на столе, потом они перемещаются на пол, Бетти садится сверху
    w
    label gallery_14931:
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    img 14926
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_1 = Movie(play="video/v_Teacher_Betty_Sex_2_1.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_1
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_2 = Movie(play="video/v_Teacher_Betty_Sex_2_2.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_2
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_3 = Movie(play="video/v_Teacher_Betty_Sex_2_3.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_3
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_4 = Movie(play="video/v_Teacher_Betty_Sex_2_4.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_4
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_5 = Movie(play="video/v_Teacher_Betty_Sex_2_5.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_5
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_6 = Movie(play="video/v_Teacher_Betty_Sex_2_6.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_6
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_7 = Movie(play="video/v_Teacher_Betty_Sex_2_7.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_7
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_8 = Movie(play="video/v_Teacher_Betty_Sex_2_8.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_8
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,5))*1.5)) + " loop 0.0>Sounds/v_Teacher_Betty_Sex_2_1.ogg"
    scene black
    image videov_Teacher_Betty_Sex_2_9 = Movie(play="video/v_Teacher_Betty_Sex_2_9.mkv", fps=30)
    show videov_Teacher_Betty_Sex_2_9
    wclean
    music Loved_Up2
    img 14927
    with diss
    teacher "Ммммммм..."
    img 14928
    with diss
    betty "Только не кончайте в меня, мистер Эдвардс!"
    # Бетти двигается на учителе и через некоторое время кончает
    img 14929
    with diss
    w
    img 14930
    with diss
    w
    img 14931
    with diss
    w
    img 14932
    #sound бетти кончает
    sound woman_moan14
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    betty "ООООООООО!!!"
    # препод вынимает из нее член и со стоном кончает на ее грудь
    img 14933
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    img 14934
    sound bulk1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    sound man_moan18
    w
    teacher "Ооо, дааааааа!"
    img 14938
    with diss
    w
    # препод крайне доволен, лежит на полу, Бетти сидит на учителе, недоверчиво смотрит на него
    music Groove2_85
    img 14935
    with fade
    teacher "Миссис Робертс, это было великолепно. Считайте, что вопрос с отчислением Барди закрыт."
    # Бетти недоверчиво
    img 14936
    with diss
    betty "Это точно?"
    img 14937
    with fade
    teacher "Да, мы с вами только что закрепили нашу договоренность."
    # Барди делает еще фото и убегает, радостный
    music Sneaky_Snitch
    img 14939
    with fadelong
    w
    call photoshop_flash()
    w
    # Бетти встает и одевается, препод тоже
    music stop
    img black_screen
    with diss
    sound snd_runaway
    pause 2.0
    music Groove2_85
    img 14940
    with fadelong
    sound snd_zip
    teacher "Если вдруг у Барди снова начнутся проблемы с учебой, я вам сразу же позвоню, миссис Робертс."
    img 14941
    with diss
    betty_t "Отлично! Я сделала то, чего хотел этот сопляк. С меня хватит!"
    betty_t "Теперь он не посмеет требовать от меня своих глупостей!"
    img 14942
    with fade
    betty "Хорошо, мистер Эдвардс. Было приятно сотрудничать с вами."
    img 14943
    with diss
    teacher "Всегда к вашим услугам, миссис Робертс."
    return True
