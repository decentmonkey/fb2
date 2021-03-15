define neighbor2 = Character(_("Сосед Эбби"), who_color=c_red)  # сосед Эбби
define brian = Character(_("Брайан"), who_color=c_orange)  # клиент Эбби вне эскорта

default monicaAbbyNoEscortClient1 = 0 # Моника согласилась поехать домой к Эбби и встретиться с ее клиентом вне эскорта
default monicaAbbyNoEscortClient2 = 0 # Моника изменила свое решение и согласилась работать с клиентами Эбби
default monicaAbbyNoEscortClient3 = 0 # Моника согласилась на секс с клиентом Эбби, не стала выгонять его
default monicaAbbyNoEscortClient4 = 0 # Моника не оставила Эбби процент, забрала все деньги


# при условии, если Моника была в гостях у Эбби
# ресторан отеля Ле Гранд
label ep22_4_dialogues5_escort_1:
	# у входа в ресторан, перед столиками Моника видит Эбби
    abby "[monica_hotel_name], привет."
    abby "Как у тебя дела?"
    mt "Какая ей разница, как у меня дела?!"
    mt "!!!"
    mt "Так, Моника, нужно быть более осторожной с этой Эбби."
    mt "Во-первых, она знает, кто главный в ВИП-эскорте."
    mt "Если я сделаю так, что она начнет мне доверять..."
    mt "То она поделится со мной этой информацией."
    # если была в гостях у Линды
    mt "Надеюсь, что она не знает о моей 'дружбе' с лицемерками Линдой и Мирандой."
    mt "Если она что-то заподозрит, то ни о каком доверии и речи быть не может."
    # если Моника сука
    mt "Я сделаю все, чтобы обыграть этих проституток-эскортниц!"
    mt "Я здесь самая умная и только я достойна занять место администраторши!"
    # если бичность низкая
    mt "Не известно, насколько верно я поступаю, обманывая этих проституток..."
    mt "Но пока у меня нет иного выхода..."
    mt "Я вынуждена притворяться их подругой."
    #
    # Моника притворно
    m "Привет, Эбби."
    m "Все нормально. Как у тебя дела?"
    abby "У меня всегда все окей."
    abby "Я хотела спросить тебя..."
    # если Моника согласилась работать с клиентами Эбби
    # if monicaAbbyRentHelp7 > 0:
    abby "Как у тебя с доходами от работы в эскорте?"
    m "Могло быть и лучше..."
    abby "Отлично. Значит, ты будешь заинтересована в подработке..."
    label ep22_4_dialogues5_escort_1a:
    abby "Мне сегодня позвонил один из моих клиентов вне ВИП-эскорта."
    abby "Хочет встретиться, а у меня на него нет времени."
    abby "Да и желания особого нет с ним встречаться..."
    m "Что за клиент?"
    abby "Да он нормальный чувак. Жадный немного, но в целом пойдет... Если совсем нет денег."
    abby "Короче, я сейчас ему позвоню и скажу, что его обслужит моя напарница, то есть ты."
    m "Подожди-подожди! Что, прямо сегодня?!"
    abby "Ага."
    m "А где?"
    abby "У меня дома. Я встречаюсь с этими клиентами только там."
    abby "В ВИП-эскорте никто об этом не должен узнать."
    abby "Мне не нужны лишние проблемы с администраторшей."
    abby "Ну что? Ты готова?"
    mt "Черт!"
    mt "!!!"
    # коррапшн
    menu:
        "Да, готова.":
            $ monicaAbbyNoEscortClient1 = day # Моника согласилась поехать домой к Эбби и встретиться с ее клиентом вне эскорта
            pass
        "Нет!":
            # Моника недовольно
            mt "Я не собираюсь возиться с этими извращенцами!"
            mt "Еще и дома у этой проститутки-эскортницы!"
            mt "Не смотря на то, что мне нужны деньги, я не хочу идти на это!"
            mt "По крайней мере, не сегодня!"
            m "Нет, Эбби! На сегодня у меня другие планы!"
            m "Возможно, в следующий раз..."
            abby "Окей. Как знаешь."
			abby "Если что - обращайся."
            # Эбби отходит от Моники
            return
    # если Моника в первый раз отказалась работать с клиенами Эбби
    # else:
    abby "Ты не передумала насчет моего предложения?"
    m "Какого предложения?"
    abby "Хорош тупить, [monica_hotel_name]!"
    m "!!!"
    abby "Я про своих клиентов вне ВИП-эскорта..."
	abby "Может, ты передумала и хочешь, чтобы я поделилась с тобой ими?"
	m "..."
	menu:
		"Отказаться! (прерывание квеста)":
            # Моника задумчиво
			mt "Она предлагает мне обслуживать каких-то нищебродов за гроши?!"
			mt "А сама хочет занять место на ресепшене?!"
			mt "Хитрая дешевая подстилка!"
			mt "!!!"
			mt "Это Я стану главной и буду решать, когда и под кого ты будешь ложиться!"
			mt "Сучка!!!"
			# Моника притворно улыбается
			m "Мне хватает того, что я зарабатываю в отеле..."
			m "А когда ты станешь... Кхм... Главной..."
			m "Я буду зарабатывать еще лучше."
			m "Спасибо, что предложила."
			m "Если я по какой-то причине изменю свое решение, я дам тебе знать."
			abby "Окей. Как знаешь."
			abby "Если что - обращайся."
            # Эбби отходит от Моники
            mt "Не хватало мне еще возиться с каким-то жалким отребьем!"
            mt "Я найду способ заработать деньги без этой гадости!"
            mt "!!!"
			return
		"Согласиться.":
			$ monicaAbbyNoEscortClient2 = day # Моника изменила свое решение и согласилась работать с клиентами Эбби
			mt "Черт!"
			mt "Я должна каждую неделю отдавать этой мерзкой сикалявке Виктории $ 5 000!"
			# если должна Перри
			mt "И еще выплачивать долг мерзкой Перри!"
			# если арендует апартаменты у Джека
			mt "И платить за грязную дыру, которую мне сдает Джек!"
			#
			mt "Мне нужны эти деньги!"
			mt "Но, Моника, неужели ты ради денег..."
			mt "Будешь обслуживать каких-то жалких, никчемных отбросов от Эбби?!"
			mt "Ты готова пойти на это?!"
			mt "?!?!?!"
			mt "Черт!!!"
			m "Я... Я думаю, что..."
			m "Что я попробую..."
			abby "Окей!"
			abby "Ты приняла верное решение, [monica_hotel_name]."
			jump ep22_4_dialogues5_escort_1a
    label ep22_4_dialogues5_escort_1b:
    # Моника задумчиво
    mt "Если я сейчас откажусь от встречи с ее гребаным клиентом..."
    mt "То рискую вообще ничего не заработать сегодня."
    mt "А мне нужны деньги."
    mt "Но это так отвратительно!"
    mt "!!!"
    mt "С другой стороны, возможно, мне стоит попробовать?"
    mt "Всего один раз..."
    mt "Зато я смогу заработать."
    mt "А если мне что-то не понравится..."
    mt "То я просто пошлю эту Эбби с ее дурацкими клиентами ко всем чертям!"
    mt "Да, я думаю, что это самое верное решение!"
    # Моника, притворно улыбаясь
    m "Да, Эбби. Я поеду."
    abby "Окей. Я тогда сейчас позвоню клиенту."
    abby "Короче, слушай..."
    abby "Сейчас поедешь ко мне домой."
    abby "Первое правило - ты должна принять душ до работы с клиентом."
    m "Не логичнее это сделать после?"
    abby "Нет! Вообще-то, ты будешь обслуживать его на моей постели!"
    abby "Так что, сначала в душ, а потом - трах с ним."
    mt "Фу, как грубо!"
    mt "!!!"
    abby "И клиента, кстати, тоже отправь в душ! Это обязательно!"
    abby "Полотенце для душа можешь взять мое. Я его, по-моему, на кровати оставила."
    mt "Надеюсь, оно чистое!"
    mt "!!!"
    abby "К клиенту обращайся по имени. Его зовут Брайан."
    # Моника язвительно
    m "Постараюсь не перепутать и не назвать его другим именем."
    m "Какие-то еще инструкции будут?"
    abby "Да. У меня через стену живет один придурок."
    abby "Везде сует свой нос. Любитель поскандалить и поворчать."
    abby "На него внимания не обращай."
    abby "Если он будет надоедать, скажи ему 'пошел на хрен отсюда, трахаюсь с кем хочу' и он отстанет."
    m "Что, так и сказать?!"
    m "Это же не прилично!"
    abby "Клиентов домой водить тоже неприлично."
    abby "И ты не высокосветская леди, так что можно обойтись без реверансов."
    m "!!!" # зло
    # Эбби сосредоточенно
    abby "Так, вроде бы я все тебе сказала."
    m "Тогда я пошла."
    abby "А, вот еще!"
    abby "Треть денег, которые Брайан тебе заплатит, оставишь на столе."
    abby "Это будет мой процент."
    abby "Теперь все."
    # затемнение, каблуки
    return

# ресторан отеля Ле Гранд
# если Моника отказалась поехать к клиенту Эбби
# при клике на Эбби
label ep22_4_dialogues5_escort_2:
	# у входа в ресторан, перед столиками
    m "Привет, Эбби."
    abby "[monica_hotel_name], привет."
    abby "Что насчет подработки?"
    abby "Я с тем клиентом так и не встретилась."
    abby "А ему не терпится и он готов приехать в любую минуту."
    abby "Если ты готова, то я позвоню ему..."
    mt "Черт!"
    mt "!!!"
    # коррапшн
    menu:
        "Да, готова.":
            $ monicaAbbyNoEscortClient1 = day # Моника согласилась поехать домой к Эбби и встретиться с ее клиентом вне эскорта
            jump ep22_4_dialogues5_escort_1b
        "Нет!":
            # Моника недовольно
            mt "Я не собираюсь возиться с этими извращенцами!"
            mt "Еще и дома у этой проститутки-эскортницы!"
            mt "Не смотря на то, что мне нужны деньги, я не хочу идти на это!"
            mt "По крайней мере, не сегодня!"
            m "Нет, Эбби! На сегодня у меня другие планы!"
            m "Возможно, в следующий раз..."
            abby "Окей. Как знаешь."
			abby "Если что - обращайся."
            # Эбби отходит от Моники
            return
    return

# мысли Моники перед домом Эбби, до встречи с клиентом
label ep22_4_dialogues5_escort_3:
	# не рендерить!!
    mt "Моника, ты понимаешь, что сейчас происходит?"
    mt "Ты сейчас пойдешь обслуживать какого-то отброса вместо проститутки Эбби!"
    mt "Ты действительно пойдешь на ЭТО?!"
    mt "Стоят ли эти деньги таких жертв с твоей стороны?!"
    mt "?!?!?!"
    return

# комната Эбби
label ep22_4_dialogues5_escort_4:
	# Моника заходит с отвращением на лице
    mt "Детская комната!.."
    mt "В которой гребаная Эбби обслуживает своих гребаных клиентов!"
	mt "И теперь ты, Моника, будешь делать то же самое! Кошмар!"
    mt "Зачем я только согласилась на это безумие?!"
    mt "!!!"
    mt "Так, что мне нужно сделать сначала?"
    mt "Что там говорила эта проститутка Эбби?"
    mt "Принять самой душ, потом отправить туда клиента..."
    mt "Называть клиента только по имени."
    mt "Хмм... По-моему, я забыла его имя..."
    mt "Неважно! Обойдется!"
    mt "Еще я не обращалась по имени ко всяким ничтожествам!"
    mt "!!!"
    menu:
        "Принять душ.":
            pass
    # Моника подходит к кровати и смотрит на полотенце
    mt "Это же то полотенце, в котором проститутка Эбби брила свою... В общем, брилась."
    mt "Я к этому полотенцу даже прикасаться не хочу!.."
    mt "А мне придется воспользоваться им после душа! Фи!"
    # Моника тянет руку к полотенцу
    # затемение, шуршание одежы, шаги босиком
    # смена кадра
    # душ, Моника заходит и брезгливо оглядывается
    mt "Фууу!!!"
    mt "Это что, общий душ?!"
    mt "Здесь такое все!.. Грязное!"
    mt "Моника, постарайся ни к чему не прикасаться!"
    mt "Ты сейчас быстро примешь душ и пойдешь в комнату..."
    # затемнение, кран, шум воды
    # Моника стоит в душе
    mt "Как же все-таки приятно..."
    mt "Мне вода всегда помогала успокоиться..."
    mt "Очистить голову от лишних мыслей..."
    mt "Расслабиться..."
    mt "Мммм..."
    # хлопает дверь
    # Моника испуганно открывает глаза
    mt "Это еще что такое?!"
    mt "Я что, не закрыла дверь?!"
    m "Кто там?!"
    m "Вообще-то, здесь занято!"
    # к душевой кабинете подходит сосед Эбби
    neighbor2 "А ты кто такая?"
    neighbor2 "Что ты здесь делаешь?!"
    # Моника прикрывается руками или хватает полотенце и прикрывается им
    m "Отвернулся быстро!"
    m "Ты что, не видишь, что перед тобой дама?!"
    neighbor2 "Тоже мне дама нашлась!"
    neighbor2 "Чего я там не видел?!"
    m "Отвернись!!!"
    neighbor2 "Еще чего!!!"
    neighbor2 "Это не твой душ! Ты чего сюда приперлась?!"
    m "Я!.. Мне!.."
    m "Мне Эбби разрешила!"
    neighbor2 "Эбби?! Шлюшка из соседней комнаты?!"
    neighbor2 "Так значит, ты ее подружка будешь?!"
    neighbor2 "Или коллега?!"
    m "Не твое дело!"
    neighbor2 "Вот именно, что МОЕ дело!"
    neighbor2 "Устроили тут проститутошную, а я должен все это терперть?!"
    neighbor2 "Я буду жаловать хозяину апартаментов!"
    neighbor2 "Какие-то дешевые шлюхи таскают сюда своих клиентов!"
    neighbor2 "Идите на улице работать, проститутки!"
    # Монику бомбит
    m "Ты где здесь проститутку увидел, придурок?!"
    m "Пошел вон отсюда, пока я полицию не вызвала!!!"
    neighbor2 "Вызывай! Полиция мне поверит, а не какой-то шлюхе!"
    m "Я не шлюха!!!"
    m "Я скажу, что ты меня домогался и тебя посадят за решетку!"
    neighbor2 "Я?! Что я домогался тебя?!"
    neighbor2 "Нужна ты мне больно, грязная шлюшка."
    m "Кретин!!!"
    # сосед осматривает Монику с головы до ног
    neighbor2 "Если хочешь, чтоб я ушел, покажи мне свои сиськи."
    m "ЧТООО?!"
    m "Совсем охренел, старый извращенец?!"
    m "А ну-ка пошел вон отсюда!"
    neighbor2 "Покажешь сиськи - не буду жаловаться хозяину апартаментов."
    # Моника зло его выталкивает из ванной комнаты
    m "ВООООН!"
    m "!!!"
    # остается одна
    mt "Какое-то безумие!!!"
    mt "Грязные отбросы общества позволяют себя так вести с тобой, Моника!"
    mt "Как он мог?!"
    mt "Мерзкий, противный старикашка!!!"
    mt "!!!"
    mt "Нужно быстрее уходить отсюда!"
    mt "Вдруг он вернется! Не хочу видеть его..."
    # Моника прерывается на полуслове, т.к. в ванную комнату заходит клиент Эбби, Брайан
    mt "!!!"
    mt "!!!!"
    brian "Ох ни хрена себе, какая у меня сегодня девка!"
    brian "Крошка Эбби не обманула, сказав, что мне понравится!"
    mt "О, нет! Это и есть клиент Эбби?!"
    brian "Познакомимся или сразу возьмешься за работу, а? Хе-хе!"
    # Моника растерянно
    m "Я..."
    m "Я [monica_hotel_name]..."
    brian "Зови меня Брайан."
    brian "Покажешь, что ты там прячешь под своим полотенцем?"
    m "Н-нет!"
    m "Сначала душ!"
    brian "Какая стеснительная малышка. Хе-хе-хе!"
    brian "Сегодня у Брайана будет отличный секс с новой телкой!"
    m "!!!"
    m "Я подожду тебя в коридоре!"
    # Моника выбегает
    # затемнение, коридор возле душа
    # Моника стоит у стены, придерживая полотенце
    mt "Что-то я все меньше уверена в своей адекватности..."
    mt "В тот момент, когда приняла предложение гребанной Эбби..."
    mt "Зачем я согласилась на это?!"
    mt "Что мне сейчас..."
    neighbor2 "Ага!"
    neighbor2 "Попалась, проститутка!"
    # сосед появляется неожиданно, Моника пугается
    m "!!!"
    m "!!!!"
    m "!!!!!"
    m "Напугал меня!"
    m "Идиот!"
    neighbor2 "Думала, так легко от меня избавишься?!"
    m "Чего тебе нужно от меня?!"
    neighbor2 "Покажешь?"
    m "Что тебе показать?"
    neighbor2 "Свои сиськи."
    m "НЕТ!"
    # он зло на нее смотрит
    neighbor2 "Какая-то проститутка строит из себя леди!"
    mt "Я и есть Леди!"
    mt "Знал бы этот недоумок, кто перед ним стоит!"
    mt "!!!"
    neighbor2 "Только поглядите на нее!"
    neighbor2 "Кто там в душе сейчас? А?"
    neighbor2 "Очередной твой хмырь?"
    m "Сам ты хмырь!"
    neighbor2 "Собралась трахаться с ним?"
    m "Тебя это не касается! Иди, куда шел!"
    neighbor2 "Невозможно больше жить в таких условиях!"
    neighbor2 "Устроили бордель!"
    neighbor2 "Спят с незнакомыми мужиками за деньги!"
    mt "Все! Он меня достал!"
    m "Ты!"
    m "Импотент гребаный!"
    m "Тащи свою задницу подальше отсюда!"
    m "Пока я сама не нажаловалась на тебя хозяину апартаментов Гарри!"
    m "Одно мое слово и он вышвырнет тебя отсюда!"
    m "Мерзкий старикашка!"
    # он на нее удивленно смотрит
    neighbor2 "Ты знаешь Гарри?"
    neighbor2 "Откуда?"
    m "Он мой друг!!!"
    # если у Моники был секс с Гарри
    #
    $ notif(_("Моника переспала с Гарри по просьбе Кэндис."))
    #
    # сосед в замешательстве
    neighbor2 "Не надо ничего говорить Гарри."
    neighbor2 "Я пойду... У меня еще столько дел, а ты меня отвлекаешь своими пустыми разговорами..."
    # уходит и про себя ворчит, не смотря на Монику
    neighbor2 "Какая-то проститутка знает Гарри..."
    neighbor2 "Гарри хороший парень и не водится с такими, как она..."
    neighbor2 "С Гарри она дружит..."
    neighbor2 "Так я и поверил!.."
    mt "Какой же этот сосед отвратительный тип!"
    mt "ААААА!!!"
    mt "Ненавижу!!!"
    mt "!!!"
    # из ванной комнаты выходит клиент
    brian "Малышка! Я готов!"
    m "Наконец-то!"
    brian "Тебе так не терпится? Хе-хе!"
    brian "Пошли скорее!" # хлопает Монику по попе
    m "!!!"
    # затемнение
    # смена кадра, комната Эбби
    # заходит Моника, следом клиент
    # он тянет ее за руку к себе
    brian "Иди сюда, малышка!"
    # начинает лапать за попу, грудь
    brian "Сейчас я с тобой буду делать все, что захочу!"
    brian "Какая ты сексуальная! Мммм!"
    # лезет рукой под полотенце на попе
    brian "Такая аппетитная! Идем скорее на кровать!"
    mt "Боже, как все это мерзко и грязно!"
    mt "Я вижу его впервые в своей жизни и даже не запомнила его имени!"
    mt "А он меня уже всю облапал своими ручищами!"
    mt "Грязный никчемный людишка!"
    mt "!!!"
    # коррапшн
    menu:
        "Терпеть клиента Эбби.":
            $ monicaAbbyNoEscortClient3 = day # Моника согласилась на секс с клиентом Эбби, не стала выгонять его
            pass
        "Выгнать его!":
            mt "Я, Моника Бакфетт!"
            mt "Леди из высшего общества и владлица многомиллионного бизнеса!"
            mt "Я мечта люього мужчины этого города и даже страны!"
            mt "И я не позволю какому-то грязному отребью прикасаться ко мне!"
            # Моника его отталкивает
            m "Хватит!"
            m "Убери свои руки!"
            brian "Эй, малышка! Ты чего?!"
            m "Ничего! Я не буду работать!"
            brian "В смысле?! Ты прикалываешься?!"
            m "Уходи!"
            brian "Но как же?.. Ведь Эбби..."
            m "Мне наплевать, что тебе пообещала Эбби!"
            m "Я не буду работать!"
            m "Пошел вон отсюда!!!"
            brian "Дура!"
            return
    # клиент продолжает лапать Монику и ведет ее к кровати
    mt "Мне нужно успокоиться!"
    mt "Глубокий вдох - выдох..."
    mt "Скоро, совсем скоро, этот кошмарный сон закончится!"
    mt "Если я все сделаю правильно, то совсем скоро Я буду зарабатывать деньги на том..."
    mt "Что эти проститутки будут обслуживать разных козлов!"
    mt "И буду штрафовать их! Всех! Особенно, Эбби!"
    mt "!!!"
    # он валит ее на кровать и срывает полотенце
    brian "Ну что, малышка! С чего начнем, а?"
    # Моника молча зло на него смотрит
    m "!!!"
    brian "Скажи мне для начала, как ты хочешь мой член!"
    # Моника продолжает зло молчать
    mt "Ни за что!"
    mt "Озабоченное грязное животное!"
    mt "!!!"
    brian "Говори! Я хочу услышать это!"
    brian "Хочешь его? Посмотри!"
    # достает свой стояк
    brian "Смотри, какой он огромный!"
    brian "Тебе ведь не терпится ощутить его внутри, да?"
    # Моника зло на него смотрит
    mt "Никто и никогда не слышал от Моники Бакфетт эти слова!"
    mt "И не услышит!!!"
    mt "!!!"
    brian "Вижу по глазам, что не терпится! Хе-хе!"
    brian "Все девки, как только видят его, готовы сразу раздвинуть ноги!"
    brian "И ты тоже хочешь!"
    mt "Фу! Нет!"
    mt "Мразь!"
    brian "Сейчас я удовлетворю тебя, малышка!"
    brian "Я буду трахать тебя, как никто и никогда, да!"
    brian "Раком!"
    m "Что?!"
    brian "Повернулась ко мне задом и встала раком! Быстро!"
    mt "!!!"
    # коррапшн
    menu:
        "Сделать, как говорит клиент.":
            pass
        "Выгнать его!":
            mt "Я, Моника Бакфетт!"
            mt "Леди из высшего общества и владлица многомиллионного бизнеса!"
            mt "Я мечта люього мужчины этого города и даже страны!"
            mt "И я не позволю какому-то грязному отребью прикасаться ко мне!"
            # Моника его отталкивает
            m "Хватит!"
            m "Убери свои руки!"
            brian "Эй, малышка! Ты чего?!"
            m "Ничего! Я не буду работать!"
            brian "В смысле?! Ты прикалываешься?!"
            m "Уходи!"
            brian "Но как же?.. Ведь Эбби..."
            m "Мне наплевать, что тебе пообещала Эбби!"
            m "Я не буду работать!"
            m "Пошел вон отсюда!!!"
            brian "Дура!"
            return
    # Моника недовольно
    mt "Грубый, неотесанный мужлан!"
    mt "Теперь я понимаю, почему гребаная Эбби не хочет с ним сама работать!"
    mt "Подсунула мне этого идиота! Сучка Эбби!"
    mt "!!!"
    mt "Так, Моника, если уж ты решилась на это..."
    mt "То нужно быть сильной и довести это дело до конца!"
    mt "Думай о том, что скоро все это закончится..."
    mt "А в твоем кармане станет больше денег!"
    # Моника встает в коленно-локтевую, лицо злое
    brian "О, дааа! Какая послушгая малышка!"
    # он лапает ее попу
    brian "Какая у тебя бархатная кожа... Мммм..."
    brian "Как ты обалденно пахнешь..."
    brian "Кайфовая шлюшка от Эбби! Хе-хе!"
    brian "Как там тебя зовут? Напомни, я забыл."
    mt "Ты не достоин произносить мое имя, никчемный неудачник!"
    mt "Даже дышать на меня не достоин, тварь!"
    brian "Имя!"
    brian "Иначе буду называть грязной шлюшкой или сучкой!"
    # шлепает ее по попе
    m "Ай! [monica_hotel_name]!"
    brian "Другое дело!"
    brian "Кайфовая шлюшка [monica_hotel_name]..."
    brian "Сейчас я войду в тебя своим огромным членом!"
    # пристраивает член к киске Моники
    brian "Ты жаждешь почувствовать его?"
    brian "Да, ты мечтаешь о нем!"
    # входит в нее
    brian "Дааа!"
    brian "О, какая бархатная киска у шлюшки [monica_hotel_name]!"
    brian "Еееее!!!"
    # начинает пялить ее, жестко
    brian "Не будь ты шлюшкой, я всегда бы тебя трахал!"
    brian "Дааа!"
    brian "Теперь я твой постоянный клиент!"
    brian "Буду покупать тебя и трахать!"
    brian "Трахать-трахать!"
    brian "Аааа!!!"
    # хватает ее за волосы на затылке (как у товарища ICSTOR'a)
    # продолжает пялить и держать за волосы
    m "Что ты делаешь?!"
    m "Мне больно!!!"
    brian "Аааа!!!"
    brian "Кааайф!"
    brian "Поверещи еще, шлюшка [monica_hotel_name]! Меня это заводит еще больше!"
    m "Хватит! Ааай!!!"
    brian "ДАА!!!"
    brian "Чертовски охренительно!!!"
    mt "Грязная скотина!"
    mt "Чертов садист!"
    mt "Ублюдок!!!"
    mt "!!!"
    # внезапно в дверь раздается громкий стук
    mt "!!!!"
    mt "!!!!!"
    neighbor2 "Развели тут бордель!"
    neighbor2 "Устроили проститутошную!"
    neighbor2 "Хватит так скрипеть кроватью!"
    neighbor2 "На весь этаж вас слышно, бесстыдники!"
    m "Чеееерт!!!"
    m "Пошел на хрен отсюда! Трахаюсь, с кем хочу!"
    neighbor2 "Бесстыдница!!!"
    # стук замолкает
    mt "Старый извращенец!!!"
    mt "!!!"
    # он резко выходит из нее и, продолжая держать за волосы, подставляет к ее губам свой член
    brian "Оближи его! Быстро!"
    mt "Дьявол!"
    mt "Он толко что был внутри моей... Внутри меня!"
    mt "Я должна теперь это все слизать?!"
    m "Но!.."
    # он водит членом по лицу Моники
    mt "Фууу!"
    brian "Бери его в рот! Выполняй!"
    menu:
        "Сделать, как говорит клиент.":
            pass
    # Моника открывает рот
    brian "В глаза мне смотри, шлюшка [monica_hotel_name]!"
    # Моника поднимает взгляд и с ненавистью смотрит на него
    brian "Вот тааак!"
    # он резко и глубоко вводит свой член
    # Моника давится
    m "Мммпфф!!!"
    m "Мпфхфпфф!!!"
    brian "Ееее! Каааайф!"
    brian "Давай, работай!"
    brian "Оооо, какая ты клевая!"
    brian "Дааа!"
    m "Мпфхфпфф!!!"
    brian "Еще немного!!! Ооооо!!!"
    menu:
        "Кончить в рот Моники.":
            brian "Аааа! Сейчас я кончу тебе в рот, шлюшка [monica_hotel_name]!"
            brian "Даааа!!!"
            brian "АААААА!!"
            brian "Глотай!"
            menu:
                "Проглотить.":
                    mt "Фууу!"
                    mt "Мерзость!!!"
                    mt "Меня сейчас стошнит!"
                "Выплюнуть!":
                    mt "Фууу!"
                    mt "Мерзость!!!"
            pass
        "Кончить на лицо Моники.":
            brian "Аааа! Хочу обкончать твое лицо, шлюшка [monica_hotel_name]!"
            brian "Даааа!!!"
            brian "АААААА!!"
            pass
        "Кончить на грудь Моники.":
            brian "Аааа! Сейчас я кончу тебе на сиськи, шлюшка [monica_hotel_name]!"
            brian "Даааа!!!"
            brian "АААААА!!"
            pass
    # он довольно отстраняется от нее, Моника злая
    mt "Сволочь!!!"
    mt "!!!"
    brian "Повторим, малышка?"
    brian "Хочу еще раз войти в твою киску."
    m "Нет!!!"
    m "Твое время вышло!!!"
    m "А благотворительностью я не занимаюсь!!!"
    m "Деньги на стол и иди отсюда!"
    brian "Хе-хе! Какая ты строптивая, шлюшка [monica_hotel_name]..."
    brian "Мне это нравится!"
    brian "Я к тебе вернусь совсем скоро. Хе-хе!"
    # затемнение, шаги, дверь
    # Моника стоит посередине комнаты, одетая
    mt "Поверить не могу, что я сделала это!"
    mt "Терпеть такое унижение ради заработка!.."
    mt "Разве эта цель оправдывает средства?"
    mt "Это было омерзительно!!!"
    mt "Гадко!!!"
    mt "Тошнотворно!!!"
    mt "!!!"
    # Моника смотрит на стол, на котором лежат деньги
    mt "Хмм..."
    mt "Интересно, сколько этот неудачник-садист оставил денег?"
    # подходит к тумбочке
    mt "150 долларов?!"
    mt "Всего?! За то, что мне пришлось вытерпеть?!"
    mt "Жадный ублюдок!!!"
    mt "Урод! Скотина!"
    mt "Ненавижу, тварь!"
    mt "!!!"
    mt "И мне еще треть отдавать гребаной Эбби?!"
    mt "..."
    # бичность
    menu:
        "Оставить $ 50 на столе и уйти.":
            mt "Пусть эта никчемная проститутка Эбби подавится своими $ 50!"
            mt "Придет время и я отомщу ей за это!"
            mt "Будет обслуживать самых грязных извращенцев за копейки!!!"
            mt "!!!"
            # оставляет 50 баксов, себе забирает 100
            # затемнение
            pass
        "Забрать все деньги и уйти.":
            $ monicaAbbyNoEscortClient4 = day # Моника не оставила Эбби процент, забрала все деньги
            mt "Пошла она к черту!"
            mt "Я заработала эти деньги!"
            mt "Они все мои, до последнего цента!"
            # забирает все деньги
            # затемнение
            pass
    return

# мысли Моники после встречи с клиентом Эбби, если забрала все деньги
label ep22_4_dialogues5_escort_5:
	# не рендерить!!
    mt "Я считаю, что поступила правильно, забрав все деньги!"
    mt "Мне пришлось терпеть этого мерзкого клиента!"
    mt "И я не обязана делиться ни с кем этим заработком!"
    mt "Я придумаю, что сказать гребаной Эбби!"
    mt "Пошла она!"
    return

# мысли Моники после встречи с клиентом Эбби, если оставила треть денег Эбби
label ep22_4_dialogues5_escort_5a:
	# не рендерить!!
    mt "Черт! Может, нужно было забрать все деньги?"
    mt "Наврала бы гребаной Эбби, что клиент не заплатил..."
    mt "..."
    mt "Нет, лучше так не рисковать. Эта Эбби не так проста, как может показаться."
    mt "Мне нужно втереться к ней в доверие."
    mt "Придет время и я припомню ей этого мерзкого клиента!"
    return

# мысли Моники после встречи с клиентом Эбби, если выгнала его и не стала с ним работать
label ep22_4_dialogues5_escort_6:
	# не рендерить!!
    mt "Это было омерзительно!!!"
    mt "Гадко!!!"
    mt "Ненавижу, тварь!"
    mt "Какого черта эта Эбби подсунула мне этого придурка?!"
    mt "!!!"
    return
