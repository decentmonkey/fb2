default monicaClareStoryAboutLife = False   # Моника рассказывает Клэр правду о себе
default monicaMollyFoto = False   # Моника разрисовала портрет Молли

# Паб. Гримерка танцовщиц. На работе Молли.
label ep210_dialogues4_dance_strip_1:
    # рыжая сидит возле зеркала, Моника стоит в дверях
    # Моника недовольно
    img 16130
    mt "Черт! Совсем забыла, что сегодня здесь звезда трущоб..."
    mt "Не хочу разговаривать с этой дрянью!"
    # Моника проходит в гримерку и подходит к вешалке рядом со столиком Клэр
    img 16132
    m "..."
    img 22815
    # рыжая ей, не поворачиваясь,
    img 22667
    w
    img 16131
    molly "Эшли говорит, что твоими выступлениями довольны посетители..."
    molly "И хотят видеть тебя чаще на сцене..."
    # Моника поворачивается и зло смотрит на нее
    img 16133
    m "И что?"
    img 16134
    mt "На что эта дрянь намекает?"
    mt "Ее бесит, что она, может быть, уже и не звезда?"
    # рыжая смотрит на Монику зло
    img 16135
    molly "Я тебя предупреждаю, шлюха!"
    molly "Если из-за тебя я потеряю хотя бы один цент от своего заработка..."
    molly "Я сделаю все, что бы тебя выкинули отсюда..."
    img 16136
    molly "Или отправлю тебя за решетку, мошенница..."
    molly "Там тебе и место!"
    molly "!!!"
    img 16137
    menu:
        "Клэр предупреждала, что лучше не конфликтовать с ней":
            # отворачивается от Молли, послав ей убийственный взгляд
            img 22823
            m "!!!"
        "Да, Клэр предупреждала. Но я не могу просто проигнорировать такую наглость!":
            # Моника ей высокомерно в ответ
            img 16138
            m "Что я слышу?.."
            m "Мне угрожает сама звезда паба Shiny Hole?!"
            img 16139
            m "Ты серьезно?!"
            m "Думаешь, что ТЫ можешь испугать меня чем-то?!"
            m "!!!"
            img 16134
            mt "Никчемная бесполезная дрянь!"
        "Взять стул и ударить эту сучку!":
            # Моника смотрит на стул, потом зло на Молли
            # арт стула крупным планом можно взять готовый
            img 22822
            mt "Черт!!!"
            mt "Не хватало еще мне проблем с полицией из-за этой сучки!"
            img 22823
            m "..."
            mt "Но когда-нибудь я не сдержусь и сделаю это!"
            m "!!!"
    # рыжая зло смотрит на Монику
    img 16140
    molly "!!!"
    # Моника отворачивается от нее
    mt "Не могу выносить ее присутствия!"
    mt "Надо скорее одеться и идти на сцену."
    m "..."
    $ log1 = _("Выйти на сцену паба и танцевать.")
    return

# далее в этот день все, как обычно. Моника выступает на сцене, потом переодевается, платит проценты Эшли и уходит

# на другой день
# Паб. Гримерка танцовщиц. На работе Клэр.
label ep210_dialogues4_dance_strip_2:
    # Клэр сидит за своим столиком, Моника стоит в дверях
    # Моника задумчиво смотрит на Клэр
    img 22709
    w
    img 22711
    mt "Надо будет узнать у нее, как она догадалась использовать хлыст..."
    mt "Хлыст от извращенцев."
    mt "Эффективная штука. Мне такая просто необходима."
    # Клэр в маске поворачивается к Монике, с улыбкой
    img 16141
    clare "Привет, [monica_pub_name]!"
    clare "Джо больше не приставал?"
    img 16142
    m "Нет,не приставал. Твой инструмент для отпугивания был..."
    m "Весомым арументом больше не лезть ко мне."
    # проходит в гримерку к вешалке
    img 22714
    clare "Да, я никогда с ним не расстаюсь."
    clare "Клиенты не обижают?"
    img 22715
    m "Пока все нормально. Сцена меня уже не так пугает как поначалу..."
    img 22716
    clare "Ты скоро научишься получать от этого удовольствие."
    img 16143
    mt "Хм, сомневаюсь в этом..."
    img 22723
    clare "[monica_pub_name], ты чем-то еще занимаешься, помимо танцев на сцене?"
    # Моника смотрит на нее, в сомнениях
    img 16144
    m "..."
    menu:
        "Рассказать ей правду.":
            img 22729
            mt "Она была добра ко мне..."
            mt "И даже помогла мне..."
            img 16145
            mt "Прогнав неудачника Джо, когда он прицепился ко мне у сцены..."
            mt "Думаю, я могу сказать ей правду..."
            mt "..."
            img 16146
            m "Я... Для меня..."
            m "Для меня трущобы - это отдельный мир... Который существует где-то далеко..."
            m "И ни при каких обстоятельствах не может появиться в моей жизни."
            img 16147
            clare "???" # смотрит на нее удивленно
            img 22724
            m "В данный момент у меня денежные трудности..."
            m "Поэтому я нахожусь здесь."
            m "Но это временно!"
            img 16148
            m "Я сильная и независимая женщина."
            m "У меня есть успешный бизнес и очень высокое положение в обществе."
            img 16149
            m "Потратить несколько тысяч долларов на платье с последней коллекции..."
            m "Что бы надеть его всего один раз на какое-нибудь мероприятие..."
            m "Это для меня в порядке вещей."
            img 16150
            clare "А почему ты тогда здесь?" # смотрит на нее удивленно
            img 16151
            m "..."
            m "Мне нужно еще немного времени и я решу свои... Небольшие проблемы..."
            img 16152
            m "И снова буду управлять своим бизнесом и сотнями подчиненных."
            m "Сидя в своем кабинете на своем кресле босса."
            clare "!!!"
            img 16153
            m "Просто мне сейчас нужно немного подзаработать денег..."
            m "Танцуя здесь..."
            m "..."
            img 16154
            clare "Ого! Ничего себе!"
            clare "Слушай, ну если вдруг тебе понадобится помощь..."
            clare "Ты всегда можешь обратиться ко мне."
            m "..."
            img 16155
            clare "А [monica_pub_name]..."
            clare "Это твое настоящее имя?"
            img 16156
            m "Нет. Это выдуманное имя. Специально для этой дыры."
            m "На самом деле я Миссис Бакфетт."
            m "Моника Бакфетт."
            img 16157
            clare "Мне можно обращаться к тебе просто Моника?"
            img 16158
            m "Да, но только когда мы вдвоем."
            m "Я не хочу, чтобы здесь узнали мое настоящее имя."
            img 16159
            clare "Моника, можешь рассказать мне, из-за чего у тебя эти..."
            clare "Временные денежные трудности."
            clare "Или из-за кого?"
            m "..."
            img 16160
            mt "Я и так рассказала ей слишком многое о себе..."
            img 16161
            m "Просто произошло небольшое недоразумение..."
            m "Которое я скоро устраню."
            img 16162
            clare "Небольшое недоразумение - это мужчина?"
            img 16163
            mt "Точнее и не скажешь."
            mt "А она догадливая..."
            img 16164
            m "Да. Мужчина."
            img 16165
            clare "Я так и подумала!"
            clare "Наверное, к другой ушел?!"
            img 16166
            m "..."
            clare "Вот сволочь!"
            clare "!!!"
            img 16167
            m "Только... Не рассказывай никому..."
            clare "Не переживай. Я на твоей стороне."
            img 16168
            m "Спасибо..."
            m "А ты, Клэр?"
            img 16169
            m "Какое у тебя настоящее имя?"
            m "Ты где-нибудь еще работаешь?"
            $ monicaClareStoryAboutLife = True # Моника рассказала Клэр правду о себе
            pass
        "Соврать ей.":
            img 16170
            mt "Клэр, конечно, ничего плохого мне не сделала..."
            mt "И даже помогла мне..."
            mt "Прогнав неудачника Джо..."
            mt "Когда он прицепился ко мне у сцены, но..."
            img 16171
            mt "Я не могу признаться, что работаю гувернанткой... Притом в своем бывшем доме..."
            mt "..."
            mt "Да и все остальное..."
            mt "Не хочу, чтобы здесь кто-то знал обо мне правду."
            img 16149
            m "..."
            m "Я? Конечно!"
            m "Вообще, у меня есть успешный бизнес и очень высокое положение в обществе."
            m "И, в принципе, я ни в чем не знаю нужды..."
            img 16150
            clare "А почему ты тогда здесь?" # смотрит на нее удивленно
            img 16172
            m "Мои подруги соответствуют моему уровню."
            m "Такие люди как я, как правило, перепробовали все виды удовольствия в жизни..."
            m "Познали все виды роскоши и..."
            img 16148
            m "Для того, чтобы получить немного адреналина, мы с подругами решили поспорить..."
            m "Что я не смогу месяц прожить без всех тех удобств и комфорта..."
            m "К которому привыкла."
            m "Чтобы выиграть спор, я должна была устроиться на работу где-нибудь в трущобах..."
            img 16152
            m "И жить только на заработанные деньги."
            m "Притворившись обычной девушкой, без денег."
            m "Естественно, это все временно."
            img 16173
            m "Это такой своего рода эксперимент. И скоро он закончится."
            m "И я вернусь в свой роскошный дом с прислугой."
            m "И в свою комфортную беззаботную жизнь."

            clare "Ого!"
            clare "Ты меня удивила!"
            clare "Какой-то странный спор..."
            img 16153
            m "Да. Но нам с подругами захотелось поэкспериментировать..."
            m "Посмотреть, так сказать, на другую жизнь."
            m "Только... Не рассказывай никому..."
            
            clare "Не переживай. Я на твоей стороне."
            clare "А [monica_pub_name]..."
            clare "Это твое настоящее имя?"
            m "Нет. Это выдуманное имя. Специально для этой дыры."
            m "На самом деле я Миссис Бакфетт."
            m "Моника Бакфетт."
            clare "Мне можно обращаться к тебе просто Моника?"
            m "Да, но только когда мы вдвоем."
            m "Я не хочу, чтобы здесь узнали мое настоящее имя."
            m "..."
            m "А ты, Клэр?"
            m "Какое у тебя настоящее имя?"
            m "Ты где-нибудь еще работаешь?"
            pass
    # Клэр, загадочно улыбаясь
    img 16174
    clare "Я? Да так..."
    clare "Ничего серьезного. Так... Случайные подработки..."
    clare "Не сравнится с тем, что рассказала мне ты, Моника."
    img 16175
    clare "И мое имя - не псевдоним. Меня и правда зовут Клэр."
    clare "..."
    clare "Мы с тобой заболтались. Тебе пора одеваться и идти на сцену."
    img 16176
    mt "Черт! Снова эта сцена! И толпа пьяных неудачников!"
    m "..."
    $ log1 = _("Выйти на сцену паба и танцевать.")
    return

# далее в этот день все, как обычно.

# Паб. Гримерка танцовщиц. На работе Молли.
label ep210_dialogues4_dance_strip_3:
    # рыжая сидит возле зеркала, Моника стоит в дверях
    # Моника недовольно
    mt "Не хочу разговаривать с этой дрянью!"
    # Моника проходит в гримерку и подходит к вешалке рядом со столиком Клэр
    m "..."
    # рыжая смотрит на нее зло, но ничего не говорит
    molly "!!!"
    # потом отворачивается к зеркалу
    # Моника переодевается
    mt "Не могу выносить ее присутствия!"
    mt "Надо скорее одеться и идти на сцену."
    m "..."
    $ log1 = _("Выйти на сцену паба и танцевать.")
    return


# после выступления Моники на сцене, она заходит в гримерку
# Паб. Гримерка танцовщиц. На работе Молли.
label ep210_dialogues4_dance_strip_4:
    # Моника заходит в гримерку
    # сразу после того, как Моника переоделась в свой наряд шлюхи, в гримерку забегает Молли
    # Молли начинает орать на Монику
    molly "Воровка!"
    molly "Я знала, что ты не чиста на руку, сучка!"
    molly "Решила прикарманить мои деньги!!!"
    molly "Дрянь! Мошенница!!!"
    # Моника в шоке
    m "Что происходит?!"
    m "!!!"
    m "Ты чего разоралась?! Какие деньги?!"
    molly "И не притворяйся, что ты тут ни при чем!!!"
    m "Ты что, дрянь, совсем головой поехала?!"
    m "Какого черта ты тут разоралась?!"
    m "!!!"
    # на шум приходит Эшли
    ashley "Что здесь происходит?!"
    ashley "Вас слышно даже у барной стойки!!!"
    ashley "У меня клиенты просятся сюда и предлагают деньги..."
    ashley "Чтобы посмотреть на битву сучек!"
    # Молли орет, тыча пальцем в Монику
    molly "Эта дрянь украла у меня мои деньги!!!"
    molly "Они всегда были в этой банке на столике!"
    molly "Сейчас там пусто!!!" # банка крупным планом, пустая
    molly "Кроме нее никого в гримерке сегодня не было!"
    molly "Это сделала она!"
    m "Что?!"
    m "!!!"
    molly "Я просто так этого не оставлю!"
    molly "Я требую вернуть мои деньги! А эту шлюху наказать!!!"
    # Эшли строго смотрит на Монику
    ashley "Это правда?!"
    # Моника возмущенно
    m "Конечно, нет!"
    m "Это какой-то бред!!!"
    m "Эта стерва специально все подстроила!!!"
    mt "Вот сучка!!!"
    mt "Ненавижу!"
    mt "!!!"
    # Молли продолжает орать
    molly "Эшли, ты сама мне рассказывала..."
    molly "Что эта дрянь воровала твои чаевые!!!"
    molly "Значит это она украла мои деньги!!!"
    molly "Я сейчас проверю ее карманы!"
    molly "Наверняка, она спрятала их там!"
    # подходит к Монике
    # Моника ее останавливает
    m "Какого черта ты тут устроила?!"
    m "Не прикасайся ко мне!!!"
    # Молли смотрит на нее насмешливо и говорит, обращаясь к Эшли
    molly "Вот видишь, Эшли?!"
    molly "Эта дрянь боится, что я найду там деньги!"
    molly "Которые она у меня украла!!!"
    m "!!!" # зло
    ashley "Сколько там было денег?"
    molly "1000 баксов!"
    # Эшли строго смотрит на Монику, подходит к ней
    ashley "[monica_pub_name], показывай, что у тебя в карманах!"
    ashley "Иначе я сама проверю их!"
    m "У меня нет ничего в карманах!"
    # Эшли засовывает руку во внутренний карман ее куртки, попутно лапая ее за грудь, Моника зло на нее смотрит
    mt "!!!"
    mt "Извращенка!"
    # Эшли вытаскивает из кармана купюры
    # Моника растерянно смотрит на них
    molly "Вот!!! Я же говорила!!! Она воровка!!!"
    m "Но... Я... Я не брала этих денег!"
    mt "!!!"
    # смотрит зло на Молли
    mt "Вот сучка!!!"
    m "Эшли! Она специально это подстроила!"
    m "Она хочет, чтобы ты выгнала меня отсюда!"
    m "Потому что я популярнее, чем она!!!"
    molly "Это не так!"
    molly "Она воровка!!!"
    molly "Эшли, вызывай полицию!"
    mt "!!!"
    ashley "Молли заткнись! Я сама разберусь!" # обращаясь к Молли
    ashley "Никакой полиции!"
    ashley "Я сама накажу [monica_pub_name], чтобы думала в следующий раз!"
    # Моника рассержена
    m "!!!"
    m "За что меня наказывать?!"
    m "Я ни в чем не виновата!!!"
    ashley "Так, [monica_pub_name], хватит!!!"
    m "!!!"
    ashley "Как мы будем решать эту проблему?"
    ashley "Это не первый раз, когда ты присваиваешь чужие деньги!"

    # если извинялась в подсобке перед Эшли
    ashley "А потом просишь простить тебя, извиняешься..."
    ashley "Пользуешься моей добротой..." # хитро смотрит на Монику
    ashley "И после этого снова крадешь деньги!" # снова строго

    ashley "Я просто так тебе этого не могу простить..."
    m "..."
    ashley "Я тебя оштрафую! Ты теперь должна отдавать мне все свои чаевые!"
    ashley "Пока Молли не простит тебя!"
    ashley "Она самая популярная девочка в этом пабе..."
    ashley "Ее слова для меня значат больше, чем твои, [monica_pub_name]..."
    m "ЧТО?!" # возмущенно
    # Эшли уходит, Моника злобно смотрит на Молли
    m "Сучка!"
    molly "..." # насмешливый высокомерный взгляд
    mt "Ненавижу!!!"
    mt "!!!"
    # та на нее смотрит свысока и уходит из гримерки
    molly "..."
    $ log1 = _("Из-за это рыжей сучки я теперь должна отдавать все свои чаевые Эшли! Ненавижу ее!!!") # квест лог
    return

# Паб. Гримерка танцовщиц.
label ep210_dialogues4_dance_strip_5:
    # Моника в ярости, смотрит на фото Молли на стене
    mt "Никчемная!"
    mt "Бесполезная!"
    mt "Сучка!!!"
    mt "!!!"
    # переводит взгляд на помаду на столике
    mt "Хммм..." # задумывает мелкую пакость
    mt "..."
    menu:
        "Взять помаду и испортить фото рыжей сучки.":
            $ monicaMollyFoto = True # Моника разрисовала портрет Молли
            pass
        "Не делать этого.":
            mt "Идея хорошая, но..."
            mt "Эта дрянь сразу поймет, что это сделала я..."
            mt "И снова мне подкинет деньги."
            mt "Или сделает какую-нибудь другую гадость."
            mt "..."
            mt "У меня и без нее проблем хватает."
            return False
    # берет помаду, подходит к потрету и рисует на нем член? кровь? рога и хвост? просто замазывает помадой?
    # потом ухмыляется довольно
    mt "Шедеврально!"
    mt "!!!"
    return

# Паб. Гримерка танцовщиц. На работе Клэр.
label ep210_dialogues4_dance_strip_6:
    # Клэр сидит за своим столиком, Моника стоит в дверях
    mt "Интересно, Клэр в курсе того, что произошло?"
    # Клэр поворачивается к ней
    clare "Моника, привет! Как ты?"
    clare "Наша звезда все-таки разозлилась на тебя?"
    # Моника удивленно
    mt "!!!"
    m "Ты в курсе?"
    clare "Да. Не переживай."
    clare "Я уверена, что это она специально все подстроила..."
    m "Я в этом не сомневаюсь!"

    # если Моника разрисовала портрет Молли
    # Клэр улыбаясь говорит
    clare "Кстати, отличный портрет получился!"
    clare "Наша звезда прямо-таки засияла..."
    #
    $ notif(_("Моника разрисовала фотографию Молли"))
    #
    m "Нет-нет... Я тут ни при чем... Я ничего не делала."
    # Клэр смотрит на нее и улыбается
    clare "Все ок. Я никому не скажу."

    clare "По поводу твоего наказания... Это несправедливо."
    clare "У меня есть план..."
    clare "Жди здесь."
    clare "Мне надо поговорить с Эшли..."
    # Клэр выходит из гримерки
    # Моника в растерянности
    mt "Клэр пошла заступаться за меня?!"
    mt "???"
    mt "..."
    mt "Наверное, попросит что-то взамен за это..."
    mt "..."
    mt "Надеюсь, не какое-нибудь извращение..."
    # возвращается Клэр вместе с Эшли
    # Эшли стоит руки в боки и строго смотрит на Монику
    ashley "Ладно, [monica_pub_name]."
    ashley "Мне тут Клэр предложила помочь тебе отработать штраф..."
    ashley "В общем, ты можешь выйти на сцену вместе с Клэр..."
    mt "???" # удивленно на Клэр, потом снова на Эшли
    ashley "Будете танцевать вдвоем."
    ashley "Все чаевые от выступления отдашь мне..."
    ashley "И я забуду про тот случай с Молли..."
    mt "!!!" # удивленно
    ashley "Или, если хочешь, разберись с Молли..."
    ashley "Советую тебе перед ней извиниться."
    ashley "Только не устраивать тут больше битву сучек!"
    mt "Извиняться перед этой никчемной сучкой?!"
    mt "!!!"
    ashley "И чтобы ничего, связанного с воровством, больше не было!!!" # грозно
    ashley "Еще раз сделаешь подобную хрень..."
    ashley "Ты просто так не отделаешься!!!"
    ashley "Ясно тебе, [monica_pub_name]?!"
    # Эшли уходит
    return

# переход на движок
# мысли Моники
# Паб. Гримерка танцовщиц, Клэр сидит у своего зеркала.
label ep210_dialogues4_dance_strip_7:
    # не рендерить!!!
    mt "..."
    mt "И что мне делать?!"
    mt "???"
    menu:
        "Попросить прощения у рыжей сучки. (в следующем обновлении)":
            mt "Возможно, мне стоит попытаться найти с этой дрянью общий язык?"
            mt "Чтобы быть уверенной в том, что она мне больше не будет пакостить..."
            mt "Ведь если Эшли меня простит после танца с Клэр..."
            mt "Эта рыжая сучка взбесится еще больше."
            mt "Мне нужно подумать об этом..."
            mt "..."
            return False
        "Танцевать с Клэр. (доступно при открытии всех движений на сцене)":
            mt "Я ни за что не буду просить прощения у этой рыжей сучки!"
            mt "Ненавижу ее!!!"
            mt "Танец с Клэр - отличный способ разрешить сложившуюся ситуацию."
            mt "И позлить эту рыжую дрянь!"
            mt "Интересно, что она сделает, когда узнает об этом?"
            mt "..."
            return
    return

# Паб. Гримерка танцовщиц, Клэр сидит у своего зеркала.
# клик на Клэр
# выбран пункт меню "Танцевать с Клэр"
label ep210_dialogues4_dance_strip_8:
    # если опция доступна, т.е. все движения на сцене открыты
    # Моника растерянно
    m "Я... Я не ожидала, что ты..."
    m "Поможешь мне..."
    clare "Да ладно! Ничего сложного для меня в этом нет."
    m "Я что-то должна тебе за это?"
    # Клэр удивленно
    clare "Нет, конечно! О чем ты?!"
    clare "Просто старайся больше не конфликтовать с нашей звездой..."
    mt "Я ей ничего не должна?"
    mt "Хммм..."
    mt "Может, здесь какой-то подвох?"
    mt "..."
    m "Клэр, а как мы будем танцевать вдвоем?"
    m "Я так ни разу не танцевала..."
    clare "Моника, все получится отлично, вот увидишь!"
    clare "Мужчин в зале это крайне порадует."
    clare "Переодевайся и выходи на сцену. Я присоединюсь к тебе во время твоего танца."
    clare "Покажем им, кто здесь звезды!"

    # если опция недоступна, движения открыты не полностью
    m "Клэр, а как мы будем танцевать вдвоем?"
    m "Я так ни разу не танцевала..."
    clare "Моника, все получится отлично, вот увидишь!"
    clare "Только сначала тебе нужно набраться больше опыта..."
    clare "Ты еще слишком скованна на сцене."
    m "..."
    $ log1 = _("Выйти на сцену паба и танцевать.")
    return

# во время танца Моники и Клэр из зала кричит Эшли
label ep210_dialogues4_dance_strip_9:
    # во время выступления из зала
    ashley "Давайте, девочки!!!"
    ashley "Покажите этим денежным мешкам, у кого самые аппетитные попки!"
    ashley "Пусть раскошеливаются!!!"
    return

# если был танец вдвоем с Клэр
# Паб. Гримерка после танца с Клэр.
label ep210_dialogues4_dance_strip_10:
    # использовать арты из идентичной сцены в версии 0.9
    # Моника отдает Эшли заработанные за двойной танец чаевые
    # Эшли требовательно
    ashley "[monica_pub_name], сколько вы заработали чаевых?"
    m "Сегодня мы заработали [monica_strip_tips_today]."
    ashley "Скажи спасибо Клэр."
    ashley "Я прощаю тебя... И чтобы больше никакой ругани с Молли!"
    ashley "Кстати, было отличное выступление!"
    ashley "Клиентам понравилось!" # с улыбочкой
    ashley "Думаю, нам нужно ввести это в программу."
    mt "В принципе, идея неплохая..."
    mt "Чаевых намного больше..."
    mt "Жаль их сейчас было отдавать Эшли..."
    mt "Из-за какой-то рыжеволосой сучки!"
    mt "!!!"
    ashley "На сегодня ты свободна, [monica_pub_name]."
    return

# если был танец вдвоем с Клэр
# Паб. Гримерка танцовщиц. На работе Молли.
label ep210_dialogues4_dance_strip_11:
    # рыжая сидит возле зеркала, Моника стоит в дверях
    mt "Какая же она сучка!"
    mt "Решила подставить меня с деньгами перед Эшли!"
    mt "Меня, Монику Бакфетт!"
    mt "Дрянь!"
    mt "!!!"
    # Моника проходит в гримерку и подходит к вешалке
    # рыжая ей, не поворачиваясь
    molly "Слышала, Эшли тебя простила..."
    molly "Клэр тебе помогла..."
    # Моника поворачивается и зло смотрит на нее
    m "И что?"
    m "Тебе какое дело?"
    # Молли, также не поворачиваясь к Монике
    molly "Смотрю, ты тут хорошо устроилась..."
    molly "Ну что ж..."
    molly "Посмотрим, надолго ли..." # злобно
    mt "!!!"
    mt "Она специально меня провоцирует на..."
    mt "На битву сучек, как Эшли это назвала..."
    mt "Эшли меня предупредила, что больше такого не должно быть..."
    mt "Я просто не буду разговаривать с этой дрянью."
    mt "..."
    mt "Как было бы хорошо, если бы ее тут просто не стало."
    mt "Может, все-таки стоит двинуть ей стулом по голове?"
    mt "..."
    # рыжая поворачивается к Монике и смотрит на нее зло
    molly "Ты здесь долго не продержишься, поняла?"
    molly "Я сделаю все для того, чтобы тебя вышвырнули отсюда!!!"
    molly "Советую тебе искать другое место для заработка."
    molly "Например, в подворотне."


    # если Моника разрисовала портрет Молли
    molly " И кстати!"
    #
    $ notif(_("Моника разрисовала фотографию Молли"))
    #
    molly "Еще раз увижу, что ты испортила мой портрет!"
    molly "Простым штрафом ты не отделаешься, сучка!!!"

    # отворачивается от Моники к зеркалу
    # Моника смотрит злобно
    mt "Дрянь!"
    mt "!!!"
    mt "Ненавижу!!!"
    $ log1 = _("Выйти на сцену паба и танцевать.")
    return

# Паб. Моника на сцене.
label ep210_dialogues4_dance_strip_12:
    # во время танца или сразу после него, когда Моника еще не ушла со сцены, с нее падают трусики
    # чаевые бешенно растут
    # Моника наклоняется, поднимает трусики
    # испуганно прикрывается и убегает со сцены, сверкая голой попой
    return

# Паб. Моника в гримерке после выступления, когда упали трусики.
label ep210_dialogues4_dance_strip_13:
    # не рендерить!!!
    # Моника переоделась в свою одежду и думает
    mt "Какой кошмар!"
    mt "Я стояла без трусиков перед толпой пьяных неудачников!!!"
    mt "!!!"
    mt "Как это могло произойти?!"
    mt "Что случилось?"
    mt "???"
    mt "Я столько раз танцевала в этих трусиках..."
    mt "Всегда все было хорошо, а тут..."
    mt "..." # выражение лица меняется, Монику посетила догадка
    mt "Хмммм..."
    mt "А возможно?.."
    # смотрит на трусики, они лежат где-нибудь на стуле
    mt "Возможно, что они не порвались на мне во время выступления..."
    mt "Возможно, что их кто-то порвал еще ДО того, как я их надела!!!"
    mt "!!!"
    mt "И этим 'кто-то' мог быть только один человек!"
    mt "Сучка Молли!!!"
    mt "!!!"
    return

# Паб. Моника, после того, как отдала процент от чаевых Эшли (сразу после dialogue_5_dance_strip_22).
label ep210_dialogues4_dance_strip_14:
    ashley "И кстати!"
    ashley "Тебе не кажется, что надо выступать вообще без трусиков, а?" # улыбочка
    m "Нет!"
    m "Мне так не кажется!"
    m "!!!"
    ashley "А что тут такого?"
    ashley "Ты видела, как публике это понравилось?"
    ashley "В следующий раз выйдешь на сцену без одежды..."
    ashley "Это привлечет в мой паб больше клиентов..."
    ashley "Значит, ты заработаешь больше чаевых."
    ashley "Тебе то какая разница, ты же в маске будешь."
    ashley "Как представлю тебя на сцене... Да еще и с голой попкой..."
    ashley "Ты будешь настоящей звездой, [monica_pub_name]!"
    m "Я не собираюсь выступать голая!!!"
    m "!!!"
    mt "Эта извращенка так и ждет, когда я выйду голая на сцену!"
    mt "Я не буду танцевать голой!"
    mt "Если меня кто-нибудь узнает, несмотря на мою маску..."
    mt "Боюсь даже думать о последствиях!"
    mt "!!!"
    return

# Паб. Гримерка танцовщиц. На работе Клэр.
label ep210_dialogues4_dance_strip_15:
    # Клэр сидит за своим столиком, Моника стоит в дверях
    mt "Наверняка, Клэр уже знает о том, что..."
    mt "Что я стояла с голой попой на сцене."
    # Клэр поворачивается к ней
    clare "Моника, привет! Как ты?"
    m "Привет, Клэр."
    m "Если не считать, что на прошлом выступлении с меня упали трусики..."
    m "И я стояла на сцене, сверкая голой попой..."
    m "То у меня все просто отлично!"
    clare "Да, я уже слышала об этом."
    clare "Трусики просто так не могли порваться. Их специально кто-то надрезал."
    m "И я догадываюсь, кто именно..."
    clare "..."
    clare "Моника, будь поаккуратнее с Молли..."
    clare "Ты же видишь, что она готова пойти на все..."
    clare "Ради того, чтобы сохранить свое положение звезды Shiny Hole."
    m "Меня эта дрянь не напугает."
    m "Я и не с такими легко справлялась."
    $ log1 = _("Выйти на сцену паба и танцевать.")
    return
    return

# Моника переодевается, добавлен пункт в меню
label ep210_dialogues4_dance_strip_16:
    menu:
        "Надеть костюм с жилетом.":
            pass
        "Надеть только трусики.":
            pass
        "Выйти на сцену голой":
            mt "Я же буду не совсем голая. На мне будет маска..."
            mt "Зато я смогу заработать много чаевых."
            mt "Меня все равно никто здесь не знает..."
            mt "..."
            pass
    return


############################################ в след. апдейте
# Джо или Эшли будут заставлять танцевать приват для сотрудника банка (т.к. у них кредит)
# Моника танцует голая, клиент может ее потрогать
# один из клиентов ей говорит, да ладно Мэрилин, снимай маску. я знаю, что это ты
# Моника снимает маску, а клиент говорит, фигасе, а я сомневался, что это ты. даже у Джо спросил, тот говорит, что это не ты
