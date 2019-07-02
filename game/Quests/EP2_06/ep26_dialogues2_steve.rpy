# Если нажать на контракт с Джейн
# Подменю
# Знакомство с Джейн
label ep26_dialogues2_steve1:
# Моника спрашивает у Стива, что ей надо еще немного денег.
# Что Моника скоро разберется со своими проблемами и вернет ему в 100 раз большую сумму.
# Что в интересах Стива, чтобы это было скорее сделано.
# Для этого ей нужна всего-лишь небольшая денежная сумма
# Стив смотрит на Монику и говорит что не уверен, что это в его инетересах, потому что Моника убъет его.
# Моника смотрит на Стива и говорит что он очень проницателен и его бизнес навыки ему не помогут,
# когда Моника доберется до него
    img 12515
    m "Стив. Мне надо еще немного денег..."
    m "Ты ведь понимаешь, что я скоро разберусь со своими проблемами и верну тебе в 100 раз большую сумму!"
    img 12516
    m "И, в твоих же интересах, чтобы это было сделано поскорее."
    m "Ты ведь бизнесмен, Стив! Ты стремишься получить прибыль как можно раньше!"
    img 12517
    m "И, чтобы ускорить этот процесс, мне нужна совсем небольшая денежная сумма."
    img 12518
    steve "Да, Моника. Я люблю прибыль."
    steve "Но жизнь я люблю еще больше."
    img 12519
    steve "И, я не уверен что это в моих интересах, потому что ты обещала убить меня."
    img 12520
    m "Да, Стив. Ты очень проницателен."
    m "Но твои бизнес навыки не помогут, когда я доберусь до тебя!"

# Стив удивленно спрашивает, почему тогда Моника требует денег от него, если собирается его убить?

# Моника говорит Стиву, чтобы он дал ей какие-то деньги, иначе она убъет его прямо сейчас!
    img 12521
    steve "Моника, но почему ты требуешь от меня денег сейчас, если собираешься потом убить меня?"
    steve "С какой стати я должен тебе помогать в этом?"
    img 12522
    m "С такой, что иначе я убью тебя прямо сейчас!"

# Стив говорит Монике что у него нет свободных денег и Моника про это знает.
# Джейн следит за Стивом и у него есть только тикет на ланч в ресторане.
# Выбор уйти или попросить тикет на ланч.
    img 12523
    steve "Моника, но я говорил, что у меня нет сейчас свободных денег!"
    steve "Ты знаешь про это!"
    img 12524
    steve "Джейн следит за мной и у меня есть только сертификат на ланч в ресторане."
    img 12525
    menu:
        "Потребовать тикет на ланч.":
            pass
        "Уйти":
            img 12526
            m "Мне не нужен твой сертификат, Стив!"
            return False

# Моника спрашивает, где Стив говорит у него ланч?
# Стив отвечает что ланч у него обычно в ресторане отеля Le Grand.
    img 12527
    m "И где обычно ты принимаешь ланч?"
    img 12528
    steve "Обычно я обедаю в ресторане Le Grand."

# Моника думает про себя что это странное совпадение. Но, с другой стороны, ресторан там вполне приличный.
# И было бы очень неплохо ощутить себя снова Леди и поесть в нормальном месте, нормальном!
    img 12529
    mt "!!!"
    mt "Странной совпадение..."
    mt "Но, с другой стороны, там вполне приличный ресторан."
    mt "И было бы очень неплохо ощутить себя снова Леди и поесть в нормально месте."
    mt "Нормальном!"

# Моника спрашивает у Стива чтобы он дал ей тикет на ланч.
# Стив отвечает что не может этого сделать.
# Моника злится и спрашивает у Стива что ему снова надо взамен?!
# Она знает что Стив урод и ничего не сделает просто так!
    img 12530
    m "Стив, дай мне этот сертификат на ланч."
    img 12531
    steve "Моника, но я не могу этого сделать!"
    img 12532
    m "Почему ты не можешь его дать?!"
    m "Что тебе снова надо взамен?!"
    img 12533
    m "Я знаю, что ты урод и ничего не делаешь просто так!"

# Стив отвечает что хочет, чтобы Моника пообщалась с Джейн.
# Джейн очень интересуется Моникой и восхищается ей и Ее фигурой.
# И, если Моника поговорит с ней, то Стив согласен поделиться с Моникой одним тикетом на ланч
# Джейн в последнее время сильно наседает на Стива, может быть если она займется своей фигурой,
# это ее временно отвлечет и она оставит Стива в покое.
    img 12534
    steve  "Моника, я бы хотел, чтобы ты пообщалась с Джейн."
    steve  "Она интересуется тобой и восхищается тобой и твоей фигурой."
    img 12535
    steve  "Я бы мог удовлетворить ее любопытство по поводу твоего тела, но не думаю что это будет тактично."
    steve "В конце концов, она моя невеста, хе-хе!"
    img 12536
    m "!!!"
    img 12537
    steve "Так вот."
    steve "Если ты пообщаешься с ней, то я готов поделиться с тобой одним тикетом на ланч."
    img 12538
    steve "Джейн в последнее время сильно наседает на меня."
    steve "Может быть, если она сосредоточится на своей фигуре, это ее временно отвлечет."
    steve "И она оставит меня в покое! Хе-хе!"

# Выбор Моники:
# Уйти или согласиться поговорить с Джейн
    img 12539
    menu:
        "Согласиться поговорить с Джейн":
            pass
        "Уйти.":
            img 12540
            m "Разбирайся сам со своими проститутками, Стив!"
            return False

# Моника соглашается поговорить с Джейн.
# Стив спрашивает не против-ли Моника если он ее позовет?
# Моника надменно говорит что не против, зови свою жалкую секретаршу.
    img 12541
    m "Ладно. Я поговорю с твоей Джейн..."
    img 12542
    steve "Моника, ты не против если я позову ее?"
    img 12543
    m "Я не против."
    m "Зови свою жалкую секретаршу..."

# Заходит Джейн. Стив говорит что у него для Джейн большой сорприз.
# Миссик Бакфетт решила оказать любезность и удовлетворить твое любопытство, касаемо ее фигуры.
# Миссис Бакфетт готова ответить на все твои вопросы и даже показать свою грудь.
    img 12544
    jane "Мистер Стив?"
    img 12545
    steve "Джейн!"
    steve "У меня для тебя большой сюрприз!"
    img 12546
    steve "Миссис Бакфетт готова ответить на все твои вопросы!"
    steve "И даже показать свою грудь!"
    steve "Помнишь, ты очень интересовалась ей?"

# Моника в шоке!!!
# Джейн тоже в шоке.
    img 12547
    m "!!!"
    mt "ГРУДЬ?!"
    img 12548
    jane "???"


# Стив говорит Джейн что она может идти, Миссис Бакфетт скоро придет к ней.
# Джейн удивленная уходит.
    img 12549
    steve "Джейн, ты можешь идти."
    steve "Миссис Бакфетт скоро придет к тебе."
    img 12550
    jane "..."

# Моника кричит на Стива: ПОКАЗАТЬ ГРУДЬ?!
# А задницу мне ей не надо показать, Стив?!
# Ты совсем сошел с ума?! Как у тебя хватает наглости говорить такое в отношении меня, Моники Бакфетт?!
    img 12551
    m "ПОКАЗАТЬ ГРУДЬ?!"
    m "А задницу мне ей не надо показать, Стив?!"
    img 12552
    m "Ты совсем сошел с ума?!"
    m "Как у тебя хватает наглости говорить такое в отношении меня, Моники Бакфетт?!"

# Стив отвечает что пусть Моника не злится. Джейн очень интересовалась грудью Моники, потому он и решил так сказать.
# Что просто разговор вряд-ли отвлечет ее от того, что она наседает на Стива.
    img 12553
    steve "Моника, пожалуйста, не злись!"
    steve "Джейн действительно очень интересовалась твоей грудью."
    img 12554
    steve "Потому я и решил так сказать."
    steve "Обычный разговор вряд-ли отвлечет ее от того, что на принялась наседать на меня."

# Выбор Моники: промолчать, угрожать Стиву тем, что Джейн может узнать про контракты.
    img 12555
    menu:
        "Промолчать...":
            pass
        "Угрожать Стиву тем, что Джейн может узнать про контракты.":
# Моника говорит что не собирается ничего показывать Джейн.
# Зато она может рассказать Джейн, чем Стив занимается здесь, пока она ждет свадьбы.
# Стив отвечает, что Моника имеет ввиду наши контракты?
# Моника, ты правда хочешь чтобы твоя репутация была так подмочена?
# К тому же, если Джейн решит уйти, ее место займет быстро займет ее подружка Тиффани. Она давно метит туда.
# Джейн мне уже поднадоела, зато Тиффани я смогу трахать сколько хочу.
# Моника говорит Стиву что он самый большой мерзавец, которого она знает.
            img 12556
            m "Я не собираюсь ничего показывать Джейн."
            img 12557
            m "Зато я могу рассказать ей, чем ты занимаешься здесь!"
            m "Пока она ждет вашей свадьбы..."
            img 12558
            steve "Моника, ты имеешь ввиду наши контракты?"
            steve "Ты правда хочешь, чтобы твоя репутация была так подмочена?"
            img 12559
            m "!!!"
            img 12560
            steve "..."
            steve "К тому же, если Джейн решит уйти, я поставлю на ее место Тиффани."
            steve "Она давно метит туда..."
            img 12561
            steve "Джейн мне уже поднадоела."
            steve "Зато Тиффани я смогу трахать сколько захочу!"
            img 12562
            m "Стив..."
            m "Ты самый большой мерзавец, которого я знаю..."

# Стив говорит что если Моника хочет, она может отказаться от этого контракта, но, в таком случае,
# других контрактов тоже не будет.
    img 12563
    steve "Моника, ты можешь отказаться от этого контракта."
    steve "Но, в таком случае, наша деловая цепочка будет разорвана."
    steve "И других контрактов тоже не будет..."
# Моника зло спрашивает: ты имеешь ввиду эти унизительные контракты,
# во время которых мне приходится сосать твой гребаный член у тебя под столом?!
    img 12564
    m "Ты имеешь ввиду эти унизительные контракты?"
    m "Во время которых мне приходится сосать твой гребаный член у тебя под столом?!"
# Стив отвечает, что он имеет виду контракты, где за очень легкую работу он платит большие деньги.
# Моника зло смотрит
    img 12565
    steve "Нет, Моника"
    steve "Я имею ввиду контракты, где за очень легкую и быструю работу я плачу больше деньги..."
    img 12566
    m "!!!"
# выбор Моники
# Уйти, либо Согласиться, либо Предложить показать грудь Стиву вместо Джейн (corruption)
    img 12567
    menu:
        "Согласиться.": #corruption
            img 12568
            m "Хорошо, Стив..."
            m "Мерзавец..."
            m "Я сделаю это..."
        "Предложить показать свою грудь Стиву, вместо Джейн": #corruption
# Если Моника выбирает показать грудь.
# Моника говорит Стиву что если он так хочет, то она может показать ему грудь, вместо это дуры Джейн.
# Стив отвечает Монике что не хочет этого делать, т.к, уже видел ее киску и кончал в нее.
# А в женщине должна оставаться какая-то загадка, иначе он может потерять интерес к ней.
# А кроме груди, у Моники есть только ее маленькая девственная дырочка в попе.
# Если Моника хочет, она может остаться для него единственной загадкой в Монике как в женщине.
            img 12569
            m "Стив, если уж ты так хочешь, то давай я покажу свою грудь тебе!"
            m "Вместо этой дуры Джейн!"
            img 12570
            steve "Моника, я не хочу этого делать."
            steve "Я уже видел твою киску."
            # если был контракт cum
            steve "Я уже видел твою киску и даже кончал в нее..."
            #
            steve "А в женщине должна оставаться какая-то загадка."
            img 12571
            steve "Иначе я могу потерять интерес к ней."
            steve "А, кроме груди, у тебя, Моника, есть только твоя маленькая девственная дырочка в попе."
            steve "Если ты захочешь, это останется для меня единственной загадкой в тебе как в женщине."

# Моника злится, переживает, кладет руки на попу, как-бы защищая ее. И говорит:
# Я... Я лучше покажу грудь Джейн...
            img 12572
            w
            img 12573
            m "Я... Я лучше покажу грудь Джейн..."

        "Уйти.":
# Если уходит, то говорит что она в аду видела его дурацкие контракты,
# Стив отвечает что он порядочный бизнесмен и ждет Монику снова
            img 12574
            m "Иди к черту со своими контрактами, Стив!"
            steve "Моника, я порядочный бизнесмен!"
            steve "И жду тебя снова!"
            return False

# Стив говорит что отлично, Моника может следовать к Джейн, та уже заждалась ее!
# Моника злая уходит.
    img 12575
    steve "Отлично!"
    steve "Ты можешь следовать к Джейн."
    steve "Она уже заждалась тебя!"
    img 12576
    m "!!!"
    return True

label ep26_dialogues2_steve2:
# Если Моника отказалась от контракта с Джейн
# С этих пор, если Моника приходит к Стиву и пытается заключить контракт, то Стив говорит ей, что у
# них сейчас нет деловых отношений и что Моника знает что сделать, чтобы их возобновить.
    img 12577
    steve "Моника."
    steve "У нас сейчас нет деловых отношений."
    steve "Но ты знаешь что надо сделать, чтобы возобновить их!" # Подмигивает
    return

label ep26_dialogues2_steve3:
# Приходит к Джейн.
# Джейн с улыбкой смотрит на Монику.
# Моника говорит чтобы Джейн встала, когда перед ней стоит ее Босс!
# Джейн встает.
    img 12578
    jane "Миссис Бакфетт?"
    img 12579
    m "!!!"
    img 12580
    jane "..."
    img 12581
    m "Джейн!"
    m "Встань, когда перед тобой стоит твой Босс!"
    img 12582
# Моника надменно спрашивает что Джейн хочет узнать у Моники по поводу ее великолепной фигуры?
# Джейн спрашивает как Монике удалось достичь такой превосходной формы?
# Моника отвечает что все дело в правильном питании и регулярном занятии фитнессом.
# Джейн спрашивает, можно-ли ей рассмотреть Монику поближе.
# Моника надменно отвечает что не видит в этои необходимости, но так уж и быть.
# Джейн спрашивает у Моники чем она питается в данный момент? Какая сейчас лучшая диета?
    img 12583
    m "Итак..."
    m "Что ты хочешь узнать относительно моей великолепной фигуры?"
    img 12584
    jane "Миссис Бакфетт, скажите, как Вам удалось достичь такое превосходной формы?"
    img 12585
    m "Все дело в правильном питании регулярном занятии фитнесом."
    img 12586
    jane "Миссис Бакфетт, можно-ли мне рассмотреть Вашу фигуру поближе?"
    img 12587
    m "Я не вижу в этом особой необходимости..."
    img 12588
    jane "..."
    img 12589
    m "Но, так уж и быть!"
    #Джейн подходит и осматривает Монику
    img 12590
    w
    img 12591
    w
    img 12592
    jane "Миссис Бакфетт, скажите, чем Вы питаетесь в данный момент?"
    jane "Какая сейчас лучшая диета?"

# Моника сконфужена...
# Чем я питаюсь? Моя диета?
# Да уж! Я боюсь что эта толстая корова не сможет выжить на моей сегодняшней диете...
    img 12593
    mt "Чем я питаюсь?"
    mt "Моя диета?"
    mt "Да уж!"
    mt "Я бобсь что эта толстая корова не сможет выжить на моей сегодняшней диете..."

# Моника отвечает что за ее рационом следит известный доктор, который скурпулезно составляет необходимые вещества.
# В общем, Джейн. Ты себе такого позволить не сможешь. Если есть другие вопросы, то задавай скорее и закончим.
    img 12594
    m "За моим рационом следит известный доктор!"
    m "Который скурпулезно составляет список блюд, содержащих необходимые вещества и витамины."
    img 12595
    m "В общем, Джейн."
    img 12596
    jane "..."
    img 12597
    m "Ты себе такого позволить не сможешь."
    m "Если есть другие вопросы, то задавай скорее и закончим с этим."

# Джейн обсматривает Монику.
    img 12598
    w
    img 12599
    w
    img 12600
    jane "..."
    img 12601
    m "..."

# Миссик Бакфетт, Вы говорили что-то по поводу фитнесса.
# Да, Джейн. Фитнесс и йога - неотъемлемая часть построения изящной фигуры...
    img 12602
    jane "Миссис Бакфетт."
    jane "Вы говорили по поводу фитнеса..."
    img 12603
    m "Да, Джейн."
    m "Фитнес и йога - неотъемлемая часть построения изящной фигуры..."

# Джейн спрашивает в какой фитнесс-центр сейчас ходит Моника и может-ли она помочь ей тоже устроиться туда на занятия.
# Моника отвечает что с ней занимается личный тренер, который внешне соответствует здоровому образу жизни.
# А также знает толк в упражнениях для достижения нужной цели.
    img 12604
    jane "Миссис Бакфетт."
    jane "А в какой фитнес-центр Вы сейчас ходите заниматься?"
    img 12605
    jane "Могли-бы Вы мне помочь тоже устроиться туда на занятия?"
    img 12606
    m "Со мной занимается личный тренер, которые внешне соответствует здоровому образу жизни."
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
    m "Фитнес-центр, куда я хожу - только для элитных девушек, имеющих положение в обществе!"
    m "И туда можно попасть только по приглашению."
    img 12610
    jane "..."
    img 12611
    m "И, разумеется, я не собираюсь давать это приглашение для тебя, Джейн!"

# Моника думает про себя, что ей не хватало еще в фитнесс центре Джейн или этой проститутки Тиффани.
# Учитывая как Бетти обращается с Моникой там, не будет ничего хорошего если эти дуры станут свидетелями этого.
    img 12612
    mt "Еще мне не хватало в фитнес-центре Джейн или этой проститутки..."
    mt "Как ее там..."
    mt "Тиффани..."
    img 12613
    mt "!!!"
    mt "Учитывая, как Бетти обращается со мной там, не будет ничего хорошего если эти дуры станут свидетелями этого..."

# Джейн обиженно смотрит.
# Джейн говорит: Миссис Бакфетт.
    img 12614
    jane "..."
    jane "Миссис Бакфетт..."

# Моника прерывает. Джейн! Ты еще не закончила со своими дурацкими вопросами?!
# Я оказываю безмерную услугу Стиву тем, что согласилась ответить на несколько вопросов для его будущей супруги.
# Но ты начинаешь меня утомлять, Джейн!
# Давай заканчивай!
# Моника думает (я хочу побыстрее пообедать в дорогом ресторане!)
    img 12615
    m "Джейн! Ты еще не закончила со своими дурацкими вопросами?!"
    m "Я оказываю безмерную услугу Стиву тем, что согласилась ответить на несколько вопросов для его будущей супруги."
    img 12616
    m "Но ты начинаешь меня утомлять, Джейн!"
    m "Давай заканчивай!"
    img 12617
    mt "Мне надоела эта Джейн!"
    mt "Я хочу побыстрее пообедать в дорогом ресторане!"

# Джейн говорит: Миссис Бакфетт. Мистер Стив сказал что Вы покажете мне свою грудь...
# Моника шипит. Джейн, ты не перегибаешь палку?!
# Джейн отвечает, Миссис Бакфетт, простите! Просто так сказал Мистер Стив!...
# Я не хотела как-то оскорбить Вас!
    img 12618
    jane "Миссис Бакфетт..."
    jane "Мистер Стив сказал, что Вы покажете мне свою грудь..."
    img 12619
    mt "!!!"
    img 12620
    m "Джейн! Ты не перегибаешь палку?!"
    img 12621
    jane "Миссис Бакфетт, простите! Просто так сказал Мистер Стив!..."
    jane "Я не хотела как-то оскорбить Вас!"

# выбор Моники:
# показать грудь
# не показывать грудь (нарушение контракта)
    img 12622
    menu:
        "Показать грудь":
            pass
        "Не показывать грудь (нарушение контракта)":
# Моника не показывает грудь:
# Моника говорит что не собирается ничего показывать Джейн. Достаточно и так!
            img 12623
            m "Я не собираюсь ничего показывать, Джейн!"
            m "Достаточно и так!"

# После этого, Моника возвращается к Стиву закрыть контракт.
# Моника говорит Стиву что сделала как они договорились и она ждет тикет на ланч в ресторане.
            img 12645
            m "Стив!"
            m "Я достаточно рассказала твоей невесте, как мы договорились."
            img 12646
            m "Я жду сертификат на ланч в ресторане."

# Если Моника не показала грудь Джейн, то Стив заявляет что Моника нарушила контракт и не показала грудь.
# За это полагается неустойка, в виде одного бесплатного контракта на массаж его члена.
# Моника злится и говорит чтобы Стив пошел к черту со своими контрактами!
            img 12647
            steve "Моника, но ты не показала свою грудь Джейн!"
            steve "Ты нарушила контракт!"
            img 12648
            steve "За это полагается неустойка в виде бесплатного контракта на массаж моего члена, хе-хе!"
            img 12649
            m "Иди ты к черту со своими контрактами!!!"
            return False

# Моника говорит что Стив умолял Монику сделать это.
# К тому же, Монике есть чем гордится и она, так уж и быть, сделает это.
# Моника показывает грудь Джейн.
    img 12624
    mt "!!!"
    img 12625
    jane "..."
    img 12626
    m "Ладно..."
    m "Стив умолял меня сделать это..."
    img 12627
    jane "..."
    img 12628
    m "К тому же, мне есть чем гордиться."
    m "И я, так уж и быть, сделаю это..."

# Моника показывает грудь.
    img 12629
    w
    img 12630
    w
    img 12631
# Джейн спрашивает, а они настоящие? можно-ли потрогать?
# выбор Моники: Можно потрогать или не дать трогать грудь
    img 12632
    jane "Миссис Бакфетт, а они настоящие?"
    jane "Можно потрогать?"
    img 12633
    menu:
        "Дать потрогать свою грудь.":
# Если дает потрогать, то:
# Моника шипит: Можно, только быстро, Джейн!
# Джейн трогает грудь
# Моника закрывается и говорит что довольно.
            img 12634
            m "Можно, только быстро, Джейн!"
            img 12636
            w
            img 12635
            w
            img 12637
            mt "Как же мне противно!"
            img 12638
            jane "..."
            img 12639
            m "Довольно!"

        "Не дать потрогать свою грудь.":

# Моника говорит что нельзя потрогать грудь:
# Моника шипит и говорит Джейн что только попробуй!
# Джейн ошеломленно отвечает что просто хотела проверить, настоящие они или нет?
# Моника отвечает что они настоящие, как и сама Моника, в отличие от Джейн, которая является лишь тенью Стива.
            img 12640
            m "Только попробуй!"
            img 12641
            jane "Простите, Миссис Бакфетт."
            jane "Я только хотела проверить, настоящие они или нет..."
            img 12642
            m "Они настоящие, как и я сама!"
            m "В отличие от тебя Джейн!"
            img 12643
            m "Ты являешься лишь тенью Стива!"
# Джейн обиженно смотрит.
            img 12644
            jane "!!!"


# Если Моника показала грудь Джейн, то Стив дает тикет на ланч в ресторане (предмет)
    img 12650
    m "Стив!"
    m "Я достаточно рассказала твоей невесте, как мы договорились."
    img 12651
    m "Я жду сертификат на ланч в ресторане."

    # Стив кладет сертивикат
    img 12652
    steve "Моника!"
    steve "Ты жестокая женщина!"
    img 12653
    steve "Сначала ты оставила меня без денег, а теперь оставляешь и без еды!"
    # Моника уходит
    img 12654
    m "Не забывай при каких обстоятельствах это происходило!"
    m "Ты еще ответишь за все, что сделал!"
    return


label ep26_dialogues2_steve4:
# В дальнейшем, если висит неустойка, то при заключении контракта со Стивом:
# Стив говорит что на Монике висит неустойка и этот раз будет бесплатным.
# Моника шипит что не собирается делать это за бесплатно!
# Стив отвечает что это свободная страна и Моника может заключать любой контракт, либо не делать этого.
    img 12655
    steve "Моника, ты помнишь про неустойку, которая все еще не погашена тобой?"
    steve "Этот раз будет бесплатным!"
    img 12656
    m "Я не собираюсь делать эти мерзости за бесплатно!"
    img 12657
    steve "Моника, это свободная страна."
    steve "И ты можешь заключать любой контракт..."
    #улыбается
    img 12658
    steve "Либо не делать этого..."

# выбор Моники:
# Согласиться компенсировать неустойку
# Уйти
    img 12659
    menu:
        "Согласиться компенсировать неустойку":
            pass
        "Уйти.":
            # уходит
            img 12660
            m "Иди к черту со своими неустойками, Стив!"
            return False

# Если Моника соглашается:
# Стив. Если я сделаю это бесплатно, то в следующий раз ты точно заплатишь?
# Стив отвечает что конечно, Моника. Он честный бизнесмен и тд.
    img 12661
    m "Стив..."
    #улыбается
    img 12662
    steve "Да, Моника?"
    img 12663
    m "Стив, если я сделаю это бесплатно, то в следующий раз ты точно заплатишь?"
    img 12664
    steve "Конечно, Моника!"
    steve "Я честный бизнесмен и всегда плачу по своим контрактам!"

    #переход на контракт

# В конце Стив говорит что неустойка компенсирована сполна.
# Что Стив ждет Монику для новых контрактов.
    img 12665
    steve "Неустойка компенсирована сполна."
    steve "Я жду тебя для новых контрактов, Моника!"
    return






label ep26_dialogues2_steve5:

# К сценам контракта со Стивом добавляется сцена, где Бетти приходит к нему.
# Только вторник и четверг (посещение фитнеса)
# Бетти заходит.
# Если первый раз:
# Заходит с Джейн
# Стив удивлен, здоровается с Бетти.
# Говорит что удивлен увидеть ее здесь
# Бетти говорит что Ральф заболел и остался дома, но ему нужно передать отчеты для Стива.
# Ральф очень переживает из-за того что отчеты окажутся у Стива невовремя.
# Поэтому он послал Бетти для того, чтобы отвезти их.
    img 12666
    jane "Мистер Стив, к Вам пришла некая Миссис Робертс."
    jane "Она говорит что пришла от Мистера Ральфа."
    img 12667
    jane "Также она говорит что Вы ее знаете..." # Смотрит прищюренно и подозрительно
    img 12668
    steve "..."
    img 12669
    jane "!!!"
    img 12670
    jane "Она говорит что ее супруг заболел и остался дома, а она привезла Вам его отчеты."
    img 12671
    steve "Ах, Бетти..."
    steve "Да, Джейн! Я знаю ее."
    img 12672
    steve "Это супруга Ральфа, он работает в нашей компании."
    steve "Ты должна быть знакома с ним."
    img 12673
    jane "..."
    img 12674
    steve "..."
    img 12675
    steve "Бетти!"
    steve "Разве у Стива нет подчиненных, чтобы доставить отчеты?"
    steve "К чему заставлять себя ехать через весь город?"
    img 12676
    betty "Ральф взял их с собой домой, чтобы проверить их и привезти сегодня тебе."
    img 12677
    steve "Бетти, у Вас есть отличная гувернантка!"
    steve "Ты бы могла поручить это ей!"
    img 12678
    betty "Если ты говоришь про ту нерадивую гувернантку, которую Ральф откуда-то подобрал..."
    betty "То я не доверяю ей даже стирать одежду и готовить еду!"
    img 12679
    steve "Правда? А мне показалось, что ей можно доверить самое ценное что у меня есть..."
    # Моника смотрит на член Стива и злится
    img 12680
    w
    img 12681
    betty "Стив, это мое дело, кому доверять, а кому нет!"
    betty "Я пришла для того, чтобы передать отчеты!"
    betty "Я согласилась на это только потому, что сегодня посещала фитнес в городе."
    img 12682
    betty "И нашла минуту, чтобы помочь моему супругу."
    betty "Вот отчет, Стив!"
    betty "А я поехала назад к своему мужу!"
    img 12683
    steve "Бетти, постой!"
    steve "Джейн, все в порядке, ты можешь идти."
    steve "Сейчас я проверю отчеты и отпущу Миссис Робертс."
    img 12684
    jane "Хорошо, Мистер Стив."
    jane "Позовете меня, если что-то потребуется."

    # Джейн уходит
    img 12686
    w
    img 12685
    betty "Что тебе надо, Стив?!"
    betty "Я принесла отчеты и уже тороплюсь!"

    # Стив встает, у него спущены штаны и стоит член
    img 12687
    steve "Ах, Бетти!"
    steve "Моя любимая Бетти!"
    steve "Я так рад что ты пришла ко мне!"
    img 12688
    betty "Стив, почему ты без штанов?!"
    img 12689
    steve "Я ждал тебя, Бетти! Я так ждал тебя!"
    img 12690
    betty "Стив, надень штаны!"
    betty "Или я ухожу!"
    img 12691
    steve "Бетти, ты не можешь уйти!"
    steve "Посмотри!"
    img 12692
    steve "Посмотри, как я соскучился по тебе!"
    steve "Неужели ты не видишь, Бетти?"
    img 12693
    w
    img 12707
    w
    img 12708
    betty "..."
    img 12694
    steve "..."
    img 12695
    betty "Стив, я тороплюсь!"
    img 12696
    steve "Бетти, подойди ко мне!"
    steve "Подойди ко мне поближе, скорее, Бетти!"

    # Бетти подходит и берет Стива за член
    img 12697
    betty "Стив, я не понимаю, чего ты от меня хочешь?"
    betty "Я же ясно сказала тебе, что тороплюсь!"
    img 12709
    w
    img 12710
    mt "!!!"
    img 12698
    betty "Меня дома ждет муж!"
    img 12699
    steve "Ах, Бетти!"
    steve "Я хочу тебя! Хочу твою попку!"
    img 12711
    w
    img 12712
    w
    img 12700
    steve "Мысль о том, что ты только что тренировала ее на фитнесе, возбуждает меня!"
    # Стив задирает юбку Бетти
    img 12701
    steve "Ты тренировала ее для меня!"
    steve "Для моего члена!"
    img 12713
    w
    img 12714
    w
    img 12702
    steve "Для того, чтобы я вогнал его в твою попку!"
    steve "В твою аппетитную попку, Бетти!"
    img 12703
    betty "..."
    img 12715
    w
    img 12716
    w
    img 12704
    betty "Я не хочу изменять мужу, Стив!"
    img 12705
    steve "Скорее! Cкорее, Бетти, повернись!"
    steve "Дай я вгоню в тебя свой член!"
    img 12717
    w
    img 12718
    w
    img 12706
    betty "!!!"
    betty "..."
    # Бетти снимает трусы
    img 12719
    w
    img 12720
    w
    img 12721
    betty "Ладно, Стив."
    betty "Только быстро!"
    img 12722
    w
    img 12723
    betty "Меня дома ждет муж!"
    # бросает их перед Моникой возле стола
    img 12724
    w
    img 12725
    betty "Стив, куда мне деть мои трусики?"
    img 12726
    w
    img 12727
    steve "Бетти, давай их сюда!"
    img 12728
    w
    img 12729
    mt "Знакомые трусики..."
    mt "Черт! Это точно сучка Бетти!"
    img 12730

    #video
    steve "Да, Бетти! Да!"

    steve "Твоя попка, Бетти!"

    steve "Она бесподобна!"
    steve "ААААААААХХХ!"

    betty "Черт, Стив! Ты снова кончил в меня?!"

    mt "Снова?!"

    steve "Бетти, это всего-лишь твоя попка!"
    steve "Не волнуйся!"

    mt "Дьявол! Эта Бетти совсем обнаглела!"
    mt "Она смеет трахаться прямо в кабинете у Стива!"
    mt "Да еще и при мне!"

    mt "!!!"
    mt "Если я скажу об это Ральфу, Барди донесет на меня Маркусу, черт!"
    mt "Он предупреждал меня и, как я уже убедилась, он не врет..."
    mt "Может быть рассказать Барди про эту сучку?"
    mt "..."
    mt "Нет, не стоит..."
    mt "Этот маленький сопляк использует это для своих целей."
    mt "И заставит Бетти потребовать от меня ходить по дому голой!"
    mt "Я уверена!"

    # Бетти одевает трусы
    betty "Все, Стив!"
    betty "Я пошла!"

    # fade
    img 12731
    m "Стив! Ты совсем обнаглел!"
    m "Ты трахаешь шлюх прямо у меня на глазах!"
    img 12732
    m "Ты поплатишься за такую наглость!"
    m "Я... Я!!!"
    img 12733
    steve "Моника, я знаю, ты собираешься убить меня..."
    img 12734
    m "Я не просто убью тебя, Стив!"
    m "Я сделаю это с особой жестокостью!"
    img 12735
    m "Я сделаю тебя ничтожеством! Ты будешь побираться на улицах до конца своих никчемных дней!"
    img 12736
    steve "Моника, но за что?!"
    steve "Я честный бизнесмен! Я облегчил тебе выполнение контракта!"
    img 12737
    steve "Вместо того, чтобы кончить в твой ротик, я кончил в зад другой женщины."
    steve "Или ты хочешь, чтобы я отдал эти деньги ей?"
    img 12738
    m "ЭТО МОИ ДЕНЬГИ! МОИ!!!"
    img 12739
    steve "Но ты нарушила условия сделки! Моя сперма только что ушла отсюда!"
    steve "Сделка не закрыта!"
    img 12740
    m "Как, по твоему, я могла закрыть эту сделку?!"
    m "Ты кончил в задницу этой шлюхи!"
    img 12741
    m "Ты сделал это сам!"
    img 12742
    steve "Моника, сперма очень долго висела перед твоим лицом, я видел это!"
    steve "У тебя были все возможности проглотить ее!"

    # выбор:
    # уйти без денег или наехать на Стива. В зависимости от сучности
    img 12743
    menu:
        "Уйти без денег.":
            # Если уходит без денег
            img 12744
            m "Ты мерзавец, Стив!"
        "Разозлиться на Стива.":
            pass

    # Наехать на Стива
    # Моника злая, подходик к Стиву
    # +bitchiness
    img 12745
    m "Стив..."
    m "Повтори еще раз..."
    img 12746
    m "Значит ты..."
    m "Хотел..."
    img 12747
    m "Чтобы я проглотила твою гребаную сперму..."
    m "Сперму, которая..."
    img 12748
    m "Вытекла из задницы Бетти?!"
    img 12749
    steve "..."
    # Моника берет Стива за яйца
    img 12750
    m "Кажется, моему терпению пришел конец, Стив!"
    m "Мне неважно что со мной будет. Я убью тебя и оторву твои яйца..."
    img 12751
    steve "Моника! Контракт закрыт!"
    steve "Пожалуйста! Я же пошутил!"
    img 12752
    w
    img 12753
    m "Еще раз пошути так, Стив..."
    m "И останешься без своих яиц..."
    m "Тебе понятно?!"
    img 12754
    steve "Да, Моника! Пожалуйста!"
    steve "Успокойся! Не надо злиться!"
    img 12755
    steve "Отпусти мои... Отпусти меня и я переведу деньги немедленно!"
    # Моника разжимает руку
    img 12756
    w
    img 12757
    m "Я отпустила твои яйца, Стив..."
    img 12758
    steve "..."
    img 12759
    m "На этот раз..."
    # Моника уходит
    img 12760
    m "Но не расчитывай на это снова!"


    return
    11232-12761
    w
    11233-12762
    w
    11234-12763
    w
    11235-12764
    w
    11236-12765
    w
    11237-12766
    w
    11238-12767
    w
    11239-12768
    w
    11240-12769
    w
    11241-12770
    w
    11242-12771
    w
    11243-12772
    w
    11244-12773
    w
    11245-12774
    w
    11246-12775
    w
    11247-12776
    11248-12777
    11249-12778
    11250-12779
    11251-12780
    11252-12781
    11253-12782
    11254-12783
    11255-12784
    11256-12785
    11257-12786
    11258-12787
    11259-12788
    11260-12789
    11261-12790
    11262-12791
    11263-12792
    11264-12793
    11265-12794
    11266-12795
    11267-12796
    11268-12797
    11269-12798
    11270-12799
    11271-12800
    11272-12801
    11273-12802
    11274-12803
    11275-12804
    11276-12805
    11277-12806
    11278-12807
    11279-12808
    11280-12809
    11281-12810
    11282-12811
    11283-12812
    11284-12813
    11285-12814
    11286-12815
    11287-12816
    11288-12817
    11289-12818
    11290-12819
    11291-12820
    11292-12821
