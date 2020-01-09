
label gallery_20503:

# Моника подходит к Мелани в гримерной (первый раз)
# Мелани сидит за гримерным столиком
    menu:
        "Мелани, ты вернулась?":
            music Groove2_85
            img 20485
            with fadelong
            m "Мелани, ты вернулась?"
            img 20486
            with diss
            m "Где ты так долго была? Что с тобой случилось?"
            music Master_Disorder
            img 20487
            with fade
            melanie "Миссис Бакфетт, это Вы?"
            music Groove2_85
            img 20488
            with fade
            m "Да, Мелани, это Я!"
            m "И я ждала тебя все это время!"
            img 20489
            with diss
            m "Почему тебя так долго не было?!"
            m "Я уже думала что Маркус забрал тебя!"
            music Master_Disorder
            img 20490
            with fade
            melanie "Миссис Бакфетт, я не понимаю о чем Вы говорите..."
            music Groove2_85
            img 20491
            with fade
            m "Что значит ты не понимаешь, Мелани?"
            m "Я говорю про твой визит к Маркусу!"
            img 20492
            with diss
            m "Ты должна была решить с ним вопрос по поводу меня!"
            m "Но, вместо этого, ты куда-то пропала!"
            music Master_Disorder
            img 20493
            with fade
            melanie "Мэм, Я не знаю о чем и о ком Вы говорите..."
            music Pyro_Flow
            img 20494
            with fade
            m "Ты что, играешь со мной, Мелани?!"
            m "Ты прекрасно знаешь что я говорю о Маркусе!"
            # Мелани отворачивается
            music stop
            img black_screen
            with diss
            pause 2.0
            music Master_Disorder
            img 20495
            with fadelong
            melanie "Мэм, я не знаю кто это..."
            img 20496
            with diss
            melanie "Миссис Бакфетт, я очень занята. Пожалуйста, не отвлекайте меня..."

            img black_screen
            with diss
            pause 2.0
            music Groove2_85
            img 20497
            with fade
            mt "Она не хочет говорить про Маркуса..."
            mt "Она что, обманула меня и не ходила к нему?!"


        "Посмотреть на Мелани." if ep26_dialogues7_melanie1_flag1 == True:
            music stop
            img black_screen
            with fadelong
            music Malicious
            pause 1.0
            img 20498
            show screen vignette_screen
            with fadelong
            m "У меня странное чувство..."
            img 20499
            with Dissolve(1.0)
            m "Мелани?"
            img 20500
            with Dissolve(1.0)
            m "Мелани!"
            # убирает волосы
            img 20501
            with Dissolve(1.0)
            m "Что там? Что там такое?"
            img 20502
            with Dissolve(1.0)
            w
            music Villainous_Treachery
            img 20503
            with Dissolve(1.0)
            with hpunch
            w
            img 20504
            with hpunch
            m "О БОЖЕ!"
            sound snd_woman_scream1a
            img 20505
            with diss
            m "НЕТ!"
            hide screen vignette_screen
            img 20506
            with fade
            melanie "Миссис Бакфетт, я просила Вас не беспокоить меня."
            img 20507
            with diss
            m "!!!"
#            music stop
            img black_screen
            with diss
            pause 2.0
            return

            img black_screen
            with Dissolve(2.0)
    #    "Мелани, сучка, ты что, никуда не ходила?! (next update) (disabled)":
    #        pass
#        "Мелани, пожалуйста, для меня это очень важно! (next update) (disabled)":
#            pass
        "Уйти.":
            img black_screen
            with diss
            return

    return

label gallery_20723:
    # Моника приходит к Мелани
    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(_("АПАРТАМЕНТЫ МЕЛАНИ"))
    img black_screen
    with Dissolve(2.0)
#    music Groove2_85
    music Villainous_Treachery
    img 20620
    with fadelong
    w
    img 20621
    with diss
    m "Мелани, я пришла..."
    img 20622
    with diss
    melanie "..."
    img 20623
    with fade
    m "И я жду ответы..."
    img 20624
    with fade
    melanie "Миссис Бакфетт."
    melanie "Я не уверена в правильности решения пригласить Вас..."
    melanie "Вы точно вошли незаметно? Вас никто не видел?"
    music Groove2_85
    img 20625
    with fadelong
    m "Мелани, меня никто не видел. Я уверена в этом."
    m "И, раз уж я пришла, позволь мне войти."
    img 20626
    with diss
    melanie "..."
    m "..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music In_Your_Arms
    img 20627
    with fadelong
    melanie "Хорошо, Миссис Бакфетт..."
    melanie "Проходите."
    #
    sound highheels_short_walk
    img 20628
    with fadelong
    melanie "Присаживайтесь."
    img 20629
    with diss
    melanie "Давайте выпьем вина..."
    img 20630
    with fade
    m "..."
    music Groove2_85
    img 20631
    with fade
    m "Мелани, давай перейдем сразу к делу."
    m "Ты видела Маркуса?"
    img 20632
    with diss
    m "Что он сказал тебе?"
    m "Как мне избавиться от него?!"
    music Villainous_Treachery
    img 20633
    with fade
    melanie "Миссис Бакфетт..."
    melanie "Вы задаете слишком прямые вопросы."
    melanie "Для меня большой риск общаться с Вами..."
    img 20634
    with diss
    m "Мелани, я задаю те вопросы, которые меня больше всего волнуют!"
    music stop
    img black_screen
    with diss
    pause 1.0
    music In_Your_Arms
    sound pour_wine
    img 20635 #наливает
    with fadelong
    melanie "Выпейте вина, Миссис Бакфетт."
    img 20630
    with diss
    m "..."
#    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
#    music In_Your_Arms
    img 20636
    with fadelong
    m "Хорошо, Мелани."
    img 20637
    with diss
    mt "Вкусное вино..."
    mt "Как вкусно..."
    mt "Я уже отвыкла..."
    melanie "Зря Вы не согласились, Миссис Бакфетт..."
    sound plastinka2
    music Groove2_85
    img 20638
    with diss
    w
    img 20639
    with diss
    m "На что я зря не согласилась, Мелани?"
    img 20640
    with fade
    melanie "На то, чтобы поехать на ферму, когда Мистер Маркус предложил Вам..."
    music Power_Bots_Loop
    img 20641
    with hpunch
    m "ЧТО?!"
    img 20642
    with fade
    m "Мелани, ты представляешь о чем идет речь?!"
    m "Ты, вообще, знаешь что это за место?!"
    img 20643
    with diss
    m "Как ты можешь говорить мне такое?!"
    music Villainous_Treachery
    img 20644
    with fadelong
    melanie "Я знаю что это за место, Миссис Бакфетт..."
    melanie "Я видела его..."
    img 20645
    with vpunch
    m "Ты была там?!"
    m "Ты видела это... это место...?"
    m "Оно действительно такое, как говорит Маркус?!"
    sound highheels_short_walk
    img 20646
    with fade
    melanie "Да, Миссис Бакфетт..."
    melanie "Оно... Даже хуже..."
    melanie "И вскоре Вы отправитесь туда..."
    music Power_Bots_Loop
    img 20647
    with hpunch
    m "Нет! Я не отправлюсь туда, никогда!"
    music Villainous_Treachery
    img 20648
    with fade
    melanie "Вы отправитесь... И будете делать что Вам скажут..."
    melanie "Вы будете умолять о том, чтобы оказаться на обложке их журнала..."
    music Power_Bots_Loop
    img 20649
    with diss
    m "Я знаю что там за журнал!"
    m "Я не буду умолять об этом!"
    music Villainous_Treachery
    img 20650
    with fade
    melanie "Будете, как и остальные девушки, которые находятся там."
    melanie "Вы будете удивлены, когда увидите КОГО там можно встретить среди них..."
    melanie "У наших хозяев действительно хороший вкус..."
    img 20651
    with diss
    m "Наших хозяев?!"
    img 20652
    with fade
    melanie "Но Вам не удастся добиться ничего..."
    melanie "Вы упустили свой шанс."
    img 20653
    with diss
    melanie "Теперь Вы попадете туда в качестве..."
    img 20654
    with diss
    melanie "Я не буду об этом..." # Отворачивается
    img 20655
    with fade
    m "Нет, Мелани! Я лучше умру!"
    img 20656
    with diss
    melanie "Миссис Бакфетт..."
    melanie "Я видела там вещи..."
    img 20657
    with diss
    melanie "Вещи... которые похуже смерти..."
    img 20658
    with vpunch
    m "!!!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music In_Your_Arms
    img 20659
    with fadelong
    melanie "Выпейте вина, Миссис Бакфетт..."
#    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.5
    show screen camera_viewfinder_screen()
    sound camera_lens1
    img 20660 # photo
    with Dissolve(0.2)
    w
    sound camera_lens1
    img 20661
    with Dissolve(0.2)
    w
    sound camera_lens1
    img 20662 #photo
    with Dissolve(0.2)
    w
    call photoshop_flash()
    w

    #
    music stop
    img black_screen
    hide screen camera_viewfinder_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20663
    with fadelong
    m "Итак, Мелани."
    m "Почему ты утверждаешь что я обязательно попаду туда?"
    music Power_Bots_Loop
    img 20664
    with vpunch
    m "Ты что, заодно с этими людьми?"
    music Groove2_85
    img 20665
    with fade
    melanie "Нет, Миссис Бакфетт."
    melanie "Я на Вашей стороне..."
    img 20666
    with diss
    m "Но как? Как ты выбралась оттуда?!"
    music Master_Disorder
    img 20667
    with fade
    melanie "Я... не выбралась оттуда, Миссис Бакфетт..."
    img 20668
    with diss
    melanie "Оттуда невозможно выбраться..."
    music Power_Bots_Loop
    img 20669
    with fade
    m "Но ты сидишь здесь, передо мной!"
    music Master_Disorder
    img 20670
    with diss
    melanie "Миссис Бакфетт..."
    melanie "Я была глупа и думала что весь мир принадлежит мне."
    melanie "Что я могу добиться любой цели и поставить на колени любого мужчину..."
    m "..."
    img 20672
    with diss
    melanie "Я ошибалась..."
    melanie "Есть мужчины, которые гораздо сильнее меня..."
    img 20671
    with diss
    melanie "И, все на что хватило моих сил - это убедить их в том, что пока я полезнее здесь."
    img 20673
    with diss
    melanie "Нежели там..."
    melanie "Потому я не проходила тех тренировок, которые проходят все, кто попадает туда."
    img 20674
    with diss
    m "..."
    img 20675
    with fade
    melanie "Это бы..."
    melanie "Это бы изменило меня..."
    melanie "И я бы не смогла быть в той форме, чтобы сохранять эффективность здесь..."
    melanie "По эту сторону Фермы 218..."
    img 20676
    with hpunch
    m "!!!"
    music Villainous_Treachery
    img 20677
    with fade
    melanie "Но меня могут вернуть туда в любой момент..."
    melanie "Например, если я вдруг стану помогать Вам..."
    melanie "Для меня большой риск даже просто говорить с Вами, Миссис Бакфетт..."
    music Groove2_85
    img 20678
    with fadelong
    m "Мелани! Все что ты говоришь..."
    m "Этот Маркус..."
    m "Ведь он всего-лишь полицейский!"
    img 20679
    with diss
    m "Ведь есть законы, есть пресса."
    m "Есть здравый смысл, в конце концов!"
    img 20680
    with fade
    m "Я была шокирована после того что случилось и действительно испугалась этих людей."
    m "Но сейчас понимаю, что это все выглядит настолько нереально, что просто не может быть правдой!"
    img 20681
    with diss
    m "Может быть обратиться в другой полицейский участок или в организацию, которая выше?"
    m "Пойти к другому адвокату, обратиться за получением новых документов..."
    music stop
    img black_screen
    with diss
    pause 1.0
    music Master_Disorder
    img 20682
    with fadelong
    melanie "Миссис Бакфетт..."
    melanie "Вы имели деньги и власть."
    img 20683
    with diss
    melanie "Неужели Вы не поняли как устроен этот мир?"
    melanie "Вы говорите про законы?"
    music Power_Bots_Loop
    img 20684
    with fade
    m "Да, Мелани! Я говорю про законы!"
    sound snd_bodyfall
    img 20685
    with diss
    m "Эта ферма! Это какое-то безумие! Произвол!"
    m "Это нарушение всех мыслимых норм!"
    music Master_Disorder
    img 20686
    with fadelong
    melanie "Миссис Бакфетт."
    melanie "Закон - это лишь инструмент для управления теми, у кого нет власти."
    melanie "Для тех, у кого есть деньги и власть, закон не существует..."
    music Groove2_85
    img 20687
    with diss
    m "Это неправда, Мелани!"
    m "Даже богача можно засадить за решетку!"
    melanie "Да, Миссис Бакфетт, можно..."
    melanie "Но..."
    #
    music stop
    img black_screen
    with diss
    pause 1.5
#    music Groove2_85
    music Loved_Up
    img 20688
    with fadelong
    melanie "Представьте, что Ваш водитель задавил собачку."
    melanie "Хозяин собачки оказался обычным человеком."
    melanie "Закон бы действовал на Вас?"
    img 20689
    with diss
    melanie "Нет. Вы бы позвонили Дику и во всем виноват оказался бы обычный человек."
    melanie "А если бы это оказалась собачка Виктории, его секретаря?"
    sound highheels_short_walk
    img 20690
    with fade
    m "!!!"
    img 20691
    with diss
    melanie "Тогда бы закон работал как обычно."
    melanie "Вы бы заплатили компенсацию..."

#    m "!!!"
    sound Jump1
    img 20692
    with diss
    melanie "Все потому, что появился бы другой человек, также имеющий власть."
    melanie "И закон в его руках был бы просто интрументом."

    img 20693
    with diss
    melanie "Миссис Бакфетт, закон работает только для равных..."
    melanie "Вы сейчас можете забыть про это..."
    m "И ты хочешь сказать что Маркус..."

    sound Jump1
    img 20694 # Мелани нагибается
    with diss
    w
    sound Jump2
    img 20695
    with diss
    melanie "Да, Миссис Бакфетт."
    melanie "Мистер Маркус - это очень... очень большой человек..."
#    sound snd_back1
    sound Jump1
    img 20696
    with diss
    m "Большой человек, который работает простым полицейским?"

    music Groove2_85
    sound highheels_short_walk
    img 20697
    with fadelong
    melanie "Мистер Маркус не является частью системы, Миссис Бакфетт..."
    melanie "Он использует ее, потому что этого хочет."
    melanie "Так ему удобнее... Быть полицейским..."

    music Power_Bots_Loop
    img 20698
    with vpunch
    m "Он просто мерзавец! И все!"
    music Master_Disorder
    img 20699
    with fadelong
    melanie "Нет, Миссис Бакфетт."
    melanie "Я не считаю его мерзавцем."
    m "Почему, Мелани?!"
    m "Как ты можешь оправдывать его?!"

    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    img 20700
    with fadelong
    melanie "Миссис Бакфетт."
    melanie "Мистер Маркус - это мужчина."
    melanie "Мужчина, который имеет силу и власть поступать так как он хочет."
    melanie "Вы не встречали таких сильных мужчин ранее..."
    melanie "И вот... встретили..."
    melanie "Впрочем и я тоже..."

    music Power_Bots_Loop
    img 20701
    with fade
    m "Силу? Власть?!"
    m "Он просто работает на каких-то безумных хозяев, которые делают немыслимые вещи!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Master_Disorder
    img 20702
    with fadelong
    melanie "Нет, Миссис Бакфетт."
    melanie "Мистер Маркус имеет свое мнение на все вопросы."
    melanie "Например, он помогает Вам вместо того, чтобы делать так, как его просят люди, стоящие за ним..."

    music Power_Bots_Loop
    img 20703
    with fade
    m "МАРКУС?! ПОМОГАЕТ?! МНЕ???"
    m "Маркус только и ждет, чтобы забрать меня!"

    music Master_Disorder
    img 20704
    with fadelong
    melanie "Все несколько иначе, Миссис Бакфетт..."
    melanie "Есть люди, которые стоят за Мистером Маркусом."
    melanie "Они тоже обладают огромном властью и влиянием."
    melanie "И они ждут Вас."
    img 20705
    with diss
    melanie "Дик нарушил их планы."
    melanie "Он хороший адвокат. Он имеет влияние и опыт, но..."
    m "Что НО...?"
    melanie "Проблемы, которые создают действия Дика, они..."
    img 20706
    with diss
    m "..."
    music stop
    img black_screen
    with diss
    pause 1.0
    music Villainous_Treachery
    img 20707
    with fadelong
    melanie "Они несколько преувеличены Мистером Маркусом в глазах людей, которые ждут Вас..."
    melanie "Мистер Маркус может забрать Вас в любой момент, Миссис Бакфетт..."
    img 20708
    with hpunch
    m "!!!"
    music Master_Disorder
    img 20709
    with diss
    melanie "Но, почему-то, он этого не делает..."
    music Power_Bots_Loop
    img 20710
    with diss
    m "Почему?!"
    m "Если он может забрать меня в любой момент, то почему он ждет от меня каких-то нарушений закона?!"
    music Master_Disorder
    img 20711
    with fade
    melanie "Вы нравитесь ему, Миссис Бакфетт."
    melanie "Он играет с Вами."
    melanie "Однако, если Вы действительно нарушите хоть что-то, ему придется забрать Вас."
    melanie "На него давят люди, которые стоят за ним."
    img 20712
    with diss
    melanie "Они очень ждут, чтобы попробовать Вас... в деле..."
    m "!!!"
    img 20713
    with fadelong
    melanie "Это как кот, который играет с пойманной мышкой."
    melanie "Мышка пытается убежать, но у нее нет шансов, она уже поймана..."
    melanie "Радуйтесь тому, что у Вас есть какое-то время до того, пока с Вами наиграются..."
    melanie "Итог один. В конце концов, Вы окажетесь в том месте..."
    music Power_Bots_Loop
    img 20714
    with hpunch
    m "!!!"

    img 20715
    with fade
    m "Я не верю..."
    m "Этого не может быть..."
    m "Должен быть какой-то выход..."

    img 20716
    with diss
    m "..."
    music stop
    img black_screen
    with diss
    pause 2.0
    music Hidden_Agenda
    img 20717
    with fadelong
    m "Мелани, я признаю что ты в чем-то разбираешься больше меня..."
    m "Подскажи, что мне делать. Как выбраться из всего этого?"

    sound snd_bodyfall
    music Loved_Up
    img 20718 # толкает
    with diss
    w
    sound Jump1
    img 20719
    with fade
    melanie "Вам не выбраться из этого, Миссис Бакфетт."
    melanie "Я советую Вам затянуть эту игру."
    img 20720
    with diss
    melanie "Создайте для Мистера Маркуса дополнительный интерес к Вам."
    melanie "Проявите инициативу."
    img 20721
    with fade
    m "Что ты имеешь ввиду, Мелани?"
    m "Какую инициативу я должна проявить?"

    img 20722
    with diss
    melanie "Придите к нему, придите к Мистеру Маркусу."
    img 20723
    with diss
    melanie "Постарайтесь понравиться ему."
    img 20724
    with fade
    melanie "Не бегайте от него, ведь он помогает Вам."
    music Power_Bots_Loop
    img 20725
    with fade
    m "Придти к человеку, который лишил меня всего?!"
    m "И, при этом, пытаться понравиться ему?!"
    music Master_Disorder
    img 20726
    with fade
    melanie "Да, это не поможет Вам избежать участи."
    melanie "Но может помочь попасть на ферму в качестве той, кто согласилась на это добровольно."
    melanie "Вы, возможно, сможете исправить совершенную ошибку..."
    sound Jump1
    music Loved_Up2
    img 20727 #Мелани залезает
    with diss
    w
    music Power_Bots_Loop
    sound plastinka2
    img 20728
    with vpunch
    m "Мелани, за кого ты принимаешь меня?!"
    m "Я что, по твоему, сошла с ума?!"

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20729
    with fadelong
    melanie "Миссис Бакфетт."
    melanie "Я могу сказать Вам честно."
    melanie "Я считала Вас надменной дурой, которой богатство и власть достались благодаря случайности."

    img 20730
    with diss
    m "..."

    img 20731
    with fade
    melanie "Когда с Вами произошли изменения, Я даже не представляла с чем Вы столкнулись."
    melanie "Сейчас, зная про Вас все, я могу сказать что восхищаюсь Вами."
    melanie "В борьбе за свою свободу Вы проявляете такую волю и характер, что..."
    img 20732
    with diss
    melanie "Что я начинаю считать Вы заслуживали то положение, которое имели..."

    img 20733
    with diss
    m "..."

    img 20734
    with fade
    melanie "Потому я искренне желаю удачи Вам."
    img 20735
    with diss
    m "И ты не винишь меня в том что случилось с тобой?"
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Power_Bots_Loop
    img 20736
    with fadelong
    melanie "..."
    img 20737
    with hpunch
    melanie "Я ненавижу Вас за это, Миссис Бакфетт."


    img 20738
    with diss
    m "Ты ненавидишь меня, но помогаешь мне?"

    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20739
    with fadelong
    melanie "Я пытаюсь извлечь выгоду даже из этой безнадежной ситуации."
    melanie "Я умею справляться со своими эмоциями..."
    img 20740
    with diss
    m "Спасибо, Мелани."

    music Master_Disorder
    img 20741
    with fade
    melanie "Вы сниметесь в костюме черного лебедя..."

    music Groove2_85
    img 20742
    with diss
    m "Что? Мелани, про что ты говоришь?"

    img 20743
    with fade
    melanie "Биф. Он заставляет меня сниматься в костюме черного лебедя."
    melanie "Мне не уйти из этой компании сейчас, Миссис Бакфетт."
    melanie "Но я не хочу проходить эту фотосессию."

    music Hidden_Agenda
    img 20744
    with diss
    m "У этого костюма нет трусиков..."
    music Groove2_85
    img 20745
    with fade
    melanie "Да, именно."
    melanie "И Вы пройдете эту фотосессию вместо меня, Миссис Бакфетт."

    music Power_Bots_Loop
    img 20746
    with diss
    m "Мелани, ты сошла с ума?!"
    m "Я не буду сниматься в таком виде!"

    music Villainous_Treachery
    img 20747
    with fade
    melanie "Вы будете, Миссис Бакфетт."
    melanie "Иначе, клянусь, Вы отправитесь к Маркусу очень скоро!"
    melanie "Помочь Вам очень сложно, а сделать наоборот очень легко..."

    img 20748
    with diss
    m "!!!"

#    melanie "Но я умею справляться со своими эмоциями..."
#    m "Мелани, спасибо. Я подумаю над твоими словами."

    img 20749
    with fade
    melanie "А сейчас Вы можете идти, Миссис Бакфетт."
    melanie "Я не хочу рисковать и далее, общаясь с Вами..."


    menu:
        "Попросить деньги у Мелани.":
            music Hidden_Agenda
            m "Мелани."
            m "Раз уж ты желаешь мне удачи..."
            m "Скажи, у тебя ведь есть деньги?"
            melanie "У меня достаточно денег, Миссис Бакфетт."
            img 20750
            with fade
            m "Могла бы ты мне немного одолжить..."
            melanie "Нет, Миссис Бакфетт. Я не собираюсь рисковать, помогая Вам..."
            m "Я поняла, Мелани. Всего хорошего."
            melanie "Всего хорошего, Миссис Бакфетт..."
        "Уйти.":
            pass


    return

label gallery_15390:
    # Мелани сидит перед зеркалом в гримерке, поправляет макияж кистью для мейкапа
    music ZigZag
    img 15392
    with fadelong
    w
    img 15393
    with fade
    melanie_t "Я выгляжу какой-то уставшей..."
    melanie_t "Мне нужно взять несколько выходных и отдохнуть."
    img 15394
    with diss
    melanie_t "Возможно, стоит полететь на острова... Океан, пальмы, никаких папарацци..."
    melanie_t "Нужно будет подойти к Бифу, попросить у него небольшой отпуск."
    img 15395
    with diss
    melanie_t "Он не сможет мне отказать."
    melanie_t "Еще ни один мужчина не отказывал мне. И Биф не станет первым..."
    # в гримерку заходит серкретарша Бифа
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    music Groove2_85
    img 15386
    with fadelong
    secretary "Мисс Мелани..."
    # Мелани поворачивается к ней
    img 15387
    with diss
    melanie "Да?"
    img 15388
    with fade
    secretary "Сейчас звонила Мисс Виктория."
    # Мелани вопросительно смотрит на нее
    img 13932
    with diss
    melanie "И что Мисс Виктория сказала?"
    img 13930
    with fade
    secretary "Она просила передать Вам, что она сегодня ждет Вас у себя."
    secretary "Она сказала, что это очень срочно."
    # Мелани смотрит на секретаря вопросительно
    img 15389
    with diss
    melanie "Говорила ли Мисс Виктория еще что-нибудь?"
    img 15390
    with fade
    secretary "Нет, Мисс Мелани. Она только сказала, что это очень срочно."
    img 15391
    music Master_Disorder
    with diss
    melanie "..."

### меню выбора взято из другого диалога

    menu:
        "Идти на встречу с Викторией":
            pass
        "Отказаться от встречи (пропуск всех событий с Викторией)":
            music Groove2_85
            img 13932
            with fade
            melanie "Если эта девочка еще раз позвонит, то передайте ей, что у меня нет времени на это." #+
            img 13933
            with diss
            secretary "Хорошо, Мисс Мелани, я передам."
            return
###
    music ZigZag
    img 13929
    with fade
    melanie "Спасибо. Я проведаю Мисс Викторию сегодня."
    melanie "Вы можете идти."
    # секретарша уходит, Мелани поворачивается снова к зеркалу и задумчиво смотрит на свое отражение
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 2.0
    music Master_Disorder
    img 13935
    with fade
    melanie_t "Что этой мерзкой Мисс Виктории снова нужно от меня?"
    melanie_t "Почему Я должна ехать к ней по первому же ее звонку?"
    melanie_t "..."
    # Мелани снова берет в руки кисть для мейка и проводит ею по скуле
    img 15396
    with diss
    melanie_t "Эта мелкая стерва возомнила себя самой умной и хитрой..."
    melanie_t "Нужно будет придумать, как поставить ее на место."
    img 15397
    with fade
    melanie_t "Кто она вообще такая, чтобы вести себя со МНОЙ подобным образом?"
    melanie_t "Нужно во что бы то ни стало лишить эту сучку возможности шантажировать меня."
    img 15398
    with diss
    melanie_t "Если я узнаю, кто снабжает ее моими фотографиями, шпионя за мной..."
    melanie_t "То у меня будет хоть какая-то зацепка. Я смогу договориться с этим папарацци."
    img 13936
    with diss
    melanie_t "Уверена, что все дело в деньгах."
    melanie_t "..."
    # положила кисть на столик, поправляет прическу
    music ZigZag
    img 15399
    with fade
    melanie_t "Конечно, проще всего было бы соблазнить Дика."
    melanie_t "В моих силах сделать так, чтобы он вышвырнул эту сучку на улицу..."
    img 15400
    with diss
    melanie_t "Где он ее и подобрал, я так полагаю."
    melanie_t "Но ведь она сидит и охраняет Дика, как цепной пес."
    img 13935
    with diss
    melanie_t "Хм... Интересно, Дик вообще ходит куда-нибудь без нее?"
    melanie_t "Нужно будет узнать об этом."
    # Мелани смотрит на себя в зеркало
    music Power_Bots_Loop
    img 15401
    with fade
    melanie_t "А пока мне придется поехать к этой мелкой сучке..."
    melanie_t "И узнать, что взбрело ей в голову на этот раз."
    music ZigZag
    img 15402
    with diss
    melanie_t "Сейчас мне нужно ехать в офис Дика."
    # встает со стула
#    $ log1 = _("Пойти в офис Дика и узнать, что нужно Виктории")
    return

label gallery_15410:
    # Моника смотрит на Мелани удивленно
    music ZigZag
    sound snd_door_open1
    img 15409
    with fadelong
    w
    sound highheels_short_walk
    img 15410
    with fade
    m "Мелани? Ты ко мне?"
    music Master_Disorder
    img 15411
    with diss
    mt "Мелани не просто так зашла ко мне в гости. Что-то случилось."
    mt "Надеюсь, это не касается Маркуса!"
    mt "!!!"
    # Мелани равнодушно
    music ZigZag
    img 15412
    with fade
    melanie "Миссис Бакфетт. Я сейчас была на встрече с нашим общим хорошим другом..."
    # Моника явно напугана
    music Master_Disorder
    img 15413
    with diss
    mt "!!!"
    sound Jump1
    img 15414
    with diss
    m "Нашим общим д-другом?"
    music ZigZag
    img 15415
    with fade
    melanie "Да, Миссис Бакфетт. Этот человек хочет сегодня встретиться с нами."
    img 15416
    with diss
    mt "!!!"
    img 15417
    with fade
    w
    img 15418
    with diss
    melanie "Встреча состоится вечером у меня."
    melanie "В Ваших же интересах, Миссис Бакфетт, присутствовать на встрече..."
    # Моника смотрит на Мелани ошарашенно
    img 15419
    with fade
    julia "???"
    img 15420
    with diss
    melanie "..."
    music Master_Disorder
    img 15421
    with fade
    mt "Встреча с Маркусом?!"
    mt "У Мелани дома?!"
    img 15422
    with diss
    mt "Сегодня?!"
    mt "!!!"
    # Юлия заинтересованно наблюдает за их диалогом
    # Моника смотрит на Юлию, потом снова на Мелани, берет себя в руки
    img 15423
    with fade
    w
    music ZigZag
    img 15424
    with diss
    m "Я поняла, Мисс Мелани. Я приду вечером."
    img 15425
    with fade
    melanie "Договорились, Миссис Бакфетт."
    # Мелани уходит
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    sound2 snd_door_close1
    pause 2.0
    # у Моники в заданиях появляется "Пойти вечером к Мелани домой на встречу с 'другом'"
    #$ log1 = _("Пойти вечером к Мелани домой на встречу с 'другом'")
    return

label gallery_15443:
    # Биф, как обычно, сидит за столом с бутылкой алкоголя
    music Groove2_85
    img 15428
    with fadelong
    w
    img 15429
    with fade
    biff "А! Моя лучшая цыпочка пришла!"
    biff "Чем порадуешь папочку сегодня?"
    music ZigZag
    img 15430
    with diss
    melanie_t "У него вокруг одни цыпочки... Как это пошло..."
    sound highheels_short_walk
    img 15431
    with fade
    melanie "Биф, я хотела поговорить с тобой."
    melanie "Надеюсь, ты мне не откажешь..."
    # смотрит на него заигрывающе, Биф сидит расплывается в улыбке
    music Groove2_85
    img 15432
    with diss
    biff "Цыпочка что-то хотела попросить у меня?"
    biff "Говори. Папочка сегодня добрый."
    music Hidden_Agenda
    img 15433
    with fade
    melanie "..."
    sound Jump1
    img 15434
    with diss
    melanie "Возможно, ты позволишь мне..."
    melanie "Взять несколько выходных дней и немного отдохнуть?"
    music Groove2_85
    img 15435
    with fade
    biff "Цыпочка устала? Конечно, папочка позволит ей отдохнуть!"
    biff "..."
    biff "Только цыпочка сначала сделает фотосессию!"
    img 15436
    with diss
    melanie "Какую фотосессию?"
    img 15437
    with fade
    biff "Мне нужны фотографии для следующего номера журнала."
    biff "И я хочу видеть на этих фотографиях твое лицо, цыпочка..."
    img 15438
    with diss
    biff "И не только лицо..."
    biff "У цыпочки есть, что показать в объектив камеры."
    # Мелани приподнимает бровь удивленно
    music ZigZag
    img 15439
    with fade
    melanie "..."
    music Groove2_85
    img 15440
    with diss
    biff "В прошлый раз я просил тебя сделать фотосессию."
    biff "А ты сама не стала в ней сниматься."
    img 15441
    with fade
    biff "Поэтому мне сейчас нужны именно твои фотографии."
    biff "А не той цыпочки, которая притворяется Моникой Бакфетт."
    music ZigZag
    img 15442
    with diss
    melanie_t "Хм... Я надеялась, что его устроят фотографии Миссис Бакфетт..."
    img 15443
    with fade
    melanie "В каком костюме нужно провести съемку?"
    music Groove2_85
    img 15444
    with diss
    biff "Мне нравится твой костюм с красными трусиками..."
    img 15445
    with diss
    biff "Хочу увидеть тебя в нем на фотографиях!"
    melanie "..."
    img 15446
    with fade
    biff "Сделай эту фотосессию и можешь взять несколько выходных."
    biff "Папочка добрый, папочка разрешает."
    # сидит с видом "хозяин мира", улыбается
    music ZigZag
    img 15447
    with diss
    menu:
        "Согласиться на фотосессию":
            pass
        "Отказаться (пропуск фотосессии)":
            music ZigZag
            img 15448
            with fade
            melanie_t "Он намекнул, что ему нужны откровенные фотографии..."
            melanie_t "В этом костюме с трусиками другие фотографии и не получатся..."
            melanie_t "..."
            melanie_t "Думаю, Биф обойдется без этих фотографий."
            img 15449
            with diss
            melanie "Биф, я пока не совсем готова к фотосессии..."
            melanie "Я ее сделаю, но позже..."
            img 15450
            with diss
            melanie_t "... возможно."
            img 12847
            with fade
            biff "Папочка добрый, поэтому разрешает тебе подумать."
            return # пропуск фотосессии, сразу в гримерку, оттуда домой на девичник
    img 15448
    with fade
    melanie_t "Что ж... У меня как раз есть время до встречи с мелкой дрянью Викторией."
    img 15451
    with diss
    melanie "Хорошо, Биф. Я сделаю, как ты хочешь." # без эмоций
    music Groove2_85
    img 15452
    with fade
    biff "Хорошая цыпочка. Папочка цыпочкой очень доволен."
    img 15453
    with diss
    melanie_t "Нужно пойти в фотостудию. Надеюсь, Алекс на месте."
    # в заданиях появляется "Провести фотосессию"
#    $ log1 = _("Провести фотосессию")
    return

############ BiffCastings 1############

label gallery_8442:
    label gallery_8442_1:
        #первый вызов
        help "Пока доступны только две возможностьи. Другие пункты будут доступны в следующих версиях игры."
        menu:
            "Показать обнаженную грудь.":
                #Моника показывает грудь в зависимости от одежды
                label gallery_8453:
                $ store_music()
                music Loved_Up
                if castingCloth == 1:
                    if chickMode == True:
                        img 8441
                        with Dissolve(0.5)
                        m "Моника Бакфетт хочет показать папочке грудь..."
                        img 8442
                        with fade
                        w
                        img 8444
                        with Dissolve(0.5)
                        w
                    else:
                        img 8441
                        with Dissolve(0.5)
                        m "Я покажу тебе грудь, потому что ты заставил меня..."
                        img 8442
                        with fade
                        w
                        img 8443
                        with Dissolve(0.5)
                        w
                if castingCloth == 2:
                    if chickMode == True:
                        sound snd_fabric1
                        img 8460
                        with fade
                        m "Леди Нуар хочет показать папочке грудь..."
                        img 8461
                        biff "Давай, Леди Нуар! Показывай свои сиськи!"
                        "Не прячь их от папочки!"
                        img 8456
                        with Dissolve(0.5)
                        w
                        img 8457
                        with Dissolve(0.5)
                        w
                        img 8458
                        with Dissolve(0.5)
                        w
                        img 8459
                        with Dissolve(0.5)
                        w

                    else:
                        sound snd_fabric1
                        img 8453
                        with fade
                        m "Биф, мне обязательно это делать?"
                        img 8454
                        biff "Давай, Леди Нуар! Показывай свои сиськи!"
                        "Не прячь их от папочки!"
                        "А то я заставлю Леди Нуар показать еще кое-что!"
                        img 8455
                        with fade
                        w
                        img 8445
                        biff "Я жду!"
                        img 8455
                        with fade
                        w
                        img 8456
                        with Dissolve(0.5)
                        w
                        img 8457
                        with Dissolve(0.5)
                        w
                        img 8458
                        with Dissolve(0.5)
                        w
                        img 8459
                        with Dissolve(0.5)
                        w
                if castingCloth == 3:
                    if chickMode == True:
                        img 8473
                        with fade
                        m "Девушка с календаря хочет показать папочке грудь..."
                        sound snd_fabric1
                        img 8477
                        with Dissolve(0.5)
                        w
                        img 8478
                        with Dissolve(0.5)
                        w
                        img 8479
                        with Dissolve(0.5)
                        w
                    else:
                        label gallery_8474:
                        img 8469
                        with fade
                        m "Я знаю, я должна показать тебе грудь..."
                        "Но можно я не буду делать этого?"
                        img 8470
                        biff "Давай! Девушка с календаря!"
                        "Показывай свои сиськи!"
                        "Иначе я скажу Алексу чтобы эти голые сиськи смотрели прямо с календаря!"
                        img 8471
                        with fade
                        mt "Черт! У меня молоток... Может убить этого мерзавца?!"
                        "Сколько мне терпеть это???"
                        "..."
                        "Нет... Слишком опасно..."
                        img 8472
                        biff "Ну же! Сиськи!"
                        img 8471
                        with fade
                        w
                        img 8474
                        with Dissolve(0.5)
                        w
                        img 8475
                        with Dissolve(0.5)
                        m "На, смотри..."
                        img 8476
                        with Dissolve(0.5)
                        w
                        "Мне не нужны проблемы..."
                        w
                if castingCloth == 4:
                    if chickMode == True:
                        label gallery_9479:
                        img 9477
                        with fade
                        sound snd_fabric1
                        m "Роза надежды хочет показать папочке грудь..."
                        img 9478
                        with Dissolve(0.5)
                        w
                        img 9479
                        with Dissolve(0.5)
                        w
                        img 9480
                        with Dissolve(0.5)
                        w
                    else:
                        img 9481
                        with fade
                        m "Я покажу тебе грудь, потому что ты заставил меня..."

                        img 9482
                        with Dissolve(0.5)
                        w
                        img 9483
                        with Dissolve(0.5)
                        w
                if castingCloth == 5:
                    if chickMode == True:
                        img 9500
                        with fade
                        sound snd_fabric1
                        m "Стюардесса хочет показать папочке грудь..."
                        img 9501
                        with Dissolve(0.5)
                        w
                        img 9502
                        with Dissolve(0.5)
                        w
                        img 9503
                        with Dissolve(0.5)
                        w
                        img 9504
                        with Dissolve(0.5)
                        w
                    else:
                        img 9500
                        with fade
                        m "Я покажу тебе грудь, потому что ты заставляешь меня это делать!.."
                        img 9501
                        with Dissolve(0.5)
                        w
                        img 9502
                        with Dissolve(0.5)
                        w
                        img 9503
                        with Dissolve(0.5)
                        w
                        img 9504
                        with Dissolve(0.5)
                        w
                if castingCloth == 6:
                    if chickMode == True:
                        label gallery_20187:
                        img 20184
                        with fade
                        sound snd_fabric1
                        m "Алая Жемчужина хочет показать папочке грудь..."
                        img 20185
                        with Dissolve(0.5)
                        w
                        img 20186
                        with Dissolve(0.5)
                        w
                        img 20187
                        with Dissolve(0.5)
                        w
                    else:
                        img 20184
                        with fade
                        m "Я покажу тебе грудь, потому что ты заставляешь меня это делать!.."
                        img 20185
                        with Dissolve(0.5)
                        w
                        img 20186
                        with Dissolve(0.5)
                        w
                        img 20187
                        with Dissolve(0.5)
                        w
                if castingCloth == 7:
                    if chickMode == True:
                        label gallery_20205:
                        img 20202
                        with fade
                        m "Запретное Желание хочет показать папочке грудь..."
                        img 20203
                        with Dissolve(0.5)
                        w
                        img 20204
                        with Dissolve(0.5)
                        w
                        img 20205
                        with Dissolve(0.5)
                        w
                        img 20206
                        with diss
                        w
                    else:
                        img 20202
                        with fade
                        m "Я покажу тебе грудь, потому что ты заставляешь меня это делать!.."
                        img 20203
                        with Dissolve(0.5)
                        w
                        img 20204
                        with Dissolve(0.5)
                        w
                        img 20205
                        with Dissolve(0.5)
                        w
                        img 20206
                        with diss
                        w
                $ restore_music()
                img 8445
                biff "Хорошо, папочка доволен!"
                #если уже несколько раз
                biff "Но папочке начинает надоедать одно и то же..."
            "Показать обнаженную попу." if shotsAmountCompleted >= shotsTotalAmount:
                label gallery_9444:
                $ store_music()
                music Loved_Up
                if castingCloth == 1:
                    if chickMode == True:
                        img 9443
                        with Dissolve(0.5)
                        m "Моника Бакфетт хочет показать папочке свой зад..."
                        img 9444
                        with fade
                        w
                        img 9445
                        with fade
                        w
                        img 9446
                        with Dissolve(0.5)
                        w
                    else:
                        img 9443
                        with Dissolve(0.5)
                        m "Я покажу тебе зад, потому что ты заставил меня..."
                        img 9444
                        with fade
                        w
                        img 9445
                        with fade
                        w
                        img 9446
                        with Dissolve(0.5)
                        w
                if castingCloth == 2:
                    if chickMode == True:
                        label gallery_9453:
                        sound snd_fabric1
                        img 9447
                        with fade
                        m "Леди Нуар хочет показать папочке свой зад..."
                        img 9448
                        biff "Давай, Леди Нуар! Показывай свои зад!"
                        "Не прячь его от папочки!"
                        img 9452
                        with fade
                        w
                        img 9453
                        with Dissolve(0.5)
                        w
                        img 9454
                        with Dissolve(0.5)
                        w
                        img 9455
                        with Dissolve(0.5)
                        w
                        img 9456
                        with Dissolve(0.5)
                        w
                        img 9456
                        with Dissolve(0.5)
                        w
                        img 9457
                        with Dissolve(0.5)
                        w
                        img 9458
                        with Dissolve(0.5)
                        w
                    else:
                        sound snd_fabric1
                        img 9449
                        with fade
                        m "Биф, мне обязательно это делать?"
                        img 9450
                        biff "Давай, Леди Нуар! Показывай свои зад!"
                        "Не прячь его от папочки!"
                        "А то я заставлю Леди Нуар показать свой зад на камеру!"
                        img 9451
                        with fade
                        w
                        biff "Я жду!"
                        img 9452
                        with fade

                        img 9453
                        with Dissolve(0.5)
                        w
                        img 9454
                        with Dissolve(0.5)
                        w
                        img 9455
                        with Dissolve(0.5)
                        w
                        img 9456
                        with Dissolve(0.5)
                        w
                        img 9456
                        with Dissolve(0.5)
                        w
                        img 9457
                        with Dissolve(0.5)
                        w
                        img 9458
                        with Dissolve(0.5)
                        w
                if castingCloth == 3:
                    if chickMode == True:
                        label gallery_9465:
                        img 9459
                        with fade
                        m "Девушка с календаря хочет показать папочке свою попу..."
                        img 9460
                        biff "Давай! Девушка с календаря!"
                        "Показывай свой зад!"
                        img 9464
                        with fade
                        w
                        sound snd_fabric1
                        img 9465
                        with Dissolve(0.5)
                        w
                        m "На, смотри..."
                        img 9466
                        with Dissolve(0.5)
                        w
                        img 9467
                        with Dissolve(0.5)
                        w
                        img 9468
                        with Dissolve(0.5)
                        w
                        img 9469
                        with Dissolve(0.5)
                        w
                    else:
                        img 9461
                        with fade
                        m "Я знаю, я должна показать тебе свой зад..."
                        "Но можно я не буду делать этого?"
                        img 9462
                        biff "Давай! Девушка с календаря!"
                        "Показывай свой зад!"
                        "Иначе я скажу Алексу чтобы этот голый зад смотрел на всех прямо с календаря!"
                        img 9463
                        biff "Ну же! Зад!"
                        img 9464
                        with fade
                        w
                        sound snd_fabric1
                        img 9465
                        with Dissolve(0.5)
                        w
                        m "На, смотри..."
                        img 9466
                        with Dissolve(0.5)
                        w
                        img 9467
                        with Dissolve(0.5)
                        w
                        img 9468
                        with Dissolve(0.5)
                        w
                        img 9469
                        with Dissolve(0.5)
                        "Мне не нужны проблемы..."
                if castingCloth == 4:
                    if chickMode == True:
                        label gallery_9492:
                        img 9485
                        with fade
                        sound snd_fabric1
                        m "Роза надежды хочет показать папочке свой зад..."
                        img 9486
                        biff "Давай, Роза!"
                        "Показывай свой зад!"

                        img 9487
                        with Dissolve(0.5)
                        w
                        img 9488
                        with Dissolve(0.5)
                        w
                        img 9489
                        with Dissolve(0.5)
                        w
                        img 9490
                        with Dissolve(0.5)
                        w
                        img 9491
                        with Dissolve(0.5)
                        w
                        img 9492
                        with Dissolve(0.5)
                        w
                    else:
                        img 9484
                        with fade
                        m "Я покажу тебе свой зад, потому что ты заставляешь меня это делать!"
                        img 9486
                        biff "Давай, Роза!"
                        "Показывай свой зад!"

                        img 9487
                        with Dissolve(0.5)
                        w
                        img 9488
                        with Dissolve(0.5)
                        w
                        img 9489
                        with Dissolve(0.5)
                        w
                        img 9490
                        with Dissolve(0.5)
                        w
                        img 9491
                        with Dissolve(0.5)
                        w
                        img 9492
                        with Dissolve(0.5)
                        w
                if castingCloth == 5:
                    if chickMode == True:
                        label gallery_9513:
                        img 9506
                        with fade
                        sound snd_fabric1
                        m "Стюардесса Fashion Airlines хочет показать папочке свой зад..."
                        img 9507
                        biff "Давай, Стюардесса!"
                        "Показывай свой зад!"
                        img 9508
                        with fade

                        img 9509
                        with Dissolve(0.5)
                        w
                        img 9510
                        with Dissolve(0.5)
                        w
                        img 9511
                        with Dissolve(0.5)
                        w
                        img 9512
                        with Dissolve(0.5)
                        w
                        img 9513
                        with Dissolve(0.5)
                        w
                        img 9514
                        with Dissolve(0.5)
                        w
                    else:
                        img 9505
                        with fade
                        m "Я покажу тебе свой зад, потому что ты заставляешь меня это делать!"
                        img 9507
                        biff "Давай, Стюардесса!"
                        "Показывай свой зад!"
                        img 9508
                        with fade

                        img 9509
                        with Dissolve(0.5)
                        w
                        img 9510
                        with Dissolve(0.5)
                        w
                        img 9511
                        with Dissolve(0.5)
                        w
                        img 9512
                        with Dissolve(0.5)
                        w
                        img 9513
                        with Dissolve(0.5)
                        w
                        img 9514
                        with Dissolve(0.5)
                        w
                if castingCloth == 6:
                    if chickMode == True:
                        label gallery_20191:
                        img 20188 #9506
                        with fade
                        sound snd_fabric1
                        m "Алая Жемчужина хочет показать папочке свой зад..."
#                        img 9507
                        biff "Давай, Жемчужина!"
                        "Показывай свой зад!"
                        img 20189 #9508
                        with fade
                        m "Биф, можно Я не буду снимать костюм?"
                        m "Это долго..."

                        img 20190
                        with fade
                        biff "Хорошо, цыпочка."
                        biff "У папочки нет времени на переодевания."

                        img 20191
                        biff "Пусть цыпочка сядет на стол."
                        biff "Папочка хочет посмотреть на сидящую цыпочку."

                        img 20192
                        with diss
                        m "Так, Биф?"
                        img 20193
                        biff "Да, цыпочка. Привыкай сидеть на жердочке."
                        biff "Скоро ты займешь место рядом с малышкой Мелани!"

                        img 20194
                        mt "!!!"

                    else:
                        img 20188 #9506
                        with fade
                        sound snd_fabric1
                        m "Я покажу тебе свой зад, потому что ты заставляешь меня это делать!"
#                        img 9507
                        biff "Давай, Жемчужина!"
                        "Показывай свой зад!"
                        img 20189 #9508
                        with fade
                        m "Биф, можно Я не буду снимать костюм?"
                        m "Это долго..."

                        img 20190
                        with fade
                        biff "Хорошо, цыпочка."
                        biff "У папочки нет времени на переодевания."

                        img 20191
                        biff "Пусть цыпочка сядет на стол."
                        biff "Папочка хочет посмотреть на сидящую цыпочку."

                        img 20192
                        with diss
                        m "Так, Биф?"
                        img 20193
                        biff "Да, цыпочка. Привыкай сидеть на жердочке."
                        biff "Скоро ты займешь место рядом с малышкой Мелани!"

                        img 20194
                        mt "!!!"
                if castingCloth == 7:
                    if chickMode == True:
                        label gallery_20210:
                        img 20207
                        with fade
                        sound snd_fabric1
                        m "Запретное Желание хочет показать папочке свой зад..."
                        img 20208
                        with diss
                        biff "Давай, Запретное Желание!"
                        "Показывай свой зад!"
                        img 20209
                        with fade
                        w

                        img 20210
                        with Dissolve(0.5)
                        w
                        img 20211
                        with Dissolve(0.5)
                        w
                        img 20212
                        with Dissolve(0.5)
                        w
                    else:
                        img 20207
                        with fade
                        m "Я покажу тебе свой зад, потому что ты заставляешь меня это делать!"
                        img 20208
                        biff "Давай, Запретное Желание!"
                        "Показывай свой зад!"
                        img 20209
                        with fade
                        w

                        img 20210
                        with Dissolve(0.5)
                        w
                        img 20211
                        with Dissolve(0.5)
                        w
                        img 20212
                        with Dissolve(0.5)
                        w
                $ restore_music()
                img 8445
                biff "Хорошо, папочка доволен!"
                #если уже несколько раз
#                biff "Но папочке начинает надоедать одно и то же..."
            "Показать обнаженную попу. (фотосессия не завершена) (disabled)" if shotsAmountCompleted < shotsTotalAmount:
                pass
#            "Раздеться и принимать различные модельные позы.":
#                $ store_music()
#                call ep210_dialogues1_office_biff_1a()
#                $ restore_music()
#                img 8445
#                biff "Хорошо, папочка доволен!"
            "Раздеться и принимать различные модельные позы. (disabled)":
                pass
#            "Раздеться и встать на колени задом к Бифу.":
#                $ store_music()
#                call ep210_dialogues1_office_biff_1b()
#                $ restore_music()
#                img 8445
#                biff "Хорошо, папочка доволен!"
            "Раздеться и встать на колени задом к Бифу. (disabled)":
                pass
#            "Раздеться и лечь на пол раздвинув ноги.":
#                $ store_music()
#                call ep210_dialogues1_office_biff_1c()
#                $ restore_music()
#                img 8445
#                biff "Хорошо, папочка доволен!"
            "Раздеться и лечь на пол раздвинув ноги. (disabled)":
                pass
            "Раздеться и сесть на стол.":
                menu:
                    "Поставить на стол одну ногу. (disabled)":
                        pass
                    "Сесть на стол лицом к Бифу, широко раздвинув ноги. (disabled)":
                        pass
                    "Сесть на стол спиной к Бифу. (disabled)":
                        pass
                    "Сесть на стол, достать член Бифа и взять его в рот. (disabled)":
                        pass
                    "Сесть на стол. достать член Бифа и возить им по киске. (disabled)":
                        pass
                    "Сесть на стол, достать член Бифа и вставить его в свою киску. (disabled)":
                        pass
                    "Сесть на стол, достать член Бифа и вставить его в анальное отверстие. (disabled)":
                        pass
                    "Назад.":
                        jump gallery_8442_1
            "Раздеться и сесть на Бифа.":
                menu:
                    "Сесть к Бифу на коленки лицом к нему. (disabled)":
                        pass
                    "Сесть к Бифу на коленки спиной. (disabled)":
                        pass
                    "Сесть Бифу киской на лицо. (disabled)":
                        pass
                    "Достать член Бифа и сесть на него лицом к Бифу (disabled)":
                        pass
                    "Достать член Бифа и сесть на него спиной к Бифу (disabled)":
                        pass
                    "Достать член Бифа и сесть на него анальным отверстием (disabled)":
                        pass
                    "Полизать папочке зад. (disabled)":
                        pass
                    "Назад.":
                        jump gallery_8442_1
            "Позвать секретаршу.":
                label gallery_8442_2:
                    menu:
                        "Поцеловать секретаршу. (disabled)":
                            pass
                        "Полизать секретарше грудь. (disabled)":
                            pass
                        "Полизать секретарше киску. (disabled)":
                            pass
                        "Засунуть секретарше язык глубоко в анальное отверстие. (disabled)":
                            pass
                        "Достать член Бифа и засунуть его в секретаршу. (disabled)":
                            pass
                        "Засунуть член в ее киску, затем вытащить и облизать его. (disabled)":
                            pass
                        "Засунуть член в ее анальное отверстие, затем вытащить и облизать его. (disabled)":
                            pass
#                        "Назад.":
#                                jump gallery_8442_2
                        "Назад.":
                            jump gallery_8442_1
    return

label gallery_13920:
# Если Моника заходит сразу же, то происходит диалог с Бифом после сдачи отчетов. Если не приходит в этот вечер, то диалог пропадает.
# Диалог с Бифом после сдачи отчета:
# Биф спрашивает что цыпочка хорошая? Цыпочка принесла отчеты?
# Моника выбирает притвориться цыпочкой или нет
    music Groove2_85
    img 13902
    with fade
    biff "Цыпочка принесла отчеты?" #-
    biff "Цыпочка сегодня хорошая?"
# Если притворяется цыпочкой, то комментирует что ей надо притвориться цыпочкой - это поможет поднять доверие Бифа, она сможет иметь больший доступ в офисе и придумает
# как вернуть все назад
# Если не притворяться, то тоже думает, но говорит что это черезчур такому Боссу как она притворяться цыпочкой
# Говорит что цыпочка хорошая и что она сдала отчеты, как просил папочка
    img 13903
    with diss
    menu:
        "Притвориться хорошей цыпочкой.":
            img 12813
            with fade
            mt "Мне надо притвориться цыпочкой." #+
            mt "Это поможет поднять доверие Бифа и я смогу иметь больший доступ в офисе."
            mt "Это поможет мне вернуть все назад..."
            music Hidden_Agenda
            img 13904
            with diss
            m "Да, цыпочка хорошая..." #-
            m "Цыпочка собрала все отчеты..."
# Бифф говорит что цыпочка должна развлечь папочку. Кто сегодня цыпочка?
# Моника отвечает что сегодня цыпочка - это важный Босс и она пришла показать грудь или попу
# Биф отвечает что папочка доволен и что цыпочка может и дальше работать в их прекрасной компании
# Моника уходит и думает что в ее компании, сволочь!
# У Бифа идет прогресс
            img 13906
            biff "Хорошая цыпочка должна развлечь папочку." #-
            biff "Кто сегодня цыпочка?"
            img 12789
            with diss
            m "Сегодня цыпочка - это важный Босс." #-
            m "У цыпочки свой отдел. Цыпочка очень довольна."
            img 13905
            with diss
            biff "Что цыпочка-Босс решила показать сегодня папочке?" #+
            menu:
                "Показать грудь.": # corruption
                    img 12783
                    with fade
                    m "Сегодня цыпочка-Босс пришла показать папочке свою грудь..." #-
                    # Показывает грудь (нексолько кадров)
                    music Loved_Up
                    sound snd_fabric1
                    img 13917
                    with fadelong
                    w
                    img 13918
                    with diss
                    w
                    img 13919
                    with diss
                    w
                    img 13920
                    with diss
                    w
                    img 12844
                    with fade
                    biff "Папочка доволен." #+

                "Показать попу.": #corruption
                    label gallery_20599:
                    img 12783
                    with fade
                    m "Сегодня цыпочка-Босс пришла показать папочке свою попу..." #-
                    # Показывает Бифу попу (несколько кадров)
                    music Loved_Up
                    sound snd_fabric1
                    img 20595
                    with fadelong
                    w
                    img 20596
                    with diss
                    w
                    img 20597
                    with diss
                    w
                    img 20598
                    with diss
                    w
                    img 20599
                    with diss
                    w
                    img 20600
                    with diss
                    w
                    img 12844
                    with diss
                    biff "Папочка доволен." #+
                "Ничего.":
                    img 12789
                    with fade
                    m "Сегодня цыпочка пришла только показать папочке отчеты." #-
                    img 12875
                    with diss
                    biff "Ладно, цыпочка, у папочки все-равно сейчас нет времени." #+


        "Не притворяться." if monicaSaidBiffSheIsWillBeAGoodChick == False:
            img 13907
            with fade
            m "Биф, я собрала отчеты, потому что ты требуешь этого!" #-
            img 12907
            biff "Хорошо, цыпочка." #+
            biff "Продолжай вести себя хорошо."
        "Не притворяться. (Моника обещала быть хорошей цыпочкой) (disabled)" if monicaSaidBiffSheIsWillBeAGoodChick == True:
            pass
    img 12815
    with fade
    biff "Цыпочка может и дальше работать в моей прекрасной компании!" #-

    # Моника уходит
    music Power_Bots_Loop
    img 12817
    with diss
    mt "В моей компании, сволочь! В МОЕЙ!" #+
    return

############ PublicEvents 1############

label gallery_6700:
    #нажатие на Монику
    img 6696
    with fade
    m "..."
    img 6700
    mt "Черт! Что же мне делать?!"
    "Здесь столько прессы..."
    "Может быть объявить что мой журнал захватили?!"
    "Попросить помощи?"
    "Это опасно! Не представляю чем это может грозить!"
    "Возможно самым худшим... Но это единственный шанс..."
    "Очень рискованный!"
    "Что же мне делать???"
    menu:
        "Сказать всем правду!":
            music Power_Bots_Loop
            img 6701
            with fade
            m "Я - Моника Бакфетт!"
            "И я хочу объявить о преступлении, которое совершено в отношении меня!"
            img 6702
            music stop
            pause(1.0)
            sound microphone_off
            empty_name "Выключается микрофон."
            $ renpy.pause(1.0, hard=True)
            music Power_Bots_Loop
            img 6703
            m "Меня незаконно обвинили в том, чего я не совершала!"
            "У меня отняли счета и документы!"
            "И теперь шантажируют, заставляя говорить немыслимые вещи!"
            "Помогите мне!!!"
            #затемнение. спустя несколько часов
            music stop
            img black_screen
            with Dissolve(2.0)
            call textonblack(_("Несколько часов спустя..."))
            img black_screen
            with Dissolve(2.0)
            music Gearhead
            img 2530
            with fadelong
            marcus "Что-ж, Миссис Бакфетт!"
            "Хорошая попытка!"
            img 2533
            "Должен признать Вам что я проиграл."
            img 2542
            m "..."
            img 2533
            with fade
            marcus "Да, я проиграл лучший виски на моем ранчо!"
            img 2571
            "Вы продержались больше одного дня!"
            "И Вы вернулись сюда... Феерично!"
            img 2563
            with fade
            "Вы отправитесь на Ранчо прямо из этого кабинета..."
            img 2572
            sound snd_woman_scream2
            m "НЕЕЕЕЕТ!!!"
            music stop
            call textonblack(_("Продолжение следует..."))
            img black_screen
            with Dissolve(1)
            $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))
            # конец игры
            return

        "Подыграть Бифу. Если я хочу все вернуть назад, то надо быть хитрее...":
            mt "Нет, это слишком рискованно!"
            "Дик говорил что все что со мной сделали - законно."
            "А это значит что я лишь наврежу себе!"
            "Мне надо сказать эти гребаные слова и заработать деньги на чертов галстук!"

            img 6704
            with fade
            m "..."
            m "Я - Моника Бакфетт!"
            "И я подтверждаю слова Мистера Бифа!"
            "Наш журнал изменит свой курс!"

            #ропот в зале
            sound audience_wow
            img 6705
            with fade
            m "..."
            biff "Ну, курица! Скажи что-нибудь еще!!!"

            img 6706
            with fade
            mt "!!!"

            img 6707
            with fade
            m "Старый курс морально устарел..."
            "Новые времена диктуют новые тренды..."
            img 6708
            "Я благодарна Мистеру Бифу за новые идеи..."
            "Наш журнал должен преобразиться..."
            sound applause1
            "Спасибо Вам за то что Вы пришли..."

            img 6709
            with fade
            biff "Молодец, цыпочка!"
            "Продолжай играть!"

            #появляется рецепшин и смотрит на Монику
            music Hidden_Agenda
            img 6710
            with fadelong
            reception_t "Не понимаю..."
            "Она выступает на сцене..."
            img 6711
            with fade
            sound applause2
            "Неужели она правда Леди?"
            "Но этого не может быть!"
            img 6712
            "Мое чутье никогда не обманывало меня!"

            music
            hide screen Reporters_Shoots_Screen2
            hide screen Reporters_Shoots_Screen
            hide screen Reporters_Shoots_Screen3
            show screen Reporters_Shoots_Screen
#            show screen Reporters_Shoots_Screen3
            music audience
            #меняется фон, Моника внизу отвечает на вопросы журналистов
            img 6713
            with fadelong
            reporter1 "Миссис Бакфетт!"
            "Скажите! Почему Вы решили сменить курс?"
            reporter2 "Скажите! Вы готовы поддержать новый курс собственным примером?"
            reporter3 "Мы слышали что Вы только что провели фотосессию!"
            "Вы решили сняться обнаженной?"
            img 6714
            with fade
            m "Нет, что вы?"
            "Это всего-лишь курс журнала!"
            "Я не собираюсь сниматься обнаженной!"
            "Я - Леди!"
            "И у меня есть достоинство!"
            hide screen Reporters_Shoots_Screen
            show screen Reporters_Shoots_Screen2
            img 6715
            with fadelong
            reporter1 "Но мы слышали что это необычная фотосессия!"
            "Мы слышали что эта фотосессия достаточно смелая!"
            reporter3 "Расскажите про фотосессию, Миссис Бакфетт!"
            img 6716
            m "Ой! Что Вы? Это обычная фотосессия!"
            reporter2 "Мы слышали что вы принимали необычные позы!"
            img 6717
            m "Ничего особенного..."
            "Просто небольшой смелый эксперимент..."
            img 6718
            reporter1 "Собираетесь-ли Вы продолжать эксперименты?"
            reporter3 "Многие хотели-бы увидеть больше!"
            hide screen Reporters_Shoots_Screen
            hide screen Reporters_Shoots_Screen2
            hide screen Reporters_Shoots_Screen3
            music Power_Bots_Loop
            img 6719
            m "Нет..."
            "Это разовый случай..."
            "Скажите этим МНОГИМ что они могут не рассчитывать на большее!"
            "Интервью закончено!"
            reporter1 "Спасибо, Миссис Бакфетт!"
            return
        "Еще подумать...":
            return
    return

label gallery_6757:
    #render
    #Секретарша сидит за столом, общение с Моникой
    music Groove2_85
    img 8205
    with fade
    dick_secretary "Миссис Бакфетт!"
    "Как Вам эта сумочка?"
    img 8206
    with fade
    "Вам она нравится? Или нет?"


    img 8207
    with fade
    w
    # Воспоминания
    # Если Моника была с Филипом, то события Филипа
    music stop
    img white_screen
    with Dissolve(1.0)
    pause 1.0
    if monicaMadeBlowjobToPhilip == True:
        music Gearhead
        if monicaMadeBlowjobToHotelStaff == True:
            img 6996
            with Dissolve(0.7)
            philip "Давай! Засунь свой член туда!"
            img 7004
            philip "Миссис Бакфетт не может ждать!"
            "Она хочет скорее твой член!"
            img 7006
            philip "Решайся, Малыш!"
            "Иначе это сделает следующий кто войдет сюда!"

            img 7022
            with fade
            philip "Я кое-что забыл..."

            img 7030
            with fade
            philip "Теперь глотай!"

            img 7034
            philip "Покажи рот! Покажи что ты все проглотила!"
            img 7035
            w
            img 7043
            with fadelong
            w
        else:
            img 6936
            with Dissolve(0.7)
            philip "Спасибо, Моника Бакфетт!"
            img 6938
            philip "Вы заработали свои $ 500!"
            img 6943
            with fade
            m "Мне нужно еще $ 500!"
            "Пожалуйста! Прошу Вас!!!"
            img 6954
            with fade
            philip "Это не аргумент, Миссис Бакфетт!"
            "Что Вы можете предложить взамен?"
    else:
        # Если была с Бифом, то события про цыпочку
        music Hidden_Agenda
        img 6754
        with Dissolve(0.7)
        m "Биф, пожалуйста, дай деньги. Я буду хорошей цыпочкой..."
        img 6755
        m "Я буду исправно сниматься в фотосессиях и..."
        img 6757
        "Буду послушной..."

    #
    img white_screen
    with Dissolve(0.5)
    pause 1.0
    music Groove2_85
    img 8206
    with Dissolve(0.8)
    dick_secretary "Я Вас слушаю!"
    img 8208
    with fade
    m "Ддда... Мне нравится эта сумочка, Мисс Виктория..."
    "У Вас хороший вкус..."

    img 8209
    dick_secretary "Я подумываю в следующую пятницу купить еще что-нибудь, когда Вы принесете деньги."
    "У Вас тоже есть вкус, возможно я даже посоветуюсь с Вами."
    "Миссис Бакфетт, вы же дадите совет мне?"
    img 8208
    m "Да... Дам..."
    img 8210
    with fade
    m "..."
    m "Виктория..."
    dick_secretary "Мисс Виктория!!!"
    m "Мисс Виктория, скажите. Если у меня не будет наличных, то как мне доставить Вам эти деньги?"
    img 8211
    dick_secretary "Нет проблем, Миссис Бакфетт!"
    "Просто купите в интернете сертификат на это имя и адрес email..." #Дает бумажку
    img 8212
    with fade
    m "Я поняла, спасибо..."
    return

label gallery_6875:
    #render
    #Моника обращается к Филиппу с танцем повторно
    $ store_music()
    music Groove2_85
    img 6864
    with fade
    w
    img 6865
    with fade
    philip "Да, Мэм?"
    "Вы надумали еще потанцевать?"

    menu:
        "Да, давай еще потанцуем.":
            pass
        "Уйти.":
            img 6866
            with fade
            m "Нет!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            $ restore_music()
            return

    m "Да, давай еще потанцуем."

    #танцуют
    #музыка
    music Last_Kiss_Goodnight
    img 6867
    with fadelong
    w
    img 6868
    with fade
    philip "Мэм! Продолжим наш светский разговор по поводу Вашего ротика?"

    img 6869
    w
    menu:
        "Я не собираюсь про это говорить!":
            music Groove2_85
            img 6870
            with fade
            m "Я не собираюсь про это говорить!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            $ restore_music()
            return
        "Хх... Хорошо... Филипп...":
            pass


    m "Хх... Хорошо... Филипп..."
    "Давай поговорим про это..."

    img 6871
    with fade
    philip "Итак... Миссис Бакфетт!"
    "$ 500 и мой член в Вашем прекрасном ротике!"

    img 6872
    m "$ 10.000, Филипп..."
    img 6873
    philip "$ 500, Миссис Бакфетт! Сегодня Ваш ротик не стоит больше..."
    "Это как на Бирже! Я покупаю акции на низкой цене!"

    img 6874
    m "Мне нужна хотя бы $ 1.000, Филипп!"

    img 6875
    philip "$ 500, Миссис Бакфетт!"
    "Ваш ротик слишком долго говорит! Скоро он начнет дешеветь!"

    music Villainous_Treachery
    img 6876
    m "$ 1.000!!!"
    "Мне никак нельзя меньше!"
    img 6877
    "(хмык)"
    img 6878
    philip "Миссис Бакфетт!"
    "Эта гостиница предоставляет разнообразные услуги!"
    "Я начинаю торопиться и скоро уже ухожу!"
    img 6879
    "Перед уходом мой член побывает в чьем-нибудь ротике!"
    "В Вашем, либо в каком-то другом!"

    img 6880
    m "..." #переживает

    img 6881
    philip "Ну так в чьем?"
    philip "Решайте скорее!"

    img 6882
    m "..."

    img 6883
    philip "Ну?!"

    img 6882
    menu:
        "В МОЕМ! (хмык)":
            pass
        "Мне... Мне надо подумать!":
            music Groove2_85
            img 6884
            with fade
            m "Мне... Мне надо подумать!"
            philip "Мэм! Спасибо за танец!"
            "Если захотите потанцевать еще, то пригласите меня!"
            $ restore_music()
            return

    music Power_Bots_Loop
    img 6885
    with fade
    m "В МОЕМ!" #очень переживает
    mt "(хмык)"
    img 6886
    w
    music Last_Kiss_Goodnight
    img 6887
    with fade
    philip "Хорошо, Миссис Бакфетт!"
    img 6888
    sound Jump2
    "Давайте еще немного потанцуем!"
    img 6889
    "Я хочу сделать это до того как испорчу помаду у Вас на губах!"

    #танцуют
    img 6890
    with Dissolve(0.5)
    w
    img 6891
    with Dissolve(0.5)
    w
    img 6892
    with Dissolve(0.5)
    w
    img 6893
    with Dissolve(0.5)
    w
    img 6894
    with Dissolve(0.5)
    w

    img 6895
    with fade
    philip "Мне нравится этот танец!"
    "Мне доставляет удовольствием наблюдать за Вашим ротиком!"
    "Ведь через 5 минут мой член будет глубоко в нем!"

    img 6896
    with fade
    mt "!!!"
    philip "Танцевать при таких обстоятельствах доставляет мне эстетическое удовольствие!"

    img 6897
    mt "!!!"

    img 6891
    with Dissolve(0.5)
    w
    img 6892
    with Dissolve(0.5)
    w
    img 6893
    with Dissolve(0.5)
    w

    music Groove2_85
    img 6898
    with fade
    philip "Достаточно! Пришла пора испортить Ваш макияж, Миссис Бакфетт!"
    img 6899
    "Идемте!"

    $ restore_music()
    return

label gallery_6915:
    music Groove2_85
    #render
    #Туалет. Моника. Филипп
    sound highheels_short_walk
    img 6900
    with fadelong
    m "Куда ты меня привел, Филипп?"
    "Это мужской туалет!"
    img 6901
    philip "Миссис Бакфетт!"
    "Мне будет неудобно находиться в женском туалете!"
    img 6902
    "Ну а для Вас, полагаю, нет никакой разницы, ведь так?"
    m "Я думала это будет хотя бы гостиничный номер!"
    img 6903
    philip "О, Мэм!"
    "Гостиничный номер будет стоить гораздо дороже Вашего ротика!"
    "Как Вы знаете, я умею считать деньги!"
    "Поэтому туалет как раз подойдет для этой цели!"

    img 6904
    mt "!!!"

    img 6905
    with fade
    philip "Итак, Миссис Бакфетт!"
    "Садитесь на колени! Вам будет неудобно принимать мой член стоя!"
    img 6906
    w
    img 6907
    w
    label gallery_6915_1:
        menu:
            "Сесть на колени. (corruption)" if corruption >= monicaPhilipBlojwobKneesCorruptionRequired:
                pass
            "Сесть на колени. (low corruption, required [monicaPhilipBlojwobKneesCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobKneesCorruptionRequired:
                jump gallery_6915_1
            "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!!":
                img 6904
                with fade
                m "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!!"
                return
    img 6908
    with fade
    mt "У меня нет времени!"
    "Это единственный выход!"
    "(хмык)"
    img 6909
    philip "Ну!?"
    "Я жду!!!"

    #Моника садится
    img 6910
    with Dissolve(1.0)
    w
    img 6911
    philip "Хорошая девочка..."
    sound snd_fabric1
    #звук раздевания
    img 6912
    with fadelong
    w
    #звук расстегивания змейки
    sound snd_zip
    img 6913
    w
    img 6914
    with fade
    w
    img 6915
    with Dissolve(0.5)
    w

    #Филипп подносит член ко рту
    img 6916
    w
    img 6917
    w
    philip "Миссис Бакфетт! Я попрошу Вас открыть свой ротик!"
    "Я мог бы сделать это своим членом..."

    "Но я привык к комфорту!"
    "Я привык что женщины сами открывают свой ротик чтобы принять мой член внутрь!"

    img 6918
    with fade
    mt "!!!"

    label gallery_6915_2:
        menu:
            "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!! (убежать)":
                music Pyro_Flow
                img 7052
                with fade
                m "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!!"
                philip "Мэм! Куда-же ВЫ?!"
                "Мы ведь только начали!"
                #уходим в hall без филиппа и helper'а
                return
            "Открыть рот... (corruption)" if corruption >= monicaPhilipBlojwobOpenMouthCorruptionRequired:
                pass
            "Открыть рот... (low corruption, required [monicaPhilipBlojwobOpenMouthCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobOpenMouthCorruptionRequired:
                jump gallery_6915_2

    #Моника открывает рот
    img 6919
    with Dissolve(0.5)
    w

    img 6920
    philip "Миссис Бакфетт!"
    "Не могли-бы Вы пошире открыть его?"
    img 6921
    "Наверное Вам оттуда плохо видно..."
    "Но поверьте, мне отсюда видно хорошо!"
    img 6922
    "Ваш ротик недостаточно открыт для того чтобы мой член комфортно вошел в него!"
    label gallery_6915_3:
        menu:
            "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!! (убежать)":
                music Pyro_Flow
                img 7052
                with fade
                m "Я НЕ СОБИРАЮСЬ ЭТОГО ДЕЛАТЬ!!!"
                philip "Мэм! Куда-же ВЫ?!"
                "Мы ведь только начали!"
                #уходим в hall без филиппа и helper'а
                return
            "Делать все что говорит Филипп. У меня нет выхода. Мне нужны эти деньги!!! (corruption)" if corruption >= monicaPhilipBlojwobOpenMouth2CorruptionRequired:
                pass
            "Делать все что говорит Филипп. У меня нет выхода. Мне нужны эти деньги!!! (low corruption, required [monicaPhilipBlojwobOpenMouth2CorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobOpenMouth2CorruptionRequired:
                jump gallery_6915_3
    img 6923
    with Dissolve(0.5)
    w
    img 6924
    with fade
    w
    img 6925
    with fade
    w
    img 6926
    with fade
    w
    music stop
    img 6927
    with fade
    w

    # звук хлюпания, вход члена в рот
    sound hlup19
    img 6928 #?????
    w


    music stop
    #video

    #Моника открывает рот сильнее
    #идет видео минета

    #идет видео минета
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_1 = Movie(play="video/v_Monica_Philip_Blowjob_1_1.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_1
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_2 = Movie(play="video/v_Monica_Philip_Blowjob_1_2.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_2
    philip "Миссис Бакфетт!"
    "Отлично!"
    "Чувствуется что у Вас недостаток практики!"
    "Но мне это даже нравится!"
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_3 = Movie(play="video/v_Monica_Philip_Blowjob_1_3.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_4 = Movie(play="video/v_Monica_Philip_Blowjob_1_4.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_4
    "Если честно, я сомневался что Ваш ротик стоит $ 500!"
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_5 = Movie(play="video/v_Monica_Philip_Blowjob_1_5.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_6 = Movie(play="video/v_Monica_Philip_Blowjob_1_6.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_6
    "Я думал что ему больше подходит цена в $ 300!"
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_7 = Movie(play="video/v_Monica_Philip_Blowjob_1_7.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_7
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_8 = Movie(play="video/v_Monica_Philip_Blowjob_1_8.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_8
    "Но нет!"
    "Теперь я уверен что $ 500 он стоит вполне!"
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_9 = Movie(play="video/v_Monica_Philip_Blowjob_1_9.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_9
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_10 = Movie(play="video/v_Monica_Philip_Blowjob_1_10.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_10
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_11 = Movie(play="video/v_Monica_Philip_Blowjob_1_11.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_11
    wclean
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_12 = Movie(play="video/v_Monica_Philip_Blowjob_1_12.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_12 #????
    wclean



    #заглядывает рецепшин
    music Hidden_Agenda
    sound snd_door_open1
    img 6929
    with fade
    w
    img 6930
    w
    music Hidden_Agenda
    img 6931
    reception_t "Ага!"
    "А я уже начала было сомневаться в своем чутье!"
    "Эта шлюха искусно маскируется!"
    #видео 13
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_13 = Movie(play="video/v_Monica_Philip_Blowjob_1_13.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_13
    wclean
    music stop
    music Hidden_Agenda
    img 6933
    "Я почти поверила что она Леди!"
    "В нашей гостинице запрещено заниматься проституцией без разрешения!"
    #видео 14
    stop music
    play music "<from " + str((rand(1,3)*1.5)) + " loop 0.0>Sounds/v_Monica_Philip_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Philip_Blowjob_1_14 = Movie(play="video/v_Monica_Philip_Blowjob_1_14.mkv", fps=30)
    show videov_Monica_Philip_Blowjob_1_14
    wclean
    music stop
    music Hidden_Agenda
    img 6932
    "В прошлый раз она приходила с такой же целью, могу поспорить!"


    music Groove2_85
    img 6934
    with fade
    w
    # звук кончания в рот Филиппом
    sound bulk1
    philip "АААААААРРГГГХХХ!!!"
    img 6935
    w
    # звук кончания в рот Филиппом
    img 6936
    with fade
    sound bulk1
    philip "АААААААРРГГГХХХ!!!"

    #Моника сидит со спермой
    img 6937
    with fadelong
    w
    img 6938
    w
    img 6939
    with fade
    w

    img 6940
    philip "Спасибо, Моника Бакфетт!"
    philip "Вы заработали свои $ 500!"

    menu:
        "Пожалуйста, дайте еще $ 500!!!":
            pass

    img 6941
    m "Еще $ 500!"
    img 6942
    philip "?"

    img 6943
    m "Мне нужно еще $ 500!"
    img 6944
    "Пожалуйста! Прошу Вас!!!"

    img 6945
    philip "Миссис Бакфетт!"
    "Почему я должен давать Вам еще $ 500?"
    img 6946
    m "Мне очень надо! ОЧЕНЬ!!!"
    img 6945
    philip "Это не аргумент, Миссис Бакфетт!"
    "Что Вы можете предложить взамен?"

    img 6946
    label gallery_6915_4:
        menu:
            "Я могу сделать это еще раз... (corruption)" if corruption >= monicaPhilipBlojwobOpenOfferedAgainCorruptionRequired:
                img 6947
                with fade
                m "Мистер..."
                img 6948
                with Dissolve(0.5)
                "Я могу..."
                "Я могу сделать это еще раз..."
                img 6949
                with Dissolve(0.5)
                "Вы дадите мне еще $ 500..."
                img 6950
                philip "Мэм! Я говорил Вам про то что люблю женщин!"
                "Женщины не стареют и не теряют своей цены, потому что..."
                img 6951
                "Потому что они разные! Разные женщины, Мэм!"
                "Я никогда! Никогда не вставляю два раза член в одну и ту же женщину!"
                "Благодаря этому правилу их у меня много и я могу наслаждаться их вкусом!"
                img 6952
                m "Но пожалуйста, Мистер!"
                # звук пальца в ротике Моники
                sound squelch9
                img 6953
                philip "Миссис Бакфетт! Я уже купил Ваш ротик!"
                img 6954
                "Я не собираюсь еще раз покупать его!!!"
            "Я могу сделать это еще раз... (low corruption, required [monicaPhilipBlojwobOpenOfferedAgainCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobOpenOfferedAgainCorruptionRequired:
                jump gallery_6915_4
            "Я не знаю... Мне нечего предложить...":
                img 6955
                m "Мне нечего предложить, но пожалуйста!"
                "Мистер!"
                "Для меня это жизнь или смерть!"

    img 6956
    with fade
    philip "Хотя..."
    "Знаете что..."
    music Power_Bots_Loop
    "Вы сделаете миньет первому мужчине, который зайдет сюда!"
    "Тогда Вы получите еще $ 500!"
    img 6957
    "Вы согласны?"

    m "Я... Я..."

    music Groove2_85
    #Заходит hotel_staff
    sound snd_door_open1
    img 6958
    hotel_staff "Ой!"
    img 6959
    with fade
    "Прошу прощения за беспокойство!"
    "Я зайду позже!"
    philip "Эй! Парень!"
    "Постой-ка!"

    img 6960
    with Dissolve(0.5)
    hotel_staff "Да, Сэр?"
    philip "Иди-ка сюда!"

    hotel_staff "Да, Сэр? Чем могу быть полезен?"
    img 6961
    philip "У тебя есть член, парень?"
    hotel_staff "Что Вы имеете ввиду, Сэр?"

    img 6962
    philip "Член! Есть член у тебя?!"
    "Я имею ввиду ту штуку что должна быть в штанах у каждого мужчины!"
    "Есть она у тебя или ее нет?"

    img 6963
    hotel_staff "Сэр... Конечно есть..."
    "Но я не понимаю зачем этот вопрос."
    "Я могу как-то помочь Вам?"

    img 6964
    philip "Да, парень!"
    "Открой глаза и посмотри!"
    "У меня здесь сидит сучка и сосет бесплатно члены!"
    "У тех кто сюда заходит!"

    img 6965
    "Для тебя бесплатно, конечно."
    "Для меня это кое-что стоит, но я готов потратить эти деньги для такого удовольствия."

    img 6966
    with fade
    "Ты только посмотри кто это!"
    sound Jump2
    img 6967
    hotel_staff "МИССИС БАКФЕТТ?!?!" #смотрит с ужасом

    #если Моника была зла к нему, то:
    img 6968
    #

    img 6969 #+
    philip "Да, это она!"
    "Парень! Такой шанс выпадает только раз!"
    "Ты счастливчик!"

    img 6970
    with Dissolve(0.5)
    "Моника Бакфетт сидит в туалете и ждет твой член!"
    "Она ждет его!"
    "Ее ротик приглашает твой член! Чтобы ты вставил его!"

    #обращается к Монике
    img 6971
    philip "Ну-ка открой свой ротик!"
    label gallery_6915_5:
        menu:
            "Открыть рот для нового члена. (corruption)" if corruption >= monicaPhilipBlojwobOpenMouthAgainCorruptionRequired:
                img 6978
                with Dissolve(0.5)
                w
                philip "Давай, парень!"
                img 6977
                philip "Этот ротик приглашает тебя!"

            "Открыть рот для нового члена. (low corruption, required [monicaPhilipBlojwobOpenMouthAgainCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobOpenMouthAgainCorruptionRequired:
                jump gallery_6915_5
            "Не открывать самой...":
                img 6972
                with fade
                w
                img 6973
                "Приглашай его член!"
                img 6974
                w
                img 6973
                "Приглашай его член!"
                "Иначе не получишь деньги!"
                music stop
                img 6975
                w
                #Моника открывает рот
                #звук открывания рта пальцем Филиппа
                sound squelch9
                img 6976
                with Dissolve(0.5)
                w
                music Groove2_85
                img 6977
                philip "Давай, парень!"
                img 6978
                with fade
                philip "Этот ротик приглашает тебя!"
    img 6979
    philip "Видишь?"
    img 6980
    w
    img 6981
    w
    img 6980
    w
    img 6982
    w
    img 6980
    w
    label gallery_6996:
    img 6983
    philip "Давай! Засунь свой член туда!"
    img 6980
    w
    img 6984
    with fade
    w
    philip "Засовывай же скорее!"
    img 6985
    philip "Миссис Бакфетт не может ждать!"
    "Она хочет скорее твой член!"
    img 6986
    philip "Решайся, Малыш!"
    "Иначе это сделает следующий кто войдет сюда!"
    img 6987
    philip "Этот ротик не уйдет отсюда, пока не попробует еще какой-нибудь член!"
    img 6988
    philip "Мой член только что проверил! Там внутри все очень комфортно!"

    #парень смотрит в ужасе

    #если Моника была добра к нему
    if hotelStaffOffended1 == False:
        img 6990
        hotel_staff "Сэр!"
        "Но я не могу этого сделать!"
        "Эта женщина была добра ко мне!"
        "Пожалуйста, дайте ей то что она хочет!"

        img 6989
        philip "Ха-ха!"
        "Ладно, парень, как хочешь!"
        #смотрит на Монику
        img 6991
        with fade
        philip "Можешь закрыть свой ротик! Ты заслужила свои деньги!"
        #Моника закрывает рот
        img 6992
        with Dissolve(0.5)
        return

    #если Моника была зла к нему

    img 6993
    hotel_staff "А ведь она собиралась уволить меня!"
    philip "Ха-ха!"
    "Тем более!"
    sound snd_zip
    img 6994
    with fade
    "Этот ротик заслужил твой член!"
    "Давай! Вставь его! Скорее!"
    #звук одежды
    sound snd_zip
    img 6995
    with fade
    w
    img 6996
    w
    img 6997
    with fade
    w
    img 6998
    with Dissolve(0.5)
    w
    img 6999
    w
    label gallery_6996_1:
        img 7000
        philip "Открой рот! Приглашай его член в себя!"
        "Иначе не получишь деньги!!!"
        img 7001
        w
        #выбор делать или нет и повтор
        menu:
            "Открыть рот. Я решила делать все что говорит Филипп. Если я не достану эти деньги, то мне конец!":
                pass
            "Я не могу это сделать...":
                mt "Если я не получу эти деньги, то завтра попаду в руки Маркуса!"
                "О БОЖЕ!!!"
                jump gallery_6996_1
    img 7002
    with fadelong
    w
    img 7003
    with Dissolve(0.5)
    w
    img 7004
    with Dissolve(0.5)
    w
    img 7005
    with fade
    w
    img 7006
    w
    img 7007
    w
    img 7008
    w
    img 7009
    hotel_staff "А она ничего мне потом не сделает за это?"
    philip "Парень! Она не сделает тебе ничего!"
    img 7010
    with fade
    hotel_staff "Правда, Сэр?"
    philip "Правда, малыш!"
    "Сделай движение вперед, не бойся!"
    music stop
    hotel_staff "Хорошо, Сэр..."
    #чавкающий звук
    # звук входа члена в Моникин рот
    sound hlup19
    img 7011
    with Dissolve(0.5)
    w
    music Groove2_85
    philip "Смелее, малыш!"
    img 7012
    music stop
    hotel_staff "Хорошо, Сэр..."
    #чавкающий звук
    # звук чавкающий
    sound hlup25
    img 7013
    with Dissolve(0.5)
    w
    music Groove2_85
    img 7014
    hotel_staff "Так, Сэр?"
    philip "Долби ее в ротик!"
    "Чего ты с ней возишься?!"

    #парень начинает ее долбить
    #видео
    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_1 = Movie(play="video/v_Monica_Helper_Blowjob_1_1.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_1
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_2 = Movie(play="video/v_Monica_Helper_Blowjob_1_2.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_2
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_3 = Movie(play="video/v_Monica_Helper_Blowjob_1_3.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_4 = Movie(play="video/v_Monica_Helper_Blowjob_1_4.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_5 = Movie(play="video/v_Monica_Helper_Blowjob_1_5.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_5
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_6 = Movie(play="video/v_Monica_Helper_Blowjob_1_6.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_6
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_7 = Movie(play="video/v_Monica_Helper_Blowjob_1_7.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_7
    hotel_staff "Простите, Мэм!"
    "Пожалуйста, не увольняйте меня!"
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_8 = Movie(play="video/v_Monica_Helper_Blowjob_1_8.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_8
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_9 = Movie(play="video/v_Monica_Helper_Blowjob_1_9.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_9
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_10 = Movie(play="video/v_Monica_Helper_Blowjob_1_10.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_10
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_11 = Movie(play="video/v_Monica_Helper_Blowjob_1_11.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_11
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_12 = Movie(play="video/v_Monica_Helper_Blowjob_1_12.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_12
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_13 = Movie(play="video/v_Monica_Helper_Blowjob_1_13.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_13
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/v_Monica_Helper_Blowjob_1_sound.ogg"
    scene black
    image videov_Monica_Helper_Blowjob_1_14 = Movie(play="video/v_Monica_Helper_Blowjob_1_14.mkv", fps=30)
    show videov_Monica_Helper_Blowjob_1_14
    wclean
#    "Я обязательно учту Ваши пожелания по поводу постера в следующий раз!"


    #парень кончает
    # звук кончания Монике в рот
    img 7015
    with fade
    hotel_staff "Иииииииииииии!!!"
    sound bulk1
    w

    music stop
    music Groove2_85
    img 7016
    with fade
    hotel_staff "Сэр, я могу идти?"
    img 7017
    philip "Сядь и открой рот!"
    "Я не говорил тебе его закрывать!"
    menu:
        "Делать как сказал Филипп...":
            pass
    img 7018
    with fade
    w
    img 7019
    with Dissolve(0.5)
    w
    sound man_steps
    img 7020
    with fadelong
    w
    img 7021
    philip "Я кое-что забыл..."

    music stop
    img 7022
    with fade
    w
    # звук слизи1
    img 7023
    with Dissolve(0.5)
    w
    sound hlup10
    # звук слизи2
    img 7024
    with Dissolve(0.5)
    w
    music Groove2_85
    img 7025
    with fade
    philip "Теперь глотай!"
    img 7026
    w
    img 7027
    philip "Глотай! И наша сделка закрыта!"
    label gallery_6996_2:
        menu:
            "Проглотить сперму двух мужчин... (corruption)" if corruption >= monicaPhilipBlojwobTakeSpermCorruptionRequired:
                #звук глотания
                music stop
                img 7028
                with fade
                w
                sound snd_gulp
                w
                music Groove2_85
                img 7031
                with fade
                philip "Покажи рот! Покажи что ты все проглотила!"
                "Иначе никакой сделки!"
                img 7033
                with Dissolve(0.5)
                w
                img 7034
                with Dissolve(0.5)
                w
                img 7035
                philip "Отлично, спасибо."
            "Проглотить сперму двух мужчин... (low corruption, required [monicaPhilipBlojwobTakeSpermCorruptionRequired]) (disabled)" if corruption < monicaPhilipBlojwobTakeSpermCorruptionRequired:
                jump gallery_6996_2
            "Притвориться что проглотила...":
                img 7028
                with fade
                w
                img 7029
                philip "Еще глоток! Там наверняка что-то осталось!!!"
                #звук глотания
#                sound snd_gulp
                img 7030
                w
                img 7031
                with fade
                philip "Покажи рот! Покажи что ты все проглотила!"
                "Иначе никакой сделки!"
                #если не проглотила, то выбор и звук глотания
                menu:
                    "Проглотить сперму по настоящему, иначе Филипп увидит и я не получу деньги...":
                        pass
                music stop
                img 7032
                with fade
                w
                sound snd_gulp
                w
                music Groove2_85
                img 7033
                with Dissolve(0.5)
                w
                img 7034
                with Dissolve(0.5)
                w
                img 7035
                philip "Отлично, спасибо."



    img 7036
    with fade
    philip "Иди, парень! Ты повеселил меня!"
    #звук одежды
    sound snd_fabric1
    img 7037
    with fadelong
    w
    #бросает деньги и они уходят
    sound snd_take_paper
    img 7038
    with fade
    philip "Вот Ваши деньги, Миссис Бакфетт!"
    img 7039
    "Я найду Вас когда захочу попробовать Вашу попку!"

    img 7040
    with fade
    m "Пожалуйста!"
    "Не говорите про это никому!!!"

    img 7041
    hotel_staff "Конечно, Мэм!"
    "Я никому не скажу!"

    #закрывается дверь
    sound snd_door_close1
    img 7042
    with fadelong
    mt "Что это?"
    "Деньги?"

    img 7043
    mt "Деньги!"

    img 7044
    mt "Это деньги!"
    "У меня теперь есть деньги для Дика!"
    "Я нашла их! Я сделала это!!!"

    img 7045
    with fade
    mt "Но что..."
    "ЧТО ЭТО БЫЛО???"
    "Я ДАЖЕ НЕ МОГУ ОСОЗНАТЬ ТОГО ЧТО ПРОИЗОШЛО!!!"
    "Это... ЭТО..."
    "У меня..."
    "У МЕНЯ НЕТ СЛОВ!!!"
    "ЧТО СО МНОЙ СДЕЛАЛИ???"
    "ИЗ-ЗА КАКОЙ-ТО ТЫСЯЧИ ДОЛЛАРОВ!!!"
    "МОНИКА, КАК ТЫ МОГЛА?!?!"

    img 7046
    mt "Но что мне оставалось делать?"
    "У меня был выбор между жизнью или смертью!!!"
    "..."
    "Но какая жизнь теперь после того что случилось???"

    img 7047
    with fade
    mt "Я, пожалуй, забуду о том что произошло здесь."
    "Даже если кто-то расскажет, все-равно этому никто не поверит!"
    "Что Моника Бакфетт могла сделать такое! Это звучит как абсурд!"

    #если Моника сучка
    if monicaBitch == True:
        music Pyro_Flow
        img 7048
        with fade
        mt "Ну а что касается того кто здесь был..."
        "Когда я решу свои небольшие проблемы, я найду Маркуса и узнаю у него..."
        "Наверняка есть какое-нибудь Ранчо 219 или что-то вроде того..."
        img 7049
        with fade
        mt "ДЛЯ МУЖЧИН!!!"
        "И кое-кто направится прямиком туда!!!"
        "И я не успокоюсь пока этого не случится!!!"
        "Никто не смеет сделать подобное с Моникой Бакфетт и остаться в живых!!!"
        "Клянусь!!!"
        #

    music Groove2_85
    img 7050
    with fade
    mt "Но что мне сейчас делать?"

    img 7051
    with Dissolve(0.5)
    mt "Мне надо умыться и {c}идти к Дику{/c}..."
    sound snd_water_hose
    #звук воды
    w
    return

############ Office 1############

label gallery_8285:
    #render
    #Моника разговаривает с секретаршей повторно
    if act == "l":
        return

    $ store_music()
    music Stealth_Groover
    if cloth == "Whore":
        img 8282
        with fade
        secretary "Мистер Биф лучше нас знает что нам необходимо."
        secretary "Мистер Биф заботится о нас..."
        img 8283
    if cloth == "CasualDress1":
        img 11242
        with fade
        secretary "Мистер Биф лучше нас знает что нам необходимо."
        secretary "Мистер Биф заботится о нас..."
        img 11243
    if cloth == "WorkingOutfit1":
        img 12771
        with fade
        secretary "Мистер Биф лучше нас знает что нам необходимо."
        secretary "Мистер Биф заботится о нас..."
        img 12772

    #если Моника сегодня не просила деньги, то появляется меню выбора
    menu:
        "Попросить деньги в долг.":
            "Дорогая..."
            secretary "Да, Миссис Бакфетт?"
            m "Скажи, у тебя не будет немного денег?"
            if cloth == "Whore":
                img 8284
            if cloth == "CasualDress1":
                img 11244
            if cloth == "WorkingOutfit1":
                img 12773

            with fade
            secretary "Миссис Бакфетт! Я пока не видела зарплаты здесь, после Вашего ухода..."
            #если у Моники меньше 5 долларов, то дает, иначе нет
            if money > 2:
                secretary "Поэтому у меня нет никаких денег сейчас, Миссис Бакфетт!"
                "Простите!"
                m "А как же Биф? Он что, не дает тебе деньги?"
                if cloth == "Whore":
                    img 8285
                if cloth == "CasualDress1":
                    img 11240
                if cloth == "WorkingOutfit1":
                    img 12769
                with fade
                secretary "Мистер Биф лучше нас знает что нам необходимо."
            else:
                #
                secretary "У меня есть только кредитная карточка, но мне надо платить за ипотечный кредит."
                "У меня есть $ 5 наличными и все..."
                m "Дорогуша, дай мне, пожалуйста, эти $ 5..."
                if cloth == "Whore":
                    img 8286
                if cloth == "CasualDress1":
                    img 11245
                if cloth == "WorkingOutfit1":
                    img 12774
                with fade
                secretary "Да, Миссис Бакфетт!"
                "Держите..."
                #дает 5 баксов

        "Дорогуша, ты не видела Мелани?" if melanieDisappeared == True:
            call gallery_8285_1()

        "Заставить секретаршу показать грудь в трущобах. (bitchiness)" if game.extra == True and ep27_quests_secretary1_show_boobs_active == True and pylonpart4startsCompleted == True and monicaWorkingAtBiffOffice == True:
            call gallery_13869()
            if _return == False:
                return
        "Уйти.":
            m "Не переживай, дорогуша!"
            "Я скоро вернусь!"
    $ restore_music()
    return

label gallery_8285_1:
    # Вопрос у секретарши: Где Мелани?
    # Секретарша отвечает что не видела ее и, может быть, Моника знает где она.
    music Groove2_85
    if cloth == "Whore":
        img 8268
        with fade
        m "Дорогуша, ты не видела Мелани?"
        img 8285
        secretary "Нет, Миссис Бакфетт."
        "Ее все ищут!"
        "Может быть Вы в курсе где она?"
        img 8270
        with fade
        m "Нет, дорогуша..."
        "Я... Я не имею представления где она может быть..."
    if cloth == "CasualDress1":
        img 11239
        with fade
        m "Дорогуша, ты не видела Мелани?"
        img 11240
        secretary "Нет, Миссис Бакфетт."
        "Ее все ищут!"
        "Может быть Вы в курсе где она?"
        img 11241
        with fade
        m "Нет, дорогуша..."
        "Я... Я не имею представления где она может быть..."
    if cloth == "WorkingOutfit1":
        img 12768
        with fade
        m "Дорогуша, ты не видела Мелани?"
        img 12769
        secretary "Нет, Миссис Бакфетт."
        "Ее все ищут!"
        "Может быть Вы в курсе где она?"
        img 12770
        with fade
        m "Нет, дорогуша..."
        "Я... Я не имею представления где она может быть..."
    return


label gallery_13869:
    # У пилона (Моника, секретарша, ситизен)
    imgl Dial_begin35_17
    imgr Dial_Citizen_4_1
    m "Привет! Помню, ты хотел познакомиться поближе?"
    imgr Dial_Citizen_4_3
    citizen4 "Конечно, давай познакомимся."
    m "Ну я не о близком знакомстве...Немного о другом."
    citizen4 "Да не вопрос, я понимаю о чем речь. Любой из нашего района тебя поймет с полуслова."

# Там Моника говорит ему что он обещал $ 50 за новую пару сисек.
# Тот отвечает что да, он заплатит $ 50, но только за новую пару малышек.
# Малышек Моники он уже видел!
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Hidden_Agenda
    img 13836
    with fadelong
    m "Ты говорил про то, что заплатишь $ 50 за новую пару сисек..."
    img 13837
    with diss
    citizen4 "Да, я помню!"
    citizen4 "Я заплачу $ 50, но только за новую пару малышек."
    citizen4 "Твоих малышек я уже видел!"
    music Power_Bots_Loop
    img 13838
    with hpunch
    mt "!!!"
# Секретарша спрашивает, Миссис Бакфетт, о чем говорит этот человек? Кто он?
# Моника говорит секретарше, чтобы та не задавала вопросов, что так надо.
# Говорит ситизену, что у нее есть с собой другая пара сисек и заплатит-ли он за них $50?
    img 13839
    with fade
    secretary "Миссис Бакфетт!"
    secretary "О чем говорит этот человек?"
    secretary "Кто он?!"
    music Groove2_85
    img 13840
    with diss
    m "Дорогуша, пожалуйста, не задавай вопросов."
    m "Так надо!"
    img 13841
    with diss
    m "..."
    music Hidden_Agenda
    img 13842
    with fade
    m "Итак, у меня есть с собой другая пара сисек."
    m "Готов-ли ты заплатить за них $ 50?"
# Тот подходит к секретарше и рассматривает ее.
    sound man_steps
    img 13843
    with diss
    w
    sound Jump1
    img 13844
    with diss
    citizen4 "..."
# Секретарша в шоке, смотрит на Монику.
    music Power_Bots_Loop
    img 13845
    with hpunch
    secretary "!!!"
    img 13846
    with diss
    secretary "!!!!!"
# Ситизен отвечает что да, он готов заплатить $ 50 за малышки этой девочки.
# Моника говорит ей, дорогуша, покажи ему свою грудь
# Секретарша спрашивает, но Миссис Бакфетт, я не могу сделать это...
# Я воспитана, у меня моральные принципы, я...
# И она не понимает зачем это надо и чем это поможет в...
    music Hidden_Agenda
    img 13847
    with fade
    citizen4 "Да, я готов заплатить $ 50 за малышки этой девочки."
    img 13848
    with diss
    m "Дорогуша, пожалуйста, покажи ему свою грудь."
    music Power_Bots_Loop
    img 13849
    with hpunch
    secretary "!!!"
    img 13850
    secretary "Но Миссис Бакфетт!"
    secretary "Я не могу сделать это..."
    secretary "Я воспитана! У меня моральные принципы! Я..."
    img 13851
    secretary "И я не понимаю, зачем это надо?"
    secretary "Чем это поможет в..."
# Моника прерывает и говорит что потом все объяснит, что та не видит всей картины.
# Что она всего-лишь работник, которые должен довериться своему Боссу на пути к действительно успешной карьере.
# Секретарша продолжает смотреть на Монику с ужасом
# Ситизен говорит собирается та показывать своих малышек или нет?
# Что он тратит свое время
    music Groove2_85
    img 13852
    with fade
    m "Дорогуша, я потом тебе все объясню!"
    m "Ты просто не видишь всей картины!"
    img 13853
    with diss
    m "Ты всего-лишь работник, и ты должна довериться мне, своему Боссу!"
    m "На пути к действительно успешной карьере!"
    img 13854
    secretary "!!!"
    img 13855
    with fade
    citizen4 "Ну так что, ты собираешься показывать мне своих малышек или нет?"
    citizen4 "Я что, зря трачу время?!"
# Моника говорит секретарше показать грудь. Скорее.
# Секретарша молчит и говорит Я... Миссис Бакфетт...
# Ситизен говорит что эта девочка не хочет показывать своих малышек, поэтому он уходит.
# Если Моника хочет, пусть покажет своих девочек снова за 1$, он готов заплатить его, раз уж уже потерял время.
    img 13856
    with fade
    m "Дорогуша, покажи свою грудь!"
    m "Скорее!"
    img 13857
    with diss
    secretary "Я..."
    secretary "Миссис Бакфетт..."
    img 13858
    with vpunch
    citizen4 "Эта девочка не хочет показывать своих малышек."
    citizen4 "Я ухожу!"
    img 13859
    with diss
    citizen4 "Хотя, если ты хочешь, покажи своих девочек снова за $ 1!"
    citizen4 "Я заплачу этот доллар, раз уж все-равно потерял время, придя сюда."
# Выбор:
# Дать ему уйти.
# Моника думает что она не сошла с ума показывать свою грудь за $ 1, при ком-то. Тем более при своей секретарше.
# Тогда он уходит.
# Секретарша спрашивает что это было, Миссис Бакфетт?
# Моника отвечает что ничего особенного, дорогуша, не обращай внимания. Я рада что ты не стала делать этого.
# Все заканчивается
    img 13860
    with diss
    menu:
        "Дать ему уйти.":
            img 13861
            with fade
            mt "Я еще не сошла с ума, показывать свою грудь за $ 1 при ком-то!"
            mt "Тем более при своей секретарше..."
            img 13862
            with diss
            citizen4 "Нет? Ну ладно, я пошел..." # Уходит
            sound man_steps
            img 13863
            with diss
            w
            music stop
            img black_screen
            with diss
            pause 1.0
            music Groove2_85
            img 13864
            with fadelong
            secretary "Миссис Бакфетт, что это было?"
            img 13865
            with diss
            m "Ничего особенного, дорогуша. Не обращай внимание."
            m "Я рада что ты не стала делать этого."
            return
        "Открыть грудь секретарши самой.":
            pass
# Открыть грудь секретарши самой.
# Моника говорит ему постой.
# Она стесняется. Сейчас я помогу ей.
    music Loved_Up
    img 13866
    with fade
    m "Постой!"
    m "Она стесняется. Сейчас я помогу ей."
# Моника открывает секретарше грудь.
# Секретарша смотрит в ужасе на свою грудь, затем на Монику
# Ситизен вблизи рассматривает грудь секретарши.
# Несколько кадров

# Затем говорит что хочет потрогать ее.
    img 13867
    with diss
    w
    sound snd_fabric1
    img 13868
    with diss
    w
    sound Jump1
    img 13869
    with diss
    w
    img 13870
    with diss
    w
    img 13871
    with diss
    w
    music Groove2_85
    img 13872
    with fade
    citizen4 "Я хочу потрогать ее. Можно?"
# Выбор:
# Запретить.
# Моника говорит что все, хватит, где ее $ 50
# разрешить.
# Моника говорит что это будет стоить еще $ 50
# Ситизен отвечает что у него столько нет и он может дать сверху только $ 10
# Выбор:
# Запретить
    img 13873
    with diss
    menu:
        "Разрешить за $ 50 сверху.":
            music Hidden_Agenda
            img 13874
            with fade
            m "Это будет стоить еще $ 50!"
            img 13875
            citizen4 "У меня столько нет!"
            citizen4 "Я могу дать сверху только $ 10!"
            menu:
                "Запретить.":
                    music Groove2_85
                    img 13876
                    with fade
                    m "Все, этого достаточно!"
                    m "Где мои $ 50?!"

                "Разрешить за $ 10 сверху.":
# Разрешить за $ 10 сверху
# Моника говорит что хорошо, $ 10 сверху и можешь потрогать ее.
# Секретарша в ужасе. Говорит Миссис Бакфетт!
# Моника отвечает что дорогуша, пожалуйста, стой спокойно, это очень важно и для нашего общего блага.
                    img 13877
                    with fadelong
                    m "..."
                    img 13878
                    with diss
                    m "Хорошо..."
                    m "$ 10 сверху и можешь потрогать ее."

                    music Power_Bots_Loop
                    img 13879
                    with hpunch
                    secretary "Миссис Бакфетт!"
                    music Loved_Up
                    img 13880
                    with fade
                    m "Дорогуша."
                    m "Пожалуйста, стой спокойно."
                    m "Это очень важно! И это для нашего общего блага."

# Ситизен лапает грудь, сжимая ее (морфы, видео). Сделать базовую сцену, где держит руки на груди
                    # Затем Моника также говорит что все, хватит, где ее $ 60
                    sound Jump2
                    img 13881
                    with diss
                    citizen4 "Какая упругая грудь!"

                    music stop
                    img black_screen
                    with diss
                    pause 1.5
                    stop music
                    play music "Sounds/audio_MonicaSecretary_Citizen4_Boobs_1.mp3"
                    scene black
                    image videov_MonicaSecretary_Citizen4_Boobs_1_2 = Movie(play="video/v_MonicaSecretary_Citizen4_Boobs_1_2.mkv", fps=30)
                    show videov_MonicaSecretary_Citizen4_Boobs_1_2
                #    with fadelong
                    wclean
                    stop music
                    play music "Sounds/audio_MonicaSecretary_Citizen4_Boobs_1.mp3"
                    scene black
                    image videov_MonicaSecretary_Citizen4_Boobs_1_3 = Movie(play="video/v_MonicaSecretary_Citizen4_Boobs_1_3.mkv", fps=30)
                    show videov_MonicaSecretary_Citizen4_Boobs_1_3
                #    with fadelong
                    wclean
                    stop music
                    music stop
                    music Loved_Up

                    img 13882
                    with diss
                    w
                    img 13883
                    with diss
                    citizen4 "я хотел бы увидеть ее на своем члене!"
                    music Groove2_85
                    img 13876
                    with fade
                    m "Все, этого достаточно!"
                    m "Где мои $ 60?!"


        "Запретить.":
            music Groove2_85
            img 13876
            with fade
            m "Все, этого достаточно!"
            m "Где мои $ 50?!"


    # уже не смотрит. Секретарша закрылась и с ужасом и стыдом смотрит на ситизена
# Ситизен говорит что пусть Моника приводит еще пару малышек и он заплатит еще $ 50.
# Секретарша спрашивает у Моники: Миссис Бакфетт, я все сделал как Вы хотели.
# Могу я идти, пожалуйста? (умоляюще)
# Моника отвечает что да, можешь идти дорогуша.
# Ты хорошо поработала. Я дам тебе потом премию за это.
    img 13884
    citizen4 "Хорошо."
    citizen4 "Ты можешь привести еще пару малышек и я заплачу тебе еще $ 50." # ситизен уходит
    sound man_steps
    img 13885
    with diss
    w
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 13886
    with fadelong
    secretary "Миссис Бакфетт..."
    secretary "Могу я идти, пожалуйста?" #(умоляюще)
    img 13887
    with diss
    m "Да, можешь идти дорогуша."
    m "Ты хорошо поработала."
    m "Я дам тебе потом премию за это."
    return

label gallery_20265:
    # Заходят подчиненные
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 0.5
    sound highheels_run2
    pause 0.5
    sound highheels_short_walk
    pause 0.5
    sound highheels_run1
    pause 2.0
    music Groove2_85
    img 20254
    with fadelong
    w
    img 20255
    with diss
    m "Все в сборе?"
    img 20256
    with fade
    w5 "Да, Миссис Бакфетт, здесь весь отдел."
    img 20257
    with diss
    m "Хорошо. Если кто-то отсутствует здесь, то передайте что он уволен."
    music stop
    sound plastinka2
    img 20258
    with hpunch
    w5 "!!!"
    img 20259
    with fade
    w
    music Groove2_85
    w5 "Мэм... Все здесь."
    img 20260
    with diss
    w
    img 20261
    with fade
    m "Итак, сразу скажу что управлять Вами - не мой уровень."
    img 20262
    m "Я нахожусь здесь для того, чтобы своими глазами убедиться в эффективности организации работы компании."
    img 20263
    with diss
    m "Эффективность должна быть везде, даже в таком никчемном отделе, как этот."
    img 20264
    with fade
    m "Потому я требую строгого подчинения."
    m "Нарушение моих распоряжений наказывается немедленным увольнением."
    m "Вам ясно?"
    img 20265
    with fade
    w5 "Да, Мэм..."
    w6 "Да, Мэм..."
    img 20266
    with diss
    w1 "Мэм, можно задать вопрос?"
    music Pyro_Flow
    img 20267
    with diss
    m "Нельзя!"
    m "Зайдешь ко мне отдельно и задашь свой вопрос."
    img 20268
    with fade
    m "А сейчас все вон отсюда!"
    m "Приступайте к работе!"
    music stop
    img black_screen
    with diss
    pause 2.0
    music I_Feel_You
    pause 1.0
    img 20269
    with fadelong
    mt "Итак..."
    mt "Я - снова Босс!"
    img 20270
    with diss
    mt "Моника, мне не верится в то, что это происходит наяву."
    mt "После всего того что было..."
    img 20271
    with diss
    mt "Хоть это и далеко до того положения, к которому я привыкла..."
    mt "Но я даже немного счастлива сейчас..."
    img 20272
    with diss
    mt "Я верну все назад, клянусь!"
    mt "Я самая умная и самая красивая!"
    img 20274
    with diss
    mt "Эти неудачники даже не сравнятся со мной!"
    mt "Я справлюсь со всеми неприятностями и снова буду владеть этой компанией!"
    img 20273
    with diss
    mt "Скоро, Моника!"
    mt "Уже скоро!"
    return

label gallery_20300:
    music Groove2_85
    img 20300
    with fade
    m "Послушай..."
    w1 "Ой... Я..."
    img 20301
    m "Ты что, язык проглотила?"
    w1 "Нет... Я..."
    img 20300
    with diss
    m "А похоже, что проглотила."
    m "Когда закончишь работать с бумагами, не забудь принести их мне в офис."
    w1 "Да, мэм!"
    return

label gallery_20303:
    music Groove2_85
    img 20302
    with fade
    mt "Этот неудачник, похоже, разбирается в компьютерах... Но я в них ничего не понимаю..."
    mt "Да и мне неинтересно..."
    mt "У меня может быть какое-то дело нему?"
    menu:
        "Задать умный вопрос.":
            img 20303
            with diss
            m "Послушай, а где здесь кнопка, которая выключает интернет?"
            w2 "Что?!"
            m "Ну такая специальная кнопка, на которую нажимаешь и отключается интернет."
            w2 "(Похоже наш босс не слишком силен в этом...)"
            w2 "Она на кухне, рядом с холодильником."
            m "Хорошо, спасибо."
            w2 "(Ха-ха-ха.)"
            # моника отошла
            music Stealth_Groover
            img 20304
            with fade
            mt "Рядом с холодильником?! Так, ерунда какая-то..."
            mt "Это такая умная шутка?"
            mt "Он играет с огнем..."
#            mt "Ладно, лучше не буду в это лезть, все равно в этом ничего не понимаю..."
#            mt "Зато я точно знаю, кто в этом разбирается..."
            return
        "Уйти.":
            m "Все равно я в этом ничего не понимаю..."
            return

label gallery_20310:
    music Groove2_85
    img 20308
    with fade
    mt "Вторая сестра... Никак не могу запомнить как их зовут.."
    img 20309 #
    with diss
    m "Здравствуй. Напомни, как тебя зовут?"
    img 20310
    with fade
    w4 "Я Элла. Мою сестру зовут Эмма. Нас всегда путают!"
    img 20311
    with diss
    m "Поняла. Продолжай работать."
    return

label gallery_20314:
#    m "Послушай..."
    music Groove2_85
    img 20314
    with fade
    w6 "Как же достали эти амбициозные новички и карьеристы!"
    w6 "Ничего не делают, только сидят в своем интернете."
    img 20315
    with diss
    w6 "А как надо сделать какой-то сложный отчет дак Грета, сделай пожалуйста..."
    mt "Боже! Какое занудство!"
#    mt "Пожалуй, пойду к себе в кабинет..."
    return

label gallery_20317:
    music Groove2_85
    img 20317
    with fade
    mt "Кажется, я ее где-то видела..."
    mt "Может быть она когда-то приходила ко мне на кастинг..."
    mt "Или нет, она работала официанткой в моем любимом ресторане..."
    mt "И где я ее могла видеть?"
    img 20318
    with diss
    if shopVisitorStage10 >= 3:
        music Power_Bots_Loop
        mt "Черт! Она же была покупательницей в этом ужасном магазине, где я работала манекеном!"
        music Groove2_85
        mt "Кошмар, надеюсь она меня не узнает..."
        mt "Хотя... Не думаю что можно связать Монику Бакфетт с какой-то продавщицей в трущобах..."
        mt "В любом случае, надо поменьше общаться с ней. Вдруг она, все-же, узнает меня..."
    else:
        mt "Кажется, я ее видела в трущобах..."
        mt "Но и она меня могла видеть..."
    mt "Лучше держаться от нее подальше."
    return

label gallery_20320:
#    m "Послушай, думаю ты знаешь, кто я, а вот я никого тут не знаю."
#    m ""
    music Groove2_85
    img 20319
    with fade
    m "Мне это не очень интересно. Я здесь не надолго."
    m "Но, все-же, расскажи мне про работников этого отдела."
    img 20320
    w5 "Миссис Бакфет! Вы сегодня прекрасно выглядите и обратились как раз по адресу."
    img 20321
    with diss
    m "Я всегда хорошо выгляжу. Не подлизывайся к Боссу, тебе это не поможет."
    m "Итак?"
    img 20322
    with diss
    w5 "Вон там сидит Марта. Она занимается отчетами."
    img 20323
    with diss
    w5 "Близняшки Элла и Эмма.. Они тоже делают отчеты."
    w5 "Хотя что говорить... Мы все тут делаем отчеты."
    img 20324
    with diss
    w5 "Эту толстуху зовут Грета. Она работает тут дольше всех."
    img 20325
    with diss
    w5 "Вон там сидит Лин. Она у нас недавно."
    img 20326
    with diss
    w5 "Нашего системного администратора ты, возможно, видела. Я даже не знаю как его зовут."
    img 20328
    with diss
    w5 "Ну и наконец Я! Самый компетентный сотрудник в этом отделе и, думаю, скоро его глава."
    w5 "Меня зовут Джон."
    mt "Ну и мерзкий же ты тип, Джон."
    img 20329
    with fade
    m "Я поняла, возвращайся к работе!"
    return

label gallery_20333:
    music Sneaky_Snitch
    img 20330
    with fadelong
    w1 "Миссис Бакфетт... Можно?"
    w1 "Я принесла отчет."
    menu:
        "Да, проходи.":
            m "Да, проходи."
            img 20332
            with diss
            m "Напомни, как тебя зовут?"
            w1 "Я...Я Марта."
            music Groove2_85
            img 20333
            with fade
            m "Марта... Ты же понимаешь, что твоя работа очень важна и я на тебя надеюсь?"
            w1 "Да... Мэм..."
            m "Отлично. А теперь положи бумаги на стол и можешь идти."
            img 20334
            with diss
            w1 "Да, хорошо..."
            sound snd_folder_drop
            img 20335
            with diss
            mt "Серая мышь..."
            return
        "Я занята!":
            music Pyro_Flow
            img 20331
            with fade
            m "Ты что, не видишь, я занята!"
            w1 "Простите..."
            m "Положи отчет на стол и выметайся!"
            img 20334
            with diss
            w1 "Хорошо..."
            sound snd_folder_drop
            img 20335
            with fade
            mt "Кучка никчемных идиотов..."
            return

label gallery_20339:
    music DarxieLand
    img 20336
    with fadelong
    w2 "Босс, я все проверил. Все работает стабильно."
    menu:
        "Разве тебя не учили стучаться?":
            music Groove2_85
            img 20337
            with fade
            m "Разве тебя не учили стучаться?"
            w2 "Ну... Я постучал..."
            m "Не правда! А теперь выйди из кабинета и если ты хочешь войти, постучись."
            w2 "Хорошо..."
            music stop
            sound snd_door_close1
            img black_screen
            with diss
            pause 1.0
            sound snd_door_knock
            pause 1.0
            sound snd_door_open1
            pause 0.5
            music DarxieLand
            # выыходит - стучится
            img 20338
            with fadelong
            w2 "Миссис Бакфетт, можно?"
            m "Да, заходи."
            music Groove2_85
            img 20339
            with diss
            m "Вот видишь, все просто. Ты говоришь, что у тебя все работает..."
            m "Хорошо. А теперь можешь идти."
            w2 "?!"
            m "Да, да, иди работай."
            return
        "Больше ничего.":
            img 20340
            with fade
            w2 "Могу я чем нибудь помочь?"
            m "Больше ничего. Можешь идти."
            w2 "Хорошо. Если Вам что-то понадобится, зовите."
            music Groove2_85
            img 20341
            with fade
            mt "Хм... Он ведет себя как болван."
            mt "Возможно я смогу его как-то использовать..."
            mt "Но как? Пока не знаю..."
#            mt "Хм...Возможно я смогу использовать этого болвана..."
#            mt ""
            return

label gallery_20345:
    music ZigZag
    img 20342
    with fadelong
    w3 "Миссис Бакфетт, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            img 20343
            with fade
            w3 "Миссис Бакфетт, в офисе очень жарко, нам нужен кондиционер."
            img 20344
            m "А что, его нет?"
            img 20345
            with diss
            w3 "В этом помещении нет и никогда не было."
            music Groove2_85
            img 20346
            with fade
            m "Эту проблему очень просто решить!"
            m "Откройте окна!"
            img 20347
            with diss
            w3 "Да, но это не совсем..."
            img 20348
            with diss
            m "Отлично, а теперь иди и продолжай работать."
            img 20349
            with fade
            mt "Никчемные люди... Все время что-то требуют..."
#            mt "Да, без кондиционера работать не комфортно... Может стоит как-нибудь помочь им..."
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            img 20347
            with diss
            w3 "Ладно, но у меня проблема..."
            music Groove2_85
            img 20348
            with fade
            m "Ты что, плохо слышишь!? Я сейчас занята!"
            return

label gallery_20354:
    music ZigZag
    img 20350
    with fadelong
    w4 "Миссис Бакфетт, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            img 20351
            with fade
            w4 "Миссис Бакфетт, у меня пропал интернет."
            img 20352
            m "Окей. И чем я тебе могу помочь?"
            img 20353
            with diss
            m "Ты же знаешь, что этими проблемами занимается наш системный администратор."
            img 20354
            with fade
            m "Пухлый коротышка в очках."
            m "Так что иди к нему со своей проблемой."
            img 20355
            with diss
            w4 "Но он не хочет мне помогать."
            music Groove2_85
            img 20356
            with fade
            m "Скажи ему, что он будет уволен, если сейчас же не решит вопрос."
            img 20357
            with diss
            w4 "Хорошо, Миссис Бакфетт."
            w4 "Я передам" # улыбается

#            m "Почему?"
#            w4 "Миссис Бакфетт, мне не очень удобно об этом говорить..."
#            m "Я твой босс, ты можешь мне рассказать, ничего страшного не произойдет..."
#            w4 "Он... Он просит, чтобы я показала ему грудь... И тогда он все починит."
#            m "Я поняла."
#            # моника берет телефон, звонит админу
#            m "Чтобы в течение 30 минут у Эллы был интернет! Ты понял?"
#            w2 "Да, мем..."
#            m "Вот и все, проблема решена."
#            w4 "Спасибо, миссис Бакфет!"
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            w4 "Ладно, но у меня проблема..."
            music Pyro_Flow
            img 20356
            with fade
            m "Ты что, не понимаешь? Я сейчас занята!"
            return

label gallery_20358:
    music Sneaky_Snitch
    img 20358
    with fadelong
    w5 "Миссис Бакфетт, я бы хотел поговорить о моем повышении!"
    menu:
        "Давай поговорим.":
            img 20359
            with diss
            m "Давай поговорим."
            img 20360
            with diss
            w5 "Миссис Бакфетт, Вы же знаете, я очень ответственный и без меня этот отдел просто развалится."
            w5 "Еще эта толстуха Грета так и норовит занять мое законное место."
            w5 "И я буду Вам бесконечно благодарен если Вы..."
            music Groove2_85
            img 20361
            with fade
            m "Достаточно..."
            m "Чем чаще ты задаешь мне такие вопросы, тем дальше от тебя эта должность."
            img 20362
            with diss
            mt "И что это вообще за должность? Почему он думает, что этому отделу нужен какой-то мифический начальник кроме меня?"
            music Sneaky_Snitch
            img 20363
            with fade
            w5 "Да, понял. Ухожу. Но знайте, миссис Бакфетт, Вы всегда можете на меня расчитывать."
            return
        "Не в этой жизни.":
            music Pyro_Flow
            img 20361
            m "Повышении?!"
            m "Не сегодня. Выйди и закрой за собой дверь."
            music Sneaky_Snitch
            img 20363
            with fade
            w5 "Хорошо. Понимаю, Вы очень заняты. Ну ничего, в другой раз."
            return

label gallery_20366:
    music Sneaky_Snitch
    img 20364
    with fadelong
    w6 "Миссис Бакфетт, можно?"
    menu:
        "Да, заходи.":
            m "Да, заходи."
            img 20365
            w6 "Миссис Бакфетт, Я бы хотела поговорить о ситуации в нашем отделе."
            img 20366
            with diss
            w6 "Вы же наверняка знаете на ком все держится..."
            img 20367
            with diss
            w6 "А этот карьерист Джон... Как он меня достал!"
            w6 "Думаю, с Вашими менеджерскими талантами Вы понимаете, кто достоин стать главой отдела."
            music Groove2_85
            img 20368
            with fade
            m "Уж будь в этом уверена."
            m "Придет время и ты все узнаешь."
            img 20369
            with diss
            mt "Глава отдела? Как же вы мне надоели..."
            img 20370
            with fade
            m "Я тебя услышала. Ты свободна."
#            w6 "Да, спасибо миссис Бакфет. Вот кстати отчет, который я сегодня сделала."
#            m "Спасибо, можешь положить на стол."
            return
        "Я занята.":
            m "Я занята, приходи завтра."
            music Pyro_Flow
            img 20370
            with fade
            w6 "Но как же..."
            m "Я сказала завтра, я сейчас занята!"
            return

label gallery_20375:
    music Sneaky_Snitch
    img 20371
    with fadelong
    w7 "Миссис Бакфетт, можно?"
    if shopVisitorStage10 >= 3:
        music Groove2_85
        img 20372
        with fade
        mt "Она может меня узнать... Лучше не говорить с ней долго."
        mt "Думаю, лучше будет ее вежливо выпроводить."
    img 20373
    with diss
    m "Кажется, тебя зовут Лин?"
    img 20374
    w
    img 20375
    with diss
    w7 "Да, мэм."
    img 20376
    with fade
    m "Лин, я сейчас очень занята. Если ты принесла отчет, положи пожалуйста его мне на стол. Я его обязательно посмотрю."
    img 20377
    with diss
    w7 "Хорошо, Мэм."
    sound snd_folder_drop
    if shopVisitorStage10 >= 3:
        img 20378
        with fade
        w7t "(Меня не покидает мысль, что где то Я видела эту миссис Бакфетт...)"
    return

label gallery_20752:
    music Groove2_85
    img 20751
    with fade
    m "Я за твоими отчетами? Я надеюсь, они готовы?"
    w2 "Миссис Бакфетт, я системный администратор."
    m "Это очень хорошо, а теперь возьми эту флеш карту и скопируй на нее свои отчеты."
    img 20752
    w2 "Миссис Бакфетт, я не пишу отчеты, я же говорю, я системный администратор."
    w2t "Да, похоже она совсем не разбирается в этом... С таким же успехом я могу сказать, что чищу вентиляторы... Ха-ха!"
    m "Напомни, а чем ты тут вообще занимаешься ?"
    w2 "Я слежу за работой сети, компьютеров и автоматизацией различных бизнес процессов..."
    img 20753
    with diss
    w2t "И определенно буду следить за твоей красивой попой."
    m "Я поняла. Ладно, следи."
    img 20304
    with fade
    mt "Как я могла забыть... Он разбирается в компьютерах... Нужно не забывать об этом..."
    return

label gallery_20759:
    music Groove2_85
    img 20754
    with hpunch
    m "Привет. Мне нужны отчеты, которые ты сделала."
    music Loved_Up
    img 20755
    with diss
    w1 "Но... Миссис Бакфетт, простите, я еще не доделала. И мне нужно будет их проверить..."
    menu:
        "Ничего страшного.":
            img 20756
            with diss
            m "Ничего страшного. Конечно, не следует такого допускать."
            m "Ты же постараешься сделать так, чтобы такой ситуации не повторилось?"
            w1 "Я...Да, конечно..."
            pass
        "И почему же они еще не готовы?":
            img 20757
            with diss
            m "И почему же они еще не готовы?"
            w1 "..."
            m "А?"
            img 20758
            w1 "Миссис Бакфетт, я... У меня..."
            m "Ты же знаешь, какую важную работу все мы здесь делаем!"
            w1 "Обещаю Вам, я их доделаю! Сегодня же!"
            pass
    img 20759
    with diss
    m "Отлично, а пока скопируй мне все, что у тебя есть на данный момент."
    w1 "Хорошо..."
    w1 "Я все скопировала."
    img 20760
    with diss
    m "Хорошо."
    m "И не забывай, твой вклад в работу компании очень высок."
    w1 "Да, миссис Бакфетт."
    return

label gallery_20765:
    music Groove2_85
    img 20761
    with fade
    m "Здравствуй. Скопируй, пожалуйста, отчеты, которые ты сделал. Вот флеш карта."
    music Sneaky_Snitch
    img 20762
    with diss
    w5 "Я очень рад, что Вы подошли Миссис Бакфетт. Да, конечно, я сейчас."
    # берет флешку
    img 20763
    with diss
    w5 "Хотите кофе, миссис Бакфетт?"
    m "Нет."
    w5 "Жаль, если вдруг захотите, дайте знать."
    music Loved_Up
    img 20764
    with fadelong
    w
    music Sneaky_Snitch
    img 20765
    with diss
    w5 "Вот, я все скопировал Вам папку в 'Наиболее качественные отчеты', чтобы Вам было проще."
    img 20766
    mt "Да уж, что бы я делала без этой папки?"
    m "Я сообщу, если ты мне понадобишься."
    img 20767
    with diss
    w5 "Да, миссис Бакфетт, можете на меня рассчитывать в любое время."
    return

label gallery_20772:
    music Groove2_85
    img 20768
    with fade
    m "Привет. Мне нужны твои отчеты. Скопируй их мне на флеш карту."
    w6 "Да, но зачем? Все же можно отправить на электронную почту..."
    # это все слышит воркер5
    music Sneaky_Snitch
    img 20769
    with fade
    w5 "Миссис Бакфетт, не обращайте внимания на Грету. Она не понимает всю важность этого действия."
    w5 "Давайте я помогу."
    # берет флешку вставляет в комп
    img 20770
    with diss
    w5 "Грета, скопируй все свои ответы миссис Бакфетт. Я надеюсь, в них нет ошибок."
    w6t "Ах ты сволочь..."
    music Groove2_85
    img 20771
    with fade
    w6 "В отличие от твоих, они качественные!"
    # садится за комп, копирует
    music Sneaky_Snitch
    img 20772
    with diss
    w6 "Пожалуйста, миссис Бакфетт."
    m "Спасибо."
    mt "Похоже, с этими двумя надо будет что-то решать..."
    return

label gallery_20775:
    music Groove2_85
    img 20773
    with fade
    m "Я за отчетами, надеюсь, они готовы."
    music ZigZag
    img 20774
    with diss
    w3 "Да, я только кое-что проверю..."
    m "Это не обязательно. Возьми эту карту и скопируй на нее всю свою работу."
    w3 "Да, мэм."
    m "Встань, когда с тобой говорит Босс."
    img 20775
    with fade
    w3 "Мэм, могу я спросить?"
    menu:
        "Спрашивай":
            m "Да, что ты хотела?"
            w3 "В офисе жарко. Когда нам установят кондиционер?"
            mt "Понятия не имею, скорее всего никогда."
            img 20776
            with diss
            m "Я не знаю, мне надо выдать распоряжение. Нужно подождать, пока у меня будет настроение для этого."
            w3 "Да мэм, спасибо."
            pass
        "Нет":
            img 20777
            with diss
            m "Не сейчас, я занята."
            w3 "Да мэм..."
            pass
    img 20778
    with fadelong
    w3 "Все скопировалось."
    m "Хорошо."
    m "Продолжай в том же духе."
    w3 "Да, миссис Бакфетт."
    return

label gallery_20784:
    music ZigZag
    img 20779
    with fade
    m "Здравствуй. Скопируй мне свои сделанные отчеты вот сюда."
    w4t "Интересно, почему я должна их копировать на флеш карту? Уже давно ими не пользуются..."
    w4 "Хорошо. Миссис Бакфетт, а зачем это? Я ведь могу их отправить Вам на почту."
    img 20780
    with diss
    mt "На самом деле, мне твои отчеты неинтересны ни на почте, ни на карте..."
    mt "Гребаный Биф!"
    img 20781
    with fade
    m "Сразу видно, ты ничего не понимаешь в безопасности. Это хороший способ!"
    img 20782
    with diss
    w3t "А у нашей начальницы отличная задница..."
    img 20783
    with diss
    w3t "И сиськи ничего такие, но мои определенно больше!"
    img 20784
    with fade
    w4 "Но что если на флеш карте окажется вирус, или Вы ее потеряете."
    m "Я? Я ее не потеряю."
    img 20785
    with diss
    mt "А она не такая и глупая... Или делает вид..."
    mt "Все-равно она не умнее меня!"
    return

label gallery_20788:
    music Groove2_85
    img 20786
    with fade
    m "Вот флеш карта, скопируй сюда сделанные тобою отчеты."
    img 20787
    with diss
    if shopVisitorStage10 >= 3:
        mt "Хоть бы она меня не узнала... Она могла видеть меня в трущобах..."
    w7 "Хорошо."
    if shopVisitorStage10 >= 3:
        w7t "Меня не покидает чувство, что я где-то видела Миссис Бакфетт. И определенно не здесь."
        # берет флешку cадится
        img 20788
        with diss
        w7t "Может быть в каком-то журнале..."
        w7t "Возможно..."
        w7t "Хотя нет!"
        img 20789
        with diss
        m "Эй! О чем задумалась? Я жду твои отчеты!"
        w7 "Да, мэм, копируется..."
        w7t "Черт, сбила с мысли..."
    img 20790
    with fadelong
    w7 "Готово."
    m "Хорошо, продолжай работу."
    return

############ Pub 1############

label gallery_9638:
    # Моника моет посуду
    music2 stop

    music stop
    sound snd_washing_dishes
    $ monicaWashingDishesImages = [9637, 9638, 9639]
    call showRandomImagesFirstFade(monicaWashingDishesImages, 1)
    $ monicaWashingDishesImages2 = [9640, 9641, 9642]
    call showRandomImagesFirstFade(monicaWashingDishesImages2, 1)
    $ rand1 = rand(1,4)
    if rand1 == 1:
        mt "Никогда бы не подумала что буду мыть посуду в подобной дыре..."
    if rand1 == 2:
        mt "Не могу поверить что я делаю это..."
    if rand1 == 3:
        mt "У меня ощущение что все это сон..."
    if rand1 == 4:
        mt "Мне надо определенно что-то менять в этой ситуации... И как можно быстрее!"

    return

label gallery_9646: # Бармен

    # Клик на бармена
    # Бармен лапает Монику
    music Hidden_Agenda
    img 9643
    with fade
    w
    img 9644
    with Dissolve(0.3)
    w
    sound Jump2
    img 9645
    with Dissolve(0.3)
    w
    mt "Черт! Кажется, этот извращенец Джо пытается меня незаметно лапать!"
    menu:
        "Не обращать внимание...":
            sound snd_washing_dishes
            music Loved_Up
            img 9646
            with Dissolve(0.3)
            w
            img 9647
            with Dissolve(0.3)
            w
            img 9648
            with Dissolve(0.3)
            w
            music Groove2_85

#        "Не обращать внимание... (low corruption, required [monicaWashHoldJoeCorruption]) (disabled)" if corruption < monicaWashHoldJoeCorruption:
#            pass
        "Прекратить это!":
            music Power_Bots_Loop
            img 9649
            with fade
            m "Джо! Ты что-то хотел взять здесь?"
            joe "Да, [monica_pub_name]!"
            "Я хочу взять чистую пивную кружку!"

    img 9650
    with fadelong
    mt "Это место - действительно Shiny Hole с извращенцами!"
    return

label gallery_9654: # Барменша
    # Клик на барменшу
    # Барменша лапает Монику
    music Hidden_Agenda
    img 9651
    with fade
    w
    img 9652
    with Dissolve(0.3)
    w
    img 9653
    with Dissolve(0.3)
    w
    sound Jump2
    img 9654
    with Dissolve(0.3)
    w

    mt "Черт! Эшли меня трогает за зад?!"
    menu:
        "Не обращать внимание...":
            sound snd_washing_dishes
            music Loved_Up
            img 9655
            with Dissolve(0.3)
            w
            img 9656
            with Dissolve(0.3)
            w
            img 9657
            with Dissolve(0.3)
            w

            music Groove2_85

#        "Не обращать внимание... (low corruption, required [monicaWashHoldAshleyCorruption]) (disabled)" if corruption < monicaWashHoldAshleyCorruption:
#            pass
        "Прекратить это!":
            music Power_Bots_Loop
            img 9658
            with fade
            m "Эшли! Ты что-то хотела взять здесь?"
            ashley "Я слежу чтобы ты лучше мыла посуду!"
            "Везде грязь!"

    img 9650
    with fadelong
    mt "О БОЖЕ!!!"
    "ЗА ЧТО МНЕ ЭТО?!"
    mt "Это место - действительно Shiny Hole с извращенцами!"
    return

label gallery_9664:
    if obj_name == "Bartender":
        if act=="l":
            if monicaWorkingAsDishwasher == False:
                mt "Он похож на бармена в этой дыре..."
            else:
                mt "Это Джо. Он дал мне работу посудомойщицей."
                mt "Это ужас, конечно, но, по крайней мере, у меня есть еда..."
    if obj_name == "Bartender_Waitress":
        if act=="l":
            if monicaWorkingAsDishwasher == False:
                mt "Похоже это официантка в этой дыре или что-то вроде того..."
            else:
                mt "Это Эшли. Жена Джо."
                mt "Мне кажется что она немного странная."
                mt "Хотя что может быть не странного в этой дыре?!"

    if obj_name == "Monica":
        mt "Какое жуткое место!"
        "Я даже представить себе не могла что могу оказаться в подобном заведении!"
    if obj_name == "Pub_Bar":
        img 9662
        with fade
        mt "SHINY HOLE?!?"
        mt "О БОЖЕ!"
        "ЧТО ЭТО ЗА ДЫРА?!?"

    if obj_name == "Pub_Bar_Table":
        mt "Жуткое заведение, жуткая мебель!"
        "Какой кошмар, Моника!"

    if obj_name == "Pub_StripteaseGirl1" or obj_name == "Pub_StripteaseGirl2":
        if act=="l":
            if obj_name == "Pub_StripteaseGirl1":
                if pubStripteaseGirl1Suffix == 1:
                    label gallery_9668:
                    img 9668
                if pubStripteaseGirl1Suffix == 2:
                    label gallery_9669:
                    img 9669
                if pubStripteaseGirl1Suffix == 3:
                    label gallery_9670:
                    img 9670
                if pubStripteaseGirl1Suffix == 4:
                    label gallery_9671:
                    img 9671
            if obj_name == "Pub_StripteaseGirl2":
                if pubStripteaseGirl2Suffix == 1:
                    img 9664
                if pubStripteaseGirl2Suffix == 2:
                    label gallery_9665:
                    img 9665
                if pubStripteaseGirl2Suffix == 3:
                    label gallery_9666:
                    img 9666
                if pubStripteaseGirl2Suffix == 4:
                    label gallery_9667:
                    img 9667
            with fade
            w
            if ep29_quests_pub_monica_knows_molly == True and obj_name == "Pub_StripteaseGirl1":
                call gallery_9667_1()
                return
            if ep29_quests_pub_monica_knows_claire == True and obj_name == "Pub_StripteaseGirl2":
                call gallery_9667_2()
                return
            mt "Эти девушки совсем не уважают себя!"
            "Как можно делать подобное у всех на виду?!"

        if act=="w":
            mt "Я не собираюсь подходить туда!"
            "Мне не на что там смотреть!!!"

    if obj_name == "Pub_Washbasin":
        mt "Там готовят еду и моют посуду..."
        mt "Какое жуткое место!"

    return

label gallery_9667_1:
    mt "Молли. Считает себя королевой сцены Shiny Hole..."
    mt "Звезда трущоб. Фи!"
    return

label gallery_9667_2:
    mt "Эта Клэр могла бы быть моделью журнала..."
    mt "А не танцевать в пабе перед толпой пьяных неудачников!"
    return


label gallery_20482:
    if monicaEatedLastDay == day:
        mt "Я уже ела сегодня."
        mt "Ни к чему тратить деньги..."
        return
    music2 stop
    music Groove2_85
    img 20462
    with fadelong
    ashley "Привет, [monica_pub_name]!"
    img 20461
    with diss
    ashley "Ты пришла, чтобы мыть посуду?"
    img 20463
    with diss
    m "Нет, я хочу заказать еду!"
    img 20464
    with fade
    ashley "Правда?"
    ashley "И что же ты хочешь заказать?"
    img 20465
    with diss
    m "Я хочу заказать..."
    $ menu_price = [pubShinyBurger, pubSphagettiPrice, pubSoupPrice]
    $ menu_price2 = [pubShinyBurger, pubSphagettiPrice, pubSoupPrice]
    $ choose_var = 0
    menu:
        "Shiny Бургер.":
            label gallery_20483:
            $ choose_var = 1
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Shiny Бургер."
            $ images_list = [20473, 20478, 20483]
        "Спагетти.":
            $ choose_var = 2
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Спагетти."
            $ images_list = [20474, 20479, 20482]
        "Суп харчо.":
            label gallery_20484:
            $ choose_var = 3
            img 20466
            with fade
            m "Я хочу заказать..."
            m "Суп харчо."
            $ images_list = [20475, 20477, 20484]
        "Уйти.":
            img 20470
            with fade
            m "Я передумала."
            img 20471
            with diss
            ashley "Ах, [monica_pub_name], у тебя нет денег!"
            ashley "Но ведь ты посудомойка. Ты всегда можешь помыть посуду!"
            img 20472
            with diss
            mt "!!!"

            # на улице
            return
    img 20467
    with diss
    joe "А выпивку?"
    img 20468
    m "Спасибо, не надо!"
    img 20469
    with fade
    ashley "Хорошо, присаживайся за стол."
    ashley "Я сейчас принесу."

    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 2.0
    sound snd_plates2
    $ pubFoodHistory.append(choose_var)
    music Groove2_85
    img images_list[0]
    with fadelong
    #Shiny Бургер.
#    img 20473
    #Спагетти.
#    img 20474
    #Суп харчо.
#    img 20475
    ashley "Но ты могла бы не тратить деньги."
    ashley "Эту еду легко заработать посудомойкой."

    img 20476
    with diss
    mt "!!!"

    if monicaPubWashingDishesCount > 5:
        # если часто мыла
        img images_list[1]
        #Shiny Бургер.
#        img 20478
        #Спагетти.
#        img 20479
        #Суп харчо.
#        img 20477
        with fade
        ashley "К тому же, я уже привыкла что ты моешь посуду."
        ashley "Мне стало как-то лень заниматься этим."
        img 20480
        with diss
        m "Спасибо, Эшли."
        m "Сегодня я не хочу... мыть посуду..."

        img 20481
        with diss
        ashley "Хорошо, [monica_pub_name], если надумаешь, приходи..."
        #


    img images_list[2]
    with fade
    #Shiny Бургер.
#    img 20483
    #Спагетти.
#    img 20482
    #Суп харчо.
#    img 20484
    #
    mt "Эшли готовит отвратительно."
    mt "Это место - действительно дыра."
    music stop
    sound snd_gulp
    img black_screen
    with diss
    mt "Но это нормальная еда, а не пирожные с заправки..."
    return

label gallery_20985:
#    menu:
#        "Спросить о повышении.":
#            pass
# Моника спрашивает, можно-ли ее повысить, чтобы она зарабатывала какие-то деньги?
    music2 pub_noise1_low
    music Groove2_85
    img 20953
    with fadelong
    m "Эшли..."
    m "Можно-ли попросить дать мне еще другую работу, чтобы я..."
    m "Чтобы я зарабатывала какие-то деньги здесь?"
# Далее:
# Если ур у Эшли и Джо < 1
    if char_info["Bartender_Waitress"]["level"] < 2 and char_info["Bartender"]["level"] < 2:
        img 20954
        with fade
        ashley "Хммм..."
        ashley "Если честно, я не уверена в тебе [monica_pub_name]."
        ashley "Поработай пока посудомойкой!"
        img 20955
        with diss
        m "!!!"
        help "Требуется отношение с Джо, либо Эшли выше 1."
        return

# Если у Эшли ур.1, то она говорит что не уверена в ней, но Джо отзывается о ней хорошо (показан хитрый Джо)
    if char_info["Bartender_Waitress"]["level"] < 2:
        img 20956
        with fade
        ashley "Хммм..."
        ashley "Если честно, я не уверена в тебе [monica_pub_name]."
        ashley "Но Джо отзывается хорошо о тебе."
        joe "..." # хитрый
    else:
    # Если у Эшли ур.2, то она говорит что уже успела разглядеть ее попку
        img 20957
        with fade
        ashley "Хммм..."
        ashley "Если честно, то я уже успела разглядеть твою попку, [monica_pub_name]."

# И, пока она работает, никто не пришел проверять ее из миграционной полиции или санитарного контроля.
# Также после ее мытья посуды не отравился ни один клиент.
# И Эшли было бы интересно посмотреть на ее голую попку, которая будет крутиться на пилоне.
# Поэтому она разрешает ей танцевать здесь, но трахаться с клиентами пока нельзя, хотя я знаю что ты за этим пришла сюда.
    img 20958
    with diss
    ashley "И, пока ты работаешь, никто не пришел проверять тебя из миграционной полиции или санитарного контроля."
    img 20959
    with diss
    m "..."
    img 20960
    with fade
    ashley "Также, после твоего мытья посуды не отравился ни один клиент."
    music Loved_Up
    img 20961
    with diss
    ashley "Так что мне было бы интересно посмотреть на твою голую попку, которая будет крутиться на пилоне."
    ashley "Поэтому, так уж и быть."
    ashley "Я разрешаю тебе танцевать здесь..."

    music Groove2_85
    img 20962
    with fade
    ashley "Но трахаться с клиентами пока нельзя!"
    ashley "Хотя я знаю что ты за этим пришла сюда."
# Моника в шоке. Отвечает что не собирается танцевать здесь в голом виде!
# Эшли удивленно спрашивает а что же она тогда хочет? О каком повышении говорит?
# Джо говорит что видишь Эшли, она приличная девушка, пусть она работает у нас официанткой!
# Эшли спрашивает у Джо что ты решил отдать мою работу Мэрилин?
    music Power_Bots_Loop
    img 20963
    with vpunch
    m "!!!"
    m "Я не собираюсь танцевать здесь в голом виде!"
    music Groove2_85
    img 20964
    with fade
    ashley "А что же ты тогда хочешь?"
    ashley "О каком повышении ты говоришь?"
    joe "Видишь, Эшли? [monica_pub_name] приличная девушка."
    joe "Пусть она работает у нас официанткой!"
    music Power_Bots_Loop
    img 20965
    with diss
    ashley "Джо, ты что, решил отдать мою работу [monica_pub_name]?!"
# Может быть ты на ней женишься вместо меня, Джо?!
# И будешь сам платить кредиты за это заведение?!
# Джо улыбается. Нет, Эшли, я не это имел ввиду.
# У нее нет документов, но ей нужно зарабатывать хотя бы пару долларов, правда, Мерилин?
    img 20966
    with diss
    ashley "Может быть ты на ней женишься вместо меня, Джо?!"
    ashley "И будешь сам платить кредиты за это заведение?!"
    img 20967
    with fade
    joe "Нет, Эшли! Я не это имел ввиду!"
    joe "У нее нет документов, но ей нужно зарабатывать хотя бы пару долларов."
    music Hidden_Agenda
    img 20968
    with diss
    joe "Правда, [monica_pub_name]?"

# Моника кривится
# Уверен, что обладательнице такой попки будут платить хорошие чаевые, которые мы можем забирать себе, Эшли!
# Она ведь работает у нас неофициально! Скажем, отдавать ей 10 процентов от того что ей дадут клиенты.
# И ей необязательно платить основную зарплату, ей вполне хватит остатка от чаевых.
# Ведь так, Мэрилин?
    img 20969
    with diss
    mt "!!!" # Моника кривится
    img 20970
    with fade
    joe "Уверен, что обладательнице такой фигуры будут платить хорошие чаевые, которые мы можем забирать себе, Эшли!"
    img 20971
    with hpunch
    mt "ЧТО?!"
    img 20972
    with fade
    joe "Она ведь работает у нас неофициально!"
    joe "Можно, скажем, отдавать ей 30 процентов от того, что ей дадут клиенты."
    joe "И нам необязательно платить ей основную зарплату."
    joe "Ей вполне хватит остатка от чаевых."
    img 20973
    with diss
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
    with fade
    joe "А ты, Эшли, будешь получать чаевых даже больше чем раньше и при этом уделять больше времени бару."
    music Groove2_85
    img 20976
    with fade
    ashley "..."
    ashley "То есть, Джо, ты предлагаешь отправить [monica_pub_name] к этим пьяницам и не платить ей деньги?"
    img 20977
    joe "Платить, но только 30 процентов от чаевых. Мы ничем не рискуем, Эшли!"
    joe "Нет зарплаты - не нужны документы! Не страшны никакие проверки!"
    img 20978
    with diss
    ashley "А если [monica_pub_name] нагрубит клиенту?"
    ashley "Или заберет чаевые себе?"
    img 20979
    m "!!!"
    img 20980
    with fade
    joe "[monica_pub_name] выглядит как порядочная девушка и не будет брать себе лишнего."
    img 20981
    with diss
    ashley "..."
    ashley "Ну, не знаю..."
    img 20982
    with diss
    ashley "[monica_pub_name], и ты согласна на такую работу?"

# Выбор:
# Я не согласна работать за такие копейки!
# Моника говорит что не согласна работать за такие копейки. (уходя)
# Джо говорит что если надумает, то пусть приходит
    menu:
        "Я не согласна работать за такие копейки!":
            music Power_Bots_Loop
            img 20983
            with fade
            m "Я не согласна работать за такие копейки!"
            img 20984
            with diss
            joe "[monica_pub_name], если надумаешь, то приходи." # подмигивает
            return
        "Согласиться.":
            pass
# Согласиться.
# Моника говорит что согласна работать, ей нужна хоть какая-то работа.
# Что не будет грубить клиентам, будет общаться с ними вежливо.
# И что будет отдавать чаевые им.
    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 20985
    with fadelong
    m "Я..."
    m "Я согласна работать. Мне нужна хоть какая-то работа."
    m "Я обещаю что не буду грубить клиентам, а буду обращаться с ними вежливо."
    img 20986
    with diss
    ashley "..."
    img 20987
    with diss
    m "И буду отдавать чаевые Вам..."
# Эшли говорит что хорошо, ты можешь вилять своей попкой, но не вздумай заигрывать с посетителями!
# Здесь не бордель! И она не потерпит официантку, которая будет вести себя как шлюха!
# Моника отвечает что Эшли может не беспокоиться, она не будет выходить за рамки рабочих обязанностей.
    music Groove2_85
    img 20988
    with fade
    ashley "Ну хорошо. Ты можешь вилять своей попкой, но не вздумай заигрывать с посетителями!"
    ashley "Здесь не бордель!"
    ashley "И я не потерплю официантку, которая будет вести себя как шлюха!"
    img 20989
    with diss
    m "Эшли, Вы можете не беспокоиться."
    m "Я не буду выходить за рамки рабочих обязанностей."
# Моника думает что ей с трудом вериться что она вообще ведет такой диалог!
# Она, Моника Бакфетт! И говорит такие слова!
# Утешает только то, что ее считают здесь Мерилин, а это значит она в этом месте не имеет ничего общего с Моникой Бакфетт.
# Иначе, она не смогла бы согласиться на такое.
    music RnB3_65
    img 20990
    with fade
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
    music Groove2_85
    with vpunch
    ashley "[monica_pub_name], ты меня слышишь?!"
    img 20992
    with fade
    m "А?" # оборачивается
    img 20993
    with diss
    ashley "[monica_pub_name], ты можешь одевать рабочую униформу и идти работать."
    return

label gallery_20996:
# При клике на барменов, Моника говорит что закончила работу и вот чаевые.
# Эшли дает ей 10 процентов и говорит приходить работать еще.
    music2 pub_noise1_low
    music Groove2_85
    img 20995
    with fadelong
    m "Эшли, я закончила работу."

    if pubMonicaWaitressTips == 0:
        m "Мне никто не дал чевых сегодня..."
    else:
        m "Вот чаевые, которые я смогла получить..."

    # если есть чаевые
        img 20996
        with diss
        ashley "Хорошо. Вот твои тридцать процентов."
        ashley "Завтра приходи работать еще."

    # если нет чаевых
#    img 20995
#    m "Мне никто не дал чевых сегодня..."
    return

label gallery_14208:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14203
    with fadelong
    mt "Надо пересилить себя..."
    m "Что будете заказывать?"
    img 14202
    with diss
    customer1 "Вообще-то я ничего не хотел, но теперь думаю, что что-то закажу."
    customer1t "И откуда этот говнюк Джо достал такую красотку?"
    customer1 "Как тебя зовут?"
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14204
    with fade
    customer1 "Отлично, [monica_pub_name]"
    customer1 "Думаю, ты тут для того, чтобы заработать, так?"
    img 14205
    with diss
    m "Ну, да..."
    mt "Надо быть осторожнее с этими пьяницами..."
    img 14206
    with fade
    customer1 "Я так и думал. Вообще, чтобы получать хорошие чаевые, нужно как минимум быть вежливой."
    customer1 "Например ты должна была сказать:"
    img 14207
    customer1 "Здравствуйте, меня зовут [monica_pub_name]..."
    customer1 "Понятно?"
    img 14208
    m "Да."
    img 14209
    with diss
    mt "Да кем он себя возомнил?"
    mt "Очередной придурок..."
    img 14210
    with fade
    customer1 "Хорошо. Думаю, в следующий раз ты будешь более вежливой. Кстати, я передумал делать заказ."
    img 14211
    with diss
    mt "Что за урод? Только зря потратила время..."
    return

label gallery_14219:
    music Hidden_Agenda
    sound highheels_short_walk

    img 14212
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer1_dance_comment_stage == 1:
        customer1 "Ты меня пытаешься надурить, детка."
        customer1 "Ты танцуешь здесь иногда у пилона!"
        m "Нет. Я же говорила, что я просто официантка..."
        customer1 "Что-то я тебе не верю..."
        mt "Да мне какая разница, веришь ты мне или нет!"
        mt "Деревенщина!"

    if monicaStartedStripDanceFlag == True and customer1_dance_comment_stage == 0:
        customer1 "А не тебя я видел виляющей попой у пилона?"
        m "Нет, Вы меня с кем-то путаете."
        m "Я работаю здесь официанткой..."
        customer1 "Только официанткой?"
        m "Еще... Еще я мою посуду..."

    #

    m "Что будете заказывать?"
    img 14213
    customer1 "Ну нет, разве я так тебя учил?"
    customer1 "Будь вежливой, скажи как тебя зовут..."
    img 14214
    menu:
        "Быть вежливой." if bitchmeterValue <= maxBitchness / 2:
            img 14215
            with fade
            mt "Насколько знаю, официантки ведут себя вежливо."
            mt "Попытаюсь притвориться, насколько у меня хватит сил..."
#            mt "Возможно, так правильнее, я совсем не знаю как работают официантки."
            img 14216
            with diss
            m "Здравствуйте, меня зовут [monica_pub_name]..."
            img 14217
            with fade
            customer1 "Отлично, [monica_pub_name]."
            customer1 "А теперь, [monica_pub_name], принеси мне пива."
            img 14218
            with diss
            m "Хорошо."
            # уходит, приносит
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Hidden_Agenda
            sound snd_plates1
            img 14219
            with fade
            w
            sound snd_beer_table
            img 14220
            with diss
            w
            img 14221
            with diss
            customer1 "Запомни, быть хорошей официанткой очень сложно. Некоторые получают по 100 долларов чаевых за заказ. А пока держи..."
            # дает 0.25
            img 14209
            with fade
            mt "Четвертак? Сколько же бокалов я должна принести, чтобы ты дал мне 100 долларов?"
#            if monicaBitch == True:
            mt "Урод..."
            return
        "Быть вежливой. (Моника недостаточно приличная) (disabled)" if bitchmeterValue > maxBitchness / 2:
            pass
        "Отказаться.":
            music Groove2_85
            img 14222
            with fade
            mt "Я не собираюсь слушаться этого деревенщину!"
            # развернуться и уйти
            sound highheels_short_walk
            img 14223
            with diss
            customer1 "Эй, ты куда?"
            return

label gallery_14231:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14225
    with fadelong
    m "Что будете заказывать?"
    img 14224
    with diss
    customer2 "Новенькая?"
    # смотрит на монику
    music Groove2_85
    img 14226
    with fade
    customer2 "Ну что сказать: нормально."
    customer2 "И откуда же ты приехала в нашу дыру?"
    img 14227
    mt "Я ни откуда не приезжала! Я просто живу в тех районах, куда такие как ты не заходят."
    img 14228
    with diss
    m "Я из этого города."
    img 14229
    with fade
    customer2 "Из этого говоришь? Я знаю всех в этом районе и ты тут недавно..."
    customer2 "Думаешь, наше знакомство лучше начать с обмана?"
    img 14230
    mt "Думаю, лучше соврать..."
    img 14231
    with diss
    m "Да, Вы правы. Я приехала недавно на заработки."
    img 14232
    with fade
    customer2 "Да, это похоже на правду."
    customer2 "И ты, похоже не из городских, иначе что тебе тут делать?"
    customer2 "Похоже, ты из какой-то деревни, коих тысячи."
    img 14233
    with diss
    mt "Из деревни здесь только ты..."
    if monicaBitch == True:
        mt "Урод..."
    img 14234
    with fade
    customer2 "Ладно, девочка, вот тебе полбакса и принеси мне пиво. Считай, это в честь первого знакомства."
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14235
    with fade
    w
    sound snd_plates1
    img 14236
    with diss
    w
    sound snd_beer_table
    img 14237
    with diss
    m "Вот, пожалуйста."
    img 14238
    with fade
    customer2 "Спасибо, можешь идти. Кстати, у тебя большой потенциал, ха-ха-ха. Буду ждать тебя на сцене."
    img 14239
    with diss
    mt "Не дождешься..."
    return

label gallery_14247:
    music Hidden_Agenda
    sound highheels_short_walk

    img 14240
    with fade

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer2_dance_comment_stage == 1:
        customer2 "Эй, я видел тебя на сцене! Это точно была ты!"
        m "Боюсь, Вы ошиблись..."
        customer2 "Не-а! Папочка не ошибается никогда!"
        mt "Чего он прицепился ко мне!!!"
        m "Я не танцую на сцене. Возможно, танцовщица просто немного похожа на меня..."
        customer2 "Да? Хммм... Ладно, я присмотрюсь внимательнее в следующий раз."
        m "Я могу идти?"


    if monicaStartedStripDanceFlag == True and customer2_dance_comment_stage == 0:
        customer2 "О-о-о-о! Ты же тут на сцене танцуешь!"
        customer2 "Решила спуститься к папочке? Аха-ха!"
        m "Нет, Вы меня с кем-то путаете."
        m "Я работаю здесь официанткой..."
        customer2 "Папочку нехорошо обманывать!"
        m "Я не обманываю..."
        customer2 "Ой, да ладно тебе!!!"
        m "Вы что-то будете заказывать? Или я могу идти?"

    #

    customer2 "Эй, официантка! Мне еще пива! Кстати, как тебя зовут?"
    # если не первый раз
    if get_pub_visitor_visits(obj_name) > 2:
        customer2 "Я все время забываю!"
    img 14241
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14242
    with fade
    customer2 "И постарайся успеть, пока я не допил свой бокал!"
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14243
    with fade
    w
    sound snd_plates1
    img 14244
    with diss
    w
    sound snd_beer_table
    img 14245
    with diss
    m "Ваше пиво."
    music Groove2_85
    img 14246
    with fade
    customer2 "Ага, могла бы и побыстрее, хотя все вы, деревенщины медлительные."
    img 14247
    with diss
    m "Вообще-то я не из деревни."
    img 14248
    with fade
    customer2 "Ну да, рассказывай. Если бы ты была не из деревни, тебя бы здесь не было!"
    customer2 "Свободна! И подходи ко мне время от времени, я быстро пью."
    customer2 "И, если будешь хорошо работать, может и заработаешь..."
    img 14239
    with diss
    mt "Да что ты знаешь про меня? Неудачник!"
    return

label gallery_14254:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14249
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 1:
        customer3 "А, это ты?"
        customer3 "Пойдем в приват?"
        m "Я не танцую. Тем более, приват!"
        customer3 "А если я тебе щедро заплачу?"
        mt "Таким неудачникам, как ты, можно только мечтать обо мне."
        mt "И не только неудачникам... Вообще всем!"
        m "Вы меня с кем-то путаете."
        customer3 "Я спрошу у Джо..."
        mt "!!!"

    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 0:
        customer3 "Твоя задница со сцены смотрится отлично."
        m "Вы меня с кем-то путаете."
        m "Я просто официантка..."
        customer3 "Я хорошо запоминаю задницы. И твою я отлично помню."
        m "Я не танцую здесь на сцене."
        customer3 "Можешь дальше врать, мне все равно."
        mt "!!!"
        mt "Он что о себе возомнил?!"

    #

    m "Вам что-нибудь принести?"
    img 14250
    with diss
    customer3 "Скучно мне..."
    img 14251
    with diss
    m "Может быть пиво?"
    img 14252
    with fade
    customer3 "Да ну его..."
    customer3 "Мне все надоело... Стриптизерши одни и те же изо дня в день, скучно..."
    customer3 "Но ты тут недавно... Как тебя зовут?"
    img 14253
    with diss
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14254
    with fade
    customer3 "Ага, ну и ладно, я все равно не запомню..."
    customer3 "Я вообще не запоминаю имена женщин, я запоминаю их жопы. И твою я запомнил!"
    customer3 "Как насчет танца?"
    img 14255
    with diss
    menu:
        "Не сегодня.":
            img 14256
            with fade
            m "Я официатка, стриптизом занимаются другие."
            img 14257
            with diss
            customer3 "Да знаю я, что другие. Но их я уже видел не один раз..."
            customer3 "Ладно, проваливай, никакого толку от тебя."
            img 14258
            with diss
            mt "Какого черта ты тут вообще сидишь, если ничего не заказываешь?"
            return
        "Я что, похожа на стриптизершу?":
            music Power_Bots_Loop
            img 14259
            with fade
            m "Я что, похожа на стриптизершу?"
            m "Даже не вздумай меня спрашивать о таком!"
            img 14260
            with diss
            customer4 "Мда, скучно... А ты еще и грубиянка... Думаю, стоит рассказать об этом Джо."
            customer4 "Или не стоит... Что-то совсем лениво."
            customer4 "Иди отсюда! Клиенты ждут!"
            img 14258
            with diss
            mt "Козел!"
            return

label gallery_14268:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14261
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    music Groove2_85
    img 14262
    with vpunch
    customer3 "Ого! Вот это дамочка!"
    # смотрит на монику
    img 14263
    with fade
    customer3 "У тебя должна быть прекрасная попка!"
    customer3 "Но ничего, сейчас ты пойдешь мне за заказом и я ее рассмотрю."
    customer3 "В общем мне пиво. Давай, поворачивайся уже!"
    img 14264
    mt "Вот извращенец."
    mt "Хотя откуда могут быть нормальные люди в этой дыре?"
    img 14265
    with diss
    m "Что к пиву?"
    img 14269
    with diss
    customer3 "Ничего, давай уже!"
    # поворачивается
    sound highheels_short_walk
    img 14266
    with diss
    w
    sound Jump1
    img 14267
    with diss
    w
    sound snd_whistle1
    img 14268
    with diss
    customer3 "Да! Я знал! Ай да жопа!"
    # уходит - приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14270
    with fade
    w
    sound snd_plates1
    img 14271
    with diss
    w
    sound snd_beer_table
    img 14272
    with diss
    m "Вот, пожалуйста."
    music Groove2_85
    img 14273
    with fade
    customer3 "О да! Жду твою жопу на пилоне!"
    img 14264
    with diss
    mt "Не дождешься..."
    return

label gallery_14294:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14274
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 1:
        customer3 "Так что? Надумала насчет моего предложения?"
        m "Какого предложения? Вы что-то хотели заказать?"
        customer3 "Тебя хочу. Сколько будет стоит?"
        mt "Моника, спокойно. Просто очередной пьяница. Их тут целый паб."
        m "Я работаю официанткой и меня нельзя заказать."
        customer3 "А если я тебе щедро заплачу?"
        mt "Отдашь всю свою зарплату за год? Думаю, даже этого будет недостаточно."
        mt "Таким неудачникам, как ты, можно только мечтать обо мне."
        mt "И не только неудачникам... Вообще всем!"
        m "Вы меня с кем-то путаете."
        customer3 "Я спрошу у Джо..."
        mt "!!!"

    if monicaStartedStripDanceFlag == True and customer3_dance_comment_stage == 0:
        customer3 "Я думал, ты уже не официанткой здесь работаешь... "
        customer3 "Твоя задница со сцены смотрится отлично."
        m "Вы меня с кем-то путаете."
        m "Я просто официантка..."
        customer3 "Я хорошо запоминаю задницы. И твою я отлично помню."
        customer3 "Сколько стоит приват? Я заплачу."
        m "Я не танцую здесь на сцене. Тем более, не танцую при..."
        customer3 "Окей. Можешь дальше врать, мне все равно."
        customer3 "Как надумаешь насчет приват танца, знаешь, где меня найти."
        mt "!!!"
        mt "Он что о себе возомнил?!"
        mt "Всего лишь очередной неудачик, который спускает все свои деньги на шлюх и пиво!"

    #

    m "Что будете заказывать?"
    img 14275
    with diss
    customer3 "Возможно, что-то и буду..."
    customer3 "Для начала, давай поговорим, а то скучно."
    img 14276
    with diss
    menu:
        "Хорошо.":
            music Hidden_Agenda
            img 14277
            with fade
            m "Хорошо."
            img 14278
            with diss
            mt "Похоже лучше поговорить с этим придурком, иначе он разольет пиво или что-нибудь еще..."
#            mt "Нмчего же не произойдет, если я с ним немного поговорю."
            pass
        "Мне некогда.":
            music Groove2_85
            img 14279
            with fade
            m "Мне некогда."
            img 14280
            with diss
            customer3 "Я клиент. И я могу сказать Джо, что ты не выполняешь мои просьбы."
            img 14281
            m "Но разговоры не входят в обязанности официантки!"
            img 14282
            with diss
            customer3 "Верно. Но тебе же нужны чаевые?"
            img 14278
            with fade
            mt "Мне противно, но если он даст чаевые, может и стоит потерпеть его дурной язык. Но только совсем чуть-чуть..."
#            mt "Здесь он прав, перекинусь с ним парой фраз..."
            img 14277
            with diss
#            m "Хорошо, немного поговрим."
            m "Хорошо, говори..."
            pass

    img 14283
    with fade
    customer3 "Напомни, как тебя зовут?"
    img 14284
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14285
    with fade
    customer3 "Очень приятно. Хотя это не важно, я не запомню. И кем ты работаешь, [monica_pub_name]?"
    music Groove2_85
    img 14286
    mt "Он что, издевается?"
    img 14287
    with diss
    m "Вы не видите? Я официантка."
    img 14288
    with fade
    customer3 "Да, я это вижу! [monica_pub_name] - официантка и я Билли - директор фирмы."
    img 14278
    with diss
    mt "Да что ты знаешь обо мне?"
    img 14289
    with fade
    customer3 "Наверняка ты хотела стать актрисой.... Или нет, моделью! А возможно ты мечтала создать модный журнал?"
    img 14290
    mt "Я его уже создала!"
    img 14291
    with fade
    customer3 "Но нет, ты [monica_pub_name] - официантка. И знаешь, [monica_pub_name]... Принеси мне бургер."
    img 14292
    with diss
    m "Хорошо."
    # поворачивается
    sound highheels_short_walk
    img 14293
    with diss
    w
    sound Jump1
    img 14294
    with diss
    w
    sound snd_whistle1
    img 14295
    with diss
    customer3 "И жопа у тебя просто отпад!"
    img 14296
    with diss
    mt "Извращенец..."
    # приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14345
    with fade
    w
    sound snd_plates1
    img 14346
    with diss
    w
    sound snd_beer_table
    img 14347
    with diss
    w
    img 14348
    with diss
    customer3 "Молодец, красивая жопа! Вот тебе целый доллар! Купи себе помаду!"
    img 14258
    with diss
    mt "Какой же он мерзкий..."
    return

label gallery_14303:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14298
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    customer5 "Какая красота! И давно ли ты тут?"
    # смотрит на монику
    img 14299
    with fade
    m "Я? Всего пару дней..."
    music In_Your_Arms
    img 14300
    with diss
    customer5 "Ой как хорошо! Теперь я буду бывать здесь еще чаще!"
    customer5 "Скажи, у тебя есть парень?"
    customer5 "Или нет... Где же мои манеры? Как тебя зовут?"
    img 14301
    mt "Не хватало еще, чтобы ко мне подкатывал какой-то кретин..."
    img 14302
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14303
    with fade
    customer5 "Ох... [monica_pub_name] и Джери...Шикарно звучит..."
    customer5 "Мне надо все обдумать... Лучше всего это делается за пивом..."
    customer5 "Да, ты не ответила на мой вопрос: У тебя есть парень?"
    img 14304
    with diss
    m "Вообще-то я замужем."
    # смотрит на моникт руку
    img 14305
    with diss
    w
    img 14306
    with fade
    customer5 "Понятно, ты врешь, кольца нет, значит ты свободна!"
    customer5 "У меня все шансы!"
    customer5 "В общем, мне пива!"
    music Groove2_85
    img 14301
    mt "Еще чего... Размечтался... Ему никогда не светит такая леди, как Я!"
    img 14307
    with diss
    m "Хорошо."
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Groove2_85
    img 14308
    with fade
    w
    sound snd_plates1
    img 14309
    with diss
    w
    sound snd_beer_table
    img 14310
    with diss
    m "Пожалуйста."
    music In_Your_Arms
#    img 14311
#    with fade
    img 14312
    with diss
    customer5 "Да, спасибо. Можешь идти."
    customer5 "Хотя стоп...Где же мои манеры? Вот тебе доллар. Скоро заработаешь себе на платье."
    img 14313
    with diss
    mt "Изысканные манеры... Фи!"
    return

label gallery_14318:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14317
    with fade
    m "Вам что-нибудь принести?"
    music Groove2_85
    img 14318
    with diss
    customer6 "А?! Ты что, не видишь, я сижу у стойки! Ик!"
    customer6 "Эй, бармен! Виски с колой! Или водку с колой?"
    customer6 "Ну или нет! Виски с водкой! Ик!"
    img 14319
    with diss
    mt "Да он похоже пьян... Думаю, Джо о нем позаботится..."
    return

label gallery_14320:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14320
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    img 14321
    with diss
    customer4 "Оу! Какая красивая мордашка! Новенькая?"
    # смотрит на монику
    music Groove2_85
    img 14322
    with diss
    m "Кто, Я?!"
    img 14323
    with fade
    customer4 "Нет, твоя мордашка! Ну конечно же ты!"
    customer4 "Мда... Понятно почему ты официантка."
    customer4 "Как зовут? Только не спрашивай кого..."
    img 14324
    mt "Он что, думает, что Я глупая?"
    mt "Я?!"
    img 14325
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14326
    with fade
    customer4 "Отлично, [monica_pub_name]! Я не буду говорить как меня зовут, и даже делать заказ."
    customer4 "Ты новенькая, не уверен, что эта информация уместится в твоей красивой головке."
    customer4 "Можешь идти, увидимся!"
    img 14327
    with diss
    mt "Почему он так со мной разговаривает? Я не глупая!"
    return

label gallery_14340:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14328
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer4_dance_comment_stage == 1:
        customer4 "А вот и официанточка, она же стриптизерша!"
        m "Я не стритизерша."
        customer4 "Ну, конечно! Еще скажи, что я снова перепутал."
        customer4 "Ты думала, в маске никто не узнает, кто ты на самом деле?"
        mt "???"
        mt "Он... узнал... м-меня?"
        mt "!!!"
        customer4 "Ты боишься, если узнают, что ты еще и официанткой тут работаешь, то приставать будут?"
        customer4 "Ладно. Я не скажу никому. Притворяйся дальше."
        mt "Как же этот придурок напугал меня!"
        mt "Фу-у-у... Что-то с нервами у меня совсем непорядок!"
        m "..."


    if monicaStartedStripDanceFlag == True and customer4_dance_comment_stage == 0:
        customer4 "Эй, отлично выступаешь на сцене!"
        m "Вы меня с кем-то путаете."
        m "Я здесь не танцую."
        customer4 "Я не могу тебя с кем-то путать. Я тебя видел на сцене!"
        m "Я не танцую на сцене."
        customer4 "Хммм... Странно..."
        mt "!!!"
        mt "Какое ему дело до этого?!"

    #

    m "Вам что-нибудь принести?"
    img 14329
    with diss
    customer4 "Да! Принеси мне пива и Ваш восхитительный Shiny бургер!"
    img 14330
    with diss
    m "Да, конечно."
    img 14331
    with fade
    customer4 "Запомнила? Одно пиво и Shiny бургер. Не харчо и не пасту!"
    music Groove2_85
    img 14332
    m "Я поняла!"
    img 14333
    customer4 "Я надеюсь..."
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14334
    with fade
    w
    sound snd_plates1
    img 14335
    with diss
    w
    sound snd_beer_table
    img 14336
    with diss
    m "Вот, пожалуйста!"
    img 14337
    with fade
    customer4 "Ой, какая молодец! Все как надо!"
    customer4 "Держи доллар за красивую мордашку! А если улыбнешься, дам два!"
    img 14338
    with diss
    menu:
        "Улыбнуться.":
            music Hidden_Agenda
            img 14339
            with diss
            mt "Доллар за одну улыбку... Чтож, пускай..."
            mt "Он не знает что я буду думать, пока улыбаюсь ему..."
            music Loved_Up
            img 14340
            with fadelong
            w
            mt "Придурок..."
            w
            img 14341
            with diss
            customer4 "Какая умничка, держи еще доллар!"
            return
        "Не улыбаться.":
            # стоит с каменным лицом
            music Groove2_85
            img 14342
            with fade
            mt "С чего бы мне улыбаться этой деревенщине?"
            img 14343
            with diss
            m "..."
            img 14344
            with diss
            customer4 "Не хочешь? Это все потому, что ты тут недавно..."
            return

label gallery_14358:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14314
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer5_dance_comment_stage == 1:
        customer5 "А я тебя ждал!"
        m "Да? Хотите сделать заказ?"
        customer5 "Конечно! Скажи, а сколько будет стоить приват с тобой?"
        m "!!!"
        m "Я не танцую!"
        mt "Как же они меня все достали со своими расспросами!!!"
        customer5 "Не, теперь ты меня не обманешь! Я видел тебя на сцене!"
        m "Вы меня с кем-то перепутали. Тут работает девушка, она немного похожа на меня..."
        customer5 "Да? Это она новенькая стриптизерша?"
        m "Да."
        customer5 "А как мне заказать у нее приват?"
        m "Не знаю. По-моему, она только на сцене танцует и в приват не ходит."
        customer5 "Жаль..."



    if monicaStartedStripDanceFlag == True and customer5_dance_comment_stage == 0:
        customer5 "Ого! Ты же на сцене танцуешь!"
        m "Вы меня с кем-то путаете."
        m "Я не танцую на сцене."
        customer5 "Серьезно? По-моему, это ты была!"
        m "Я работаю тут просто официанткой и не танцую стриптиз."
        customer5 "Вот черт. Видимо, я перебрал с пивом тогда..."
        mt "Неудивительно..."

    #


    m "Вам что-нибудь принести?"
    img 14315
    with diss
    customer5 "Да! Мне пожалуйста два бургера, и два Ваших самых лучших коктейля!"
    img 14316
    with diss
    m "Хорошо, один момент!"
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14349
    with fade
    w
    sound snd_plates1
    img 14350
    with diss
    w
    sound snd_beer_table
    img 14351
    with diss
    w
    img 14353
    with diss
    m "Вот, пожалуйста! Что-нибудь еще?"
    music In_Your_Arms
    img 14354
    with fade
    customer5 "Да, Вас! Не зря же я купил всего по два!"
    customer5 "Садитесь рядом и давайте пообщаемся!"
    customer5 "Я верю, что мы созданы друг для друга!"
    menu:
        "Сесть рядом с клиентом. (в будущих обновлениях) (disabled)":
            # в след обнове
            return
        "Не буду!":
            # клиент злой
            m "Не буду!"
            music Power_Bots_Loop
            img 14355
            with fade
            customer5 "Ах ты глупая официантка! Даже школьницы знают этот способ знакомства!"
            customer5 "Не могла сказать сразу?!"
            img 14357
            with diss
            m "Я подумала, что Вы очень голодный."
            m "Что-нибудь еще?"
            img 14358
            with diss
            customer5 "Да! Свали отсюда!"
            return

label gallery_14370:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14359
    with fadelong
    m "Вы готовы сделать заказ?"
    # рассматривает
    sound snd_whistle1
    img 14360
    with diss
    w
    music Groove2_85
    img 14361
    with fade
    customer10 "Да! Я желаю Вас. Сколько?"
    music Power_Bots_Loop
    img 14362
    with hpunch
    m "Что? Вы это о чем? Я не продаюсь!"
    img 14363
    with diss
    customer10 "Серьезно? У всего есть цена..."
    customer10 "Как тебя зовут?"
    music Groove2_85
    img 14364
    with fade
    m "Меня зовут [monica_pub_name]."
    img 14365
    with diss
    customer10 "Любопытно... [monica_pub_name] - это сценическое имя или настоящее?"
    img 14366
    mt "Почему он спрашивает?"
    img 14367
    with diss
    m "Конечно настоящее!"
    img 14368
    with fade
    customer10 "Правда? Я думаю, тебе бы больше пошло имя Анжелина! Или Виолетта!"
    customer10 "Что думаешь?"
    img 14369
    with diss
    m "Ничего... Мне мое имя нравится..."
    img 14370
    with diss
    customer10 "А мне вот что-то не очень... Надо бы тебе придумать другое имя...Подумай над этим!"
    customer10 "А пока принеси мне что-нибудь выпить!"
    img 14371
    with diss
    m "Да, хорошо."
    # уходит приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14372
    with fade
    w
    sound snd_plates1
    img 14373
    with diss
    w
    sound snd_beer_table
    img 14374
    with diss
    customer10 "А...Виолетта! Наконец то!"
    music Groove2_85
    img 14375
    m "Я не Виолетта..."
    img 14376
    with diss
    customer10 "Это не важно, но важно то, что я тут постоянный клиент и советую тебе это запомнить, Виолетта!"
    customer10 "Но я могу тебя звать и Новенькая... Что думаешь?"
    img 14377
    mt "Что ты урод!"
    img 14378
    with diss
    m "Меня зовут [monica_pub_name]."
    img 14379
    with fade
    customer10 "Да, Виолетта, я помню!"
    customer10 "Кстати, спасибо за выпивку. Еще увидимся."
    img 14380
    with diss
    mt "Надеюсь, нескоро."
    return

label gallery_14383:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14381
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer11_dance_comment_stage == 1:
        customer11 "Не буду ничего говорить про то, как ты танцуешь у пилона."
        m "Я..."
        customer11 "А то снова будет много слов о том, что ты не такая."
        customer11 "Ты же официантка сейчас?"
        m "Да..."
        customer11 "Давай, ты просто выполнишь свою работу и все?"
        mt "?!"

    if monicaStartedStripDanceFlag == True and customer11_dance_comment_stage == 0:
        customer11 "Ты неплохо танцевала в прошлый раз на сцене."
        m "!!!"
        m "Вы меня с кем-то путаете. Я не танцую на сцене."
        customer11 "Расскажи это кому-нибудь другому."
        m "Я официантка, а не стрип..."
        customer11 "Мне это неинтересно совсем!"
        mt "!!!"
        mt "Очередной хам..."

    #


    m "Вы готовы сделать заказ?"
    # рассматривает
    sound snd_whistle1
    img 14382
    with diss
    w
    music Groove2_85
    img 14383
    with diss
    customer11 "А ты конфетка!"
    customer11 "В общем все просто: мне пиво и бургер и быстро!"
    img 14384
    m "Да, конечно!"
    img 14385
    customer11 "И можно это делать без слов. Быстро пошла и принесла мой заказ."
    img 14386
    with diss
    mt "Грубиян..."
    # уходит приходит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14387
    with fade
    w
    sound snd_plates1
    img 14388
    with diss
    w
    sound snd_beer_table
    img 14389
    with diss
    w
    img 14390
    with fade
    customer11 "Вот видишь, все очень просто. Молодец, держи." # дает чай
    img 14391
    with diss
    m "Спасибо."
    music Groove2_85
    img 14392
    with diss
    customer11 "Да, да... Иди уже..."
    img 14393
    with fade
    mt "Очередной придурок."
    return

label gallery_14395:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14394
    with fadelong
    m "Здравствуйте! Что будете заказывать?"
    img 14395
    with diss
    customer9 "Оу! Новенькая? Скажи, ты любишь подарки?"
    img 14396
    mt "Подарки? Вероятно, он о чаевых..."
    img 14397
    with diss
    menu:
        "Ну да...":
            music Hidden_Agenda
            img 14398
            with fade
            m "Да."
            img 14399
            with diss
            customer9 "Я так и думал. Вот скажи, что тебе подарить?"
            img 14400
            with diss
            m "У меня все есть, но чаевые были бы кстати."
            img 14401
            with fade
            customer9 "Нет, я не о чаевых. Как насчет страстного поцелуя?"
            music Groove2_85
            img 14402
            with diss
            m "Нет, спасибо."
            img 14403
            with diss
            mt "Да как он может подобное спрашивать у такой как Я!?"
            if monicaBitch == True:
                mt "Придурок!"
            pass
        "Я не готова отвечать на этот вопрос.":
            music Groove2_85
            img 14404
            with fade
            m "Я не готова отвечать на этот вопрос."
            img 14405
            with diss
            customer9 "Я понял... Свидетели... Хорошо, не отвечай, потом расскажешь!"
            pass
    # смотрит на монику
    img 14406
    with fade
    customer9 "Ты любишь классический секс или в попу?"
    music Power_Bots_Loop
    img 14407
    with hpunch
    m "А?!"
    img 14408
    customer9 "Я понял! Это значит в попу... Иначе ты бы не работала в Shiny Hole."
    img 14403
    with diss
    mt "Он нормальный?"
    img 14409
    with fade
    customer9 "Мне пожалуй ничего, но я очень рад нашему знакомству!"
    img 14410
    with diss
    mt "Неадекватный урод..."
    return

label gallery_14413:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14412
    with fadelong
    m "Вы готовы сделать заказ?"
    # рассматривает
    img 14413
    with diss
    w
    sound Jump1
    img 14414
    with diss
    w
    img 14415
    with fade
    customer12 "А время зря не теряет..."
    customer12 "Как зовут?"
    img 14416
    with diss
    m "Меня зовут [monica_pub_name]."
    music Groove2_85
    img 14417
    with fade
    customer12 "Сколько стоят твои сиськи, [monica_pub_name]?"
    customer12 "Думаю, сколько приготовить тебе на чай. Я плачу 1 процент от цены сисек."
    music Power_Bots_Loop
    img 14418
    with hpunch
    m "Вы о чем? Они не продаются!"
    img 14419
    with fade
    customer12 "Не обмынывай! Ну дак что, сколько ты заплатила за операцию?"
    img 14420
    m "Они настоящие!"
    music Groove2_85
    img 14421
    with fade
    customer12 "Ну да, значит твои чаевые составят ноль долларов. Хотя кто знает..."
    customer12 "Другая официантка получает по 3 доллара, имей ввиду..."
    img 14422
    with diss
    mt "О чем ты вообще? Лучше бы я к тебе не подходила!"
    img 14424
    with fade
    customer12 "И это только за сиськи. А ведь есть еще и зад..."
    customer12 "Какая-то ты не разговорчивая для первого раза... Тогда и я ничего не буду заказывать..."
    img 14423
    with diss
    mt "Похоже, половина посетителей этого бара ненормальные..."
    return

label gallery_14428:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music RocknRoll_loop
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False:
        img 14453
        with fadelong
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        img 14425
        with fadelong
    m "Здравствуйте! Что будете заказывать?"
    img 14426
    with diss
    customer7 "Заказ? Да, готовы, но мы скажем, что мы хотим официантке, а Ты поднимайся! Надоело уже смотреть на эту стриптизершу."
    # смотрит на монику
    img 14427
    with diss
    m "Я и есть официантка..."
    img 14428
    with fade
    customer7 "Да? Да быть не может! Ты гораздо эффектнее смотрелась бы на пилоне!"
    customer7 "Ты новенькая?"
    customer7 "Как тебя зовут?"
    img 14429
    with diss
    m "Да, я тут недавно. Меня зовут [monica_pub_name]"
    img 14430
    with fade
    customer7 "[monica_pub_name], ты хочешь заработать?"
    img 14431
    with diss
    mt "Да я зарабатываю побольше, чем вся твоя семья и твой товарищ, и все их родственники во всем мире!"
    img 14432
    with diss
    m "Да, именно за этим я здесь."
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False:
        img 14454
        with fadelong
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        img 14433
        with fadelong
    customer7 "Я так и думал... Просто для информации: гораздо больше можно заработать тут.." # показывает на шест
    img 14434
    with diss
    m "Мне это не интересно."
    img 14435
    with fade
    customer7 "Да, да, все так говорят, пока не узнают какие тут деньги..."
    img 14437
    mt "Неужели и правда большие?"
    img 14455
    with diss
    menu:
        "И какие же?":
            img 14456
            with fade
            m "И какие же?"
            img 14457
            with fade
            customer7 "Ну за представление можно заработать 100 долларов..."
            customer7 "Но все зависит от того, что ты покажешь..."
            img 14458
            m "Я поняла, мне это неинтересно."
            img 14459
            with diss
            mt "100 долларов за вечер? Немаленькие деньги для такой дыры..."
            mt "Но это не для меня! Я не собираюсь танцевать у всех на виду!"
            pass
        "Мне это не интересно.":
            img 14460
            with fade
            m "Говорю же, мне это не интересно."
            img 14461
            with diss
            customer7 "Конечно, конечно, это пока..."
            pass
    img 14462
    with fade
    customer7 "А пока, принеси нам два шота! На свой вкус."
    img 14463
    with diss
    m "Хорошо."
    # уходит принтсит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music RocknRoll_loop
    img 14464
    with fade
    w
    img 14465
    with diss
    w
    sound snd_plates1
    img 14466
    with diss
    w
    sound snd_beer_table
    img 14467
    with fade
    customer7 "То что надо! Похоже, ты умеешь читать мысли!"
    customer7 "Вот, держи!" # дает доллар
    customer7 "Приходи к нам чаще! Я вижу в тебе потенциал."
    img 14468
    mt "Какой еще потенциал?"
    img 14469
    with diss
    m "До свидания."
    return

label gallery_14452:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14438
    with fadelong


    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer12_dance_comment_stage == 1:
        customer12 "О, это ты! Слушай, а как насчет привата?"
        m "Я не танцую приват... И на сцене не танцую."
        customer12 "Я это уже слышал... Аха-ха!!!"
        customer12 "Хорош уже строить из себя невинную цыпочку!"
        customer12 "Сколько за приват?"
        mt "?!"
        m "Я не танцую приват!"
        customer12 "А зря! Могла бы хорошо заработать!"
        customer12 "Ладно, думаю, это временно. Скоро ты передумаешь."
        mt "!!!"
        mt "Ни за что не пойду в приват!"
        mt "За кого он меня принимает?!"


    if monicaStartedStripDanceFlag == True and customer12_dance_comment_stage == 0:
        customer12 "Эй, ты же у пилона теперь сиськами трясешь!"
        customer12 "Или ты здесь на двух работах?"
        m "!!!"
        m "Вы меня с кем-то путаете. Я не танцую на сцене."
        customer12 "Ну конечно! Я что, слепой что-ли?!"
        m "Я просто официантка..."
        customer12 "Ну ладно. Не хочешь - не говори."
        customer12 "Только на сцене в следующий раз танцуй без этих своих шмоток."
        m "!!!"
        customer12 "Тогда не придется подрабатывать официанткой."
        customer12 "За такие сиськи чаевых много будут платить."
        mt "Фу, как грубо!"
        mt "По-моему, здесь все такие грубияны!"
        mt "!!!"
        mt "Как мне надоела эта дыра!"

    #


    m "Здравствуйте, что будете заказывать?"
    img 14439
    with diss
    customer12 "Пиво, бургер и ваш изумительный харчо!"
    img 14440
    with diss
    m "Да, хорошо, сейчас сделаем."
    # разворачивается спиной , кастомер бьет ее по жопе + звук шлепка
    sound snd_slap1
    img 14441
    with hpunch
    sound_from_side "(шлепок)"
    img 14442
    customer12 "Вот именно поэтому ты получаешь чаевые!"
    img 14443
    with diss
    menu:
        "Какого?!":
            music Power_Bots_Loop
            img 14444
            with fade
            m "Еще раз так сделаешь, и тебе не сдобровать!"
            img 14445
            with diss
            customer12 "Оу, какая ты злая, оказывается..."
            customer12 "Давай, неси уже мой заказ!"
            customer12 "И кстати, ты только что обнулила свои чаевые."
            # уходит за заказом, приходит, ставит на стол
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Groove2_85
            sound snd_plates1
            img 14446
            with fade
            w
            sound snd_beer_table
            img 14447
            with diss
            w
            img 14448
            with fade
            customer12 "Можешь идти. Если в следующий раз не будешь грубить, получишь пару долларов."
            img 14449
            with diss
            mt "Идиот..."
            return
        "Проигнорировать.":
            music Hidden_Agenda
            img 14451
            with fade
            mt "И не только поэтому..."
            img 14452
            with diss
            customer12 "Постарайся сделать так, чтобы я получил свой заказ как можно скорее."
            # уходит за заказом, ставит на стол
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 1.0
            music Hidden_Agenda
            sound snd_plates1
            img 14446
            with fade
            w
            sound snd_beer_table
            img 14447
            with diss
            w
            img 14450
            with diss
            customer12 "Как раз вовремя! Молодчина!"
            customer12 "Вот, держи! Доллар за скорость и доллар за твою попку!"
            customer12 "Что стоишь? Иди, не заставляй клиентов ждать!"
            return

label gallery_14474:
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music RocknRoll_loop

    img 14470
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer78_dance_comment_stage == 1:
        customer7 "Эй, детка! Когда уже разденешься на сцене?!"
        m "Я... Я не танцую..."
        customer7 "Мы это уже слышали. Не танцует она! Аха-ха!!!"
        customer7 "Запомни: чем меньше одежды на сцене, тем больше чаевые!"
        m "!!!"
        mt "Похотливые животные! Ненавижу!"
        m "Я..."
        customer7 "А если пойдешь с нами в приват, то заработаешь раз в десять больше!"
        m "Я не танцую!"
        mt "!!!"
        customer7 "А если будешь работать официанткой с голыми сиськами..."
        customer7 "То чаевых будет еще больше! Аха-ха!!!"
        mt "!!!"



    if monicaStartedStripDanceFlag == True and customer78_dance_comment_stage == 0:
        customer7 "О, детка! Правильно сделала, что послушалась нашего совета!"
        m "Какого совета?"
        customer7 "Отпадные сиськи! На сцене выглядишь охренительно!"
        m "Я официантка, а не стриптизерша..."
        customer7 "Конечно, конечно... А то я тебя не разглядел на сцене отсюда!"
        m "Я..."
        customer7 "В следующий раз снимай с себя все эти тряпки на сцене."
        customer7 "Если хочешь заработать хорошие чаевые."
        mt "!!!"

    #


    m "Что будете..."
    img 14471
    with diss
    customer7 "Нам два шота! И быстро! Хотим их выпить перед очередным выступлением!"
    img 14472
    with diss
    m "Хорошо, один момент!"
    # уходит - приносит
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.0
    music Hidden_Agenda
    img 14464
    with fade
    w
    img 14465
    with diss
    w
    sound snd_plates1
    img 14466
    with diss
    w
    sound snd_beer_table
    img 14473
    with diss
    m "Вот, пожалуйста! Что-нибудь еще?"
    img 14474
    with fade
    customer7 "Да, вот еще что! Не могла бы ты в следующия раз быть побыстрее!"
    customer7 "Похоже тебя сюда взяли по двум причинам. Эти причины: сиськи и жопа! Но уж точно не скорость!"
    music RocknRoll_loop
    img 14467
    with diss
    w
    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False:
        img 14454
        with fadelong
    if get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        img 14433
        with fadelong
    customer7 "А теперь иди, шоу уже началось!"
    img 14475
    with diss
    mt "Козлы..."
    return

label gallery_14477:
    music Hidden_Agenda
    sound highheels_short_walk
    img 14411
    with fadelong

    # комментарий насчет танцев
    if monicaStartedStripDanceFlag == True and customer9_dance_comment_stage == 1:
        customer9 "Эй, не могу дождаться, когда ты покажешь свою голую попку со сцены!"
        m "Вы меня с кем-то..."
        customer9 "Я хочу, чтобы ты сняла с себя трусики на сцене и бросила их мне..."
        customer9 "Я хочу забрать их..."
        customer9 "Я готов заплатить за это. Сколько? Назови цену."
        mt "?!"
        m "Я не танцую на..."
        customer9 "Не хочешь говорить? Хорошо, я буду ждать этого момента."
        customer9 "А потом просто заберу их..."
        mt "..."
        mt "Человек, озабоченный чужими трусами!"
        mt "Кого только не встретишь в этой дыре!"
        mt "!!!"


    if monicaStartedStripDanceFlag == True and customer9_dance_comment_stage == 0:
        customer9 "У меня в штанах дымится, когда вижу тебя на сцене!"
        m "!!!"
        m "Вы меня с кем-то путаете. Я не танцую на сцене."
        customer9 "Расскажи это кому-нибудь другому."
        m "Я официантка, а не стрип..."
        customer9 "Охренительная задница!!!"
        customer9 "Не могу дождаться, когда ты ее оголишь на сцене перед всеми!"
        m "Я..."
        customer9 "А еще хочу увидеть, как ты танцуешь только для меня..."
        mt "Долбанный извращенец!"
        mt "По-моему, здесь все такие!"
        mt "!!!"
        mt "Как мне надоела эта дыра!"

    #


    m "Что будете заказывать?"
    # чел резко хватает монику и садит себе на колени
    music Groove2_85
    sound Jump1
    img 14476
    with vpunch
    m "Ай!"
    sound Jump2
    img 14477
    with hpunch
    customer9 "Скажи, ты была хорошей девочкой?"
    customer9 "Расскажи Санте!"
    customer9 "И возможно, Санта сделает тебе хороший подарок!"
#    mt "Меня посадил к себе на колени незнакомый мужик! Возможно, стоит ему подыграть..."
    img 14478
    with diss
    menu:
        "Быстро отпусти меня!":
            music Power_Bots_Loop
            sound snd_punch_face2
            img 14479
            with diss
            m "Быстро отпусти меня!"
            sound Jump1
            img 14480
            with diss
            m "Еще раз попробуй сделай так и я сломаю тебе нос, урод!"
            # моника вырывается
            img 14481
            with fade
            customer9 "Ах вот ты как! Ну и вали! Ваше пиво кстати отстой!"
            img 14482
            with diss
            mt "Что же ты его тогда пьешь?"
            return
        "Да, я была хорошей девочкой.":
            label gallery_14485:
            music Hidden_Agenda
            img 14483
            with fade
            m "Да, я была хорошей девочкой."
            img 14484
            with diss
            customer9 "Я так и думал! Уверен, ты обслужила очень много клиентов и они остались довольны."
            # кладет ей под чулок купюру
            sound snd_take_paper
            img 14485
            with diss
            w
            img 14486
            with fade
            customer9 "Ладно, беги, у меня еще есть пиво."
            img 14487
            with diss
            mt "Он дал мне 20 долларов! Ничего себе..."
            return

label gallery_21047:
# Если идет, вызывается меню со сценами с Джо (открываются последовательно)
# Сцена1:
# Трогает зад
# Джо
    music Loved_Up
    img 21027
    with fadelong
    joe "О, [monica_pub_name], ты пришла!"
    m "Да, Джо, я пришла."
    music Groove2_85
    img 21028
    with diss
    joe "Тебя точно не видела Эшли?"
    joe "Не видела как ты сюда заходила?"
    img 21029
    with diss
    m "Нет, Джо."
    m "Меня не видела Эшли."
    m "Но она может придти сюда в любой момент."
    img 21030
    with fade
    joe "Нет, [monica_pub_name], она не придет."
    joe "Пока меня нет, она не оставит бар без присмотра."
    joe "У нас здесь, знаешь-ли, такие клиенты... хе-хе."
    img 21031
    m "Я знаю какие здесь клиенты, Джо..."
    img 21032
    joe "..."
    music Hidden_Agenda
    img 21033
    with fade
    m "Джо, я готова еще раз извиниться за то что не отдала деньги."
    m "Я правда забыла и..."
    music Loved_Up
    sound Jump1
    img 21034
    with diss
    joe "[monica_pub_name], хватит про эти деньги."
    joe "Мне не нужны эти деньги, я хочу тебя, [monica_pub_name]!"
    joe "Я хочу твою попку, [monica_pub_name]!"
    music Power_Bots_Loop
    img 21035
    with hpunch
    m "Джо, это исключено!"
    m "У тебя есть жена, которая прямо за стенкой!"
    m "Да, я хочу работать здесь, но я не собираюсь за это спать с таким жирным толстяком, как ты, Джо!"
    music Loved_Up
    img 21036
    with fade
    joe "[monica_pub_name], очень жаль."
    img 21037
    with diss
    joe "Но повернись, хотя бы, своей попой."
    joe "Покажи ее мне!"
    img 21038
    with diss
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            m "Нет, Джо!"
            return
    music Groove2_85
    img 21039
    with fade
    m "И на этом все, ты сделаешь так, чтобы Эшли простила меня!"
    img 21040
    with diss
    joe "Хорошо, [monica_pub_name]."
    joe "Повернись своей попой, скорее!"
    music Hidden_Agenda
    img 21041
    with fade
    m "..."
    mt "Дьявол, мне не хочется делать этого!"
    mt "С другой стороны, в этом нет ничего страшного и это позволит мне снова работать здесь..."
    mt "Мне нужны деньги..."
    img 21042
    with diss
    m "..."
    joe "Я жду!"
    # Моника показывает зад
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 21043
    with fadelong
    w
    img 21044
    with diss
    w
    sound Jump1
    img 21045
    with diss
    w
    img 21046
    with diss
    joe "!!!"
    music Groove2_85
    img 21047
    with fade
    m "Все? Достаточно?"
    sound Jump1
    img 21048
    with diss
    joe "[monica_pub_name], я должен потрогать твою попу!"
    joe "Она такая сладкая! Я хочу этого, [monica_pub_name]!"
    music Power_Bots_Loop
    img 21049
    with hpunch
    m "Нет!"
    music Groove2_85
    img 21050
    with fade
    joe "Я потрогаю ее и обещаю что Эшли простит тебя!"
    music Hidden_Agenda
    img 21051
    with diss
    mt "Черт! Что же мне делать?"
    mt "Мне нужна эта работа. Я могу здесь заработать хотя бы на еду..."
    mt "Но неужели я соглашусь на то, чтобы какой-то толстяк в трущобах лапал меня?!"
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21049
            m "Нет, Джо!"
            return
    music Groove2_85
    img 21052
    with fade
    m "Ладно, но только в одежде!"
    m "И я не буду отдавать те чаевые, которые взяла себе!"
    music Loved_Up
    img 21053
    with diss
    joe "Хорошо, [monica_pub_name]!"
    joe "Можешь оставить эти деньги себе!"
    label gallery_21061:
    music stop
    img black_screen
    with diss
    pause 1.5
    # трогает
    music Loved_Up
    img 21054
    with fadelong
    joe "Ахххх!"
    joe "Как я мечтал об этом!"
    sound Jump1
    img 21055
    with diss
    joe "Я стал мечтать об этом с первой минуты, когда увидел тебя здесь, [monica_pub_name]!"

    img 21056
    with diss
    w
    sound Jump2
    img 21057
    with diss
    w
    stop music
    play music "Sounds/audio_Monica_Joe_Ass_1.mp3"
    scene black
    image videov_Monica_Joe_Ass_1_1 = Movie(play="video/v_Monica_Joe_Ass_1_1.mkv", fps=30)
    show videov_Monica_Joe_Ass_1_1
#    with fadelong
    wclean
    stop music
    music stop
    music Loved_Up
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    img 21056
    with diss
    w
    sound hlup25
    img 21057
    with diss
    w
    music Groove2_85
    img 21058
    with fade
    mt "Очередной озабоченный мерзавец!"

    music stop
    img black_screen
    with diss
    pause 1.5
    stop music
    play music "Sounds/audio_Monica_Joe_Ass_1.mp3"
    scene black
    image videov_Monica_Joe_Ass_1_2 = Movie(play="video/v_Monica_Joe_Ass_1_2.mkv", fps=30)
    show videov_Monica_Joe_Ass_1_2
    with fadelong
    wclean
    stop music
    music stop

    music Loved_Up2
    img 21059
    with diss
    joe "Ах, твоя попка!"
    img 21060
    with diss
    joe "Она такая упругая!"
    img 21061
    with diss
    joe "Ах!"
    music Groove2_85
    img 21062
    with fade
    m "Ну все, хватит!"
    m "Идем к Эшли!"
    return

label gallery_21180:
# Эшли
# Просит поцеловаться (хватает Монику за зад, под джинсы)
    music Groove2_85
    img 21172
    with fadelong
    m "Я пришла, Эшли..."

    music Loved_Up
    img 21173
    with diss
    ashley "О, [monica_pub_name]!"
    sound Jump1
    img 21174 # jump
    with diss
    ashley "Иди ко мне!"
    ashley "Я ждала когда ты что-нибудь натворишь..."
    img 21175
    with diss
    ashley "Иди ко мне! Иди я поцелую тебя!"
    img 21176
    with diss
    menu:
        "Позволить Эшли поцеловать себя.": #corruption
            pass
        "Отказать.":
            music Power_Bots_Loop
            img 21177
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return
#    music Loved_Up
    # Эшли целует Монику
    sound snd_longkiss1
    img 21178
    with fade
    ashley "Ммммм..."
    sound snd_longkiss1
    img 21179
    with fade
    mt "!!!"


    music audio_longkiss1
    scene black
    image videov_Monica_Ashley_Kiss_1_1 = Movie(play="video/v_Monica_Ashley_Kiss_1_1.mkv", fps=30)
    show videov_Monica_Ashley_Kiss_1_1
    with fadelong
    wclean

    stop music
    music Loved_Up
    sound snd_longkiss1
    img 21180
    with diss
    ashley "Ммммм... Моя конфетка... Мммммм..."
    # Эшли пропускает руку Монике под джинсы сзади
    sound snd_longkiss1
    img 21181
    with fade
    w
    music Loved_Up2
    sound Jump2
    img 21182
    with diss
    #sound
    w
    sound snd_longkiss1
    img 21183
    with diss
    mt "!!!"

    music2 audio_longkiss1
    scene black
    image videov_Monica_Ashley_Kiss_1_1 = Movie(play="video/v_Monica_Ashley_Kiss_1_1.mkv", fps=30)
    show videov_Monica_Ashley_Kiss_1_1
    with fadelong
    wclean

    music2 stop
#    music Loved_Up2
    img 21184
    with diss
    ashley "Ах, эта сладкая попка... Мммммм..."
    img 21185
    with diss
    ashley "Какая она упругая... Мммммм...."
    # Моника отстраняется
    music Groove2_85
    img 21186
    with fadelong
    m "Эшли, пожалуйста, хватит!"
    img 21187
    with diss
    ashley "[monica_pub_name], ты получила прощение на этот раз..."
    ashley "Я подожду, пока ты снова что-нибудь не напроказничаешь..."
    img 21188
    mt "!!!"
    return

label gallery_21069:
# Трогает голую грудь
    music Loved_Up
    img 21063
    with fadelong
    joe "[monica_pub_name], ты пришла!"
    joe "Я хочу посмотреть твою грудь!"
    joe "Я хочу увидеть ее!"
    music Groove2_85
    img 21064
    with hpunch
    m "Нет!"
    img 21065
    with fade
    joe "Мне жаль, [monica_pub_name], но Эшли начнет что-то подозревать."
    joe "Это большой риск для меня."
    img 21066
    with diss
    mt "Дьявол! Снова я в такой глупой ситуации!"
    mt "Настолько-ли мне нужна эта дурацкая работа?!"
    menu:
        "Согласиться показать грудь.": #corruption
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21064
            with fade
            m "Нет, Джо!"
            return

    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 21067 # звук одежды
    with fadelong
    m "Ладно..."
    m "Только быстро..."
    # Моника снимает верх
    sound Jump1
    img 21068
    with fadelong
    joe "Ах! Какие сиськи!"
    img 21069
    with diss
    joe "Тебе определенно надо танцевать на сцене, [monica_pub_name]!"
    mt "!!!"
    img 21070
    with diss
    joe "Можно я потрогаю их?"
    m "Нет, Джо! Мы договорились!"
    music Groove2_85
    img 21071
    with fade
    joe "Я не могу так, не могу, [monica_pub_name]!"
    joe "Дай я только прикоснусь к ним и Эшли простит тебя, я обещаю!"
    music Hidden_Agenda
    img 21072
    with diss
    mt "Я не могу пойти на это!"
    mt "..."
    mt "Хотя... Он не знает кто я на самом деле..."
    menu:
        "Согласиться.": #corruption
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21071
            with fade
            m "Нет, Джо!"
            return
    music Groove2_85
    img 21073
    with fade
    m "Ты прикоснешься к моей груди буквально на секунду."
    joe "Да, [monica_pub_name], я обещаю!"
    img 21074
    with diss
    m "И больше никаких условий после этого."
    m "Обещаешь?!"
    joe "Да, [monica_pub_name], я обещаю!"
    music Hidden_Agenda
    img 21075
    with fadelong
    mt "Дьявол!"
    mt "Мое изысканное тело создано для того, чтобы быть на обложке модного журнала..."
    mt "До чего я докатилась, О БОЖЕ!"
    img 21076
    with diss
    mt "Хотя... Это не Я... Это [monica_pub_name]..."
    music stop
    img black_screen
    with diss
    pause 1.5
    music Loved_Up2
    img 21077
    with fadelong
    w
    # джо трогает грудь
    sound Jump2
    img 21078
    with diss
    joe "Ах, какие сиськи!"
    img 21079
    with diss
    joe "Вот это да!"
    music stop
    img black_screen
    with diss
    pause 1.5
    stop music
    play music "Sounds/audio_Monica_Joe_Boobs_1.mp3"
    scene black
    image videov_Monica_Joe_Boobs_1_1 = Movie(play="video/v_Monica_Joe_Boobs_1_1.mkv", fps=30)
    show videov_Monica_Joe_Boobs_1_1
#    with fadelong
    wclean
    stop music
    music stop
    music Loved_Up2

    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21080
    with diss
    w
    sound hlup10
    img 21081
    with diss
    w
    img 21082
    with diss
    w
    label gallery_21083:
    music stop
    img black_screen
    with diss
    pause 1.5
    stop music
    play music "Sounds/audio_Monica_Joe_Boobs_1.mp3"
    scene black
    image videov_Monica_Joe_Boobs_1_2 = Movie(play="video/v_Monica_Joe_Boobs_1_2.mkv", fps=30)
    show videov_Monica_Joe_Boobs_1_2
#    with fadelong
    wclean
    stop music
    music stop
    music Loved_Up2

    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21084
    with diss
    w
    sound hlup10
    img 21083
    with diss
    w
    img 21085
    with diss
    joe "Лучшие сиськи в shiny hole!"

    music Power_Bots_Loop
    img 21086
    with fade
    m "Все, Джо!"
    m "Хватит!"
    m "Идем к Эшли!"
    return

label gallery_21194:
    music Groove2_85
    img 21189
    with fadelong
    m "Я пришла, Эшли..."
    music Loved_Up
    img 21190
    with diss
    ashley "О, [monica_pub_name]!"
    ashley "Иди ко мне!"
    ashley "Дай я потрогаю твою киску!"
    menu:
        "Позволить Эшли потрогать свою киску.": #corruption
            pass
        "Отказать.":
            music Power_Bots_Loop
            img 21189
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return
    music Groove2_85
    img 21191
    with fade
    mt "О Боже!"
    mt "Что эта Эшли собралась делать?!"
    # Эшли запускает руку Монике в джинсы и трогает киску
    music Loved_Up
    sound Jump1
    img 21192
    with fade
    ashley "Да, [monica_pub_name]!"
    ashley "Чувствуешь меня?"
    sound audio_Monica_Cabinet_FaceSitting_3
    img 21193
    with diss
    m "Ахххх!"
    img 21194
    with diss
    w
    ashley "Наслаждаешься этим?"
    img 21195
    with diss
    m "Ахххх!"
    music Loved_Up2
    sound audio_Monica_Cabinet_Dildo_3
    img 21196
    with diss
    w
    img 21197
    with diss
    w
    ashley "Почуствуй меня, [monica_pub_name]!"
    img 21198
    with diss
    ashley "Если захочешь, это можно сделать по другому."
    img 21199
    with diss
    m "ААА! Ааааахх!"
    img 21200
    with diss
    ashley "Ах, какая ты вкусная, [monica_pub_name]!"

    music2 stop
    # Моника отстраняется
    music Groove2_85
    img 21201
    with vpunch
    m "Погоди, Эшли!"
    m "Я..."
    m "На меня что-то начинает накатывать..."
    m "Погоди, я боюсь этого..."
    music Loved_Up
    img 21202
    with fade
    ashley "Это оргазм, моя [monica_pub_name]."
    ashley "Ты разве не любишь это?"
    img 21203
    with diss
    m "Я... Я не совсем знаю что это такое и..."
    img 21204
    with fade
    ashley "Ах, иди ко мне, [monica_pub_name], я тебе покажу!"
    music Groove2_85
    img 21205
    with diss
    m "Нет, Эшли! Мне..."
    m "Мне надо идти!"
    return

label gallery_21108:
# Просит посмотреть на ее обалденную попку
    music Loved_Up
    img 21087
    with fadelong
    joe "[monica_pub_name], я хочу увидеть твою попку!"
    m "!!!"
    img 21088
    with diss
    m "Ладно..."
    # Моника поворачивается задом
    img 21089
    with diss
    w
    img 21090
    with diss
    w
    img 21091
    with diss
    w
    music Groove2_85
    img 21092
    with hpunch
    joe "Нет, [monica_pub_name], я хочу увидеть твою попку голой!"
    joe "Покажи ее мне и я сделаю так, чтобы Эшли снова простила тебя!"
    music Hidden_Agenda
    img 21093
    with diss
    m "Джо, может быть, можно как-то без этого?"
    music Groove2_85
    img 21094
    with fade
    joe "Нет, [monica_pub_name], я действительно хочу увидеть твою попку."
    joe "Это мое самое большое желание сейчас!"
    joe "И, пока оно не исполнится, я не смогу ничего сделать с Эшли."
    music Hidden_Agenda
    img 21095
    with diss
    mt "Что же мне делать?"
    mt "Может быть лучше достать $ 500? Но как?!"
    menu:
        "Показать Джо свою голую попу.": #corruption
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21094
            with fade
            m "Нет, Джо!"
            return
    music Groove2_85
    img 21096
    with fade
    m "Джо, но только никаких прикосновений, тебе ясно?!"
    joe "Конечно, [monica_pub_name], я только посмотрю!"
    img 21097
    with diss
    m "И никаких дополнительных условий, ясно?!"
    joe "Да, [monica_pub_name], я обещаю!"
    music Hidden_Agenda
    img 21098
    with fade
    mt "Дьявол!"
    mt "Мне так стыдно делать это..."
    mt "Показывать свой голый зад в какой-то shiny hole посреди трущоб..."
    mt "Это какой-то сон..."
    music Groove2_85
    img 21099
    with diss
    joe "[monica_pub_name], я жду!"
    img 21100
    with diss
    joe "Скорее, показывай свою попку!"
    img 21101
    with diss
    m "!!!"
    # Моника показывает голую попу
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 21102
    with fadelong
    w
    img 21103
    with diss
    w
    img 21104
    with diss
    joe "Ах, какая попка!"
    img 21105
    with diss
    joe "Давно я не видел такой идеальной формы!"
    music Groove2_85
    img 21106
    with fade
    mt "Ты этого недостоин, толстяк! Смотреть на мое восхитительное тело!"

    music Loved_Up2
    sound Jump1
    img 21107 #jump
    with diss
    w
    img 21108
    with diss
    joe "[monica_pub_name], почему ты не показала мне ее сразу, как только пришла?"

    img 21109
    with diss
    joe "Я бы сразу взял тебя официанткой. Без необходимости мыть посуду!"
    img 21110
    with fade
    mt "Это он думает что оказал бы мне честь?! Сразу бы дал работать официанткой в этой дыре?!"
    mt "Мне?! Монике Бакфетт?!"
    sound Jump2
    img 21111
    with vpunch
    joe "[monica_pub_name], можно потрогать?!"
    # Моника одевается
    music Power_Bots_Loop
    img 21112
    with diss
    m "Только попробуй, Джо!"
    m "И я сломаю тебе пальцы!"
    music Groove2_85
    img 21113
    with fade
    joe "Но [monica_pub_name]! Мы ведь только начали!"
    joe "Признайся, ты ведь для этого и пришла сюда, в Shiny Hole."
    joe "Чтобы показывать свое тело за деньги!"
    joe "Просто ты не хочешь торопиться с этим."
    joe "Хочешь сначала освоиться здесь."
    joe "Я тебя понимаю, [monica_pub_name]."
    joe "Все девочки, которые танцуют на сцене, сначала стеснялись."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    music Groove2_85
    img 21114
    with fadelong
    m "Все, Джо!"
    m "Хватит!"
    img 21115
    with diss
    m "Идем к Эшли!"
    return

label gallery_21226:
    music Groove2_85
    img 21206
    with fadelong
    m "Эшли, я пришла."
    m "Только пожалуйста, давай ты не будешь трогать мою киску..."
    m "По крайней мере не в этот раз..."
    music Loved_Up
    img 21207
    with diss
    ashley "Хорошо, [monica_pub_name]."
    ashley "Снимай свой низ, я хочу потереться о твою сладкую попку!"
    menu:
        "Сделать то о чем просит Эшли.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21206
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return
    sound snd_fabric1
    img 21208
    with fadelong
    m "Эшли, и что будет дальше?"
    img 21209
    with diss
    ashley "Не бойся, [monica_pub_name], снимай!"
    sound snd_fabric1
    img 21210
    with fadelong
    m "Ладно..."
    m "А ты мне точно разрешишь снова работать здесь?"
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    # Моника снимает низ
    img 21211
    with fadelong
    # Эшли поднимает юбку
    ashley "Потрись о мою попку своей и я прощу тебя!"
    music Power_Bots_Loop
    img 21212
    with hpunch
    m "ЧТО??!"
    music Loved_Up
    img 21213
    with fadelong
    ashley "Давай, [monica_pub_name]!"
    ashley "Я хочу почувствовать твою сладкую попку!"
    img 21214
    with diss
    ashley "Иначе я тебя не прощу!"
    menu:
        "Сделать то о чем просит Эшли.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21213
            with fade
            m "Нет, Эшли! Я не способна на такое!"
            return

    # Моника трется своей попой о попу Эшли.

    img 21215
    with fade
    ashley "Ну же, [monica_pub_name]!"
    img 21216
    with diss
    ashley "Я не чувствую твою попку! Где она?"
    img 21217
    with diss
    ashley "Не будет твоей попки - не будет прощения!"
    music Groove2_85
    img 21218
    with fadelong
    w
    img 21219
    with fade
    mt "О БОЖЕ! Что я делаю?!"
    music Loved_Up2
    sound hlup10
    img 21220
    with diss
    ashley "Да, [monica_pub_name]!"
    sound hlup25
    img 21221
    with diss
    ashley "Какая у тебя упругая и приятная попка!"
    ashley "Это просто персик!"
    img 21222
    with diss
    mt "!!!"
    sound hlup25
    img 21223
    with diss
    ashley "Ах! Как здорово!"
    sound hlup10
    img 21224
    with diss
    ashley "Ах! Ах! Да!"
    sound hlup10
    img 21225
    with diss
    w
    sound hlup19
    img 21226
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    ashley "Дааааааа!!!" # Эшли кончает
    music stop
    img black_screen
    with diss
    pause 2.0
    music Groove2_85
    img 21227
    with fadelong
    ashley "Ты отлично справилась, [monica_pub_name]."
    ashley "Но, если при клиентах ты будешь такой же шлюхой, какой была сейчас, я тебя уволю."
    img 21228
    mt "Я не шлюха!!!"
    return

label gallery_21145:
# Просит раздеться и забраться на стол
    music Groove2_85
    img 21116
    with fadelong
    joe "[monica_pub_name], ты уже украла столько денег..."
    joe "И Эшли уже начинает что-то подозревать."
    img 21117
    with diss
    joe "Обычно... Знаешь..."
    joe "Больше денег я люблю только шлюх..."
    joe "И Эшли знает об этом и очень ревнует."
    music Power_Bots_Loop
    img 21118
    with vpunch
    mt "Я не шлюха!!!"
    music Groove2_85
    img 21119
    with fade
    joe "Если честно, она так следит за мной, что уже очень давно я не видел другой голой женщины."
    m "И что же ты хочешь на этот раз, Джо?"
    joe "Я хочу чтобы ты разделась, [monica_pub_name]."
    joe "Полностью."
    img 21120
    with diss
    m "Это исключено, Джо!"
    img 21121
    with diss
    joe "Тогда извини, для меня это слишком большой риск."
    joe "Ты можешь идти. Если Эшли догадается, она прибьет меня."
    menu:
        "Уйти.":
            music Power_Bots_Loop
            img 21122
            with fade
            m "Твоя жена тоже может быть голой женщиной, Джо!"
            m "Смотри лучше на нее!"
            return
        "Предложить компромисс.":
            pass

    music stop
    img black_screen
    with diss
    pause 1.0
    music Hidden_Agenda
    img 21123
    with fadelong
    m "Джо..."
    m "Мне действительно надо снова работать здесь."
    m "Может быть мне не надо раздеваться полностью?"
    music Groove2_85
    img 21124
    with fadelong
    joe "Хорошо, [monica_pub_name]."
    joe "Ты можешь раздеться наполовину и встать на этот стол."
    joe "И принять пару сексуальных поз."
    mt "!!!"
    img 21125
    with diss
    joe "Это будет как приватный танец."
    music Hidden_Agenda
    img 21126
    with fadelong
    m "Ладно, Джо..."
    m "Сейчас я сниму верх..."
    music Groove2_85
    img 21127
    with diss
    joe "Нет, [monica_pub_name]!"
    joe "Я хочу чтобы ты сняла низ!"
    music Power_Bots_Loop
    img 21128
    with hpunch
    m "ЧТОООО?!"
    music Groove2_85
    img 21129
    with fade
    joe "[monica_pub_name], твоя грудь прекрасна!"
    joe "Но от твоей попки я просто без ума!"
    joe "Это мое условие!"
    joe "Если ты не согласна, то можешь идти и искать $ 500!"
    img 21130
    with diss
    m "!!!"
    menu:
        "Согласиться.":
            pass
        "Отказаться.":
            music Power_Bots_Loop
            img 21128
            with fade
            m "Нет, Джо!"
            return
    music Hidden_Agenda
    img 21131
    with fade
    mt "Дьявол!"
    mt "До чего ты докатилась, Моника!"
    mt "..."
    mt "Мне не стоит даже в мыслях называть себя Моникой..."
    mt "Вдруг я проговорюсь..."
    mt "Ведь меня здесь знают под именем [monica_pub_name]..."
    img 21132
    with diss
    mt "Черт! Мо... [monica_pub_name]!"
    mt "Закрой глаза и сделай это..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.0
    # Моника снимает низ и залезает на стол
    music Groove2_85
    img 21133
    with fadelong
    mt "Ненавижу этого Джо!"
    mt "На что мне приходится идти ради этой дурацкой работы!"
    img 21134
    with diss
    mt "Как могло дойти до такого?"
    mt "Не могу поверить..."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Molten_Alloy
#    music RocknRoll_loop
    img 21135
    with fadelong
    sound heel1
    # звук каблука
    w
    img 21136
    with diss
    w
    img 21137
    with fade
    sound heel1
    joe "О да, [monica_pub_name]!"
    img 21138
    with diss
    joe "Покажи мне свою попу, Да!"
    img 21139
    with fade
    joe "Давай, меняй позы! Развлеки малыша Джо!"
    img 21140
    with fade
    joe "Вот так! Активнее виляй своей задницей, [monica_pub_name]!"
    img 21141
    with diss
    joe "Вот так! Теперь повернись, ДА!"
    img 21142
    with fade
    joe "Да! Запомни! Клиент должен хорошо рассмотреть твою задницу, [monica_pub_name]!"
    joe "Тогда ты получишь больше чаевых!"
#    music stop
    img 21143
    with diss
    joe "Стоп! Вот так, замри!"
    # достает член
    img 21144
#    with fade
    sound jump1
    # jump
    w
#    music Molten_Alloy
    img 21145
    with diss
    joe "Можешь продолжать!"
    joe "Положи руки на задницу."
    img 21146
    with diss
    joe "Вот так!"
    img 21147
    with fade
    joe "Давай, [monica_pub_name], двигайся поактивнее!"
    joe "Зарабатывай на чай!"
    m "Джо, хватит грязных комментариев!"
    m "Я и так не знаю как согласилась на это!"
    img 21148
    with diss
    joe "Да, [monica_pub_name]! У тебя лучшая задница, которую я видел в Shiny Hole!"
    img 21149
    with diss
    joe "Да, выгнись посильнее, да!"
    joe "Твоя задница ослепительная!"
    img 21150
    with diss
    joe "Ни у одной из наших девочек нет таких идеальных форм!"
    img 21151
    with diss
    joe "Эта задница должна сиять в Shiny Hole!"
    joe "[monica_pub_name], ты станешь звездой!"
    m "Нет, Джо!"
    m "Я никогда не буду танцевать голой на публике!"
    sound snd_masturbation1
    img 21152
    with diss
    joe "Продолжай! Поближе! Я... Я почти все..."
    img 21153
    with fade
    joe "Но как же! Ты должна танцевать!"
    joe "За такую задницу дадут... дадут..."
    joe "Аххх!"
    img 21154
    with diss
    joe "Дадут 20... 50..."
    img 21155
    with diss
    joe "Нет, даже 100 долларов! Сто!"
    img 21156
    with diss
    m "Сколько?! 100 долларов?!"
    m "Ты шутишь, Джо?!"
    img 21157
    with diss
    joe "Может... Ах.... Может не столько..."
    joe "Но 20 долларов за такую задницу дадут точно, [monica_pub_name]!"
    joe "Это хорошие деньги... Аххххх!"

    music Groove2_85
    img 21158
    with fadelong
    m "Все, мне надоело кривляться!"
    joe "Аааааххх!"

    music Power_Bots_Loop
    img 21159
    with hpunch
    m "ЧТО?!"
    m "Ты там что, дрочишь на меня, Джо?!"
    sound snd_masturbation1
    img 21160
    with diss
    joe "Ааааххх! Ааааааааххх!"
    joe "Еще чуть-чуть!"
    music Groove2_85
    img 21161
    with fade
    m "Дьявол!!!"
    m "Все, шоу закончено!"
    m "Иди к Эшли, немедленно!"
    m "Мне нужна эта работа!"
    mt "Извращенец!!!"

    music Power_Bots_Loop
    img 21162
    with fade
    joe "Что?! Кто-то идет?"
    img 21163
    with diss
    joe "Это Эшли! Прячься!"
    mt "О БОЖЕ!"
    music stop
    img black_screen
    with diss
    sound snd_bodyfall
    pause 1.5
    music Groove2_85
    img 21164 #Моника прячется
    with fadelong
    w
    img 21165
    with fade
    ashley "Джо! Вот ты где!"
    ashley "Что ты здесь делаешь, дармоед?!"
    music Power_Bots_Loop
    img 21166
    with diss
    mt "Как я вляпалась!"
    mt "Я здесь, без трусов, прячусь за диваном!"
    mt "От жены хозяина какой-то дыры в трущобах!"
    mt "Моника! Как до такого могло дойти?!"
    mt "Что ты сделала не так, чтобы такое произошло?! ЧТО?!"
    music Groove2_85
    img 21167
    with fade
    ashley "Я что, должна одна целый день обслуживать пьяниц?!"
    ashley "Эта шлюха, [monica_pub_name], больше не работает здесь! Ты забыл?!"

    img 21168
    with diss
    joe "Эшли! Я просто устал, решил отдохнуть..."
    sound snd_kick_fred1
    img 21169
    with fade
    ashley "Никакого отдыха! Быстро работать!"
    img 21170
    with fadelong
    ashley "Зачем я только вышла замуж за такого растяпу!"
    music stop
    img black_screen
    with diss
    pause 1.5
    music Hidden_Agenda
    img 21171
    with fadelong
    m "!!!"
    mt "Хорошо что Эшли не заметила мою одежду. Мне надо незаметно выбраться отсюда..."
    return

label gallery_22676:
    # нажатие на Молли
    # к Монике поворачивается рыжая, смотрит на нее неприветливо
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22664
    with fadelong
    stripper "Это ты новая танцовщица что-ли?.." #осматривает Монику с ног до головы
    img 22665
    with fade
    stripper "М, понятно..."
    img 22666
    with diss
    mt "???"
    img 22667
    with diss
    w
    # и отворачивается
    music Groove2_85
    img 22668
    with fade
    stripper "Увижу тебя рядом со своими вещами - скажу Джо, что ты у меня украла что-нибудь." # не глядя на Монику
    stripper "Советую держаться подальше."
    # Моника неприятно удивлена таким теплым приемом
    music Power_Bots_Loop
    img 22669
    with diss
    sound highheels_short_walk
    mt "..."
    mt "И я рада познакомиться..."
    mt "Как грубо!"
    mt "Всего лишь какая-то стриптизерша из трущоб!"
    mt "Ей, видимо, неизвестно, что такое воспитание и манеры..."
    # Моника зло смотрит на нее и проходит в гримерку
    music Groove2_85
    img 22670
    with fade
    mt "Мне надо надеть сценический костюм. Которого у меня нет..."
    mt "Что же делать?"
    music Hidden_Agenda
    img 22671
    with diss
    mt "Попросить у этой хамки что-нибудь из одежды?"
    # Моника смотрит на рыжую
    sound highheels_short_walk
    img 22672
    with fade
    mt "..."
    # рыжая поворачивается к Монике
    music Groove2_85
    img 22673
    with diss
    stripper "Чего уставилась?!" #разговаривает высокомерно
    stripper "Тебе на сцену через пять минут, чего ты ждешь?"
    stripper "Или ты пойдешь в этом наряде для бомжей?"
    # Моника смотрит на нее с неприязнью
    img 22674
    with fade
    m "Мне не выдали сценический костюм. Я не знаю, в чем выходить на сцену."
    sound snd_woman_laugh
    img 22675
    with diss
    stripper "Сценический костюм?!"
    stripper "Аха-ха!!!"
    img 22676
    with diss
    sound snd_woman_laugh3
    stripper "Может, тебе еще личного ассистента и гримера предоставить?!"
    stripper "Аха-ха-ха!"
    music Power_Bots_Loop
    img 22677
    with fade
    mt "..." #Моника убивает ее взглядом
    # рыжая снова отворачивается к зеркалу
    music Groove2_85
    img 22678
    with diss
    stripper "Ты же не думаешь, что я тебе дам свою одежду?!"
    stripper "Иди танцуй голая!"
    music Power_Bots_Loop
    img 22679
    with diss
    mt "Вот стерва!!!"
    mt "!!!" # отворачивается от рыжей
    music Groove2_85
    img 22680
    with fade
    mt "Что же мне теперь делать?" # растерянно
    mt "Выйти на сцену в этой одежде?"
    mt "Но я не могу идти на сцену в таком виде!"
    mt "Кто-нибудь из этих неудачников узнает меня!"
    # с негодованием
    img 22681
    with diss
    mt "И не хватало еще, чтобы мое лицо узнал кто-то за пределами этих трущоб..."
    mt "..."
    music Groove2_85
    img 22682
    with fade
    sound highheels_short_walk
    mt "Где эта Эшли?!"
    mt "В чем, по ее мнению, я должна танцевать?!"
#    $ log1 = _("Спросить у Эшли костюм для выступления.")
#    $ log1 = _("Эта рыжая стриптизерша слишком многое себе позволяет. Как она смеет так общаться со мной?!")
    return

label gallery_22725:
    music stop
    img black_screen
    with diss
    pause 1.5
    # брюнетка стоит спиной к Монике, переодевается, Моника стоит в дверях
    music Groove2_85
    img 22709
    with fadelong
    mt "Это и есть вторая стриптизерша?"
    img 22710
    with fade
    mt "Надо приготовиться к знакомству со второй хамкой." # с воинственным настроем
    mt "Она, наверное, тоже возомнила себя звездой, как та рыжая стерва..."
    music Pyro_Flow
    img 22711
    with diss
    mt "Звездой в грязном пабе в трущобах!.." # высокомерно
    # Брюнетка поворачивается к Монике, она после выступления в черной маске
    music Groove2_85
    img 22712
    with fade
    stripper "Привет." # без улыбки, спокойно
    stripper "Молли мне говорила, что у нас новенькая. Это ты?"
    # Моника готовилась не к такому знакомству, растерянно
    img 22713
    with diss
    m "..."
    m "Д-да... Привет..."
    img 22714
    with fade
    stripper "Я Клэр. А ты?"
    img 22715
    with diss
    m "Я [monica_pub_name]. А Молли это та рыжая стриптизерша?"
    img 22716
    with fade
    clare "Да." # с ехидной улыбкой
    img 22717
    with diss
    clare "Она тут звезда и очень гордится этим."
    img 22718
    with fade
    clare "С ней лучше дружить и не вставать у нее на пути."
    img 22719
    with diss
    mt "Звезда! Ха-ха! Стриптизерша со звездной болезнью!"
    mt "Похоже, эта Клэр единственная в этой дыре, кто может нормально общаться."
    img 22720
    with fade
    clare "Ты давно в стриптизе, [monica_pub_name]?"
    music Hidden_Agenda
    img 22721
    with diss
    m "Нет. Сегодня будет мое первое выступление..."

    # если были сцены в трущобах с ситизенами
    python:
        flag1 = False
        for progress_name in corruption_places:
            if progress_name.find('monicaWhoringClothPylonDanceCorruption') != -1:
                flag1 = True
    if flag1 == True:
        img 22722
        with diss
        mt "Танцы у пилона на улицах трущоб - не в счет!" # если были сцены в трущобах с ситизенами
    #
    music Groove2_85
    img 22723
    with fade
    clare "Не волнуйся." # дружелюбно
    clare "Я выступаю уже несколько лет и мне очень нравится."
    img 22724
    with diss
    m "Нравится?!" # удивленно
    m "Я думала такое делают только из-за денег..."
    img 22725
    with fade
    clare "Для меня это искусство. Мне нравится делиться своей красотой и видеть восторженные взгляды мужчин."
    img 22726
    with diss
    clare "Это занятие не является источником денег для меня."
    img 22727
    with fade
    mt "Хм... Искусство?.."
    mt "Возможно, если так к этому относиться, то намного проще выходить на сцену."
    mt "Но я не представляю себе такого отношения к этому."
    music Groove2_85
    img 22728
    with diss
    mt "Сами по себе танцы полуголой на публике отвратительны."
    mt "И я не изменю своего отношения к этому никогда!"
    mt "!!!"
    music Groove2_85
    img 22729
    with fade
    clare "[monica_pub_name], почему ты не переодеваешься?"
    clare "В чем ты будешь выступать?"
    clare "Тебе уже пора выходить на сцену."
    # Моника проходит в гримерку и подходит к Клэр. Та стоит возле вешалки.
    img 22730
    with diss
    m "У меня нет одежды для сцены..."
    m "Эшли сказала, что я могу спросить одежду у тебя."
    img 22731
    with fade
    clare "Без проблем. Ты можешь взять вот это." # отворачивается к вешалке, потом кладет одежду для Моники на стул рядом
    # Моника в это время смотрит на ее фигуру
    music Hidden_Agenda
    img 22732
    with diss
    mt "А из этой Клэр получилась бы неплохая модель..."
    mt "Конечно, до Мелани, а тем более до меня, ей далеко, но все же."
    img 22733
    with diss
    mt "И что она забыла в этой дыре, тем более, что она тут не из-за денег..."
    # Клэр поворачивается к Монике
    music Groove2_85
    img 22734
    with fade
    clare "К вещам Молли лучше не приближайся."
    img 22735
    with diss
    clare "Наша звезда очень ревностно к этому относится." # с ехидной улыбкой
    sound snd_fabric1
    img 22736
    with fade
    clare "У меня полно подобных шмоток."
    img 22737
    with diss
    clare "Можешь этот костюм оставить себе."
    img 22738
    with fade
    m "Серьезно?!" # удивленно
    music Groove2_85
    img 22739
    with diss
    m "..." # смотрит на вещи на стуле
    mt "Мне придется надевать на себя ЭТО?"
    mt "Фи! Какой вульгарный костюм!"
    mt "Да еще и после стриптизерши!"
    img 22740
    with diss
    mt "Какой ужас!"
    mt "Я, Моника Бакфетт, буду танцевать полуголая! В дешевом пабе для толпы неудачников!!!"
    mt "Я не могу поверить в это!"
label gallery_22725_1:
    menu:
        "Надеть костюм с жилетом.":
            pass
        "Надеть только трусики.":
            m "Я не выйду на сцену с голой грудью!!!"
            jump gallery_22725_1
    # Клэр отвернулась к вешалке, Моника снимает с себя свою одежду
    music Groove2_85
    img 22741
    with fadelong
    mt "Одно дело трущобы..." # если были сцены в трущобах с ситизенами
    mt "Там, конечно, приходилось показывать себя всяким неудачникам."
    music Power_Bots_Loop
    img 22742
    with diss
    mt "Но тут сцена!"
    mt "И этих неудачников целая толпа!!!"
    mt "Для меня быть на сцене - это все-равно что позировать на фотосессии перед всем миром."
    mt "Это не идет ни в какое сравнение с тихой подворотней, где меня никто не знает."
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Molten_Alloy
    img 22744
    with fadelong
    w
    img 22743
    with fade
    mt "!!!"
    # Моника надевает костюм
    img 22745
    with diss
    mt "..."
    mt "Я очень надеюсь, что в этой маске мое лицо никто не узнает..."
    mt "..."
    music Groove2_85
    img 22746
    with fade
    mt "Так, мне надо собраться и сделать это!"
    mt "Это не я, а [monica_pub_name]."
    mt "Для [monica_pub_name] в этом нет ничего страшного."
    # Клэр поворачивается и смотрит на переодетую Монику
    music Groove2_85
    img 22747
    with diss
    clare "Отлично. Только..."
    # внимательно смотрит на Монику
    clare "Кое-чего тебе не хватает."
    img 22748
    with diss
    clare "Сразу видно, что у тебя нет опыта выступления на сцене."
    mt "???"
    # Клэр берет со столика в руки флакон
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22749
    with fadelong
    clare "Тебе нужно намазать тело этим маслом."
    img 22750
    with diss
    sound Jump1
    w
    sound highheels_short_walk
    img 22751
    with fade
    clare "Тогда ты будешь выглядеть более эффектно на сцене."
    img 22752
    with diss
    clare "[monica_pub_name], давай я тебе помогу?"
    img 22753
    with diss
    w
    menu:
        "Взять у Клэр масло и намазаться самой.":
            pass
        "Позволить Клэр намазать меня маслом.":

            # Клэр намазывает ее маслом
            label gallery_22768:
            img 22754
            with fade
            sound hlup2
            w
            music stop
            music2 Loved_Up
            img 22755
            with diss
            sound skin_lotion11
            w
            img 22756
            with diss
            w
            img 22757
            with fade
            w
            img 22758
            with diss
            sound skin_lotion11
            clare "А у тебя отличная фигура, [monica_pub_name]."
            img 22759
            with fade
            sound skin_lotion11
            mt "Она что, ко мне пытается пристать, как Эшли?!"
            mt "Я не хочу связываться с еще одной лесбиянкой!"
            img 22760
            with diss
            sound skin_lotion11
            clare "Мужчины в зале с ума сойдут, когда тебя увидят."
            img 22761
            with diss
            mt "Я к этому привыкла."
            mt "Мужчины всегда сходили по мне с ума..."
            img 22762
            with fade
            sound skin_lotion11
            w
            img 22763
            with diss
            w
            img 22764
            with fade
            sound skin_lotion11
            clare "Ты сегодня будешь звездой, [monica_pub_name]."
            img 22765
            with diss
            sound skin_lotion11
            mt "Конечно, буду! Мне нет здесь равных!"
            mt "И не только здесь! Мне нет равных нигде!"
            img 22766
            with fade
            sound skin_lotion11
            w
            img 22767
            with diss
            sound skin_lotion11
            w
            img 22768
            with diss
            sound skin_lotion11
            clare "Таким шикарным ногам и такой попе, как у тебя, позавидует любая модель."
            img 22769
            with fade
            sound skin_lotion11
            w
            img 22770
            with diss
            sound skin_lotion11
            clare "Ты просто создана для обложки какого-нибудь модного журнала."
            img 22771
            with fade
            mt "Хм... Хорошо, что она их не читает."
            mt "Боюсь себе даже представить, если меня здесь кто-нибудь узнает."
            ###################################
            if game.extra == True:
                img black_screen
                with diss
                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_1 = Movie(play="video/v_Monica_Claire_Oiling3_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_1
                with fadelong
                wclean

                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_2 = Movie(play="video/v_Monica_Claire_Oiling3_2.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_2
                with fadelong
                wclean

            ###################################
            music2 stop
    # Клэр, осматривая Монику
    music stop
    img black_screen
    with diss
    pause 1.5
    music Molten_Alloy
    img 22772
    with fadelong
    clare "Вот теперь ты выглядишь на миллион баксов!"
    img 22773
    with fade
    mt "Я всегда выгляжу на миллион баксов... И не только выгляжу... Я и стою..."
    img 22774
    with diss
    mt "Миллиарды..."
    mt "Но, думаю Клэр не умеет даже считать до стольки..."

    # выход на движок (персонажи в сцене)
    clare "Давай, тебя там уже ждут!"
    mt "Черт. Черт! Черт!!!"

#    $ log1 = _("Выйти на сцену паба и танцевать.")
#    $ log1 = _("Похоже, Клэр единственная в этой дыре, с кем можно нормально общаться.") # квест лог
    return

label gallery_22841:
    # брюнетка стоит спиной к Монике, переодевается, Моника стоит в дверях
    # Моника задумчиво смотрит на Клэр
    music Groove2_85
    img 22826
    with fadelong
    mt "Эта Клэр могла бы являть свою красоту с обложки журнала..."
    mt "А не танцуя в пабе перед толпой пьяных неудачников!"
    # Клэр в маске поворачивается к Монике, с улыбкой
    img 22827
    with fade
    clare "Привет, [monica_pub_name]. Ну как ты?"
    clare "Эшли говорит, что у тебя уже лучше получается. Она тобой довольна."
    img 22828
    with diss
    m "Хм. Я не удивлена, что Эшли довольна мной."  # проходит в гримерку и начинает раздеваться
    music Power_Bots_Loop
    img 22829
    with diss
    mt "Еще бы она была недовольна! Она теперь может на меня пялиться." # сердито
    mt "Как и ее муж-неудачник!"
    music Groove2_85
    img 22830
    with fade
    clare "Надеюсь, у тебя не было конфликтов с ней?"
    clare "Про Эшли ходят не очень хорошие слухи."
    clare "Так что, лучше не связывайся с ней..."
    img 22831
    with diss
    m "Да? Я не знала..." # удивленно
    m "Спасибо за предупреждение..."
    music Groove2_85
    img 22832
    with diss
    mt "Эта озабоченная Эшли со своим таким же озабоченным мужем уже достали меня!"
    mt "Кто бы предупредил меня заранее, что с ними не стоит связываться?!"
    # Моника переодевается
    call gallery_22841_1()
    if _return == 0:
        $ cloth = "StripOutfit1"
        $ cloth_type = "StripOutfit"
    if _return == 1:
        $ topless = True
        $ cloth = "StripOutfit2"
        $ cloth_type = "StripOutfit"
#    menu:
#        "Надеть костюм с жилетом.":
#            pass
#        "Надеть только трусики.":
#            m "Я не выйду на сцену с голой грудью!!!"
#            return False
    # Клэр берет со столика в руки флакон
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    # корсет
    if topless == False:
        img 22753
        with fade
    # без корсета
    else:
        img 22833
        with fade
    clare "Ты забыла намазаться маслом для тела..."
    clare "[monica_pub_name], давай я тебе помогу?"
    menu:
        "Взять у Клэр масло и намазаться самой.":
            pass
        "Позволить Клэр намазать меня маслом." if game.extra == True or cloth == "StripOutfit1":
            # Клэр намазывает ее маслом
            if topless == True:
                img 22754
                with fade
                sound hlup2
                w
                music stop
                music2 Loved_Up
                img 22834
                with diss
                sound skin_lotion11
                w
                img black_screen
                with diss
                music stop
                stop music
                play music "<from " + str(float(rand(1,5))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling1_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling1_1 = Movie(play="video/v_Monica_Claire_Oiling1_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling1_1
                with fadelong
                wclean

#                music Loved_Up
                img 22835
                with diss
                clare "Какая же у тебя отличная фигура, [monica_pub_name]."

                img 22836
                with fade
                sound skin_lotion11
                mt "Она что, снова ко мне пытается пристать, как Эшли?!"

                music stop
                stop music
                play music "<from " + str(float(rand(1,5))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling1_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling1_2 = Movie(play="video/v_Monica_Claire_Oiling1_2.mkv", fps=30)
                show videov_Monica_Claire_Oiling1_2
                with fadelong
                wclean
#                music Loved_Up
                img 22837
                with diss
                sound skin_lotion11
                w
                img 22838
                with diss
                sound skin_lotion11
                clare "Мужчины в зале с ума сойдут, когда тебя увидят."
                img 22839
                with fade
                mt "Я к этому привыкла."
                mt "Мужчины всегда по мне с ума сходили..."
                img 22840
                with diss
                w

                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling2_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling2_1 = Movie(play="video/v_Monica_Claire_Oiling2_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling2_1
                with fadelong
                wclean

                img 22841
                with diss
                sound skin_lotion11
                w
                img 22842
                with diss
                sound skin_lotion11
                clare "Ты сегодня будешь звездой, [monica_pub_name]."

                img 22843
                with fade
                sound skin_lotion11
                mt "Конечно, буду! Мне нет здесь равных!"
                mt "И не только здесь! Мне нигде нет равных!"

                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_1 = Movie(play="video/v_Monica_Claire_Oiling3_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_1
                with fadelong
                wclean
#                music Loved_Up
                img 22844
                with diss
                sound skin_lotion11
                clare "Таким шикарным ногам и такой попе, как у тебя, позавидует любая модель."
                img 22845
                with diss
                sound skin_lotion11
                clare "Ты просто создана для обложки какого-нибудь модного журнала."
                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_2 = Movie(play="video/v_Monica_Claire_Oiling3_2.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_2
                with fadelong
                wclean
                music2 stop
                music Groove2_85
                img 22846
                with fade
                mt "Хм... Хорошо, что она их не читает."
                mt "Боюсь себе даже представить, если меня здесь кто-нибудь узнает."
                ###################################





                ###################################

            else:
                img 22754
                with fade
                sound hlup2
                w
                music Loved_Up
                img 22755
                with diss
                sound skin_lotion11
                w
                img 22756
                with diss
                w
                img 22757
                with fade
                w
                img 22758
                with diss
                sound skin_lotion11
                clare "Какая же у тебя отличная фигура, [monica_pub_name]."
                img 22759
                with fade
                sound skin_lotion11
                mt "Она что, снова ко мне пытается пристать, как Эшли?!"
                img 22760
                with diss
                sound skin_lotion11
                clare "Мужчины в зале с ума сойдут, когда тебя увидят."
                img 22761
                with diss
                mt "Я к этому привыкла."
                mt "Мужчины всегда сходили по мне с ума..."
                img 22762
                with fade
                sound skin_lotion11
                w
                img 22763
                with diss
                w
                img 22764
                with fade
                sound skin_lotion11
                clare "Ты сегодня будешь звездой, [monica_pub_name]."
                img 22765
                with diss
                sound skin_lotion11
                mt "Конечно, буду! Мне нет здесь равных!"
                mt "И не только здесь! Мне нет равных нигде!"
                img 22766
                with fade
                sound skin_lotion11
                w

                img black_screen
                with diss
                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_1.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_1 = Movie(play="video/v_Monica_Claire_Oiling3_1.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_1
                with fadelong
                wclean

                music Loved_Up
                img 22767
                with diss
                sound skin_lotion11
                w
                img 22768
                with diss
                sound skin_lotion11
                clare "Таким шикарным ногам и такой попе, как у тебя, позавидует любая модель."

                music stop
                stop music
                play music "<from " + str(float(rand(1,7))*1.2) + " loop 0.0>Sounds/v_Monica_Claire_Oiling3_2.ogg" # 1,3 - это рандом от 1 до 3-х. 1.66666 - длина видео в секундах
                scene black
                image videov_Monica_Claire_Oiling3_2 = Movie(play="video/v_Monica_Claire_Oiling3_2.mkv", fps=30)
                show videov_Monica_Claire_Oiling3_2
                with fadelong
                wclean
                music Loved_Up
                img 22769
                with fade
                sound skin_lotion11
                w
                img 22770
                with diss
                sound skin_lotion11
                clare "Ты просто создана для обложки какого-нибудь модного журнала."
                img 22771
                with fade
                mt "Хм... Хорошо, что она их не читает."
                mt "Боюсь себе даже представить, если меня здесь кто-нибудь узнает."
                ###################################



                ###################################

#            return 1
    # Клэр, осматривая Монику
    # Переход на движок
    return

label gallery_22841_1:
    menu:
        "Костюм для сцены (с жилетом)":
            return
        "Костюм для сцены (без жилета)":
            if pubDanceCount < 4 or len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
                m "Я не выйду на сцену с голой грудью!!!"
                help "У Моники мало опыта работы танцовщицей."
                if len(list(set(stage_Monica_shoots_array))) < monicaPosesOpenedToStage2:
                    help "Окрыты не все движения. Требуется [monicaPosesOpenedToStage2]."
                if pubDanceCount < monicaDanceAmountToTopless:
                    help "Требуется выйти на сцену [monicaDanceAmountToTopless] раз."
                return
            return
    return

label gallery_22777:
    # Джо стоит перед выходом на сцену
    music2 pub_noise1_low
    music Hidden_Agenda
    img 22775
    with fadelong
    joe "[monica_pub_name], а ты горячая штучка!"  # смотрит похотливо
    music Power_Bots_Loop
    img 22776
    with fade
    m "..." # раздраженно
    music Hidden_Agenda
    img 22777
    with diss
    joe "Только, жилет этот тут лишний."
    joe "Если хочешь чаевых, то сними это с себя!"
    joe "Местные девочки танцуют без одежды."
    # если видел грудь Моники
    if pubMonicaWaitressTipsPunishmentJoeStage >= 2:
        img 22778
        with fade
        joe "А твоих малышек наши посетители очень оценят, я их уже оценил!"
    #
    # если видел попу Моники
    if pubMonicaWaitressTipsPunishmentJoeStage >= 3:
        img 22779
        with diss
        joe "И твоя попа также бесподобна. Тебе не стоит прятать ее от наших ребят!"
    #
    music Groove2_85
    img 22780
    with fade
    m "???" # удивленно и зло
    # движок
    menu:
        "Выйти на сцену в жилете.":
            pass
        "Снять жилет.":
            m "Я не выйду на сцену с голой грудью!!!"
            return
    return

label gallery_22786:
    # Эшли требовательно
    music2 stop
    music stop
    img black_screen
    with diss
    pause 1.5
    music2 pub_noise1_low
    music Groove2_85
    img 22781
    with fadelong
    ashley "Ну что, [monica_pub_name], сколько ты заработала сегодня?"
    img 22782
    with fade
    m "???"
    img 22783
    with diss
    m "Что значит 'заработала'?! Я танцевала здесь!!!"
    m "Разве этого не достаточно?!" # возмущенно
    img 22784
    with fade
    ashley "Здесь надо не просто танцевать, а зарабывать деньги!"
    ashley "Если бы ты показала публике свою грудь или голую попку..."
    ashley "То тебе определенно дали бы несколько долларов."
    music Power_Bots_Loop
    img 22785
    with hpunch
    m "Я не собираюсь этого делать!!!"
    img 22786
    with diss
    ashley "А придется! Как ты собираешься возвращать мне долг?"
    ashley "Ты думала, что будешь просто танцевать?"
    ashley "Ты мне будешь отдавать свои чаевые, а я буду постепенно списывать твой долг."
    img 22787
    with diss
    m "!!!" # Моника офигевает
    music Groove2_85
    img 22788
    with fade
    ashley "Надеюсь, в следующий раз ты заработаешь хоть что-то на чай..."
    ashley "Для этого достаточно будет снять жилетку на сцене."
    img 22789
    with diss
    m "..."
    return

label gallery_22803:
    # Джо стоит перед выходом на сцену
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music2 pub_noise1_low
    music Groove2_85
    img 22797
    with fadelong
    joe "[monica_pub_name], это костюм Клэр?"  # смотрит похотливо
    img 22798
    with fade
    m "Да." # раздраженно
    music Hidden_Agenda
    img 22799
    with diss
    joe "Я смотрю, ты с ней подружилась..."  # подмигивает
    music Groove2_85
    img 22800
    with fade
    m "Тебе что с этого?" # раздраженно
    img 22801
    with diss
    joe "Выяснишь для меня, как к ней подкатить?"
    m "???" # смотрит на него как на идиота
    music Hidden_Agenda
    img 22802
    with fade
    joe "Она тут ни с кем не общается..."
    joe "И никого к себе не подпускает..."
    joe "На приваты не соглашается, хотя предложений много..."
    joe "А она тут работает уже не один год. И я все это время не знаю, как подойти к ней..."
    # выходит Клэр с нагайкой, включает строгую училку
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.0
    music Groove2_85
    img 22803
    with fadelong
    clare "Что здесь происходит?!" # смотрит на Джо строго
    sound Jump2
    img 22804
    with hpunch
    clare "Тебе чего надо от [monica_pub_name]?!" # ткнув его в грудь нагайкой
    joe "Я... Мне... Я просто..." # растерянно мямлит и смотрит на нагайку
    music Power_Bots_Loop
    sound Jump2
    img 22805
    with vpunch
    clare "Я просто пойду сейчас к твоей жене!" #с угрозой
    clare "И расскажу, чем ТЫ тут занимаешься!"
    music Groove2_85
    img 22806
    with fade
    joe "Ч-ч-чем???"
    music Power_Bots_Loop
    img 22807
    with diss
    clare "Пристаешь к [monica_pub_name]!!!"
    music Groove2_85
    img 22808
    with diss
    joe "Я... Я не пристаю!"
    joe "Не надо ничего говорить Эшли!"
    music Power_Bots_Loop
    img 22809
    with diss
    clare "Тогда пошел отсюда! Быстро!!!" # ткнув его снова нагайкой
    joe "!!!"
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.0
    music Groove2_85
    img 22810
    with fade
    # Джо растерян, уходит
    clare "Вот кобель!"
    clare "!!!"
    # смотрит на Монику, улыбается
    img 22811
    with diss
    clare "Если снова будет приставать, скажи мне. Он меня боится."
    img 22812
    with fade
    m "Спасибо, Клэр."
    # Клэр уходит
    mt "Когда я выберусь из этого дна, заведу себе такой же хлыст от извращенцев!"
    music stop
    img black_screen
    with diss
    pause 1.5
    return

label gallery_22819:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22814
    with fadelong
    sound highheels_short_walk
    mt "Я не хочу разговаривать с этой хамкой!"
    # Моника проходит в гримерку и молча переодевается в одежду Клэр
    # рыжая смотрит на Монику высокомерно
    img 22815
    with diss
    molly "Тебя здороваться не учили?.."
    # рыжая отворачивается
    img 22816
    with diss
    molly "Понабирают на работу шлюх из подворотни..."
    # Моника поворачивается и зло смотрит на нее\
    music Power_Bots_Loop
    img 22817
    with diss
    mt "!!!"
    menu:
        "Клэр предупреждала, что лучше не конфликтовать с ней":
            # отворачивается от Молли, послав ей убийственный взгляд
            pass
        "Да, Клэр предупреждала, но я же не могу просто проигнорировать такую наглость":
            music Power_Bots_Loop
            img 22818
            with fade
            m "Ты это сейчас про себя, да?" # со злостью
            m "Я такого же мнения после нашего с тобой так сказать 'знакомства'!"
            img 22819
            with diss
            mt "Этой хамке самое место в подворотне со шлюхами! Как она здесь оказалась?"
            # рыжая поворачивается к Монике и смотрит вопросительно и высокомерно
            music Groove2_85
            img 22820
            with fade
            molly "Мне послышалось или ты что-то сейчас мне сказала?"
            # Моника ей также высокомерно в ответ
            music Groove2_85
            img 22821
            with diss
            menu:
                "Взять стул Клэр и ударить им рыжую сучку!":
                    music Groove2_85
                    img 22822
                    with fade
                    mt "Нет, я не могу пока этого позволить себе."
                    mt "Эта сучка Эшли выгонит меня отсюда и я не смогу зарабатывать деньги..."
                    mt "Которые мне так нужны..."
                    mt "..."
                    mt "Я сделаю это позже..."
                "Мне не о чем разговаривать с такой как ты!":
                    pass
            music Groove2_85
            img 22823
            with fade
            m "Мне не о чем разговаривать с такой как ты!"
            m "И, тем более, о чем-то спорить!"
            img 22824
            with diss
            sound highheels_short_walk
            m "Я не собираюсь опускаться до твоего уровня!!!"
            m "!!!"
            # рыжая офигевает от такого, ничего не отвечает и зло смотрит на Монику
            music Power_Bots_Loop
            img 22825
            with fade
            molly "!!!"
    # Моника отворачивается от нее
    music Groove2_85
    img 22825
    with diss
    mt "Не могу выносить ее присутствия!"
    mt "Надо скорее одеться и идти на сцену."
#    menu:
#        "Надеть костюм с жилетом.":
#            pass
#        "Надеть только трусики.":
#            mt "Я не выйду на сцену с голой грудью!!!"
#            return False
#    $ log1 = _("Выйти на сцену паба и танцевать.")
    return

label gallery_22874:
    # Джо смотрит на Монику похотливо
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    sound2 man_steps
    pause 1.5
    music2 pub_noise1_low
    music Groove2_85
    img 22870
    with fadelong
    w
    img 22871
    with fade
    joe "[monica_pub_name], ты сегодня заработала хорошие чаевые..."  # с улыбкой
    img 22872
    with diss
    m "Да. А тебе какое дело до этого, Джо?" # раздраженно
    music Hidden_Agenda
    img 22873
    with fade
    joe "[monica_pub_name], ты хочешь заработать настоящие деньги?"
    joe "А не эти жалкие несколько баксов?"
    img 22874
    with diss
    m "На что ты намекаешь, Джо?" # с подозрением
    img 22875
    with fade
    joe "Есть один клиент..."
    joe "Он хочет, чтобы ты станцевала для него..."
    joe "Только для него."  # подмигивает
    music Power_Bots_Loop
    img 22876
    with hpunch
    m "Приватный танец?!" # зло
    m "Ты за кого меня принимаешь?!"
    music Groove2_85
    img 22877
    with diss
    mt "Как он смеет предлагать мне подобное?!"
    mt "Чтобы Моника Бакфетт танцевала приват!!!"
    mt "И для кого?! Для какого-нибудь неудачника?!"
    mt "Для которого лучшее развлечение в жизни - придти в эту дыру и выпить пива?!"
    mt "!!!"
    mt "Ни за какие деньги Я не стану этого делать!!!"
    img 22878
    with fade
    m "Я не собираюсь зарабатывать ТАКИМ способом, Джо!" # сердится
    m "И не хочу слышать больше подобных предложений!!!"
    m "!!!"
    music2 stop
    music Hidden_Agenda
    img 22879
    with diss
    joe "[monica_pub_name], может ты все-таки подумаешь хорошо?"
    joe "Это и правда неплохие деньги..."
    music Groove2_85
    img 22880
    with fade
    m "???" # смотрит на него как на идиота
    m "Нет!!!"
    music Hidden_Agenda
    img 22881
    with diss
    joe "Хорошо, [monica_pub_name]."
    joe "Но если подобные предложения от клиентов еще будут, то я тебе скажу об этом."
    joe "Вдруг ты передумаешь..." # Джо подмигивает и уходит
    m "..."
    music stop
    img black_screen
    with diss
    pause 1.5
    return

############ Slums 1############

label gallery_6127:
    #render
    #Моника пришла к кебабу говорить о еде
    #первый раз
    $ store_music()
    music DarxieLand
    img 6084
    shawarma "Мадаме! Снова ВЫ!"
    "Осмелюсь высказать сожаление, Мадаме!"
    img 6085
    m "О чем?!" #раздраженно
    shawarma "О Вашем платье, Мадаме!"
    "Вам оно шло гораздо больше, Мадаме!"
    "Все женщины, в погоне за красотой, в конце концов теряют её!"
    music Hidden_Agenda
    img 6086
    with fade
    m "Ты считаешь что я некрасивая?"
    img 6087
    music DarxieLand
    shawarma "О нет, Мадаме! Вы прекрасны как утренний цветок!"
    img 6088
    m "Какой еще утренний цветок?"
    m "Слушай... У меня к тебе вопрос..."
    img 6089
    shawarma "Да, Мадаме! Я слушаю Вас!"
    music Hidden_Agenda
    img 6090
    with fade
    m "Так я тебе нравлюсь или нет..." #ехидно смотрит
    img 6091
    w
    img 6092
    music DarxieLand
    shawarma "Да, Мадаме! Как утренний цветок!"
    img 6093
    mt "Что за утренний цветок!? Этот идиот несет какую-то чушь..."
    music Hidden_Agenda
    img 6094
    with fade
    m "Ты говорил что у тебя вкусный кебаб?"
    img 6095
    mt "Как же я хочу есть!"
    img 6096
    with fade
    shawarma "Да, Мадаме! Самый вкусный кебаб в округе, Мадаме!"
    img 6097
    m "И ты дашь его попробовать такой красивой девушке как Я?"
    img 6098
    shawarma "Мадаме, я не могу дать Вам мой самый вкусный кебаб, Мадаме!"
    img 6099
    m "Почему это?"
    img 6100
    shawarma "Ваша красота слишком велика, чтобы покупать её, Мадаме!"
    music Stealth_Groover
    img 6101
    m "Причем здесь покупать? Я ничего не собираюсь продавать тебе!"
    #до этого добавить kebab advertising!
    img 6102
    shawarma "Но как же, Мадаме! Вы предложили французский поцелуй за мой вкусный кебаб, Мадаме!"
    music Pyro_Flow
    img 6103
    m "ЧТО Я ПРЕДЛОЖИЛА?!"
    img 6104
    "ЕЩЕ ЧЕГО!!!"
    "Я говорю тебе дай свой кебаб сюда, быстро!"
    img 6105
    shawarma "Хорошо, Мадаме! Только для Вас самый вкусный кебаб за $ 1! Мадаме!"
    img 6118
    w
    img 6119
    with fade
    w
    music DarxieLand
#    if money > 0:
#        call monica_shawarma_dialogue2a() from _call_monica_shawarma_dialogue2a_1
#        return
    #если есть доллар, то уходим на покупку
#    music Stealth_Groover
    img 6106
    mt "Черт! У меня нет этого гребаного доллара!!!"
    img 6107
    m "Можешь дать мне его просто так?"
    img 6108
    shawarma "Нет, Мадаме! Только за $ 1, Мадаме!"
#    music Pyro_Flow
    img 6109
    m "У меня нет этого гребаного доллара! Есть еще какие-то варианты?"
    img 6110
    music DarxieLand
    shawarma "Конечно есть, Мадаме!"
    "Если такой красивый женщин, как Вы, {c}расскажет всем вокруг про мой самый вкусный кебаб{/c}, то кебаб сам будет Вас искать!"
    img 6111
    "Он уже ждет, он хочет чтобы Вы всем рассказали про него!"
    img 6112
    m "Итак, ты хочешь чтобы я кому-то рассказала про тебя?"
    img 6113
    shawarma "Да, Мадаме! Вы разносить всем красивый флаер с рекламой самого вкусного кебаба!"
    "Если Вы разнести все флаер, то вкусный кебаб ждать Вас!"
    music Stealth_Groover
    img 6114
    m "Хорошо, если ты дашь мне сейчас свой кебаб, то {c}я разнесу твои флаеры{/c}..."
    img 6115
    with fade
    w
    music DarxieLand
    img 6116
    shawarma "Нет, Мадаме! Сначала флаер, потом вкусный кебаб!"
    img 6117
    mt "Вот урод!"
    "Неужели мне правда стоит разносить эти флаеры за какой-то кебаб?"
    menu:
        "Согласиться разносить флаеры.":
            music Hidden_Agenda
            img 6120
            mt "О БОЖЕ! Что мне только ни приходится делать чтобы хоть что-то поесть!"
            img 6121
            "Надеюсь я скоро решу это небольшое недоразумение и забуду это как кошмарный сон!"
            img 6122
            with fade
            m "Давай сюда свои флаеры!"
            img 6123
            music DarxieLand
            shawarma "Да, Мадаме! Вам надо надеть это!"
            music stop
            img 6124
            w
            #звук одежды
            sound snd_cardboard1
            img 6125
            with fade
            w
            img 6126
            w
            music Power_Bots_Loop
            img 6127
            m "ЧТО..."
            "ЧТО ЭТО ЗА ХРЕНЬ!?!?!?"
            img 6128
            "ЧТО ТЫ НАЦЕПИЛ НА МЕНЯ?!"
            img 6129
            w
            img 6130
            w
            shawarma "Это условие работа!"
            "Нет реклама, нет вкусный кебаб!"
            img 6131
            w
            img 6132
            w
            music Hidden_Agenda
            img 6133
            m "О БОЖЕ!"
            "Мне придется в этом ходить?!?!"
            img 6134
            mt "Он заплатит за это!"
            "..."
            "Но по крайней мере меня точно никто не узнает в этом!"
            "Я быстро раздам эти долбаные флаеры и забуду этот кошмар!"

        "Отказаться.":
            music Power_Bots_Loop
            img 6135
            m "Я не собираюсь ничего разносить! Давай кебаб сюда!"
            img 6136
            shawarma "Нет, Мадаме! Нет флаер, нет кебаб!"
            w
            img 6138
            with fade
            w
    return

label gallery_7110:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_9_1
    if citizen9_offered_last_day == day and monicaGotJoint != True:
        imgr Dial_Citizen_9_4
        citizen9 "Хэй! Мы уже разговаривали."
        return
    citizen9 "А? Да?"
    "Что?"
    menu:
        "Потрогай мою сиську." if monicaGotJoint == True:
            imgl Dial_Monica_Sandwich_0
            m "Потрогай мою сиську."
            imgr Dial_Citizen_9_3
            citizen9 "Как скажешь, дамочка."
            #подходит к монике сзади и хватает за грудь. так как на ней табличка, ей сложно сопротивляться.
            $ imagesArr = ["7110", "7111", "7112", "7113", "7114"]
            $ images = random.sample(set(imagesArr), 2)
            sound Jump2
            img images[0]
            w
            img images[1]
            w
            img scene_Hostel_Street
            imgl Dial_Monica_Sandwich_0
            imgr Dial_Citizen_9_3
            m "Идиот! Что ты делаешь?"
            imgr Dial_Citizen_9_3
            citizen9 "То, что ты мне сказала! Хе-хе-хе. Отличная грудь кстати!"
            m "Идиот! Я от Джека!"
            imgr Dial_Citizen_9_2
            citizen9 "Ууу, дамочка, с этого и надо было начинать. Что у тебя?"
            #citizen9 отходит
            menu:
                "Дать косяк.":
                    imgl Dial_Monica_Sandwich_0
                    m "Вот."
                    imgr Dial_Citizen_9_3
                    citizen9 "Отлично. Узнаю старину Джека. Отличная вещь. Хочешь?"
                    imgl Dial_Monica_Sandwich_1
                    m "Нет, спасибо. Вот, возьми еще флаер."
                    imgr Dial_Citizen_9_2
                    citizen9 "Флаер? Ладно. Как насчет потрогать сиську еще раз?"
                    imgl Dial_Monica_Sandwich_2
                    m "Нет!"
                    mt "Идиот."
                    return
                "Ничего":
                    imgl Dial_Monica_Sandwich_0
                    m "Ничего, я, кажется, ошиблась..."
                    return

        "Возьмите, пожалуйста, этот флаер..." if citizen9_offered_last_day != day:
            imgl Dial_Monica_Sandwich_1
            #если нет косяка
            m "Возьмите, пожалуйста, этот флаер..."
            if rand(0, citizen9_refuse_probability) > 0:
                imgr Dial_Citizen_9_2
                citizen9 "А? Что?"
                "Флаер?"
                imgr Dial_Citizen_9_3
                "Хорошо..."
                citizen9 "Ооо, дамочка, а пойдемте к пилону! я потрогаю твою сиську еще разок!"
                menu:
                    "Да ни за что на свете!":
                        #img Моника злится
                        m "Мне ничего от тебя не нужно!"
                    "Ну точно не сейчас.":
                        m "Не в этот раз."
                        citizen9 "Ооо, ты не отказываешься... Хорошо. Тогда приходи, как будешь не так занята. Кстати, у Найджела есть деньги!"
            else:
                imgr Dial_Citizen_9_4
                citizen9 "Отстань, дамочка! Я пытаюсь кое-что вспомнить..."
                citizen9 "Вы меня отвлекаете!"
        "Уйти.":
            pass
#        "Уйти.":
#            pass
    return

label gallery_7118:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_7_1
    if citizen7_offered_last_day == day:
        imgr Dial_Citizen_7_4
        citizen7 "Я пытаюсь сосредоточиться на искусстве!"
        "Не отвлекайте меня!"
        return
    citizen7 "Да? Что Вы хотели?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            m "Возьмите, пожалуйста, этот флаер..."
            # Реально ли тут сделать картинку или что то в этом духе, как художник достает кисть и измеряет монику?
            img 7118
            w
            img 7117
            citizen7 "Прекрасно, очень хорошо! А теперь повернитесь!"
            img 7116
            w
            img 7117
            mt "Что вообще происходит?"
            # тут эффект, что художник подходит к монике сзади и точно также ее мереет, либо она настолько становится паражена от этих манипуляций, что поворачивается. Что проще реализовать ?
            img scene_Hostel_Street3
            imgl Dial_Monica_Sandwich_1
            imgr Dial_Citizen_7_1
            m "Эй, мистер, Вы возьмете флаер?"
#                    // художник делает еще несколько кругов\замеров
            # здесь будет вставка новых событий
            if rand(0, citizen7_refuse_probability) > 0:
                imgr Dial_Citizen_7_2
                imgr Dial_Citizen_7_2
                citizen7 "Я закончил. Флаер? Да давайте уже..."
                imgr Dial_Citizen_7_3
                citizen7 "Я бы хотел провести блее детальные замеры. В менее людном месте, это необходимо. Давайте отойдем чуть подальше."
                menu:
                    "Я никуда с тобой не пойду":
                        #img Моника злится
                        m "Мне ничего от тебя не нужно!"
                    "Куда именно?":
                        m "Куда именно?"
                        citizen7 "Здесь в подворотне есть прекрасное место для вдохновения. Мне нужно оценить ваши формы."
                        mt "Кажется я знаю о каком месте он говорит..."
                        m "Не дождешься!"
                        citizen7 "И напрасно. Вы же понимаете, что работа модели всегда оплачивается?"
                        if fallingPathStarted == True:
                            mt "В любом случае об этом лучше говорить без этой дурацкой рекламы кебаба..."

            else:
                imgr Dial_Citizen_7_4
                citizen7 "Я пытаюсь сосредоточиться на искусстве!"
                "Не отвлекайте меня!"
#        "Уйти.":
#            pass
    return

label gallery_8493:
    imgl Dial_Monica_Sandwich_0
#    menu:
#        "Мистер... Можно к Вам обратиться?":
    m "Мистер... Можно к Вам обратиться?"
    #img Моника спрашивает
    imgr Dial_Citizen_12_1
    if citizen12_offered_last_day == day:
        imgr Dial_Citizen_12_4
        citizen12 "Я тороплюсь! Мне некогда!"
        return
    citizen12 "Да, Крошка? Что ты хочешь от меня?"
    menu:
        "Возьмите, пожалуйста, этот флаер...":
            imgl Dial_Monica_Sandwich_1
            m "Возьмите, пожалуйста, этот флаер..."
            if questOffendMonicaFlyersCitizen12Started == True:
                citizen12 "Конечно, крошка, а ты не хочешь ничего у меня взять?"
                m "Вы это о чем?"
                imgr Dial_Citizen_12_4
                citizen12 "Сейчас, я покажу..."
                music Power_Bots_Loop
                sound snd_bodyfall
                img 8484
                with fadelong
                #звук падения тела
                w
                sound snd_woman_pain
                img 8485
                with hpunch
                m "Аххх!!!"
                # img хватает монику за плечи и сажает на колени
                img 8486
                with fade
                m "Что ты себе позволяешь?! Что ты делаешь?"

                sound snd_zip
                img 8487
                with fade
                #звук ширинки
                citizen12 "Расслабься, уверен, тебе это не впервой."
                # img ситизен расстегивает ширинку
                img 8488
                mt "Черт, из за дурацкой рекламы мне сложно двигаться..."
                img 8489
                m "Помогите! Кто-нибудь! Полиция!"
                img 8490
                with fade
                mt "Черт! Какая еще полиция?! Мне нельзя полицию!"
                img 8491
                with fade
                citizen12 "Крошка, сейчас сделаешь мне минет и получишь свои 5 долларов."
                img 8492
                w
                img 8493
                with fade
                m "Что ты сказал?! ПОМОГИТЕ, КТО НИБУДЬ!"
                # img появлятеся citizen6
                music Groove2_85
                img 8494
                with fadelong
                citizen6 "Что здесь происходит?"
                img 8495
                citizen12 "Эй, мужик, иди своей дорогой, или присоединяйся!"
                img 8496
                m "Пожалуйста, помогите мне! Я не шлюха!"
                img 8497
                citizen6 "А что мне за это будет?"
                img 8498
                m "Все, что захочешь, только помоги мне!"
                # citizen6 бьет citizen12 и тд тп
                img 8499
                with fadelong
                #звук удара
                sound snd_punch_face
                w
                #звук падения тела
                sound snd_bodyfall
                img 8500
                w
                img 8501
                w
                img 8502
                with fade
                w
                img 8503
                w
                img 8504
                w
                img 8505
                with fade
                m "Спасибо, спасибо большое!"
                citizen6 "Ага, подойдешь ко мне, обсудим мою награду."
                m "Что?"
                citizen6 "Ну ты же сама обещала, что у меня будет все, что я захочу..."
                return
            if rand(0, citizen12_refuse_probability) > 0:
                imgr Dial_Citizen_12_2
                citizen12 "Ээээ... взять что?"
                m "Возьмите, пожалуйста, этот флаер..."
                citizen12 "Ок..."
                imgr Dial_Citizen_12_3
                citizen12 "И все? А как же развлечься?"
                menu:
                    "Я никого не собираюсь развлекать!":
                        imgl Dial_Monica_Sandwich_2
                        #img Моника злится
                        m "Я никого не собираюсь развлекать!"
                    "Чем тебя развлечь?":
                        m "Ты это о чем?"
                        citizen12 "Да все просто, отойдем в сторонку, покажешь сиськи, может что еще."
                        m "Не сегодня, засранец!"
                        citizen12 "Да ладно тебе! Подумай об этом. Это быстрый способ заработать."
            else:
                imgr Dial_Citizen_12_4
                citizen12 "Мне неинтересны никакие флаеры!"
#        "Уйти.":
#            pass
    return

label gallery_10597:
    # Ситизен предлагает Монике показать грудь за $ 50
    music Groove2_85
    img 10571
    with fade
    citizen4 "Хотя... Ты красивая девочка. Хочу оценить их без одежды."
    "Я недавно провернул одно дельце и у меня есть лишние 50$. Что скажешь?"
    menu:
        "Согласиться..." if corruption >= monicaWhoringClothNakedBoobsCorruptionRequired and fallingPathServedCustomersTotal >= 20:
            pass
        "Согласиться... (low corruption, required: [monicaWhoringClothNakedBoobsCorruptionRequired], 20 customers served) (disabled)" if corruption < monicaWhoringClothNakedBoobsCorruptionRequired or fallingPathServedCustomersTotal < 20:
            pass
#        if fallingPathServedCustomersTotal >= 20 and citizen4BoobsShowedFirstTime == False:
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10572
            with fade
            m "Да за кого ты меня принимаешь?!"
            m "Этого не будет никогда!"
            img 10571
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return False
#                call pylonController(1, 1) #моника просто стоит у пилона
    img 10573
    with fade
    mt "50$ были бы не лишними... Хорошо, что здесь никого нет."
    img 10574
    with diss
    m "50$ ?"
    img 10575
    citizen4 "Все верно, девочка. Покажешь своих подружек и они твои."
    img 10576
    with fade
    mt "Черт! Моника, ты уверена что станешь делать это???"
    mt "Станешь показывать свою грудь какому-то нищему за жалкие 50$?"
    img 10577
    with diss
    mt "Но, с другой стороны, это же не я показываю грудь, а какая-то шлюха в трущобах."
    mt "Ведь никто даже представить себе не может что это делает Моника Бакфетт."
    mt "Это как какая-то виртуальная игра, в которой все не по настоящему..."
    mt "Но вот 50$, которые я получу, вполне реальны!"
#                call pylonController(3, 1)
    img 10578
    with fade
    m "Ладно, только не трогать!"
    img 10579
    citizen4 "Об этом не волнуйся, детка. Я не хочу проблем с твоим сутенером."
    music Power_Bots_Looop
    img 10580
    mt "Да за кого он меня принимает?"
#                call pylonController(3, 2)
    img 10581
    m "Хорошо, давай деньги."
    music Groove2_85
    img 10582
    with diss
    citizen4 "Только после того, как покажешь."
    citizen4 "Деньги вперед я могу дать только твоему сутенеру!"
    citizen4 "Извини, но таким девочкам как ты я на слово не верю..."
#                citizen4 "А ты не глупая девочка. Вот, держи."
#                $ add_money(50)
#                with fade
#                call showRandomImages(nakedboobsImages, 4)
#                call pylonController(3, 5) #моника показывет голые сиськи
    img 10583
    m "!!!"
    m "Отвернись!"
    img 10584
    with fade
    w
    music Loved_Up
    img 10585
    with fade
    w
    #показывает
    img 10586
    with fade
    w
    img 10587
    with Dissolve(0.3)
    $ renpy.pause(1.5)
    music stop
    sound plastinka2
    img 10586
    with Dissolve(0.3)
    music Groove2_85
    citizen4 "Эй! Куда ты их спрятала?!"
    img 10588
    with diss
    m "Я показала тебе свою грудь! Давай деньги!"
    citizen4 "Ты что, пошутила?! Я ничего не успел рассмотреть!"
    m "Ты увидел достаточно! Давай деньги, скорее!"
    img 10589
    with fade
    citizen4 "Я не дам тебе ничего, пока ты не покажешь мне грудь нормально!"
    citizen4 "Я хочу рассмотреть ее как следует! Иначе никаких денег!"
    img 10590
    with fadelong
    m "!!!"
    menu:
        "Согласиться...":
            pass
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10591
            with fade
            m "Да за кого ты меня принимаешь?!"
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return
    #Моника снова показывает грудь быстро
    music Loved_Up
    img 10592
    with Dissolve(0.3)
    $ renpy.pause(0.5)
    music stop
    sound plastinka2
    img 10590
    with Dissolve(0.3)
    music Groove2_85
    citizen4 "Эй! Хватит кривляться! Покажи грудь нормально!"

    img 10593
    citizen4 "Покажи грудь, а я досчитаю до пяти!"
    citizen4 "Если ты уберешь грудь раньше, то не получишь никаких денег!"
    img 10594
    with fade
    m "..."
    citizen4 "..."
    m "..."
    citizen4 "50$!"
    menu:
        "Согласиться...":
            pass
        "Отказаться.":
#                        call pylonController(4, 1)
            music Pyro_Flow
            img 10572
            with fade
            m "Да за кого ты меня принимаешь?!"
            citizen4 "Тогда мои 50$ достанутся более сговорчивой девочке."
            return

    #Моника показывает грудь, а citizen ее обсматривает
    music Loved_Up
    img 10595
    with Dissolve(1.0)
    w
    img 10596
    with fade
    citizen4 "Один..."
    img 10597
    with fade
    citizen4 "Два..."
    img 10598
    with fade
    citizen4 "Три..."
    img 10599
    with fade
    w
    img 10600
    with fade
    w
    img 10601
    with diss
    w
    img 10602
    with fade
    citizen4 "Четыре..."
    img 10603
    with fade
    w
    img 10604
    with fade
    w
    citizen4 "Пять..."
    #Моника убирает грудь
    music Groove2_85
    img 10606
    with diss
    m "Доволен?"
    citizen4 "Более чем..."
#    $ pylonpart3startsCompleted = True
    # Добавить сколько то corruption
    return

label gallery_11759:
    img 11745
    with fade
    citizen1 "Тетя, у нас с братом возникла шикарная идея!"
    img 11746
    citizen1 "Мы ведь с тобой не первый раз видимся и уже не чужие люди.."
    img 11747
    m "Ты это к чему?"
    img 11748
    citizen1 "Мда, не умею я говорить намеками..."
    citizen1 "Короче мы хотим посмотреть на твои сиськи, но уже так сказать без всего!"
    img 11749
    menu:
        "Мне нужны деньги...":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11750

            m "Хватит с вас и того, что вы уже видели!"
            return
    music Groove2_85
    img 11751
    with fade
    m "Ну а мне это зачем?"
    img 11752
    citizen1 "Ну как зачем? А зачем ты нам их в одежде показываешь?"
    citizen1 "Мы заплатим!"
    music Hidden_Agenda
    img 11753
    with diss
    m "Хорошо, смотрите, только руками не трогать!"
    m "И отвернитесь!"
    # отворачиваются
    sound snd_fabric1
    img 11755
    with fade
    w
    img 11754
    citizen1 "О чем речь, тетя! Разве мы когда нибудь тебя обманывали?"
    m "Можете поворачиваться.."
    img 11756
    w
    img 11757
    w
    # поворачиваются, моника показывает сиськи
    music Loved_Up
    img 11758
    with diss
    citizen1 "Ого! Прямо как у моей бывшей!"
    # показывает сиськи еще
    img 11759
    with diss
    w
    img 11760
    with diss
    citizen1 "Вот это класс, тетя! Так они смотрятся гораздо лучше."
    img 11761
    with diss
    w
    img 11762
    with diss
    w
    img 11763
    with diss
    w
    img 11764
    with diss
    # показывает сиськи еще
    w
    music Groove2_85
    img 11765
    with diss
    citizen1 "Да, сегодня день прошел не зря!"
    return

label gallery_11776:
    music Groove2_85
    img 11766
    with fade
    citizen1 "Тетя, покажи нам свои сиськи!"
    img 11767
    m "Как именно?"
    img 11768
    citizen1 "А ты шутница. Конечно голыми, так интереснее!"
    img 11769
    menu:

        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11770
            m "Хватит с вас и того, что вы уже видели!"
            return

    #m "Отвернитесь!"
    # отворачиваютяс, моника переодевается...
    #m "Можете повернуться."
    img 11771
    m "Хорошо. Если заплатите..."
    music Loved_Up
    img 11772
    with fadelong
    w
    img 11773
    with diss
    m "Только руками не трогать!"
    img 11774
    citizen1 "Какие вопросы, тетя!"
    # показывает
    img 11775
    citizen1 "Не могу наглядеться, красота!"
    # смена картинки, под другим углом
    img 11776
    w
    img 11777
    w
    img 11778
    w
    img 11779
    citizen1 "Тетя, а че ты молчишь?"
    img 11780
    m "Мне нечего вам сказать..."
    img 11781
    citizen1 "Ого! Ну ладно, глядя на такие сиськи можно и ничего не говорить!"
    # смена картинки, под другим углом
    img 11782
    w
    img 11783
    w
    img 11784
    w
    img 11785
    citizen1 "Эй, тетя! Как насчет того, чтобы получить немного больше?"
    img 11786
    with diss
    m "..."
    img 11787
    citizen1 "У меня идея! Нас как раз двое, как и твоих подружек. Давай обнимемся!"
    music Groove2_85
    img 11788
    with diss
    m "Даже не надейся!!!"
    img 11789
    citizen1 "Кто-то сегодня не в духе? Ладно, и так все очень хорошо!"
    return

label gallery_11801:
    music Groove2_85
    img 11790
    with fade
    citizen1 "Тетя, покажи нам свои сиськи!"
    img 11791
    m "Как именно?"
    img 11792
    citizen1 "Серьезно?! Давай снимай уже все!"
    img 11793
    menu:
        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11794
            m "Хватит с вас и того, что вы уже видели!"
            return
    img 11795
    with fade
    m "Отвернитесь!"
    # отворачиваютяс, моника переодевается...
    music Loved_Up
    sound snd_fabric1
    img 11796
    with fade
    w
    img 11797
    with diss
    m "Можете повернуться."
    m "Только руками не трогать!"
    img 11798
    citizen1 "Конечно, тетя!"
    # показывает
    img 11799
    w
    img 11800
    w
    img 11801
    citizen1 "Вау! Как в первый раз!"
    img 11802
    w
    img 11803
    w
    img 11804
    # смена картинки
    music Groove2_85
    img 11805
    citizen1 "Ты же не против заработать чуть больше... Сожми ка свои аппетитные соски!"
    img 11806
    m "Ну...Я не знаю..."
    img 11807
    citizen1 "Давай! И прямо сейчас получишь часть денег!"
    img 11808
    menu:
        "Хорошо.":
            pass
        "Хватит с вас и того, что вы уже видели!":
            img 11809
            m "Хватит с вас и того, что вы уже видели!"
            return

    # смена картинки - моника сжимает соски
    music Loved_Up
    img 12487
    with fade
    w
    img 12488
    w
    img 12489
    citizen1 "Уф...А ты горячая!"
    citizen1 "И так заводит!"
    img 12490
    m "Ай!"
    mt "Это немного больно и даже немного приятно... Странно..."
    # смена картинки - моника сжимает соски
    img 12491
    w
    img 12492
    w
    music Groove2_85
    img 12493
    with fade
    citizen1 "Ух, тетя, снова нас порадовала!"
    # ?? может есть смысл сделать картинку: если было сжатие сосков - моника наклоняется и поднимает монетку
    return
