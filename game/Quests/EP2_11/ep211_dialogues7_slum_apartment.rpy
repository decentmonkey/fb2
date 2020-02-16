default monicaShawarmaApartment1 = False  # Моника спросила у продавца шавермы про квартиру
default monicaShawarmaApartment2 = False  # Моника сразу согласилась посмотреть квартиру продавца шавермы
default monicaShawarmaApartment3 = False  # Моника посмотрела квартиру и согласилась ее арендовать (50 баксов)
default monicaShawarmaApartment4 = False  # Моника согласилась арендовать квартиру за 300 баксов
default monicaShawarmaApartment5 = False # Моника внесла первую оплату Джеку за квартиру
default monicaShawarmaApartment6 = False  # Моника согласилась сделать минет за скидку в 10 процентов
default monicaShawarmaApartment7 = False  # Моника согласилась заняться сексом за скидку в 20 процентов
default monicaShawarmaApartment8 = False  # Моника заплатила $ 300 за квартиру (без скидки)
default monicaShawarmaApartment9 = False  # Джек выселил Монику за неуплату
default monicaShawarmaApartment10 = False  # Моника заплатила денег после ее выселения и снова может жить в квартире

default skip_scenes_list = []

label check_skip_scene(skip_scene_check_name):
    if skip_scene_check_name in skip_scenes_list:
        menu:
            "Продолжить.":
                return False
            "Пропустить.":
                return True
    $ skip_scenes_list.append(skip_scene_check_name)
    return False

# улица Хостела, рядом с пабом, после работы
label ep211_dialogues6_slum_apartment_1:
    # Моника стоит на улице
    mt "Каждый раз, когда прихожу сюда..."
    mt "Боюсь, что встречу ту кошмарную лесбиянку."
    mt "Как вспомню этот ужас в хостеле..."
    mt "Нет! Даже думать об этом не хочу!"
    mt "Тоже мне, дешевый ночлег!"
    mt "!!!"
    mt "Хммм..."
    mt "Кстати, о дешевом ночлеге..."

    # если нет отношений с Юлией и Моника не задумывалась ранее об аренде квартиры
    mt "И почему я раньше об этом не задумывалась?!"
    mt "У меня сейчас есть работа. Заработок у меня стабильный."
    mt "Возможно, мне удастся арендовать какую-нибудь небольшую квартиру?"
    mt "По-моему, это хорошая идея!"
    mt "Я, наконец-то, перестану работать на эту семейку идиотов!"
    mt "И жить независимо ни от кого!!!"
    mt "Только как мне подобрать подходящую по цене квартиру?"
    mt "..."
    #

    # если Моника была в гостях у Юлии и задумывалась об аренде квартиры
    mt "Юлия снимает квартиру в ужасном доме!"
    mt "Но стоит признать, что квартира у нее довольно уютная."
    mt "Конечно, там все старое и убогое..."
    mt "Но все же я была бы не против жить в подобной квартире."
    mt "Представь только, Моника!"
    mt "Никто не будет тебе указывать, что делать и какую одежду носить..."
    mt "Никто не будет ограничивать тебя в еде или в походах в душ..."
    mt "..."
    #

    mt "Кто может знать, где найти дешевое жилье?"
    mt "???"
    mt "В прошлый раз продавец шавермы посоветовал мне хостел..."
    mt "Возможно, стоит спросить у него?"
    $ log1 = _("Спросить у продавца шавермы про аренду квартиры.")
    return

# трущобы, рядом с шавермой
label ep211_dialogues6_slum_apartment_2:
    # не рендерить!
    mt "Уверена, он знает какое-нибудь дешевое жилье."
    mt "Мне эта идея настолько понравилась..."
    mt "И почему я раньше об этом не подумала?"
    return

# разговор с продавцом шавермы, при клике на него
label ep211_dialogues6_slum_apartment_3:
    menu:
        "Спросить про апартаменты...": #corruption
            img 16940
            shawarma "О, Мадаме!"
            shawarma "Вы пришли за самый вкусный кебаб в округе?"
            m "Нет. Мне не нужен твой кебаб!"
            m "..."
            $ monicaShawarmaApartment1 = True # Моника спросила у продавца шавермы про квартиру
            pass
        "Уйти отсюда.":
            img 16940
            shawarma "О, Мадаме!"
            shawarma "Вы пришли за самый вкусный кебаб в округе?"
            img 16941
            mt "Нет, я пока не готова тратить деньги на апартаменты."
            mt "Мне это сейчас не по карману."
            img 16942
            m "Сам ешь свой отвратительный кебаб!"
            # если называла его животным
            #
            $ notif(_("Моника называла продавца шавермы животным"))
            #
            img 16943
            mt "Животное!"
            #
            m "!!!"
            return False
    # ехидно смотрит на него
    img 16942
    m "Я хотела кое-что у тебя спросить..."
    img 16944
    shawarma "Все, что Мадаме захотеть, Джек все сделать!"
    shawarma "Для прекрасной Мадаме Джеку ничего не жалко!"
    img 16945
    m "Мне..."
    m "..."
    m "Одной моей знакомой нужны апартаменты."
    img 16946
    m "Она хочет их арендовать..."
    m "За небольшую плату."
    m "Ты знаешь, где можно найти что-то подходящее?"
    img 16947
    shawarma "О, Мадаме!"
    shawarma "Вы правильно сделали, что пришли ко мне!"
    shawarma "Джек все здесь знать!"
    shawarma "Для восхитительной Мадаме у Джека есть апрартаменты!"
    img 16948
    m "Это... Это не для меня квартира..."
    shawarma "Мадаме может не волноваться."
    shawarma "Джек никому не рассказывать!" # подмигивает ей
    img 16949
    m "!!!"
    m "Так у тебя есть апартаменты под аренду?" # воодушевленно
    img 16944
    shawarma "Конечно, Мадаме!!!"
    shawarma "И как раз сейчас они свободны!"
    shawarma "Это шикарный апрартамент! Мадаме будет очень доволен!"
    shawarma "И всего за 50 долларов за один неделя!"
    shawarma "Прекрасный Мадаме не найдет ничего дешевле!"
    img 16950
    mt "Всего 50 долларов в неделю?!"
    mt "Боже! Я не верю в эту удачу!"
    mt "Наконец-то!"
    img 16951
    mt "..."
    mt "Хотя... Это не такие уж маленькие деньги для меня сейчас..."
    mt "!!!"
    mt "Интересно, что это за апартаменты?"
    img 16945
    m "А где эти апартаменты находятся?"
    shawarma "Недалеко отсюда, Мадаме!"

# если отказалась идти смотреть квартиру, диалог начнется с этого момента
    img 16940
    shawarma "Мадаме хочет посмотреть свой будущий шикарный апрартамент?"
    m "..."
    menu:
        "Согласиться.": #corruption
            $ monicaShawarmaApartment2 = True # Моника сразу согласилась посмотреть квартиру продавца шавермы
            pass
        "Нет. $ 50 в неделю - это слишком дорого.":
            img 16941
            mt "Я пока не готова тратить деньги на жилье."
            mt "Мне это сейчас не по карману."
            img 16942
            m "Нет."
            m "Мне нужно еще подумать."
            img 16944
            shawarma "Если Мадаме надумает, может приходить к Джеку!"
            shawarma "Джек будет рад помочь прекрасной Мадаме!"
            return False
    # подозрительно
    img 16945
    m "А там никто больше не будет жить, кроме меня?"
    img 16947
    shawarma "Конечно, нет!"
    shawarma "Мадаме будет хозяйкой в этот шикарный апрартамент!"
    img 16946
    m "Отлично!"
    m "Я хочу их посмотреть!"
    # Некоторое время спустя Моника и животное оказываются в новой локации перед страшным домом в трущобах
    return

# Моника возле дома, где будет снимать квартиру (глазик)
label ep211_dialogues6_slum_apartment_4:
    # не рендерить!
    mt "Этот дом просто кошмарный!!!"
    return

# Моника с животным возле дома, где будет снимать квартиру
label ep211_dialogues6_slum_apartment_5:
    # стоит возле дома, Джек стоит рядом
    mt "Жуть!!!"
    mt "Он что-то говорил про шикарные апартаменты?"
    mt "Шикарные апартаменты в ТАКОМ доме?!"
    mt "???"
    m "Ты уверен, что апартаменты хорошие?"
    shawarma "Конечно, Мадаме!"
    shawarma "Там есть очень большой комнат!"
    shawarma "Отдельный кухня!"
    shawarma "И даже отдельный душ!"
    shawarma "Мадаме идти за мной и сам все посмотреть!"
    m "..."
    return

# квартира Моники
label ep211_dialogues6_slum_apartment_6:
    # Моника стоит посередине квартиры
    img 16968
    w
    img 16953
    w
    img 16954
    m "Куда ты меня привел?!"
    m "Это что?! Квартира?!"
    m "?!?!?!"
    img 16955
    shawarma "Да, Мадаме!"
    shawarma "Теперь это Ваш шикарный апрартамент!"
    img 16956
    m "Шикарный?!"
    m "Да ты охренел?!"
    img 16957
    shawarma "В этот прекрасный апрартамент раньше жить рабочие."
    m "Рабочие?!"
    img 16958
    shawarma "Да! Они делать ремонт в очень богатых местах!"
    shawarma "Может быть, Мадаме слышать про отель Ле Фгранд или офис Модный Журнал?"
    img 16959
    m "!!!"
    img 16960
    shawarma "Рабочий, который делать такую хорошую работу, всегда любить комфорт и чистота."
    shawarma "Они бы не жить здесь, если бы это место не быть таким хорошим!"
    img 16961
    m "..."
    m "А что это за убогие обои?! Это тоже от рабочих?"
    img 16962
    shawarma "Нет, Мадаме."
    shawarma "Еще раньше здесь жить прекрасный женщин, чистый ангел!"
    shawarma "Он оказывать здесь небольшие услуги уважаемым жителям нашей улица!"
    img 16963
    mt "Боже! Какой кошмар!"
    img 16964
    shawarma "Ну что? Мадаме будет жить в этот шикарный квартир?"
    m "..."
    menu:
        "Согласиться.":
            $ monicaShawarmaApartment3 = True # Моника посмотрела квартиру и согласилась ее арендовать (50 баксов)
            pass
        "Уйти отсюда!":
           img 16965
            m "Я не буду жить в этой!"
            m "В этой!"
            m "В этом пристанище для бомжей!!!"
            m "!!!"
            img 16966
            shawarma "Если Мадаме надумает, может приходить к Джеку!"
            shawarma "Джек будет рад помочь прекрасной Мадаме!"
            # если называла его животным
            #
            $ notif(_("Моника называла продавца шавермы животным"))
            #
            img 16967
            mt "Животное!"
            #
            m "!!!"
            # Моника уходит
            return False
    img 16967
    mt "Может быть, стоит арендовать эту грязную дыру?"
    mt "Всего 50 долларов в неделю..."
    mt "..."
    img 16969
    mt "Это ведь на какое-то время."
    mt "Потом я подберу себе жилье получше."
    img 16970
    m "Я... Я согласна арендовать эти ужасные апра... апартаменты ненадолго."
    shawarma "Отлично! Мадаме сделать правильный решение!"
    shawarma "Джек очень счастлив, что такой восхитительный женщин будет жить в его апрартамент!"
    img 16971
    m "Когда требуется оплата, прямо сейчас? Я сразу смогу здесь жить?"
    img 16972
    shawarma "Конечно, Мадаме сразу может тут остаться и жить!"
    shawarma "Только Джеку сначала нужен документ Мадаме..."
    img 16973
    mt "Документы?!"
    mt "Дъявол!!!"
    mt "!!!"
    mt "Что же делать?!"
    img 16974
    m "Я... Я не хотела бы показывать свои документы..."
    m "Тем более, у меня их нет с собой..."
    img 16975
    m "Я их забыла дома..."
    m "..."
    m "Без документов никак нельзя?"
    img 16976
    shawarma "Если Мадаме хочет снять этот квартир без документ..."
    shawarma "То Джек легко помочь Мадаме с этим!"
    shawarma "Этот прекрасный апартамент не входит в жилой фонд..."
    img 16966
    shawarma "Поэтому здесь нет злой проверяющий миграционных бумаг!"
    shawarma "И такой прекрасный леди мочь жить здесь без документ!"
    img 16977
    m "В таком случае, мы договорились."
    m "Я арендую эту ужасную квартиру!"
    img 16962
    shawarma "Прекрасно! Джек счастлив помочь такой восхитительный женщин!"
    shawarma "Этот шикарный квартир будет стоить всего 300 долларов в неделю для Мадаме!"
    img 16956
    m "!!!"
    m "ЧТО?!"
    m "Ты же говорил, что она стоит $ 50 в неделю!"
    m "Почему сейчас стало $ 300?!"
    m "?!?!?!"
    img 16957
    shawarma "Специально для Мадаме!"
    shawarma "Документ есть - апартамент стоит $ 50 в неделю!"
    shawarma "Документ нет - апартамент стоит $ 300 в неделю!"
    img 16964
    shawarma "Джек все для Вас готов сделать, Мадаме!"
    shawarma "Мадаме никакой квартир больше не найдет, если у нее нет документ!"
    shawarma "Да еще и по специальный цена!"
    img 16978
    m "Апартаменты в трущобах за 300 долларов в неделю?!"
    m "?!?!?!"
    img 16959
    mt "Вот сволочь!"
    mt "!!!"
    mt "300 долларов в неделю..."
    mt "..."
    menu:
        "Согласиться.":
            $ monicaShawarmaApartment4 = True # Моника согласилась арендовать квартиру за 300 баксов
            pass
        "Уйти отсюда!":
            img 16965
            m "Я не буду жить в этом!"
            m "В этом пристанище для бомжей!!!"
            m "Да еще и за такие деньги!"
            m "!!!"
            img 16966
            shawarma "Если Мадаме надумает, может приходить к Джеку!"
            shawarma "Джек будет рад помочь прекрасной Мадаме!"
            # если называла его животным
            #
            $ notif(_("Моника называла продавца шавермы животным"))
            #
            img 16967
            mt "Животное!"
            #
            m "!!!"
            # Моника уходит
            return False
    img 16979
    mt "Вот дъявол!"
    mt "Мне не удастся снять жилье без документов..."
    mt "Получается, что это единственный вариант, который я могу найти..."
    mt "..."
    img 16980
    shawarma "Мадаме жить один и Джек ее не беспокоить совсем."
    shawarma "Только один раз в неделю Джек приходить за деньгами."
    img 16981
    mt "И что мне делать?"
    mt "???"
    mt "С другой стороны... Это будет МОЕ жилье... МОЕ!!!"
    img 16982
    mt "О том, где я живу, никто не будет знать..."
    mt "Я буду сама себе хозяйка..."
    mt "И больше никакие никчемные деревенщины мною не будут командовать!"
    # поворачивается к Джеку
    img 16955
    shawarma "Мадаме согласен?"
    m "Деньги платить сейчас?"
    shawarma "Да. Сейчас."
    shawarma "И Мадаме может сразу оставаться жить здесь."
    img 16970
    m "Следующая оплата ровно через неделю?"
    shawarma "Джек будет приходить {c}каждая суббота вечер{/c} за деньгами."
    shawarma "Мадаме платить и оставаться здесь жить!"
    m "..."
    menu:
        "Заплатить $ 300 за апартаменты.":
            $ monicaShawarmaApartment5 = True # Моника внесла первую оплату Джеку за квартиру
            pass
    # у Моники списываются с баланса деньги
    img 16983
    shawarma "Джек счастлив помочь прекрасной Мадаме!"
    shawarma "Джек придти за деньгами в следующий суббота."
    img 16985
    shawarma "Вот ключи от Ваш шикарный апартамент!"
    # ключи кладет куда-нибудь на стол и уходит
    img 16984
    shawarma "До суббота, прекрасный леди!"
    img 16986
    m "..." # смотрит на него недовольно
    # Джек уходит
    $ log1 = _("Заработать $ 300 за аренду апартаментов до субботы.")
    $ log1 = _("У меня теперь есть место, где я могу жить. Апартаменты в трущобах...
    Но это лучше, чем подвал в доме, где живет семейка идиотов.") # квест-лог
    return

# квартира Моники, сразу после ухода Джека
label ep211_dialogues6_slum_apartment_7:
    # Моника стоит посередине квартиры оглядывается
    # не рендерить!
    mt "Это самое жуткое место, которое я видела в своей жизни!"
    mt "Ни в коем случае нельзя, чтобы кто-нибудь узнал, что Моника Бакфетт живет здесь!"
    mt "!!!"
    mt "С другой стороны..."
    mt "Теперь у меня есть МОЕ жилье!"
    mt "Я могу послать к черту сопляка Барди и эту дуру Бетти!"
    mt "Хотя... Наверное пока не стоит этого делать..."
    mt "Вдруг у меня не окажется денег на продление аренды..."
    mt "Но, все равно, Я теперь независима от них!"
    mt "Это маленький шаг навстречу к моей цели."
    mt "Тот день, когда Моника Бакфетт вернет себе все, что у нее отняли, становится все ближе!"
    return


# квартира Моники, мысли Моники, когда осматривает квартиру
# лейблы с 8а по 8к не рендерить!
# комната
label ep211_dialogues6_slum_apartment_8a:
    # комната (стены, пол, окна)
    mt "Какое же кошмарное это место!"
    mt "Может, стоит сделать тут небольшой ремонт?"
    return
label ep211_dialogues6_slum_apartment_8b:
    # мусор на полу, бочки и т.п.
    mt "Фи! Какая грязь!"
    mt "Кто сюда притащил весь этот хлам?"
    return
label ep211_dialogues6_slum_apartment_8c:
    # раскладушка
    mt "Это, конечно, не сравнится с моей шикарной кроватью..."
    mt "На которой спит теперь эта сучка Бетти."
    mt "Но все же, на этом можно спать..."
    return
label ep211_dialogues6_slum_apartment_8d:
    # деревянные стулья, столик, деревянная рыбка, тумбочка
    mt "Что за кошмарная мебель здесь?!"
    mt "Я не хочу даже прикасаться к ней!"
    return
label ep211_dialogues6_slum_apartment_8e:
    # шкаф
    mt "Нужно будет принести сюда свои наряды..."
    return
# кухня
label ep211_dialogues6_slum_apartment_8f:
    # кухня (стены, пол)
    mt "Ужасная кухня!"
    mt "Надеюсь, здесь нет тараканов?"
    mt "Все равно я не смогу готовить здесь еду!"
    return
label ep211_dialogues6_slum_apartment_8g:
    # кухонная утварь, посуда
    mt "Эта посуда осталась от прежних жильцов?"
    mt "Фи! Я не буду ее трогать!"
    return
# ванная комната
label ep211_dialogues6_slum_apartment_8h:
    # комната (стены, пол)
    mt "Эта ванная комната отвратительна!"
    mt "Я не хочу сюда даже заходить!"
    return
label ep211_dialogues6_slum_apartment_8i:
    # унитаз
    mt "Фууу!"
    mt "Как мне на этом писать?!"
    return
label ep211_dialogues6_slum_apartment_8j:
    # раковина
    mt "Это что за непонятная куча старого хлама?"
    mt "В этом можно как-то умываться и мыть руки?"
    return
label ep211_dialogues6_slum_apartment_8k:
    # душ
    mt "Мне придется мыть свое великолепное тело водой из куска ржавой трубы..."
    mt "..."
    return
#label ep211_dialogues6_slum_apartment_8l:
    # стиральная машинка
#    mt "Душ сделан из куска ржавой трубы, зато есть стиральная машинка..."
#    mt "Это уже неплохо."
#    mt "Мои прекрасные руки не предназначены для таких вещей, как стирка одежды."
#    return

# квартира Моники
# если Моника подходит к шкафу, то открыв его находит там домашнюю одежду
label ep211_dialogues6_slum_apartment_9:
    
    mt "А это еще что?"
    mt "Хммм..."
    mt "Это подделка на мою любимую модель этого бренда..."
    mt "..."
    mt "Почему бы мне не носить это дома?"
    mt "Нужно померить этот наряд."
    # переодевается и смотрит на себя в зеркало. если нет зеркала, то просто смотрит на себя
    mt "..."
    mt "Я, конечно, догадываюсь, кто носил это раньше..."
    mt "Но это неважно... Это теперь МОЕ!!!"
    return

# Моника в квартире в домашней одежде (глазик)
label ep211_dialogues6_slum_apartment_9a:
    # не рендерить!
    mt "Хорошо, что никто не увидит меня в подделке этого бренда..."
    mt "О том, что их до меня носил кто-то я предпочитаю не думать."
    mt "Джек говорил, что раньше здесь жила какая-то проститутка..."
    mt "..."
    mt "Мне не важно! Эта одежда теперь моя!"
    return

# квартира Моники, вечером в субботу приходит Джек за деньгами
label ep211_dialogues6_slum_apartment_10:
    # стук в дверь, затемнение экрана - шаги, звук открывающейся двери
    shawarma "Прекрасный Мадаме!"
    shawarma "Джек пришел взять с нее деньги за шикарный апартамент!"
    mt "За эту квартиру и $ 50 жалко платить..."
    m "..."
    shawarma "Мадаме стал еще прекрасней в этот домашней костюм!"
    shawarma "Джек не может отвести глаз от прелестной Мадаме!"
    shawarma "Вы такой яркий сияющий женщин!"
    shawarma "Я подходить к дом и видеть, как он светится, благодаря Ваша красота!"
    mt "Когда он уже заткнется и уйдет отсюда!"
    m "..."
    shawarma "Я подумал, что Мадаме слишком прекрасен, чтобы давать Джеку целых $ 300!"
    shawarma "Джек сделать благородный поступок и предложить скидку для Мадаме!"
    m "Скидку?"
    shawarma "Да!"
    shawarma "Джек сделать скидка в 10 процент, если..."
    shawarma "Мадаме позволит прикоснуться ему к ее красота и целовать Джека!"
    mt "!!!"
    shawarma "Но это еще не все!"
    shawarma "Джек сделать очень-очень щедрый скидка для Мадаме. 20 процент!"
    shawarma "Если нефритовый стержень Джека проникать внутрь прекрасный Мадаме!!!"
    m "Что ты несешь?!"
    m "Что это все значит?!"
    shawarma "Это значит, Джек предлагать Вам выгодный сделка."
    shawarma "Скидка в 10 или 20 процент."
    m "..."
    menu:
        "Заплатить со скидкой.": #corruption
            menu:
                "Скидка 10 процентов.":
                    # Моника с подозрением
                    mt "Почему бы мне не воспользоваться его предложением?"
                    mt "Скидка мне не помешает."
                    m "И что мне сделать, чтобы получить эту скидку?"
                    shawarma "У прекрасной Мадаме рот как лепесток роз!"
                    shawarma "Такой же восхитительный и нежный!"
                    shawarma "Джек будет счастлив дать в этот рот свой нефритовый стержень!"
                    m "ЧТО?!"
                    m "Да как ты смеешь мне подобное предлагать?!"
                    m "!!!"
                    shawarma "Джек делать очень щедрый и благородный предложение Мадаме..."
                    shawarma "Но если Мадаме откажется, Джек на нее не обижаться."
                    shawarma "Тогда она может просто заплатить Джеку $ 300 за шикарный квартир."
                    mt "Черт!"
                    mt "И что же мне делать?"
                    mt "10 процентов от $ 300 - это немало."
                    mt "А у меня сейчас каждый цент на счету."
                    m "..."
                    menu:
                        "Согласиться.": #corruption
                            $ monicaShawarmaApartment6 = True # Моника согласилась сделать минет за скидку в 10 процентов
                            # переход к лейблу ep211_dialogues6_slum_apartment_11
                            return
                        "Ни за что!!!":
                            m "Ты что, ненормальный?!"
                            m "Конечно, я не буду этого делать!"
                            m "Как ты мог вообще до такого додуматься!!!"
                            # если называла его животным
                            #
                            $ notif(_("Моника называла продавца шавермы животным"))
                            #
                            mt "Животное!"
                            #
                            m "!!!"
                            shawarma "Тогда Мадаме платить Джеку $ 300."
                            # jump на первоначальное меню
                            return
                    return
                "Скидка 20 процентов.": #corruption
                    # Моника с подозрением
                    mt "Почему бы мне не воспользоваться его предложением?"
                    mt "Скидка мне не помешает."
                    m "И что мне сделать, чтобы получить эту скидку?"
                    shawarma "Красота Мадаме ослеплять Джека!"
                    shawarma "Мадаме прекрасна как древнегреческий богинь!"
                    shawarma "Джек будет счастлив, если она позволит..."
                    shawarma "Проникнуть нефритовый стержень Джека в ее сладкий дырочка!"
                    m "ЧТО-О-О-О?!"
                    m "?!?!?!"
                    m "Да как ты смеешь мне подобное предлагать?!"
                    m "!!!"
                    shawarma "Джек делать очень щедрый и благородный предложение Мадаме..."
                    shawarma "Но если Мадаме откажется, Джек на нее не обижаться."
                    shawarma "Тогда она может просто заплатить Джеку $ 300 за шикарный квартир."
                    mt "Черт!"
                    mt "И что же мне делать?"
                    mt "20 процентов от $ 300 - это немало."
                    mt "А у меня сейчас каждый цент на счету."
                    m "..."
                    menu:
                        "Согласиться.": #corruption
                            $ monicaShawarmaApartment7 = True # Моника согласилась заняться сексом за скидку в 20 процентов
                            # переход к лейблу ep211_dialogues6_slum_apartment_12
                            return
                        "Ни за что!!!":
                            m "Ты что, ненормальный?!"
                            m "Конечно, я не буду этого делать!"
                            m "Как ты мог вообще до такого додуматься!!!"
                            # если называла его животным
                            #
                            $ notif(_("Моника называла продавца шавермы животным"))
                            #
                            mt "Животное!"
                            #
                            m "!!!"
                            shawarma "Тогда Мадаме платить Джеку $ 300."
                            # jump на первоначальное меню
                            return
                    return
            return
        "Заплатить $ 300":
            # Моника с деловым видом
            m "Мне не нужны никакие скидки!"
            m "Я готова заплатить сумму полностью."
            m "Забирай деньги и иди!"
            shawarma "Отлично, Мадаме! Джек очень рад!"
            shawarma "Джек придет в {c}следующий суббота вечер{/c}!"
            shawarma "И Мадаме может не сомневаться!"
            shawarma "Джек очень благородный и щедрый!"
            shawarma "Он снова предлагать Мадаме скидку в следующий суббота!"
            m "Все! Иди! Мне некогда!"
            # $ 300 списываются с баланса Моники, Джек уходит
            mt "Животное!"
            mt "Как хорошо, что я его целую неделю теперь не увижу!"
            $ monicaShawarmaApartment8 = True # Моника заплатила $ 300 за квартиру (без скидки)
            return
        "У меня нет денег.":
            # Моника нерешительно
            mt "Что же мне делать?"
            mt "У меня не хватает денег на оплату..."
            mt "Может, он согласится подождать несколько дней?"
            m "..."
            m "Я тебе смогу заплатить за апартаменты через несколько дней."
            m "Ты же не выселишь такую прекрасную леди, как я, на улицу?"
            m "Всего лишь несколько дней и я все оплачу."
            shawarma "Нет-нет, Мадаме!"
            shawarma "Джек восхищается Вашей красотой."
            shawarma "Но Джек с Мадаме договорился, что деньги будут каждый суббота."
            shawarma "Нет денег в суббота - нет шикарный апрартамент у Мадаме!"
            shawarma "Джеку, конечно, очень жаль..."
            shawarma "Но он вынужден выселять прекрасный леди прямо сейчас!"
            # затемнение экрана. Моника оказывается на улице (переход к лейблу ep211_dialogues6_slum_apartment_13)
            $ monicaShawarmaApartment9 = True # Джек выселил Монику за неуплату
            return
    return

# если выбран пункт меню 'Скидка 10 процентов' и 'Согласиться'
label ep211_dialogues6_slum_apartment_11:
    call check_skip_scene("ep211_dialogues6_slum_apartment_11")
    if _return == True:
        return True


    # Моника смотрит на Джека зло
    m "10 процентов - это сколько?"
    shawarma "Целых $ 30, Мадаме!"
    shawarma "Джек делать очень щедрый предложение для Вас!"
    mt "Черт!"
    mt "Если я соглашусь, я сэкономлю целых $ 30!"
    mt "..."
    m "Если об этом узнает хоть одна живая душа!!!"
    m "!!!"
    shawarma "Что Вы, Мадаме?!"
    shawarma "Джек честный и благородный!"
    shawarma "Джек никому не рассказать о Мадаме!"
    m "Если кто-то узнает, я тебя убью!"
    shawarma "Прекрасный Мадаме может не переживать!"
    shawarma "Джек дает слово мужчины!"
    # Джек расстегивает штаны и достает свой причиндал
    mt "Моника, до чего ты докатилась?"
    mt "Ты собралась делать минет какому-то неудачнику за скидку..."
    mt "..."
    mt "Но об этом ведь никто не узнает..."
    mt "Тем более он даже не догадывается кто я такая..."
    mt "..."
    mt "А я сэкономлю деньги."
    # Моника опускается на колени перед ним
    mt "Фу! Не могу поверить, что я делаю это..."
    mt "И, главное, кому?!"
    mt "Фу!!!"
    mt "!!!"
    # минет
    shawarma "О, прекрасный Мадаме!"
    shawarma "Словно лепестки роз ласкают мой нефритовый стержень!"
    shawarma "Такие нежный и сладкий губы и ротик у Мадаме."
    shawarma "Джек готов наслаждаться этим вечно!"
    shawarma "О, Мадаме! Поласкайте мой стержень своим нежным языком!"
    shawarma "Да, восхитительно!"
    shawarma "Мммммм!!!"
    shawarma "Ещееее!"
    shawarma "ОООООООО!!!" # кончает
    # Моника недовольно вытирает рот
    shawarma "Мадаме, мне никто не доставлял большего наслаждения, чем Вы!!!"
    shawarma "Джек сдержать свое слово и сделать для Мадаме скидку в 10 процент!"
    m "..."
    shawarma "Джек снова предлагать Мадаме скидку в следующий суббота!"
    m "Все! Иди! Мне некогда!"
    # $ 270 списываются с баланса Моники, Джек уходит
    mt "Животное!"
    mt "Как хорошо, что я его целую неделю теперь не увижу!"
    mt "Не могу поверить, что я сделала это!!!"
    mt "Какая мерзость!!!"
    mt "В следующий раз никаких скидок, Моника!"
    mt "Такой леди, как ты, не пристало заниматься подобными непотребствами!"
    mt "!!!"
    return


# если выбран пункт меню 'Скидка 20 процентов' и 'Согласиться'
label ep211_dialogues6_slum_apartment_12:
    call check_skip_scene("ep211_dialogues6_slum_apartment_12")
    if _return == True:
        return True

    # Моника смотрит на Джека зло
    m "20 процентов - это сколько?"
    shawarma "Целых $ 60, Мадаме!"
    shawarma "Джек делать очень щедрый предложение для прекрасный леди!!!"
    mt "Черт!"
    mt "Если я соглашусь, я сэкономлю целых $ 60!"
    mt "..."
    mt "Моника, ты сейчас серьезно?!"
    mt "Как ты можешь даже предполагать подобное?!"
    mt "Ты действительно займешься с этим животным сексом за скидку в $ 60?!"
    mt "?!?!?!"
    mt "..."
    mt "Но об этом ведь никто не узнает..."
    mt "..."
    mt "А я сэкономлю деньги."
    # с угрозой
    m "Я тебя сразу предупрежаю!!!"
    m "Если об этом узнает хоть одна живая душа!!!"
    m "Если ты хотя бы намекнешь кому-то о том, что здесь сейчас будет!!!"
    m "Я тебя убью!!!"
    m "!!!"
    m "Ты меня понял?!"
    shawarma "Что Вы, Мадаме?!"
    shawarma "Джек честный и благородный!"
    shawarma "Джек никому не рассказать о Мадаме!"
    shawarma "Прекрасный Мадаме может не переживать!"
    shawarma "Джек дает слово мужичины!"
    # Джек расстегивает штаны и достает свой причиндал
    shawarma "У Мадаме великолепный попочка!!!"
    shawarma "Сладкий и прекрасный попочка!!!"
    shawarma "Джек очень любить такие!"
    m "Не смей делать какие-нибудь извращенства!"
    shawarma "Нет-нет, что Вы, Мадаме."
    shawarma "Джек просто трогать сладкий попочка."
    shawarma "Ммммм, гладкий и упругий... как персик!"
    mt "Боже... Когда же он заткнется?!"
    # Моника опирается на стол или кушетку, встает задом к Джеку
    mt "Фу! Не могу поверить, что я делаю это..."
    mt "!!!"
    # секс
    shawarma "О, какой сладкий дырочка у Мадаме!!!"
    shawarma "Как тепло и хорошо мой нефритовый стержень!!!"
    shawarma "Ооооо, как сладко!!!"
    shawarma "Джек готов наслаждаться этим вечно!"
    shawarma "Мммммм!!!"
    shawarma "Джек делать прекрасный Мадаме скидка каждый суббот!!!"
    shawarma "Оооо, Джек просто на седьмом небе!!!"
    shawarma "Ааааа!!!"
    shawarma "Мммммм!!!"
    shawarma "ОООООООО!!!" # кончает
    # Моника недовольно вытирает рот
    shawarma "Мадаме, мне никто не доставлял больший наслаждений, чем Вы!!!"
    shawarma "Джек сдержать свое слово и сделать для Мадаме скидку в 20 процент!"
    m "..."
    shawarma "Джек снова предлагать Мадаме скидку в следующий суббота!"
    m "Все! Иди! Мне некогда!"
    # $ 240 списываются с баланса Моники, Джек уходит
    mt "Животное!"
    mt "Как хорошо, что я его целую неделю теперь не увижу!"
    mt "Не могу поверить, что я сделала это!!!"
    mt "Какая мерзость!!!"
    mt "В следующий раз никаких скидок, Моника!"
    mt "Такой леди, как ты, не пристало заниматься подобными непотребствами!"
    mt "!!!"
    return True

# если выбран пункт меню 'У меня нет денег' и Джек выселил Монику
label ep211_dialogues6_slum_apartment_13:
    # Моника стоит на улице перед домом
    # не рендерить!
    mt "Вот скотина!"
    mt "Грязное инстинктивное животное!!!"
    mt "Как он посмел меня выставить на улицу?!"
    mt "?!?!?!"
    mt "Я все равно зайду обратно в квартиру!"
    mt "Ключи же остались у меня!"
    mt "!!!"
    mt "Только нужно дождаться, когда он уйдет из квартиры."
    $ log1 = _("Вернуться в квартиру позже.")
    return

# если Моника пытается зайти в квартиру сразу же после того, как Джек ее выставил
label ep211_dialogues6_slum_apartment_14:
    # не рендерить!
    mt "Мне нужно немного позже прийти сюда."
    mt "Это животное еще в квартире..."
    return

# Моника приходит в квартиру спустя какое-то время
label ep211_dialogues6_slum_apartment_15:
    # Моника стоит на улице перед домом
    # не рендерить!
    mt "Вот скотина!!!"
    mt "Он поменял замки в моей квартире!!!"
    mt "Сволочь!!!"
    mt "!!!"
    mt "И что мне теперь делать?!"
    mt "Неужели мне придется идти к нему и уговаривать впустить меня обратно?!"
    mt "?!?!?!"
    if money < 300:
        mt "Он все равно меня не впустит. У меня нет денег заплатить за неделю..."
        mt "Мне нужно заработать $ 300."
        mt "Потом я пойду и поговорю с ним."
        mt "Он не сможет отказать мне."
#        $ log1 = _("Заработать $ 300.")
    return

# у Моники на балансе достаточно денег, чтобы заселиться в квартиру снова
# если Моника пришла к дому, где квартира
label ep211_dialogues6_slum_apartment_16:
    # не рендерить!
    mt "Я не могу зайти в свою квартиру..."
    mt "Эта сволочь поменяла замки!"
    mt "Мне нужно пойти к нему."
    $ log1 = _("Поговорить с Джеком и снова заселиться в квартиру.")
    return

# у Моники на балансе достаточно денег, чтобы заселиться в квартиру снова
# если Моника пришла к шаверме
label ep211_dialogues6_slum_apartment_17:
    menu:
        "Спросить про квартиру...":
            shawarma "О, Мадаме!"
            shawarma "Вы пришли за самый вкусный кебаб в округе?"
            shawarma "Или Мадаме хочет снова жить в шикарный апрартамент?"
            m "Я хочу вернуться в свою квартиру!"
            shawarma "Джек не может отказать такой прекрасный леди!"
            shawarma "А у Мадаме есть деньги?"
            m "Да!"
            shawarma "Мадаме может заплатить деньги Джеку прямо сейчас."
            shawarma "Джек даст Мадаме новый ключ."
            shawarma "И она может снова жить в шикарный апрартамент Джека!"
            menu:
                "Заплатить $ 300.":
                    shawarma "Отлично, Мадаме!"
                    shawarma "Джек счастлив, что прекрасный Мадаме снова будет жить в его апрартамент!"
                    shawarma "Вот Ваш ключ. С возвращенем, прекрасный леди!"
                    mt "Наконец-то я могу вернуться в свою квартиру!"
                    mt "!!!"
                    $ monicaShawarmaApartment10 = True # Моника заплатила денег после ее выселения и снова может жить в квартире
                    return
                "Нет! Я не готова платить такую сумму!":
                    mt "Нет, я пока не готова тратить деньги на жилье."
                    mt "Мне это сейчас не по карману."
                    m "Я пока не готова заплатить деньги..."
                    shawarma "Если Мадаме передумает, она знать, где найти Джека!"
                    m "..."
                    return False
            return
        "Уйти отсюда.":
            shawarma "О, Мадаме!"
            shawarma "Вы пришли за самый вкусный кебаб в округе?"
            shawarma "Или Мадаме хочет снова жить в шикарный апрартамент?"
            mt "Нет, я пока не готова тратить деньги на жилье."
            mt "Мне это сейчас не по карману."
            m "Я пока не готова заплатить деньги..."
            shawarma "Если Мадаме передумает, она знать, где найти Джека!"
            m "..."
            return False
    return

# Моника вернулась в квартиру после ее выселения
label ep211_dialogues6_slum_apartment_18:
    # не рендерить!
    mt "Наконец-то я дома!"
    mt "Никогда бы не подумала, что буду рада вернуться сюда!"
    mt "!!!"

    # Если суббота, но Моника ночевала не дома
    $ log1 = _("Оплата за апартаменты в трущобах.")
    return
