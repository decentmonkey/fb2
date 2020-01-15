label ep27_dialogues6_julia0:
    menu:
        "Отношения с Юлией..." if juliaQuestLastDay != day and e210_quests_julia_aborted == False:
            return 3
        "Отношения с Юлией... (disabled)" if (juliaQuestLastDay == day and juliaQuestStage0_Progress > 0):
            pass
        "Заставить Юлию собрать отчеты вместо Моники." if monicaWorkFlashCardQuestActive == True and monicaWorkFlashCardNeedReportsAmount > monicaWorkFlashCardReportsCollected and monicaWorkFlashCardReportLastDay != day:
            return 2
        "Юлия, что там с отчетами, которые надо обработать сегодня?":
            return 1
        "Уйти.":
            return False
    return

label ep27_dialogues6_julia0b:
    menu:
        "Юлия... Ты сегодня хорошо выглядишь..." if juliaQuestStage0_Progress >= 1:
            return 1
        "Юлия, ты красивая девушка и мне нравится твоя прическа..." if juliaQuestStage0_Progress >= 2:
            return 2
        "Сделать Юлии комплимент по поводу ее фигуры." if juliaQuestStage0_Progress >= 3:
            return 3
        "Поцеловать Юлию." if juliaQuestStage0_Progress >= 4:
            return 4
        "Ущипнуть Юлию за зад." if juliaQuestStage0_Progress >= 5:
            return 5
        "Выяснить, какого цвета трусики на Юлии сегодня" if juliaQuestStage1_Progress > 0 and juliaQuestMonicaRefusedFred == False:
            return 6
        "Уйти.":
            return 0
    return


label ep27_dialogues6_julia1:
# Моника может говорить Юлии собрать отчеты
# Юлия, вот тебе флеш карта. Быстро собери отчеты у каждого из этих никчемных работников!
    # Моника подходит, Юлия испуганно смотрит на Монику
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20791
    with fade
    m "Юлия, вот тебе флеш карта."
    sound highheels_run2
    img 20792
    with diss
    m "Быстро собери отчеты у каждого из этих никчемных работников!"
    julia "Да, Миссис Бакфетт, я сейчас все сделаю!"

    # несколько минут спустя
    sound highheels_run1
    music stop
    call textonblack(_("Спустя некоторое время...")) from _call_textonblack_29
    img black_screen
    with Dissolve(1)
    music Groove2_85
    # Моника сидит в кресле
    img 20793
    with fadelong
    julia "Вот, Миссис Бакфетт."
    julia "Я собрала отчеты у всех сотрудников."
    menu:
        "Ты долго делала это, могла бы быстрее!":
            music Pyro_Flow
            img 20794
            with fade
            m "Ты долго делала это, могла бы быстрее!"
            img 20795
            with diss
            julia "..."
            if juliaOfficeOffended2 == False:
                $ juliaOfficeOffended2 = True
                $ juliaOfficeOffendedDay = day
            call bitch(10, "ep27_dialogues6_julia1_1") from _call_bitch_199
        "Хорошо, Юлия.":
            m "Хорошо, Юлия. Спасибо."
            img 20796
            with diss
            julia "Да, Миссис Бакфетт, пожалуйста."
            call bitch(-10, "ep27_dialogues6_julia1_1") from _call_bitch_200
    return

label ep27_dialogues6_julia2:
# После того, как все отчеты сняты, время дня меняется на вечер и Моника комментирует что теперь можно отнести отчеты секретарше.
# Выход из офиса блокируется (entrance), пока отчеты не сданы.
    mt "Все отчеты собраны."
    mt "Теперь можно отнести их моей секретарше."
    return

label ep27_dialogues6_julia3b:
    # Моника пытается выйти из офиса до того как сдала собранные отчеты
    mt "Мне надо сдать отчеты моей секретарше."
    return


# Набор евентов с Юлией и Фредом в офисе.

label ep27_dialogues6_julia3:
# Начало после того как Моника отдаст первый отчет Бифу
# После нажатия начать работу появляется Фред.
# Фред говорит Монике какая встреча, Миссис Бакфетт.
# Рад видеть Вас в кресле Босса.
# Юлия смотрит с удивлением.
    music Hidden_Agenda
    img 20797
    with fadelong
    w
    music stop
    sound plastinka2
    img 20798
    with hpunch
    mt "ФРЕД?!"
    music Groove2_85
    img 20799
    with fade
    fred "О, какая встреча, Миссис Бакфетт."
    fred "Рад видеть Вас в кресле Босса."
    music Hidden_Agenda
    img 20800
    with diss
    julia "???"

# Моника говорит Фреду что он делает здесь?!
# Фред отвечает что он работает в этой компании, поэтому это странный вопрос. И непрофессиональный.
# Моника говорит что его профессионализм не должен выходить за пределы рулевого колеса.
# Моника строго спрашивает у Юлии не пришел-ли Фред к ней?
# Юля смущается.
    music Pyro_Flow
    img 20801
    with fade
    m "Фред, что ты делаешь здесь?!"
    img 20802
    with diss
    fred "Миссис Бакфетт, я работаю в этой компании, поэтому Ваш вопрос звучит странно."
    fred "И непрофессионально."
    img 20803
    with fade
    m "Твой профессионализм не должен выходить за пределы рулевого колеса, Фред!"
    m "Что ты здесь делаешь, спрашиваю еще раз!"
    img 20804
    with diss
    m "Юлия, он что, пришел к тебе?!"
    img 20805
    with diss
    julia "..."
# Фред говорит что, если говорить о сферах профессионализма, то, возможно, кое-кому стоит ограничиться обязанностями гувернантки.
# А работа Боссом может выходить за профессиональные рамки основной профессии.
# Юлия смотрит на Фреда
# Фред смотрит на Монику улыбаясь
# Моника смотрит напряженно на Фреда и на Юлию
# Моника говорит Юлии, чтобы она вышла из кабинета, быстро.
    music Groove2_85
    img 20806
    with fade
    fred "Миссис Бакфетт."
    fred "Если говорить о сферах профессионализма, то, возможно, кое-кому стоит ограничиться обязанностями гувернантки."
    fred "А работа Боссом при этом - это выход за профессиональные рамки основной профессии."
# Юлия смотрит на Фреда
    music Master_Disorder
    img 20807
    with diss
    julia "???"
# Фред смотрит на Монику улыбаясь
    img 20808
    with diss
    m "!!!"
    img 20809
    with diss
    fred "..."
# Моника смотрит напряженно на Фреда и на Юлию
    img 20810
    with diss
    m "..."
# Моника говорит Юлии, чтобы она вышла из кабинета, быстро.
    music Power_Bots_Loop
    img 20811
    with fadelong
    m "Юлия, выйди из кабинета."
    m "Быстро!"

# Юлия выходит
    img 20812
    with diss
    julia "..."

    # затемнение

# Моника говорит Фреду не слишком-ли тот зарывается
# Добавляет (если ударила его рукой или ногой) мало-ли ему показалось в прошлый раз?
# Фред отвечает, что усвоил то, что Монику лучше не трогать и не принуждать к чему-то силой.
# Это опасно
# Моника отвечает что рада что Фред это понимает.
    sound highheels_run2
    music stop
    img black_screen
    with diss
    pause 1.5
    sound snd_door_close1
    music Pyro_Flow
    img 20813
    with fadelong
    m "Фред, не слишком-ли ты нарываешься?!"
    # если била его рукой или ногой
    if fredKickedByMonicaToBalls == True or fredKickedByMonicaToFace == True:
        m "Тебе что, в прошлый раз показалось мало?!"
    #
    music Groove2_85
    img 20814
    with diss
    fred "Миссис Бакфетт, я усвоил то, что Вас лучше не трогать и не принуждать к чему-либо силой."
    fred "В вашем случае это опасно."
    img 20815
    with diss
    m "Я рада что ты, Фред, это понимаешь."

# Фред отвечает, что гораздо безопаснее, если Моника сделает это сама.
# Моника злится и спрашивает что Фред имеет ввиду?
# И говорит что не собирается спать с Фредом ни за что!
# Фред говорит что насчет попки Миссис Бакфетт у него отдельные планы.
# Они связана с попками Стефани и Ребекки, если Моника помнит...
    img 20816
    with fade
    fred "Гораздо безопаснее, Миссис Бакфетт, если Вы сделаете это сами..."
    music Power_Bots_Loop
    img 20817
    with hpunch
    m "!!!"
    img 20818
    with diss
    m "Что ты имеешь ввиду, Фред?!"
    m "Если ты рассчитываешь на то, чтобы я спала с тобой, то можешь даже не надеяться!"
    m "Я не пойду на это ни за что!"
    music Groove2_85
    img 20819
    with fade
    fred "О, Миссис Бакфетт, насчет Вашей попки у меня отдельные планы."
    img 20820
    with diss
    fred "Они также связаны с попками Стефани и Ребекки, если Вы помните..."
# Моника зло отвечает Фред...
# Фред говорит что Миссис Бакфетт хороший Босс.
# А у хорошего Босса не должно быть секретов от своих подчиненных.
# Это непрофессионально.
# Моника спрашивает на что Фред намекает
    music Master_Disorder
    img 20821
    with diss
    mt "!!!"
    m "Фред..." # Шипит убийственно
    music Groove2_85
    img 20822
    with fade
    fred "Миссис Бакфетт, Вы хороший Босс."
    fred "А у хорошего Босса не должно быть секретов от своих подчиненных."
    fred "Это непрофессионально."
    img 20823
    with diss
    m "На что это ты намекаешь, Фред?!"
# Фред отвечает что считает профессиональным долгом рассказать всему коллективу о том, что их Босс имеет основную работу.
# Гувернантки.
# Моника злится
    img 20824
    with diss
    fred "Миссис Бакфетт, я считаю профессиональным долгом рассказать всему коллективу о том, что их Босс имеет основную работу..."
#    music stop
    img 20825
    fred "Гувернанткой." # вблизи улыбается
    music Master_Disorder
    img 20826
    with hpunch
    m "!!!" # Моника в ярости
# Если уровень Барди низкий, то говорит что гувернантки, которая носит трусики Юлии, потому что у нее нет других.
# (если уровень не выше далее) И она теперь трет пятно на ковре в своем доме, сверкая Юлиными трусиками каждый день.
# Если уровень Барди выше (?), то говорит что гувернантки, которая носит трусики своей новой хозяйки, которые та носила за день до этого
# (если уровень не выше далее) И она теперь трет пятно на ковре в своем доме, сверкая разными трусиками каждый день.
# Если уровень Барди выше (?), то говорит, но которой, в конце концов, вообще запретили носить трусики
# И она теперь трет пятно на ковре без трусиков, сверкая своей очаровательной попой.

    if char_info["Bardie"]["level"] < 3:
        img 20827
        with diss
        fred "Гувернанткой, которой приходится носить трусики Юлии, потому что у нее нет других."
        img 20828
        with diss
        fred "Или, может быть, ей нравится это..."
        img 20830
        with diss
        fred "И она теперь трет пятно на ковре в своем доме, сверкая Юлиными трусиками каждый день."
    else:
        if char_info["Bardie"]["level"] < 5:
            img 20827
            with diss
            fred "Гувернанткой, которая носит трусики Юлии, а также трусики своей новой хозяйки."
            img 20828
            with diss
            fred "Которые та носила за день до этого."
            img 20830
            with diss
            fred "И она теперь трет пятно на ковре в своем доме, сверкая то Юлиными трусиками, то трусиками хозяйки каждый день."
        else:
            img 20827
            with diss
            fred "Гувернанткой, которая носила трусики Юлии, а затем трусики новой хозяйки дома."
            img 20828
            with diss
            fred "Которые та носила за день до этого."
            fred "И она терла пятно на ковре в своем доме, сверкая то Юлиными трусиками, то трусиками хозяйки каждый день."
            img 20829
            with diss
            m "!!!"
            fred "А затем ей вообще запретили носить трусики."
            img 20830
            with diss
            fred "И она теперь трет пятно на ковре без трусиков, сверкая своей очаровательной попой."

# Я люблю смотреть на Вашу попу, Миссис Бакфетт, когда Вы трете пятно...
    music Groove2_85
    img 20831
    with fade
    fred "Я люблю смотреть на Вашу попу, Миссис Бакфетт."
    fred "Когда Вы трете то пятно..."
# Моника !!!
# Ты не расскажешь этого никому!
# Почему-же? Ваше фото и видео того, как Вы трете пятно, понравится всем в этом отделе.
# Моника отвечает у тебя не фото и видео этого, ты лжешь!
# Фред отвечает что нет, но он может сделать их в любое время, например завтра.
# Или послезавтра. Ведь Моника не будет уклоняться от обязанностей по дому, правда?
# Моника злится!
    music Power_Bots_Loop
    img 20832
    with hpunch
    m "!!!" # Моника в ярости
    img 20833
    with fade
    m "Ты не расскажешь этого никому!" # шипит
    fred "Почему-же?"
    fred "Ваше фото и видео того, как Вы трете пятно, понравится всем в этом отделе."
    img 20834
    with vpunch
    m "У тебя нет ни фото, ни видео этого!"
    m "Ты лжешь!"
    img 20835
    with diss
    fred "Вы правы, у меня этого нет."
    fred "Но я могу сделать их в любое время."
    fred "Например, завтра."
    fred "Или послезавтра."
    img 20836
    with diss
    fred "Ведь Вы стараетесь быть хорошей гувернанткой и не будете уклоняться от обязанностей по дому, правда?"
    fred "В конце концов, я за Вас поручился перед Мистером Робертсом."
    img 20837
    with diss
    m "!!!"

# Особенно это видео понравится Юлии.
# Я, пожалуй, покажу его ей первой.
# Моника отвечает: Фред, мерзавец. Ты всегда пользуешься ситуацией в свою пользу.
# ...
# Ты говорил что у тебя другие планы... насчет меня...
# Что ты хочешь сейчас? Ведь ты меня просто шантажируешь, я знаю.
# Ты не станешь никому рассказывать про то что я делаю в своем доме.
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 20838
    with fadelong
    fred "Особенно это видео понравится Юлии."
    m "!!!"
    img 20839
    with diss
    fred "Я, пожалуй, покажу ей эти видео-материалы первой."
    sound snd_door_open1
    img 20840
    with fadelong
    sound highheels_run2
    w1 "Миссис Бакфетт, можно войти?"
    music Power_Bots_Loop
    img 20841
    with vpunch
    m "Вон отсюда!"
    # убегает темнота
    music stop
    img black_screen
    with diss
    sound highheels_run1
    pause 1.5
    music Groove2_85
    img 20842
    with fadelong
    m "..."
    m "Фред, мерзавец..."
    m "Ты всегда пользуешься ситуацией в свою пользу."
    img 20843
    with diss
    fred "..." # Улыбается
    music Hidden_Agenda
    img 20844
    with fade
    m "..."
    m "Ты говорил что у тебя другие планы... насчет меня..."
    m "Что ты хочешь сейчас?"
    m "Ведь ты меня просто шантажируешь, я знаю."
    m "Ты не станешь никому рассказывать про то что я делаю в своем доме."

# Фред отвечает что это сущая мелочь.
# Фред уважает Миссис Бакфетт как Босса и как профессионала и хочет, чтобы та просто вела себя более вежливо по отношению к Юлии.
# Моника отвечает что и так ведет себя по отношению к Юлии как того требует профессиональная этика.
# Фред отвечает что Юлия хрупкая и ранимая девушка и ей не помешало бы побольше нежности от такого строгого Босса как Моника.
# Скажите Юлии в следующий раз, что она хорошо выглядит сегодня.
    img 20845
    with diss
    fred "О, Миссис Бакфетт, мне нужна сущая мелочь."
    fred "Я уважаю Вас как Босса и как профессионала."
    fred "И я хочу, чтобы Вы просто вели себя более вежливо по отношению к Юлии."
    img 20846
    with fade
    m "Я и так веду себя по отношению к Юлии так, как того требует профессиональная этика."
    img 20847
    with diss
    fred "Да, но Юлия хрупкая и ранимая девушка."
    fred "И ей бы не помешало побольше нежности от такого строгого Босса как Вы, Миссис Бакфетт."
    img 20848
    m "???"
    img 20849
    with diss
    fred "Скажите Юлии, что она хорошо выглядит сегодня."

# Моника отвечает что не понимает зачем?
# Фред отвечает что Вы скажете это, иначе Ваше профессиональные тайны станут достоянием общественности.
# Моника злится и спрашивает когда она должна это сделать?
# Фред отвечает что завтра или в ближайшее время.
# Моника спрашивает и как ты узнаешь что я это сделала.
# Фред говорит что общается с Юлей и что Юля расскажет об этом непременно.
    music Groove2_85
    img 20850
    with fade
    m "Я не понимаю, зачем мне это говорить?"
    m "Она всего-лишь работник, а я ее Босс!"
    fred "Вам придется это сказать, Миссис Бакфетт."
    fred "Иначе Ваши профессиональные тайны станут достоянием общественности."
    img 20851
    with diss
    m "!!!"
    img 20852
    with diss
    fred "..." # Улыбается
    img 20853
    with fade
    m "Ладно..."
    m "Когда я должна это сделать?"
    fred "Сделайте это завтра или в ближайшие дни."
    m "И как ты узнаешь что я это сделала?"

    img 20854
    with diss
    if juliaHasSexInPool == True:
        # Если Юлия спала с фредом
        $ notif(_("Юлия имела секс с Фредом."))
        fred "Юлия иногда доверяется моему... профессиональному мнению."
    else:
        # Юлия не имела секса с Фредом
        $ notif(_("Юлия не имела секс с Фредом."))
        fred "Юлия немного стесняется меня, но иногда спрашивает моего совета."
        fred "Дополнительное доверие ко мне поможет ей расслабиться в будущем."
    #

# Выбор
# Я подумаю над этим.
# Моника отвечает что подумает над этим.
# Фред уходит, говоря что подумайте, Миссис Бакфетт.
    img 20851
    with diss
    menu:
        "Я подумаю над этим.":
            pass
        "Прогнать Фреда (пропуск событий с Юлией).":
# Либо:
# Прогнать Фреда
# Моника говорит Фреду чтобы он убирался со своими мелкими шантажами!
# И, если хоть что-то просочится сюда про нее, то она оторвет ему яйца.
# Жаль что не сделал этого в прошлый раз!
# Фред говорит что мы еще обсудим это, Миссис Бакфетт и уходит.
# В таком случае квест скипается
            music Power_Bots_Loop
            img 20855
            with fade
            m "Фред, лучше убирайся со своими мелкими шантажами!"
            m "Предупреждаю!"
            img 20856
            with diss
            m "Если хоть что-то просочится в эти стены про то, что я делаю в своем доме..."
            m "Я оторву тебе яйца, клянусь!" # злая близко
            # Если Моника била Фреда в фитнес зале
            if fredKickedByMonicaToBalls == True or fredKickedByMonicaToFace == True:
                m "Жаль что я не сделала этого в прошлый раз в раздевалке фитнес зала!"
            return False

# Проходит рабочий день.
    m "Я подумаю над этим."
    img 20852
    with diss
    fred "Я буду держаться в курсе, Миссис Бакфетт..."
    return True


label ep27_dialogues6_julia4:
# В конце рабочего дня Моника думает о том что Фред от нее хочет.
# Этот мерзавец тоже начал шантажировать ее.
# В этом мире трудно жить такой доброй Леди как она, потому что все мерзавцы этого мира пытаются использовать ее.
# Но ничего, она скоро вернет все назад и сделает Фреда бездомным.
# Но а пока, ей придется сказать Юлии то что он попросил ее.
# В конце концов, это не так уж и сложно.
# Сделаю это завтра днем.
# Либо можно потянуть время. Фред сказал что я могу подумать.
    mt "Фред - еще один мерзавец, который принялся шантажировать меня!"
    mt "В этом мире трудно жить такой доброй и порядочной Леди как Я."
    mt "Все мерзавцы этого мира пытаются использовать меня."
    mt "В отличие от них, я никогда не использовала власть для того, чтобы унизить кого-то!"
    mt "..."
    mt "Но ничего, скоро я верну все назад и сделаю Фреда бездомным!"
    mt "Ну а пока..."
    mt "Пока, возможно, мне придется сказать Юлии те слова, что он просил."
    mt "В конце концов, это не так уж и сложно."
    mt "Сделаю это {c}завтра днем{/c}."
    mt "Либо можно {c}потянуть время{/c}."
    mt "Фред сказал что я могу подумать."

# Появляется квестлог о том, что Фред просит говорить Юлии какие-то странные слова.
# Ей приходится делать это, либо она может потянуть время.
    return

label ep27_dialogues6_julia4a:
    mt "Фред - еще один мерзавец, который принялся шантажировать меня!"
    return

label ep27_dialogues6_julia5:

# Появляется пункт сказать Юлии что она сегодня хорошо выглядит
# Моника говорит Юлии что та хорошо выглядит сегодня
# Юлия удивленно смотрит на Монику и говорит спасибо
# Это действие добавляет уровень у Юлии
    music Hidden_Agenda
    img 20877
    with fade
    m "Юлия... Ты сегодня хорошо выглядишь..."
    julia "???"
    music Groove2_85
    img 20881
    with diss
    m "..." # Надменно
    img 20880
    with fadelong
    julia "Ссс... Сссспасибо... Миссис Бакфетт..."
# Это действие добавляет уровень 1 у Юлии
    return

label ep27_dialogues6_julia6:
# На следующий день в working_office Монику встречает Фред
# Говорит Монике что Вы прекрасно справились.
# Сегодня Вы скажете что Юлия очень красивая девушка и ей нравится ее прическа
# Моника спрашивает зачем мне говорить это.
# Фред отвечает что Моника знает зачем, чтобы не случилось кое-чего, чего Моника не хочет
# Моника отвечает что подумает
    music Groove2_85
    img 20857
    with fade
    fred "Миссис Бакфетт."
    m "Фред... Мерзавец..."
    m "Зачем ты подкараулил меня здесь?"
    m "Я сделала как ты просил!"
    m "Что тебе снова надо?"
    fred "Миссис Бакфетт, Вы прекрасно справились."
    music Hidden_Agenda
    img 20858
    with diss
    m "Тише!"
    img 20857
    with diss
    fred "Сегодня Вы скажете что Юлия очень красивая девушка и Вам нравится ее прическа."
    img 20858
    with diss
    m "Зачем мне говорить это? С какой стати?!"
    music Groove2_85
    img 20857
    with fade
    fred "Миссис Бакфетт, Вы знаете зачем."
    fred "Чтобы не случилось кое-что, чего Вы бы не хотели чтобы случилось..."
    img 20859
    with diss
    m "!!!"
    m "Я подумаю..."
    return

label ep27_dialogues6_julia7:
# Появляется пункт сказать Юлии что Монике нравится ее прическа
# Моника говорит Юлии что она красивая девушка и Моника нравится ее прическа.
# Юлия странно смотрит на Монику с удивлением.
# И говорит спасибо, Миссис Бакфетт. У Вас тоже очень красивые волосы.
# Моника отвечает надменно что она знает об этом.
# Это действие добавляет уровень у Юлии
    music Hidden_Agenda
    sound highheels_short_walk
    img 20875
    with fade
    w
    img 20876
    with diss
    w
    img 20877
    with fade
    m "Юлия, ты..."
    img 20878
    with diss
    julia "Да, Миссис Бакфетт?"
    img 20879
    with fade
    m "Юлия... Ты... Ты красивая девушка."
    sound Jump2
    img 20880
    with vpunch
    julia "..."
    img 20881
    with fade
    m "И... И мне нравится твоя прическа."
    sound Jump1
    img 20882
    with diss
    julia "..." # ошарашена и странно смотрит
    music Groove2_85
    img 20883
    with fade
    m "..." # надменно
    img 20884
    with diss
    julia "Спасибо, Миссис Бакфетт."
    julia "У Вас тоже очень красивые волосы."
    img 20885
    with diss
    m "Спасибо, но я и так знаю это!" # Надменно отвечает и уходит
    sound highheels_short_walk
# Это действие добавляет уровень 1 у Юлии
    return


label ep27_dialogues6_julia8:
# На следующий день в фотостудии Монику встречает Фред
# Говорит Монике что Вы прекрасно справились.
# Сегодня Вы скажете Юлии что у нее сексуальная фигура.
# Затем попросите повернуться спиной и сказать что у нее красивая попа.
# Моника говорит что она так не считает, с какой стати ей говорить это Юлии?
# Юлия обычная бездарность, у которой фигура не сравнится с фигурой Моники.
# Фред говорит что если Моника не оценит фигуру Юлии, то весь отдел оценит фигуру Моники в позе гувернантки, трущей пятно.
# Моника злится и уходит.
    music Groove2_85
    img 20860
    with fadelong
    fred "..." # Улыбается
    m "Снова ТЫ!"
    m "Не даешь переодеться нормально! Все вынюхиваешь здесь!"
    img 20861
    with diss
    fred "Миссис Бакфетт, Вы снова прекрасно справились!"
    fred "Сегодня Вы скажете Юлии что у нее сексуальная фигура и грудь."
    fred "Затем попросите повернуться ее спиной и сказать что у нее красивая попа."
    fred "Вы должны произнести именно эти слова!"
    img 20860
    with fade
    m "Я не считаю ее фигуру красивой, а тем более сексуальной!"
    m "С какой стати мне говорить это ей?!"
    m "Юлия - обычная бездарность, у которой фигура не сравнится с моей!"
    img 20861
    with diss
    fred "Миссис Бакфетт..."
    fred "Если Вы не оцените фигуру Юлии, то весь отдел оценит Вашу прекрасную фигуру в позе гувернантки, трущей пятно."
    img 20862
    with diss
    m "!!!"
    return

label ep27_dialogues6_julia9:
# Появляется выбор сказать Юлии комплимент по поводу тела.
# Моника сидит за креслом и зовет Юлию, чтобы та подошла к Монике
# Юлия подходит
# Моника напрягается и смотрит на Юлию
# Юлия вопросительно смотрит на Монику
# Моника говорит Юлии что у нее красивая фигура и Монике нравится ее грудь.
# Юлия очень удивленно смотрит на Монику и молчит
# Моника говорит Юлии, чтобы та повернулась спиной к ней
    music Groove2_85
    img 20886
    with fadelong
    w
    img 20887
    with diss
    m "Юлия, подойди ко мне!"
# Юлия подходит
    sound highheels_short_walk
    img 20888
    with fadelong
    julia "Да, Миссис Бакфетт?" # немного испуганно
    img 20889
    with diss
    m "..."
    img 20890
    with diss
    julia "..." # вопросительно
    music Hidden_Agenda
    img 20891
    with fade
    m "Юлия..."
    img 20892
    with diss
    m "Юлия, у тебя красивая фигура и мне нравится твоя грудь."
    sound Jump1
    img 20893
    with vpunch
    julia "..." # Юлия очень удивленно смотрит на Монику и молчит
    music Groove2_85
    img 20894
    with fade
    m "А теперь повернись ко мне спиной!" # жестко

# Юлия поворачивается
# Моника говорит что у Юлии также красивая попа и что она нравится МОнике
# Юлия ошарашенно смотрит на Монику
# Моника зло смотрит на Юлию
# Юлия отвечает Сссспасибо, Миссис Бакфетт.
# Для меня это неожиданно. Я могу идти на свое рабочее место?
# Моника говорит что да, она может идти
# Это действие добавляет уровень у Юлии
    img 20895
    with diss
    julia "???"
    img 20896
    with diss
    m "!!!"
    music Hidden_Agenda
    img 20897
    with fade
    w
    img 20898
    with diss
    w
    img 20899
    with diss
    w
    img 20900
    with fade
    m "У тебя также красивая попа и она также нравится мне."
    sound Jump2
    img 20901
    with vpunch
    julia "!!!" # Юлия ошарашенно смотрит на Монику
    music Groove2_85
    img 20902
    with fade
    m "!!!" # Моника зло смотрит на Юлию
    img 20903
    with fade
    julia "Ссссс... Сссспасибо, Миссис Бакфетт..."
    julia "Для меня это неожиданно..."
    img 20904
    with diss
    julia "Я могу идти на свое рабочее место?"
    img 20905
    with diss
    m "Да, Юлия, ты можешь идти!"
# Это действие добавляет уровень 1 у Юлии
    return

label ep27_dialogues6_julia10:
# На следующий день в entrance Монику встречает Фред
# Говорит Монике что Вы прекрасно справились.
# Сегодня Вы поцелуете Юлию, можно в щеку
# Моника отвечает ЧТОООО???
# Я не собираюсь делать этого.
# Фред отвечает что в этом нет ничего особенного, зато что-то особенное может случиться, если она этого не сделает.
# До встречи, Миссис Бакфетт.
    music Groove2_85
    img 20870
    with fadelong
    m "Фред! Хватит преследовать меня!"
    fred "Миссис Бакфетт, Вы снова справились на отлично."
    m "Тише!"
    img 20871
    with diss
    fred "Сегодня Вы поцелуете Юлию."
    fred "Можно в щеку."
    music Power_Bots_Loop
    img 20872
    with vpunch
    m "ЧТООООО???"
    m "Я не собираюсь делать этого!!!"
    music Groove2_85
    img 20873
    with diss
    fred "Миссис Бакфетт, в этом нет ничего особенного."
    fred "Зато что-то особенное может случиться, если Вы не сделаете этого..."
    m "!!!"
    fred "До встречи, Миссис Бакфетт..." # уходит
    music stop
    img black_screen
    with diss
    sound man_steps
    pause 1.5
    music Sneaky_Snitch
    img 20874
    with fadelong
    w5 "Миссис Бакфетт, это Ваш водитель?"
    w5 "Хотите я предложу ему тоже кофе?"
    if monicaBitch == True:
        $ notif_monica()
        m "Да, это мой водитель!"
        m "И моя прислуга не нуждается в кофе!"
    m "Иди работай!"
    w5 "Хорошо, Миссис Бакфетт. Вы всегда можете рассчитывать на меня."
    return

label ep27_dialogues6_julia10a:
    # говорит после Фреда
    m "ФРЕД!!!"
    m "Мерзавец..."
    m "Ненавижу его..."
    return


label ep27_dialogues6_julia11:
# Появляется вариант поцеловать Юлию
# Моника подходит к Юлии
# Юлия встает и говорит чем она может помочь?
# Моника говорит сядь и сиди работай, я просто хочу проверить как ты работаешь
# Юлия отвечает да, конечно и садится
# Моника встает сзади и смотрит
    music Groove2_85
    sound highheels_short_walk
    img 20906
    with fadelong
    w
    sound desk_open
    img 20907
    with diss
    julia "Миссис Бакфетт, чем я могу помочь Вам?"
    music Hidden_Agenda
    sound highheels_short_walk
    img 20908
    with fade
    m "Юлия, сядь и сиди работай."
    m "Я просто хочу проверить как ты работаешь."
    img 20909
    with diss
    julia "Да, конечно, Миссис Бакфетт."
    julia "Как скажете."
    sound desk_open
    img 20910
    with fade
    m "..."
# Выбор:
# Поцеловать Юлию
# Не целовать.
# Нет, я не могу зайти настолько далеко. Все-таки, я Босс!
    img 20911
    with diss
    $ menu_corruption = [juliaMonicaKissCorruptionRequired]
    menu:
        "Поцеловать Юлию.":
            pass
        "Не целовать.": #corruption
            music Groove2_85
            img 20912
            with fade
            mt "Нет, я не могу зайти настолько далеко."
            mt "Все-таки, я Босс!"
            return -1

# Если поцеловать:
# Моника нагибается и пытается поцеловать Юлию
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    img 20913
    with fadelong
    w
    img 20914
    with diss
    w
    img 20915
    with diss
    w
    img 20916
    with diss
    w
    img 20917
    with diss
    w
    img 20918
    with diss
    w
# Если уровень не 2, то Юлия уворачивается и говорит: Миссис Бакфетт, что Вы собираетесь сделать?!
    if char_info["Julia"]["level"] < 2:
        sound Jump1
        music Power_Bots_Loop
        img 20919
        with hpunch
        julia "Миссис Бакфетт, что Вы собираетесь сделать?!"
# Моника говорит что ничего (смущенно) и уходит.
# Появляется сообщение что Юлия должна быть ур.2
        img 20920
        with fade
        m "Ничего!" # смущенно и уходит
        $ notif(_("Требуется отношения с Юлией ур.2"))
        music stop
        img black_screen
        with diss
        sound highheels_run2
        pause 1.5
        music Power_Bots_Loop
        img 20921
        with fadelong
        mt "Гребаный Фред!"
        mt "Я чувствую себя полной дурой!"
        return -2

# Если уровень 2, то Моника быстро целует Юлию в щечку
# Юлия в шоке
# Спрашивает Миссис Бакфетт, что это было?
# Моника отвечает что ничего.
    sound snd_kiss2
    img 20922
    with diss
    m "(чмок)" #звук
    img 20924
    with diss
    w
    sound snd_kiss3
    img 20923 #чмок звук снова
    with hpunch
    julia "!!!"
    music Groove2_85
    img 20925
    with fade
    m "..."
    julia "Миссис Бакфетт, что это было?"
    img 20926
    with diss
    m "Ничего..." # уходит в кресло

# Моника садится в кресло.
# Моника сидит и смотрит в сторону гордо и надменно (думает гребаный фред)
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 1.5
    music Groove2_85
    img 20921
    with fadelong
    mt "Гребаный Фред!"
    mt "Я чувствую себя полной дурой!"
# Юлия ошарашенно продолжает сидеть и смотреть на Монику

# Это добавляет прогресс к ур.2
    return

label ep27_dialogues6_julia11a:
    mt "Гребаный Фред!"
    mt "Я чувствую себя полной дурой!"
    return

label ep27_dialogues6_julia12:
# На следующий день в entrance Монику встречает Фред
# Говорит Монике что Вы прекрасно справились.
# Сегодня Вы можете говорить с Юлией о чем хотите, но Вы должны ущипнуть ее за попу.
# Моника злится на Фреда. К чему ты клонишь, Фред?!
# Я не какая-нибудь лесбиянка! Я леди и я твой Босс, не забывай этого!
# Фред отвечает что не будет ничего страшного, если женщина Босс ущипнет за попу свою подчиненную.
# Это одинаковый пол, поэтому это не будет считаться харрасментом и будет вполне профессионально.
# Однако, если Моника этого не сделает, то отдел скоро увидит фото как их Босса щипает за задницу Фред в то время, когда она трет пятно.
# Моника говорит Фреду что убьет его.
# Фред отвечает что он профессионал и нет необходимости убивать его.
# Просто сделайте что я прошу.
# Моника злится
    music stop
    img black_screen
    with diss
    pause 1.5
    music Power_Bots_Loop
    img 20863
    with fadelong
    m "ФРЕД!!!"
    m "Мерзавец..."
    m "Ты что, подглядываешь как я переодеваюсь?!"
    music Groove2_85
    img 20864
    with diss
    fred "Вы прекрасно справились, Миссис Бакфетт."
    fred "Продолжим нашу маленькую игру."
    fred "Сегодня Вы можете говорить с Юлией о чем хотите..."
    img 20865
    with diss
    fred "..."
    fred "Но Вы должны ущипнуть ее за попу."
    music Power_Bots_Loop
    img 20866
    with hpunch
    m "!!!"
    img 20867
    with fade
    m "К чему ты клонишь, Фред?!"
    m "Я не какая-нибудь лесбиянка!"
    m "Я - Леди! И я твой Босс!"
    m "Не забывай этого!"
    music Groove2_85
    img 20864
    with fade
    fred "Миссис Бакфетт, не будет ничего страшного, если женщина Босс ущипнет за попу свою подчиненную."
    fred "Это одинаковый пол, поэтому это не будет считаться харрасментом."
    fred "И будет вполне профессионально."
    img 20865
    with diss
    fred "Однако, Миссис Бакфетт, если Вы этого не сделаете..."
    fred "То весь Ваш отдел скоро увидит фото, как их Босса щипает за задницу другой мужчина."
    img 20868
    with diss
    m "Ты..."
    img 20865
    with diss
    fred "В то время, когда их Босс трет пятно на ковре."
    img 20869
    with fade
    m "Я убью тебя, Фред..."
    fred "Миссис Бакфетт, я профессионал и нет необходимости убивать меня."
    fred "Просто сделайте что я прошу..."
    m "!!!"
    return

label ep27_dialogues6_julia13:
# Появляется вариант Ущипнуть Юлию за зад.
# Моника подходит к Юлии и просит ее встать и подойти к ней.
# Моника подходит к окну, Юлия следует за ней
    music stop
    img black_screen
    with diss
    pause 1.0
    sound highheels_short_walk
    music Groove2_85
    img 20927
    with fadelong
    w
    sound desk_open
    img 20928
    with diss
    julia "Миссис Бакфетт?"
    sound highheels_short_walk
    img 20929
    with fadelong
    m "Юлия."
    m "Пожалуйста, встань и подойди ко мне."
# Моника встает чуть сзади Юлии и говорит ей посмотреть в окно.
# Спрашивает у Юлии что она там видит?
# Юлия смущается и говорит Монике что видит там город.
    sound highheels_short_walk
    img 20930
    with diss
    julia "..."
    music Loved_Up
    img 20931
    with diss
    m "Юлия, посмотри, пожалуйста, в окно."
    img 20932
    with fade
    julia "..."
    img 20933
    with diss
    w
    img 20934
    with diss
    m "Юлия, что ты там видишь?"
    img 20935
    with fade
    julia "Миссис Бакфетт, я вижу там город..."

# Выбор:
# Ущипнуть Юлию
# Не делать этого.
# # Если не делать: Моника говорит Юлии что хватит смотреть в окно, пора возвращаться к работе.
# Юлия подозрительно смотрит на Монику
    img 20936
    with diss
    $ menu_corruption = [juliaMonicaPinchAssCorruptionRequired]
    menu:
        "Ущипнуть Юлию.": #corruption
            pass
        "Не делать этого.":
            music Groove2_85
            mt "Нет, я не могу сделать это..."
            # моника уходит к столу
            sound highheels_run2
            img 20937
            with fadelong
            m "Юлия, хватит смотреть в окно!"
            m "Пора возвращаться к работе!"
            julia "..." # удивленно смотрит
            return -1

    img 20938
    with fade
    w
    img 20939
    with diss
    m "Да, там город..."
# Если ущипуть:
    if char_info["Julia"]["level"] < 3:
# Если ур. меньше 3, то Моника пытается щипнуть Юлию, а та отскакивает и говорит Монике что она собирается сделать?
# Моника отвечает что это ей показалось и пусть она идет заниматься работой, а не смотреть в окно.
# Потому что, если она будет плохо работать, то ее ждет увольнение!
# Юлия в шоке отвечает да, конечно и идет работать
        # отскакивает
        sound Jump1
        img 20940
        with diss
        w
        music Power_Bots_Loop
        sound Jump2
        img 20941
        with vpunch
        julia "Миссис Бакфетт!"
        julia "Что Вы собираетесь сделать?!"
        img 20942
        with fade
        m "Я? Ничего!"
        m "Видимо тебе что-то показалось, Юлия."
        sound highheels_run2
        img 20943
        with fadelong
        m "Иди занимайся работой."
        m "Хватит смотреть в окно!"
        return -2

# Если ур. больше или равен 3
# Моника щипает Юлию за попу.
# Юлия вскрикивает от неожиданности, она ошарашена.
# Спрашивает у Моники: Миссис Бакфетт, что Вы делаете?
# Вы ущипнули меня... за мою попу!
# Моника отвечает что это ей показалось и пусть она идет заниматься работой, а не смотреть в окно.
# Потому что, если она будет плохо работать, то ее ждет увольнение!
# Юлия в шоке отвечает да, конечно и идет работать
    # щипает
    music stop
    img black_screen
    with diss
    pause 1.0
    music Loved_Up
    sound Jump1
    img 20940
    with diss
    w
    sound Jump2
    img 20944
    with diss #jump
    w
    music Power_Bots_Loop
    img 20946
    with hpunch
    julia "Ай!"
    img 20945
    with diss
    w
    sound Jump1
    img 20947
    with vpunch
    julia "!!!"
    img 20948
    with fade
    julia "Миссис Бакфетт, что Вы сделали?!"
    m "..."
    music Groove2_85
    img 20949
    with diss
    julia "Вы... Вы ущипнули меня за мою попу!"
    img 20950
    with fade
    m "Нет!"
    m "Видимо тебе что-то показалось, Юлия."
    m "Иди занимайся работой."
    m "Хватит смотреть в окно!"
    img 20951
    with diss
    julia "..."
    img 20952
    with fade
    m "Если ты будешь плохо работать, то тебя ждет увольнение!"
    julia "Да, Миссис Бакфетт..."
    julia "Конечно..."

# Это добавляет прогресс к ур.3
# Затем сообщение что дальнейший прогресс с Юлией будет доступен в следующем обновлении.
#    help "Дальнейший прогресс с Юлией будет доступен в следующем обновлении."
    return 1
