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
    img 18849
    victoria "Я бы с удовольствием осталась и помогла тебе, подружка..."
    victoria "Но я не хочу смущать Алекса."
    # Виктория хихикает
    img 18850
    victoria "Ладно, мне нужно идти."
    victoria "Не нужно, чтобы Алекс знал, что я тебе помогаю, подружка."
    victoria "Ты помнишь, что ты должна будешь надеть и что должна будешь сказать при этом Алексу?"
    melanie "Помню..."
    victoria "Кстати, я чуть не забыла."
    # лезет в сумочку, достает оттуда камеру
    img 18851
    victoria "Если я не хочу смущать Алекса, не значит, что я не хочу посмотреть..."
    # Виктория оставляет камеру на столе
    # Мелани в недоумении смотрит на нее
    melanie "Может, лучше спрятать ее?"
    victoria "Нет, подружка. Камера будет стоять здесь."
    img 18852
    melanie "А что мне сказать Алексу, когда он спросит про эту камеру?"
    img 18853
    victoria "Подружка, ты же умная."
    victoria "Ты не можешь сама придумать, что сказать Алексу?"
    img 18854
    melanie "..."
    img 18855
    victoria "Хорошо... Я тебе помогу."
    victoria "Скажи Алексу, что ты любишь записывать все на камеру..."
    victoria "А потом выкладывать это в интернет."
    # Мелани в шоке
    img 18856
    melanie "?!"
    melanie "?!?!!"
    melanie "?!?!!??!?"
    img 18857
    victoria "Я пошутила."
    # Виктория хихикает
    img 18858
    victoria "Ты доверяешь своей подружке смотреть это и решать, выкладывать это в интернет или нет."
    victoria "Ведь это так?"
    # Мелани все еще шоке
    melanie "Да, я доверяю тебе..."
    # Виктория пристально смотрит на Мелани
    img 18859
    victoria "Кстати, подружка..."
    victoria "Ко мне недавно заходили полицейские от мистера Маркуса."
    # Мелани испуганно смотрит на нее
    img 18860
    melanie "!!!"
    melanie "!!!!!!"
    melanie "!!!!!!!!!"
    img 18861
    victoria "Они спрашивали про Миссис Бакфетт и ее ближайшее окружение."
    victoria "Я собралась им рассказать про тебя..."
    melanie "!!!"
    img 18862
    victoria "Но потом вспомнила, что вы мои подружки и сказала, что ничего не знаю."
    victoria "Они меня попросили сообщить им, если вдруг мне что-то станет известно..."
    # Виктория подходит к двери
    img 18863
    victoria "Помни, подружка."
    victoria "Ты не должна прятаться от камеры."
    img 18864
    victoria "Я должна постоянно видеть подружку в кадре."
    victoria "Алекс останется жить у подружки сегодня и у вас обязательно сегодня должен быть секс."
    # Виктория уходит, Мелани задумчиво смотрит на камеру
    img 18865
    w
    img 18866
    melanie "..."
    return


# апартаменты Мелани
label ep214_dialogues4_melanie_alex_2:
    # Мелани все также задумчиво сидит на диване
    # стук в дверь
    # Мелани идет к двери
    # затемнение, дверь открывается
    # заходит Алекс
    img 18867
    w
    img 18868
    alex_photograph "Мелани, привет."
    # Алекс напряжен, Мелани не глядя на него говорит
    img 18869
    melanie "Привет, Алекс."
    melanie "Проходи."
    # Мелани идет к дивану, садится
    # Алекс садится в кресло напротив
    img 18870
    w
    img 18871
    w
    img 18872
    melanie "..."
    img 18873
    alex_photograph "Кхм..."
    alex_photograph "Честно сказать, для меня было большой неожиданностью твое приглашение."
    # если Мелани делала Алексу минет на камеру
    if monicaMelanieVictoriaPunishment3 == True:
        alex_photograph "Я подумал, что в тот раз... В общем, это все было постановкой."
        #
        $ notif(_("Мелани делала Алексу минет на камеру"))
        #
        img 18874
        melanie "Почему ты так подумал, Алекс?" # у Мелани покер-фейс
        img 18875
        alex_photograph "Ну..."
        alex_photograph "Я же попытался с тобой поговорить после этого, Мелани..."
        alex_photograph "Ты мне ясно дала понять, что не хочешь иметь со мной ничего общего."
        img 18876
        melanie "Я просто немного перенервничала, Алекс..."
        alex_photograph "Да?"
        # Алекс заметно нервничает
        alex_photograph "Кхм... Я не знаю, что это значит, Мелани."
        alex_photograph "Но вообще..."
    img 18877
    alex_photograph "Ты всегда так холодно ко мне относилась..."
    alex_photograph "Совсем не обращала на меня внимания..."
    alex_photograph "Я даже надеяться не мог на интерес с твоей стороны."
    img 18878
    melanie "Тем не менее, это так, Алекс."
    melanie "Я... Просто хорошо умею скрывать свои чувства."
    img 18879
    alex_photograph "То есть все, что тогда говорила Виктория про тебя..."
    alex_photograph "Это правда?"
    # Мелани бросает взгляд на камеру
    img 18880
    melanie "..."
    img 18881
    melanie "Да, правда."
    melanie "Виктория моя подружка и знает о моих чувствах к тебе."
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса
    # У Виктории ехидная улыбка
    # затемнение, смена кадра
    # апартаменты Мелани
    img 18882
    alex_photograph "Я не ожидал услышать подобного признания от тебя, Мелани..."
    alex_photograph "Я... Я немного растерян..."
    alex_photograph "Ты - самая знаменитая топ-модель..."
    alex_photograph "У тебя миллионы поклонников..."
    alex_photograph "И я..."
    img 18883
    melanie "Все хорошо, Алекс."
    melanie "Выпей немного вина, расслабься."
    melanie "И мне налей."
    melanie "А я пока включу нам что-нибудь романтическое..."
    img 18932
    w
    img 18884
    # Мелани протягивает руку к патефону
    # затемнение, звук льющегося в бокал вина
    # звук патефона, музыка (какой-нибудь романтик)
    # смена кадра
    # играет патефон, перед Мелани на столе стоит полный бокал вина, она без эмоций сидит и смотрит в одну точку
    img 18885
    melanie "..."
    # Алекс в этой время делает глоток вина и немного расслабляется, но все еще на нервах
    img 18886
    w
    img 18887
    alex_photograph "Приятная музыка, Мелани. Твоя любимая?"
    # Мелани выходит из состояния задумчивости
    img 18888
    melanie "Что?"
    melanie "Музыка?"
    melanie "Ах, да. Мне тоже нравится..."
    # Алекс смотрит на патефон и только сейчас замечает, что за ним стоит камера
    img 18889
    alex_photograph "Мелани, это что, камера?"
    melanie "Да."
    img 18890
    alex_photograph "Зачем тебе камера?"
    alex_photograph "Ты хочешь все записать?"
    melanie "Да, хочу..."
    img 18891
    alex_photograph "Хм, это странно..."
    alex_photograph "Я не замечал раньше за тобой такого."
    alex_photograph "Ты всегда избегала моей камеры, Мелани."
    # она ему холодно отвечает
    img 18892
    melanie "Потому что тогда тебя не было со мной в кадре, Алекс."
    melanie "Я хочу запечатлеть наше с тобой свидание."
    melanie "На память..."
    img 18893
    melanie "Ты же не будешь против, Алекс?"
    img 18894
    alex_photograph "Все равно мне кажется это странным..."
    alex_photograph "Но я не против, Мелани. Ты знаешь, я люблю камеры!"
    # Алекс откидывается на спинку кресла и осматривается, смотрит на портреты на стене
    # замечает, что один из портретов разрисован
    # Алекс удивленно смотрит на портрет
    img 18895
    w
    img 18896
    alex_photograph "Мелани, это одна из моих любимых работ."
    alex_photograph "Почему она разрисована?"
    alex_photograph "Она тебе не нравится?"
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса, с улыбочкой
    # затемнение, смена кадра
    # апартаменты Мелани
    # Мелани, глядя в камеру, говорит
    img 18872
    melanie "Алекс, я..."
    melanie "Я мечтала о твоем члене, рисовала его и думала в тот момент о тебе."
    melanie "Это твоя работа и я хочу, чтобы это тут осталось."
    melanie "Как символ наших с тобой чувств."
    melanie "Поэтому, давай не будем это стирать?"
    img 18851
    w
    Мелаани 1
    # Алекс удивленно смотрит на Мелани
    img 18897
    alex_photograph "Ну хорошо..."
    alex_photograph "Ты правда думала о моем... Обо мне, когда рисовала это?"
    melanie "Да."
    img 18882
    alex_photograph "И много у тебя разрисованных портретов?"
    img 18883
    melanie "..."
    melanie "Только этот."
    melanie "И я..."
    # снова взгляд на камеру
    menu:
        "Предложить Алексу жить вместе.":
            $ melanieAlexFirstDate1 = True # Мелани предложила Алексу жить вместе
            pass
    img 18898
    melanie "Я надеюсь, что мне не придется больше мечтать о тебе, Алекс..."
    melanie "Рисуя на твоих работах."
    melanie "Потому что ты согласишься на мое предложение."
    img 18899
    alex_photograph "Какое предложение, Мелани?"
    melanie "..."
    melanie "Жить вместе со мной."
    # Алекс шокирован
    img 18900
    alex_photograph "Ты хочешь, чтобя я и ты?"
    alex_photograph "Чтобы мы жили вместе?!"
    img 18901
    alex_photograph "?!!!!?!?!"
    img 18902
    melanie "Да..." # без особого энтузиазма
    # тем времнем в офисе Дика
    # показываем офиса Дика
    # Виктория сидит и смотрит на компе свидание Мелани и Алекса
    # затемнение, смена кадра
    # апартаменты Мелани
    # Алекс не верит
    img 18851
    w
    Мелаани 2
    w
    img 18903
    alex_photograph "Это очень странно, Мелани..."
    alex_photograph "Почему ты предлагаешь мне сразу жить вместе?"
    melanie "Потому что я хочу этого, Алекс..."
    img 18904
    alex_photograph "Мы с тобой даже не встречались."
    alex_photograph "Ты всегда была так холодна со мной и вдруг сразу предлагаешь жить вместе."
    img 18905
    melanie "..."
    melanie "Просто я долго сомневалась."
    melanie "Но теперь я точно знаю, что хочу этого."
    img 18906
    alex_photograph "Мелани, но как ты можешь это утверждать?"
    alex_photograph "У нас с тобой не было даже интима!"
    # Мелани снова смотрит на камеру
    menu:
        "Переодеться в одежду, которую выбрала Виктория.":
            $ melanieAlexFirstDate2 = True # Мелани переоделась для Алекса в наряд, который выбрала Виктория
            pass
    img 18907
    melanie "Алекс, подожи минуту. Я сейчас вернусь."
    # затемнение
    # спустя несколько минут
    # Мелани возвращается в гостиную, переодевшись в откровенный наряд
    # Алекс смотрит на нее обалдевшим взглядом
    # она садится напротив него, смотрит в камеру
    img 18908
    w
    img 18909
    w
    img 18910
    w
    img 18911
    melanie "Алекс, ты меня очень огорчишь, если откажешься жить со мной."
    # он пускает на нее слюни и ничего уже не соображает
    img 18912
    alex_photograph "Мелани!"
    alex_photograph "О Боже! Мелани, что ты со мной делаешь?!"
    # Алекс соскакивает с кресла и припадает к ногам Мелани (она на диване, он на коленях на полу перед ней)
    img 18913
    alex_photograph "Я согласен! Я все готов сделать для тебя, Мелани!"
    alex_photograph "Дай мне! Дай рассмотреть твою киску вблизи!"
    # Мелани недовольно смотрит на камеру, потом на Алекса
    menu:
        "Раздвинуть ноги.":
            pass
    img 18914
    melanie "..."
    # раздвигает ноги
    img 18915
    alex_photograph "Оооо!!!"
    img 19013
    alex_photograph "Оооо, Меланиии..."
    # Алекс взглядом маньяка рассматривает ее, потом припадает губами к ее киске, ликинг
    img 18916
    w
    img 18917
    w
    img 18918
    alex_photograph "Ммммм!!!"
    img 18919
    w
    img 18920
    alex_photograph "МММММ!!!"
    w
    img 18921
    w
    img 18922
    w
    img 18923
    w
    img 18924
    # Мелани сидит, прикрыв глаза, особо не эмоционирует
    # потом снова смотрит на камеру
    # офис Дика, Виктория сидит у компа
    # Виктория зло смотрит на монитор
    victoria "И что, подружка? Ты решила отделаться лишь этим?"
    victoria "Просто дать полизать ему свою киску?"
    victoria "Ты решила подвести меня?"
    # смена кадра на апартаменты Мелани
    img 18925
    melanie "Алекс, стоп!"
    img 18926
    alex_photograph "Да? Что-то не так?"
    alex_photograph "Тебе что-то не нравится?"
    img 18927
    melanie "Все хорошо, Алекс."
    melanie "Может, пойдем в спальню?"
    melanie "Нам там будет намного удобнее..."
    img 18928
    alex_photograph "Да-да, пойдем."
    alex_photograph "Конечно."
    # Мелани берет камеру с собой
    img 18929
    alex_photograph "Мелани, давай мы оставим камеру здесь?"
    melanie "..."
    melanie "Я хотела бы записать не только наше с тобой первое свидание, Алекс."
    melanie "Но и наш первый интим."
    melanie "Ты ведь не откажешь мне в этом?"
    img 18930
    alex_photograph "Я не в силах отказать тебе, Мелани."
    alex_photograph "Мне до сих пор кажется, что я попал в один из своих снов..."
    alex_photograph "Что все это сюр и..."
    alex_photograph "Скоро я открою глаза и ты растворишься в утреннем тумане."
    alex_photograph "Мелани... У меня просто нет слов, насколько ты прекрасна!"
    img 18931
    melanie "Спасибо, Алекс..."
    # берет камеру
    # смена кадра, спальня
    # Мелани заходит в спальню
    # Алекс идет за ней, плотоядно на нее смотрит
    # Показываем камеру на тумбочке со звуком того что ее ставят, Мелани стоит рядом
    # Алекс подходит к ней и присев или наклонившись (как делал Эдвардс) целует ее ягодицы
    img 18933
    w
    img 18934
    w
    img 18935
    w
    img 18936
    alex_photograph "Меланиии..."
    alex_photograph "Ты - богиня."
    img 18937
    alex_photograph "Мммм..."
    w
    img 18940
    w
    img 18941
    # Мелани остается равнодушной
    img 18938
    melanie "Алекс, подожди."
    melanie "Пойдем на кровать?"
    # Алекс отстраняется, Мелани ложится на кровать в соблазнительную позу
    # Алекс смотрит на нее и пускает слюни
    # она смотрит на камеру
    img 18939
    w
    img 18942
    w
    img 18943
    melanie "Алекс..."
    melanie "Чего ты ждешь?"
    melanie "Иди сюда."
    img 18944
    # Алекс снимает с себя свой свитер и лезет к Мелани на кровать
    # она выжидательно смотрит на него, эмоций никаких не показывает
    # Алекс осторожно прикасается ладонями к ее ногам
    # ведет ладонями от коленей вверх по бедрам
    # Мелани во время ласк лежит на кровати, прикрыв глаза
    # иногда приоткрывает глаза и бросает взгляд на камеру или на Алекса
    img 18945
    alex_photograph "Я никода не видел столь совершенной красоты..."
    alex_photograph "Мелани..."
    alex_photograph "Твоя кожа как бархат..."
    # ладонями по попе и к талии
    img 18946
    alex_photograph "Твои формы... Такие женственные... Идеальные..."
    # Алекс опускает ладнони на грудь Мелани
    alex_photograph "Моя богиня..."
    # смена кадра, офис Дика
    # Виктория сидит у компа, отодвинувшись от стола
    # ноги широко раздвинуты, одна на столе
    # Виктория неотрывно смотрит в монитор и ласкает себя
    # смена кадра на апартаменты Мелани
    # Алекс гладит Мелани по скуле, прикасается пальцем к губам
    img 18947
    w
    img 18948
    w
    img 18949
    w
    img 18950
    w
    img 18951
    alex_photograph "Смотрю на тебя и у меня просто сносит крышу."
    alex_photograph "Мне никто в этом мире больше не нужен."
    alex_photograph "Только ты, моя богиня."
    # наклоняется к ее губам
    # поцелуй
    img 18952
    alex_photograph "Мммм..."
    alex_photograph "Мелани..."
    # целует ее лицо, шею
    img 18953
    alex_photograph "Какой божественный аромат..."
    # спускается на плечи, потом ниже
    # целует грудь через бра
    img 18954
    alex_photograph "Твоя грудь..."
    img 18955
    alex_photograph "Я мечтал прикоснуться к ней... Целовать ее, ласкать..."
    # приспускает или снимает бра
    # гладит груди ладонями, сжимает их
    # наклоняется к соскам и целует их (или посасывает, немного оттягивая грудь вверх)
    img 18956
    alex_photograph "Мммм..."
    img 18957
    w
    img 189558
    # спускается поцелуями по животу
    img 18959
    alex_photograph "Ты само совершенство, Мелани..."
    alex_photograph "Обожаю тебя..."
    alex_photograph "Мммм..."
    # спускается к ее киске, начинает лизать
    img 18960
    alex_photograph "Ммммм!!!"
    # Мелани прикрывает глаза, ей приятно, но не более того, никаких бурных эмоций
    # Алекс лижет киску и одной рукой надрачивает свой стояк
    # после буквально пары движений рукой вверх-вниз Алекс кончает
    img 18961
    w
    img 18962
    w
    img 18963
    w
    img 18967
    w
    img 18964
    w
    img 18965
    alex_photograph "ААА!"
    img 18966
    alex_photograph "АААААА!!"
    img 18968
    alex_photograph "ААААААААА!!!"
    # Алекс растерянно смотрит на свой член
    # Мелани приподнимается и удивленно и слегка насмешливо смотрит на него
    img 18969
    melanie "И это все?"
    melanie "???"
    # Мелани смотрит на камеру, она обеспокоенна
    img 18970
    melanie "..."
    menu:
        "Черт! Виктория сказала, что обязательно должен быть секс...":
            $ melanieAlexFirstDate3 = True # Мелани и Алекс занимались сексом перед камерой
            pass
    img 18971
    melanie "А я?"
    melanie "???"
    melanie "А интим?"
    img 18972
    melanie "Если ты хочешь жить со мной..."
    melanie "То ты..."
    melanie "Ты должен сделать это..." # Смущенно отворачивается
    # Алекс вовсе не возражает
    img 18973
    alex_photograph "Я сейчас..."
    alex_photograph "Дай мне пару минут."
    alex_photograph "Я сейчас все сделаю, Мелани."
    # он снова гладит ее бедра, она переворачивается на живот
    # он начинает мять попу
    img 18974
    w
    img 18975
    alex_photograph "Ммммм... Какие формы..."
    # потом приближает свой полувялый член к ее попе и начинает им водить туда-сюда по ягодицам, трется
    # у него начинает вставать
    # Мелани снова бросает обеспокоенный взгляд в камеру
    img 18976
    w
    img 18977
    w
    img 18978
    alex_photograph "Мммм..."
    img 18979
    melanie "Алекс?"
    alex_photograph "Да, Мелани?"
    melanie "Ты точно не против жить со мной?"
    melanie "Ты точно этого хочешь?"
    img 18980
    alex_photograph "Да!"
    alex_photograph "Я о таком даже мечтать не мог!"
    # Алекс начинает вводить член в ее киску, вводит наполовину
    img 18981
    melanie "Точно? Ты в этом уверен?"
    alex_photograph "Конечно, Мелани!"
    # он вводит в нее головку и спрашивает
    alex_photograph "Мелани, ты не передумала?"
    alex_photograph "Я могу войти в тебя глубже?"
    melanie "Я не передумала, Алекс..."
    # он вводит головку полностью
    img 18982
    alex_photograph "Точно?"
    alex_photograph "Я могу полность войти в твою киску, Мелани?"
    melanie "Алекс, сделай уже это!"
    melanie "Я не передумала!"
    # Алекс входит в нее, начинает двигаться
    img 18983
    alex_photograph "Ооооо!!!"
    img 18984
    alex_photograph "Как же хорошо!"
    img 18985
    alex_photograph "Не могу поверить, что мой член внутри такой топ-модели!!"
    alex_photograph "Оооох..."
    img 18986
    alex_photograph "У тебя миллионы поклонников!"
    img 18987
    alex_photograph "Но именно мне выдался шанс трахать тебя!"
    alex_photograph "Даааа!!!"
    # смена кадра, офис Дика
    # Виктория продолжает смотреть в монитор и ласкать себя
    # смена кадра на апартаменты Мелани
    # потом Алекс останавливается
    img 18970
    w
    img 18988
    alex_photograph "Мелани, я хочу видеть твое лицо!"
    alex_photograph "Давай, поменяем позу?"
    # Мелани говорит ему равнодушно
    img 18989
    melanie "На сегодня достаточно, Алекс..."
    melanie "Секс уже был."
    img 18990
    alex_photograph "Но Мелани!"
    alex_photograph "Раз ты не кончила, значит секса не было!"
    # Мелани смотрит на камеру, злится
    img 18991
    melanie "!!!"
    img 18992
    melanie "Какую позу ты хочешь, Алекс?"
    alex_photograph "Я хочу, чтобы ты смотрела мне в глаза."
    alex_photograph "Хочу увидеть, как ты кончаешь!"
    melanie "Мне перевернуться?"
    alex_photograph "Нет, давай по-другому..."
    alex_photograph "Садись на меня..."
    # Мелани медлит
    img 18993
    melanie "..."
    melanie "Я не очень люблю эту позу..."
    alex_photograph "Ну, Мелани!"
    alex_photograph "Давай!"
    alex_photograph "Хотя бы чуть-чуть!"
    # Мелани смотрит на камеру, потом нехотя соглашается
    img 18994
    melanie "Хорошо..."
    melanie "Ложись на кровать."
    # Алекс довольный ложится на спину
    # Мелани свысока смотрит на него, на его член
    # потом нехотя садится на него, смотрит на камеру, потом в его глаза
    # секс, Мелани сверху, она начала получать удовольствие от процесса, стонет
    # Алекс периодически мнет ее груди, гладит ее бедра
    img 18995
    w
    img 18996
    w
    img 18997
    alex_photograph "Ооооо!!!"
    alex_photograph "Как же хорошо!"
    alex_photograph "Ты само совершенство, Мелани..."
    # смена кадра, офис Дика
    # Виктория продолжает смотреть в монитор и ласкать себя
    # смена кадра на апартаменты Мелани
    img 18970
    w
    img 18998
    alex_photograph "Звезда мира моды! Знаменитость!"
    alex_photograph "Сколько журналистов гадали, какая твоя киска на вкус!"
    img 18999
    alex_photograph "Оооо..."
    img 19000
    alex_photograph "Тебя желает пол мира!!!"
    img 19001
    alex_photograph "А трахаю тебя Я!!!"
    alex_photograph "Ааааа!!"
    img 19002
    alex_photograph "Оооох..."
    melanie "Мммм..."
    img 19003
    alex_photograph "Ааааа!!"
    img 19004
    alex_photograph "Мммм..."
    img 19005
    alex_photograph "Даааа... Продолжай таааак..."
    melanie "Мммм..."
    img 19006
    alex_photograph "Быстрее..."
    # Мелани кончает первой, Алекс следом за ней
    img 19007
    melanie "Ооооо!!"
    melanie "ОООООО!!!"
    menu:
        "Кончить внутрь Мелани.":
            img 19008
            alex_photograph "Я сейчас кончуууу!!!"
            melanie "Не вздумай кончать в меня!"
            # она хочет встать, но Алекс хватает ее за бедра и удерживает, кончает внутрь
            img 19009
            alex_photograph "ААА!"
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            img 19010
            melanie "Черт!"
            melanie "Алекс!"
            melanie "!!!"
            # испуганный взгляд на камеру
            pass
        "Кончить на киску Мелани.":
            img 19008
            alex_photograph "Я сейчас кончуууу!!!"
            alex_photograph "ААА!"
            melanie "Не вздумай кончать в меня!"
            # Мелани приподнимается и он кончает на нее
            img 19009
            alex_photograph "АААААА!!"
            alex_photograph "ААААААААА!!!"
            img 19011
            w
            img 19012
            # Мелани смотрит недовольно на камеру
            pass
    # смена кадра, офис Дика
    # Виктория кончает
    img 18970
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
