default melanieAlexFirstDate1 = False  # Мелани предложила Алексу жить вместе
default melanieAlexFirstDate2 = False  # Мелани переоделась для Алекса в наряд, который выбрала Виктория
default melanieAlexFirstDate3 = False  # Мелани и Алекс занимались сексом перед камерой



# апартаменты Мелани
label ep214_dialogues4_melanie_alex_1:
    # Виктория с Мелани вдвоем, Мелани в своем домашнем пеньюаре
    # Виктория стоит, собираясь уходить
    # Мелани сидит на диване
    img 18840
    victoria "Подружка Мелани, ты же помнишь что нужно делать?"
    melanie "Помню..."
    victoria "Позвони Алексу. Спроси, он скоро придет?"
    img 18841
    melanie "Я ему уже звонила."
    melanie "Он сказал, что скоро будет."
    # Виктория насмешливо
    img 18842
    victoria "Подружка, ты же хочешь, чтобы я осталась и посмотрела?"
    # Мелани зло на нее смотрит
    img 18843
    melanie "..."
    img 18844
    victoria "Я не слышу ответа, подружка Мелани..."
    img 18845
    melanie "Да!"
    img 18846
    victoria "Что 'да'? Скажи, я хочу это слышать."
    img 18847
    melanie "Я хочу, чтобы ты осталась... Подружка..."
    img 18848
    w
    
    victoria "Я бы с удовольствием осталась и помогла тебе, подружка..."
    victoria "Но я не хочу смущать Алекса."
    # Виктория хихикает
    victoria "Ладно, мне нужно идти."
    victoria "Не нужно, чтобы Алекс знал, что я тебе помогаю, подружка."
    victoria "Ты помнишь, что ты должна будешь надеть и что должна будешь сказать при этом Алексу?"
    melanie "Помню..."
    victoria "Кстати, я чуть не забыла."
    # лезет в сумочку, достает оттуда камеру
    victoria "Если я не хочу смущать Алекса, не значит, что я не хочу посмотреть..."
    # Виктория оставляет камеру на столе
    # Мелани в недоумении смотрит на нее
    melanie "Может, лучше спрятать ее?"
    victoria "Нет, подружка. Камера будет стоять здесь."
    melanie "А что мне сказать Алексу, когда он спросит про эту камеру?"
    victoria "Подружка, ты же умная."
    victoria "Ты не можешь сама придумать, что сказать Алексу?"
    melanie "..."
    victoria "Хорошо... Я тебе помогу."
    victoria "Скажи Алексу, что ты любишь записывать все на камеру..."
    victoria "А потом выкладывать это в интернет."
    # Мелани в шоке
    melanie "?!"
    melanie "?!?!!"
    melanie "?!?!!??!?"
    victoria "Я пошутила."
    # Виктория хихикает
    victoria "Ты доверяешь своей подружке смотреть это и решать, выкладывать это в интернет или нет."
    victoria "Ведь это так?"
    # Мелани все еще шоке
    melanie "Да, я доверяю тебе..."
    # Виктория пристально смотрит на Мелани
    victoria "Кстати, подружка..."
    victoria "Ко мне недавно заходили полицейские от мистера Маркуса."
    # Мелани испуганно смотрит на нее
    melanie "!!!"
    melanie "!!!!!!"
    melanie "!!!!!!!!!"
    victoria "Они спрашивали про Миссис Бакфетт и ее ближайшее окружение."
    victoria "Я собралась им рассказать про тебя..."
    melanie "!!!"
    victoria "Но потом вспомнила, что вы мои подружки и сказала, что ничего не знаю."
    victoria "Они меня попросили сообщить им, если вдруг мне что-то станет известно..."
    # Виктория подходит к двери
    victoria "Помни, подружка."
    victoria "Ты не должна прятаться от камеры."
    victoria "Я должна постоянно видеть подружку в кадре."
    victoria "Алекс останется жить у подружки сегодня и у вас обязательно сегодня должен быть секс."
    # Виктория уходит, Мелани задумчиво смотрит на камеру
    melanie "..."
    return


# апартаменты Мелани
label ep214_dialogues4_melanie_alex_2:
    # Мелани все также задумчиво сидит на диване
    # стук в дверь
    # Мелани идет к двери
    # затемнение, дверь открывается
    # заходит Алекс
    alex_photograph "Мелани, привет."
    # Алекс напряжен, Мелани не глядя на него говорит
    melanie "Привет, Алекс."
    melanie "Проходи."
    # Мелани идет к дивану, садится
    # Алекс садится в кресло напротив
    melanie "..."
    alex_photograph "Кхм..."
    alex_photograph "Честно сказать, для меня было большой неожиданностью твое приглашение."
    # если Мелани делала Алексу минет на камеру
    if monicaMelanieVictoriaPunishment3 == True:
        alex_photograph "Я подумал, что в тот раз... В общем, это все было постановкой."
        #
        $ notif(_("Мелани делала Алексу минет на камеру"))
        #
        melanie "Почему ты так подумал, Алекс?" # у Мелани покер-фейс
        alex_photograph "Ну..."
        alex_photograph "Я же попытался с тобой поговорить после этого, Мелани..."
        alex_photograph "Ты мне ясно дала понять, что не хочешь иметь со мной ничего общего."
        melanie "Я просто немного перенервничала, Алекс..."
        alex_photograph "Да?"
        # Алекс заметно нервничает
        alex_photograph "Кхм... Я не знаю, что это значит, Мелани."
        alex_photograph "Но вообще..."

    alex_photograph "Ты всегда так холодно ко мне относилась..."
    alex_photograph "Совсем не обращала на меня внимания..."
    alex_photograph "Я даже надеяться не мог на интерес с твоей стороны."
    melanie "Тем не менее, это так, Алекс."
    melanie "Я... Просто хорошо умею скрывать свои чувства."
    alex_photograph "То есть все, что тогда говорила Виктория про тебя..."
    alex_photograph "Это правда?"
    # Мелани бросает взгляд на камеру
    melanie "..."
    melanie "Да, правда."
    melanie "Виктория моя подружка и знает о моих чувствах к тебе."
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса
    # У Виктории ехидная улыбка
    # затемнение, смена кадра
    # апартаменты Мелани
    alex_photograph "Я не ожидал услышать подобного признания от тебя, Мелани..."
    alex_photograph "Я... Я немного растерян..."
    alex_photograph "Ты - самая знаменитая топ-модель..."
    alex_photograph "У тебя миллионы поклонников..."
    alex_photograph "И я..."
    melanie "Все хорошо, Алекс."
    melanie "Выпей немного вина, расслабься."
    melanie "И мне налей."
    melanie "А я пока включу нам что-нибудь романтическое..."
    # Мелани протягивает руку к патефону
    # затемнение, звук льющегося в бокал вина
    # звук патефона, музыка (какой-нибудь романтик)
    # смена кадра
    # играет патефон, перед Мелани на столе стоит полный бокал вина, она без эмоций сидит и смотрит в одну точку
    melanie "..."
    # Алекс в этой время делает глоток вина и немного расслабляется, но все еще на нервах
    alex_photograph "Приятная музыка, Мелани. Твоя любимая?"
    # Мелани выходит из состояния задумчивости
    melanie "Что?"
    melanie "Музыка?"
    melanie "Ах, да. Мне тоже нравится..."
    # Алекс смотрит на патефон и только сейчас замечает, что за ним стоит камера
    alex_photograph "Мелани, это что, камера?"
    melanie "Да."
    alex_photograph "Зачем тебе камера?"
    alex_photograph "Ты хочешь все записать?"
    melanie "Да, хочу..."
    alex_photograph "Хм, это странно..."
    alex_photograph "Я не замечал раньше за тобой такого."
    alex_photograph "Ты всегда избегала моей камеры, Мелани."
    # она ему холодно отвечает
    melanie "Потому что тогда тебя не было со мной в кадре, Алекс."
    melanie "Я хочу запечатлеть наше с тобой свидание."
    melanie "На память..."
    melanie "Ты же не будешь против, Алекс?"
    alex_photograph "Все равно мне кажется это странным..."
    alex_photograph "Но я не против, Мелани. Ты знаешь, я люблю камеры!"
    # Алекс откидывается на спинку кресла и осматривается, смотрит на портреты на стене
    # замечает, что один из портретов разрисован
    # Алекс удивленно смотрит на портрет
    alex_photograph "Мелани, это одна из моих любимых работ."
    alex_photograph "Почему она разрисована?"
    alex_photograph "Она тебе не нравится?"
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса, с улыбочкой
    # затемнение, смена кадра
    # апартаменты Мелани
    # Мелани, глядя в камеру, говорит
    melanie "Алекс, я..."
    melanie "Я мечтала о твоем члене, рисовала его и думала в тот момент о тебе."
    melanie "Это твоя работа и я хочу, чтобы это тут осталось."
    melanie "Как символ наших с тобой чувств."
    melanie "Поэтому, давай не будем это стирать?"
    # Алекс удивленно смотрит на Мелани
    alex_photograph "Ну хорошо..."
    alex_photograph "Ты правда думала о моем... Обо мне, когда рисовала это?"
    melanie "Да."
    alex_photograph "И много у тебя разрисованных портретов?"
    melanie "..."
    melanie "Только этот."
    melanie "И я..."
    # снова взгляд на камеру
    menu:
        "Предложить Алексу жить вместе.":
            $ melanieAlexFirstDate1 = True # Мелани предложила Алексу жить вместе
            pass
    melanie "Я надеюсь, что мне не придется больше мечтать о тебе, Алекс..."
    melanie "Рисуя на твоих работах."
    melanie "Потому что ты согласишься на мое предложение."
    alex_photograph "Какое предложение, Мелани?"
    melanie "..."
    melanie "Жить вместе со мной."
    # Алекс шокирован
    alex_photograph "Ты хочешь, чтобя я и ты?"
    alex_photograph "Чтобы мы жили вместе?!"
    alex_photograph "?!!!!?!?!"
    melanie "Да..." # без особого энтузиазма
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса
    # затемнение, смена кадра
    # апартаменты Мелани
    # Алекс не верит
    alex_photograph "Это очень странно, Мелани..."
    alex_photograph "Почему ты предлагаешь мне сразу жить вместе?"
    melanie "Потому что я хочу этого, Алекс..."
    alex_photograph "Мы с тобой даже не встречались."
    alex_photograph "Ты всегда была так холодна со мной и вдруг сразу предлагаешь жить вместе."
    melanie "..."
    melanie "Просто я долго сомневалась."
    melanie "Но теперь я точно знаю, что хочу этого."
    alex_photograph "Мелани, но как ты можешь это утверждать?"
    alex_photograph "У нас с тобой не было даже интима!"
    # Мелани снова смотрит на камеру
    menu:
        "Переодеться в одежду, которую выбрала Виктория.":
            $ melanieAlexFirstDate2 = True # Мелани переоделась для Алекса в наряд, который выбрала Виктория
            pass
    melanie "Алекс, подожи минуту. Я сейчас вернусь."
    # затемнение
    # спустя несколько минут
    # Мелани возвращается в гостиную, переодевшись в откровенный наряд
    # Алекс смотрит на нее обалдевшим взглядом
    # она садится напротив него, смотрит в камеру
    melanie "Алекс, ты меня очень огорчишь, если откажешься жить со мной."
    # он пускает на нее слюни и ничего уже не соображает
    alex_photograph "Мелани!"
    alex_photograph "О Боже! Мелани, что ты со мной делаешь?!"
    # Алекс соскакивает с кресла и припадает к ногам Мелани (она на диване, он на коленях на полу перед ней)
    alex_photograph "Я согласен! Я все готов сделать для тебя, Мелани!"
    alex_photograph "Дай мне! Дай рассмотреть твою киску вблизи!"
    # Мелани недовольно смотрит на камеру, потом на Алекса
    menu:
        "Раздвинуть ноги.":
            pass
    melanie "..."
    # раздвигает ноги
    alex_photograph "Оооо!!!"
    alex_photograph "Оооо, Меланиии..."
    # Алекс взглядом маньяка рассматривает ее, потом припадает губами к ее киске, ликинг
    alex_photograph "Ммммм!!!"
    alex_photograph "МММММ!!!"
    # Мелани сидит, прикрыв глаза, особо не эмоционирует
    # потом снова смотрит на камеру
    # офис Дика, Виктория сидит у компа
    # Виктория зло смотрит на монитор
    victoria "И что, подружка? Ты решила отделаться лишь этим?"
    victoria "Просто дать полизать ему свою киску?"
    victoria "Ты решила подвести меня?"
    # смена кадра на апартаменты Мелани
    melanie "Алекс, стоп!"
    alex_photograph "Да? Что-то не так?"
    alex_photograph "Тебе что-то не нравится?"
    melanie "Все хорошо, Алекс."
    melanie "Может, пойдем в спальню?"
    melanie "Нам там будет намного удобнее..."
    alex_photograph "Да-да, пойдем."
    alex_photograph "Конечно."
    # Мелани берет камеру с собой
    alex_photograph "Мелани, давай мы оставим камеру здесь?"
    melanie "..."
    melanie "Я хотела бы записать не только наше с тобой первое свидание, Алекс."
    melanie "Но и наш первый интим."
    melanie "Ты ведь не откажешь мне в этом?"
    alex_photograph "Я не в силах отказать тебе, Мелани."
    alex_photograph "Мне до сих пор кажется, что я попал в один из своих снов..."
    alex_photograph "Что все это сюр и..."
    alex_photograph "Скоро я открою глаза и ты растворишься в утреннем тумане."
    alex_photograph "Мелани... У меня просто нет слов, насколько ты прекрасна!"
    melanie "Спасибо, Алекс..."
    # берет камеру
    # смена кадра, спальня
    # Мелани заходит в спальню
    # Алекс идет за ней, плотоядно на нее смотрит
    # Показываем камеру на тумбочке со звуком того что ее ставят, Мелани стоит рядом
    # Алекс подходит к ней и присев или наклонившись (как делал Эдвардс) целует ее ягодицы
    alex_photograph "Меланиии..."
    alex_photograph "Ты - богиня."
    alex_photograph "Мммм..."
    # Мелани остается равнодушной
    melanie "Алекс, подожди."
    melanie "Пойдем на кровать?"
    # Алекс отстраняется, Мелани ложится на кровать в соблазнительную позу
    # Алекс смотрит на нее и пускает слюни
    # она смотрит на камеру
    melanie "Алекс..."
    melanie "Чего ты ждешь?"
    melanie "Иди сюда."
    # Алекс снимает с себя свой свитер и лезет к Мелани на кровать
    # она выжидательно смотрит на него, эмоций никаких не показывает
    # Алекс осторожно прикасается ладонями к ее ногам
    # ведет ладонями от коленей вверх по бедрам
    # Мелани во время ласк лежит на кровати, прикрыв глаза
    # иногда приоткрывает глаза и бросает взгляд на камеру или на Алекса
    alex_photograph "Я никода не видел столь совершенной красоты..."
    alex_photograph "Мелани..."
    alex_photograph "Твоя кожа как бархат..."
    # ладонями по попе и к талии
    alex_photograph "Твои формы... Такие женственные... Идеальные..."
    # Алекс опускает ладнони на грудь Мелани
    alex_photograph "Моя богиня..."
    # смена кадра, офис Дика
    # Виктория сидит у компа, отодвинувшись от стола
    # ноги широко раздвинуты, одна на столе
    # Виктория неотрывно смотрит в монитор и ласкает себя
    # смена кадра на апартаменты Мелани
    # Алекс гладит Мелани по скуле, прикасается пальцем к губам
    alex_photograph "Смотрю на тебя и у меня просто сносит крышу."
    alex_photograph "Мне никто в этом мире больше не нужен."
    alex_photograph "Только ты, моя богиня."
    # наклоняется к ее губам
    # поцелуй
    alex_photograph "Мммм..."
    alex_photograph "Мелани..."
    # целует ее лицо, шею
    alex_photograph "Какой божественный аромат..."
    # спускается на плечи, потом ниже
    # целует грудь через бра
    alex_photograph "Твоя грудь..."
    alex_photograph "Я мечтал прикоснуться к ней... Целовать ее, ласкать..."
    # приспускает или снимает бра
    # гладит груди ладонями, сжимает их
    # наклоняется к соскам и целует их (или посасывает, немного оттягивая грудь вверх)
    alex_photograph "Мммм..."
    # спускается поцелуями по животу
    alex_photograph "Ты само совершенство, Мелани..."
    alex_photograph "Обожаю тебя..."
    alex_photograph "Мммм..."
    # спускается к ее киске, начинает лизать
    alex_photograph "Ммммм!!!"
    # Мелани прикрывает глаза, ей приятно, но не более того, никаких бурных эмоций
    # Алекс лижет киску и одной рукой надрачивает свой стояк
    # после буквально пары движений рукой вверх-вниз Алекс кончает
    alex_photograph "ААА!"
    alex_photograph "АААААА!!"
    alex_photograph "ААААААААА!!!"
    # Алекс растерянно смотрит на свой член
    # Мелани приподнимается и удивленно и слегка насмешливо смотрит на него
    melanie "И это все?"
    melanie "???"
    # Мелани смотрит на камеру, она обеспокоенна
    melanie "..."
    menu:
        "Черт! Виктория сказала, что обязательно должен быть секс...":
            $ melanieAlexFirstDate3 = True # Мелани и Алекс занимались сексом перед камерой
            pass
    melanie "А я?"
    melanie "???"
    melanie "А интим?"
    melanie "Если ты хочешь жить со мной..."
    melanie "То ты..."
    melanie "Ты должен сделать это..." # Смущенно отворачивается
    # Алекс вовсе не возражает
    alex_photograph "Я сейчас..."
    alex_photograph "Дай мне пару минут."
    alex_photograph "Я сейчас все сделаю, Мелани."
    # он снова гладит ее бедра, она переворачивается на живот
    # он начинает мять попу
    alex_photograph "Ммммм... Какие формы..."
    # потом приближает свой полувялый член к ее попе и начинает им водить туда-сюда по ягодицам, трется
    # у него начинает вставать
    # Мелани снова бросает обеспокоенный взгляд в камеру
    alex_photograph "Мммм..."
    melanie "Алекс?"
    alex_photograph "Да, Мелани?"
    melanie "Ты точно не против жить со мной?"
    melanie "Ты точно этого хочешь?"
    alex_photograph "Да!"
    alex_photograph "Я о таком даже мечтать не мог!"
    # Алекс начинает вводить член в ее киску, вводит наполовину
    melanie "Точно? Ты в этом уверен?"
    alex_photograph "Конечно, Мелани!"
    # он вводит в нее головку и спрашивает
    alex_photograph "Мелани, ты не передумала?"
    alex_photograph "Я могу войти в тебя глубже?"
    melanie "Я не передумала, Алекс..."
    # он вводит головку полностью
    alex_photograph "Точно?"
    alex_photograph "Я могу полность войти в твою киску, Мелани?"
    melanie "Алекс, сделай уже это!"
    melanie "Я не передумала!"
    # Алекс входит в нее, начинает двигаться
    alex_photograph "Ооооо!!!"
    alex_photograph "Как же хорошо!"
    alex_photograph "Не могу поверить, что мой член внутри такой топ-модели!!"
    alex_photograph "Оооох..."
    alex_photograph "У тебя миллионы поклонников!"
    alex_photograph "Но именно мне выдался шанс трахать тебя!"
    alex_photograph "Даааа!!!"
    # смена кадра, офис Дика
    # Виктория продолжает смотреть в монитор и ласкать себя
    # смена кадра на апартаменты Мелани
    # потом Алекс останавливается
    alex_photograph "Мелани, я хочу видеть твое лицо!"
    alex_photograph "Давай, поменяем позу?"
    # Мелани говорит ему равнодушно
    melanie "На сегодня достаточно, Алекс..."
    melanie "Секс уже был."
    alex_photograph "Но Мелани!"
    alex_photograph "Раз ты не кончила, значит секса не было!"
    # Мелани смотрит на камеру, злится
    melanie "!!!"
    melanie "Какую позу ты хочешь, Алекс?"
    alex_photograph "Я хочу, чтобы ты смотрела мне в глаза."
    alex_photograph "Хочу увидеть, как ты кончаешь!"
    melanie "Мне перевернуться?"
    alex_photograph "Нет, давай по-другому..."
    alex_photograph "Садись на меня..."
    # Мелани медлит
    melanie "..."
    melanie "Я не очень люблю эту позу..."
    alex_photograph "Ну, Мелани!"
    alex_photograph "Давай!"
    alex_photograph "Хотя бы чуть-чуть!"
    # Мелани смотрит на камеру, потом нехотя соглашается
    melanie "Хорошо..."
    melanie "Ложись на кровать."
    # Алекс довольный ложится на спину
    # Мелани свысока смотрит на него, на его член
    # потом нехотя садится на него, смотрит на камеру, потом в его глаза
    # секс, Мелани сверху, она начала получать удовольствие от процесса, стонет
    # Алекс периодически мнет ее груди, гладит ее бедра
    alex_photograph "Ооооо!!!"
    alex_photograph "Как же хорошо!"
    alex_photograph "Ты само совершенство, Мелани..."
    # смена кадра, офис Дика
    # Виктория продолжает смотреть в монитор и ласкать себя
    # смена кадра на апартаменты Мелани
    alex_photograph "Звезда мира моды! Знаменитость!"
    alex_photograph "Сколько журналистов гадали, какая твоя киска на вкус!"
    alex_photograph "Оооо..."
    alex_photograph "Тебя желает пол мира!!!"
    alex_photograph "А трахаю тебя Я!!!"
    alex_photograph "Ааааа!!"
    alex_photograph "Оооох..."
    melanie "Мммм..."
    alex_photograph "Ааааа!!"
    alex_photograph "Мммм..."
    alex_photograph "Даааа... Продолжай таааак..."
    melanie "Мммм..."
    alex_photograph "Быстрее..."
    # Мелани кончает первой, Алекс следом за ней
    melanie "Ооооо!!"
    melanie "ОООООО!!!"
    menu:
        "Кончить внутрь Мелани.":
            alex_photograph "Я сейчас кончуууу!!!"
            melanie "Не вздумай кончать в меня!"
            # она хочет встать, но Алекс хватает ее за бедра и удерживает, кончает внутрь
            alex_photograph "ААА!"
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            melanie "Черт!"
            melanie "Алекс!"
            melanie "!!!"
            # испуганный взгляд на камеру
            pass
        "Кончить на киску Мелани.":
            alex_photograph "Я сейчас кончуууу!!!"
            alex_photograph "ААА!"
            melanie "Не вздумай кончать в меня!"
            # Мелани приподнимается и он кончает на нее
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            # Мелани смотрит недовольно на камеру
            pass
    # смена кадра, офис Дика
    # Виктория кончает
    victoria "Мммм..."
    victoria "Ааааа!"
    victoria "АААААААА!!!"
    # смена кадра на апартаменты Мелани
    # Мелани ложится спать
    # довольный Алекс лезет обниматься к ней
    alex_photograph "Мелани, это был самый лучший вечер в моей жизни!"
    alex_photograph "Ты прекрасна!"
    alex_photograph "Я тебя обожаю, Мелани!"
    # Мелани раздражена
    melanie "Алекс..."
    melanie "Ты будешь спать на диване в гостиной."
    # Алекс расстроенно
    alex_photograph "Но, Мелани..."
    alex_photograph "Почему?"
    alex_photograph "Если мы теперь живем вместе, то и спать должны вместе!"
    melanie "Я привыкла спать одна в своей постели..."
    melanie "Мне нужно время."
    melanie "Поэтому сегодня ты спишь в гостиной."
    melanie "И это не обсуждается, Алекс."
    alex_photograph "..." # расстроен
    # Алекс уходит, говорит оборачиваясь
    alex_photograph "Тогда я с утра приду к тебе."
    alex_photograph "И разбужу тебя своими ласками!"
    alex_photograph "Люблю начинать день с хорошего секса!"
    melanie "!!!"
    # Мелани зло на него смотрит
    # занавес
    return
