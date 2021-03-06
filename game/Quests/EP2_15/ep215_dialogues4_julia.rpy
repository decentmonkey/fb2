
default monicaJuliaVictoriaOffice1 = False # Виктория приходила в офис к Юлии и пила с ней вдвоем чай
default monicaJuliaVictoriaOffice2 = False # офисные работники сплетничают о фотосессии Моники перед инвесторами

#call ep215_dialogues4_julia_1() # айтишник, чаепитие без трусов (Виктория и Юлия)
#call ep215_dialogues4_julia_2() # рабочий кабинет Моники Виктория уходит
#call ep215_dialogues4_julia_3() # близняшки и Лин сплетничают


# при условии, что у Виктории уже был визит в офис Моники
# спустя несколько дней Моника приходит в будний день на работу
label ep215_dialogues4_julia_1:
    # при клике в меню на рабочий кабинет Моники, показываем, как Моника заходит в отдел отчетов
    # ей со всех сторон летит
    fadeblack
    sound snd_lift
    pause 2.0
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 17772
    w
    imgf 32112
    w3 "Добрый день, Миссис Бакфетт!"
    w5 "Здравствуйте, Миссис Бакфетт!"
    w1 "Добрый день!"
    # она сделала лицо кирпичом и не глядя ни на кого идет в свой кабинет
    imgd 17767
    mt "Никчемные людишки. Сидят занимаются никому ненужной работой!"
    mt "И думают, что делают важное дело!"
    mt "Бесполезные!"
    mt "Никчемные!"
    mt "!!!"
    # проходит мимо айтишника, также не глядя на него
    imgf 32113
    sound highheels_short_walk
    w
    # смена кадра, айтишник
    # показываем айтишника за его рабочим столом
    fadeblack 2.0
    music Marty_Gots_a_Plan
    imgfl 31470
    w
    # показываем кадр со спины айтишника, виден его монитор
    # у него на мониторе трансляция видео со скрытой камеры с комнаты отдыха
    # вид из-под стола - две пары женских ног, сидят рядом друг с другом, обе без трусиков (Виктория и Юлия)
    sound keyboard_click
    imgf 32205
    w
    imgd 32139
    w
    sound camera_zoom
    imgf 32140
    w
    sound camera_zoom
    imgd 32141
    w
    # айтишник про себя думает
    imgf 31471
    w2t "Интересно, в этом офисе все ходят без трусиков?"
    w2t "Хммм..."
    imgd 31487
    w2t "Нужно расставить камеры и под другими столами в офисе."
    w2t "И почему я раньше до этого не додумался?"

    # вдруг Виктория раздвигает ноги в показывает в камеру знак V пальцами
    # админ испугался
    imgf 32142
    sound Jump2
    w
    music stop
    sound plastinka1b
    img 32143 hpunch
    w2t "О ЧЕРТ!"
    w2t "Она заметила камеру???"

    # затемнение, смена кадра на кабинет Моники
    return


# рабочий кабинет Моники
label ep215_dialogues4_julia_2:
    # Моника заходит в свой рабочий кабинет
    # смотрит на рабочий стол Юлии, а ее нет на месте
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 32114
    w
    imgf 32115
    mt "Куда делась эта никчемная Юлия?"

    # если есть отношения с Юлией
    if monicaJuliaLoveStory8 == True:
        #
        $ notif(_("Моника состоит с Юлией в отношениях и живет у нее."))
        #
        music Stealth_Groover
        imgd 32116
        mt "Впрочем, это хорошо, что ее нет."
        mt "Наконец-то, я смогу спокойно провести день без этой надоедливой дурочки..."

    # Моника идет к своему столу и тут поворачивает голову в сторону комнаты отдыха
    # в это время в комнате отдыха Виктория встает из-за стола и обращается к Юлии (на Монику они не смотрят)
    # Виктория разговаривает с Юлией очень мило
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 32118
    w
    music Power_Bots_Loop
    img 32117 hpunch
    mt "КАКОГО ЧЕРТА?!"
    mt "!!?!?!!!"
    music Groove2_85
    imgd 32119
    victoria "Юлия, дорогая, спасибо за кофе."
    victoria "Я с удовольствием поболтала бы с тобой еще, но..."
    victoria "К сожалению, мне пора идти по делам."
    # Юлия смотрит на нее с обожанием
    imgf 32120
    julia "Приходите почаще, Мисс Виктория!"
    julia "Мне так нравится проводить с вами время!"
    julia "В следующий раз угощу вас прекрасным зеленым чаем..."
    julia "И куплю что-нибудь вкусненькое."
    # Юлия встает, Виктория своим привычным жестом указывает на свою щеку, Юлия наклоняется к ней и чмокает в щечку
    imgd 32121
    victoria "Спасибо, Юлия! Ты такая милая!"
    victoria "Обязательно загляну к тебе скоро."
    sound kiss2
    imgf 32122
    w
    # камера на Монику, у нее шок и ужас на лице
    music Power_Bots_Loop
    img 32123 hpunch
    mt "ЧТО???"
    mt "ЭТА ДРЯНЬ!!!"
    mt "ТУТ ДЕЛАЕТ?!?!?!"
    # кадр на комнату отдыха
    # Виктория направляется к выходу
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgfl 32124
    # кадр на кабинет Моники и на Монику
    # Виктория проходит мимо нее, Моника смотрит на нее со злым недоумением
    w
    music Power_Bots_Loop
    sound highheels_short_walk
    imgf 32125
    mt "!!!"
    mt "!!!!!!"
    # Виктория с ехидной улыбочкой
    music Groove2_85
    imgd 32126
    victoria "Привет, подружка Моника!"
    victoria "Я знаю, что ты хотела бы поболтать со мной, но у меня дела..."
    victoria "В следующий раз я обязательно уделю тебе свое внимание."
    victoria "И, кстати, моя ценная вещь все еще у тебя?"
    sound snd_woman_laugh3
    # Моника со злостью и раздражением
    # pause 1.5
    # music Power_Bots_Loop
    imgd 32127
    m "!!!"
    m "Да!"
    imgd 32128
    victoria "Хорошо. Скоро я ее заберу."
    victoria "Смотри, не потеряй."
    victoria "Ну все, подружка Моника, пока."
    victoria "Передавай привет нашей подружке Мелани. Хи-хи."
    sound snd_woman_laugh3
    # Виктория уходит
    # Моника в шоке смотрит на Юлию, та убирает чашки со стола
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Pyro_Flow
    imgfl 32129
    mt "Что эта сучка Виктория пытается вынюхать здесь!?"
    mt "Зачем она общается с никчемной дурочкой Юлией?"

    # если отношений с Юлией нет, то Моника рявкает на нее
    imgf 32130
    m "Юлия, тебе платят за то, что бы ты занималась работой, а не всякой ерундой!!!"
    m "Или ты забыла свое место!? Хочешь вылететь с этой работы?"
    sound highheels_run1
    imgd 32131
    m "РАБОТАТЬ!!!"
    m "ЖИВО!!!"
    julia "Д-да, М-м-миссис Бакфетт..." # испуганно
    julia "Из-звините..."
    # Юлия испуганно бежит к своему столу

    # если отношения с Юлией есть
    if monicaJuliaLoveStory8 == True:
        #
        $ notif(_("Моника состоит с Юлией в отношениях и живет у нее."))
        #
        music Hidden_Agenda
        imgf 17817
        mt "Нужно аккуратно спросить у этой дурочки Юлии, о чем они говорили с Викторией."
        # Моника подходит к Юлии, обнимает за талию
        fadeblack
        sound highheels_short_walk
        pause 1.5
        music Loved_up
        imgfl 32132
        m "Милая, смотрю, вы подружились с Мисс Викторией..."
        # Юлия начинает восторженно рассказывать
        imgf 32133
        julia "О, Миссис Бакфетт! Мисс Виктория такая чудесная. Она очень милая и добрая!"
        julia "Я так счастлива, что мы познакомились с ней."
        julia "Как жаль, что вы не смогли присоединиться к нашему чаепитию! Оно было волшебным!"
        # Моника притворно улыбается
        imgd 32134
        m "Да, Юлия... Мисс Виктория очень милая и добрая девушка..."
        # снова притворно улыбается и целует Юлию
        sound kiss2
        imgf 32135
        w
        imgd 32134
        m "Дорогая, я рада, что твой день начался так чудесно."
        m "А теперь нам пора поработать."
        imgf 32136
        julia "Миссис Бакфетт, я соскучилась..."
        mt "О БОЖЕ!"
        m "Юлия, прости, мне надо работать..."

    # возвращается на свое рабочее место, Юлия - на свое
    fadeblack
    sound highheels_short_walk
    pause 1.5
#    music Groove2_85
    music Pyro_Flow
    imgfl 20253
    w
    imgf 32137
    mt "Виктория! Белобрысая тварь!"
    mt "Притворяется перед Юлией белой овечкой! А сама разнюхивает тут что-то!!!"
    mt "Лицемерная сучка!!!"
    mt "Бесит!!!"
    mt "Ненавижу!!!"
    mt "!!!"

    # Виктория идет мимо админа, кладет ласково на него руку
    # подмигивает
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Marty_Gots_a_Plan
    imgfl 32138
    w
    imgf 32145
    w
    imgd 32144
    sound Jump2
    victoria "Пока, красавчик..."

    # админ в шоке смотрит ей вслед
    imgf 32146
    sound snd_woman_laugh3
    w2t "!!!"
    $ monicaJuliaVictoriaOffice1 = True # Виктория приходила в офис к Юлии и пила с ней вдвоем чай
    return


# при условии, что у Моники была фотосессия перед толпой инвесторов
# через неделю Моника приходит в офис и при клике в меню быстрого перемещения на отдел отчетов
# кадр на сотрудников отдела отчетов
label ep215_dialogues4_julia_3:
    # близняшки и Лин, наклонившись друг к другу, шепчутся, сплетничают
    # сбоку от них стоит серая мышь и периодически пытается участвовать в разговоре
    fadeblack
    music Hidden_Agenda
    imgfl 32147
    w
    imgf 32148
    w
    imgd 32149
    w3 "Помните!?"  # одна близняшка
    w3 "Я говорила вам, что та обложка, где она в красном платье и с голой грудью - это только начало?"
    # Лин и вторая близняшка переглядываясь
    w4 "Да."  # вторая близняшка
    w7 "Помню." # Лин
    # Первая близняшка выпрямилась и огляделась по сторонам
    sound Jump2
    imgf 32150
    w
    imgd 32149
    w3 "Недавно была фотосессия, где она позировала перед толпой каких-то мужчин..."
    w3 "Почти голая!"
    w3 "Представляете?!"
    # Все наклоняются к первой близняшке, прикрыв рот от удивления
#    music Sneaky_Snitch
    imgf 32151
    w4 "Ого!"
    w4 "Серьезно?!"
    # Лин, сдерживая улыбку и радось от интересной сплетни
    sound oooh4
    w7 "Да ладно!?"
    sound oooh1
    sound2 snd_woman_laugh2
    w7 "Не может такого быть!"
    # Первая близняшка вполголоса
    w3 "Это информация из проверенного источника. 100 процентов!"
    # 2-я близняшка с удивлением
    imgd 32152
    w4 "Что, прямо перед толпой мужчин?!"
    w4 "А кто они такие?"
    # Первая близняшка пожимая плечами
    w3 "Не знаю... Говорят, что какие-то богачи!"
    # Серая мышь вклинивается в разговор и все раздражительно оборачиваются на неё
    imgf 32154
    w1 "Но зачем ей это делать? Ради денег?"  # серая мышка в очках
#    music Hidden_Agenda
    imgd 32155
    w7 "Да ну, какие-то глупые слухи..."
    w7 "Денег у нее побольше, чем у каких-то там богачей."
    w7 "И этот журнал..."
    w3 "Говорю же вам, это правда!"
    w7 "Но тогда зачем ей это?"
    w7 "Раз деньги ей не нужны..."
    w3 "Не знаю, но зачем-то она делает это!"
    # спрашивает серая мышка в очках, с негодованием и стеснением
#    music Sneaky_Snitch
    imgf 32153
    w1 "Может быть, ей это нравится?"
    sound snd_woman_laugh2
    # Вторая блезняшка хихикая
    w4 "Может, она извращенка!?"
    # Первая блезняшка хихикая
    w3 "Хорошо, что она тебя сейчас не слышит!"
    sound snd_woman_laugh1

    # если Моника работала манекеном в магазине одежды
    if monicaAgreedToSellDress == True:
        #
        $ notif(_("Моника работала манекеном в магазине одежды."))
        #
        # Лин говорит,оглядываясь по сторонам

        imgd 32156
        w7 "Вообще-то... Я ее уже где-то видела..."
        w7t "Только никак не могу вспомнить, где же?"
        w7t "Хммм..."
        # Все наклоняются к Лин с удивлением и интересом

        w3 "И где же?.."
        w4 "В смысле, где?!"
        w4 "На обложке журнала, где же еще?!"
        w4 "Ну или в интервью."
        w7 "Кстати!"
    #
    imgf 32155
    w7 "Я видела интервью с ней на приеме у Кэмпбелла!"
    w7 "Она говорила, что никогда не стала бы обнажаться перед камерой!"
    # все оборачиваются и с раздражением смотрят на нее
    imgd 32154
    w1 "Я не верю в эти слухи!"
    # Первая близняшка нагибается и говорит вполголоса
    imgf 32157
    w3 "Да я же вам говорю, что информация из достоверного источника."
    # Первая близняшка раздраженно
    w3 "Как вообще такое можно было придумать?!"
    # Вторая близняшка с сарказмом и смехом
    imgd 32158
    w1 "Тебе наврали!"
    w4 "Это что-ли твой любовничек достоверный источник?"
    w4 "Какой-нибудь младший помощник какого-нибудь начальника в каком-нибудь мелком отделе?"
    sound snd_woman_laugh2
    w4 "Хи-хи-хи..."
    w4 "Я даже знаю такого... Работает этажом ниже..."
    w4 "Я как-то видела тебя с ним..."

    # Первая близняшка с раздражением и надменным лицом
    imgf 32159
    w3 "Нет!"
    w3 "Что ты такое говоришь?!"
    w3 "Что бы Я с ним!?"
    w3 "Ни за что!"
    w3 "Ты так говоришь, потому что мне завидуешь и сама хотела бы с ним..."
    w3 "Общаться!"
    # Вторая близняшка с сарказмом и смехом
    w4 "С ним?!"
    w4 "Фуууу!"
    w4 "Конечно, нет!"

    # кадр на Гретту
    # она с грозным видом смотрит на сплетничающих сотрудниц
    music Groove2_85
    imgd 32160
    w6 "Эй, вы! Дуры надутые!"  # Грета
    w6 "Немедленно прекратите эти сплетни на рабочем месте!"
    # сотрудницы межу собой переглядываются
    imgf 32149
    w3 "Достала уже эта жирная корова!"
    w4 "Везде свой нос сует!"
    imgd 32161
    w6 "Так! Вы на работу пришли делом заниматься или сплетничать?!"
    # близняшки и Лин переглянулись
    # тут кто-то из них испуганно
    music stop
    sound plastinka1b
    img 32162 hpunch
    w3 "Бакфетт идет!!!"
    # все пугаются
    music Turbo_Tornado
    w3 "Твою мать!"
    w4 "Быстро все по местам!!!"
    w1 "АААА!!!"
    sound highheels_run2
    pause 2.0
    # затемнение, топот
    $ monicaJuliaVictoriaOffice2 = True # офисные работники сплетничают о фотосессии Моники перед инвесторами
    return
