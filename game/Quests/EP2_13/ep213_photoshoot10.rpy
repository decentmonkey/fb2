label ep213_photoshoot10:
    # Моника стоит, прикрывая грудь
	img 24230
	w
	img 24231
    mt "Биф выгонит меня с работы, если я сорву эту фотосессию..."
    mt "Нужно сказать Алексу, чтобы не брал откровенные ракурсы."
    mt "Если это вообще возможно в ЭТОМ!"
    mt "!!!"
	
	img 24232
    m "Алекс..."
    alex_photograph "Да, Миссис Бакфетт?"
    alex_photograph "Вы готовы? Отлично выглядите!"
    m "Алекс, никаких откровенных ракурсов!"
    m "Ты понял меня?"
    alex_photograph "Да, конечно, Миссис Бакфетт."
    m "И никаких крупных планов!"
	
	img 24233
    alex_photograph "Я все сделаю, как надо, Миссис Бакфетт."
    alex_photograph "Не переживайте..."
    m "..."
    alex_photograph "Начнем?"

	# фразы Моники во время позирования для Алекса:
	
    m "Алекс, не забудь, что ты мне обещал."
    alex_photograph "Конечно, Миссис Бакфетт."

    m "Алекс, мне кажется эта поза слишком откровенная..."
    alex_photograph "Нет, Миссис Бакфетт. Это будет отличный кадр, вот увидите."

    m "Может, мне стоит немного прикрыть здесь руками?"
    biff "Миссис Бакфетт, отличная поза. Ничего не надо прикрывать!"
    m "!!!"

    campbell "Думаю, здесь получится отличный кадр..."
    biff "Согласен с Вами, Мистер Кэмпбелл."
    m "Но..."
    biff "Алекс, продолжай работу!"
    alex_photograph "Да, Мистер Биф."

    investor2 "На прошлых двух фотосессиях было мало кадров сзади."
    investor2 "Я предлагаю сделать кадры именно с такого ракурса..."
    biff "Отличная идея!"
    biff "Алекс, ты слышал? Возьми крупным планом."
    m "Алекс!"
    alex_photograph "Миссис Бакфетт, я просто делаю свою работу."
    mt "Биф мерзавец!!!"
    mt "!!!"

    philip "Хотел бы добавить свое пожелание, если позволите..."
    biff "Да, конечно!"
    philip "Мне кажется, будет очень сексуальный кадр, если Миссис Бакфетт ляжет..."
    philip "И развинет ноги..."

    mt "ЧТО?!"
    biff "Миссис Бакфетт, прошу вас. Вы слышали пожелание нашего многоуважаемого гостя."
    mt "Биф, это съемка для модного журнала, а не для..."
    # Биф подходит к Монике и зло ей шепчет
    biff "Еще одно слово, кукла безмозглая, и ты вылетишь с работы!"
    biff "Только сначала, шлюха, я отдам тебя всем этим денежным мешкам!"
    biff "Пусть делают с тобой все, чего им захочется!"
    biff "Быстро сделала, как сказал инвестор!"
    mt "!!!"
    menu:
        "Принять позу, которую хочет увидеть инвестор.":
            pass
    mt "Если я сейчас откажусь принимать эту позу, то я сорву фотосессию..."
    mt "Знал бы этот мерзавец, как мне нужны эти деньги..."
    mt "Ненавижу их всех!"
    mt "!!!"

    # Биф отходит обратно к инвесторам
    investor3 "Какие-то проблемы, Мистер Биф?"
    investor3 "Миссис Бакфетт отказывается от продолжения?"
    biff "Нет, все в порядке..."
    biff "Ей просто нужен был небольшой перерыв."
    biff "Алекс, продолжай!"

    # Моника ложится в нужную позу
    steve "Вы были правы, Мистер Филипп."
    steve "Поза очень сексуальная."
    steve "Если взять еще несколько крупных планов, то получатся отличные кадры..."

    mt "Этот никчемный неудачник Стив еще что-то советует?!"
    mt "И вообще! Какого черта он здесь делает?!"
    mt "!!!"
    m "Алекс, старайся не брать крупные планы..."
    alex_photograph "Я не делаю снимки, Миссис Бакфетт..."
    alex_photograph "Я просто подбираю лучший ракурс."
    mt "Этот фотограф-извращенец просто пялится на меня!"
    mt "!!!"

    alex_photograph "Съемка окончена!"
    biff "Отлично! Спасибо, Алекс!"
    # Моника стоит, прикрывшись, Биф обращается к инвесторам
    biff "Господа, спасибо за ваше присутствие!"
    biff "Надеюсь, вы убедились в серьезности наших намерений."
    biff "Всегда будем рады видеть вас в нашем офисе!"
    # все инвесторы встают со стульев, кроме одного
    # затемнение, звук мужских шагов
    # смена кадра
    # Моника стоит также прикрывшись, на стуле сидит один инвестор, Биф стоит рядом с ним
    investor4 "Я специально задержался, Мистер Биф..."
    investor4 "Меня впечатлила презентация Миссис Бакфетт, а также ее умение держаться перед камерой..."
    investor4 "Я вижу, что у вас достаточно серьезные намерения относительно смены курса журнала."
    investor4 "И Миссис Бакфетт это сегодня подтвердила... Почти..."
    investor4 "В связи с этим я принял решение..."
    biff "..."
    m "..."
    investor4 "Я готов инвестировать в журнал Миссис Бакфетт, но у меня есть одно условие..."
    biff "Какое условие? Мы готовы его рассмотреть!"
    investor4 "Я инвестирую в журнал, если Миссис Бакфетт сделает еще один кадр..."
    m "Какой кадр?!"
    investor4 "Широко раздвинет ноги и сдвинет свои трусики."
    investor4 "Таким образом, я буду уверен в том, что..."
    investor4 "Откровенные кадры, которыми вы аргументируете серъезность принятого вами курса..."
    investor4 "Они являются плодом регулярной работы, а не случайным явлением... #они - it"
    investor4 "Когда фотограф внезапно подловил модель."
    investor4 "Я хочу увидеть, что Миссис Бакфетт осознанно сделает это..."
    m "!!!"
    # Биф радостный, Моника в шоке
    m "Что?!"
    m "Я..."
    biff "О, Господин Инвестор, с этим нет никаких проблем!"
    biff "Конечно же, Миссис Бакфетт сделает это!"
    # поворачивается к Монике
    biff "Сделает прямо сейчас!"
    m "Биф!"
    biff "И не будет тратить время на бесполезные разговоры."
    biff "У нашего многоуважаемого Господина Инвестора каждая минута на счету!"
    biff "Время - деньги, Миссис Бакфетт!"
    mt "!!!"
    menu:
        "Согласна.": #corruption высокий!
            $ monicaBiffPhotoshootInvestor4 = True # Моника согласилась сдвинуть трусики на фотосессии
            pass
        "НЕТ!!!":
            m "Нет! Я не буду делать ЭТОГО!"
            # Биф начинает наезжать на Монику
            biff "Миссис Бакфетт!!!"
            biff "Вы сейчас же сделаете, как просит Господин Инвестор!"
            biff "Иначе!"
            biff "Вы, Миссис Бакфетт, помните, что будет!"
            m "Я не собираюсь сдвигать трусики!!!"
            m "!!!"
            # Моника уходит с фотосессии
            return
    # Моника в растерянности
    mt "У меня есть шанс сделать так, что еще один инвестор согласится на инвестицию в мой журнал!"
    mt "Но не таким же способом!"
    mt "А вдруг этот снимок станет общедоступным?!"
    mt "Что тогда, Моника?!"
    mt "?!"
    mt "Дьявол!"
    mt "Но если я сейчас откажусь..."
    mt "Где я потом смогу зарабатывать $ 5000 каждую неделю?!"
    m "..."
    m "Я..."
    m "Я сделаю это..."

# с этого момента начнется повторно, если Моника в первые раз сорвала фотосессию
    # Биф радостно
    biff "Алекс, ты готов?"
    alex_photograph "Да, Мистер Биф. Конечно."
    # хитро улыбается
    mt "Боже! Моника, как могло дойти до того, что ты сдвигаешь трусики для какого-то жалкого инвестора?!"
    mt "Да какая разница, для кого?!"
    mt "Как ты вообще могла позволить дойти до ТАКОГО?!"
    mt "?!?!?!"
    mt "Я отомщу кретину Бифу за это!"
    mt "И этому извращенцу инвестору тоже!"
    mt "Они еще пожалеют об этом!"
    mt "!!!"
    # Моника раздвигает ноги и сдвигает трусики
    # Алекс делает кадр
    alex_photograph "!!!"
    investor4 "..."
    investor4 "Спасибо, Миссис Бакфетт."
    investor4 "Можете вернуть Ваши трусики на место."
    # инвестор встает
    biff "Господин Инвестор, пройдемте в мой кабинет."
    biff "Обсудим с Вами подробности нашей сделки."
    # они уходят
    mt "Сволочи!"
    mt "Никчемные жалкие неудачники!"
    mt "!!!"
    # Алекс смортит к Монике
    alex_photograph "Миссис Бакфетт, это была Ваша лучшая фотосессия!"
    # Моника прикрывается
    m "Алекс, не смотри на меня!"
    m "Отвернись, быстро!"
    mt "Еще одни извращенец!"
    mt "!!!"
