default monicaPrisonerLiveTogether1 = False  # Моника зашла в полицейский участок
default monicaPrisonerLiveTogether2 = False  # Моника попросила Боба подселить к ней в камеру заключенного
default monicaPrisonerLiveTogether3 = False  # Моника решила подыграть заключенному и сказать, что она хорошая шлюха
default monicaPrisonerLiveTogether4 = False  # Моника попросила разрешения показать свою грудь
default monicaPrisonerLiveTogether5 = False  # Моника попросила разрешения показать свою грудь и сказала, что она шлюха
default monicaPrisonerLiveTogether6 = False  # Моника показала свою грудь заключенному
default monicaPrisonerLiveTogether7 = False  # Моника помогла заключенному пописать
default monicaPrisonerLiveTogether8 = False  # Моника сказала Бобу, что помогает писать заключенному
default monicaPrisonerLiveTogether9 = False  # Моника легла к заключенному
default monicaPrisonerLiveTogether10 = False  # Моника сказала Бобу, что все ок, когда заключенный заставил делать минет
default monicaPrisonerLiveTogether11 = False  # Моника согласилась сделать минет заключенному
default monicaPrisonerLiveTogether12 = False  # Моника попросила заключенного о сексе

# Если с момента прошлого посещения Маркуса прошла неделя, то Моника при клике на полицию говорит
label ep213_dialogues_police1:
    mt "Маркус сказал, чтобы я снова пришла к нему..."
    mt "Иначе я потеряю для него интерес и он заберет меня на ферму, несмотря на действия Дика!"
    mt "Какой ужас! Я боюсь думать о том, что со мной может случиться!"
    mt "И я боюсь идти туда!"
    mt "Но у меня нет выхода!"
    mt "Если я этого не сделаю, то все будет только хуже!"
    menu:
        "Зайти внутрь.":
            $ monicaPrisonerLiveTogether1 = True # Моника зашла в полицейский участок
            pass
        "Уйти":
            return False
    # Если нет пробки с собой
    mt "Мне... Лучше взять с собой ту пробку, которую мне дал Маркус..."
    mt "Боюсь представить что будет, если этот извращенец попросит показать ее... #ее - it"
    mt "Ведь он не разрешал мне ее вынимать... #ее - it"
    return False
    #

label ep213_dialogues_police2:
    mt "Я вся трясусь от ужаса!"
    mt "Неужели я смогу сделать еще шаг вперед и войти туда?!"

    # входит
    mt "О БОЖЕ! О БОЖЕ!!"
    mt "Может быть еще не поздно повернуть назад???"
    mt "В прошлый раз я еле выбралась отсюда!"

    # подходит
    policewoman "Гражданка, что вам надо?"
    policewoman "Что вы здесь слоняетесь?!"
    policewoman "Покиньте учреждение!"
    m "ММММэм... Я пришла..."
    m "Я пришла..."
    policewoman "Говорите внятнее!"
    policewoman "Я не понимаю, что вы там бубните себе под нос!"
    m "Мэм... Я пришла..."
    m "У меня дело к Мистеру Маркусу..."
    policewoman "Мистер Маркус большой начальник!"
    policewoman "Кто вы такая, что у вас к нему дело?!"
    m "Он... Он ждет меня, Мэм..."
    policewoman "Я позову детектива и пусть он разбирается с вами!"
    m "Да, Мэм... Конечно..."

    # policeman2 - с усами (посмотреть как сделано до этого, возможно поменять имена местами)

    # затемнение
    # приходит детектив
    detective "Здравствуйте, Мэм."
    detective "Я припоминаю вас. Можете напомнить, как вас зовут?"
    m "Меня зовут... Моника Бакфетт, Сэр..."
    detective "Мэм, какое у вас дело к Мистеру Маркусу?"
    m "Сэр... Я уже... Я уже приходила к нему..."
    m "Он сказал мне явиться снова через какое-то время..."
    detective "Мэм, одну минуту..."
    m "Да, конечно, сэр..."
    # затемнение
    # Детектив возвращается, по краям Монику окружают полицейские
    detective "Мэм. Мистер Маркус согласился принять вас."
    m "..."
    detective "Однако, он сейчас не здесь."
    detective "Мистер Маркус примет вас завтра."
    detective "Он спросил, не будете ли вы любезны подождать его здесь?"
    policeman1 "..." # улыбается, Моника смотрит на него
    m "!!!"
    m "Да, сэр... Конечно... Я... Я подожду его..."
    detective "Мэм, вы пройдете со мной добровольно?"
    m "!!!"
    detective "Или окажете сопротивление?"
    mt "О БОЖЕ!"
    mt "Я догадываюсь, куда меня поведут!"
    mt "Но я знаю, что у меня нет выбора..."
    m "Я..."
    m "Я пойду добровольно, сэр..." # смотрит на полицейских со страхом

    # Затемнение, тюрьма, перед столом Боба, полицейские ведут Монику в камеру, останавливаясь на мгновение около Боба
    # Детектив идет следом, чуть поодаль (не участвует в разговоре)
    policeman1 "Боб, мы привели к тебе постоянного клиента!"
    policeman1 "Она снова пришла сама!"
    policeman1 "Что ты здесь делаешь с ней такого, что она снова и снова возвращается к тебе?"
    policeman1 "Ха-ха-ха!"
    policeman2 "Куда ее? Как обычно?"
    overseer "Что?! Снова она?!"
    overseer "У меня только что забрали одну шумную заключенную!"
    overseer "И вы сразу ведете другую!"
    overseer "Моя голова! Она не выдержит!"
    policeman1 "Боб, если она будет шуметь, ты знаешь кого позвать!" # подмигивает

    # Подходит детектив
    overseer "Мистер Детектив?!"
    detective "Приветствую, Боб."

    # Вид переключается на полицейских в камере + Моника
    # полицейские грубо общаются с Моникой
    policeman1 "Ну что, шлюшка, тебе здесь нравится?"
    policeman1 "Раздевайся! Здесь неположено находиться в таком виде!"
    policeman1 "Ха-ха-ха!"
    # Моника раздевается
    mt "Все это уже было... Все уже было..."
    mt "Я всегда справлялась..."
    mt "Я справлюсь и в этот раз!"

    # Моника раздевается, видна пробка
    policeman2 "Что это там у тебя?"
    m "Это... Это приказал носить Мистер Маркус..."
    policeman2 "Хорошо, но мы должны проверить, что ты ничего не прячешь под этим."

    m "Не прячу? Где не прячу?"

    policeman1 "Сучка, слушай что тебе говорят!"
    policeman1 "Вынимай эту штуку! Мы должны провести досмотр!"

    m "Что? Какой досмотр?"

    # угрожающе
    policeman1 "Вынимай эту штуку и покажи нам свою задницу!"
    policeman1 "Иначе я возьму дубинку и засуну тебе ее туда, чтобы проверить, нет ли там чего! #ее - it"

    mt "О БОЖЕ!!!"

    # Моника с трудом достает пробку
    policeman1 "Давай, показывай нам!"

    # Моника наклоняется, чтобы показать что у нее там ничего нет (не брать вблизи)
    # Полицейский1 заглядывает туда в упор

    policeman1 "Давай, стой так! Я еще не разглядел как надо!"

    mt "О БОЖЕ! Как такое может быть?!"
    mt "Я, Моника Бакфетт, стою, показывая свой зад!"
    mt "А какой-то никчемный полицейский рассматривает, что у меня внутри!"
    mt "О УЖАС!!!"

    policeman1 "Странно, но там ничего нет..."
    policeman1 "Сучка, признайся, ты задумала с помощью этой пробки устроить побег?!"

    m "Что? Побег?"

    policeman1 "Аха-ха-ха!!!"

    # Сменяется на детектива и Боба
    detective "Боб, завтра эта заключенная встретится с Мистером Маркусом, если тот успеет вернуться."
    detective "После встречи, либо если Мистера Маркуса завтра не будет, она отправится на объект."

    overseer "Да, Мистер Детектив, я понял..."
    detective "Поэтому, проследи, чтобы на ней не было никаких следов воздействия..."
    overseer "Да, Мистер Детектив, конечно..."
    detective "Не так, как было с предыдущей заключенной, которую я забрал вчера."
    overseer "Мистер Детектив, меня никто не предупреждал, потому я... а..."

    # полицейские идут от камеры
    policeman1 "Пока, сучка! Смотри, не потеряй свою пробку! Ха-ха!"
    # подходят к столу Бобу, там детектив подключается к тому, чтобы уйти с ними
    # детектив бросает Бобу
    detective "Ты меня услышал, Боб."
    overseer "Да, Мистер Детектив. Так точно..."
    return

label ep213_dialogues_police3:
    # Моника голая
    # Сжавшись у кровати
    mt "Мерзкие халдеи!!!"
    mt "Знали бы они, с кем обращаются подобным образом!!!"
    mt "Моника, ты выдержишь! Выдержишь!"
    mt "Ты встретишься с Маркусом и договоришься с ним!"
    mt "У тебя железная деловая хватка и ты можешь решить любую проблему!"
    mt "Не сдавайся!"
    return

    # сцена, не рендерить
label ep213_dialogues_police4:
    # решетка
    mt "Я не хочу подходить туда..."
    mt "Там только этот дебил Боб и куча заключенных извращенцев..."
    return

    # туалет.
label ep213_dialogues_police5:
    mt "Я пока не хочу писать..."
    return

label ep213_dialogues_police6:
    # нажимает на пробку, которая валяется на кровати или полу после осмотра попы полицейскими
    mt "Нужно будет не забыть вставить ее обратно перед тем, как я пойду к Маркусу."
    return

    # рендерить
label ep213_dialogues_police7:
    # кровать
    # Моника лежит на кровати, голая
    mt "Удивительно, но я начинаю привыкать к этому месту..."
    mt "Пожалуй, я лягу спать."
    mt "Пока я сплю, наступит завтрашний день."
    mt "Я поговорю с Маркусом и отправлюсь на свободу."
    mt "Возможно, мой кошмар и вовсе закончится..."
    mt "Все снова станет таким, как было раньше..."
    mt "Спокойной ночи, Моника..."
    mt "Я сплю..."

    # затемнение

    # резкое прерывание сна
    overseer "Я тебе говорю, что ее трогать нельзя!"
    overseer "Мистер Детектив сказал, что Мистер Маркус отправит ее на их объект!"
    overseer "Завтра!"

    # Моника просыпается в ужасе
    mt "Объект?! ЧТОООООО?!"
    mt "Он говорит про Ферму 218?!?!"

    # Боб и заключенный1 говорят около решетки Моники
    prisoner1 "Но Боб! Ты обещал!"
    prisoner1 "Почему Джон целую неделю развлекался с предыдущей шлюхой?!"
    prisoner1 "А ведь та шлюха была плохой!"
    prisoner1 "И вот, наконец-то, моя очередь!"
    # Если Моника была хорошей шлюхой
    prisoner1 "И к нам подселили хорошую шлюху"
    #
    prisoner1 "А ты говоришь, что нельзя!"
    prisoner1 "Так несправедливо, Боб!"

    # Моника подбегает к решетке
    m "ЧТО?! Боб! Куда меня должны отправить завтра?!"
    m "Я должна увидеться с Мистером Маркусом!"

    overseer "Ты и увидишься с ним, а потом отправишься на какой-то объект."
    overseer "Куда отправляют на перевоспитание таких шумных заключенных, как ты!"
    overseer "Из-за тебя всегда шум!"
    overseer "И из-за этого у меня болит голова! Каждый день!"

    m "Это решит Мистер Маркус! Он отпустит меня!"

    overseer "Мистер Маркус очень важный и занятой человек!"
    overseer "У него вряд ли найдется время разговаривать с тобой!"
    overseer "Он даже не может найти время, чтобы поговорить с Бобом!"
    overseer "Куда уж тебе?!"
    overseer "Детектив сказал, что заберет тебя завтра!"
    overseer "И сказал, что тебя нельзя наказывать!"

    prisoner1 "Но Боб, как они узнают?!"

    overseer "У них там ентот... Тщательный досмотр..."
    overseer "Вот значит!"

    mt "О БОЖЕ!"
    mt "Если Маркус не найдет на меня время, то мне конец!!!"
    mt "Я встречусь с ним!"
    mt "Я обязательно встречусь с ним!"

    prisoner1 "Боб, так не честно!"
    prisoner1 "Боб, но ты обещал!"

    overseer "Заключенную трогать нельзя!"
    overseer "Так сказал Мистер Детектив!"

    prisoner1 "Боб, я обещаю, что не буду трогать ее!"
    prisoner1 "Честное слово!"
    prisoner1 "Ты сможешь выполнить приказ Мистера Детектива и выполнить свое обещание передо мной!"

    overseer "Не будешь трогать?"

    prisoner1 "Да, Боб!"
    prisoner1 "Я буду только смотреть на нее!"

    overseer "Но ее завтра уже отправят. Ты пропустишь свою очередь."
    overseer "Следующая заключенная уже достанется другому заключенному, который будет вести себя тише всех."

    prisoner1 "Да, Боб!"
    prisoner1 "Я знаю!"
    prisoner1 "Я хочу именно эту!"
    prisoner1 "Если ее завтра заберут, я не смогу ее пропробовать!"
    prisoner1 "Ой, то есть, не смогу на нее посмотреть!"

    overseer "Нет!"
    overseer "А если она расскажет Мистеру Детективу?"

    prisoner1 "Боб! Она ничего не расскажет ему!"

    overseer "Это еще почему?"

    prisoner1 "Боб, она сама хочет, чтобы я побыл с ней!"

    overseer "Сама?! Брехня!"

    # заключенный нагибается через решетку и шепчет Монике
    prisoner1 "Шлюха, быстро говори что ты хочешь, чтобы я подсел к тебе!"
    prisoner1 "Иначе ты станешь плохой шлюхой, и ты знаешь что тогда будет!"

    mt "Этот мерзавец снова шантажирует меня тем, что расскажет детективу про меня!"
    mt "Сволочь!"
    mt "Мне и так придется стараться изо всех сил, чтобы выйти отсюда!"
    mt "И, если ко всему прочему, им станет известно про мой побег отсюда..."
    mt "Тогда у меня не будет шансов избежать страшной участи!"
    mt "О БОЖЕ!"
    mt "Что же мне делать???"

    menu:
        "Попросить Боба подсадить заключенного к себе в камеру.":
            $ monicaPrisonerLiveTogether2 = True # Моника попросила Боба подселить к ней в камеру заключенного
            pass
        "Поставить заключенного на место.":
            m "Нет, Боб!"
            m "Я не хочу, чтобы это жалкое ничтожество приближалось ко мне!"
            m "Только попробуй сделать это и Мистер Детектив все передаст Мистеру Маркусу!"
            m "И у тебя будут проблемы, Боб!"
            prisoner1 "Ах ты шлюха!"
            m "Заткни свою пасть, ничтожество!"
            m "Иначе завтра я расскажу самому Мистеру Маркусу про то..."
            m "Как ты подбиваешь стража порядка к тому, чтобы нарушить приказ!"
            m "Только представь, что с тобой будет после этого!"
            # Если Моника била заключенных
            m "К тому же, тебе показалось мало в прошлый раз?"
            m "Только попробуй еще раз сделать подобное..."
            m "Я постараюсь получше и твои яйца вытекут на пол целиком..."
            prisoner1 "Ладно, ладно..." # испуганно
            prisoner1 "Это совершенно необязательно..."

            # разговор об одежде
            return


    mt "Я не верю... Я не верю в то, что прошу подселить ко мне какого-то заключенного..."
    mt "Это кошмар... Это сон..."
    m "Мммистер... Боб..."
    overseer "Да?!"
    # Моника смотрит затравленно на заключенного
    m "..."
    # заключенный смотрит угрожающе
    prisoner1 "!!!"

    m "Я... Я..."

    overseer "Ну, говори!"
    overseer "Когда я жду, у меня еще больше начинает болеть голова!"

    m "Мистер Боб..."
    m "Я... Я хотела бы, чтобы этот заключенный был здесь, в моей камере..."

    overseer "Что, правда? Ты сама этого просишь?"

    prisoner1 "!!!"
    m "Да, Мистер Боб... Я... Я уверена..."

    overseer "..." # думает
    overseer "Хорошо, но чтобы на ней не было никаких следов! Тебе ясно?!"

    prisoner1 "Да, Боб!"
    prisoner1 "Конечно!"

    overseer "Иди в свою камеру, я позову тебя!"
    # уходит, затемнение

    # разговор об одежде
    m "Мистер Боб... Скажите..."
    m "Могли бы вы дать мне какую-то одежду..."

    overseer "Всю одежду увезли в прачечную! Уже какое-то время назад!"
    overseer "И назад не привозили!"

    # Моника убеждающе
    # Если диалог при заключенном
    m "Но Мистер Боб..."
    m "Этот заключенный... Если я буду без одежды... Я боюсь, что он может нарушить свое обещание..."
    m "А ведь вы знаете, что приказал Мистер Детектив..."
    # Если далог без заключенного (поставила на место)
    m "Но Мистер Боб..."
    m "В таком виде я... Я могу замерзнуть здесь..."
    m "А Мистер Детектив сказал, что меня должны будут куда-то везти..."
    m "Живой..."
    #

    overseer "Хммм..."
    overseer "Есть одежда заключенной, которую увезли вчера, но..."

    m "Мистер Боб. Вы джентельмен!"
    m "Я знаю, что Вы дадите мне ту одежду! Пожалуйста!"

    overseer "Кто Я? Дже... Джент..."
    overseer "Хватит путать меня своими словечками!"
    overseer "А то не буду кормить!"
    m "!!!"
    overseer "Сейчас принесу, если я ее еще не выбросил... #ее - it"

    # Затемнение, Моника одета
    m "Что это, Боб?!"
    m "Почему... Почему вся одежда порвана?!"

    overseer "Эта заключенная, до тебя..."
    overseer "Она была такая же шумная, как и ты!"
    overseer "Все время ругалась и кричала какую-то ерунду про то, что она известный журналист."
    overseer "И большой Босс!"
    overseer "Для меня есть только один Босс - это Мистер Маркус!"
    overseer "А такие как ты - только врут!"
    overseer "Я помню, как ты строила из себя Босса!"
    overseer "А оказалось, что у тебя ничего нет!"

    mt "О БОЖЕ!"
    mt "Я боюсь представить, что с ней случилось..."
    mt "Зачем я снова пришла сюда?!"
    mt "Как мне снова выбраться из этого ада?!"
    mt "Но Маркус сказал мне снова прийти к нему!"
    mt "Иначе он заберет меня, невзирая на Дика!"

    overseer "Ну, что ты смотришь?!"
    overseer "Ты снова собираешься шуметь здесь!?"
    m "Нннет, Мистер Боб..."
    m "Я не буду шуметь, обещаю..."
    # конец диалога

    # появляется заключенный
    prisoner1 "Боб, я готов!"

    # затемнение
    # заключенный внутри
    # Боб снаружи
    overseer "Сидите здесь!"
    overseer "И чтобы не шуметь!"
    overseer "На сегодня отбой!"

    # затемнение
    # заключенный перед Моникой
    # Моника на кровати, зажата, смотрит зло
    return

# день1
label ep213_dialogues_police8:
# заставляет показать грудь и сказать что шлюха хорошая. и что ей очень жаль, что ей запретили трахаться с заключенным
# ложатся спать отдельно
    prisoner1 "Ну что, шлюха..."
    prisoner1 "Шлюха сама попросила Боба о том, чтобы я с тобой жил!"
    prisoner1 "Это значит что шлюха хорошая, так ведь?"
    prisoner1 "Шлюха скажет, какая она."
    prisoner1 "Говори, шлюха!"
    m "Что тебе от меня надо, ничтожество!?"
    prisoner1 "Мне надо услышать какая шлюха, хорошая или плохая."
    prisoner1 "Плохая шлюха хотела убежать отсюда..."
    prisoner1 "Если мы расскажем об этом, нам увеличат паек..."
    prisoner1 "И поменяют Боба на кого-нибудь посговорчивее."
    m "!!!"
    prisoner1 "Хорошая шлюха не собиралась убегать."
    prisoner1 "Хорошая шлюха рада обслуживать нас."
    prisoner1 "Скажи, какая ты шлюха: хорошая или плохая?"
    mt "Мерзавец!"
    mt "Жалкое ничтожество!"
    mt "Он даже не представляет насколько он жалок по сравнению со мной!"
    mt "..."
    mt "Что же мне делать?"
    mt "Ни в коем случае нельзя допустить, чтобы кто-то из полиции узнал о том, что я пыталась убежать отсюда..."
    menu:
        "Подыграть заключенному.":
            $ monicaPrisonerLiveTogether3 = True # Моника решила подыграть заключенному и сказать, что она хорошая шлюха
            pass
        "Поставить его на место!":
            # Моника толкает заключенного и тот падает на землю
            # Моника ставит ногу на его шею
            m "Слушай меня внимательно, мерзкий червь!"
            m "Если ты хоть раз дотронешься до меня или поднимешь на меня взгляд..."
            m "То я расскажу Мистер Маркусу о том, что вы коррумпируете местного надзирателя."
            m "Расскажу, про то, что ты, ничтожество, пытался прикоснуться ко мне!"
            m "Я пришла сюда по просьбе Мистера Маркуса."
            m "И, если он узнает про то что здесь происходит, он отправит тебя в такое место..."
            m "Где ты будешь молить о конце своей жалкой никчемной жизни!"
            m "Ты меня понял, червь?!"
            prisoner1 "Аггхмм... Ммммм..."
            prisoner1 "Я понял... Отпусти меня..."
            prisoner1 "Аггхмм... Ммммм..."
            prisoner1 "Пожалуйста..."
            m "То-то же!"
            return False

    mt "Мне надо подыграть ему... Снова..."
    mt "Детектив сказал, что меня нельзя трогать..."
    mt "Это значит, что далеко этот мерзавец зайти не сможет..."
    mt "Я в безопасности, но мне надо притвориться и не дать ему повод рассказать обо мне..."

    m "Я... Я хорошая шлюха..."
    prisoner1 "Ага! Да! Есть!"
    prisoner1 "Хорошая шлюха просит разрешения показать свои сиськи!"
    m "!!!"
    # угрожающе
    prisoner1 "Иначе шлюха будет плохой..."
    menu:
        "Попросить у заключенного разрешения показать свою грудь.":
            $ monicaPrisonerLiveTogether4 = True # Моника попросила разрешения показать свою грудь
            pass
        "Поставить его на место!":
            return False


    m "Я..."
    m "Я прошу разрешения показать свою грудь..."

    prisoner1 "Сиськи! Показать сиськи!"
    prisoner1 "Скажи, кто ты! И скажи свою просьбу правильно!"

    menu:
        "Сказать, что Моника шлюха и попросить у заключенного разрешения показать свои сиськи.":
            $ monicaPrisonerLiveTogether5 = True # Моника попросила разрешения показать свою грудь и сказала, что она шлюха
            pass
        "Поставить его на место!":
            return False

    m "Я... Я хорошая шлюха..."
    m "И я прошу разрешения..."
    m "Показать... Показать свои..."
    prisoner1 "!!!"
    m "Я прошу разрешения показать свои сиськи..."
    prisoner1 "Я разрешаю хорошей шлюха показать свои сиськи!"
    m "..."
    prisoner1 "Ну?! Шлюха может показывать их!"

    menu:
        "Показать заключенному свою грудь.":
            $ monicaPrisonerLiveTogether6 = True # Моника показала свою грудь заключенному
            pass
        "Поставить его на место!":
            return False

    # Моника задирает майку и показывает грудь.
    prisoner1 "Хорошая шлюха!"
    prisoner1 "А теперь проси разрешения показать свою задницу!"
    m "ЧТО?! НЕТ!"
    overseer "Эй! Что вы там шумите?!"
    overseer "Я сказал отбой! Быстро спать!"

    # Заключенный убегает на другую кровать.
    return

# День2
label ep213_dialogues_police9:
    # Моника просыпается
    # Заключенный спит на другой кровати
    mt "Наконец-то наступило завтра!"
    mt "Мне нужно увидеться с Маркусом и убираться отсюда!"
    mt "Детектив что-то говорил о том, что меня должны отправить на объект..."
    mt "Но, я уверена, это было актуально до того, как я пришла сама к Маркусу."
    mt "Я ничего не нарушала и, уверена, после встречи с Маркусом меня отпустят..."


    mt "Кажется, это мерзкое насекомое еще спит..."
    mt "Мне надо быть тихой и не разбудить его."
    mt "Надо позвать Боба и убираться отсюда!"

# Моника подходит к решетке нормально
    overseer "Чего тебе?"
    m "Мистер Боб, скажите, Мистер Маркус ждет меня?"
    overseer "Да, Мистер Маркус сказал доставить тебя к нему!"
    overseer "Выходи!"
    m "Да, Мистер Боб, конечно, сейчас иду!"
    mt "Черт! Я забыла про пробку!"
    # Моника вставляет пробку
    mt "Мне надо вставить ее обратно в себя... #ее - it"
    mt "Вдруг Маркус проверит, ношу ли я это..."
    mt "Это ужасные ощущения!"
    mt "Я с ужасом вспоминаю как первый раз садилась на нее..."
    mt "Но, каждый раз, когда я делаю это, меня пронзает боль!"

    m "Мистер Боб, я готова идти."
    # кадры как Моника идет мимо заключенных, видна пробка сквозь колготки
    prisoners "Хорошая шлюха! Шлюха хорошая!"
    return

label ep213_dialogues_police10:
    # Возврашается, заключенный спит
    # ложится спать
    mt "Это было ужасно!"
    mt "У меня есть шанс снова выбраться отсюда, но он очень призрачный..."
    mt "Я не думала, что все так плохо на этот раз!"
    mt "Мне надо стараться изо всех сил!"
    mt "Хорошо, что хоть это ничтожество, которое поселилось в моей камере, уже спит..."

    # затемнение
# Ложится спать, просыпается от того, что заключенный собирается на нее писать.
# Моника в шоке, ей приходится держать член заключенного
    m "ЭЙ! ЧТО ТЫ СОБИРАЕШЬСЯ ДЕЛАТЬ?!?!"
    prisoner1 "Я проснулся от того, что хочу в туалет!"
    m "И?! ПРИ ЧЕМ ЗДЕСЬ Я?!"
    prisoner1 "Я собираюсь сделать это на тебя!"
    m "ЧТО?! ТЫ В СВОЕМ УМЕ?!?!"
    m "ДЕЛАЙ ЭТО КУДА ПОЛОЖЕНО!!!"
    prisoner1 "Если шлюха чего-то хочет, то пусть она сама делает это!"
    m "ЧТО ТЫ ИМЕЕШЬ ВИДУ?! УБЕРИ ЭТО ОТ МЕНЯ!!!"
    prisoner1 "Пусть шлюха возьмет мой член в руку и сама направит его!"
    m "ЧТО?! Я НЕ СОБИРАЮСЬ ТРОГАТЬ ЕГО!!!"
    prisoner1 "Тогда член будет писать туда, куда захочет!"
    m "НЕТ!!! ДЕЛАЙ ТУДА, В УНИТАЗ!!!"
    prisoner1 "Тогда возьми и направь его туда!"
    mt "Что это извращенец собрался делать?!"
    menu:
        "Помочь заключенному.":
            $ monicaPrisonerLiveTogether7 = True # Моника помогла заключенному пописать
            pass
        "Поставить его на место!":
            return False

    mt "О БОЖЕ! НЕ МОГУ ПОВЕРИТЬ ЧТО Я ДЕЛАЮ ЭТО!"
    # Заключенный писает в унитаз, а Моника держит его за член
    prisoner1 "Шлюху нельзя трахать целыми днями..."
    prisoner1 "Поэтому шлюха должна компенсировать это заботой..."
    mt "Ничтожество!"
    mt "Извращенец!"

    # Подходит Боб
    overseer "Эй! Что вы там делаете!"
    overseer "Я же сказал, что этого делать нельзя!"

    prisoner1 "Шлюха, быстро сказала ему, что просто помогаешь мне!"
    m "Что???"
    prisoner1 "Быстро!"

    menu:
        "Сказать, что Моника просто помогает заключенному.":
            $ monicaPrisonerLiveTogether8 = True # Моника сказала Бобу, что помогает писать заключенному
            pass
        "Поставить его на место!":
            return False

    m "Мистер Боб, Я..."
    m "Я просто помогаю ему... писать..."

    overseer "Что ты помогаешь ему делать?!"

    m "Я... Я помогаю ему писать, сэр..."

    overseer "Хватит там шуметь! Быстро спать!"

# Затем он перекладывается к ней. Моника против, но он настаивает. Ложится сзади, обнимая и член упирается Монике в попу.
    # заключенный ложится сзади Моники, приобнимая ее
    m "Эй! Иди спать на свое место!"
    m "Что ты себе позволяешь, мерзавец!?"
    # Моника вскакивает
    prisoner1 "Я пришел спать со своей шлюхой!"
    prisoner1 "Хорошая шлюха должна быть рада этому!"
    prisoner1 "Хорошая шлюха ляжет назад на место и скажет, что ей это нравится!"
    m "Нет! Я не буду спать рядом с тобой!"
    prisoner1 "Тогда ты станешь плохой шлюхой!"
    prisoner1 "Мне нельзя трахать тебя!"
    prisoner1 "От этой шлюхи нет никакого толка!"
    prisoner1 "Я лучше расскажу про плохую шлюху и получу дополнительный паек!"
    m "Ты не посмеешь!"
    prisoner1 "Быстро ложись ко мне или станешь плохой шлюхой!"
    prisoner1 "Говорю последний раз!"
    prisoner1 "Или прямо сейчас зову Боба и возвращаюсь назад к себе в камеру!"
    prisoner1 "Считаю до трех!"
    prisoner1 "Раз!"
    m "!!!"
    prisoner1 "Два!"
    mt "О БОЖЕ!"
    mt "Я не могу спать рядом с этим животным!"
    mt "Но я не представляю что случиться, если он расскажет обо мне!"
    mt "Это конец!"
    prisoner1 "Три!"
    menu:
        "Лечь к заключенному.":
            $ monicaPrisonerLiveTogether9 = True # Моника легла к заключенному
            pass
        "Поставить его на место!":
            return False

    m "Стой!"
    # Моника ложится к заключенному
    m "Только не дыши на меня своим смрадом!"
    prisoner1 "Шлюхе нравится спать со мной?"
    prisoner1 "Я не расслышал!"
    m "Мне... Мне нравится... спать с тобой..."
    mt "Это невыносимо!"
    # заключенный упирается членом Монике в попу сквозь колготки, упирается в пробку
    m "ТЫ СОШЕЛ С УМА?!"
    m "ТЕБЕ БОБ ЯСНО СКАЗАЛ, ЧТО ЭТОГО ДЕЛАТЬ НЕЛЬЗЯ!"
    prisoner1 "Я не нарушаю приказ Боба!"
    prisoner1 "У тебя итак в заднице торчит какая-то хрень."
    prisoner1 "Может, вытащить ее и заменить на кое-что получше? #ее - it"
    m "ЕСЛИ ТЫ ЭТО СДЕЛАЕШЬ, Я ВСЕ РАССКАЖУ БОБУ!"
    prisoner1 "Ладно, ладно..."
    prisoner1 "Шлюхе должно нравиться, что мой член оказывает ей внимание!"
    prisoner1 "И вообще, шлюха! Не мешай мне спать!"
    mt "Боже! Я не знаю, как мне вынести все это!"
    mt "Скорее бы настал завтрашний день!"
    # затемнение
    return

label ep213_dialogues_police11:
# день3
# После сна Моника обнаруживает что у нее во рту член заключенного.
    m "Мммммпхффф!!!"
    m "Что?!"
    m "Что это такое?!"
    m "Ты охренел, скотина?!"
    # Заключенный одевает штаны
    # Подбегает Боб
    overseer "Что здесь за шум?!"
    # заключенный говорит Монике тихо
    prisoner1 "Быстро скажи, что здесь все в порядке, шлюха!"
    prisoner1 "Иначе тебе будет хуже!"
    prisoner1 "Если Боб меня отселит, я все расскажу про тебя!"
    menu:
        "Сказать Бобу что все в порядке.":
            $ monicaPrisonerLiveTogether10 = True # Моника сказала Бобу, что все ок, когда заключенный заставил делать минет
            pass
        "Поставить его на место!":
            return False

    m "!!!"
    mt "Сволочь! Ненавижу!!!"
    m "Мистер Боб, здесь все в порядке..."
    overseer "А что ты тогда шумишь?!"
    overseer "Почему нарушаешь порядок?"
    m "Простите, Мистер Боб..."
    m "Такого больше не повторится..."
    overseer "У меня снова болит голова из-за тебя!"
    overseer "Скорее бы тебя забрали на ентот их объект!"
    m "!!!"
    return

    # У решетки, дергает
    # повтор диалога с Бобом, Моника уходит

label ep213_dialogues_police12:
    # Моника возвращается
    mt "Как долго будет продолжаться это безумие?"
    mt "Я бизнес-леди, а не какая-то кошка!"
    mt "Все это какой-то сюр, это не может быть реальным!"
    mt "Это все сон! Я проснусь!"
    mt "Я должна проснуться и все это исчезнет!"

    # Моника видит заключенного, тот сидит на ее кровати без штанов
    m "Что?! Что это?!"
    m "Почему ты сидишь в таком виде?!"
    m "Ты знаешь, что приказал Боб!"
    prisoner1 "Мне плевать, что приказал Боб!"
    prisoner1 "Мой член хочет, чтобы хорошая шлюха взяла его в рот!"
    m "Но Боб увидит!"
    prisoner1 "Ты сделаешь это тихо!"
    prisoner1 "Если Боб хоть что-то заподозрит, ты знаешь что с тобой будет!"
    # Если Моника уже делала групповой blowjob
    prisoner1 "Давай! Ты уже знакома с моим малышом!"
    prisoner1 "Садись на колени и проси разрешения пососать мой член!"
    mt "Боже! Это все заходит дальше и дальше!"
    mt "Это надо как-то прекратить, но как?!"
    mt "Одно его слово и я отправлюсь на эту ужасную ферму!"

    menu:
        "Сделать как требует заключенный.":
            $ monicaPrisonerLiveTogether11 = True # Моника согласилась сделать минет заключенному
            pass
        "Поставить его на место!":
            return False

    # Моника садится
    mt "Мне надо притвориться, что я делаю это..."
    mt "Ведь я на самом деле этого не делаю..."
    mt "А просто притворяюсь..."
    prisoner1 "Давай, шлюха, скажи кто ты и проси разрешения пососать мной член!"
    m "!!!"
    m "Я... Я хорошая шлюха..."
    m "И я прошу разрешения взять в рот твой член..."
    prisoner1 "Я разрешаю шлюхе взять его..."
    prisoner1 "Можешь приступать!"
    mt "Я с трудом представляю, как можно дотронуться до этого грязного вонючего отростка..."
    prisoner1 "Делай это тихо! Боб не должен услышать!"
    prisoner1 "Если Боб услышит и выгонит меня, то это будет твоя вина!"
    prisoner1 "А это значит, что шлюха станет плохой! Со всеми последствиями для нее!"
    m "!!!"
    # Моника берет его член в рот
    prisoner1 "Да, вот так..."
    prisoner1 "Хорошая шлюха... Соси..."
    prisoner1 "Соси еще... Да..."

    # заключенный кончает
    # Монику рвет в туалет (со спины)
    mt "О БОЖЕ! МЕНЯ СЕЙЧАС ВЫРВЕТ!"

    # Появляется надзиратель
    overseer "Эй! Что за шум!"
    overseer "Вы нарушаете мой приказ?"
    # Моника поворачивается и смотрит на заключенного, тот на нее
    # Моника смотрит на Боба
    m "Нет, сэр..."
    m "Меня просто вырвало..."
    m "Видимо, я съела что-то не то..."
    # Поворачивается к заключенному
    m "Завтра я выйду отсюда и больше никогда не увижу твою мерзкую морду!"
    # затемнение

    # Моника ложится спать, член заключенного снова упирается в нее
    mt "Мне надо продержаться до завтра..."
    mt "Завтра меня ждет экзамен..."
    mt "Я справлюсь и я выйду отсюда!"
    mt "Я вырвусь и никогда сюда не вернусь!"
    mt "И мне не важно, что скажет Маркус!"
    mt "Я больше не смогу вынести этот ад..."
    mt "Лежать рядом с безмозглым грязным животным..."
    mt "Как до такого могло дойти?!"
    mt "Все, Моника... Хватит об этом..."
    mt "Постарайся заснуть..."

    # затемнение
    return

# день4
label ep213_dialogues_police13:
# После сна Моника обнаруживает что заключенный стянул с нее одежду и хочет войти в нее. (лежа сзади, как вечером)
    m "ЭЙ! ТЫ СОВСЕМ ОХРЕНЕЛ?!"
    # Моника вскакивает
    m "ТВАРЬ!!!"
    m "НЕ СМЕЙ ПРИКАСАТЬСЯ КО МНЕ ТАМ!"
    # Заключенный зло шипит, он очень слой и грозный
    prisoner1 "Шлюха! Тихо!"
    prisoner1 "Ты решила сегодня сбежать от меня, да?!"
    prisoner1 "Значит, моя очередь быть с женщиной пройдет и мне придется ждать еще не один месяц..."
    prisoner1 "И ты хочешь вот так просто уйти отсюда?!"
    m "Мерзавец, ты знаешь что приказал Боб!"
    m "Тебе запрещено прикасаться ко мне!"
    prisoner1 "Если бы я делал то, что мне говорят, то не оказался бы здесь!"
    prisoner1 "И, раз уж до этого дошло, я не упущу свой шанс!"
    prisoner1 "Если ты хорошая шлюха, то ты снимешь одежду."
    prisoner1 "Упрешься на унитаз, повернешься ко мне задницей и будешь просить меня войти в тебя!"
    m "Нет! Ни за что!"
    prisoner1 "Я не шучу, шлюха..."
    prisoner1 "Мне нечего терять..."
    prisoner1 "Если я не попробую тебя сейчас, то буду долго жалеть..."
    prisoner1 "Тебя все равно сегодня переведут отсюда..."
    prisoner1 "И я подозреваю, что переведут туда, откуда не возвращаются..."
    m "Нет! Я вернусь!"
    prisoner1 "Я буду рад, если шлюха вернется..."
    m "Я вернусь... Я вернусь на свободу! Не в это жуткое подземелье!"
    prisoner1 "Если Боб меня выгонят сейчас, то я ничего не потеряю..."
    m "Боб накажет тебя!"
    prisoner1 "Но я расскажу все про тебя и про Боба..."
    prisoner1 "И тогда Боба уберут отсюда..."
    prisoner1 "Я ничего не теряю, шлюха."
    prisoner1 "Зато плохая шлюха потеряет все..."
    prisoner1 "Поэтому выбирай, кто ты..."
    prisoner1 "Хорошая шлюха или плохая..."
    mt "О БОЖЕ!"
    mt "МНЕ КОНЕЦ!"
    mt "Этому животному и правда нечего терять!"
    mt "Моника, как ты влипла в такую ситуацию?!"
    mt "Неужели тебе придется заниматься этим с..."
    mt "Я даже не знаю как это назвать, это не человек..."
    mt "Это самый жалкий отброс, который только можно представить!"
    prisoner1 "Раз..."
    mt "Может быть, мне что-то придумать?"
    mt "Как-то потянуть время?"
    prisoner1 "Два..."
    mt "Но как?!"
    mt "Мои мысли путаются..."
    mt "Я... Я ничего не могу придумать..."
    prisoner1 "Три!"
    menu:
        "Снять одежду и просить заключенного о сексе...":
            $ monicaPrisonerLiveTogether12 = True # Моника попросила заключенного о сексе
            pass
        "Поставить его на место!":
            return False

    # заключенный отворачивается
    prisoner1 "Я иду звать Боба!"
    # Моника роняет лицо на руки
    m "Стой!"
    m "Я сделаю это..."

    prisoner1 "Да! Давай, шлюха! Скорее!"
    # заключенный обращается к остальным заключенным
    prisoner1 "Эй, ребята!"
    prisoner1 "Ведите себя тихо!"
    prisoner1 "Я собираюсь трахать нашу шлюху!"
    prisoner1 "Если вдруг придет Боб, отвлеките его!"
    prisoners "Шлюха! Шлюха!"
    prisoners "Трахать шлюху! Да!"

    # Моника раздевается, встает на унитаз, поворачиваясь попой к заключенному
    prisoner1 "Вынь эту пробку!"
    prisoner1 "Я хочу трахнуть тебя в задницу!"
    m "Нельзя! Мистер Маркус приказал не вынимать это!"
    m "Если я выну пробку, он заметит это!"

    prisoner1 "Хитрая шлюха! Ничего! Я еще доберусь до твоей задницы!"
    prisoner1 "Тогда давай, подставляй свою киску!"
    prisoner1 "Сейчас я буду трахать тебя!"

    m "Боб услышит..."
    m "Или увидит следы..."

    prisoner1 "Я не буду в этот раз кончать на тебя, шлюха!"
    prisoner1 "И да, заткни свой рот!"
    prisoner1 "Если Боб услышит тебя, то пеняй на себя!"
    prisoner1 "Ну же! Говори кто ты! Проси меня трахнуть тебя!"
    m "Я... хорошая шлюха..."
    m "Я... Я прошу войти в меня..."
    prisoner1 "Трахнуть! Ты просишь трахнуть тебя!"
    m "Я... Я прошу... Я прошу трахнуть меня..."

    # Моника зажимает рукой рот
    # Заключенный начинает в нее входить (сцена)

    prisoner1 "Да, шлюха!"
    prisoner1 "Да! Как я ждал этот момент!"
    prisoner1 "Не могу поверить, что трахаю такую богатую шлюху!"
    mt "Не могу поверить в то, что происходит..."
    mt "Меня трахает какой-то грязный заключенный..." # вряд ли Моника будет думать такое грубое слово в отношении себя...
    mt "На грязном унитазе..."
    mt "И мне приходится зажимать рот, чтобы скрыть это от надзирателя..."
    mt "Какой ужас..."
    prisoner1 "Ребята будут завидовать мне!"
    prisoner1 "Мне даже придется поделиться тобой в следующий раз!"
    prisoner1 "У тебя там так комфортно!"
    prisoner1 "Уверен, их членам понравится в тебе!"
    prisoner1 "Жаль, что они не влезут все сразу!"
    prisoner1 "Но несколько влезет точно!"

    # Заключенный собирается кончать
    prisoner1 "АААААААХХХХ!!!"
    m "Не в меня!!!"
    # Заключенный кончает куда-нибудь в сторону

    m "Мерзавец! Ничтожество!"
    m "Ты заплатишь за то, что сделал! Клянусь!"

    overseer "Что здесь за шум?!"
    overseer "Почему ты голая?!"
    overseer "Вы что, нарушили мой приказ?!"

    prisoner1 "Шлюха, ты знаешь что ответить..."
    prisoner1 "И ты знаешь, что будет, если ты ответишь неправильно..."
    m "!!!"

    m "Нет, сэр... Я..."
    m "Я решила раздеться чтобы..."
    m "Чтобы..."
    m "Чтобы пописать..."

    overseer "Быстро одевайся!"
    overseer "Мистер Маркус ждет тебя!"
    m "Да сэр... Конечно..."
    return

# Моника писает
label ep213_dialogues_police14:
    # Моника садится на туалет, заключенный стоит перед ней и смотрит в упор
    m "Я хочу писать, отвернись!"
    prisoner1 "Ты наша шлюха! Я буду смотреть на тебя когда хочу!"
    m "Я не могу писать, когда кто-то смотрит!"
    prisoner1 "Писай! Хорошая шлюха хочет писать!"
    # Моника писает
    mt "О БОЖЕ!"
    mt "Какой стыд!"
    mt "Как мне вынести все это..."
    return


# не рендерить
label ep213_dialogues_police15:
    # смотрит на заключенного после того, как поставила на место
    mt "Жалкий червь!"
    # говорит
    mt "Мне не о чем общаться с этим червяком!"
    return

label ep213_dialogues_police16:
# не рендерить
    # смотрит на заключенного в обычном режиме
    mt "Мне надо что-то придумать!"
    mt "Я не могу постоянно поддаваться на его гнусный шантаж!"
    # говорит
    mt "Отвратительное существо!"
    mt "Я хочу держаться от него подальше!"
    return

# еда
label ep213_dialogues_police17:
# Боб отходит от камеры Моники
# раз в день она просит у него еду
    m "Стой!"
    m "Боб..."
    overseer "Чего тебе?"
    m "Боб... Принеси, пожалуйста, мне поесть..."
    # Боб уходит и приносит еду.
    overseer "На, жри!"
    # либо
    overseer "Мне передали, что ты сегодня уже ела!"
    mt "Что?! Ела эту ужасную кошачью еду?!"
    return
#
