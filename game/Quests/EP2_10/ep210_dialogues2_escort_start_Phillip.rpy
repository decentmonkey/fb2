# Моника приходит в ресторан на ужин
# ресторан отеля ЛеГранд
label ep210_dialogues2_escort_start_Phillip_1:
    # Моника заказывает еду у официантки ( ep26_dialogues4_restaurant - разговор с официанткой и заказ еды)
    # пока ждет, когда принесут ее заказ, сидит на стуле с задумчивым видом
    img 22946
    mt "Наконец-то моя прежняя жизнь постепенно возвращается..."
    mt "Я на верном пути."
    mt "Совсем недавно я могла себе позволить только ужасный кебаб..."
    mt "Или не менее ужасное пирожное..."
    img 22947
    mt "А сейчас я в ресторане, на мне красивое платье..."
    mt "Я поела такой вкусный ужин..."
    mt "Скоро Моника Бакфетт вернет себе все, что у нее отняли!"
    mt "И накажет всех, кто посмел недостойно себя вести в отношении нее..."
    # приносят ужин и тут ее мысли прерывает мужской голос
    img 22948
    philip "Миссис Бакфетт, какая неожиданная и приятная встреча!"
    # Моника поднимает взгляд, рядом с ее столиком стоит Филипп
    img 22949
    mt "О нет! Только не этот мерзкий тип!"
    mt "Что он здесь делает?!"
    # Филипп продолжает любезно улыбаться
    img 22950
    philip "Добрый вечер, Миссис Бакфетт. Позвольте вашу ручку?"
    # Филипп целует ее руку и садится за ее столик. Она вопросительно смотрит на него
    img 22951
    philip "Я впечатлен Вашей презентацией, Миссис Бакфетт."
    img 22952
    m "Спасибо, Филипп."
    mt "Что ему от меня надо?"
    img 22953
    philip "На этой презентации я увидел у Вас кое-что интересное, Мэм..."
    m "..."

    # если Моника делала ему минет в туалете
    philip "Я, конечно, не использую одну и ту же женщину дважды..."
    #
    $ notif(_("Моника делала Филиппу минет в туалете"))
    #
    philip "Но у Вас я пробовал только ротик..."
    philip "Я решил, что неплохо было бы мне засунуть член в Ваше отверстие."
    # если Моника НЕ делала ему минет в туалете
    img 22954
    m "Это не твое дело, Филипп! Мне без разницы, что ты там увидел..."
    img 22953
    philip "Как что? Вашу прекрасную попу, Миссис Бакфетт!"
    philip "И я решил, что неплохо было бы мне засунуть член в Ваше отверстие."
    #

    img 22954
    mt "!!!"
    m "Даже не мечтай, Филипп! Ты никогда не сможешь этого сделать!"
    img 22955
    philip "Я всегда могу сделать это с Вами. За деньги."
    # Моника злится, говорит возмущенно
    img 22956
    m "Ты меня считаешь проституткой?!"
    m "С чего ты взял, что меня можно купить?!"
    # Филипп, улыбаясь
    img 22957
    philip "Я знаю это."
    philip "Я куплю Вашу киску за 300 долларов."
    img 22958
    mt "!!!"
    menu:
        "Как он смеет предлагать мне подобное?!":
            # Монику бомбит
            m "Как ты смеешь предлагать мне подобное?"
            img 22959
            m "Моя... Она стоит миллионы долларов!"
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 22960
            mt "Мерзкий самовлюбленный извращенец!"
            m "Уходи отсюда и не порти мне аппетит!"
            mt "Сволочь!"
            img 22961
            philip "Вы уверены, Миссис Бакфетт?"
            img 22962
            m "!!!"
            img 22963
            philip "Хорошо, сейчас я уйду..."
            philip "Но в следующий раз..."
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит, тот мерзко улыбается и уходит
            return False
        "А почему 300?!":
            pass

    # Моника возмущенно
    img 22964
    m "А почему 300?!"
    img 22965
    philip "Ну вот видите, Вы уже торгуетесь..."
    philip "Вы обычная шлюха, которую я сейчас куплю."
    img 22966
    m "Как ты смеешь такое обсуждать со мной?!"
    m "Я не шлюха! Меня нельзя купить!!!"
    img 22967
    philip "..." # улыбается
    img 22968
    m "И вообще, почему 300?!"
    m "В прошлый раз ты предлагал 500 долларов и за меньшее!"
    m "Ты считаешь, что моя... Неважно... Что она стоит так мало?!"
    img 22969
    philip "Ваши акции дешевеют, Миссис Бакфетт..."
    img 22970
    m "???"
    img 22971
    philip "Ваша киска сейчас стоит не более 100 долларов..."
    philip "И я делаю Вам щедрое предложение, предлагая 300."
    # Моника смотрит на него зло
    img 22972
    mt "Черт!"
    mt "Мне нужны деньги..."
    mt "Но не таким же способом!"
    mt "!!!"
    mt "Какая же сволочь этот Филипп!"
    img 22973
    m "..."
    m "Ты хочешь сделать это и рассказать всем?"
    img 22974
    philip "Это не в моих интересах..."
    philip "Я не хочу, чтобы все знали, что я покупаю женщину так дешево."
    img 22975
    mt "!!!"
    img 22976
    philip "Миссис Бакфетт, вы закончили свою трапезу?"
    philip "Мы можем идти."
    img 22977
    mt "Как он смеет такое мне предлагать?!"
    mt "С другой стороны, мне нужны деньги..."
    mt "Скоро я все верну и мне нельзя подрывать свою репутацию..."
    mt "А он сказал, что никому не расскажет об этом."
    mt "Что же мне делать?!"
    mt "Моника, неужели ты способна на такое пойти?!"
    mt "..."
    menu:
        "Уйти!":
            # Монику бомбит
            m "Как ты смеешь предлагать мне подобное?"
            img 22959
            m "Моя... Она стоит миллионы долларов!"
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 22960
            mt "Мерзкий самовлюбленный извращенец!"
            m "Уходи отсюда и не порти мне аппетит!"
            mt "Сволочь!"
            img 22961
            philip "Вы уверены, Миссис Бакфетт?"
            img 22962
            m "!!!"
            img 22963
            philip "Хорошо, сейчас я уйду..."
            philip "Но в следующий раз..."
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит, тот мерзко улыбается и уходит
            return False
        "Согласиться на предложение Филиппа.":
            pass
    # Моника смотрит на него пристально
    img 22978
    philip "Мы можем идти."
    m "Если про это кто-то узнает - я тебя убью!"
    img 22979
    philip "Не беспокойтесь, мой член бывал и не в таких местах..."
    philip "И при этом у меня все прекрасно."
    m "..."
    img 22980
    m "Оплати мой счет."
    # Моника смотрит на него, тот ей улыбается в ответ
    img 22981
    philip "Это повысит общую стоимость моих расходов, и они превысят стоимость Вашей киски."
    m "Мерзавец!"
    m "!!!"
    img 22982
    philip "Пойдемте, Миссис Бакфетт. Думаю, что мне пора попробовать Вашу киску."
    return

# ресторан отеля ЛеГранд, туалет
label ep210_dialogues2_escort_start_Phillip_2:
    # Моника с Филиппом стоят в туалете

    # если Моника делала ему минет в туалете
    img 16086
    m "Снова это жуткое место..."
    #
    $ notif(_("Моника делала Филиппу минет в туалете"))
    #
    m "Неужели нельзя было в этот раз подобрать место получше?!"
    img 16087
    philip "Гостиничный номер будет стоить гораздо дороже Вашей киски!"
    philip "Как Вы знаете, я умею считать деньги!"
    # если Моника НЕ делала ему минет в туалете
    img 16086
    m "Куда ты меня привел, Филипп?"
    m "Это мужской туалет!"
    img 16087
    philip "Миссис Бакфетт!"
    philip "Мне будет неудобно находиться в женском туалете!"
    philip "Ну а для Вас, полагаю, нет никакой разницы, ведь так?"
    img 16088
    m "Я думала это будет хотя бы гостиничный номер!"
    img 16089
    philip "Гостиничный номер будет стоить гораздо дороже Вашей киски!"
    philip "Как Вы знаете, я умею считать деньги!"
    philip "Поэтому туалет как раз подойдет для этой цели!"
    #

    # Моника зло на него смотрит
    img 16090
    philip "Задирайте платье, Миссис Бакфетт. Покажите мне Вашу киску."
    m "!!!"
    m "Что, прямо вот так?! Так быстро?!"
    img 16091
    philip "Да. Я это купил и это уже мое."
    img 16092
    mt "Мерзавец!"
    m "..."
    img 16093
    menu:
        "Уйти!":
            # Монику бомбит
            img 16094
            m "Как ты смеешь так со мной обращаться?!"
            m "Моя... Она стоит миллионы долларов!"
            img 16095
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 16096
            mt "Мерзкий самовлюбленный извращенец!"
            mt "Сволочь!"
            img 16097
            philip "Вы уверены, Миссис Бакфетт?"
            img 16098
            m "!!!"
            philip "Хорошо..."
            philip "Но в следующий раз..."
            img 16099
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return False
        "Ударить мерзавца и уйти! (прерывание квеста)":
            # Монику бомбит, она подходит к нему ближе и орет на него
            img 16094
            m "Как ты смеешь так со мной обращаться?!"
            m "Мерзкий самовлюбленный извращенец!"
            m "!!!"
            # бьет между ног коленом
            img 16100
            w
            img 16101
            m "Сволочь!"
            m "!!!"
            img 16102
            philip "АААААААА!!!" # падает
            philip "Сучка!!!"
            img 16103
            m "Да пошел ты, придурок!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return False
        "Задрать платье.":
            pass
    # Моника неуверенно поворачивается к нему задом и задирает платье немного
    img 16104
    philip "Это никуда не годится, Миссис Бакфетт..."
    philip "Я за это и цента не заплачу."
    img 16105
    philip "Поднимай платье еще выше."
    # Моника задирает его до талии и стоит перед ним с голой попой
    img 16106
    w
    img 16107
    philip "А теперь предложите мне себя..."
    philip "Раздвиньте ноги и покажите мне, что там между ними."
    # Моника злится
    img 16108
    m "!!!"
    m "Но..."
    img 16109
    philip "Никаких 'но'. Будете много разговаривать, ничего не заработаете."
    philip "Раздвигайте ноги!"
    mt "!!!"
    img 16110
    menu:
        "Уйти!":
            # Монику бомбит
            img 16094
            m "Как ты смеешь так со мной обращаться?!"
            m "Моя... Она стоит миллионы долларов!"
            img 16095
            m "А таким негодяям, как ты, о ней остается только мечтать!"
            m "!!!"
            img 16096
            mt "Мерзкий самовлюбленный извращенец!"
            mt "Сволочь!"
            img 16097
            philip "Вы уверены, Миссис Бакфетт?"
            img 16098
            m "!!!"
            philip "Хорошо..."
            philip "Но в следующий раз..."
            img 16099
            m "Не будет никакого следующего раза!!!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return False
        "Ударить мерзавца и уйти! (завершение квеста)":
            # Монику бомбит, она подходит к нему ближе и орет на него
            img 16094
            m "Как ты смеешь так со мной обращаться?!"
            m "Мерзкий самовлюбленный извращенец!"
            m "!!!"
            # бьет между ног коленом
            img 16100
            w
            img 16101
            m "Сволочь!"
            m "!!!"
            img 16102
            philip "АААААААА!!!" # падает
            philip "Сучка!!!"
            img 16103
            m "Да пошел ты, придурок!"
            m "!!!"
            # Моника зло на него смотрит и уходит
            return False
        "Раздвинуть ноги.":
            pass
    # Моника нагибается и раздвигает ноги
    img 16111
    mt "Ненавижу!!!"
    # он расстегивает ширинку и достает член
    img 16112
    philip "Давно я не трахал таких 'леди' в туалете ресторана."
    m "!!!"
    # подходит к ней ближе и засовывает член в нее
    # Моника в ужасе, но не сопротивляется
    img 16113
    mt "Я постараюсь это сейчас перетерпеть, потому что мне нужны деньги."
    mt "Но потом я ему отомщу!"
    mt "Он будет одним из первых, кого Моника Бакфетт накажет за все его мерзкие поступки!"
    # секс с Филиппом
    img 16114
    w
    img 16115
    philip "Мммммм..."
    philip "У Вас неплохая киска, Миссис Бакфетт..."
    philip "Конечно, она не стоит 300 долларов..."
    philip "Но все же..."
    philip "Ммммм..."
    img 16116
    philip "Мне приятно Вас трахать, Миссис Бакфетт..."
    philip "Думаю, это не последняя наша с Вами встреча..."
    philip "Ммммм..."
    img 16117
    philip "Даааа..."
    # кончает
    img 16118
    w
    img 16119
    w
    img 16120
    philip "АААААААА!!!"
    img 16121
    # кадр меняется, Филипп с застегнутой ширинкой, Моника с недовольным видом поправляет платье
    img 16122
    philip "Неплохо, Миссис Бакфетт..."
    philip "Можете забирать свои деньги."
    # кладет деньги куда-нибудь на столик или раковины
    img 16123
    m "Мерзавец!"
    m "!!!"
    img 16124
    philip "Вы знаете, Миссис Бакфетт..."
    philip "Я готов сделать исключение из своего правила не использовать одну и ту же женщину дважды..."
    # протягивает ей свою визитку
    img 16125
    m "???"
    m "Что это значит?"
    img 16126
    philip "Это значит, что мне нужна шлюха выходного дня."
    img 16127
    m "Что за мерзкое название?"
    img 16098
    philip "Я предлагаю Вам быть моей личной шлюхой, которая приходит ко мне по субботам..."
    m "!!!"
    img 16128
    philip "Это исключение, которое я делаю далеко немногим."
    philip "Будешь приходить в субботу. Остальные дни у меня расписаны."
    philip "Вообще, субботняя шлюха у меня уже есть... Но она иногда по субботам приходить не может."
    img 16091
    philip "Поэтому Вы, Миссис Бакфетт, будете субботней шлюхой номер два... На замену."
    philip "Придете ко мне вечером в субботу. Я плачу 100 долларов за вечер."
    img 16095
    m "!!!"
    m "Я никогда на такое не пойду!"
    # Моника злобно смотрит на него, тот улыбается мерзкой улыбочкой
    img 16129
    philip "Не забудьте, Миссис Бакфетт! Вечером в субботу."
    img 16099
    m "Иди к черту!"
    m "!!!"
    # Моника уходит
    $ log1 = _("У меня появилась возможность дополнительного заработка по субботам. У Филиппа. Но смогу ли я?") # квест лог
    return

# Моника, выйдя на улицу после секса с Филиппом
label ep210_dialogues2_escort_start_Phillip_3:
    # не рендерить!
    mt "Боже, какой кошмар!"
    mt "Я не верю, что я смогла решиться на такое!!!"
    mt "Моника, неужели это все происходит с тобой на самом деле?!"
    mt "... (хмык)"
    mt "Как он мог мне предложить стать его субботней шлюхой?!"
    mt "Да еще и на замену!"
    mt "Он предложил это мне, Монике Бакфетт!!!"
    mt "Этот никчемный жадный неудачник думает, что я соглашусь на подобное?!"
    mt "!!!"
    return

# Моника, выйдя на улицу, если послала Филиппа и секса не было
label ep210_dialogues2_escort_start_Phillip_4:
    # не рендерить!
    mt "Мерзкий извращенец!!!"
    mt "Никчемный неудачник!!!"
    mt "Как он посмел со мной так обращаться!!!"
    mt "Ненавижу его!"
    return

# Моника, проходя мимо ресепшна отеля, когда выходит на улицу
label ep210_dialogues2_escort_start_Phillip_5:
    img 16367
    reception "А что это за мужчина присел за ваш столик, Мэм?"
    reception "Вы уверены в том, что это был просто ужин?"
    img 16368
    m "А вы уверены, что я должны отчитываться перед каким-то администратором?"
    m "Это мое личное дело и вас это не касается!"
    img 16369
    mt "Какая-то никчемная администраторша, а задает мне такие вопросы!"
    mt "!!!"
    # Моника гордо уходит, азиатка подозрительно смотрит ей вслед (взять арты из предыдущей сцены в отеле)
    return

# мысли Моники перед посещением квартиры Филиппа
label ep210_dialogues2_escort_start_Phillip_6:
    # не рендерить!
    mt "Я же могу послать все к черту и просто не ехать к этому мерзавцу..."
    mt "И поискать другой способ заработать деньги."
    mt "С другой стороны, я быстро смогу заработать у него."
    mt "..."
    mt "Еще он говорил, что не встречается с одной женщиной дважды... А меня пригласил к себе домой..."
    mt "..."
    mt "Возможно, он неравнодушен ко мне... В принципе, как и все мужчины..."
    mt "И под такой грубой манерой общения пытается скрыть это."
    mt "..."
    mt "А еще он богат и, возможно, можно заставить его помочь мне с деньгами."
    mt "Тогда я смогу купить себе дом..."
    mt "И послать к черту тех деревенщин, что живут сейчас в моем бывшем доме."
    mt "Хммм... Мне кажется, что мне нужно будет поехать домой к Филиппу... И попытаться найти с ним общий язык."
    return

# мысли Моники (клик на дом Филиппа) суббота
label ep210_dialogues2_escort_start_Phillip_7:
    # не рендерить!
    mt "Неужели я на такое пойду?!"
    mt "Но мне нужны эти деньги..."
    return

# мысли Моники (клик на дом Филиппа) не суббота
label ep210_dialogues2_escort_start_Phillip_8:
    # не рендерить!
    mt "Мне сегодня нечего там делать."
    mt "Этот мерзавец сказал приходить к нему в субботу вечером."
    return

# мысли Моники (клик на дом Филиппа) суббота, день
label ep210_dialogues2_escort_start_Phillip_9:
    # не рендерить!
    mt "Мне сейчас нечего там делать."
    mt "Этот мерзавец сказал приходить к нему в субботу вечером."
    return

# мысли Моники (глазик) в красивом платье
label ep210_dialogues2_escort_start_Phillip_10:
    # не рендерить!
    mt "Я не могу поверить в происходящее..."
    mt "Я, Моника Бакфетт, приехала к этому мерзавцу!"
    mt "Возможно, я смогу сделать так, чтобы этот неудачник помог мне с деньгами."
    return

# мысли Моники (глазик) в любой одежде, кроме красивого платья
label ep210_dialogues2_escort_start_Phillip_11:
    # не рендерить!
    mt "Я не могу прийти к этому мерзавцу в такой одежде."
    mt "Он знает, что я Моника Бакфетт. Я леди. И должна выглядеть соответствующе."
    return

# дом Филиппа в субботу
label ep210_dialogues2_escort_start_Phillip_12:
    # Моника заходит в дом Филиппа, стоит рядом с входной дверью в гостиной
    # Филипп на диване или стоит посередине гостиной
    img 16373
    philip "..."
    m "Филипп, я пришла..."
    m "..."
    img 16374
    w
    img 16375
    philip "Скажи, кто ты?"
    philip "Кто ко мне пришел?"
    img 16376
    m "???"
    menu:
        "Субботняя шлюха номер 2.":
            img 16377
            mt "Черт!"
            mt "Я не хочу это говорить!"
            mt "Но если я не скажу это..."
            img 16378
            mt "Он выгонит меня и я не смогу заработать денег."
            mt "..."
            img 16379
            m "Я субботняя... Субботняя ш-шлюха..."
            philip "У меня уже есть одна субботняя шлюха. А ты кто?"
            img 16380
            m "Субботняя шлюха номер 2."

            # если Филипп в этот день без шлюхи номер 1
            img 16381
            philip "Субботняя шлюха номер 2 может заходить."
            # Моника проходит в гостиную

            # если Филипп в этот день с шлюхой номер 1
            # к нему подходит другая девушка с отеля и он ее обнимает
            # шлюха номер 1 на Монику смотрит пренебрежительно
            img 16381
            philip "У меня сегодня субботняя шлюха номер 1."
            philip "Субботняя шлюха номер 2 может прийти через неделю."
            img 16454
            w
            img 16455
            # Моника оказывается на улице
            mt "Вот мерзавец!"
            mt "Неужели я стала шлюхой?!"
            mt "Нет. Это не так."
            mt "Это просто временные трудности!"
            mt "Я делаю это вынужденно..."
            mt "Так что этот раз не считается..."
            return
        "Моника Бакфетт!":
            img 16382
            mt "Вот мерзавец!"
            mt "Он хочет, чтобы я назвала себя какой-то шлюхой!"
            img 16383
            mt "Не дождется!!!"
            mt "Достаточно того, что я сюда приехала!"
            img 16379
            m "Я Моника Бакфетт!"
            philip "У меня нет ничего общего с Миссис Бакфетт."
            # Моника оказывается на улице
            mt "Неужели я стала шлюхой?!"
            mt "Нет. Это не так."
            mt "Это просто временные трудности!"
            mt "Я делаю это вынужденно..."
            mt "Так что этот раз не считается..."
            return False
    return

label ep210_dialogues2_escort_start_Phillip_13a: #На улице
    whore_number_1 "Шлюха номер 2, подожди!"
    return

# если у Филиппа шлюха номер 1
# в один из визитов Моники, после того, как она оказалась на улице
label ep210_dialogues2_escort_start_Phillip_13:
    # к ней выходит шлюха номер 1
    img 23167
    whore_number_1 "Шлюха номер 2, подожди!"
    img 23168
    m "???" # смотрит на нее удивленно
    img 23169
    whore_number_1 "Слушай, я зарабатываю 200 долларов у него."
    whore_number_1 "Хочешь, я дам тебе 50 долларов?"
    img 23170
    m "50 долларов?"
    m "За что?"
    img 23171
    whore_number_1 "Ты мне поможешь удовлетворить Филиппа."
    img 23172
    m "Что? За 50 долларов?!"
    img 23173
    whore_number_1 "Да. 50 баксов тебе, остальные 150 - мои."
    img 23174
    m "..."
    menu:
        "Отказаться.":
            # Моника зло смотрит на нее
            img 23175
            mt "Он платит этой шлюхе 200 долларов!"
            mt "А мне - какие-то жалкие 100!"
            mt "Мне! Самой красивой женщине этого города!!!"
            mt "!!!"
            # высокомерно говорит шлюхе номер 1
            img 23176
            m "Неужели ты думала, что я соглашусь на такое?!"
            m "Конечно, нет!!!"
            mt "Да еще и за 50 долларов!"
            mt "!!!"
            return False
        "Мне нужны эти деньги (в следующем обновлении).":
            return
    return

# Моника зашла в гостиную Филиппа
label ep210_dialogues2_escort_start_Phillip_14:
    img 16384
    mt "Мне даже думать противно о том, что мне предстоит сейчас сделать..."
    mt "Чтобы заработать какие-то жалкие 100 долларов."
    menu:
        "Минет.":
            return 1
        "Секс.":
            return 2
    return


# если выбран пункт "Минет"
label ep210_dialogues2_escort_start_Phillip_15:
    # Филипп садится на диван перед ТВ
    img 16385
    philip "У меня была тяжелая неделя."
    philip "Я хочу, чтобы шлюха номер 2 расслабила меня своим ротиком."
    mt "..."
    # он берет пульт от ТВ и смотрит телевизор
    img 16386
    mt "Моника, неужели ты способна на такое пойти?!"
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            img 16387
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16388
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            img 16389
            m "!!!"
            # Моника уходит
            return False
        "Сделать, что требует Филипп.":
            pass
    # Филипп поворачивается к Монике
    img 16390
    m "..."
    philip "В чем дело? Мне долго еще ждать?"
    img 16387
    mt "..."
    mt "Боже! Как же это все омерзительно!"
    mt "Но мне нужны эти деньги..."
    # Моника подходит к дивану, на котором сидит Филипп, и опускается перед ним на колени
    img 16391
    philip "Открывай свой ротик и приступай к работе."
    # расстегивает ширинку, достает член и продолжает смотреть в ТВ
    img 16392
    m "Я тебе буду делать это... А ты... Будешь смотреть телевизор?!"
    m "!!!"
    img 16393
    philip "Это тебя не касается."
    philip "Шлюха номер 2 должна отрабатывать свои деньги..."
    philip "А не задавать мне глупые вопросы."
    img 16394
    mt "!!!"
    mt "Мерзавец!"
    mt "Ненавижу!!!"
    # Моника берет в рот его член, Филипп в это время продолжает смотреть ТВ со скучающим видом
    # минет
    img 16395
    philip "Да... Вот так..."
    img 16396
    w
    img 16397
    w
    img 16398
    w
    img 16399
    philip "Возьми его глубже..."
    img 16400
    w
    img 16401
    w
    img 16402
    w
    img 16403
    w
    img 16404
    philip "Еще глубже."
    img 16405
    w
    img 16406
    w
    img 16407
    w
    img 16408
    w
    img 16409
    # Моника давится, он кончает
    img 16410
    philip "Мммммм..."
    # сперма стекает изо рта Моники
    img 16411
    philip "Теперь проглоти это."
    m "..."
    menu:
        "Выплюнуть.":
            # Моника смотрит на него с отвращением
            img 16412
            mt "Я не смогу проглотить это!"
            mt "Меня стошнит."
            # выплевывает
            img 16413
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            img 16389
            pass
        "Проглотить.":
            pass
            img 16414
            w
    # Филипп достает из кармана купюру 100 долларов и кидает ее на диван
    img 16415
    philip "Субботняя шлюха номер 2 может забрать свои деньги."
    philip "И уходить."
    # Моника забирает деньги
    img 16416
    m "..."
    img 16419
    menu:
        "Попросить еще денег.":
            img 16417
            mt "Может, поросить у него еще денег?"
            mt "Ведь в прошлый раз он заплатил мне 300 долларов."
            img 16420
            m "Филипп, я..."
            m "..."
            m "Хотела спросить, не мог бы ты дать мне еще немного денег?"
            # поворачивается к ней
            img 16421
            philip "???"
            philip "Моей субботней шлюхе нужны деньги?"
            img 16422
            philip "Я тебе их только что заплатил."
            philip "Хочешь еще денег - приходи через неделю."
            # отворачивается
            img 16423
            mt "Жадный неудачник!"
            return
        "Уйти.":
            pass
    img 16417
    mt "Сволочь!"
    mt "!!!"
    img 16418
    # Моника уходит
    return

# если выбран пункт "Секс"
label ep210_dialogues2_escort_start_Phillip_16:
    # Филипп садится на диван
    img 16424
    philip "Сейчас шлюха номер 2 предложит мне себя, как в прошлый раз."
    philip "А я пока подумаю, что я с ней сегодня сделаю."
    # выбор: уйти или предложить себя Филиппу
    img 16386
    mt "Моника, неужели ты способна на такое пойти?!"
    mt "..."
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            img 16387
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16425
            m "Нет. Я..."
            m "Я не буду этого делать!"
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            img 16418
            return False
        "Предложить себя Филиппу.":
            pass
    # Моника стоит перед ним в нерешительности
    img 16426
    m "..."
    m "Ч-что мне сделать?"
    img 16427
    philip "Задирай платье и нагибайся, раздвинув ноги."
    # Моника поворачивается к нему задом и делает, как он сказал
    img 16428
    w
    img 16429
    philip "Что же шлюха может предложить мне сегодня?"
    philip "Возможно, свою задницу?"
    img 16430
    mt "О, нет! Он хочет сделать это с моей попой?!"
    mt "Нет! Я не перенесу этого!"
    mt "!!!"
    img 16431
    philip "Хммм... Нет, задницу я оставлю на потом..."
    philip "Я подожду, когда твои акции подешевеют..."
    philip "А сейчас... Может быть, ротик?"
    # Филипп расстегивает штаны, достает стояк, начинает подрачивать его
    img 16432
    philip "Субботняя шлюха, повернись и покажи мне свою грудь, приспусти платье."
    # Моника поворачивается и приспускает платье, смотрит на него зло
    img 16433
    philip "Хорошо. Мне нравится, что моя шлюха такая послушная."
    img 16434
    mt "Сволочь!"
    mt "!!!"
    img 16435
    philip "Кстати, я даже не предложил своей субботней шлюхе номер 2 присесть..."
    philip "Иди сюда. Присаживайся."
    # Моника смотрит на диван и делает шаг
    img 16436
    philip "Нет, не на диван. Садись на мой член."
    img 16437
    menu:
        "Убежать!":
            # Моника смотрит с отвращением
            img 16438
            mt "Этот мерзавец обращается со мной, как с дешевой шлюхой..."
            mt "Я не могу пойти на это!"
            img 16439
            m "Нет. Я..."
            m "Я не буду этого делать!"
            img 16440
            m "Я не могу!"
            m "!!!"
            # Моника уходит
            return False
        "Сесть на член Филиппа.":
            pass
    # Моника смотрит на его член
    img 16441
    mt "Ненавижу этого мерзавца!"
    mt "!!!"
    # подходит к нему и нерешительно выполняет, сев к нему на колени, лицом к нему
    # тот, откинувшись на диван, самодовольно ухмыляется
    img 16442
    philip "Давай, выполняй. Шлюха же хочет заработать денег?"
    # секс, Моника на его коленях, двигается вверх-вниз, он лапает ее за попу и за грудь
    img 16448
    mt "Это так... Так неприятно..."
    mt "Скорее бы это закончилось."
    mt "Хочу забрать деньги и уйти отсюда."
    img 16443
    philip "Да..."
    img 16444
    philip "Давай, быстрее..."
    img 16445
    philip "Еще..."
    # Моника смотрит на него с отвращением
    img 16446
    w
    img 16447
    m "..."
    img 16449
    philip "Оооо... Даааа..."
    # кончает ей на платье или на живот
    img 16450
    philip "Мммммм..."
    img 16451
    w
    img 16452
    w
    img 16453
    # Филипп одевается и бросает на диван купюру
    img 16415
    philip "Это твой сегодняшний заработок."
    philip "Субботняя шлюха номер 2 может забрать свои деньги."
    philip "И уходить."
    # Моника одевается и забирает деньги
    img 16416
    m "..."
    menu:
        "Попросить еще денег.":
            img 16417
            mt "Может, поросить у него еще денег?"
            mt "Ведь в прошлый раз он заплатил мне 300 долларов."
            img 16420
            m "Филипп, я..."
            m "..."
            m "Хотела спросить, не мог бы ты дать мне еще немного денег?"
            # смотрит на нее
            img 16421
            philip "???"
            philip "Моей субботней шлюхе нужны деньги?"
            img 16422
            philip "Я тебе их только что заплатил."
            philip "Хочешь еще денег - приходи через неделю."
            # отворачивается
            img 16423
            mt "Жадный неудачник!"
            return
        "Уйти.":
            pass
    img 16418
    mt "Сволочь!"
    mt "!!!"
    # Моника уходит
    return


# мысли Моники (вышла от Филиппа, заработав деньги)
label ep210_dialogues2_escort_start_Phillip_17:
    # не рендерить!
    mt "Я заставлю пожалеть его об этом!"
    mt "Он еще будет умолять меня о прощении!"
    mt "!!!"
    return

# мысли Моники (вышла от Филиппа, НЕ заработав денег)
label ep210_dialogues2_escort_start_Phillip_18:
    # не рендерить!
    mt "Мерзкий извращенец!"
    mt "Притворяется джентельменом, а на деле ведет себя как грязный хам!"
    mt "Ненавижу его!"
    return

# мысли Моники (вышла от Филиппа, хочет снова зайти к нему домой)
label ep210_dialogues2_escort_start_Phillip_19:
    # не рендерить!
    mt "Не хочу его больше видеть!!!"
    mt "Мерзавец!"
    return

# мысли Моники (глазик, вышла от Филиппа)
label ep210_dialogues2_escort_start_Phillip_20:
    # не рендерить!
    mt "Я не могу поверить в происходящее..."
    mt "Я, Моника Бакфетт, унижалась перед этим мерзавцем!"
    mt "Из-за каких-то 100 долларов!"
    mt "!!!"
    mt "Я заставлю его пожалеть об этом!"
    return
