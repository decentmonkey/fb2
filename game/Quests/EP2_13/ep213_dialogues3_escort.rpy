

default monicaEscortLindaTable1 = False  # Моника согласилась работать реквизитом Линды
default monicaEscortLindaTable2 = False  # Моника осталась с инвестором вдвоем в отеле
default monicaEscortLindaTable3 = False  # Моника врезала инвестору по яйцам
default monicaEscortLindaTable4 = False  # Моника промолчала, когда инвестор стал называть ее грязной шлюшкой
default monicaEscortLindaTable5 = False  # Моника врезала инвестору по яйцам после минета
default monicaEscortLindaTable6 = False  # Моника промолчала, когда инвестор сказал, что оттрахает ее
default monicaEscortLindaTable7 = False  # Моника снова нахамила Линде (после сцены с инвестором)


# после сцены в эскорте с семейной парой, через неделю доступна след. сцена
# при выборе пункта меню "Встреча с клиентом (сцена)" (лейбл ep211_escort_scene1_1a), подпункт "Работать реквизитом в номере"

# Моника сидит за столиком в ожидании клиента
label ep213_dialogues2_escort_1:
    # Моника думает
    img 30076
    mt "Дьявол!"
    mt "Сколько уже можно сидеть тут и ждать очередного извращенца?!"
    mt "?!"
    # поменять предлог. сделать пару мысле в женском туалете
    img 30085
    mt "..."
    mt "Думаю, если я отлучусь ненадолго, никто не заметит."
    # встает со стула и идет к выходу

    # смена кадра, туалет ресторана
    # Моника стоит возле раковины (моет руки или смотрится в зеркало)
    #
    $ notif(_("Моника удовлетворяла Филиппа в туалете отеля Ле Гранд."))
    img 17969
    mt "Ужасное место!"
    img 17970
    mt "Каждый раз захожу сюда и вспоминаю этого мерзавца Филиппа!"
    mt "Фу! Какой же он отвратительный тип!"
    img 17971
    mt "!!!"
    #

    # затемнение, текст "Несколько минут спустя", и звук каблуков
    # Моника возвращается к своему столику
    # ее столик занят, за ним сидит девочка из эскорта (брюнетка с длинными волосами - Линда)
    img 17972
    w
    img 17973
    w
    img 17974
    mt "!!!"
    mt "Это еще что такое?!"
    # Моника возмущенно
    img 17975
    m "Та заняла МОЕ место!"
    m "!!!"
    # брюнетка ей высокомерно отвечает
    img 17976
    girl_4 "???"
    girl_4 "С чего ты взяла, что это ТВОЕ место?!"
    girl_4 "Где хочу, там и сижу."
    # Линда отворачивается от Моники, якобы теряя к ней интерес
    img 17977
    girl_4 "Иди за другой столик..."
    # Моника недовольно оглядывается на другие столики
    # видит, что другие девочки на них заинтересованно смотрят и ехидно улыбаются
    img 17978
    w
    img 17979
    mt "!!!"
    mt "Какого черта эта сучка сюда пришла?!"
    mt "Почему это Я должна уходить отсюда?!"
    # Моника встает руки в боки и начинает качать права
    img 17980
    m "Так! Если ты сейчас же не уберешь свою задницу отюда!"
    m "Я пожалуюсь администратору, что ты мешаешь мне работать!"
    m "Быстро ушла за свой столик!"
    m "Какая-то эскортница-проститутка еще будет указывать МНЕ, куда идти и что делать!"
    # брюнетка высокомерно смотрит на нее
    img 17981
    girl_4 "Вот как?!"
    girl_4 "Я, по-твоему, 'какая-то эскортница-проститутка'?!"
    img 17982
    m "ДА!"
    m "!!!"
    # подходит брюнетка с каре и обращается к Линде
    img 17983
    girl_1 "Привет, Линда!"
    girl_1 "Что тут у вас происходит?"
    # Линда недовольно, указывая на Монику
    img 17984
    linda "Я села за свой столик, а эта грубиянка пытается меня отсюда выгнать..."
    linda "Говорит, что я заняла ее место."
    img 17985
    girl_1 "С чего она взяла, что это ее столик?"
    linda "Я тоже этого не могу понять... Здесь где-то написано, что это ее место?"
    # брюнетка с каре поворачивается к Монике
    img 17986
    girl_1 "Ты кто такая, чтобы указывать ей?!"
    linda "И хамить..."
    # Моника злится
    img 17987
    mt "Ненавижу эту стерву!"
    mt "Ненавижу их всех!!!"
    img 17988
    m "Я никому не хамила!"
    m "Я просто называю вещи своими именами!"
    m "!!!"
    # брюнетка с каре злобно смотрит на нее, потом смотрит на Линду
    img 17989
    w
    img 17990
    girl_1 "Хм, слушай... Я уже давно думаю, как бы нам наказать ее..."
    girl_1 "Я хотела сделать кое-что, но для этого мне нужно дождаться моего клиента."
    img 17991
    m "Наказать МЕНЯ?!"
    m "?!?!?! "
    m "Еще чего!"
    # брюнетка игнорирует и продолжает разговаривать с Линдой
    img 17992
    girl_1 "Но мы можем кое-что сделать уже сейчас."
    girl_1 "Там как раз пришел твой постоянный клиент..."
    # указывает пальцем на Монику
    img 17993
    girl_1 "Думаю, нужно эту грубиянку взять на твою встречу с ним."
    # Линда осматривает Монику высокомерно с ног до головы
    img 17994
    linda "Ее?!"
    # потом поворачивается к брюнетке
    linda "Да нууу! Зачем?"
    # брюнетка с каре наклоняется к ней и что-то шепчет на ухо, потом они обе хихикают и смотрят на Монику
    img 17995
    w
    img 17996
    w
    img 17997
    girl_1 "Аха-ха!"
    linda "Хи-хи-хи..."
    # брюнетка говорит заговорщицки Линде
    img 17998
    girl_1 "Я сейчас все устрою."
    # смотрит ехидно на Монику и уходит
    # Моника говорит брюнетке зло
    img 17989
    w
    img 17999
    m "Мне все равно, что вы там задумали!"
    m "Я не собираюсь принимать участие в ваших глупостях!"
    m "Иди работай, никчемная эскортница!"
    m "И не мешай мне!"
    img 18000
    # Линда на нее смотрит и улыбается ехидно, потом встает и уходит
    img 18001
    return

# Моника садится за свой столик
label ep213_dialogues2_escort_2:
    # сидит, довольная
    img 30085
    mt "Какие-то никчемные эскортницы-проститутки!"
    mt "Кто они такие, что бы себя вести подобным образом со МНОЙ?!"
    mt "Знали бы они, что разговаривают с самой Моникой Бакфетт!"
    mt "Я тогда посмотрела бы на них!"
    img 30061
    mt "!!!"
    mt "Сотни и даже тысячи подобных им выстраиваются в бесконечные очереди..."
    mt "Чтобы просто попасть ко мне на кастинг!"
    mt "!!!"
    if monicaBitch == True:
        $ notif_monica()
        mt "Строят из себя не понятно кого, а на деле обычные серые мыши!!"
    # подходит официантка (использовать имеющиеся арты)
    img 30062
    waitress "Здравствуйте, Мэм! Администратор Вас ждет на ресепшене."

    #
    $ notif(_("У Моники хорошие отношения с официанткой."))
    #
    img 30064
    mt "Черт!"

    # если была сцена с выездом к клиенту Нэду
    img 30064
    mt "Надеюсь, это не выезд к клиенту в какой-нибудь гостевой дом..."
    mt "Где его друзья с женами..."

    # если была сцена с семейной парой
    img 30064
    mt "И не сумасшедшая семейка, где муж неудачник, а жена тупая провинциальная дура!"
    img 30067
    m "Я сейчас подойду к ней."

    # официантка уходит

    #
    $ notif(_("У Моники плохие отношения с официанткой."))
    #
    img 30067
    mt "Снова она!"
    m "Что?"
    img 30069
    waitress "Мэм..."
    waitress "Администратор меня попросила позвать проститу... Кхм..." # ехидно
    waitress "Женщину, которая сидит за этим столиком."
    # Моника перебивает ее
    img 30071
    m "ЧТО?!"
    m "?!?!?!"
    img 30065
    waitress "Я просто передаю слова администратора."
    m "!!!"
    waitress "Она вас ждет на ресепшене вместе с одной из эскортниц..."
    img 30072
    m "Так! Хватит!"
    m "Меня не интересует, кто и кем работает в вашем никчемном ресторане!"
    if monicaBitch == True:
        $ notif_monica()
        img 30073
        m "Я здесь гость! И я не обязана выслушивать всякие глупости от какой-то официантки!"
    # официантка уходит
    $ log1 = _("Пойти на ресепшн к администратору.")
    return

# ресепшн
label ep213_dialogues2_escort_3:
    # Моника приходит на ресепшн, там стоит Линда и администратор
    img 18002
    reception "[monica_hotel_name], есть работа."
    reception "Сегодня ты работаешь в номере вместе с Линдой."
    # администратор указывает на брюнетку, та высокомерно смотрит на Монику
    # Моника возмущенно
    img 18003
    m "?!?!?!"
    m "Почему я работаю вместе с ней?!"
    # администратор недовольно
    img 17525
    reception "Ты задаешь слишком много вопросов, [monica_hotel_name]!"
    reception "Линда тебя ждет, чтобы вместе пойти в номер."
    # Линда равнодушно говорит администратору
    img 18004
    linda "Пусть она наденет маску."
    linda "Не хочу спугнуть клиента ее вечно недовольной физиономией."
    img 18005
    reception "Слышала, [monica_hotel_name]?"
    reception "Маска есть среди вещей девочек. Найдешь в служебном коридоре..."

    # Моника зло смотрит на Линду
    # если была сцена с семейной парой в номере отеля
    img 17543
    mt "Вот черт!"
    mt "А если повторится ситуация, как в прошлый раз с той сучкой из эскорта?!"
    mt "Нет! Я больше не позволю себя унижать!"
    img 18006
    mt "Если эта мерзкая Линда сделает хоть что-то, что не понравится мне..."
    mt "Я оттаскаю эту сучку за волосы!"
    mt "!!!"

    # администратор рявкает на Монику
    img 17509
    reception "Чего ты стоишь?!"
    reception "Клиент вас уже ждет!"
    img 30113
    reception "И еще! [monica_hotel_name], я тебя предупреждаю!"
    reception "Ты будешь делать то, что тебе скажет Линда! И никаких глупостей!!"
    reception "Линда намного опытнее и умнее, чем ты."
    reception "Тебе бы поучиться у нее, как надо работать с клиентами!"
    # Моника насмешливо ухмыляется
    img 18007
    mt "Что?!"
    mt "Эта никчемная эскортница умнее МЕНЯ?!"
    mt "Владелицы многомиллионного бизнеса и самого успешного журнала страны?!"
    mt "!!!"
    img 18008
    reception "Что ты ухмыляешься?"
    reception "Думаешь, что ты самая умная?!"
    m "..."

    #
    $ notif(_("Моника сказала администратору, что она не леди, чтобы устроиться на работу в ВИП-эскорт."))
    img 18009
    reception "Ты обычная лгунья, которая пыталась пройти в ресторан, притворяясь леди."
    reception "А на самом деле мешала девочкам работать, забирая их клиентов!"
    reception "Или ты уже забыла об этом?"
    #
    img 18010
    reception "В общем, если ты не будешь слушаться Линду и сделаешь хотя бы что-то не так..."
    reception "Я даже разбираться не буду кто прав, кто виноват!"
    reception "Сразу же оштрафую тебя! Поняла, [monica_hotel_name]?!"
    # Моника злобно
    img 17520
    m "..."
    m "Да!"
    img 18011
    mt "Сучка!"
    mt "Ненавижу!!!"
    img 18012
    reception "А теперь надевай маску и иди в номер!"
    reception "Быстро!!"
    # затемнение, через несколько минут
    # Моника идет к лифту, на ней маска, которая скрывает ее лицо
    return

# возле лифта
label ep213_dialogues2_escort_4:
    # возле лифта стоит Линда
    img 18013
    mt "Высокомерная сучка!"
    mt "И какого черта я должна работать с ней?!"
    mt "Еще и в этой дурацкой маске?!"
    mt "?!"
    # Линда смотрит на Монику
    img 18014
    linda "От тебя многого не требуется..."
    linda "Будешь просто стоять и молчать."
    img 18015
    m "Просто стоять и молчать?"
    m "???"
    # Линда усмехается
    img 18016
    linda "Да..."
    # осматривает Монику оценивающим взглядом
    linda "Сомневаюсь, что он захочет чего-то большего с тобой..."
    img 18017
    m "!!!"
    img 18018
    linda "В общем, надеюсь, ты справишься с этой несложной задачей..."
    linda "Если сделаешь что-то не так, я нажалуюсь на тебя администратору."
    linda "Думаю, ты понимаешь, что последствия будут не самыми приятными для тебя."
    img 18019
    mt "Ненавижу!!!"
    mt "!!!"
    img 18020
    linda "Как только мы зайдем в номер, я от тебя не должна слышать ни слова."
    linda "Понятно?"
    linda "Встанешь, где я скажу и будешь стоять."
    img 18021
    m "..."
    m "А сколько я за это заработаю?"
    m "И обязательно мне быть в этой маске?!"
    img 18022
    linda "Маску снимать нельзя."
    linda "Девушкой в номере перед клиентом буду только Я."
    linda "Тебе приготовлена другая роль..."
    # Моника упрямо
    img 18023
    m "Какая еще роль?!"
    m "И я сама решу, быть мне в маске или нет!"
    m "С какой стати ты МНЕ будешь указывать?!"
    # Линда равнодушно
    img 18024
    linda "Насчет оплаты... Администратор будет решать, сколько тебе заплатить."
    linda "После того, как выслушает мое мнение о твоей работе..."
    img 18025
    mt "!!!"
    mt "Эта сучка не смеет мной командовать!"
    mt "Я принципиально сниму эту маску прямо перед ее клиентом!"
    img 18026
    mt "Посмотрим, кто клиенту понравится больше, она или Я!"
    mt "И мне плевать, что она скажет администратору после этого!"
    mt "!!!"
    # заходят в лифт
    return

# номер отеля
label ep213_dialogues2_escort_5:
    # Моника с Линдой заходят в номер, клиент (блондин-инвестор) сидит на краешке кровати
    # увидев Линду улыбается и непонимающе и удивленно смотрит на Монику
    img 18036
    w
    img 18043
    w
    img 18037
    investor3 "Линда, дорогая!"
    investor3 "Я так рад тебя видеть!"
    img 18038
    w
    img 18039
    investor3 "Но... Я думал, мы с тобой будем вдвоем..."
    # Линда подходит к инвестору, он приобнимает ее или целует руку
    # Моника в это время стоит в сторонке и внимательно смотрит на них
    img 18040
    mt "Я уже видела где-то этого неудачника..."
    mt "Вот только где?"
    mt "???" # думает, пытается вспомнить
    mt "..."
    mt "!!!" # узнает инвестора, шок
    img 18041
    mt "О Боже! Это же один из инвесторов!!!"
    mt "!!!!!"
    mt "Как же хорошо, что я в маске!"
    mt "Боюсь представить, если бы этот инвестор узнал меня!!"
    mt "Я прямо вижу заголовки журналов..."
    mt "Монику Бакфетт может купить любой желающий!"
    mt "Или 'Моника Бакфетт работает в эскорте!'"
    img 18042
    mt "!!!"
    mt "!!!!!!"
    mt "О, Боже!!! Нельзя допустить того, чтобы он узнал меня!"
    mt "!!!"
    # инвестор, поприветствовав Линду, смотрит в сторону Моники
    img 18044
    investor3 "Дорогая, а кто это?"
    # Линда бросает пренебрежительный в сторону Моники
    img 18045
    linda "Это?"
    linda "Просто небольшой реквизит."
    # поворачивается к инвестору
    img 18046
    linda "Ты же не откажешься немного доплатить за это? Ради моего удовольствия..."
    linda "Мой реквизит совсем недорогой."
    img 18047
    mt "Сучка!"
    mt "!!!"
    # инвестор с обожанием смотрит на Линду
    img 18048
    investor3 "Любимая, ты же знаешь, что я готов все сделать для тебя..."
    investor3 "Особенно, если моя любимая девочка получит от этого удовольствие."
    # Линда ему игриво улыбается
    img 18049
    # потом поворачивается к Монике и показывает рукой на пол возле кровати
    img 18050
    linda "Встань сюда на колени и обопрись ладонями на пол."
    linda "И не двигайся!"
    linda "Ты сегодня работаешь реквизитом. А именно - моим столиком."
    linda "И ни звука, ты помнишь?"
    # Моника в шоке
    img 18051
    mt "Что-о-о?!"
    mt "Я?!"
    mt "Реквизитом?!"
    mt "У какой-то никчемной эскортницы-проститутки?!"
    mt "?!?!?!"
    menu:
        "Пошла она к черту!!! (прерывание квеста и увольнение с эскорта)":
            # Моника возмущенно
            img 18052
            mt "Да она издевается надо мной!"
            mt "!!!"
            # встает руки в боки
            img 18054
            m "Ты что себе позволяешь?!"
            m "Сама вставай и работай реквизитом перед этим мешком с деньгами!"
            m "Еще мне какая-то дешевая проститутка будет указывать, что делать!"
            img 18055
            linda "Что?!"
            linda "Я все расскажу..."
            img 18056
            m "Да пошла ты вместе со своим гребаным администратором!"
            m "Сучка!"
            # Моника уходит
            img 18057
            mt "Ненавижу!"
            mt "!!!"
            return
        "Работать реквизитом Линды.":
            $ monicaEscortLindaTable1 = True # Моника согласилась работать реквизитом Линды
            pass
    # Моника злится, но молчит
    img 18052
    mt "Эта... Эта!"
    mt "Эта мразь хочет унизить меня!"
    mt "Моника Бакфетт, владелица модного журнала, работает столиком!"
    mt "Перед инвестором!!!"
    mt "Перед которым недавно проводила презентацию!!!!!!"
    img 18053
    mt "!!!"
    mt "Но с другой стороны..."
    mt "Он ведь не знает, что это я. На мне маска. И мне не нужно ничего делать."
    mt "Мне..."
    mt "Вернее, [monica_hotel_name] нужно просто молча постоять, пока эта стерва работает."
    mt "Для [monica_hotel_name] это не самый сложный способ заработать деньги..."
    # Моника злобно смотрит на Линду, потом встает на четвереньки возле кровати
    img 18058
    w
    img 18059
    linda "Хорошо. И еще кое-что..."
    # Линда берет со стола поднос, на котором стоит два фужера и бутылка и ставит на спину Монике
    img 18060
    w
    img 18061
    linda "Твоя задача - ничего не уронить с подноса, стоять смирно и не шевелиться."
    linda "И ни звука!"
    # Моника сверлит ее взглядом
    img 18062
    mt "Боже! До чего я докатилась!"
    mt "Из-за каких-то жалких нескольких сотен долларов!"
    mt "Но мне недолго осталось терпеть все эти гадости!"
    img 18063
    mt "Я отомщу им всем!"
    mt "Я их всех уничтожу!"
    mt "И эту сучку тоже!"
    mt "Ненавижу!!!"
    mt "!!!"
    # Линда садится за "столик" на кровать, инвестор тоже садится за "столик" напротив Линды на стул
    img 18064
    w
    img 18065
    investor3 "Любимая, это так необычно..."
    investor3 "Раньше ты приходила на встречу без реквизита."
    # Линда улыбается
    img 18066
    linda "Я решила внести небольшое разнообразие..."
    img 18067
    investor3 "Как же ты прекрасна, дорогая!"
    investor3 "Я так соскучился по тебе!"
    # Линда тянет к нему бокал, чтобы чокнуться
    img 18068
    w
    img 18069
    w
    img 18070
    linda "За встречу?"
    investor3 "За встречу!"
    img 18071
    # затемнение экрана, звон бокалов

    # кадр меняется, Моника со злым лицом также стоит, эти двое сидят за "столиком"
    # клиент держит руку Линды в своей руке
    img 18072
    investor3 "Линда, ты необыкновенная девушка!"
    investor3 "Я очень тебя люблю!"
    # Линда ему улыбается и смущенно опускает глазки
    img 18073
    w
    img 18074
    w
    img 18075
    w
    img 18076
    investor3 "Дорогая, может быть, сегодня ты согласишься заняться со мной любовью?"
    investor3 "Я так долго жду этого. Так безумно хочу тебя..."
    img 18084
    # она мило ему улыбается
    img 18077
    linda "Я тоже хочу этого, но..."
    img 18078
    w
    img 18079
    linda "Для этого мы должны быть вместе."
    linda "Не просто встречаться раз в неделю в номере отеля..."
    linda "А жить вместе, дорогой."
    img 18080
    linda "Когда ты меня заберешь отсюда?" # капризно
    investor3 "Любимая, осталось подождать совсем немного..."
    investor3 "Я собираюсь поговорить с женой на днях..."
    investor3 "Потом я подам на развод и сразу заберу тебя отсюда!"
    img 18081
    linda "..."
    linda "Правда?"
    img 18082
    investor3 "Да, любимая."
    investor3 "Мне больно сознавать тот факт, что ты вынуждена работать здесь."
    investor3 "И эти мысли отравляют мою душу и не дают мне покоя..."
    # Линда говорит
    img 18083
    linda "Любимый, я с нетерпением жду, когда мы сможем жить вместе!"
    linda "Только представь: тогда нам больше никто и ничто не помешает любить друг друга!"
    investor3 "О, Линда! Любимая моя девочка!"
    # они наклоняются друг к другу и целуются (анимация-?)
    # Моника все это время стоит в позе столика со злобным лицом
    img 18085
    w
    img 18086
    w
    img 18087
    w
    img 18090
    mt "Меня уже тошнит от этих мерзких нежностей!"
    mt "!!!"
    mt "Вот стерва эта Линда!"
    mt "Спит тут с разными мужчинами, а этому придурку пудрит мозги, что его любит!"
    mt "Этот инвестор действительно такой идиот или притворяется?"
    img 18091
    mt "..."
    mt "Хммм... Интересно..."
    mt "Будь я на ее месте... Сделала бы я то же самое или нет?"
    mt "Это могло бы быть неплохой возможностью..."
    mt "..."
    # клиент продолжает держать руку Линды
    img 18092
    linda "Дорогой, ну сколько мне еще ждать?"
    linda "Знаешь, мне предлагают свою руку и сердце и другие мужчины..."
    linda "..."
    # инвестор горделиво
    img 18093
    investor3 "Но они явно не такие успешные как Я!"
    investor3 "У меня очень много проектов, включая инвестиционные."
    investor3 "Ты знаешь о том, что я даже являюсь ключевым инвестором одного модного журнала?"
    investor3 "Я одним движением руки могу сделать тебя супер моделью мирового масштаба."
    # Моника офигевает
    img 18094
    mt "ЧТОООООО?!"
    mt "?!?!?!"
    # Линда заинтересованно
    img 18073
    linda "Модный журнал? Как интересно!"
    investor3 "Да, дорогая... Может, ты слышала о Монике Бакфетт?"
    img 18095
    mt "!!!"
    img 18076
    investor3 "Она является создателем и лицом этого журнала."
    # Линда задумчиво
    img 18077
    linda "Да, я слышала где-то имя... Это какая-то бизнес-вумен?"
    investor3 "Да, это очень известная персона в нашем городе."
    img 18095
    mt "Он говорит ей про меня!!!"
    mt "!!!"
    mt "Хорошо, что такие никчемные дуры как она не читают журналы о моде!"
    mt "Черт!"
    img 18096
    mt "А если она после разговора с ним захочет купить и посмотреть мой журнал?!"
    mt "Что тогда?!"
    mt "!!!"
    mt "!!!!!!"
    # Линда тянется к инвестору за поцелуем
    img 18097
    linda "Дорогой, ты такой умный!"
    linda "Я так тебя люблю!"
    # они снова целуются
    img 18085
    w
    img 18089
    w
    img 18088
    # затемнение экрана

    # прошло некоторое время
    # Линда и инвестор сидят рядом на кровати, он гладит ее руку, целует
    # Линда мечтательно
    img 18098
    w
    img 18099
    linda "Скорее бы мы стали жить вместе..."
    linda "Каждую ночь засыпали бы вместе в одной кровати..."
    linda "И я смогла бы забыть эту кошмарную работу, как страшный сон."
    img 18100
    investor3 "Девочка моя любимая, я все сделаю для того, чтобы это случилось как можно быстрее!"
    # целуются
    img 18101
    w
    img 18102
    w
    img 18103
    w
    img 18104
    w
    img 18108
    mt "Да сколько уже можно лизаться?! Фу!"
    img 18105
    linda "Дорогой, убери поднос с моего реквизита..."
    linda "У меня устали ножки."
    investor3 "Да, любимая. Сейчас."
    # он убирает поднос, она складывает свои ноги Монике на спинку, вытягивается
    img 18106
    w
    img 18107
    mt "СУЧКА!!!"
    mt "Охреневшая мерзкая тварь!!!"
    mt "Убью!!!"
    mt "!!!"
    img 18109
    w
    img 18111
    investor3 "Не хочу расставаться с тобой сегодня..."
    investor3 "Я уже скучаю по тебе и хочу поскорее следующей нашей встречи..."
    img 18110
    linda "Любимый, я тоже жду нашей встречи с нетерпением..."
    # Моника психует
    img 18112
    mt "Когда уже это все кончится?!"
    mt "Когда эта сучка уберет с меня свои мерзкие ноги?!"
    mt "!!!"
    # Линда встает
    img 18113
    w
    img 18062
    mt "Ну наконец-то!"
    mt "Сучка!"
    mt "!!!"
    # инвестор тоже встает, обнимает ее, целует
    img 18114
    w
    img 18115
    linda "Любимый, мне жаль, но мне пора идти."
    linda "Надеюсь, что ты расскажешь о наших отношениях своей жене."
    linda "И подашь с ней на развод."
    img 18116
    investor3 "Я обещаю тебе, любимая, что совсем скоро мы будет вместе!"
    img 18117
    w
    img 18118
    # Линда направляется к выходу
    img 18119
    linda "Дорогой, я оставляю тебе свой реквизит..."
    linda "Можешь им воспользоваться..."
    investor3 "???"
    img 18120
    linda "Я понимаю что тебе одиноко, пока ты ждешь нашего воссоединения."
    linda "Можешь сделать это... Я не буду ревновать."
    linda "Это уже включено в ту сумму, что ты заплатил за нее."
    # Линда уходит, Моника с облегчением
    img 18063
    mt "Сейчас этот идиот свалит отсюда и я, наконец-то, смогу встать!"
    mt "У меня отнимаются ноги и руки!"
    mt "Я больше не могу так стоять!!!"
    mt "Давай, придурок, вали отсюда скорее!"
    mt "!!!"
    # затемнение, звук шагов
    return

# номер отеля
label ep213_dialogues2_escort_6:
    # Моника стоит "столиком", инвестор подошел к ней, стоит рядом и рассматривает ее с интересом
    img 18121
    w
    img 18122
    investor3 "Ну что? Раз Линда снова отказала мне и ушла... Оставив мне тебя..."
    investor3 "Значит, пришло время познакомиться с тобой поближе..."
    investor3 "А то у меня уже яйца опухли!"
    # Моника мысленно в панике
    img 18123
    mt "Поближе?! О, нет!"
    mt "Только не это!"
    mt "!!!"
    mt "А вдруг он снимет с меня маску?! Он узнает меня!"
    mt "Да он просто по голосу может меня узнать!!!"
    img 18124
    mt "!!!"
    mt "Моника, ни в коем случае нельзя допустить этого!"
    mt "Последствия для тебя будут ужасными!"
    mt "!!!"
    menu:
        "Убежать отсюда!!!":
            # Моника в панике
            img 18125
            mt "Нужно срочно бежать отсюда, пока он не раскрыл мою личность!"
            mt "Это будет провал!"
            mt "Моника, быстрее! Беги отсюда!"
            mt "!!!"
            # Моника убегает, инвестор с недоумением смотрит ей вслед
            img 18126
            investor3 "???"
            return
        "Промолчать и остаться в номере.":
            $ monicaEscortLindaTable2 = True # Моника осталась с инвестором вдвоем в отеле
            pass
    # Моника напряжена
    img 18125
    mt "Если я сейчас убегу, то у меня будут проблемы с сучкой-администраторшей..."
    mt "Она меня уволит, а мне нужны деньги! Черт!"
    mt "!!!"
    mt "Лучше я останусь и дождусь, когда этот никчемный идиот уйдет отсюда."
    mt "..."
    # Моника ничего не отвечает на его вопрос
    img 18124
    mt "Самое главное, чтобы он не снял с меня маску..."
    mt "..."
    # инвестор немного наклоняется и шлепает Монику по попе
    img 18127
    w
    investor3 "Чего ты молчишь?"
    investor3 "После очередного отказа Линды мне требуется компенсация."
    img 18146
    w
    img 18147
    # Моника в шоке, но продолжает упорно молчать
    img 18107
    mt "!!!"
    mt "Твою мать!"
    mt "Чертов извращенец!!!"
    # инвестор расстегивает брюки, достает свой стояк
    img 18128
    investor3 "Встань на колени!"
    mt "!!!"
    menu:
        "Сделать как требует инвестор.":
            pass
    # Моника поднимается с четверенек и стоит только на коленях, не смотрит на него
    img 18129
    w
    img 18129
    w
    img 18130
    mt "Главное, чтобы он не узнал меня!"
    img 18131
    investor3 "На меня смотри!"
    mt "!!!"
    # она поднимает лицо и смотрит на него
    img 18132
    # он держит свой стояк перед ее лицом, медлит
    investor3 "Хм... Странно, но мне кажется, что я тебя где-то видел..."
    investor3 "..."
    img 18133
    mt "Дьявол!"
    mt "!!!"
    img 18134
    investor3 "Как тебя зовут?"
    menu:
        "Промолчать.":
            pass
    img 18135
    m "..."
    img 18136
    investor3 "Молчишь?"
    investor3 "Тогда я буду звать тебя Линдой."
    investor3 "Хотя нет..."
    investor3 "Тебе лучше пойдет имя Грязная шлюшка."
    img 18137
    investor3 "Конечно, если ты против, ты можешь сказать мне об этом."
    investor3 "А если тебе все нравится - тогда просто продолжай молчать."
    investor3 "Аха-ха!"
    m "!!!" # зло
    menu:
        "Врезать ему по яйцам!!! (прерывание квеста и увольнение с эскорта)":
            # Моника злобно смотрит на него
            img 18138
            m "Я тебе не грязная шлюшка!"
            m "Ублюдок!"
            m "!!!"
            # бьет или по мошонке или по члену
            # он загибается
            img 18139
            w
            img 18140
            w
            img 18141
            investor3 "АААААА!!!"
            investor3 "ПОДЛАЯ СУКА!!!"
            investor3 "!!!"
            img 18142
            mt "Моника, быстрее! Беги отсюда!"
            mt "!!!"
            # Моника убегает, инвестор остается валяться на полу
            img 18144
            investor3 "АААААА!!!"
            $ monicaEscortLindaTable3 = True # Моника врезала инвестору по яйцам
            return
        "Убежать отсюда!!!":
            # Моника в панике
            img 18130
            mt "Нет! Я не позволю какому-то неудачнику унижать меня!"
            mt "!!!"
            mt "Моника, быстрее! Беги отсюда!"
            mt "!!!"
            # Моника убегает, инвестор с недоумением смотрит ей вслед
            img 18145
            investor3 "???"
            return
        "Промолчать и остаться в номере.":
            $ monicaEscortLindaTable4 = True # Моника промолчала, когда инвестор стал называть ее грязной шлюшкой
            pass
    # Моника зло на него смотрит, но продолжает молчать
    img 18130
    mt "Вот урод!"
    mt "!!!"
    mt "Но если я что-то скажу ему, он может узнать мой голос!"
    mt "!!!"
    mt "И убежать я не могу. Мне не нужны проблемы с администратором!"
    mt "Ненавижу!"
    mt "!!!"
    img 18143
    investor3 "Грязная шлюшка молчит?"
    investor3 "Аха-ха!"
    investor3 "Просто ей нравится мой член."
    # он приближает свой стояк к ее лицу, стукает им по ее лбу
    img 18148
    w
    img 18149
    investor3 "Нравится тебе, шлюшка?"
    investor3 "Хочешь его?"
    investor3 "Смотри, какой он твердый..."
    img 18150
    mt "ФУУУ!"
    mt "!!!"
    # инвестор начинает водить своим стояком по ее щекам, по губам
    img 18151
    ц
    img 18152
    w
    img 18153
    w
    img 18154
    w
    img 18155
    investor3 "Ты ведь любишь сосать члены, грязная шлюшка?"
    investor3 "Сколько членов в день через тебя проходят, м? 10? Или 20?"
    img 18156
    mt "!!!"
    mt "Ублюдок!"
    img 18157
    investor3 "Ты сейчас мечтаешь о том, чтобы взять мой член в рот, да?"
    investor3 "Очередной член, чтобы заработать еще немного денег..."
    # Моника злобно смотрит на него
    img 18158
    mt "Я мечтаю о том, чтобы оторвать тебе яйца, скотина!"
    investor3 "Так уж и быть..."
    investor3 "Я не буду мучать грязную шлюшку и дам тебе пососать его."
    investor3 "Открывай рот!"
    menu:
        "Открыть рот.":
            pass
    img 18159
    m "!!!"
    # инвестор вводит член в ее приоткрытые губы
    img 18160
    w
    img 18161
    investor3 "Оооо..."
    # Моника начинает водить головой туда-сюда
    img 18162
    investor3 "Дааа..."
    w
    img 18163
    investor3 "Давай, быстрее..."
    img 18164
    investor3 "Еще!"
    investor3 "Глубже!"
    # он берет ее руками за голову и глубоко входит в нее, Моника давится, у нее текут слезы
    img 18165
    investor3 "Вот таааак..."
    img 18166
    m "!!!"
    img 18167
    m "ХПФМММ!"
    img 18168
    m "ММПППХХХФФФФ!!!"
    # через несколько толчков он отстраняет Монику от себя
    img 18137
    investor3 "Теперь снимай платье и ложись на кровать!"
    investor3 "Сейчас я оттрахаю тебя, грязная шлюшка."
    img 18143
    investor3 "Ты же хочешь этого?"
    investor3 "Конечно, если ты не хочешь, ты можешь сказать мне об этом."
    investor3 "Аха-ха!"
    img 18132
    m "!!!" # зло
    menu:
        "Врезать ему по яйцам!!! (прерывание квеста и увольнение с эскорта)":
            # Моника злобно смотрит на него
            img 18138
            m "Я тебе не грязная шлюшка!"
            m "Ублюдок!"
            m "!!!"
            # бьет или по мошонке или по члену
            # он загибается
            img 18139
            w
            img 18140
            w
            img 18141
            investor3 "АААААА!!!"
            investor3 "ПОДЛАЯ СУКА!!!"
            investor3 "!!!"
            img 18142
            mt "Моника, быстрее! Беги отсюда!"
            mt "!!!"
            # Моника убегает, инвестор остается валяться на полу
            img 18144
            investor3 "АААААА!!!"
            $ monicaEscortLindaTable5 = True # Моника врезала инвестору по яйцам после минета
            return
        "Убежать отсюда!!!":
            # Моника в панике
            img 18130
            mt "Нет! Я больше не позволю этому неудачнику унижать меня!"
            mt "!!!"
            mt "Моника, быстрее! Беги отсюда!"
            mt "!!!"
            # Моника убегает, инвестор с недоумением смотрит ей вслед
            img 18145
            investor3 "???"
            return
        "Промолчать и остаться в номере.":
            $ monicaEscortLindaTable6 = True # Моника промолчала, когда инвестор сказал, что оттрахает ее
            pass
    # Моника зло на него смотрит, но продолжает молчать
    img 18169
    mt "Он пользуется тем, что я молчу, потому что боюсь раскрыть свою личность!"
    mt "Мерзавец!"
    mt "Ненавижу!!!"
    mt "!!!"
    menu:
        "Снять платье и лечь на кровать.":
            pass
    # Моника снимает платье и ложится на спину на кровать
    img 18170
    mt "Я сотру этого неудачника в порошок!"
    mt "!!!"
    img 18171
    w
    img 18172
    w
    img 18173
    w
    img 18174
    # он лезет на нее сверху
    investor3 "Грязная шлюшка послушная."
    investor3 "Мне это нравится..."
    # вводит свой член в ее киску
    img 18176
    mt "Долбанный неудачник!"
    mt "Знал бы он, кого он тут обзывает шлюшкой!!!"
    mt "Сволочь!!!"
    mt "!!!"
    # инвестор шпилит Монику
    img 18175
    w
    img 18177
    investor3 "Дааа..."
    img 18178
    w
    img 18179
    w
    img 18180
    w
    img 18181
    w
    img 18182
    investor3 "Грязной шлюшке нравится чувствовать в себе члены?"
    img 18183
    investor3 "Ааааа! Сучкааа!"
    img 18184
    investor3 "Она любит трахаться с незнакомыми мужиками!"
    img 18185
    investor3 "Грязная сучка!"
    investor3 "Ради денег готова раздвигать ноги перед всеми!"
    img 18186
    mt "Я убью его!"
    mt "Он еще будет ползать у меня в ногах и просить прощения!"
    mt "Тварь!!!"
    mt "!!!"
    img 18187
    menu:
        "Кончить внутрь Моники.":
            img 18188
            investor3 "Аааа... Кончаю!"
            investor3 "Линда, даааааааа!!!"
            investor3 "ЛИНДАААААААА!!!"
            img 18189
            mt "Перед тем, как я его убью, я оторву ему яйца!"
            mt "!!!"
            img 18190
            pass
        "Кончить на киску Моники.":
            img 18188
            investor3 "Аааа... Кончаю!"
            investor3 "Линда, даааааааа!!!"
            investor3 "ЛИНДАААААААА!!!"
            img 18189
            mt "Перед тем, как я его убью, я оторву ему яйца!"
            mt "!!!"
            img 18191
            w
            img 18192
            pass
    # затемнение
    # Моника сидит на кровати в платье, инвестор стоит перед кроватью уже одетый
    investor3 "Отличная шлюшка... Мне понравилось."
    investor3 "В следующий раз попрошу Линду снова привести тебя поработать реквизитом."
    investor3 "Аха-ха!"
    # Моника зло смотрит
    mt "Оторву яйца, но убивать не буду!"
    mt "Пусть этот ублюдок живет с этим и мучается!"
    mt "!!!"
    # инвестор уходит
    # Моника сидит на кровати в номере одна
    mt "Это было отвратительно!!!"
    mt "Я себя чувствую нечистой. Как-будто меня выпачкали в грязи."
    mt "Я хочу принять душ."
    mt "..."
    mt "А если бы этот мерзавец захотел снять с меня маску?!"
    mt "!!!"
    mt "Моника, какой кошмар! Даже не думай об этом!"
    mt "!!!"
    retutn

# ресепшн, если отказалась работать "столиком" и послала Линду
# либо если ударила инвестора по яйцам
# диалог с лейбла ep212_dialogues3_escort_hotel_5_1 - увольнение


# ресепшн, если отработала, в том числе если просто молча убежала от инвестора
label ep213_dialogues2_escort_7:
    # Моника подходит на ресепшн, говорит недовольно
    img 30107
    m "Я закончила на сегодня работу."
    m "Сделала все, как надо."
    m "Клиент должен быть доволен."
    img 30113
    reception "[monica_hotel_name], я уже пообщалась с Линдой..."
    m "..."
    img 17525
    reception "Она сказала, что не совсем довольна твоей работой!"
    reception "Ей показалось, что ты не понравилась ее клиенту."
    # Моника в шоке
    img 30110
    m "Что?!"
    m "?!"
    m "Да она..."
    # администратор ее перебивает
    img 17509
    reception "Тихо! Я еще не договорила!"
    img 30114
    m "..."

    #     если был секс с инвестором
    img 30108
    reception "Но клиент мне сказал совсем другое..."
    reception "Он очень доволен твоей работой."
    reception "И еще он оставил тебе чаевые, про которые просил не рассказывать Линде."
    img 17520
    m "Серьезно?!"
    # протягивает ей деньги
    img 30111
    reception "Да. Вот твой заработок."
    img 30112
    reception "Здесь 350 долларов."
    reception "Процент я уже вычла."
    $ add_money(350.0)

    #     если секса не было и Моника сбежала
    img 30108
    reception "Но так как ты не делала никаких глупостей..."
    reception "То я тебе заплачу 10 процентов от заработка Линды."
    reception "Думаю, этого будет более, чем достаточно..."
    img 17520
    m "Серьезно?!"
    # протягивает ей деньги
    img 30111
    reception "Да. Вот твой заработок."
    img 30112
    reception "Здесь 100 долларов."
    $ add_money(100.0)
    img 30113
    reception "На сегодня все, [monica_hotel_name]."
    reception "Приходи завтра. Клиенты любят свежих девочек, а не использованных."
    # Моника про себя думает, что ей могли бы заплатить и больше!
    img 30115
    mt "Могла бы заплатить и больше!"
    mt "Сучка!!!"
    mt "!!!"
    return

# Моника вышла на улицу после диалога на ресепшене (если ей админ заплатила за работу)
label ep213_dialogues2_escort_8:
    # не рендерить!!
    mt "Сучка Линда специально нажаловалась администратору!"
    mt "Стерва!!!"
    mt "!!!"
    mt "Гребанный инвестор!"
    mt "Мерзкий отвратительный ублюдок!!!"
    mt "АААААА!!!"
    mt "НЕНАВИЖУ ИХ!"
    mt "!!!!!"
    return


# Моника вышла на улицу после увольнения (послала Линду перед клиентом или ударила клиента)
# лейбл ep212_dialogues3_escort_hotel_7_1


# диалог с Линдой после этой сцены
# когда Моника только пришла в ресторан и села за свой столик, чтобы работать эскортницей
label ep213_dialogues2_escort_9:
    # подходит Линда и брюнетка с каре
    # они смотрят на Монику насмешливо, Моника на них злобно
    img 18027
    girl_1 "Линда, смотри, кто пришел!"
    mt "Что этим сучкам нужно от меня?!"
    linda "Привет..."
    img 18028
    m "..." # Моника вызывающе смотрит на Линду
    img 18029
    linda "..."
    linda "Я жду, что ты будешь более вежливо общаться со мной."
    linda "Иначе я придумаю еще что-нибудь, что можно с тобой сделать."
    img 18030
    girl_1 "Хи-хи-хи..."
    girl_1 "Линда, ты что, меня опередила?"
    girl_1 "Я хотела, чтобы она отлизала у меня первой."
    # Линда улыбается своей подружке
    img 18031
    linda "Дорогая, я всегда впереди всех."
    img 30081
    m "..."
    menu:
        "Послать их!":
            img 30084
            mt "Эти сучки думают, что смогут запугать МЕНЯ?!"
            mt "Я, Моника Бакфетт! Я никогда не позволю унижать себя!"
            mt "Придет время и я всем им отомщу!"
            mt "!!!"
            img 18032
            m "Проваливайте отсюда!"
            m "Дешевые проститутки-эскортницы!"
            m "Серые мыши!"
            m "!!!"
            # девочки зло переглядываются
            img 18034
            linda "!!!"
            girl_1 "!!!"
            # и уходят
            img 18035
            $ monicaEscortLindaTable7 = True # Моника снова нахамила Линде (после сцены с инвестором)
            pass
        "Поздороваться с Линдой.":
            img 30084
            mt "Я сделаю вид, что принимаю их правила..."
            mt "Эти дуры все равно не поймут, что я просто притворяюсь."
            mt "Придет время и я им всем отомщу!"
            mt "!!!"
            img 18033
            m "Привет..."
            linda "Так-то лучше!"
            # зло смеются
            img 18034
            linda "Аха-ха!!!"
            girl_1 "Аха-ха!!!"
            # уходят
            img 18035

            pass
    # Моника недовольно
    img 30077
    mt "Мерзкие высокомерные стервы!"
    mt "Что они о себе возомнили?!"
    mt "?!?!?!"
    return
