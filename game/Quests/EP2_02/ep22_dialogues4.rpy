# Бетти:
# Если Бетти прокачана до ур.3, то она предлагает Монике сходить на фитнесс. Разрешает ей не убираться в этот день.
# Потом фитнесс активируется через 3 дня. Если сегодня фитнеса нет, то Бетти говорит что я пойду на днях.

# На фитнесе в первый раз Моника в шоке что это тот фитнесс где занимается она.
# Приходит туда, там Стефани и Ребекка. Моника в шоке, общается с ними и с Бетти.
# Пускает пыль в глаза что это все специально, девочки, вы потом удивитесь тому что я задумала.
# Те удивляются и идут заниматься
# Сцена занятия

# В конце Стефани обнаженная пристает к Ребекке. Та ее отшивает

# Заходит Бетти и говорит Монике ждать на улице. Моника ждет час.

# При повторе, Стефани и Ребекка спрашивают у Моники что когда она закончит свое приключение? Та отвечает что скоро.
# Они удивляются и идут заниматься.
# При входе Моники они обнаженные (только повтор) У Ребекки зад показан не совсем.
# Одеваются и идут заниматься

# Бетти также говорит Монике ждать на улице.

# Бетти качается фитнесом также как и уборкой и достигает ур.4. На этом все


# Если Бетти прокачана до ур.3, то она предлагает Монике сходить на фитнесс. Разрешает ей не убираться в этот день.
# Потом фитнесс активируется через 3 дня. Если сегодня фитнеса нет, то Бетти говорит что я пойду на днях.
label ep22_dialogues4_1:
    # Если Бетти ур.3
    img 6018
    with fade
    betty "Моника, гувернантка."
    img 6019
    "Как я выгляжу?"
    img 6020
    "Тебе нравится?"
    img 6021
    mt "!!!"
    img 6022
    m "Да, Мэм. Вы выглядите великолепно."
    img 6023
    betty "Да, получше чем ты!"
    img 6024
    # Если фитнесс сегодня есть:
    if bettyFitnessToday == True:
        img 6029
        betty "Моника, я могу взять тебя с собой на фитнесс."
        "Покажу тебе что надо делать, чтобы выглядеть так как Я."
        "Понесешь мои вещи."
        "Ты можешь наблюдать за мной, возможно, даже я куплю тебе однажды абонемент туда..."
        menu:
            "Согласиться...":
                img 6028
                m "Да, Миссис Робертс, я готова."
                img 6027
                betty "Хорошо, ты можешь переодеться, только не в свои грязные тряпки, как у проститутки!"
                img 6029
                m "Миссис Робертс, я могу поехать в униформе, если Вы разрешите..."
                betty "Хорошо, можешь ехать в униформе."
                "В конце концов, ты прислуга и это стоит подчеркивать!"
                img 6025
                mt "!!!"
                img black_screen
                with Dissolve(1.0)
                pause 1.0
                sound snd_car_turn_on
                img 8531
                with fade
                w
                img 8532
                sound snd_car_engine
                pause 2.0
                img scene_Map
                with fade
                w
                return True
            "Отказаться.":
                img 6028
                m "Миссис Робертс. Простите. Я планировала еще заняться пятном на ковре..."
                betty "Хорошо, Моника, занимайся..."
                return False
    else:
        # Если фитнеса сегодня нет
        img 6029
        betty "Я собираюсь поехать на фитнесс на днях. Если ты хочешь, я смогу взять тебя с собой."
        betty "Он {c}по вторникам и четвергам{/c}"
        betty "Напомни мне."
        img 6028
        m "Да, Миссис Робертс. Хорошо..."
    return False


label ep22_dialogues4_1a:
    # На улице. Водитель Фред, Бетти и Моника. Первый раз
    if ep22_quest_flag1 == False:
        $ ep22_quest_flag1 = True
        mt "О БОЖЕ!!!"
        "Это же фитнесс-зал куда я ходила!!!"
        "Мне нельзя туда в таком виде!!!"
        betty "Моника, гувернантка, почему ты отстаешь от меня?"
        "Поторопись! За мной!"
    return

label ep22_dialogues4_2:
    # повтор
    betty "Моника, гувернантка, почему ты отстаешь от меня?"
    "Поторопись! За мной!"
    return
label ep22_dialogues4_2a:
    # повтор
    betty "Моника, гувернантка, почему ты отстаешь от меня?"
    "Поторопись! За мной!"
    return False

label ep22_dialogues4_3:
    # Зал фитнеса, autorun первый раз
    mt "Черт! Этот инструктор!"
    "Мне надо как-то повернуться, чтобы он не узнал меня!"

    fitness_instructor "Добрый день, Миссис Робертс!"
    "Вы сегодня выглядите очаровательно."

    betty "Ой, спасибо!"
    "Ты заставляешь краснеть меня!"

    mt "Эта сучка что, флиртует с ним?!"
    return

label ep22_dialogues4_4: #клик по Бетти ил иниструктору в фитнесс-зале
    mt "Эта сучка что, флиртует с ним?!"
    return False

label ep22_dialogues4_5:
    # Моника заходит в раздевалку, там Стефани и Ребекка
    mt "ДЬЯВОЛ!!!"
    "Эти дуры здесь, как всегда!"
    "Мне надо как-то выкрутиться!"
    "Я не могу себе позволить упасть в их глазах!"
    "Мне еще с ними общаться после того как это все закончится!"
    return

label ep22_dialogues4_5a:
    # render
    # Моника подходит к раздевалкам, либо к Стефани и Ребекке
    # первый раз
    #rebecca
    #stephanie
    img 7678
    w
    img 7679
    w
    img 7680
    w
    img 7681
    w
    img 7682
    w
    img 7683
    w
    # Подружки смотрят на нее с удивлением
    img 7684
    w
    img 7685
    w
    img 7686
    w
    img 7687
    betty "Гуверантка! Где моя сумка с униформой?"
    img 7688
    betty "Быстро неси ее сюда!"
    img 7689
    m "Вот Ваша сумка, Миссис Робертс."
    img 7690
    w
    #fade
    img 7691
    sound snd_fabric1
    img 7692
    betty "Гувернантка, ты можешь подождать меня здесь, пока я занимаюсь." #Вид на голую грудь Бетти
    img 7694
    w
    img 7695
    w
    img 7696
    w

    img 7693
    m "Да, Миссис Робертс" # Монику корежит, на нее смотрят

    # Бетти в спортивном
    img 7697
    betty "Можешь посидеть здесь или понаблюдать за мной."

    # Бетти уходит
    img 7698

    #fade
    img 7699
    stephanie "Моника! Что это значит?!"
    stephanie "Почему эта провинциальная дура разговаривает с тобой в таком тоне?!"

    img 7700
    rebecca "И почему ты одета в это?!"
    "Это что, униформа гувернантки?!"
    img 7701
    "Фу! Моника!"
    img 7702
    stephanie "И куда ты пропала?"
    img 7703
    "У нас был девичник и мы не смогли дозвониться до тебя!"
    img 7704
    mt "ЧЕРТ!!!"
    "Я влипла!!!"
    "Я знаю что я очень умная, но как возможно выкрутиться из этого!"
    img 7705
    "Правду говорить им точно не стоит!"
    "Помощи от них не будет никакой!"
    "Они только разболтают об этом всему городу!"
    "ДЬЯВОЛ!!!"

    img 7706
    m "Ой! Девочки!"
    "Пожалуйста, тише!"
    "Не выдавайте меня этой дуре!"
    img 7707
    stephanie "Но почему, Моника!"
    rebecca "Моника, что все это значит?!"
    img 7708
    m "Тсссс! Тише!"
    "Девочки! Я не могу Вам пока рассказать!"
    "Но обзавидуетесь мне, когда потом все узнаете!"
    img 7709
    "Это секретная операция, меня надоумил Дик на нее!"
    "Скоро все будет закончено и я окажусь на первых полосах всех газет!"
    "Вот увидите!"
    img 7710
    "Но сейчас я претворяюсь гувернанткой этой дуры."
    img 7711
    "Ее муж крупный мафиози и мы выведем его на чистую воду!"
    img 7712
    rebecca "Секретная операция, мафиози..."
    "Моника, зачем тебе это все надо?"
    img 7713
    stephanie "Да, Моника!"
    "Я допускаю что Вы играете с Диком в какие-то странные игры."
    "Но зачем позволять так общаться с собой, как делает эта провинциальная дура!"
    img 7714
    m "Ой! Девочки!"
    "Не учите меня жить!"
    "Я испытала гораздо больше удовольствий чем Вы за всю свою жизнь!"
    "И мне становится скучно!"
    "Я хочу разнообразия, адреналина!"
    img 7715
    "Вы живете скучно, девочки!"
    "Я потом расскажу Вам все, Вы обзавидуетесь, обещаю!"
    img 7716
    stephanie "Ну не знаю, Моника... Возможно..."
    "Но обещай что все расскажешь потом!"
    img 7717
    rebecca "Да, Моника! Нам же интересно!"
    img 7718
    m "Конечно, девочки!"
    "Вы же знаете, у меня от Вас нет секретов!"
    img 7719
    rebecca "Хорошо, Моника!"
    "Нам не терпится узнать!"
    img 7720
    stephanie "Моника, а ты придешь на следующий девичник?"
    "Он уже скоро!"
    img 7721
    m "Я подумаю, девочки."
    "Мне это кажется сейчас скучным."
    img 7722
    rebecca "Моника, но мы все-равно будем ждать тебя!"
    img 7723
    stephanie "Моника, приходи!"
    "Заодно расскажешь все!"
    img 7724
    m "Хорошо, девочки."
    "Вы можете идти заниматься..."
    stephanie "Пока, Моника!"
    rebecca "Пока, подружка!"
    m "Пока, девочки!"
    img 7725
    w
    return

label ep22_dialogues4_6:
    #render
    #Сцена занятия йогой.
    #Стефани, Ребекка, Бетти

    #выбор
    img 7755

    #Stephanie - 7756, 7757, 7765, 7766, 7767, 7768, 7780, 7781, 7782, 7783, 7798, 7799, 7800, 7801, 7802, 7803, 7816, 7817, 7818, 7819, 7824, 7825, 7826, 7827, 7828, 7829,
    # 7842, 7843, 7844, 7845, 7846, 7861, 7862, 7863, 7864, 7875, 7876, 7877, 7878, 7879, 7880, 7892, 7893, 7894, 7895, 7896, 7908, 7909, 7910, 7911
    #Rebecca - 7760, 7761, 7762, 7763, 7764, 7784, 7785, 7786, 7787, 7788, 7789, 7790, 7791, 7792, 7793, 7794, 7795, 7796, 7797, 7820, 7821, 7822, 7823, 7830, 7831, 7832,
    # 7833, 7834, 7847, 7848, 7849, 7850, 7851, 7852, 7858, 7859, 7860, 7881, 7882, 7883, 7884, 7885, 7897, 7898, 7899, 7900, 7901, 7902, 7903, 7904, 7912, 7913, 7914, 7915, 7916
    #Betty - 7758, 7759, 7769, 7770, 7771, 7772, 7773, 7774, 7775, 7776, 7777, 7778, 7779, 7804, 7805, 7806, 7807, 7808, 7809, 7810, 7811, 7812, 7813, 7814, 7815,
    # 7835, 7836, 7837, 7838, 7839, 7840, 7841, 7853, 7854, 7855, 7856, 7857, 7865, 7866, 7867, 7868, 7869, 7870, 7871, 7872, 7873, 7874, 7886, 7887, 7888, 7889, 7890, 7891,
    # 7905, 7906, 7907, 7917, 7918, 7919, 7920, 7921, 7922, 7923, 7924, 7925, 7926, 7927, 7928, 7929, 7930

    #Инструктор подходит к Ребекке
    img 7931
    fitness_instructor "Ребекка, давай я помогу тебе..."
    img 7932
    rebecca "Спасибо, не надо..."

    #Инструктор подходит к Стефани
    img 7933
    fitness_instructor "Стефани, давай я помогу тебе..."
    #Если был секс
    img 7934
    stephanie "Муррр..."
    stephanie "Мой тигр хочет помочь мне?..."
    img 7935
    fitness_instructor "Стефани, твой тигр всегда готов придти на помощь!"
    img 7936
    stephanie "Муррр..."
    img 7937
    w
    img 7938
    w

    #Если секса не было
    img 7933
    stephanie "Я предпочитаю помощь от кого-то более сообразительного чем ты..."
    fitness_instructor "Стефани, что я могу сделать?"
    img 7939
    stephanie "Продолжай быть настойчивым..."
    "Хи-хи..."


    #Инструктор подходит к Бетти
    img 7940
    fitness_instructor "Бетти, давай я помогу тебе..."
    betty "Конечно!"
    "С удовольствием!"
    img 7941
    fitness_instructor "Сосредоточься на себе..."
    img 7942
    betty "Хорошо..."
    img 7943
    fitness_instructor "Давай попробуем еще одно упражнение..."
    betty "Хорошо..."
    #fade
    #если первый раз
    img 7944
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

    #если последующие разы
    fitness_instructor "У тебя уже лучше получается, Бетти!"
    betty "Спасибо!"
    fitness_instructor "Останешься сегодня снова на частный урок?"
    fitness_instructor "Тебе надо еще позаниматься..."
    betty "Да, я останусь..."
    #

    img 7951
    stephanie "Эй! Прошу прощения!"
    img 7952
    "Мне тут нужна небольшая помощь в упражнениях!"
    img 7953
    fitness_instructor "Тогда до встречи после занятий, Бетти..."
    img 7954
    betty "До встречи!"

    return

label ep22_dialogues4_7:
    #render
    #Конец занятия йогой, Бетти говорит с Моникой
    img 7726
    betty "Моника, гувернантка, подожди меня на улице, я скоро выйду."
    m "Да, Миссис Робертс..."

    #Сменяется на город
    mt "Черт! Уже прошел час!"
    "Что там делает эта сучка Бетти?!"
    #fade
    betty "Я закончила. Поехали, Фред!"
    fred "Поехали, Мэм!"
    return

# При повторе, Стефани и Ребекка спрашивают у Моники что когда она закончит свое приключение? Та отвечает что скоро.
# Они удивляются и идут заниматься.
# При входе Моники они обнаженные (только повтор) У Ребекки зад показан не совсем.
# Одеваются и идут заниматься

label ep22_dialogues4_8:
    # в раздевалки издалека Стефани и Ребекка обнаженные
    # render
    # Повтор, раздевалка. Стефани, Ребекка, Бетти
    img 7727
    w
    img 7729
    w
    img 7728
    w
    img 7730
    betty "Гуверантка! Где моя сумка с униформой?"
    img 7731
    betty "Быстро неси ее сюда!"

    img 7732
    betty "Что ты там копаешься?!"
    img 7733
    m "Вот Ваша сумка, Миссис Робертс."

    # Бетти уходит в спортивном
    img 7734
    betty "Можешь посидеть здесь или понаблюдать за мной."
    img 7735
    m "Спасибо, Миссис Робертс... Я посижу здесь..."
    img 7736
    w
    #fade
    # Девочки обнаженные
    img 7737
    rebecca "Привет, Моника!"
    img 7738
    stephanie "Моника, когда ты закончишь свое приключение?"
    img 7739
    "Ты знаешь..."
    img 7740
    "Это смешно выглядит со стороны..."
    sound snd_fabric1
    img 7742
    "Хи-хи!"

    img 7741
    rebecca "И когда ты будешь снова заниматься с нами?"
    img 7743 #?
    w
    sound snd_fabric1
    img 7744
    w
    img 7745
    w
    img 7746
    with Dissolve(0.5)
    w
    img 7747
    "Почему ты всю тренировку сидишь здесь?"
    img 7748
    m "Привет, девочки!"
    "Я уже скоро закончу свое приключение."
    img 7749
    "Осталось совсем немного!"
    img 7750
    "Скоро я снова буду заниматься с Вами!"
    img 7751
    stephanie "Ну хорошо... Как-то это все странно..."
    img 7752
    rebecca "Хи-хи"
    img 7753
    w

    mt "СУЧКИ!!!"
    return
# На фитнесе в первый раз Моника в шоке что это тот фитнесс где занимается она.
# Приходит туда, там Стефани и Ребекка. Моника в шоке, общается с ними и с Бетти.
# Пускает пыль в глаза что это все специально, девочки, вы потом удивитесь тому что я задумала.
# Те удивляются и идут заниматься
# Сцена занятия
