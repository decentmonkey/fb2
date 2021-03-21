default melanieVictoriaFitness1 = 0  # Мелани и Виктория посетили первое занятие в фитнес-зале


# при условии, что секс-вечеринка у Мелани уже была
# перед входом в фитнес, у здания
# Мелани и Виктория
# Мелани в голубых шортах и желтой рубашке, Виктория в своем рабочем платье
label ep22_4_dialogues2_fitness_1:
    img 43547
    victoria "Ой, подружка Мелани, я так рада, что мы с тобой вместе идем на фитнес!"
    victoria "Хорошие подружки должны все делать вместе."
    victoria "Не только встречаться на девичниках, но и устраивать совместный шоппинг..."
    victoria "Как мы с тобой сделали, чтобы выбрать тебе костюм."
    img 43548
    victoria "И на фитнес вместе теперь будем ходить!"
    victoria "Ты рада этому, подружка?"
    img 43549
    melanie "Очень..."
    img 43550
    victoria "Я знала, что тебе будет приятно заниматься спортом вместе со мной."
    victoria "И вместе с нашими новыми подружками."
    victoria "Кстати, ты, подружка, отлично справилась с выполнением моей просьбы..."
    victoria "На той вечеринке, когда Стефани была у тебя в гостях."
    victoria "Скоро Стефани тоже станет моей лучшей подружкой. Хи-хи-хи!"
    # если Мелани выключила камеру в самом начале сцены со Стефани
    img 43551
    victoria "Кстати, подружка Мелани... Хотела сказать тебе..."
    victoria "Подружка Мелани сделала не очень хорошо, выключив камеру."
    victoria "Хоть я и осталась довольна, что она сняла для меня достаточно материала."
    #
    img 43552
    melanie "..."
    img 43553
    victoria "Я знаю, что ты не будешь ревновать меня к ней."
    victoria "Ты же хорошая подружка?"
    melanie "Я не буду ревновать..."
    melanie "Потому что я хорошая подружка."
    img 43554
    victoria "Хи-хи-хи!"
    victoria "Ну пошли скорее!"
    victoria "Занятие скоро начнется, а нам с тобой еще нужно переодеться."
    img 43555
    melanie "..."
    return

# фитнес
# Мелани и Виктория заходят, их встречает тренер
label ep22_4_dialogues2_fitness_2:
    # он жадно осматривает Мелани с головы до ног, Викторию как-будто и не замечает
    img 43560
    fitness_instructor "Добрый день, девочки!"
    fitness_instructor "Я ваш фитнес-инструктор."
    # Мелани равнодушно смотрит на него
    melanie "Добрый день."
    img 43561
    fitness_instructor "Добро пожаловать на наше занятие!"
    fitness_instructor "Надеюсь, вам понравится и вы хорошо и с пользой проведете время."
    img 43562
    fitness_instructor "И обязательно вернетесь к нам! И не один раз!"
    # Виктория любезничает с ним
    img 43563
    victoria "Ой, приятно с вами познакомиться!"
    victoria "Я уверена, что мы станем вашими постоянными клиентками!"
    victoria "Меня зовут Виктория."
    img 43564
    victoria "А это моя подружка Мелани."
    # тренер пожирает Мелани глазами, она равнодушно смотрит в сторону
    img 43565
    fitness_instructor "Мне очень приятно!"
    melanie "Взаимно..."
    img 43566
    fitness_instructor "Девочки, проходите в раздевалку."
    fitness_instructor "Она находится вон там." # указывает рукой
    fitness_instructor "И через 10 минут я жду вас в этом зале."
    # Виктория, флиртуя
    img 43567
    victoria "Хорошо. Мы скоро вернемся. Хи-хи-хи!"
    # он смотрит на Мелани, игноря попытки Виктории
    # она это видит и недовольно косится на Мелани
    img 43568
    w
    img 43569
    w
    img 43570
    victoria "!!!"
    # Мелани и Виктория идут в раздевалку, тренер смотрит Мелани вслед
    # затемнение, каблуки
    # смена кадра на раздевалку
    # там, как обычно, тусят Стефани и Ребекка, они переодеваются
    # Виктория подбегает к ним
    img 43571
    victoria "Девочки, мы пришли!"
    # чмокает их в щечку по очереди
    img 43572
    rebecca "Привет, Виктория!" # дружелюбно
    img 43573
    w
    img 43574
    stephanie "Привет..." # прохладно
    img 43575
    victoria "Я так рада, что мы снова встретились!"
    victoria "Так здорово, что мы теперь будем ходить на занятия вместе! Правда?!"
    rebecca "Да, это будет прикольно!"
    # к ним подходит Мелани
    # Стефани сама идет к Мелани и чмокает ее в щечку
    img 43576
    w
    img 43577
    stephanie "Мелани, привет!"
    img 43578
    # отстранясь, смотрит на ее губы и улыбается
    img 43579
    stephanie "Рада видеть тебя..."
    # Мелани, как всегда, с равнодушным видом
    img 43580
    melanie "Привет."
    # Виктория пристально смотрит на то, как Стефани любезничает с Мелани
    ##Можно поставить пожалуйста эмоции Виктории чуть выше
    ## после фразы Стефани "Рада видеть тебя"
    victoria "!!!"
    # Ребекка встревает в разговор и Стефани отходит от Мелани
    img 43582
    rebecca "Привет! Здорово, что вы теперь с нами!"
    rebecca "Будет веселее! Да, Стефани?"
    stephanie "Да, Ребекка."
    img 43581
    w
    img 43583
    rebecca "Переодевайтесь, девочки! Занятие скоро начнется!"
    # Мелани и Виктория отходят к шкафчикам
    # Мелани начинает раздеваться с непроницаемым выражением лица
    # Виктория ехидно на нее оглядывает и тоже начинает снимать платье
    img 43584
    victoria "Подружка Мелани, хорошо, что мы купили тебе костюм для фитнеса."
    victoria "Мне кажется, что тебе в нем будет очень удобно заниматься."
    img 43585
    melanie "Да... Очень..."
    img 43586
    victoria "Я, как твоя лучшая подружка, тебе посоветовала самый лучший вариант."
    melanie "Да, подружка."
    victoria "Мне нравится ходить с тобой на шоппинг и выбирать тебе костюмы."
    victoria "Думаю, из меня получился бы отличный стилист. Да, подружка?"
    img 43587
    melanie "Да."
    img 43588
    victoria "Заодно и у меня появляются обновки. Хи-хи-хи!"
    img 43589
    melanie "!!!"
    # затемнение, шуршание одежды
    # Мелани и Виктория переоделись
    # Стефани и Ребекка в афиге смотрят на костюм Мелани
    img 43590
    w
    img 43591
    w
    img 43592
    rebecca "Ого! Круто!!"
    # Стефани смотрит скорее с вожделением
    img 43593
    stephanie "Мелани, ты, как всегда, на высоте."
    img 43594
    stephanie "Потрясно!"
    img 43595
    # Виктория ехидно улыбается
    img 43596
    victoria "Девочки, прикольный костюм я посоветовала купить Медани?"
    img 43597
    rebecca "О да! Отпад!"
    img 43598
    w
    img 43599
    victoria "Хи-хи-хи!"
    # затемнение
    # девочки выходят в зал
    # тренер смотрит на Мелани, не замечая никого, у него шок
    fitness_instructor "Оооо!"
    fitness_instructor "Я..."
    fitness_instructor "Кхм..."
    # Мелани с каменным лицом проходит мимо него, Виктория следом с ехидной улыбочкой
    melanie "..."
    # Стефани смотрит на тренера, прищурившись, ревниво
    stephanie "!!!"
    # он замечает это и перестает пялиться на Мелани
    fitness_instructor "Девочки, занимайте свои места..."
    fitness_instructor "Начинаем!"
    # Мелани занимается в переднем ряду рядом со Стефани (Мелани на месте Моники)
    # Ребекка с Викторией сзади (Виктория на месте Бетти)
    # во время занятия Стефани периодически бросает на Мелани заинтересованные взгляды, как и Ребекка
    # показываем немного, как каждая из девочек занимается
    # тренер к ним по очереди подходит
    # к Виктории (помогая ей, бросает взгляды на попу Мелани)
    fitness_instructor "Делай вот так, Виктория, выгибай ногу сильнее."
    victoria "Вот так?"
    fitness_instructor "Да, так. Еще сильнее."
    fitness_instructor "Я помогу тебе, надо только немного поддержать..."
    victoria "Ой, мне так больно!"
    fitness_instructor "Терпи, сейчас все пройдет. Я желаю, чтобы ты добилась результатов."
    fitness_instructor "Доверься мне, Виктория."
    victoria "Теперь получается?"
    fitness_instructor "Да, Виктория, ты молодец."
    fitness_instructor "Я вижу в тебе потенциал."
    # к Ребекке
    fitness_instructor "Ребекка, тебе надо держать корпус ровнее..."
    rebecca "Так?"
    fitness_instructor "Еще немного..."
    rebecca "Так лучше?"
    fitness_instructor "Да, у тебя с каждым разом получается все лучше."
    fitness_instructor "Теперь расслабься..."
    fitness_instructor "Вот так, молодец."
    # к Стефани (Виктория посматривает на них подозрительно)
    fitness_instructor "Хорошо, молодец, Стефани."
    fitness_instructor "У тебя отлично получается."
    stephanie "Да, я стараюсь."
    fitness_instructor "Постарайся больше выгибать спинку, Стефани..."
    stephanie "Вот так?"
    fitness_instructor "Умничка. Теперь еще немного... Еще-еще..."
    fitness_instructor "Давай я тебе помогу."
    stephanie "Да, хорошо."
    fitness_instructor "Молодец, Стефани."
    fitness_instructor "Продолжай в том же духе. Я пока помогу другим девочкам."
    # к Мелани (на них все пялятся, а он пожирает взглядом прелести Мелани)
    fitness_instructor "Мелани, ты слишком напряжена, ты чувствуешь это?"
    fitness_instructor "Тебе надо расслабиться. Я помогу."
    fitness_instructor "Вот так. Молодец, Мелани."
    melanie "..."
    fitness_instructor "Теперь тяни ножку, тяни сильнее..."
    fitness_instructor "Тебе не больно?"
    melanie "Немного."
    fitness_instructor "Я помогу тебе, Мелани..."
    fitness_instructor "У тебя получается, ты чувствуешь?"
    melanie "Да, чувствую."
    fitness_instructor "Теперь тянись, тянись как можешь..."
    fitness_instructor "Вот так, хорошо..."
    fitness_instructor "Давай, Мелани, ты можешь еще, я знаю."
    # Виктория ехидно смотрит на Стефани, та ревниво на тренера, который помогает Мелани
    # Виктория ехидно улыбается
    # затемнение
    fitness_instructor "Девочки, на сегодня все!"
    # Ребекка и Виктория улыбаются ему, Мелани равнодушна, Стефани прситально на него смотрит
    fitness_instructor "Вы все молодцы!"
    fitness_instructor "Я очень доволен вашими результатами!"
    fitness_instructor "В следующий раз мы выполним упражнения посложнее."
    # все девочки идут в раздевалку, Стефани позади них и немного задерживается возле тренера, смотрит на него, флиртуя
    stephanie "..."
    # Виктория в это время, пока ее никто не видит, с любопытством выглядывает в зал
    victoria "???"
    # if (у Стефани с тренером секс):
    #
    $ notif(_("Фитнес-тренер любовник Стефани."))
    #
    fitness_instructor "Стефани, я так соскучился по тебе..."
    stephanie "Тихо ты! Нас могут услышать!"
    fitness_instructor "Ну и пусть! Твой Тигр готов провести для тебя персональную тренировку!"
    # он трогает Стефани за попу
    stephanie "Ну хватит! Я не хочу, чтобы кто-то знал!"
    # Виктория злорадно
    victoria "Ага! Вот я и узнала твой секретик, подружка Стефани!"
    victoria "Хи-хи-хи!"
    fitness_instructor "Ты останешься?"
    stephanie "Да. А сейчас убери руки!"
    fitness_instructor "Я жду тебя здесь. Рррр!"
    stephanie "Ха-ха! Я приду, когда девочки уйдут."
    #
    # else:
    #
    $ notif(_("Стефани флиртует с фитнес-тренером."))
    #
    fitness_instructor "Стефани, ты такая красивая..."
    stephanie "Без тебя знаю!"
    fitness_instructor "Задержишься, когда все уйдут?"
    fitness_instructor "Я хочу провести для тебя персональную тренировку!"
    # он прикасается к руке Стефани или кладет руку ей на талию
    stephanie "Убери руку!"
    stephanie "Никаких персональных тренировок! Пока что... Я еще думаю..."
    # Виктория злорадно
    victoria "Ага! Вот я и узнала твой секретик, подружка Стефани!"
    victoria "Хи-хи-хи!"
    fitness_instructor "Я готов ждать тебя столько, сколько нужно!"
    fitness_instructor "Тебе понравятся мои персональные тренировки, Стефани!"
    stephanie "Ха-ха-ха!"
    #
    # Виктория прячется обратно в раздевалку, чтоб Стефани ее не заметила
    # Стефани уходит в раздевалку
    # затемнение
    # все девочки стоят в раздевалке
    # Виктория восторженно
    victoria "Ой, девочки!"
    victoria "Такое волшебное чувство! Я так расслабилась!"
    victoria "Такая легкость во всем теле!"
    rebecca "Тебе понравилось занятие, Виктория?"
    victoria "Да! Я в восторге, девочки!"
    victoria "Обязательно приду снова!"
    stephanie "А тебе понравилось, Мелани?"
    melanie "Да, это действительно расслабляет..."
    victoria "Еще немного и мы с подружкой Мелани станем спортивными и подтянутыми, как вы, девочки!"
    victoria "Ой, не могу! Вы такие красотки!"
    rebecca "Спасибо, Виктория. Ты такая милая!"
    # Стефани бросает на Виктория недружелюбный взгляд
    stephanie "..."
    # потом обращается к Мелани
    stephanie "Мелани, будет круто, если ты продолжишь заниматься с нами."
    melanie "Я приду, почему нет?"
    melanie "По крайней мере, здесь нет сумасшедших поклонников и папарацци..."
    stephanie "Да, именно поэтому в этот зал просто так не попадают..."
    stephanie "Посторонние люди..." # смотрит недовольно на Викторию
    # Виктория это видит, но стоит и мило ей улыбается
    victoria "Стефани, я так рада, что ты смогла пригласить меня и мою подружку Мелани!"
    victoria "Теперь мы будем заниматься все вместе!"
    victoria "Так здорово!!!"
    stephanie "Да. Прикольно."
    rebecca "Я тоже очень рада!"
    # затемнение, шуршание одежды
    # они все переоделись, чмокают друг друга в щечку на прощание
    rebecca "Нам нужно будет как-нибудь встретиться всем вместе!"
    rebecca "Мне так понравилось у тебя на девичнике, Виктория!"
    melanie "!!!" # зло
    victoria "Обязательно встретимся, девочки!"
    victoria "Совсем скоро! И мою лучшую подружку Монику обязательно пригласим!"
    victoria "Пока, подружки! До встречи!"
    stephanie "Пока, девочки."
    rebecca "Пока-пока! Скоро увидимся!"
    melanie "Пока..."
    # затемнение, каблуки
    # Мелани и Виктория идут мимо тренера на выход из зала
    # он пялится на Мелани
    fitness_instructor "Девочки, вы молодцы!"
    fitness_instructor "Жду вас на следующем занятии!"
    victoria "Мы обязательно придем! Я просто в восторге!"
    victoria "Вы так здорово проводите тренировку!"
    victoria "Сразу видно - настоящий мастер своего дела!"
    fitness_instructor "Спасибо, Виктория."
    fitness_instructor "Пока, девочки!"
    victoria "До свидания!"
    melanie "До встречи..."
    # они выходят, тренер смотрит Мелани вслед
    $ melanieVictoriaFitness1 = day # Мелани и Виктория посетили первое занятие в фитнес-зале
    return

# Мелани и Виктория вышли из фитнес-зала и стоят у здания
label ep22_4_dialogues2_fitness_3:
    img 43556
    victoria "Тебе понравилось занятие, подружка Мелани?"
    melanie "..."
    melanie "Да, неплохо..."
    victoria "А тренер тебе понравился?"
    melanie "Нет."
    # Виктория с фальшивой озабоченностью
    img 43557
    victoria "Странно..."
    victoria "Я была уверена, что тебе понравится такой мужчина, как тренер..."
    # Мелани подозрительно смотрит на нее
    melanie "Почему ты меня об этом спрашиваешь?"
    # Виктория ехидно
    img 43558
    victoria "Я немного позже все тебе расскажу, подружка Мелани."
    victoria "Пусть пока это останется моим маленьким секретиком!"
    victoria "Хи-хи-хи!"
    img 43559
    melanie "!!!"
    return
