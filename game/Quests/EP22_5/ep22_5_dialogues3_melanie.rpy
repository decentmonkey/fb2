default melanieVictoriaInstructorDate1 = 0  # Мелани увидела на руках Виктории шрамы
default melanieVictoriaInstructorDate2 = 0  # у Мелани было DP с Алексом и фитнес-тренером

# апартаменты Виктории
# Мелани и Виктория сидят на диванчике, на котором сидела Стефани
label ep22_5_dialogues3_melanie_1:
    # Виктория, как обычно, с самодовольной улыбочкой
    victoria "Ой, подружка Мелани, я так рада, что наша дружба становится все крепче и крепче!"
    victoria "Мне нравится, что мы теперь не только по магазинам ходим вместе..."
    victoria "Но и на тренировки в фитнес-зал!"
    victoria "Это так здорово! Да, подружка?"
    victoria "Тебе нравится дружить со мной?"
    # Мелани без эмоций смотрит на нее
    melanie "Очень нравится... Подружка..."
    # Виктория хихикает, поднимая руку к лицу, как обычно
    victoria "Хи-хи-хи!"
    # браслеты по ее руке сползают вниз и становится видно свежие следы от потертостей
    # Мелани опускает взгляд на эти шрамы на руке Виктории и ее брови удивленно поднимаются вверх
    melanie "?!"
    melanie "?!!?!"
    # Виктория прохихикалась и опускает руку, кладет к себе на колени
    # Виктория продолжает болтать, а Мелани пристально смотрит на ее шрамы, не отводя взгляда, Виктория этого не замечает
    victoria "Подружка Мелани, я тут подумала, что нужно спросить у тебя..."
    victoria "Я часто тебе даю какие-то советы по-дружески..."
    victoria "Хотела спросить у тебя, ценишь ли ты мое искреннее, дружеское участие?"
    victoria "Ведь я делаю это из благих намерений. Я стараюсь ради тебя, подру..."
    # Мелани все это время рассматривает ее шрамы, потом перебивает Викторию на полуслове
    melanie "Что это за шрамы на твоих руках?"
    # Виктория резко смотрит на свои руки, потом на Мелани, выглядит расстерянной
    victoria "!!!"
    # Мелани поднимает взгляд и вопросительно смотрит на Викторию
    melanie "Похоже, это следы от веревок или от наручников."
    # Виктория закрывает шрамы ладонью другой руки, на которой тоже видно шрамы
    melanie "Виктория... Тебя что, связывали?"
    # Виктория резко прячет обе руки так, чтобы Мелани их не видела, она все еще выглядит расстерянной
    victoria "!!!"
    victoria "Ты... Кхм..."
    victoria "Я..."
    # потом берет себя в руки и выражение лица становится обычным, насмешливым
    victoria "Так, подружка Мелани."
    victoria "На чем мы там остановились?"
    # Мелани предпринимает попытку вывести ее на разговор
    melanie "Виктория, тебя кто-то принуждает ко всему этому?.."
    melanie "Скажи мне и я..."
    # Виктория демонстративно игнорит ее слова и перебивает
    victoria "Ах, да! Мы говорили про мои дружеские советы. Хи-хи!"
    melanie "!!!"
    victoria "Я вижу, что ты очень ценишь мои советы, подружка..."
    victoria "И у меня для тебя есть еще один совет."
    victoria "Я могу тебе по-дружески кое-что подсказать..."
    victoria "Ты готова будешь делать так, как я тебе посоветую?.."
    # Мелани все еще в недоумении смотрит на Викторию
    melanie "..."
    victoria "Что молчишь, подружка Мелани?"
    victoria "Если ты считаешь, что я в чем-то заблуждаюсь, то ты всегда можешь сказать об этом."
    victoria "Мы ведь дружим и должны быть искренними друг с другом. Так ведь?"
    # Мелани косится на руки Виктории
    melanie "Да..."
    victoria "Готова последовать моему совету и в этот раз, подружка?"
    melanie "Готова..."
    # пристальный взгляд на Викторию, но та всячески игнорит
    melanie "..."
    # Виктория язвительно улыбается Мелани и говорит
    victoria "Ой, подружка, что-то у меня так устали мои ножки!.."
    victoria "Не могла бы ты помассировать их немного?"
    victoria "По-дружески..."
    melanie "..."
    menu:
        "Сделать, как говорит Виктория.":
            pass
    # Мелани встает с дивана, опускается на колени перед Викторией и начинает стягивать с нее сапог
    melanie "?!"
    # стянув сапог, держит в руках ее ногу, а сама смотрит на ее руки, которые Виктория пытается спрятать
    melanie "?!?!"
    # Виктория говорит еходно Мелани
    victoria "Тебе удобно, подружка Мелани?"
    melanie "..."
    melanie "Да... Удобно..."
    victoria "Я сейчас дам тебе несколько дружеских советов..."
    victoria "А потом мы вместе пойдем на шоппинг. Я помогу тебе подобрать новый наряд. Здорово, правда?!"
    melanie "Да..."
    # Виктория указывает пальцем на свою ногу
    victoria "Ты, подружка, пока будешь слушать мои советы..."
    victoria "Можешь помассировать мою ножку своим язычком."
    # Мелани пристально смотрит на нее и выполняет
    victoria "Хи-хи-хи!"
    melanie "!!!"
    # затемнение
    $ melanieVictoriaInstructorDate1 = day # Мелани увидела на руках Виктории шрамы
    return

# день, кафе в трущобах, где было свидание Моники и Юлии
label ep22_5_dialogues3_melanie_2:
    # тем временем
    # Мелани в новом аутфите заходит в эту забегаловку, останавливается и осматривается
    # на лице выражение брезгливости
    melanie "!!!"
    # у посетителей, которые сидят за столиками, отваливается челюсть, все в шоке смотрят на нее
    cafe_visitor2 "Это же модель Мелани!"
    cafe_visitor2 "Вот это да!!!"
    # один из них (тот, который в свитере) встает и подбегает к ней
    cafe_visitor1 "П-простите, в-вы М-мелани?!"
    cafe_visitor1 "М-модель?!"
    cafe_visitor1 "А м-можно ваш автограф? П-пожалуйста!"
    # Мелани с выражением лица а-ля как надоела эта вся рутина с поклонниками
    melanie "Можно..."
    # не показываем, как дает автограф, кадр в это время на баристу, которая в шоке смотрит на Мелани
    cafe_barista "Охренеееть!"
    cafe_barista "Интересно, что она забыла в нашей забегаловке?!"
    cafe_barista "Явно не на ужин сюда пришла, ха-ха!"
    cafe_barista "А вырядилась-то как! Со съемок что-ли сбежала?"
    # кадр на Мелани, довольный поклонник отходит от нее
    cafe_visitor1 "С-спасибо, М-мелани!"
    cafe_visitor1 "В-вы такая к-красивая!!! Спасибо!!!"
    # Мелани снова оглядывается, не обращая внимания на поклонника
    # из-за одного из столиков ей машет рукой фитнес-тренер, широко улыбаясь
    fitness_instructor "Я тут!"
    fitness_instructor "Иди сюда!"
    # Мелани смотрит на него, как на насекомое, медлит
    melanie "!!!"
    melanie "!!!!"
    # потом направляется к его столику и садится за него
    # на тарелке перед ним лежит бургер (как в Шайни-хол)
    # посетители с завистью смотрят на инструктора и Мелани
    fitness_instructor "Привет, Мелани!"
    melanie "Здравствуй..."
    fitness_instructor "Здорово, что ты предложила сходить на свидание!"
    fitness_instructor "Я так офигел, когда твоя подружка пережала мне, что ты запала на меня!"
    melanie "!!!"
    fitness_instructor "Я чуть в штаны от радости не наложил!"
    fitness_instructor "Кому из чуваков расскажу - не поверят! Ха!"
    fitness_instructor "Пусть обзавидуются мне, придурки!"
    melanie "!!!"
    # подходит официантка, она же бариста
    cafe_barista "Добрый день! Что будете заказывать?"
    fitness_instructor "О! Бургер бери!"
    # Мелани брезгливо смотрит на тренера и не глядя на официантку отвечает
    melanie "Нет, спасибо... Я ничего не буду заказывать."
    cafe_barista "Окей. Если что-то понадобится - позовите меня."
    # официантка отходит и оборачивается, пялясь на Мелани
    fitness_instructor "А чего ты не хочешь заказывать еду?"
    fitness_instructor "Бери! Я угощаю!"
    melanie "Спасибо, не надо... Я не ем фастфуд."
    fitness_instructor "Так и я не ем! Я же на спорте, ха!"
    fitness_instructor "Но раз в месяц можно себя побаловать!"
    fitness_instructor "Потом пара пробежек в парке и как-будто бы и не было никакого бургера с колой!"
    fitness_instructor "Ну так что, уговорил я тебя, а?"
    melanie "На что?"
    fitness_instructor "На бургер с колой, ха!"
    melanie "Нет."
    fitness_instructor "Эээх, зря!.."
    # Мелани пристально смотрит на него нечитаемым взглядом
    # тот сидит жует с довольной рожей
    # потом резко перестает жевать и смотрит на Мелани
    fitness_instructor "Ой, я это!.. Забыл совсем!"
    # торопливо вытирает руку об свою футболку и тянет ее Мелани
    fitness_instructor "Меня зовут Эд! А то мы так и не познакомились."
    fitness_instructor "Но ты можешь называть меня Тедди! Мне нравится, когда девки меня так называют, ха!"
    melanie "!!!"
    # Мелани смотрит на его руку и игнорирует рукопожатие
    # с трудом натягивает на лицо полуулыбку
    melanie "Рада познакомиться с тобой, Тедди..."
    # ему по фигу, он убирает руку и продолжает жевать
    fitness_instructor "А я-то как рад!"
    fitness_instructor "Сижу, смотрю на тебя и не верю, что такая чика, как ты..."
    # она его перебивает
    melanie "Почему ты выбрал для нашей встречи именно это место?"
    # он с придурковатым выражением лица
    fitness_instructor "Так я тут недалко, в парке, бегал."
    fitness_instructor "Я каждый день бегаю в этом парке."
    fitness_instructor "Мне там нравится. Тем более, он недалеко от моего дома."
    fitness_instructor "Хочешь, будешь бегать со мной вместе?"
    fitness_instructor "Тебе стопудово понравится! Классный парк!"
    melanie "Спасибо, я подумаю..."
    # снова подходит официантка
    cafe_barista "Может быть, вы выбрали что-нибудь?"
    # Мелани снова не глядя в ее сторону
    melanie "Нет."
    # официантка поворачивается к инструктору
    cafe_barista "А вам принести еще чего-нибудь?"
    fitness_instructor "Не-а."
    cafe_barista "Окей, как хотите."
    # официантка отходит
    fitness_instructor "Слушай, Мелани!"
    fitness_instructor "Если не хочешь бургер, давай я угощу тебя шавермой!"
    fitness_instructor "Тут недалеко, за углом, продается лучшая шаверма в городе!"
    fitness_instructor "Пальчики оближешь!"
    # Мелани в шоке смотрит на него
    melanie "Шаверма?!"
    fitness_instructor "Да! Пойдем? Прямо там, на улице, и съедим по шаверме!"
    fitness_instructor "Заодно с Джеком тебя познакомлю! Такой классный чувак! Он тебе понравится!"
    melanie "!!!"
    fitness_instructor "Или можно пойти в парк! Сядем на лавочку и поедим, а?!"
    fitness_instructor "Мне кажется, я круто придумал!"
    fitness_instructor "Устроим романтическое свидание, ха!"
    # Мелани снова с трудом изображает улыбку
    melanie "Я... Давай, в следующий раз?"
    melanie "Я планировала, что мы сегодня..."
    fitness_instructor "А хочешь, я проведу для тебя персональную тренировку?"
    melanie "???"
    fitness_instructor "Ты не взяла свой костюм для йоги?"
    melanie "Нет..."
    fitness_instructor "Ну и ладно! В этом костюмчике тоже можно тренироваться!"
    fitness_instructor "Пошли, позанимаемся йогой в парке, а?"
    fitness_instructor "Я помогу тебе расслабиться, а то какая-то напряженная вся."
    fitness_instructor "Волнуешься что-ли, как пройдем свидание со мной, ха?!"
    fitness_instructor "Да ты не переживай! Круто выглядишь, я тоже красавчик!"
    fitness_instructor "Сейчас я доем и пойдем гулять."
    # Мелани с обреченным видом
    melanie "Тедди..."
    fitness_instructor "Угу... Чего?"
    melanie "..."
    menu:
        "Следовать советам Виктории.":
            pass
    # Мелани с видимым трудом выговаривает
    melanie "Я тут подумала..."
    melanie "Почему бы мне не пригласить такого..."
    melanie "Такого красавчика, как ты, к себе..."
    melanie "К себе в гости."
    # он удивленно смотрит на нее
    fitness_instructor "К тебе?"
    melanie "Ко мне..." # обреченно
    fitness_instructor "Ааа! Я врубился!"
    fitness_instructor "Ты забыла свой костюм для йоги дома!"
    fitness_instructor "И поэтому хочешь, чтобы я провел тебе персональную тренировку не в парке, как я предлагаю..."
    fitness_instructor "А у тебя дома! Правильно, да?"
    melanie "..."
    melanie "Да, Тедди."
    # он глупо хихикает
    fitness_instructor "Тедди не только красавчик. Тедди еще и умный парень, ха!"
    melanie "Да... И мне это..."
    melanie "Мне это очень нравится."
    fitness_instructor "Хи-хи-хи!"
    fitness_instructor "Да, я такой! Крутой перец!"
    fitness_instructor "Може, все-таки сначала по шаверме, а?"
    melanie "Нет-нет... У меня не так много времени."
    melanie "Мне нужно успеть провести тренировку до... До вечера."
    # он торопливо встает из-за стола
    fitness_instructor "Понял! Не дурак!"
    fitness_instructor "Я сейчас быстро расплачусь и поедем к тебе!"
    # уходит
    # Мелани остается за столиком одна, на лице буря эмоций из отвращения, ненависти, злости
    melanie "!!!"
    melanie "!!!!"
    melanie "!!!!!!"
    # теренер возвращается и встает рядом с Мелани, тянет ей свою руку
    fitness_instructor "Ну что, погнали?!"
    # затемнение, звук мотора
    # смена кадра на квартиру Мелани
    # она заходит в гостиную, тренер идет следом за ней и пялится на ее попу
    melanie "Чувствуй себя, как дома... Тедди."
    fitness_instructor "Ага. А нормальная такая у тебя хата!"
    fitness_instructor "У меня квартира раза в три меньше!"
    fitness_instructor "За сколько арендуешь?"
    melanie "Это мои апартаменты."
    fitness_instructor "О, ну да. Ты, наверное, зарабатываешь кругленькую сумму, да?"
    fitness_instructor "Сколько у тебя выходит в год? Миллион, наверное? Или даже два!"
    melanie "Неважно."
    fitness_instructor "Ну ладно, не хочешь - не говори."
    fitness_instructor "Но офигеть, какая ты крутая!"
    fitness_instructor "Мои друганы о таких чиках, как ты, даже мечтать не смеют..."
    fitness_instructor "А я тут бац! И приехал в гости к самой модели Мелани, ха!"
    melanie "!!!"
    menu:
        "Следовать советам Виктории.":
            pass
    # Мелани направляется к своей спальне
    melanie "Тедди..."
    melanie "Как я тебе уже говорила, у меня мало времени."
    melanie "Мне нужно успеть до вечера... Провести тренировку с тобой."
    fitness_instructor "Ага, я помню."
    fitness_instructor "Приступим?"
    melanie "Да, давай начнем..."
    fitness_instructor "Ну тогда переодевайся в свой костюм для йоги. Я тебя жду здесь."
    # Мелани идет в спальню, затемнение
    # спястя 5 минут
    # кадр на гостиную, инструктор ждет Мелани и ходит по гостиной, разминаясь перед тренировкой
    # голос из-за двери спальни
    melanie "Тедди?"
    # он резко поворачивает голову в сторону спальни
    fitness_instructor "Ты готова, Мелани?"
    melanie "Я думаю, что нам лучше провести тренировку тут."
    melanie "Так будет гораздо удобнее."
    melanie "Иди сюда."
    # он идет в сторону спальни
    # затемнение
    # смена кадра на спальню
    # тренер заходит и у него от удивления открывается рот
    # он во все глаза пялится на Мелани
    fitness_instructor "ОГО!!!"
    # она стоит голая и с ненавистью смотрит на камеру на прикроватной тумбе
    melanie "!!!"
    # смена кадра
    # приемная в офисе Дика
    # Виктория сидит на своем рабочем месте и смотрит в монитор, довольно хихикая
    victoria "Хи-хи-хи!"
    # затемнение
    # смена кадра на спальню Мелани
    # она поворачивается к тренеру, тот стоит в шоке
    melanie "..."
    menu:
        "Продолжать следовать советам Виктории.":
            pass
    # Мелани равнодушно
    melanie "На кровати гораздо удобнее заниматься йогой. Не так-ли, Тедди?"
    fitness_instructor "Ага, да... К-конечно, уд-добнее..."
    fitness_instructor "А ты?.."
    # Мелани лезет на кровать
    melanie "Мне будет удобно делать это без костюма для йоги..."
    fitness_instructor "Я... А мне... Кхм!"
    # Мелани соблазнительно ложится на живот, косится на камеру
    melanie "Думаю, что тебе тоже одежда будет мешать..."
    melanie "Если так - сними ее."
    # тренер в ступоре смотрит на округлости Мелани
    fitness_instructor "Офигеееть!"
    fitness_instructor "Я сейчас, Мелани! Пару секунд!"
    # он быстро скидывает с себя одежду
    fitness_instructor "Все! Я готов к тернировке!"
    # Мелани зло смотрит на камеру
    melanie "Иди ко мне..."
    melanie "Помоги мне расслабиться... Тедди."
    # тренер лезет на кровать и начинает лапать попу Мелани
    fitness_instructor "Да, Мелани, ты слишком напряжена."
    fitness_instructor "Тебе нужно расслабиться."
    fitness_instructor "Сейчас я помогу тебе."
    fitness_instructor "Раздвинь немного ноги в стороны, Мелани."
    fitness_instructor "Так я более эффективно смогу тебе помочь..."
    melanie "..."
    menu:
        "Раздвинуть ноги.":
            pass
    # Мелани раздвигает ноги
    # тренер кладет ладони на ее ягодицы и разводит их в стороны
    fitness_instructor "Ууууф..."
    fitness_instructor "Ты все еще очень напряжена, Мелани."
    fitness_instructor "Сейчас я помассирую тебя немного и мы приступим к тренировке."
    # рассматривает и трогает пальцем ее дырочки, сует палец то в киску, то в попу
    fitness_instructor "Вот тааак... Хорошо..."
    fitness_instructor "Я вижу, как ты расслабляешься все больше и больше."
    fitness_instructor "Сейчас мы поработаем с твоими мышцами, Мелани."
    fitness_instructor "После этой тернировки ты почувствуешь легкость во всем теле."
    fitness_instructor "И тебе захочется повторять наши персональные тренировки снова и снова."
    fitness_instructor "Ооох..."
    # он пристраивает член к киске Мелани
    fitness_instructor "Сейчас я помассирую тебя немного по-другому."
    fitness_instructor "Это будет более эффективный массаж, чем руками."
    fitness_instructor "Ты ведь хочешь этого, Мелани?"
    melanie "..."
    menu:
        "Следовать советам Виктории.":
            pass
    # Мелани зло смотрит в камеру
    melanie "Да, я с нашей первой встречи в фитнес-зале..."
    melanie "Мечтала об этом..."
    melanie "Помассируй меня, как следует, тренер..."
    # он приподнимает немного ее попу и направляет член на киску
    # водит головкой между ног Мелани
    fitness_instructor "Ооо... Круто как..."
    fitness_instructor "Мне нравится тренировать тебя, Мелани!"
    # вводит член в киску
    fitness_instructor "Ееее!"
    fitness_instructor "Тедди проник в киску модели Мелани!"
    fitness_instructor "Рррр!.. Охренительно!!!"
    fitness_instructor "Тебе нравится, Мелани, а?"
    melanie "Да."
    # он начинает двигаться в ней, а Мелани смотрит в камеру
    fitness_instructor "Мммм, кайфово-то как!"
    fitness_instructor "Меня так надолго не хватит, Мелани."
    fitness_instructor "МММММ... Дааа!!!"
    fitness_instructor "Давай ты будешь сверху!"
    fitness_instructor "Хочу смотреть на тебя, Мелани!"
    # смена кадра
    # приемная в офисе Дика
    # Виктория сидит на своем рабочем месте и трогает свою киску
    victoria "Сегодня у подружки отличная тренировка."
    victoria "Стефани было бы интересно посмотреть на это. Хи-хи!"
    # затемнение
    # смена кадра на спальню Мелани
    # тренер лежит на спине, Мелани двигается на нем сверху
    # он тискает ее груди, лапает за бедра
    fitness_instructor "Поверить не могу, что меня трахает модель с обложки журнала!"
    fitness_instructor "О, сделай так еще раз!"
    fitness_instructor "Такая секс-бомба потекла по Тедди, да!"
    fitness_instructor "Дааа!"
    fitness_instructor "Она не могла не запасть на такого крутого перца, как я, ха!"
    # раздается хлопок дверью, пришел Алекс
    # Мелани перестает двигаться и замирает на тренере, она в афиге
    alex_photograph "Милая, я дома!"
    melanie "!!!"
    alex_photograph "Мне позвонили и передали, что ты для меня приготовила сюрприз."
    alex_photograph "И чтобы я пришел домой пораньше."
    melanie "!!!!"
    alex_photograph "Милая, ты где?"
    # Алекс заходит в спальню и видит Мелани с тренером, она так и продолжает сидеть на нем
    # тренер глупо улыбается
    fitness_instructor "Гы! А это кто?"
    # Алекс в шоке
    alex_photograph "?!?!?!"
    alex_photograph "Мелани?!"
    melanie "Алекс?!"
    alex_photograph "Что это такое, Мелани?!"
    alex_photograph "Объясни мне, что тут происходит?!"
    # Мелани отворачивается от Алекса и смотрит в камеру
    melanie "!!!"
    # смена кадра на приемную в офисе Дика
    # Виктория хихикает
    victoria "Импровизируй, подружка Мелани!"
    victoria "Мне так интересно!"
    victoria "Хи-хи-хи!"
    # ласкает себя
    # затемнение
    # смена кадра на спальню Мелани, она также сидит на теренере
    # Алекс возмущенно
    alex_photograph "Мелани, что ты творишь?!"
    alex_photograph "Зачем ты так поступаешь со мной?!"
    melanie "..."
    alex_photograph "Одно дело твои игры, а другое - любовник в постели!"
    alex_photograph "И после этого ты говоришь о нашей свадьбе?!"
    alex_photograph "Как ты себе представляешь это?!"
    # тренер теряет интерес к Алексу и водит рукой по бедру Мелани, рассматривает ее
    melanie "..."
    menu:
        "Успокоить Алекса (Виктория разозлится, если Алекс уйдет от Мелани).":
            pass
    # Мелани игриво улыбается Алексу
    melanie "Алекс..."
    melanie "Это и есть мой сюрприз для тебя, о котором тебе сказали по телефону."
    alex_photograph "Вот ЭТО сюрприз?!"
    alex_photograph "Я прихожу к свой любимой девушке, а ее трахает незнакомый мужик!"
    alex_photograph "Это, по-твоему, сюрприз?!"
    melanie "Да, Алекс. Я очень хочу поиграть с тобой..."
    melanie "И очень ждала тебя."
    # Алекс зло
    alex_photograph "Ждала меня?"
    melanie "Да, Алекс..."
    alex_photograph "Для чего?"
    melanie "Ох, Алекс..."
    melanie "Я вспоминаю нашу вечеринку со Стефани..."
    melanie "Вспоминаю, как ты и Джон одновременно овладели ее телом..."
    melanie "И меня так возбуждает это. Мммм..."
    # Мелани делает движения бедрами на тренере
    fitness_instructor "Ооох, сделай так еще разочек, Мелани."
    # она повторяет движение
    # тренер кладет руку ей на груди и мнет их
    fitness_instructor "Ееее..."
    # Мелани изображает возбуждение, прикрывая глаза и облизывая губы
    melanie "Мммм... Даа..."
    melanie "Алекс, я так возбуждаюсь от мысли о том..."
    melanie "Что ты сейчас войдешь в мою попу..."
    melanie "В то время как внутри моей киски член другого мужчины!.."
    # тренер продолжает лапать Мелани и качает ее бедра на своем члене
    fitness_instructor "Ууууф, как круто!"
    fitness_instructor "Как ты возбуждена, Мелани..."
    melanie "Да! Я так завожусь от этой мысли!"
    melanie "Так хочу этого!"
    # Алекс растерянно смотрит на происходящее
    alex_photograph "..."
    # потом залипает взглядом на попе Мелани
    alex_photograph "..."
    # она видит его взгляд и проводит рукой по своим ягодицам
    melanie "Алекс, ты же не откажешь мне? Я ведь так ждала тебя!"
    alex_photograph "Нуу... Ты что, правда так хочешь этого?"
    melanie "Да-да! Войди же в меня, Алекс!"
    # Алекс смотрит на ее попу и начинает раздеваться
    melanie "!!!"
    # смена кадра на приемную в офисе Дика
    # Виктория радостно
    victoria "Ох, как подружка Мелани умеет изображать страсть!"
    victoria "Какая старательная и хорошая подружка!"
    # ласкает себя
    # затемнение
    # смена кадра на спальню Мелани
    # голый Алекс уже лезет на постель к Мелани
    # трогает попу Мелани
    melanie "О, да, Алекс! Сделай это скорее!"
    melanie "Я так возбуждена! Я так хочу тебя!"
    melanie "Быстрее, Алекс!"
    # Алекс пристраивается членом к ее попе
    alex_photograph "Да, милая. Сейчас..."
    alex_photograph "Ты и правда так возбуждена..."
    alex_photograph "Ты такая страстная..."
    alex_photograph "Я не могу тебе отказать, милая... Просто не в силах отказать."
    # Алекс вводит свой член в попу Мелани
    melanie "Аааа!"
    melanie "Даааа!!!"
    # тренер довольно улыбается и двигает бедрами, продолжая лапать Мелани за грудь
    fitness_instructor "Ооо, кайф! Как же круто!"
    melanie "Мммммм!!!"
    alex_photograph "Оооох..."
    melanie "Даааа... Продолжай таааак..."
    melanie "Аааах!!!"
    alex_photograph "Мммм..."
    melanie "Мпфааа!!!"
    alex_photograph "Ааааа!!"
    fitness_instructor "Вот это тренировка! Да!!!"
    # Мелани кончает первой (ну, или делает вид)
    melanie "Я не могу больше сдерживаться!"
    melanie "ОООООО!!!"
    melanie "Кончаю!"
    melanie "ООООО!!!"
    melanie "ОООООООО!!!"
    alex_photograph "И я сейчас кончуууу!!!"
    fitness_instructor "Да-да! Я тоже!"
    menu:
        "Кончить внутрь Мелани.":
			fitness_instructor "Ррррр!"
			fitness_instructor "Оооох..."
			fitness_instructor "ДАААААА!!!"
            alex_photograph "ААА!"
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            melanie "Ммммм..."
            pass
        "Кончить на Мелани.":
			fitness_instructor "Ррррр!"
			fitness_instructor "Оооох..."
			fitness_instructor "ДАААААА!!!"
            alex_photograph "ААА!"
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            melanie "Ммммм..."
            pass
    # Мелани, вся в сперме, смотрит на камеру
    melanie "!!!"
    # затемнение
    # смена кадра на приемную в офисе Дика
    # Виктория кончает
    victoria "Мммм..."
    victoria "Ааааа!"
    victoria "АААААААА!!!"
    # потом расслаблено откидывается в кресле
    victoria "Отличная работа, подружка Мелани..."
    victoria "Хи-хи-хи!"
    # затемнение
    $ melanieVictoriaInstructorDate2 = day # у Мелани было DP с Алексом и фитнес-тренером
    return
