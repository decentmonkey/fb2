default monicaPubPrivatDanceJoe1 = False # Моника согласилась пойти в приват
default monicaPubPrivatDanceJoe2 = False # Моника согласилась назвать себя шлюхой
default monicaPubPrivatDanceJoe3 = False # Моника согласилась потереться об клиента попой


# приват будет доступен один раз в неделю

# Паб. Моника находится в гримерке после выступления на сцене.
# в гримерку заходит Джо.
label ep212_dialogues2_shiny_hole_1:
    # частично использовать имеющиеся арты
    # Джо смотрит на Монику похотливо
    img_22870
    w
    img_22871
    joe "[monica_pub_name], тебе очень идет этот костюм."
    joe "Я тебе говорил уже об этом?"
    # Моника смотрит на него презрительно и молчит
    img_22880
    mt "Что опять нужно от меня этому неудачнику Джо?"
    m "..."
    joe "Не спеши переодеваться, [monica_pub_name]."
    img_22874
    m "Почему это?" # раздраженно
    m "Я только что со сцены."
    m "С меня хватит!"
    joe "У тебя есть еще на сегодня работа..."
    m "???" # подозрительно
    m "Какая еще работа?"

    joe "Один наш постоянный клиент... В общем..."
    joe "Он хочет, чтобы ты станцевала для него..."
    img_22873
    joe "И только для него."  # подмигивает

    m "Только для него?"
    m "Приватный танец?!" # зло
    joe "Да!"
    m "Нет!"
    m "!!!"

    #
    $ notif(_("Моника танцевала приват для Мистера Беркельбауха"))
    #
    mt "Я не собираюсь больше танцевать приват!"
    mt "Мне хватило этого неудачника банкира в прошлый раз!"
    mt "Мало того, что пришлось прикасаться к его..."
    mt "К нему своей попой!"
    mt "Так я еще ни цента за это не заработала!"
    mt "!!!"
    mt "Может, предложить ему, пусть Эшли идет в приват?"

    m "Пусть ваша рыжая королева шлюх идет в приват!"
    m "Я не собираюсь заниматься этим, Джо!" # сердится
    m "!!!"
    joe "[monica_pub_name], в этот раз у тебя нет выбора."
    joe "Клиент требует именно тебя."
    joe "И я уже пообещал ему, что ты придешь..."
    joe "Он ждет тебя в подсобке барменов."
    m "Что значит 'нет выбора'?!"
    m "Выбор всегда есть!"
    m "Я просто не пойду сейчас к клиенту и ты ничего мне не сможешь сделать!"
    m "!!!"
    joe "Да ладно тебе, [monica_pub_name]!"
    joe "Ты ведь уже танцевала в привате для какого-то клиента..."
    joe "Мне Эшли говорила, что он остался тобой очень доволен."

    #
    $ notif(_("Эшли показала свою голую попу Мистеру Беркельбауху"))
    #
    mt "Он остался доволен голым задом твой жены, придурок!"
    mt "Видимо, она тебе об этом ничего не рассказала..."

    joe "Не переживай, [monica_pub_name]."
    joe "Он ничего тебе не сделает..."
    joe "Просто посмотрит и все..."
    joe "А я лично проконтролирую, чтобы с тобой ничего не случилось!"
    m "Лично?!"
    m "Ты тоже собираешься присутствовать при этом?!"
    m "?!?!?!"
    joe "Конечно!"
    joe "Только ради твоей безопасности!"
    joe "Я пообещал тебе, что все будет гладко."
    joe "Поэтому лично прослежу за этим!"

    # если Моника просила прощения у Джо и показывала ему свою попу
    $ notif(_("Моника просила прощения у Джо"))
    #
    joe "Тем более, я уже видел твою попку..."
    joe "И не откажусь еще раз посмотреть на нее." # подмигивает

    m "!!!"

    # Подмигивает
    joe "Ты просто еще не знаешь сколько клиент обещает за твой приват..."
    m "..."
    $ menu_corruption = [ep212_private_dance1]
    menu:
        "Сколько клиент заплатит за приват?":
            $ monicaPubPrivatDanceJoe1 = True # Моника согласилась пойти в приват
            pass
        "Я не пойду в приват!":
            mt "Я не собираюсь раздеваться перед каким-то..."
            mt "Никчемным неудачником!"
            mt "Пусть Джо предложит своей жене повертеть голым задом перед клиентом!"
            m "!!!"
            m "За кого ты меня принимаешь?!"
            m "Я не пойду ни в какой приват!"
            joe "Но [monica_pub_name]!"
            joe "Клиент уже ждет тебя!"
            m "Это не мои проблемы!"
            m "Ты ему обещал приват, вот ты и танцуй!"
            m "Мелкое ничтожество!"
            m "!!!"
            # Моника гордо уходит
            return False
    m "Сколько клиент заплатит за этот приват?"
    joe "Клиент обещал заплатить 500 долларов за этот приват."
    joe "Подумай только, [monica_pub_name]."
    joe "Один танец и 500 баксов у тебя в кармане."
    joe "Это же так просто - станцуешь перед ним и все!"
    mt "500 долларов?"
    mt "..."
    mt "Черт!"

    # если Моника уже работает в эскорте
    $ notif(_("Моника зарабатывает деньги, обслуживая клиентов в эскорте"))
    #
    mt "Я столько за один вечер не всегда могу заработать даже в эскорте..."
    mt "Обслуживая разных извращенцев..."
    mt "А здесь.. Просто раздеться..."
    mt "Без секса и других мерзостей..."

    # если Моника уже арендует шикарный апартамент
    $ notif(_("Моника арендует апартаменты у продавца кебабов"))
    #
    mt "Этих денег хватит с лихвой, чтобы продлить мои апартаменты на целую неделю..."
    mt "Без всяких скидок от этого грязного Джека!"

    m "Джо, я не пойду!"
    m "Этот клиент потом всем расскажет..."
    m "Я не хочу, чтобы все знали об этом."
    m "..."
    joe "Об этом можешь не переживать, [monica_pub_name]."
    joe "Я уже предупредил клиента."
    joe "Он никому не скажет."
    # улыбается от уха до уха
    joe "Ты ведь знаешь, [monica_pub_name], что мне можно доверять!"
    joe "Ну что, пошли?"
    # Джо выходит из гримерки
    # Моника в сомнениях
    mt "500 долларов..."
    mt "..."
    mt "Если мне что-то не понравится, я пошлю Джо к черту и уйду оттуда."
    mt "И этот никчемный Джо мне ничего не сможет сделать."
    $ log1 = _("Пойти в подсобку барменов.")
    return True

# подсобка барменов
label ep212_dialogues2_shiny_hole_2:
    # на диване сидит, развалившись клиент (скучающий чувак у шеста)
    # Джо стоит в стороне и наблюдает
    $ temp_var1 = monica_strip_tips_today
    customer3 "О, наконец-то пришла..."
    mt "Фу! Я помню этого клиента..."
    mt "Строит из себя непонятного кого..."
    mt "А на самом деле такой же неудачник, как и все!"
    customer3 "Ну давай... Как там тебя зовут?"
    m "Я..."
    customer3 "Впрочем, неважно. Я все равно не запомню."
    customer3 "Я рад что ты не как Мэнсфилд..."
    customer3 "Хорошо, что ты такая же шлюха, как та рыжая..."
    mt "!!!"
    mt "Мерзавец!"
    m "Я не шлюха!" # зло
    # Джо вмешивается и строго говорит
    joe "Не спорь с клиентом!!!"
    # Моника смотрит на Джо
    m "!!!"
    customer3 "Да, лучше не спорь..."
    customer3 "Скажи, что ты шлюха. Я доплачу тебе за это 50 баксов."
    mt "Что этот неудачник себе позвояет?!"
    mt "?!?!?!"
    $ menu_corruption = [ep212_private_dance2]
    menu:
        "Притвориться шлюхой.":
            $ monicaPubPrivatDanceJoe2 = True # Моника согласилась назвать себя шлюхой
            customer3 "Ну, отвечай..."
            customer3 "Ты шлюха?"
            m "..."
            mt "Если я сейчас не сделаю, как он просит..."
            mt "Клиент будет недоволен и Джо расскажет об этом Эшли."
            mt "И эта извращенка Эшли снова меня оштрафует."
            mt "Я не могу допустить того, чтобы она отбирала у меня деньги..."
            mt "Тем более, это не я себя назову шл... Этим словом."
            mt "Это делает [monica_pub_name]..."
            mt "..."
            m "Я..."
            m "Шлюха..."
            $ add_money(50.0)
            $ monica_strip_tips_today += 50.0
            customer3 "Да..."
            customer3 "Видишь, как все просто?"
            customer3 "Сказала всего два слова и уже заработала полтинник."
            customer3 "А теперь шлюха станцует для меня."
            customer3 "И получит за это еще денег..."
            customer3 "Шлюха же хочет еще денег?"
            m "..." # зло смотрит на него
            customer3 "Скучно с тобой... Даже поговорить не можешь нормально." # лениво
            customer3 "Не удивительно, что ты не можешь устроиться на нормальную работу, как Я..."
            customer3 "А зарабатываешь, показывая свою задницу со сцены..."
        "Поставить на место этого идиота! (Моника слишком приличная) (disabled)" if monicaBitch == False: #
            pass
        "Поставить на место этого идиота!" if monicaBitch == True:
            # Монику бомбит, она орет на клиента
            $ notif_monica()
            m "Слышишь, ты?!"
            m "Еще раз назовешь меня шлюхой, я тебе оторву твои яйца!"
            joe "[monica_pub_name]!"
            # рявкает на Джо
            m "Заткнись, Джо!"
            m "!!!"

                # потом снова на клиента
#                m "Засунь свои гребанные деньги себе в задницу!"
#                m "Инстинктивное животное!"
#                m "!!!"
            # уходит
    mt "Вот сволочь!"
    mt "Знал бы он, кто Я такая на самом деле!"
    mt "!!!"
    customer3 "Я рад, что я первый, для кого ты танцуешь приват."
    customer3 "Помимо меня еще много желающих посмотреть на твою голую задниицу."
    customer3 "Но я их всех опередил."
    # Джо улыбается ехидно
    joe "..."
    m "..."
    mt "Самомнение просто зашкаливает, а на деле..."
    mt "Очередной никчемный неудачник!"
    customer3 "Танцуй давай!"
    menu:
        "Начать танцевать.":
            pass
    # Моника начинает танцевать
    # клиент с Джо похотливо на нее смотрят
    customer3 "Знаешь, ты хоть и скучная, но задница у тебя что надо..."
    customer3 "Я давно хотел, чтобы ты сняла свой наряд официантки и показала мне ее..."
    customer3 "Я видел почти всю твою задницу, когда заглядывал тебе под юбку в прошлый раз."
    customer3 "Но знаешь, так мне будет гораздо удобнее ее разглядеть."
    mt "?!?!?!"
    m "Я не..."

    # если с клиентом уже был диалог, что он видел ее на сцене, а Моника-официантка это отрицала
    $ notif(_("Моника говорила клиенту, что не танцует на сцене."))
    #
    customer3 "Ну да, ну да..."
    customer3 "Ты не работаешь здесь официанткой... Бла-бла-бла..."
    customer3 "Неважно..."

    customer3 "Снимай одежду..."
    customer3 "Я плачу деньги не за танцы в этих тряпках."
    mt "Животное!"
    mt "!!!"
    # Моника танцует и снимает с себя жилет
    # Джо стоит подрачивает под своим фартучком
    # после того как она полностью разделась, клиент достает свой член
    $ add_money(100.0)
    $ monica_strip_tips_today += 100.0
    customer3 "Эй ты, смотри что у меня для тебя есть!"
    customer3 "Иди сюда, я хочу потрогать тебя..."
    mt "Начинается!"
    mt "!!!"
    m "По правилам бара клиентам на меня можно только смотреть."
    m "Прикасаться нельзя."
    customer3 "Да ладно тебе! Заработаешь больше."
    customer3 "Об этом все равно никто не узнает."
    customer3 "Да, Джо?" # ехидно улыбается
    joe "Конечно!" # тоже противно улыбается
    joe "Клиент должен быть удовлетворен!"
    mt "..."
    $ menu_corruption = [ep212_private_dance3]
    menu:
        "Сделать как требует клиент.":
            $ monicaPubPrivatDanceJoe3 = True # Моника согласилась потереться об клиента попой
            pass
        "Поставить на место этого идиота!": #
            # Монику бомбит, она орет на клиента
            $ notif_monica()
            m "Слышишь, ты, животное?!"
            m "Засунь свои гребанные деньги себе в задницу!"
            m "И не смей прикасаться ко мне!"
            m "Иначе я тебе яйца оторву!"
            joe "[monica_pub_name]!"
            # рявкает на Джо
            m "Заткнись, Джо!"
            m "!!!"
            # потом снова на клиента
            m "Неудачник!"
            m "!!!"
            # уходит
            return -1
    # Моника или злится
    m "Я здесь танцую, а не занимаюсь проституцией!" # клиенту
    m "Джо, ты говорил, что ничего подобного происходить не будет!" # Джо
    m "Что он просто посмотрит и все!"
    m "!!!"
    joe "Все правильно."
    joe "Клиентам к девочкам на привате нельзя прикасаться... Руками..."
    m "???"
    m "Что это значит, Джо?!"
    joe "Что ты сейчас удовлетворишь клиента."
    joe "Он тебя трогать при этом не будет."
    joe "Таким образом, ты не нарушишь правила, а клиент останется доволен."
    m "!!!"
    mt "Мерзавец Джо!"
    mt "О чем я только думала, когда пошла сюда с ним?!"
    mt "?!?!?!"
    mt "С другой стороны..."
    mt "Он же не будет прикасаться к моему телу своими грязными руками..."
    mt "А я смогу заработать больше денег..."
    mt "Вернее, [monica_pub_name]... Она это будет делать..."
    mt "Моника Бакфетт на такое никогда бы не пошла!"
    mt "Ой, Моника, перестань называть себя по имени даже в мыслях, пока ты здесь!"
    mt "..."
    # клиент встает с дивана
    customer3 "Мне надоело ждать..."
    customer3 "Подвинься!"
    customer3 "Я хочу, чтоб ты сделала это на столе..."
    # клент ложится на стол
    mt "!!!"
    customer3 "Что ты так смотришь?"
    customer3 "Как будто впервые увидела член."
    customer3 "Я заплачу тебе еще 100 баксов."
    customer3 "Давай, отрабатывай..."
    mt "Черт!"
    mt "..."
    menu:
        "Тереться о член клиента.":
            pass
    # Джо стоит дрочит
    # Моника неуклюже пристраивается над клиентом так, чтобы можно было тереться об его член
    # но у нее не получается ничего
    m "!!!"
    customer3 "Ну что ты делаешь?.."
    customer3 "Повернись ко мне своим задом и подвинься ближе."
    # Моника делает, как сказал клиент
    customer3 "Вооот, другое дело!"
    customer3 "Вот так мне нравится больше."
    customer3 "Теперь я могу рассмотреть твою задницу поближе..."
    mt "Долбанный извращенец!"
    mt "!!!"
    customer3 "Давай, шустрее шевели своей задницей!"
    customer3 "Дааа..."
    customer3 "Еще быстрей..."
    # Моника со злым лицом трется о клиента
    customer3 "Мммммм..."
    customer3 "Еще немного..."
    customer3 "Вот так..."
    customer3 "Мммммм..."
    menu:
        "Кончить на попу Моники.":
            customer3 "Аааааа..."
            customer3 "ААААА..."
            customer3 "АААААААА!!!"
            # Джо тихонько кончает в кулачок
            joe "Оооох..."
            joe "Ммммммм..."
            # Моника зло на него смотрит
            mt "Джо сволочь!!!"
            mt "Твоя жена тебя не видит!"
            mt "!!!"
            pass
        "Кончить на лицо Моники.":
            customer3 "Подставь свое лицо!"
            customer3 "Аааааа..."
            customer3 "Быстро!"
            customer3 "Дам за это сверху $ 30!"
            # Моника поворачивается и приближается лицо к его члену
            # он додрачивает и кончает на лицо
            customer3 "ААААА..."
            customer3 "АААААААА!!!"
            mt "!!!"
            mt "Фууу!"
            customer3 "Аха-ха!"
            $ add_money(30.0)
            $ monica_strip_tips_today += 30.0
            customer3 "Так твое лицо смотрится гораздо лучше!"
            mt "!!!"
            # Моника зло на него смотрит
            mt "Джо сволочь!!!"
            mt "Твоя жена тебя не видит!"
            mt "!!!"
            pass
    # смена кадра
    # клиент стоит одетый, клиент и Джо расслабленные и довольные, Моника стоит в трусиках, злая
    $ add_money(100.0)
    $ monica_strip_tips_today += 100.0
    customer3 "Вот твой заработок..."
    customer3 "За то, что неплохо трешься задницей."
    # клиент протягивает деньги
#    customer3 "50 баксов за то, что ты шлюха..."
#    customer3 "100 баксов за танец..."
#    customer3 "И 100 баксов за то, что неплохо трешься задницей..."
    $ temp_var1 = monica_strip_tips_today - temp_var1
    customer3 "Всего [temp_var1]. Ты неплохо заработала!"
    customer3 "Почти ничего не делая..."
    m "[temp_var1] долларов?!"
    m "?!?!?!"
    customer3 "Да..."
    customer3 "Видишь, я могу быть очень щедрым, если шлюха хорошая."
    # клиент уходит, Моника остается вдвоем с Джо
    # Моника сердито смотрит на него
    m "[temp_var1] долларов!"
    m "Джо!"
    m "Где обещанные 500?!"
    joe "[monica_pub_name], клиент обещал заплатить 500."
    joe "С тем условием, что ему все понравится."
    joe "В противном случае, клиент имеет право снизить сумму."
    joe "Тебе надо было лучше стараться, [monica_pub_name]..."
    mt "!!!"
    joe "И не забудь отдать с этих денег процент Эшли."
    # Джо уходит
    mt "Он обманул меня!"
    mt "Мерзавец!"
    mt "И я еще должна платить процент Эшли!"
    mt "АААААА!!!"
    mt "Ненавижу!"
    mt "!!!"
    return

# если Моника в другой день работает официанткой и подходит к этому клиенту и приват с ним уже был
label ep212_dialogues2_shiny_hole_3:
    # использовать имеющиеся арты
    mt "Этот жалкий жадный неудачник!!!"
    mt "!!!"
    m "Что будете заказывать?"
    customer3 "О! Хочу снова заказать твою задницу!"
    m "Это невозможно, я..."
    customer3 "Ты не танцуешь приват. Ага..."
    customer3 "Это всего лишь вопрос денег..."
    customer3 "Аха-ха!!!"
    mt "Долбануть бы этого козла чем-нибудь потяжелее!"
    mt "!!!"
    m "Что вам принести?"
    customer3 "Какая же ты все-таки скучная..."
    customer3 "Принеси мне пива..."
    # Моника уходит и возвращается с пивом
    m "Пожалуйста, ваше пиво..."
    mt "Урод!"
    customer3 "Ага..."
    customer3 "Я дам тебе $ 10 на чай, если ты нагнешься и поднимешь ту зажигалку."
    customer3 "Только сделай это спиной ко мне! Аха-ха!!!"
    # если первый раз
    m "!!!"
    customer3 "Давай, не стесняйся! Я там все уже видел!"
    customer3 "Аха-ха!!!"
    mt "Вот мерзавец!"
    mt "Я не собираюсь зарабатывать на чай таким образом!"
    mt "..."
    mt "С другой стороны, здесь, похоже, других способов нет..."
    mt "Тем более он уже все видел..."
    customer3 "Давай! Сделай это передо мной!"
    customer3 "Здесь больше никого нет!"
    # если уже было
    m "Я уже поднимала эту зажигалку..."
    customer3 "Но ведь ты хочешь еще чаевые?"
    customer3 "Тогда подними ее еще раз!"
    #

    m "..."
    menu:
        "Нагнуться за зажигалкой.":
            pass
        "Уйти.":
            m "Сам поднимай свои зажигалки, придурок!"
            return False

    customer3 "Отличная задница!"
    customer3 "Скоро я всажу в нее свой член!"
    m "Этого никогда не будет!!!"
    customer3 "Иди уже."
    mt "!!!"
    return True















#
