# Дом. Комната Барди. Разговор Барди и Бетти.
label dialogue_betty_college_0_1:
    # Бетти стоит в комнате Барди и недовольно
    img 14566
    betty "Чего тебе надо? Зачем ты меня звал?"
    # Барди лежит на кровати и смотрит на Бетти с улыбочкой
    img 14567
    bardie "Мне нужно проверить, соблюдаешь ли ты правила этого дома..."
    img 14568
    betty_t "Как же меня этот сопляк достал со своими глупостями! Пусть проверяет... и отстанет уже от меня."
    # подходит к Бетти и задирает ей юбку, заглядывает под нее. Бетти без трусиков. Барди довольно
    img 14569
    w
    img 14570
    w
    img 14571
    w
    img 14572
    bardie "Хорошо. Я вижу, что ты соблюдаешь правила. Позови гувернантку. Я давно не проверял ее."
    # Бетти недовольно
    img 14573
    betty "Тебе надо - ты и зови. Мне нет дела до твоих глупостей."
    img 14574
    bardie "Я сказал тебе, чтобы ты позвала гувернантку..."
    bardie "Или ты решила, что меня не надо слушаться? Ты забыла, что у меня есть парочка очень интересных фото с тобой и тренером?"
    # Бетти поворачивается к Барди, зло смотрит на него
    img 14575
    betty_t "Когда же ты уже отстанешь от меня?!"
    betty_t "!!!"
    # Барди с серьезной миной
    img 14576
    bardie "Ну? Я жду!"
    img 14577
    betty "!!!"
    img 14578
    betty "Гувернантка! Гувернантка!!!"
    # спустя несколько минут появляется Моника, Барди возле Моники
    # с лица
    img 14579
    mt "Эта деревенщина не знает, что так орать на весь дом - неприлично..."
    mt "Что на этот раз?.. Эта Бетти с этим малявкой. Я уже даже не знаю, чего ожидать от них."
    mt "Когда же они все уже исчезнут из моего дома?.."
    # со спины
    img 14580
    m "Да, миссис Робертс..."
    # Бетти, не поворачиваясь к Монике
    # Барди идет к кровата
    img 14582
    betty "Гувернантка, я тебя позвала, чтобы..."
    img 14583
    betty "..."
    # Барди прыгает на кровать
    img 14581
    w
    img 14584
    betty "Хм. Барди, что ты там хотел? Давай, быстрее.!"
    img 14585
    bardie "Мне нужно проверить, насколько хорошо вы соблюдаете правила этого дома и..."
    img 14586
    betty "И?"
    img 14587
    bardie "... и запечатлеть это на свой телефон!"
    # Барди поворачивается к Монике и говорит
    img 14588
    bardie "Начнем с тебя. Ты же хорошая гувернантка? Ты соблюдаешь правила?"
    # Моника в шоке, смотрит на него, как на больного
    img 14589
    mt "Он совсем обнаглел!!!"
    mt "Эта малявка требует от меня, Моники Бакфетт, чтобы я согласилась задрать юбку!"
    mt "Задрать юбку перед каким-то малявкой, который будет снимать это на телефон! Который поселился в МОЕМ доме!!!"
    mt "!!!"
    img 14590
    m "Я не буду делать этого! Да как ты смеешь?! В обязанности гувернантки не входит позировать в голом виде перед камерой!"
    img 14591
    bardie "А в обязанности хорошей гувернантки - входит. Ты же хорошая гувернантка?"
    # Моника смотрит зло
    img 14592
    m "!!!"
    img 14593
    bardie "Или ты не соблюдаешь правила этого дома и хочешь получить штраф?"
    bardie "???"
    # Моника думает
    if monicaUnder != "Nude":
        img 14594
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        # Моника убегает
        img 14595
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        return False
    img 14594
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            # Моника убегает
            img 14595
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return False
    img 14596
    m "!!!"
    # Моника, срипя зубами соглашается, поднимает юбку, Барди фото не делает и смотрит на Бетти
    img 14597
    w
    img 14598
    w
    img 14599
    bardie "Бетти, а ты чего ждешь? Я хочу запечатлеть на фото вас вдвоем. Поднимай юбку!"
    # Бетти офигевает и начинает ор-р-р-рать
    img 14600
    betty "Если эта шлюха готова поднять юбку перед любым, даже перед моим приемным сыном..."
    betty "То я на такое никогда не соглашусь!"
    img 14601
    betty "!!!"
    # Бетти уходит, Моника продолжает держать юбку и смотрит ей вслед
    img 14602
    betty "Я порядочная замужняя женщина и ты не смеешь требовать от меня такого!" #высокомерно
    bardie "Стой! Я с тобой еще не договорил! Ты куда?" # в этом же арте
    # кадр меняется на Барди
    img 14603
    bardie_t "Значит вот так?.. Значит, она у меня еще недостаточно под контролем."
    bardie_t "Окей... Я придумаю что-нибудь еще, помимо фоток с тренером."
    return

# Дом. Спальня. Разговор Барди и Бетти.
label dialogue_betty_college_1:
    # Барди разговаривает нагло, отдает приказ
    img 14604
    w
    img 14605
    bardie "Сегодня мой преподаватель вызывает к себе родителей..."
    # Бетти вопросительно
    img 14606
    betty "???"
    # Поворачивается
    img 14607
    betty "А я здесь причем?"
    betty "Иди к Ральфу, скажи ему об этом."
    img 14608
    bardie "Ты же моя приемная мать. Ты и сходишь в колледж. Отцу не обязательно об этом знать."
    bardie "У меня там небольшие проблемы: меня могут отчислить. Я хочу, чтобы ты уладила этот вопрос."
    img 14609
    betty "В смысле, 'ты хочешь'?! Почему я должна идти в колледж и вообще тратить свое время на это?"
    img 14610
    bardie "Потому что отцу не обязательно знать не только о том, что у меня проблемы в колледже, но и еще кое о чем..."
    bardie "О чем мы оба с тобой знаем."
    # Бетти зло смотрит
    img 14611
    betty "!!!"
    img 14612
    bardie "Вот поэтому сегодня именно ТЫ пойдешь в колледж и сделаешь так, чтобы меня не отчислили!"
    # Бетти раздражена назойливостью Барди
    img 14613
    betty_t "Чего эта малявка пристала ко мне?! Как бы поскорее отвязаться от него?"
    img 14614
    betty "Это твои проблемы, разбирайся с этим сам!"
    img 14615
    bardie "Это наша общая проблема! Так же, как и проблема того, что ты трахаешься со всеми подряд!"
    # Бетти, кипя от злости
    img 14616
    betty "!!!"
    img 14617
    betty "Вообще-то, я верная жена! Не смей говорить обо мне такое!"
    # Барди в ответ смеется
    img 14618
    bardie "Если хочешь, чтобы отец и дальше думал, что ты верная жена, делай, что я тебе говорю."
    bardie "И только попробуй не уладить вопрос моего отчисления. Тебе же хуже будет!"
    # Бетти убийственным взглядом смотрит на него и уходит
    img 14619
    betty "!!!"
    img 14620
    bardie_t "Мне нужно будет убедиться, что она все сделает правильно. Надо за ней проследить!"
    return

# Колледж. Бетти, полная решимости, идет в кабинет преподавателя. Барди, следуя за ней, остается возле двери кабинета и подглядывает.
# Колледж. Кабинет учителя. Разговор Бетти с учителем.
label dialogue_betty_teacher_1:
    # Бетти садится напротив учителя, который сидит за учительским столом. Бетти с улыбкой
    betty "Добрый день, мистер..."
    # учитель с серьезным лицом
    teacher "...Эдвардс. Добрый день. Я так понимаю, вы - мать Барди?"
    betty "Да, мистер Эдвардс. Барди сказал, что у него какие-то проблемы..."
    teacher "У Барди серьезные проблемы с успеваемостью. У него много прогулов и много не сданных зачетов."
    teacher "Я неоднократно пытался проводить с ним разъяснительные беседы, но безуспешно."
    teacher "К сожалению, я вынужден вам сообщить, что я сейчас готовлю документы на отчисление Барди для передачи директору."
    betty "Мистер Эдвардс, документы еще находятся у вас? Я могу их посмотреть?"
    teacher "Да, конечно. Я вас пригласил сегодня именно для этого. Вот личный файл Барди, можете ознакомиться."
    # Учитель дает Бетти папку с документами, та их просматривает, сосредоточенно думая. Учитель в это время пялится на ее грудь
    betty_t "Этот мелкий сопляк совсем не бывает в колледже!"
    betty_t "Если мне удастся уговорить учителя притормозить это дело, у меня появится отличная возможность приструнить его..."
    betty_t "В противном случае, Барди мне вообще никакой жизни не даст. Я итак его уже видеть не могу."
    betty_t "Интересно, как мне уговорить этого мистера Эдвардса? Может, попросить денег у Ральфа? Скажу, что для колледжа..."
    # Бетти поднимает взгляд на учителя, тот продолжает пялиться на нее. Бетти уже без улыбки, с серьезным выражением лица
    betty "Мистер Эдвардс, я вижу, что у Барди совсем все плохо с учебой. Этот сорванец и правда в последнее время совсем отбился от рук."
    betty "Возможно, мы с вами как-то сможем уладить этот вопрос? Я могла бы оказать спонсорскую помощь колледжу. Купить мел для доски, например."
    betty "Я обещаю, что поговорю с Барди. Этот сопл... Барди больше не будет прогуливать занятия и сдаст все зачеты."
    teacher "..."
    betty "Мистер Эдвардс?"
    # учитель, наконец, отрывает взгляд от ее груди.
    teacher "А? Что?"
    betty "Я говорю, что готова поговорить с Барди и он будет себя хорошо вести..."
    teacher "..."
    teacher "Ну... Я даже не знаю... Документы уже подготовлены."
    teacher "Боюсь, что ничего уже нельзя изменить."
    # Барди подглядывает через приоткрытую дверь, переживает
    bardie_t "Черт!"
    bardie_t "..."
    bardie_t "Эта деревенщина не сможет договориться с преподом. Надо было гувернантку посылать к нему."
    # Бетти продолжает уговаривать учителя
    betty "Личный файл Барди все еще находится у вас. Значит, именно от вас зависит, дойдут ли документы до директора."
    betty "Что я могу сделать для того, чтобы Барди остался в колледже?"
    # препод снова залипает на груди Бетти, задумчиво
    teacher "Хм. Я вижу, что вы искренне переживаете за сына, Миссис Робертс."
    # Бетти расплывается в улыбке
    betty_t "Ненавижу этого сопляка!"
    teacher "Возможно, я смогу что-нибудь придумать. Это будет непросто... Ведь, помимо меня, и другие учителя в курсе ситуации с Барди."
    teacher "Мне придется как-то аргументировать то, что я изменил свое решение..."
    betty "Мистер Эдвардс, я понимаю, что это сложный процесс. Если я смогу чем-то вам помочь, то я буду только рада."
    # тут Бетти случайно роняет паку Барди на пол
    betty "Oй!"
    # наклоняется за ней, поворачивает голову и видит, что учитель сидит с внушительным стояком
    betty "!!!"
    # Бетти зависает на этом зрелище, но тут же берет себя в руки, выпрямляется. Глаза у нее заблестели, но она делает вид, что ничего не видела
    betty "..."
    betty "Так на чем мы остановились, мистер Эдвардс?.."
    # учитель догадался, что она его спалила, и принимает решение развести Бетти на "помощь"
    teacher "На том, что вы могли бы мне помочь в этом непростом деле."
    # Бетти воодушевленно
    betty "Да, конечно. Я буду рада помочь вам. Что мне нужно будет сделать?"
    teacher "..."
    # учитель встает со стула, поправляет ширинку и пристально смотрит на Бетти. Бетти сидит на стуле и не может оторвать взгляд от его стояка, который прямо перед ее лицом
    betty "М-м-мистер Эд-д-двардс... Я н-не совсем вас п-п-понимаю..."
    betty_t "Вот черт. Что же мне делать?"
    betty_t "Так, стоп! Я же замужняя женщина и верная жена."
    betty_t "Тем более, я разговариваю с учителем Барди! Я не должна так смотреть на то, что у него в штанах!"
    # Бетти поднимает взгляд от ширинки препода и смотрит ему в глаза. Говорит возмущенно
    betty "Мистер Эдвардс! Я замужем! Как вы можете предлагать мне подобное?!"
    teacher "Вы же сами предложили мне помощь, миссис Робертс... Это очень помогло бы мне..."
    # Бетти снова уставилась на его стояк
    teacher "Тем более, я не прошу о многом. Вы могли бы просто приласкать его рукой. У меня так давно не было никого."
    teacher "А вы такая красивая, миссис Робертс, что я просто не в силах держать себя в руках."
    # учитель медленно начинает расстегивать ремень
    betty_t "..."
    betty_t "Я не должна этого делать! Что вообще себе позволяет этот мистер Эдвардс?!"
    # учитель расстегивает молнию на брюках, Бетти не в силах отвести взгляд
    betty_t "С другой стороны..."
    betty_t "Хм... Если я просто потрогаю его, это же не будет считаться изменой?"
    betty "М-мистер Эд-двардс, если об этом кто-нибудь узнает..."
    teacher "Миссис Робертс, это не в моих интересах, чтобы кто-либо узнал о нашей с вами договоренности."
    teacher "Я в виде исключения предлагаю вам единственный из всех возможных способов решить эту проблему с вашим сыном."
    teacher "Для этого вам достаточно просто протянуть руку..."
    # препод достает свой стояк
    teacher "... и немного погладить его."
    betty "!!!"
    menu:
        "Постараться убедить учителя не делать этого":
            betty "Мистер Эдвардс, я никогда себе не позволяю такого с другими мужчинами. Только с мужем..."
           return 1
        "Поддаться давлению со стороны учителя":
            pass
    betty "Мистер Эдвардс, я, конечно, не совсем уверена. Это единственный способ?"
    betty_t "У него просто каменный стояк. Если я к нему притронусь... Так интересно ощутить его."
    teacher "Это единственный способ, миссис Робертс. Просто прикоснитесь ко мне."
    # Бетти протягивает руку и замирает буквально в сантиметре от члена
    betty_t "Что я делаю? Это так неправильно..."
    betty_t "Я просто потрогаю его и вопрос с Барди будет решен. Я делаю это не ради своего удовольствия!"
    # препод берет ее за запястье и притягивает ее руку к своему члену, Бетти прикасается к нему пальцами
    betty_t "Ммм... Он и правда каменный. И такой горячий..."
    betty "Мистер Эдвардс, я... мне... это так неправильно..."
    teacher "Вы уже делаете это, миссис Робертс. Еще совсем немного. Сожмите его своей ручкой."
    # препод убирает свою руку, Бетти обхватывает его член рукой
    betty_t "Ооо! У этого мистера Эдвардса просто отличный член. Интересно, какой он на вкус?"
    betty_t "!!!"
    betty_t "О боже! О чем я думаю?!"
    # Бетти медленно начинает дрочить ему
    teacher "Да, так! У вас отлично получается, миссис Робертс! Быстрее!"
    # Бетти пристально смотрит на член и старается с удвоенной силой
    # Барди все видит и слышит. Волнение на его лице сменяется злорадной ухмылкой. Он достает свой смартфон и делает фото.
    bardie_t "Офигеть! Бетти даже в колледже умудрилась подержать чужой член в руке!"
    bardie_t "!!!"
    bardie_t "Может, будет какое-то продолжение?"
    # Бетти продолжает усердно работать рукой, не отрывая глаз от члена учителя
    teacher "Ооо, миссис Робертс... Да, так! Еще..."
    teacher "Ммм... Еще быстрее!"
    #препод со стоном кончает на личный файл Барди, который на столе, попадает и Бетти на руку
    teacher "ООООООООО!!!"
    # препод крайне доволен, надевает обратно брюки и садится за стол, а Бетти, изображая из себя оскорбленную невинность, вытирает руку
    betty "Вы испачкали документы Барди, мистер Эдвардс."
    teacher "Ничего страшного, миссис Робертс. Директор все равно этого не заметит."
    # Бетти в шоке, учитель с улыбочкой
    betty "В смысле?! Мы же с вами договорились, что эти документы не дойдут до директора!"
    teacher "Миссис Робертс, в моих силах пока только притормозить это дело."
    betty "???"
    teacher "Но если вы еще раз посетите меня на днях, то, возможно, я смогу закрыть этот вопрос."
    # Бетти удивленно
    betty "Еще раз?!"
    teacher "Именно. Мне может снова потребоваться ваша помощь."
    # Барди злорадно ухмыляется за дверью
    bardie_t "!!!"
    bardie_t "Отлично! Нужно будет дождаться продолжения!"
    # Барди убегает, Бетти, сидя напротив учителя, пристально смотрит на него
    betty_t "Из-за этого сопляка мне придется тащиться сюда снова. Он теперь в долгу передо мной. Нужно только окончательно уговорить учителя."
    betty "Хорошо, мистер Эдвардс. Я загляну к вам на днях. И, надеюсь, мы с вами закроем этот вопрос."
    teacher "Конечно, миссис Робертс. С нетерпением буду ждать встречи с вами."
    return

# Дом. Двор. Спустя некоторое время Бетти возвращается домой и во дворе дома сталкивается с Барди.
label dialogue_betty_college_2:
    # Барди делает вид, что ничего не знает, спрашивает Бетти
    img 14621
    bardie "Ну как? Надеюсь, ты все уладила?"
    # Бетти смотрит возмущенно
    img 14622
    betty "Ты хоть видел свои оценки?! Ты думаешь так просто решить этот вопрос, если ты вообще не бываешь в колледже?!"
    # Барди строго
    img 14623
    bardie "То есть у тебя не получилось договориться с учителем?"
    bardie "..."
    bardie "Я так и знал, что тебе ничего нельзя поручить..."
    img 14624
    betty "Ты как со мной разговариваешь, сопляк! Почему это мне ничего нельзя поручить?! Я почти договорилась с ним!"
    # Барди заинтересованно
    img 14625
    bardie "Что значит 'почти'?"
    # Бетти растерянно смотрит на Барди
    img 14626
    betty "..."
    img 14627
    betty_t "Черт!.."
    betty_t "Вот пристал! Я что, должна отчитываться перед ним?!"
    # отводит взгляд в сторону, Барди вопросительно смотрит на нее
    img 14628
    bardie "Ну?"
    img 14629
    bardie_t "Давай, соображай быстрее. Даже соврать нормально не может..."
    img 14630
    betty "Мы... Хм..."
    betty "..."
    # Бетти поворачивается к Барди, с уверенным видом заявляет
    img 14631
    betty "Мы с мистером Эдвардсом обсуждаем, на каких условиях нам договариваться!"
    betty "!!!"
    # Барди с сарказмом и мерзкой улыбочкой
    img 14632
    bardie "И чего учитель хочет?"
    img 14633
    betty "..."
    img 14634
    betty "А это не твое дело, сопляк!"
    betty "Как только учитель согласится не выкидывать тебя из колледжа, я тебе об этом скажу!"
    betty "А теперь отойди! У меня нет времени на тебя!"
    img 14635
    betty "!!!"
    # Бетти уходит, Барди, все с той же улыбочкой
    img 14636
    bardie_t "Ну-ну. Я прослежу, как ты дальше будешь 'договариваться' с ним."
    bardie_t "Мастер переговоров. Аха-ха!"
    return

# Дом. Второй этаж.
label dialogue_betty_college_3:
    # Бетти нахмуренно смотрит на себя в зеркало
    betty_t "!!!"
    betty_t "Как же меня достал этот мерзкий мальчишка со своими глупостями! Не могу его больше видеть!"
    betty_t "Скорее бы закрыть вопрос с его отчислением. Надеюсь, тогда он отстанет от меня!"
    betty_t "..."
    # с улыбкой
    betty_t "Хм... А у меня сегодня хорошо получилось уговорить учителя насчет документов этого сопляка..."
    betty_t "Я не только порядочная, но еще и умная женщина. Ральфу очень повезло, что у него такая жена, как я!"
    return

# Колледж. Кабинет учителя. Барди снова прячется за приоткрытой дверью кабинета.
label dialogue_betty_teacher_2:
    # Бетти сидит напротив учителя, как в прошлый раз. Говорит с улыбкой
    betty "Мистер Эдвардс, я пришла, как мы с вами и договаривались."
    # учитель тоже улыбается
    teacher "Рад вас видеть снова, миссис Робертс. Документы Барди все еще у меня."
    betty "Спасибо. Я надеюсь, что мы с вами закроем сегодня этот вопрос?"
    teacher "Возможно, миссис Робертс. Все зависит от того, насколько вы готовы помочь мне в этом..."
    betty "..."
    # учитель, как и в прошлый раз, пялится на ее грудь
    betty_t "Почему мне, порядочной женщине, приходится заниматься подобными вещами из-за какого-то малявки?!"
    betty_t "Мне снова придется работать рукой? Что ж, в прошлый раз это помогло..."
    betty_t "Но только рукой! На большее я не соглашусь, это уже будет изменой! А я замужняя женщина!"
    teacher "..."
    betty "Мистер Эдвардс?"
    teacher "Миссис Робертс, вы же не будете против, если я прикоснусь к вашей прекрасной груди?"
    # Бетти растерянно
    betty "???"
    betty "Я... Я думала, что мы просто повторим нашу прошлую встречу..."
    teacher "Я просто потрогаю ее и все. У вас такая красивая грудь!"
    betty "..."
    menu:
        "Не делать этого. Я порядочная замужняя женщина. Я же пришла сюда, чтобы удовлетворить его только рукой...":
            betty "Мистер Эдвардс, я порядочная замужняя женщина. Как вы себе это представляете?"
            return 1
        "Почему нет? Он же просто потрогает мою грудь.":
            pass
    betty "Мистер Эдвардс, я не против, если вы только потрогаете ее. Не более того!"
    teacher "Миссис Робертс, я просто теряю голову от вашей красоты! Позвольте мне прикоснуться к вам. Хотя бы один раз."
    # Бетти встает со стула, приспускает платье и оголяет грудь. Учитель встает, обходит свой стол и подходит к ней
    # Барди подглядывает через приоткрытую дверь, делает фото
    bardie_t "!!!"
    bardie_t "Сегодня в моей коллекции прибавятся отличные фотки с Бетти! Жаль, отец пока не может оценить их."
    # учитель берет в ладонь грудь Бетти, приподнимает ее, сжимает
    betty "Ох. Мистер Эдвардс. Достаточно." # ахххх
    betty_t "Ммм, это так приятно..."
    teacher "Миссис Робертс, я хочу поцеловать ее."
    betty "Нет, нет. Мы об этом не договаривались." # возмущенно (но ахх)
    # учитель не слушает ее, целует ее соски
    betty "Ох! Ооо!"
    betty_t "Мне нужно остановить это немедленно. Ммм... Иначе одной рукой я не обойдусь сегодня."
    betty_t "Я порядочная и замужняя женщина! Я не могу себе позволить большего!"
    # Бетти отталкивает препода, неуверенно
    betty "Мистер Эдвардс! Давайте, сделаем все, как в прошлый раз и я пойду. У меня мало времени."
    teacher "Как скажете. Но вам же это нравится, миссис Робертс. Зачем вы сопротивляетесь?"
    # учитель расстегивает ремень и ширинку, достает член, Бетти смотрит на его стояк
    teacher "Возьмите его в руку, миссис Робертс."
    betty "..."
    # Бетти подходит к преподу ближе и гладит его член
    betty_t "Ммм... Какой же он... Ммм..."
    betty_t "Так! Мне надо держать себя в руках и не забывать о том, что я замужем."
    teacher "Давайте, миссис Робертс, смелее. Прикоснитесь к нему губами."
    betty "Губами?!"
    menu:
        "Как он мог предложить мне такое?! Я порядочная женщина!":
            betty "Мистер Эдвардс, я не могу на такое согласиться. Я порядочная женщина."
            return 1
        "Мне совсем неинтересно, какой он на вкус!!!":
            pass
    betty "Мистер Эдвардс, вам не достаточно нравится, как я делаю это рукой и вы хотите большего?"
    teacher "Миссис Робертс, просто поцелуйте его. Неужели он вам не нравится?"
    betty_t "Черт!!! Мне неинтересно... Мне неинтересно..."
    teacher "Всего один поцелуй..."
    betty "Только один!"
    # Бетти опускается на колени перед преподом, смотрит на член
    betty_t "Что я творю?"
    betty_t "..."
    betty_t "Я просто прикоснусь к нему губами... и языком. Я делаю это не ради себя!"
    # Бетти прикасается к члену учителя губами, потом проводит языком по головке
    betty_t "Ммм... Ну и что, что он оказался таким вкусным..."
    # и еще раз языком по стволу и по головке
    betty "Мистер Эдвардс, я... думаю, что... достаточно..."
    # а сама облизывает его
    teacher "Еще немного, миссис Робертс. Обхватите его губами."
    # Бетти обхватывает губами головку и насаживается головой на член
    teacher "Ооо, да!"
    betty_t "!!!"
    # Бетти запускает свою руку под платье, в трусики (платье поднимает, трусики красные)
    betty "Ммммфмммффф..."
    # Бетти старательно делает минет преподу, а Барди делает фото
    bardie_t "В прошлый раз подрочила, сегодня отсосала... Как она старается, чтобы меня не отчислили!"
    bardie_t "Аха-ха!"
    bardie_t "!!!"
    # Бетти продолжает работать ртом
    teacher "Ммм... Как же чертовски хорошо! Еще, быстрее!"
    betty "Ммммфмммффф..."
    # препод со стоном кончает на ее лицо
    teacher "Ооо, дааааааа!"
    # Бетти делает еще несколько движений своей рукой у себя в трусиках и кончает следом за ним
    betty "ООООООООО!!!"
    # препод крайне доволен (уже одет)
    teacher "Миссис Робертс, это было великолепно. Думаю, нам с вами нужно будет еще раз встретиться, чтобы закрепить нашу договоренность."
    # смотрит на него снизу вверх, вся в сперме
    betty "Еще раз?"
    teacher "Именно. Еще раз и я закрою этот вопрос с отчислением Барди."
    # Барди злорадно ухмыляется за дверью
    bardie_t "!!!"
    bardie_t "Отлично!"
    # Барди убегает, Бетти, сидя на полу перед учителем
    betty_t "Еще один визит к преподавателю и этот сопляк у меня в руках! Не могу дождаться, чтобы, наконец, поставить его на место."
    betty "Хорошо, мистер Эдвардс. Я загляну к вам на днях. И мы закрепим с вами нашу договоренность."
    teacher "Конечно, миссис Робертс. С нетерпением буду ждать встречи с вами."
    return

# Дом. Двор. Спустя некоторое время Бетти возвращается домой и во дворе дома сталкивается с Барди.
label dialogue_betty_college_4:
    # Барди снова делает вид, что не знает ничего
    bardie "Ну как? Есть хорошие новости для меня?"
    # Бетти высокомерно
    betty "Ты думашь, что серьезные дела так быстро решаются?!"
    betty "Я же тебе сказала, что сообщу тебе! А пока отстань от меня!"
    betty_t "Сопляк!"
    betty_t "!!!"
    # Бетти уходит, Барди хихикает злорадно
    bardie_t "Надо придумать, как 'отблагодарить' ее. Не зря же она так старательно договаривается с учителем."
    # задумчиво
    bardie_t "Хм... У меня есть неплохая идея..."
    return

# Колледж. Кабинет учителя. Барди, как обычно, прячется за приоткрытой дверью кабинета.
label dialogue_betty_teacher_3:
    # Бетти сидит напротив учителя, как в прошлый раз. Бетти с улыбкой
    betty "Мистер Эдвардс, я пришла, как мы с вами и договаривались."
    teacher "Рад вас видеть снова, миссис Робертс."
    betty "Я надеюсь, что мы с вами закроем сегодня вопрос отчисления Барди с колледжа?"
    teacher "Возможно, миссис Робертс. Все зависит от того, насколько вы готовы помочь мне в этом..."
    betty "..."
    # учитель, как и в прошлый раз, пялится на ее грудь
    betty_t "Сегодня нельзя соглашаться на большее! Достаточно было прошлого раза..."
    betty_t "Я не собираюсь изменять своему мужу!"
    teacher "Миссис Робертс, вы же не будете против, если я прикоснусь к вашей прекрасной груди, как в прошлый раз?"
    betty "???"
    betty "Я... Да. Только как в прошлый раз, не более того!"
    teacher "Миссис Робертс, ну конечно! Вам не о чем переживать!"
    # Бетти встает, приспускает платье и оголяет грудь. Учитель подходит к ней, берет в ладонь грудь Бетти, целует соски
    betty_t "Ммм, как же хорошо..."
    betty "Ох. Мистер Эдвардс."
    teacher "Миссис Робертс, я сниму с вас платье? Оно мешает мне рассмотреть вашу красоту."
    # Бетти растерянно
    betty "Вы хотите снять с меня платье?!"
    menu:
        "Это все закончится сексом. Я не должна делать этого! Я порядочная женщина...":
            betty "Мистер Эдвардс, вы забыли, что я порядочная женщина? Достаточно моей голой груди."
            return 1
        "Он хочет приласкать меня. Это же просто ласки, а не измена? Я же порядочная женщина...":
            pass
    betty "Мистер Эдвардс, вам не достаточно моей голой груди и вы хотите большего?"
    teacher "Миссис Робертс, я ничего такого не собираюсь делать. Просто приласкаю вас немного."
    teacher "Вы же в прошлый раз сделали мне приятно, теперь я хочу сделать так, чтобы и вам было хорошо."
    # Бетти возмущенно
    betty "Нет, Мистер Эдвардс! Вы - преподаватель. Как вы вообще можете предлагать мне такое?!"
    betty "Мне, замужней женщине!"
    teacher "Миссис Робертс, вы такая заботливая мать, так искренне переживаете за вашего сына..."
    teacher "Я предлагаю вам единственный из всех возможных способов окончательно решить вопрос об учебе Барди."
    teacher "Если вы сейчас откажетесь, то я буду вынужден передать документы Барди директору."
    teacher "И тогда ничего нельзя уже будет исправить. Подумайте хорошо, прежде чем отказывать мне."
    # Бетти пристально смотрит на препода, сомневается
    betty "..."
    # принимает решение
    betty "Ну ладно, мистер Эдвардс... Только быстро!"
    # Бетти раздевается до трусиков, учитель гладит ее рукой через трусики
    betty "Ах!"
    betty_t "О, как же приятно!"
    # учитель подводит ее к столу, нагибает над ним и снимает с нее трусики, второй рукой расстегивает свою ширинку
    betty "Ммм..."
    # продолжает рукой ласкать ее киску, а потом входит в нее пальцами
    betty "Ооо... М-мистер Эд-двардс... Ммм..."
    betty_t "Ох, черт! Как же хорошо! Но я должна остановить его!"
    betty "М-мистер Эд-двардс, я... дум-маю, что... д-достаточно..."
    # учитель продолжает водить рукой туда-сюда
    teacher "Еще немного, миссис Робертс. Раздвиньте ножки пошире."
    # учитель убирает пальцы, берет в руки свой член, нацеливается в киску Бетти и входит в нее
    betty "Ааааах!"
    teacher "Ооооо..."
    # Барди злорадно ухмыляется за дверью и делает несколько кадров
    bardie_t "!!!"
    bardie_t "Отлично! Теперь она от меня никуда не денется!"
    # препод "любит" Бетти на столе, потом они перемещаются на пол, Бетти садится сверху
    teacher "Ммммммм..."
    betty "Только не кончайте в меня, мистер Эдвардс!"
    # Бетти двигается на учителе и через некоторое время кончает
    betty "ООООООООО!!!"
    # препод вынимает из нее член и со стоном кончает на ее грудь
    teacher "Ооо, дааааааа!"
    # препод крайне доволен, лежит на полу, Бетти сидит на учителе, недоверчиво смотрит на него
    teacher "Миссис Робертс, это было великолепно. Считайте, что вопрос с отчислением Барди закрыт."
    # Бетти недоверчиво
    betty "Это точно?"
    teacher "Да, мы с вами только что закрепили нашу договоренность."
    # Барди делает еще фото и убегает, радостный
    # Бетти встает и одевается, препод тоже
    teacher "Если вдруг у Барди снова начнутся проблемы с учебой, я вам сразу же позвоню, миссис Робертс."
    betty_t "Отлично! Я сделала то, чего хотел этот сопляк. С меня хватит!"
    betty_t "Теперь он не посмеет требовать от меня своих глупостей!"
    betty "Хорошо, мистер Эдвардс. Было приятно сотрудничать с вами."
    teacher "Всегда к вашим услугам, миссис Робертс."
    return

# Дом. Двор. Бетти возвращается домой и видит во дворе, как Барди играет с мячом.
label dialogue_betty_college_5:
    # Барди снова делает вид, что не замечает ее. Бетти стоит, руки в боки и зовет его
    betty "Эй, ты! Иди сюда!"
    # Барди к ней подходит и, делая вид, что ничего не знает, вопросительно смотрит на нее
    # Барди держит мяч
    bardie "???"
    bardie "Что?"
    # Бетти ему высокомерно
    betty "Я договорилась с твоим преподавателем. Это было непросто, но я смогла его убедить не отчислять тебя из колледжа."
    betty "Он очень не хотел оставлять тебя. Мне пришлось три раза посетить его и, в итоге, я смогла его уговорить."
    # Барди продолжает молча смотреть на нее, но уже едва сдерживает улыбку
    bardie "..."
    betty "Я сделала то, о чем ты меня попросил. Но хочу сразу тебя предупредить, что я в любой момент могу позвонить мистеру Эдвардсу..."
    # Бетти с угрозой
    betty "... и он выкинет твою задницу из колледжа!"
    betty "!!!"
    betty "Поэтому с этого дня ты перестаешь строить из себя здесь хозяина и командовать мною! Если будешь хорошо себя вести, то с твоей учебой все будет в порядке."
    # Бетти с торжествующей улыбкой на лице
    betty_t "Вот ты и попался, мелкий сопляк! Попробуй теперь покомандовать в моем доме!"
    bardie "..."
    # На это Барди, не выдерживая, злорадно хохочет
    bardie "Аха-ха!!! Ты это серьезно сейчас?!"
    bardie "!!!"
    bardie "Жду тебя через пять минут в своей комнате! И не задерживайся!"
    bardie "Аха-ха!!!"
    # Барди уходит, Бетти в недоумении
    betty_t "???"
    betty_t "Что еще этому мерзкому мальчишке нужно от меня?"
    betty_t "Почему я, такая порядочная и умная женщина, должна терпеть такое в своем же доме?!"
    betty_t "!!!"
    betty_t "Он, наверное, не понял, что он больше здесь не хозяин. Хм, что ж... Пойду к нему, объясню ему еще раз, более доходчиво!"
    # Бетти с уверенным видом уходит
    return

# Дом. Комната Барди.
label dialogue_betty_college_6:
    # Барди стоит возле своего стола и улыбается, Бетти заходит к нему в комнату, возмущается
    betty "Ты, наверное, не понял, о чем я тебе говорила! Ты почему со мной так разговариваешь?!"
    betty "!!!"
    # Барди с улыбочкой указывает рукой на свой ноут
    bardie "Я позвал тебя, чтобы ты посмотрела мою коллекцию фотографий. За последние дни я сделал несколько очень интересных фоток."
    betty "???"
    betty "Что за глупости?! Какое мне дело до твоих дурацких коллекций?"
    bardie "Я уверен, что тебе понравится... Посмотри."
    # Бетти подходит к его столу и заглядывает в ноут, видит на фото себя с учителем и офигевает
    betty "!!!"
    betty "ЧТО! ЭТО! ТАКОЕ?!"
    # Бетти бомбит
    betty "Ты что делаешь, сволочь!!!"
    betty "Я порядочная женщина! Что это за фотографии?!"
    betty "Как ты смеешь, мерзкий сопляк?! Я это сделала для тебя, а ты!.. Ты!!!"
    # Барди спокойно отвечает
    bardie "Я не просил тебя трахаться с ним. Ты даже в моем колледже нашла член, за который можно подержаться."
    bardie "На этих фото доказательство очередной измены моему отцу. Попробуй только сделать что-нибудь не так..."
    bardie "..."
    bardie "Нууу, например, не слушаться меня... Эти фото сразу же увидит твой муж. И с того момента он станет уже твоим 'бывшем мужем'."
    # Бетти кипит от злости
    betty_t "!!!"
    betty_t "Ненавижу! Да как он смеет?!"
    # Бетти смотрит на Барди убийственным взглядом
    betty_t "Этот сопляк шпионил за мной! Он это все специально подстроил!"
    betty_t "!!!"
    betty_t "Но я не могу позволить, чтобы Ральф увидел эти фотографии! Даже несмотря на то, что я это делала для его сына!"
    betty_t "..."
    # Бетти, злая, складывает руки на груди и спрашивает Барди
    betty "Чего тебе надо от меня?"
    betty_t "Ненавижу этого сопляка!"
    bardie "Так-то лучше."
    bardie "Помнишь, я хотел тебя сфотографировать с задранной юбкой? Ты мне отказала тогда..."
    bardie "Так вот..."
    # Бетти снова начинает орать
    betty "Да ты совсем охренел!"
    betty "НЕТ!"
    betty "Ни за что!!! Я не буду фотографироваться так!"
    betty "!!!"
    # Барди с мерзкой улыбочкой
    bardie "???"
    bardie "Ты хорошо подумала?"
    betty "..."
    # Барди показывает свой смартфон
    bardie "Копии твоих фотографий с учителем есть у меня в телефоне. Отправить их отцу - вопрос нескольких секунд."
    betty "Ты не сделаешь этого!"
    bardie "Я уже делаю это."
    betty "!!!"
    # делает вид, что отправляет фотки, Бетти не выдерживает
    betty "Хорошо, твоя взяла... Я согласна... Но только одно фото и ты обещаешь, что никому его не покажешь!"
    betty "..."
    bardie "Естественно, не покажу. Это только для меня..."
    bardie_t "... и моего одноклассника."
    bardie_t "Теперь он мне точно поверит!"
    # Бетти фыркает, психует, но подчиняется и задирает юбку, она в трусиках
    betty "Давай, быстрее!"
    # Барди ничего не делает и смотрит на нее вопросительно
    bardie "..."
    bardie "Во-первых, почему ты в трусах?"
    # Бетти опускает юбку, смотрит возмущенно и зло, но молчит
    bardie "Ты забыла, что должна соблюдать правила этого дома? Снимай их, быстро!"
    bardie "Во-вторых, позови гувернантку. Я хочу сфотографировать вас вдвоем."
    # Бетти опять бомбит
    betty "Я не собираюсь фотографироваться с этой шлюхой!"
    betty "!!!"
    bardie "Ты сейчас снимешь свои трусы и позовешь гувернантку! Я жду!"
    # Барди садится на свою кровать и демонстративно показывает Бетти свой телефон. Бетти кипит от злости, но подчиняется
    betty_t "Ненавижу этого сопляка!"
    # Бетти отворачивается от Барди, со злостью снимает трусики
    betty "!!!"
    # Бетти с напряженным лицом зовет Монику
    betty "Гувернантка!!! Иди сюда!"
    # Барди самодовольно ухмыляется
    return

игра за Бетти. добавить ее комментарии "мне надо идти туда-то", комменты возле школы и т.д. + мысли, когда смотрит на учителя + парты, класс и остальные предметы
