default ep23_dialogues5_2_first_time = True
default ep23_dialogues5_2a_first_time = True

# Моника хочет попросить Мелани о помощи с Диком.
# В это время появляется пункт спросить у Алекса где Мелани. Алекс отвечает что она бывает днем.
label ep23_dialogues5_1:
    # Моника спрашивает у Алекса где Мелани?
    img 6519
    m "Алекс... А где Мелани?"
    alex_photograph "Мелани обычно бывает днем, Миссис Бакфетт..."
    "А зачем она Вам?"
    m "Это не твое дело, Алекс..."
    return


# Если Моника была доброй с Мелани, то Моника зовет Мелани поговорить и Мелани идет в гримерку
# Если была злой, то Мелани не хочет идти, но Моника уговаривает ее
label ep23_dialogues5_2:
    if ep23_dialogues5_2_first_time == True:
        img 8693
        m "Мелани... Я хочу поговорить с тобой..."
        melanie "О чем Вы хотите поговорить со мной, Миссис Бакфетт?"

        img 8692
        m "Может мы отойти с тобой куда-нибудь?"
        "Я бы не хотела чтобы Алекс слышал наш разговор?"

        # Если Моника была злой с Мелани
        if melanieOffended2 == False and melanieOffended1 == False:
            $ notif(_("У Моники хорошие отношения с Мелани"))
            pass
        else:
            $ notif(_("У Моники плохие отношения с Мелани"))
            img 8694
            melanie "Миссис Бакфетт, у нас с Вами официальные отношения."
            "Я бы хотела чтобы у нас не было никаких секретов."
            "Это может повредить моей карьере..."
            img 8695
            mt "Мне надо как-то уговорить Мелани пойти со мной."
            "Я не собираюсь заводить разговор здесь, в присутствии Алекса!"
            "..."
            "Мелани любит лесть..."
            menu
                "Попросить вежливо.":
                    img 8696
                    m "Мелани, пожалуйста..."
                    "Да, у нас официальные отношения и ты отличный профессионал."
                    "Ты самая красивая модель в этом журнале."
                    "И я бы хотела поговорить с тобой наедине..."

                "Уйти.":
                    return False
            return

        $ ep23_dialogues5_2_first_time = False
        img 8697
        melanie "Хорошо, Миссис Бакфетт."
        "Пройдемте в гримерную комнату."

        # заходят в гримерку
        #fadelong
        img 8698
        mt "Хм..."
        "Я смотрю Мелани здесь неплохо обосновалась, пока меня нет..."

        # В гримерке Моника говорит что хочет попросить Мелани об услуге.
        # Мелани интересуется чем-же она таким может помочь Монике Бакфетт.
        img 8699
        melanie "Итак, Миссис Бакфетт?"
        m "Мелани, я хочу попросить тебя об услуги..."
        melanie "Интересно... Чем же я могу помочь Миссис Бакфетт?"

        # Моника говорит что это касается мужчины, а Мелани в этом очень сильна.
        # И это касается решения ее небольших проблем. И что она будет очень благодарна Мелани за это.
        # И повысит ее значительно выше, когда вернется назад.
        img 8700
        m "Это... Это касается одного мужчины..."
        "А ты, Мелани, насколько я знаю, очень сильна в этих вопросах..."
        "Это касается решения кое-каких небольших проблем, которые у меня возникли в последнее время..."
        img 8701
        "Я обещаю что повышу тебя значительно выше, чем ты сейчас..."
        "Когда верну все назад..."

        # Мелани говорит что не понимает зачем Моника ходит в таком виде. Она развелась с мужем и он забрал все ее деньги?
        # Моника говорит что муж у нее плохой, на что Мелани отвечает что не бывает плохих мужчин, надо просто знать к ним подход.
        # Так что, надо помочь с мужем?
        img 8702
        melanie "Да, Миссис Бакфетт."
        "По Вашему виду можно сказать что у Вас возникли небольшие проблемы."
        "Мне не совсем понятно, зачем вы ходите в этом..."
        "Вы развелись с мужем и он забрал все Ваши деньги?"
        img 8703
        m "Нет, Мелани... Муж у меня..."
        "Не будем об этом... Я не могу сказать ничего положительного про него..."
        img 8704
        melanie "Миссис Бакфетт. Не бывает плохих мужчин."
        "Просто надо знать подход к ним..."
        "Так Вам надо помочь с Вашим мужем?"

        # Моника отвечает что нет, надо помочь с другим мужчиной.
        # Мелани удивляется. Значит в этом замешан еще один мужчина? Это, значит любовь?
        # Как я сразу не догадалась. Только любовь может заставить Монику Бакфетт идти на такие жертвы у всех на виду.
        # Моника говорит что это не совсем любовь, и на пути стоит еще одна женщина.
        # Мелани говорит что еще одна женщина? Это становится интересно.
        # И что же сама Миссис Бакфетт хочет от Мелани?
        img 8705
        m "Нет, Мелани..."
        m "Мне надо помочь с... другим мужчиной..."
        img 8706
        melanie "Значит в этом замешан еще один мужчина?"
        melanie "Значит это любовь?!"
        melanie "Как я сразу не догадалась!"
        melanie "Только любовь может заставить Монику Бакфетт идти на такие жертвы!"
        img 8707
        "У всех на виду!"
        img 8708
        m "Мелани... знаешь..."
        "Это... не совсем любовь..."
        "Это касается еще одной женщины... на моем пути..."
        img 8709
        melanie "Еще одной женщины?"
        "Это становится интересно!"
        "И что же САМА Миссис Бакфетт хочет от Мелани?"

        # Моника говорит что у нее есть подозрения, что этот человек замешан в том что у нее возникли небольшие временные трудности.
        # Этот мужчина был поклонником Моники и любил ее, бегал за ней как пудель, но вдруг он изменился.
        # И еще там появилась другая женщина. И Моника предполагает что ее проблемы могут быть связаны с этим.
        # Моника пыталась найти подход к нему, но потерпела неудачу.
        # Этот мужчина любит женщин и перед Мелани он не устоит.
        # Если Дик признавался что хочет Мелани, то Моника об этом говорит. Мелани улыбается и отвечает что получает тысячи признаний в любви каждый день.
        # А как же Вы? Вы считаете что я красивее Вас, Миссис Бакфетт? Что я могу затмить ту женщину, которая встала между Вами?
        # Моника думает.
        img 8710
        m "У меня есть подозрения, что этот мужчина замешан в том, что у меня возникли небольшие временные трудности..."
        "Этот мужчина был моим поклонником и любил меня. Бегал за мной как пудель, но..."
        "Но, вдруг, он изменился."
        img 8711
        "Впоследствии еще появилась другая женщина."
        "И у меня серьезные подозрения, что все проблемы могут быть связаны с этим."
        img 8712
        "Я пыталась найти подход у этому мужчине, но потерпела неудачу."
        "Не знаю почему!!!"
        "Но этот мужчина любит женщин и перед тобой он вряд-ли устоит!"

        #Если Дик признавался что хочет Мелани
        $ notif(_("Дик признавался что хочет Мелани"))
        img 8713
        m "Еще он как-то проговорился о том что мечтает о тебе..."
        melanie "Ой, Миссис Бакфетт..."
        "Я получаю тысячи признаний в любви каждый день..."
        #

        img 8714
        melanie "А как же Вы?"
        "Вы считаете что я красивее Вас, Миссис Бакфетт?"
        "Что я смогу затмить ту женщину, которая встала между Вами?"
    else:
        img 8692
        m "Мелани... Я хочу поговорить с тобой..."
        melanie "Хорошо, Миссис Бакфетт."
        "Пройдемте в гримерную комнату."
        img 8713
        m "Я... про наш разговор..."
        img 8714
        melanie "Что же Вы ответите?"
        "Вы считаете что я красивее Вас, Миссис Бакфетт?"
        "Что я смогу затмить ту женщину, которая встала между Вами?"

    if ep23_dialogues5_2a_first_time == True:
        # Возможен ответ да или нет. Если нет, то выход. Затем диалог короче.
        img 8716
        menu:
            "Да, Мелани, возможно ты справишься лучше.":
                pass
            "Нет, Мелани. Я не думаю что ты лучше меня.":
                img 8715
                m "Нет, Мелани. Я не думаю что ты лучше меня."
                return False
        # Моника говорит что красота - это условная вещь, но в чем Мелани хорошо разбирается- так это в том как управлять мужчинами.
        # Мелани улыбается и говорит что это очевидно и она рада что Моника это признала.
        # Моника говорит что этим мужчиной будет управлять не так просто.
        # Мелани говорит что любым мужчиной управлять просто. Мужчины готовы идти на любые жертвы, воевать друг с другом.
        # Ради женщины. Им надо всего-лишь показать что Вы именно та женщина, ради которой стоит это делать.
        # Любой мужчина готов на все ради меня, Миссис Бакфетт.
        # Моника говорит что у нее тоже много поклонников.
        # Мелани спрашивает, почему тогда вы не попросите о помощи их?
        # Нет, Миссис Бакфетт. Вы не умеете управлять мужчинами.
        # Оставьте это мне. Так кто тот мужчина, с которым Вам никак не справиться?
        img 8717
        m "Видишь ли, Мелани."
        "Красота - это условная вещь."
        "Но в чем ты, Мелани, действительно разбираешься..."
        "Так это в том как управлять мужчинами..."
        img 8718
        melanie "Миссис Бакфетт, это очевидно. Я рада что Вы, наконец-то, это признали..."
        img 8719
        m "Но мужчиной, про которого я говорю, будет управлять не так просто."
        img 8720
        melanie "Миссис Бакфетт, любым мужчиной управлять просто."
        "Мужчины готовы идти на любые жертвы, воевать друг с другом."
        "Ради женщины..."
        img 8721
        "Им надо, всего-лишь, показать что Вы именно та женщина..."
        "Ради которой стоит это делать..."
        "..."
        "Любой мужчина готов на все ради меня, Миссис Бакфетт."
        img 8722
        m "У меня тоже много поклонников!"
        img 8723
        with fade
        w
        img 8724
        w
        img 8725
        melanie "Почему же тогда Вы не попросите помощи их?"
        img 8726
        mt "!!!"
        img 8727
        melanie "Нет, Миссис Бакфетт... Вы не умеете управлять мужчинами."
        "Оставьте это мне..."
        "Так кто тот мучжина, с которым Вам никак не справиться?"

        # Моника говорит что скажет если Мелани согласится помочь ей.
        # Мелани говрит что поможет, если Моника поучаствует в фотосессии с Мелани.
        # Биф хочет от нее какую-то пошлятину и Моника может помочь. Мелани не собирается задерживаться здесь, но хочет завершить подписанный контракт.
        # Моника спрашивает чем-же она может помочь в этом?
        # Мелани отвечает что там что поучаствует вместе с ней (улыбается)
        # Моника надменно улыбается, значит Биф от тебя что-то хочет? И почему-же ты не управляешь им, а?
        # Мелани отвечает что именно это она и делает (улыбается)
        img 8728
        m "Я скажу тебе если ты согласишься помочь мне!"
        $ ep23_dialogues5_2a_first_time = False
    else:
        img 8692
        m "Мелани... Я хочу поговорить с тобой..."
        melanie "Хорошо, Миссис Бакфетт."
        "Пройдемте в гримерную комнату."
        img 8713
        m "Я... про наш разговор..."
    img 8729
    melanie "Я помогу Вам, Миссис Бакфетт, если..."
    img 8730
    m "Если?"
    img 8731
    melanie "Если Вы поучаствуете со мной в фотосессии."
    melanie "Биф хочет от меня какую-то пошлятину и Вы можете помочь мне с этим."
    img 8732
    melanie "В любом случае я не собираюсь задерживаться здесь."
    melanie "Я лишь хочу завершить подписанный контракт."
    img 8733
    m "И чем-же я могу помочь тебе?"
    img 8734
    melanie "Тем что поучаствуете вместе со мной..."
    img 8735
    m "Значит Биф что-то требует от тебя?"
    "И почему-же ты не управляешь им, а?"

    img 8736
    melanie "Миссис Бакфетт... Я именно это и делаю..."
    img 8734
    melanie "Ну так что?"
    img 8737

    # Моника соглашается, либо нет. Если нет, то выход. Затем диалог короче.
    menu:
        "Хорошо, я согласна.":
            pass
        "Я не хочу участвовать в каких-то сомнительных фотосессиях.":
            img 8739
            m "Я не хочу участвовать в каких-то сомнительных фотосессиях."
            img 8734
            melanie "Значит мы отложим этот разговор..."
            return False

    # Моника говорит что согласна и спрашивает когда будет фотосессия.
    # Если соглашается, но фотосессия не открыта, то Мелани говорит что это запланировано после фотосессий с Вами.
    # Если открыто, то говорит что завтра вечером.
    # Моника думает что очередная глупая фотосессия, но ей надо добраться до Дика!
    # Далее в зависимости от того Моника сучка или нет, про себя ругается на Мелани что та сучка.
    img 8738
    m "Хорошо, Мелани..."
    "Я... Согласна сделать с тобой фотосессию..."
    "Когда она будет?"

    # Если фотосессия не открыта
    img 8740
    melanie "Насколько я знаю, до этого Биф запланировал некоторые фотосессии с Вами."
    "Сделайте их и мы начнем."
    help "Надо открыть остальные фотосессии перед съемками с Мелани."

    #Если открыто
    img 8740
    melanie "Это будет ближайшая фотосессия."
    "Вы можете узнать у Бифа."
    #

    img 8741
    mt "Итак... Очередная глупая фотосессия..."
    "Но я сделаю ее, мне надо добрться до Дика!"
    if monicaBitch == True:
        img 8742
        mt "Сучка Мелани! Ставит какие-то глупые условия мне!"
        "МНЕ, МОНИКЕ БАКФЕТТ! ЕЕ БОССУ!!!"
    return True

label ep23_dialogues5_2a:
    # Если Моника подходит к Мелани после этого, то Мелани отвечает когда будет фотосессия.
    img 8692
    m "Мелани, когда будет эта твоя фотосессия?"
    # Если фотосессия не открыта
    img 8693
    melanie "Насколько я знаю, до этого Биф запланировал некоторые фотосессии с Вами."
    "Сделайте их и мы начнем."
    help "Надо открыть остальные фотосессии перед съемками с Мелани."

    #Если открыто
    img 8693
    melanie "Это будет ближайшая фотосессия."
    "Вы можете узнать у Бифа."
    #
    return

label ep23_dialogues5_3:
    # ФОТОСЕССИЯ
    m "Что это за униформа, Алекс?"
    alex_photograph "Это униформа Стюардессы, Мэм!"
    m "Зачем это мне?"
    alex_photograph "Сегодня мы снимаем фотосессию для Fashion Airlines!"
    "Это крупная авиакомпания!"
    "И мы должны показать как авиакомпания и ее персонал относятся к клиентам!"
    m "И как они относятся?"
    alex_photograph "Они восхищаются ими, Миссис Бакфетт!"
    m "И кто будет в роли клиента?"
    melanie "В роли клиента буду я, Миссис Бакфетт..."
    mt "Как же могло быть иначе!"
    "Я с самого начала знала что эта фотосессия будет идиотской!!!"
    m "Ладно, Алекс..."
    "Только условие, никаких неприличных ракурсов!"
    alex_photograph "Конечно, Мэм!"
    "Вы же знаете, Мелани не согласится на неприличные ракурсы!"
    "Правда, Мелани?"
    melanie "Правда, Алекс..."
    alex_photograph "Итак, мотор!"

    m "Алекс, я не буду сниматься в таком ракурсе!"

    m "Алекс, даже не думай делать такой кадр!"

    # Алекс говорит встаньте в эту позу или в эту
    # Моника говорит комментарии что так снимать или не снимать
    # Если fail по corruption, то Мелани говорит с Моникой что фотосессия перенесена.
    # Пусть Моника приходит, когда будет более раскованна. Мелани это устраивает.
    # Моника думает что не Мелани говорить про раскованность. Это не ей приходится унижаться перед камерой!
    # Алекс подходит и говорит что мистер Биф недоволен тем что фотосессия сорвалась.
    # После фотосессии Моника может идти к Бифу на кастинг(?).

    # если fail по corruption
    m "Алекс, я не собираюсь вставать в эту позу!!!"
    "Даже не мечтай!"
    call ep23_dialogues5_3a() # прерывание фотосессии

    # Если фотосессия доходит до конца, то Алекс просит Моника сесть между ног Мелани и сделать вид,
    # что касается язычком ее киски в трусиках.
    # Объясняет это тем что это эротическая фотосессия в которой авиакомпания хочет показать что готова на все,
    # лишь бы ее клиенты остались довольны!

    # Если у Моники хорошие отношения с Мелани, то Моника может сказать Мелани что, пожалуйста,
    # скажи Алексу что хватит. Тогда Мелани говорит Алексу что в этом кадре нет необходимости и фотосессия завершается.
    # Мелани говорит на сцене Монике что будет ждать ее в гримерной комнате.
    alex_photograph "Миссис Бакфетт, пожалуйста, поместите голову Мелани между ног!"
    "И сделайте вид что Вы касаетесь язычком ее киски!"
    m "ЧТО?!?! АЛЕКС, ТЫ В СВОЕМ УМЕ?!?!"
    alex_photograph "Миссис Бакфетт, это эротическая фотосессия."
    "В ней авиакомпания хочет показать что готова на все, лишь бы ее клиенты остались довольны!"

    menu:
        "Прервать фотосессию.":
            return False
        "Сделать что просит Алекс.":
            pass
        "Попросить Мелани не делать этого (хорошие отношения с Мелани)": if melanieOffended2 == False and melanieOffended1 == False:
            m "Мелани, пожалуйста!"
            "Скажи Алексу что хватит!"
            melanie "Хорошо, Миссис Бакфетт..."
            melanie "Алекс, я думаю этого достаточно!"
            "Я ведь знаю что этот кадр твоя инициатива!"
            # конец фотосессии
        "Попросить Мелани не делать этого (плохие отношения с Мелани) (disabled)": if melanieOffended2 == True or melanieOffended1 == True:
            pass
    # Если Моника коснулась язычком трусиков, то после фотосессии Мелани говорит Монике что ей понравилось.
    # И не хочет-ли Миссис Бакфетт коснуться язычком без трусиков.
    alex_photograph "Мэм! Мы закончили фотосессию!"

    melanie "Миссис Бакфетт..."
    "А мне понравилась последняя поза..."
    "Не хотите-ли Вы коснуться меня язычком еще раз..."
    "Без трусиков..."

    # На что Моника категорически отвечает что нет, этого не будет никогда!
    # И пусть Мелани следит за своим языком и не забывает кто она и кто Моника!
    # Мелани многозначительно улыбается...
    # Хорошо, Миссис Бакфетт. Я буду ждать Вас в гримерной комнате.
    # Появляется вход в гримерную комнату.
    m "НЕТ, МЕЛАНИ!!!"
    "ЭТОГО НЕ БУДЕТ НИКОГДА!!!"
    "И следи за своим языком и не забывая КТО Я и КТО ТЫ!!!"
    melanie "..."
    melanie "Хорошо, Миссис Бакфетт. Я буду ждать Вас в гримерной комнате."
    return

label ep23_dialogues5_3a:
    #прерывание фотосессии
    melanie "Миссис Бакфетт. Вы прервали сессию."
    "Меня это вполне устраивает."
    "Может быть мой контракт закончится раньше, чем мы ее завершим."
    "В любом случае, Вы можете придти, когда будете более раскованны."
    mt "Не Мелани говорить про раскованность!"
    "Это не ей приходится унижаться перед камерой!"

    alex_photograph "Мистер Биф не будет доволен тем, что фотосессия сорвалась."
    return

label ep23_dialogues5_3b:

    # Там Мелани. С работы не выйти. Моника говорит что надо к Мелани.
    mt "Мне надо к Мелани!"
    return


label ep23_dialogues6:
    # Моника говорит Мелани что выполнила ее просьбу и теперь ее очередь.
    # Мелани улыбается и спрашивает так кто этот мужчина?
    # Моника говорит что это Дик Адвокат.
    # Мелани презрительно удивляется. Кто? Дик Адвокат? Этот толстячок?
    # Какие у Вас могли возникнуть проблемы с тем, чтобы добиться от него желаемого?
    # Моника молчит и зло смотрит.
    m "Мелани! Я выполнила твою просьбу! Теперь твоя очередь!"
    melanie "Так кто этот мужчина, Миссис Бакфетт?"
    m "Этот мужчина..."
    "Это..."
    "Это Дик Адвокат..."
    melanie "Пфи!! Кто???"
    "Дик Адвокат? Этот толстячок?"
    "Мэм, какие у Вас могли возникнуть проблемы с тем, чтобы добиться от него желаемого?"
    m "..."
    mt "!!!"

    # Мелани спрашивает так что мне надо от него получить?
    # Моника говорит что Дик занимается одним очень важным делом касаемо Моники.
    # Но у нее подозрение что необходимость в этом деле возникла по его же инициативе.
    # Что если бы не он, то у нее не возникло бы подобных трудностей.
    # Мелани спрашивает хорошо, мне надо только узнать информацию?
    # Моника говорит что не только. Там эта Виктория, его секретарша, она против того чтобы Дик помогал Монике в этом деле.
    # Значит из-за любви к ней Дик перестал помогать Вам?
    # Моника стеснительно отвечает что нет, не перестал, я договорилась с Викторией, временно.
    # Мелани удивленно: договорились? О чем? (улыбается)
    melanie "Так что мне надо от него получить?"
    m "Дик занимает одним очень важним делом, которое касается меня."
    "Но у меня стойкое подозрение что сама необходимость в этом деле возникла..."
    "По его же инициативе!"
    "И, если бы не он, то у меня не возникло бы подобных трудностей, какие есть сейчас."
    melanie "Хорошо, мне надо только узнать информацию?"
    m "Вообще, не только... Там еще есть Виктория, его секретарша..."
    "Она против того чтобы Дик помогал мне..."
    melanie "Значит из-за любви к ней Дик перестал помогать Вам?"
    m "Нет, Дик... он не перетсал помогать мне..."
    "Я договорилась с Викторией... временно..."
    melanie "Договорились? О чем?"

    # Моника отвечает что это неважно, может Мелани узнать что за всем этим стоит?
    # Мелани отвечает что это выглядит простым делом, но Миссис Бакфетт не забыла о награде, которую обещала?
    # Моника говорит что она поучаствовала с Мелани в этой жуткой фотосессии. Что же Мелани еще надо?
    # Мелани отвечает что она женщина, а женщина всегда хочет больше.
    # Моника говорит что если Мелани и правда поможет ей, то может рассчитывать на то что станет управляющей этого журнала.
    # Мелани отвечает: О! Да это и впрямь так важно для Вас, Миссис Бакфетт!
    # Хорошо, я проведаю этого Дика в ближайшее время.
    m "Это... Это неважно, Мелани!!!"
    m "Можешь просто узнать кто или что за всем этим стоит?"
    melanie "Знаете, Миссис Бакфетт... Это выглядит простым делом."
    "Но не забыли-ли Вы о награде, которую обещали?"
    m "Я уже приняла участие в той жуткой фотосессии!"
    "Что же тебе еще надо?!"
    melanie "Видите-ли, Миссис Бакфетт... Я - женщина."
    "А женшина всегда хочет больше..."
    m "Мелани!"
    "Если ты поможешь мне, то можешь рассчитывать на пост главного редактора этого журнала!"
    melanie "О! Да это и впрямь так важно для Вас, Миссис Бакфетт!"
    m "..."
    melanie "Хорошо, я проведаю этого Дика в ближайшее время."

    # Моника говорит что только опасайся Виктории. Эта сучка очень, очень опасна!
    # Мелани улыбается и говорит чтобы Миссис Бакфетт занималась своим делом. Кричала и командовала людьми.
    # А как найти подход к мужчине, Мелани знает лучше. Ей доставит удовольствие сделать то, что не получилось сделать у самой Моники Бакфетт.
    # И ее очень привлекает то, что Моника будет благодарна Мелани за это. Это очень поможет моей карьере.
    # Ждите новостей, Миссис Бакфетт.
    m "Только будь аккуратна с Викторией. Эта сучка очень, ОЧЕНЬ опасна!"
    melanie "Миссис Бакфетт, Вам стоит заниматься своим делом, которое у Вас получается очень хорошо."
    "Это кричать и командовать людьми."
    "Но я знаю лучше Вас как найти подход к мужчине."
    "И мне доставит удовольствие сделать то, что не получилось сделать у самой Моники Бакфетт!"
    melanie "И меня очень привлекает то, что Вы будете должны мне."
    "Это очень поможет моей карьере..."
    m "..."
    melanie "Ждите новостей, Миссис Бакфетт!"

    # Моника думает ну все. Держись сучка Виктория. Я нашла кое-кого кто тебе не по зубам!
    mt "Ну все!!!"
    if monicaBitch == True:
        "Ну держись, сучка Виктория!"
    else:
        "Ну держись, Виктория!"
    "Я нашла кое-кого кто тебе не по зубам!"
    return
































#
