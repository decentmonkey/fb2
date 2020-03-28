default monicaMelanieVictoriaPunishment1 = False  # Моника согласилась выслушать план Мелани
default monicaMelanieVictoriaPunishment2 = False  # Мелани согласилась на откровенную фотосессию
default monicaMelanieVictoriaPunishment3 = False  # Мелани согласилась на секс с Алексом на камеру



# после того, как был паблик ивент в новом ресторане
# Моника приходит на работу в офис
# кабинет Моники
label ep212_dialogues6_melanie_punishment_1:
    # Моника сидит за своим столом, Юлия работает за своим
    img 22009
    mt "В этом отделе собрали самых никчемных сотрудников."
    mt "Они целыми днями сидят, зарывшись в своих бумажках."
    img 20335
    mt "И думают, что их отчеты кому-то здесь нужны."
    mt "Неудачники. Бесполезные людишки..."
    # смотрит на Юлию
    img 22008
    mt "А эта Юлия вообще готова до поздней ночи сидеть и делать никому ненужную работу."
    mt "От нее больше пользы было, когда она работала гувернанткой..."
    # открывается дверь и в ее кабинет заходит Мелани, встает перед Моникой
    img 15409
    w
    img 17256
    melanie "Здравствуйте, Миссис Бакфетт."
    # Моника заметно пугается, вскакивает со стула
    img 172557
    w
    img 15414
    w
    img 15421
    mt "Мелани?!"
    mt "Зачем она снова ко мне пришла? Какое-то чертово дежа-вю!"
    img 15422
    mt "Неужели снова эта мерзкой Виктории что-то нужно?!"
    mt "?!?!?!"
    # Юлия с интересом наблюдает за поведением Моники
    img 15419
    julia "???"
    img 15423
    mt "!!!"
    # Моника бросает взгляд на Юлию, потом делает покер-фейс, садится обратно на свой стул и обращается к Мелани
    img 15424
    m "Мелани, ты вернулась?"
    m "Где ты пропадала столько времени?"
    # Мелани невозмутимо отвечает
    img 15410
    melanie "Я брала несколько выходных дней у Бифа..."
    m "Надеюсь, ты пришла не для того, чтобы пригласить меня на девичник?"
    img 15412
    melanie "Как раз об этом я и хотела с Вами поговорить, Миссис Бакфетт..."
    melanie "..."
    # Моника смотрит на Мелани и думает
    img 20270
    mt "Чтобы я еще раз пошла на встречу с этой сучкой Викторией?!"
    mt "Ни за что!!!"
    img 20808
    mt "Если Мелани согласна на еще один такой девичник..."
    mt "То пусть развлекает сама эту мелкую дрянь!"
    mt "!!!"
    img 17258
    m "Да, Мелани, я слушаю..."
    # Юлия все это время с подозрением смотрит на Монику
    # Мелани поворачивается, смотрит на Юлию
    img 17259
    melanie "..."
    # потом снова на Монику
    img 17260
    # Моника тоже обращает внимание, что Юлия греет уши
    img 17261
    mt "..."

    # если есть отношения с Юлией и Моника уже сказала ей, что та ей нравится
    $ notif(_("У Моники с Юлией отношения"))
    img 17261
    m "Юлия, мне нужно обсудить с Мелани важный рабочий момент."
    # Юлия бросает на Мелани ревнивый взгляд
    img 17262
    julia "!!!"
    img 17263
    m "..."
    img 20800
    julia "Я... Мне выйти, Миссис Бакфетт? "
    img 22288
    m "Да, выйди ненадолго."
    # Юлия недовольная выходит из кабинета
    img 17266

    # если нет отношений с Юлией
    img 20810
    m "Юлия!"
    m "Я смотрю, наш разговор с Мелани тебя интересует больше, чем работа?!"
    img 17264
    julia "Н-нет, Миссис Бакфетт..."
    julia "Извините..."
    img 20811
    m "Выйди из кабинета!"
    img 17265
    julia "Д-да, конечно."
    img 20798
    m "Быстро!"
    # Юлия недовольная выходит из кабинета
    img 17266

    # Моника, как только Юлия выходит из кабинета, вскакивает со своего стула
    img 17267
    m "Мелани!"
    m "Больше никаких встреч с этой сучкой Викторией!!!"
    m "Я даже слышать об этом ничего не хочу!"
    img 17268
    m "Какая-то выскочка решила поиграть со мной, Моникой Бакфетт, в свои извращенские игры!!!"
    m "И думает, что ей это просто так сойдет с рук!!!"
    # Мелани спокойно смотрит на Монику
    img 15418
    melanie "Именно это я и хотела обсудить с Вами, Миссис Бакфетт..."
    # Моника смотрит на нее с возмущением
    img 17269
    m "!!!"
    menu:
        "Я тебя слушаю, Мелани.":
            $ monicaMelanieVictoriaPunishment1 = True # Моника согласилась выслушать план Мелани
            pass
        "Я больше ни слова не хочу слышать об этой стерве!!! (пропуск событий с Мелани)":
            # Сделать из 2-х артов, не более
            img 15424
            m "Мелани! Я больше ни слова не хочу слышать об этой стерве!"
            m "И ничего не собираюсь обсуждать!"
            img 15425
            melanie "Вы уверены, Миссис Бакфетт?"
            melanie "Это ведь в Ваших интересах..."
            # Моника перебивает Мелани
            img 17270
            m "Я это уже слышала от тебя, Мелани!"
            m "Я больше не хочу ничего обсуждать!!!"
            img 15420
            melanie "Хорошо, Миссис Бакфетт. Я Вас услышала..."
            melanie "До свидания, Миссис Бакфетт."
            img 15427
            melanie_t "Миссис Бакфетт, конечно, не самая умная женщина..."
            melanie_t "И в такие моменты я в этом убеждаюсь лишний раз..."
            # Мелани выходит из кабинета
            return
    # Моника садится на свой стул
    img 17271
    m "Я тебя слушаю, Мелани."
    img 17272
    melanie "Миссис Бакфетт, я согласна с Вами."
    melanie "Просто так нельзя оставлять то, что Виктория сделала в тот вечер."
    img 15412
    melanie "Я рассчитываю на Ваше содействие в том, чтобы поставить ее на место."
    melanie "И лишить ее возможности манипулировать нами."
    img 20905
    m "Эту стерву уже давно следовало бы поставить на место!"
    m "!!!"
    m "Вопрос в том, как это сделать?!"
    img 17273
    melanie "Дело в том, что я навела кое-какие справки..."
    img 20362
    mt "Хм... Интересно..."
    mt "Что бы там ни было, я сделаю все, чтобы отомстить этой мелкой сучке!"
    img 17274
    melanie "Я задействовала свои связи..."
    melanie "И узнала, что у одного фотографа есть знакомый папарацци..."
    melanie "Он одно время интересовался Викторией и у него есть фото, компрометирующее ее."
    # Моника смотрит на нее недоверчиво
    img 17258
    m "И что это за фото?"
    melanie "На этой фотографии доказательство того, что Виктория изменяет Дику."
    # Моника смотрит на нее удивленно
    img 15413
    m "?!?!?!"
    img 17275
    melanie "Да. Она сделала это прямо в его кабинете на рабочем столе."
    melanie "Я пообщалась с фотографом и попросила достать эту фотографию..."
    img 20247
    m "И?"
    m "Это фото у тебя?"
    img 17276
    melanie "В том и дело, что нет."
    melanie "Он не готов просто так отдавать эту фотографию и выдвинул определенное условие..."
    img 17277
    m "Какое условие? Что ему нужно? Деньги?"
    m "Мелани, ты же понимаешь, что нам просто необходимо достать это фото?!"
    m "Заплати ему!"
    img 17278
    melanie "Понимаю, Миссис Бакфетт."
    melanie "Его условие следующее: взамен фото я позволю ему снять меня на камеру."
    melanie "Он уже давно вьется вокруг меня..."
    img 17279
    melanie "Неоднократно просил эксклюзивную фотосессию, но я ему всегда отказывала."
    melanie "Поэтому я не удивлена, что он выдвинул такое условие."
    img 17280
    m "Ты собираешься раздеться?"
    melanie "Ни в коем случае. Он бы хотел этого, но будет достаточно взять более сексуальный ракурс..."
    img 20269
    mt "Всего лишь очередная фотосессия для Мелани."
    mt "Подумаешь..."
    mt "Не вижу здесь ничего сложного для нее."
    mt "Только..."
    img 17281
    m "Мелани, а ты уверена, что у этого фотографа действительно есть это фото?"
    m "А если он нас обманет?"
    img 17256
    melanie "Я не думаю, Миссис Бакфетт."
    melanie "Он достаточно известен в индустрии моды и ему ни к чему ссорится со мной..."
    melanie "Или с Вами."
    img 20372
    m "Когда назначена встреча с ним? И где?"
    img 15412
    melanie "Сегодня вечером, Миссис Бакфетт. У меня дома."
    img 17282
    m "Договорились, Мелани."
    melanie "До встречи, Миссис Бакфетт."
    # Мелани уходит
    img 15427
    mt "Надеюсь, что никаких проблем этот никчемный фотограф не доставит."
    mt "В конце концов, давно пора поставить сучку Викторию на место!"
    mt "Ненавижу эту тварь!"
    $ log1 = _("Пойти домой к Мелани вечером")
    return

# Моника в конце рабочего дня
# мысли
label ep212_dialogues6_melanie_punishment_2:
    # не рендерить!!
    mt "Я, конечно, могу не ехать к Мелани..."
    mt "Она и без меня может провести встречу с этим никчемным фотографом..."
    mt "Но я должна проконтролировать, что все пройдет как нужно..."
    mt "И у нас будет компромат на сучку Викторию!"
    mt "Не могу дождаться этого момента!"
    mt "!!!"
    return

# Моника пытается пойти к Мелани в любом наряде, кроме одежды шлюхи
# мысли
label ep212_dialogues6_melanie_punishment_3:
    # не рендерить!!
    mt "В прошлый раз я была у Мелани в костюме шлюхи. Сегодня тоже нужно надеть его."
    return

# квартира Мелани
label ep212_dialogues6_melanie_punishment_4:
    # Моника заходит в квартиру Мелани, садится на диван (или стул)
    # Мелани в красном пеньюаре
    # Моника переживает
    img 17283
    w
    img 17284
    m "Мелани, этот твой фотограф еще не пришел?"
    img 17285
    melanie "Нет, Миссис Бакфетт. Он должен подойти с минуты на минуту."
    img 17286
    m "Мелани..."
    m "..."
    m "А вдруг Виктория узнает о том, что у нас есть на нее компромат..."
    m "Еще до того, как мы покажем это фото Дику?"
    # Мелани абсолютно спокойна
    img 17287
    melanie "Миссис Бакфетт, я абсолютно уверена в этом фотографе."
    melanie "У него не хватит мозгов, чтобы создать такую интригу."
    melanie "Я уверена, что наш план сработает."
    img 17288
    melanie "И мы с Вами, наконец-то, избавимся от нашей 'милой подружки'..."
    melanie "Меня тошнит от того, что я должна целовать ее при встрече."
    melanie "Я больше никогда не стану делать этого!"
    img 15531
    m "Не могу дождать этого момента."
    # стук в дверь, Мелани идет открывать дверь
    # заходит Алекс, Викторию пока не видно
    # смотрит на Мелани с довольной улыбкой
    img 17289
    w
    img 17290
    alex_photograph "Привет, Мелани!"
    melanie "Здравствуй, Алекс."
    img 17291
    m "Алекс?!" # удивленно
    # Алекс переводит взгляд на Монику и удивленно
    img 17292
    alex_photograph "Миссис Бакфетт?!"
    alex_photograph "Здравствуйте, не ожидал Вас здесь увидеть..."
    alex_photograph "Приятно удивлен..."
    # Моника подозрительно смотрит на Алекса
    img 17293
    mt "Хмм... Мелани не говорила, что это будет Алекс..."
    mt "Она действительно уверена, что этому фотографу-извращенцу можно доверять?.."
    mt "???"
    # Алекс делает шаг в квартиру Мелани и за ним заходит Виктория с самодовольным видом
    img 17294
    victoria "Привет, подружки."
    # Моника вскакивает со стула, Мелани в шоке
    img 17295
    melanie "!!!"
    img 17296
    m "!?!?!?!"
    img 17297
    victoria "Я так рада нашей встрече."
    victoria "Я тут подумала, что мы давно не встречались с вами..."
    victoria "И я решила сделать вам сюрприз."
    # подружки в ступоре, Виктория ехидно смотрит на них, Алекс пялится на грудь Мелани
    img 17298
    victoria "Удивлены?"
    victoria "Не знали, что мы с Алексом знакомы?"
    img 17299
    melanie "..."
    img 17300
    m "..."
    
    victoria "Мне кажется или мои подружки не рады видеть меня?"
    # Моника с Мелани переглядываются
    mt "Как!"
    mt "Такое!"
    mt "Могло!"
    mt "Случиться?!"
    mt "!?!?!?!"
    mt "Мелани!!!"
    mt "Алекс!!!" # переводит вгляд на Алекса и злобно смотрит на него
    melanie_t "Эта сучка в курсе наших планов!"
    melanie_t "!!!"
    melanie_t "Алекс!!!" # тоже смотрит на Алекса, потом переводит взгляд на Викторию
    melanie "..."
    melanie "Конечно, мы рады нашей встрече... Подружка..."
    # Виктория смотрит на портрет Мелани, который она разрисовывала на девичнике, помада стерта
    victoria "???"
    # потом снова смотрит на Мелани
    victoria "..."
    victoria "Мелани..."
    melanie "..."
    victoria "Ты хорошая подружка?"
    melanie "Да..."
    victoria "Ты уверена в том, что ты хорошая подружка?"
    melanie "..."
    melanie "Уверена..."
    victoria "Что ты должна сделать, если ты и правда рада нашей встрече?"
    # выбор у Мелани, Моника стоит позади и бросает гневные взгляды на Алекса
    m "!!!"
    melanie "..."
    menu:
        "Подойти к Виктории и поцеловать ее":
            pass
    # Мелани целует Викторию в щечку, Виктория хихикает
    # потом Виктория проходит и по-хозяйски садится на диван, все остальные тоже садятся
    m "Алекс!"
    m "Я не знала, что ты знаком с нашей подружкой Викторией..."
    alex_photograph "Да, Миссис Бакфетт..."
    # Виктория перебивает его
    victoria "Да, мы знакомы..."
    victoria "Алекс рассказал мне про эксклюзивную фотосессию."
    victoria "Он также сокрушался о том, что Мелани соглашается только на приличные кадры."
    victoria "И я предложила ему свою помощь."
    # Моника испепеляет Алекса взглядом, Мелани вопросительно смотрит на Алекса
    m "!!!"
    melanie "???"
    alex_photograph "Мисс Виктория сказала, что ..."
    # Виктория снова перебивает его
    victoria "Я сказала Алексу, что моя подружка Мелани не откажет мне..."
    victoria "Если я попрошу ее сделать эту фотосессию несколько откровенной."
    melanie "Откровенной?"
    victoria "Именно."
    # Виктория обращает внимание на Монику
    victoria "Может быть, Миссис Бакфетт тоже захочет поучаствовать?"
    mt "НЕТ!"
    mt "!!!"
    victoria "..."
    victoria "Но маловероятно, чтобы сама Моника Бакфетт снизошла до такого... Возможно, в следующий раз..."
    victoria "Но она тоже моя подружка, поэтому будет не против этой фотосессии."
    victoria "Ты же не против, подружка Моника?"
    # взгляд на Мелани
    mt "По-моему, она поняла, что этот план придумала Мелани..."
    mt "И решила наказать ее..."
    melanie "..."
    # потом снова смотрит на Викторию
    mt "Эта мелкая дрянь узнала обо всем! От Алекса!"
    mt "!!!"
    mt "Я даже представить не могу, что она собирается сделать..."
    mt "..."
    mt "Мерзкая извращенка!"
    mt "!!!"
    # Моника отвечает
    menu:
        "Дать согласие на фотосессию Мелани":
            pass
    m "Я не против..."
    victoria "Хорошо."
    victoria "А что скажет подружка Мелани?"
    victoria "Она ведь не откажет МНЕ?"
    # Мелани смотрит на нее, потом на Алекса
    melanie "..."
    menu:
        "Согласиться на фотосессию":
            $ monicaMelanieVictoriaPunishment2 = True # Мелани согласилась на откровенную фотосессию
            pass
        "Отказаться (пропуск событий с Мелани)":
            # Максимум 3 арта
            melanie_t "Я больше не позволю этой мелкой сучке унижать меня."
            melanie_t "Да еще и в присутствии Алекса."
            melanie "..."
            melanie "Подружка... Я согласна удвоить еженедельные взносы в счет нашей дружбы..."
            # Ехидно
            victoria "Хорошо, подружка..."
            victoria "Так уж и быть..."
            victoria "Жду тебя как обычно..."
            # затемнение экрана
            return
    melanie_t "Значит, Алекс ей все рассказал..."
    melanie_t "Я не предполагала что они знакомы."
    melanie_t "У Алекса совсем нет мозгов, мне следовало быть более осторожной с ним..."
    melanie_t "Но с Алексом я разберусь позже."
    melanie_t "Эта сучка теперь будет мстить мне за попытку раздобыть компромат на нее."
    melanie_t "Нужно согласиться на эту фотосессию."
    melanie_t "Пусть Виктория думает, что я раскаиваюсь..."
    melanie_t "А снимки я позже заберу у этого безмозглого Алекса."
    melanie "..."
    melanie "Я согласна."
    victoria "Я знала, что ты не сможешь отказать мне, подружка Мелани."
    victoria "Так..."
    # смотрит на наряд Мелани оценивающе
    victoria "Эта одежда вполне сойдет для фотосессии..."
    victoria "Ну что? Приступим?"
    return


# квартира Мелани
# фотосессия
label ep212_dialogues6_melanie_punishment_5:
    # Моника наблюдает со стороны, Мелани позирует
    # Виктория комментирует и заставляет принимать максимально открытые позы и брать соотв. ракурсы
    alex_photograph "Мелани, я так рад, что ты согласилась на эту фотосессию."
    # смотрит на него холодно
    melanie "..."
    alex_photograph "Ну что, начнем."

    # поза 1
    alex_photograph "Отличная поза, Мелани."
    melanie "Алекс, старайся не брать крупным планом..."
    victoria "Нет-нет. Так не пойдет."
    victoria "Нужно что-то более раскрепощенное, подружка Мелани."
    melanie_t "!!!"

    # поза 2
    victoria "Подружка Мелани сейчас перестанет прикрываться."
    victoria "Не забывай, что у нас откровенная фотосессия."
    alex_photograph "О, отличный ракурс! Это будут шедевральные кадры!"
    melanie_t "Алекс так радуется..."
    melanie_t "Как-будто я позволю ему оставить эти кадры себе..."

    # поза 3
    victoria "Алекс, возьми еще с этого ракурса."
    melanie "Алекс, думаю, что это перебор."
    alex_photograph "Что ты, Мелани! В кадре все смотрится прекрасно!"
    melanie_t "!!!"

    # поза 4
    victoria "Подружка Мелани, расставь ноги пошире."
    victoria "Это будет смотреться более изысканно."
    melanie "Алекс, ты помнишь, что я тебе говорила про кадры крупным планом?"
    alex_photograph "Да, Мелани, конечно."
    alex_photograph "Не беспокойся."
    melanie_t "Дрянь!"

    # поза 5
    victoria "Думаю, если подружка Мелани снимет свои трусики..."
    victoria "Кадры станут намного интереснее."
    victoria "Что скажешь, Алекс?"
    alex_photograph "О, да! Это отличная идея, Мисс Виктория!"
    melanie "Алекс, недостаточно того, что у меня грудь практически не прикрыта?"
    alex_photograph "Мелани,  не переживай."
    alex_photograph "Я буду брать такие ракурсы, что ничего лишнего не будет видно."
    melanie_t "Он думает, что меня также легко обмануть, как Миссис Бакфетт..."
    # Виктория пристально смотрит на нее
    victoria "Ну? Мы ждем, подружка..."
    melanie_t "!!!"
    # Мелани снимает трусики и остается в одном прозрачном пеньюаре

    # поза 6
    victoria "По-моему, отличная поза."
    victoria "Не останавливайся, Алекс. Продолжай работать."
    melanie "Алекс, мы делаем кадры для порножурнала?"
    alex_photograph "Нет, конечно, Мелани!"
    melanie "Тогда не нужно делать кадры в такой позе."
    melanie_t "!!!"

    # поза 7
    victoria "Алекс, возьми еще с этого ракурса крупным планом."
    victoria "Получится отличный кадр."
    melanie_t "Сучка!"

    # поза 8
    melanie "Алекс, думаю, что пора заканчивать."
    alex_photograph "Еще несколько кадров, Мелани!"
    alex_photograph "Ты не представляешь, какие шикарные кадры получаются!"
    melanie_t "Тебе осталось недолго радоваться этим кадрам..."

    # поза 9
    victoria "Нужно сделать снимки еще в этой позе."
    victoria "И с этого ракурса."
    melanie_t "!!!"
    alex_photograph "Отличная идея, Мисс Виктория!"

    # завершения фотосессии
    # Алекс доволен
    alex_photograph "Это была отличная работа, Мелани!"
    alex_photograph "Мисс Виктория, спасибо Вам за помощь!"
    alex_photograph "Вы подсказали много интересных ракурсов."
    # Виктория самодовольно смотрит на Мелани
    victoria "Всегда рада помочь своей подружке."
    # Мелани с покерфейсом
    melanie_t "Надеюсь, на этом все?"
    melanie_t "Не хочу больше видеть их в своем доме."
    melanie_t "Виктория выглядит вполне довольной. Получила, что хотела. Сучка!"
    melanie_t "Завтра я заберу эти кадры у Алекса."
    melanie_t "Я не могу позволить, чтобы такая фотосессия хранилась у кого бы то ни было."
    melanie_t "Существует шанс того, что она просочится в мир."
    # Моника смотрит на Мелани
    mt "Какой кошмар!"
    mt "Не представляю, если бы эта дрянь заставила меня делать подобные кадры!"
    mt "!!!"
    melanie "Алекс, пожалуйста, оставь эти кадры пока при себе."
    melanie "Завтра мне надо будет поговорить с тобой..."
    return

# квартира Мелани
label ep212_dialogues6_melanie_punishment_6:
    # после фотосессии все сидят снова на своих местах
    # Моника с Мелани недовольны
    mt "Скорее бы оказаться подальше от этой дряни!"
    mt "Вместе с этим фотографом-извращенцем!"
    mt "Придурок!!!"
    mt "!!!"
    # Виктория обращается к Алексу, тот сидит довольный и пялится на Мелани
    victoria "Ну что, Алекс, ты доволен?"
    alex_photograph "Конечно, Виктория! Я так рад что тебе удалось убедить Мелани!"
    alex_photograph "Не знал что вы с ней такие близкие подруги!"
    victoria "Алекс, что скажешь насчет моего портфолио?"
    victoria "Мне кажется, что тебе ничего не стоит помочь мне в его продвижении."
    victoria "Всего несколько рекомендаций нужным людям."
    victoria "Уверена, для тебя это не составит никакого труда."
    # Алекс смотрит на Викторию, потом снова на Мелани
    alex_photograph "Виктория, конечно, для меня это не трудно..."
    alex_photograph "Но я привыке помогать в продвижении девушкам с такими данными, как у Мелани."
    alex_photograph "С девушками с обычной внешностью я не работаю."
    # Виктория зло смотрит на Мелани
    victoria "!!!"
    # Мелани про себя злорадствует и смотрит на нее высокомерно
    melanie "..."
    # Виктория снова обращается к Алексу
    victoria "Алекс, а если я расскажу тебе ее маленький секрет?"
    alex_photograph "???"
    # Мелани с Моникой в шоке
    melanie_t "Что эта сучка может рассказать ему?"
    melanie_t "Она собирается рассказать про Маркуса?"
    # Алекс заинтересованно смотрит на Викторию
    victoria "Так как мы с Мелани очень хорошие подружки..."
    victoria "Она делится со мной всеми своими секретами."
    victoria "И она говорила мне, что хочет переспать с тобой, Алекс."
    melanie "Что?"
    melanie "Это не так, Алекс."
    melanie "Я..."
    # Виктория перебивает ее и снова обращается к Алексу
    victoria "Что, если Мелани позволит тебе переспать с ней?"
    melanie "Нет. Это исключено."

    # Виктория ехидно
    victoria "Мелани, подружка, ну признайся!"
    victoria "Ты хотела, чтобы он тебе принес фото."
    victoria "А на самом деле это был просто предлог, чтобы переспать с ним?"
    melanie "!!!"
    # Алекс в шоке
    alex_photograph "Мелани... Я..."
    alex_photograph "Я и не знал, что нравлюсь тебе..."
    alex_photograph "Ты поэтому избегала меня все это время?"

    melanie_t "Что за бред несет эта дряная Виктория?!"
    melanie_t "Чего она добивается?"
    melanie_t "Фотосессии было недостаточно?"
    melanie "..."
    victoria "Ну, подружка Мелани, не стесняйся. Признайся, что хочешь этого."
    # угрожающе
    victoria "Ты ведь хорошая подружка, не правда-ли?"

    # Мелани сквозь зубы, зло
    melanie "Да..."
    victoria "Что 'да'?"
    menu:
        "Я хочу переспать с Алексом":
            pass
    melanie "Я пригласила сюда Алекса, чтобы..."
    melanie "Чтобы переспать с ним."
    melanie "..."
    # Виктория самодовольно
    victoria "Хорошая подружка."
    victoria "Ты же не будешь против, если мы с подружкой Моникой будем присутствовать при этом?"

    melanie_t "Я уничтожу эту дрянь Викторию!"
    melanie_t "Я задействую для этого все свои связи!"
    melanie_t "!!!"
    melanie "Нет, я не против."
    # Моника в шоке
    mt "О, Боже!"
    mt "Я не могу поверить, что эта сучка заставляет Мелани делать это!"
    mt "!!!"

    # Виктория хихикает и продолжает командовать
    victoria "Отлично!"
    victoria "Алекс, раз уж ты привык все снимать на камеру, то почему бы не снять то, как вы будете делать это?"
    victoria "Подружка Мелани любит, когда ее снимают на камеру."
    victoria "Даже во время секса. Да, Мелани?"
    melanie "..." # зло
    victoria "Я не слышу ответа. Ты же хочешь, чтобы я сняла вас с Алексом на камеру?"
    # Мелани в ярости
    melanie "..."
    melanie "Виктория, это не идет ни в какие рамки!!! Я..."
    victoria "Хорошая подружка хочет этого."
    victoria "Плохая подружка не будет дружить со мной..."
    melanie "!!!"
    menu:
        "Да, хочу...":
            pass
    # Мелани сквозь зубы, злобно смотрит на Алекса
    melanie "Да, хочу..."
    melanie_t "Я готова потерпеть Алекса."
    melanie_t "..."
    melanie_t "Пусть эта стерва порадуется."
    melanie_t "Потом я сотру ее в порошок!"
    melanie_t "Я найду способ!"
    melanie_t "!!!"
    # Алекс думает, что Мелани и правда хочет его и радуется
    alex_photograph "Мелани, я тоже не против!"
    alex_photograph "Не знал, что ты настолько любишь камеру!"
    victoria "Подружка Мелани любит ролевые игры, поэтому это будет не просто секс..."
    alex_photograph "Ух ты! Даже так?!"
    victoria "Да, Алекс."
    victoria "Мы разыграем небольшую сцену."
    victoria "И так как ты, Алекс, будешь занят, то я, так уж и быть, сама готова снять это на свой телефон."
    victoria "Сейчас ты, подружка Мелани, на камеру скажешь, что..."
    victoria "Что, как обычно, сделаешь минет за $ 50, а сексом займешься за $ 100."
    victoria "И сделаешь это."
    victoria "А Алекс нам подыграет."
    # Моника напугана происходящим
    mt "Эта белобрысая дрянь - настоящий дъявол!"
    mt "Как она могла вообще до такого додуматься?!"
    mt "!!!"
    mt "А что, если бы я сейчас был на месте Мелани?!"
    mt "Кошмар!!!"
    mt "!!!"
    # Мелани зло смотрит на Викторию
    melanie "..."
    melanie "Подружка Виктория, может, мы сделаем это в другой раз?"
    melanie "В какой-нибудь более подходящей обстановке?"
    melanie "Да, Алекс?"
    victoria "Не стоит так стесняться, подружка Мелани."
    victoria "Просто снимем небольшое видео. Повеселимся."
    victoria "Ты же не будешь спорить и сделаешь все, что я тебе скажу?"
    victoria "Ты же хорошая подружка, Мелани?" # угрожающе
    melanie "..."
    menu:
        "Сделать как требует Виктория":
            $ monicaMelanieVictoriaPunishment3 = True # Мелани согласилась на секс с Алексом на камеру
            pass
        "Отказаться (пропуск сцены)":
            # Максимум 3 арта
            melanie_t "Я больше не позволю этой мелкой сучке унижать меня."
            melanie_t "Да еще и в присутствии Алекса."
            melanie "..."
            melanie "Подружка... Я согласна удвоить еженедельные взносы в счет нашей дружбы..."
            # Ехидно
            victoria "Хорошо, подружка..."
            victoria "Так уж и быть..."
            victoria "Жду тебя как обычно..."
            # затемнение экрана
            return
    melanie "Да, я хорошая подружка..."
    melanie "Я сделаю, как ты скажешь..."
    melanie "..."
    # переглядываются с Моникой
    mt "!!!"
    mt "!!!!!!"
    # затемнение
    # Мелани сидит в кресле, Виктория снимает все на камеру на телефоне
    # Алекс подходит к Мелани со спущенными штанами, его видно со спины
    alex_photograph "Какой у тебя прейскурант, Мелани?"
    melanie "!!!"
    victoria "???"
    # Мелани отвечает
    melanie "Как обычно, сделаю минет за 50 долларов, секс стоит 100 долларов."
    # Алек бросает ей 50 баксов
    alex_photograph "Вот твой сегодняшний заработок."
    alex_photograph "Соси!"
    # Мелани медлит
    melanie_t "Этот гребаный Алекс еще и подыгрывает ей!"
    melanie_t "Я сотру эту стерву в порошок!"
    melanie_t "Сейчас просто нужно сделать вид, что я ее слушаюсь."
    melanie_t "!!!"
    alex_photograph "Ну? Отрабатывай свои деньги!"
    # делает минет Алексу
    alex_photograph "Ооооо, Меланиииии!!!"
    alex_photograph "Ааааааа!!!"
    alex_photograph "Возьми его глубже!"
    alex_photograph "Ещеееее!!!"
    alex_photograph "Быстрее! Быстрее!!!"
    # Алекс кончает
    menu:
        "Кончить в рот Мелани.":
            alex_photograph "Дааа..."
            alex_photograph "Дааа!!!"
            alex_photograph "ДААААААА!!!"
            pass
        "Кончить на лицо Мелани.":
            alex_photograph "Дааа..."
            alex_photograph "Дааа!!!"
            alex_photograph "ДААААААА!!!"
            pass
        "Кончить на грудь Мелани.":
            alex_photograph "Дааа..."
            alex_photograph "Дааа!!!"
            alex_photograph "ДААААААА!!!"
            pass
    victoria "Видео снято!"
    victoria "Алекс, спасибо!"
    # затемнение
    return

# квартира Мелани
label ep212_dialogues6_melanie_punishment_7:
    # кадр меняется, Мелани с Моникой и Викторией одни, Алекс ушел
    # Виктория хихикает
    victoria "Подружки, мы отлично с вами повеселились сегодня."
    victoria "Теперь у меня на память есть видео."
    victoria "Оно побудет у меня. Вы же не против, подружки?"
    victoria "Хорошие подружки доверяют друг другу."
    victoria "И, ради хорошей подружки Мелани, я это видео никому не покажу..."
    victoria "Может быть, только Мистеру Дику..."
    # Мелани сидит злая, Моника в шоке
    melanie_t "Я уничтожу эту сучку Викторию!"
    mt "Она покажет ЭТО Дику?!"
    mt "?!?!?!"
    victoria "И еще, подружка Мелани..."
    victoria "Я кажется тебе запрещала стирать мой рисунок с этой фотографии?"
    melanie "..."
    victoria "Почему ты меня ослушалась?"
    victoria "Ты хочешь стать плохой подружкой?"
    # Мелани безразлично
    melanie "Нет. Я просто забыла..."
    victoria "На первый раз я тебя прощаю..."
    victoria "Но если такое повторится, я тебя накажу, подружка Мелани!"
    # она подходит с помадой к фото Мелани и подрисовывает член
    melanie "!!!"
    mt "!!!"
    victoria "Так намного лучше."
    victoria "Все, подружки, мне пора."
    victoria "Надеюсь, скоро снова увидимся."
    # Виктория уходит, Моника с Мелани вдвоем
    # Моника говорит
    m "Мелани!"
    m "Мелани, ты в порядке? Ты слышишь меня?"
    melanie "Миссис Бакфетт..."
    melanie "Я сотру стерву Викторию в порошок!"
    melanie "Я сделаю для этого абсолютно все!"
    melanie "!!!"
    return

# мысли Моники, после того как ушла от Мелани, если Мелани отказала Виктории
label ep212_dialogues6_melanie_punishment_8:
    # не рендерить!!
    mt "Судя по всему, Мелани тоже еженедельно приносит Виктории деньги..."
    mt "Ей это делать гораздо проще! У нее они есть!"
    mt "И она не спешит делиться со мной!"
    mt "!!!"
    return

# мысли Моники, после того как ушла от Мелани, если сцена была проиграна полностью
label ep212_dialogues6_melanie_punishment_9:
    # не рендерить!!
    mt "Никогда не видела Мелани такой обозленной..."
    mt "Даже после того девичника..."
    mt "Виктория мерзкая сучка!"
    mt "Ненавижу ее!"
    mt "!!!"
    return

# через несколько дней после фотосессии в наряде "Королева сердец"
# Моника заходит в свой отдел отчетов
label ep212_dialogues6_melanie_punishment_10:
    # офис полон сотрудников, несколько из них (серая мышка, близняшки и китаянки Лин) стоят в кучке возле стола
    # они что-то рассматривают на столе и обсуждают
    w1 "Ой... Какой кошмар!!!" # серая мышка
    w3 "А я и не удивлена!" # одна из близняшек
    w3 "Это еще только начало!"
    w4 "Да-да! Позже будут публиковать фотографии еще хуже! Вот увидите!" # вторая близняшка
    w7 "Тихо!" # китаянка Лин
    # они видят Монику и замолкают, все смотрят на нее
    mt "Это еще что такое?!"
    mt "Почему эти никчемные сотрудники так на меня смотрят?!"
    # подбегает подхалим
    w5 "Миссис Бакфет! Вы сегодня прекрасно выглядите!" # подхалим Джон
    w5 "Хотите чашечку горячего кофе?"
    m "Нет."
    m "Что здесь происходит?!" # сердито
    m "Почему половина офиса не на рабочих местах?!" # включаем большого босса
    # подбегает Гретта
    w6 "Миссис Бакфетт, а они сегодня целый день ничего не делают!" # Гретта
    w6 "Только сидят и сплетничают!"
    m "Так! Быстро все за работу!!!"
    m "Или я уволю вас всех сегодня же!!!"
    m "!!!"
    w5 "Не понятно, за что они деньги получают!"
    w5 "Ничего не делают!"
    w5 "Целый день сегодня сидят и какой-то неприличный журнал обсуждают!"
    # в разговор вмешивается айтишник
    w2 "Гретта, они читают наш журнал."
    w2 "В котором мы работаем."
    w5 "А? Наш?!"
    w2 "Кстати, Миссис Бакфетт..."
    w2 "Отличная фотосессия получилась!"
    w5 "Согласен на все сто."
    w5 "Это лучшее, что я видел в своей жизни, Миссис Бакфетт!"
    m "Ты о чем?"
    w5 "Вам очень идет то красное платье..."
    w2 "И корона. Вы как настоящая королева на снимках."
    # Моника сначала не понимает, о чем они, но постепенно до нее доходит
    mt "Красное платье и корона?"
    mt "???"
    mt "?!?!?!"
    mt "ЧТОООООО?!"
    # шок, злость
    # потом орет на всех
    m "Быстро все за работу!!!"
    m "!!!"
    m "Бездельники!!!"
    m "!!!!!"
    # идет в свой кабинет
    mt "Боже!"
    mt "Какой кошмар!"
    mt "Теперь все эти никчемные сотрудники видели мои фото с той ужасной фотосессии!!!"
    mt "!!!"
    mt "Это все Бифф!"
    mt "Если бы не его дурацкая смена курса журнала!"
    mt "Никто и никогда не увидел бы подобных фотографий Моники Бакфетт!"
    mt "Потому что их не было бы!!!"
    mt "!!!"
    mt "Я ненавижу этого мерзавца Биффа!"
    mt "Ненавижу!"
    mt "Убью его!"
    mt "!!!"
    mt "!!!!!!"
    return
