label ep28_dialogues_jail1:
    # Моника ложится спать
    # Монике снится сон с Маркусом.
    m "Маркус?!"
    m "ГДЕ Я?!"
    m "У меня все болит!"
    m "О БОЖЕ!"
    marcus "Ты знаешь где ты..."
    m "Это... Это Ранчо 218?!"
    m "Я... Я попала сюда?!"
    m "Но нет! Этого не может быть!"
    m "Этого еще не случилось!"
    m "НЕЕЕЕТ!"
    marcus "Это скоро случится..."
    m "Зачем! Зачем ты снишься мне!"
    m "Уйди отсюда! Я должна отсюда выбраться!"
    m "Я должна проснуться!"
    marcus "Я снюсь тебе, чтобы сказать как избежать всего этого..."
    m "Что?"
    m "Ты... Ты можешь мне сказать как этого избежать?!"
    m "Что мне сделать? Я сделаю все, абсолютно все!"
    marcus "Полюбить меня..."
    m "Что..."
    # Конец сна
    return



label ep28_dialogues_jail2:
# Боб приходит в камеру и начинает трогать Монику во сне
# Моника просыпается от кошмара и кричит на Боба что он делает здесь
# Боб смущается и отвечает что принес ей похлебку.
# Моника смотрит на похлебку с отвращением и говорит что ей не нужна эта жуткая еда
# Ей надо встретиться с Мистером Маркусом и уйти из этого жуткого места
    m "Что..."
    m "Что это?!"
    m "Кто здесь!!!"
    m "БОБ?!"
    m "Что ты делаешь здесь?!"
    overseer "А... Кхм..."
    overseer "Я... Экхм..."
    overseer "Я принес тебе похлебку."
    m "!!!"
    mt "Фу! Какая гадость! Я и забыла как это выглядит..."
    m "Мне не нужна эта жуткая еда!"
    m "Мне надо встретиться с Мистером Маркусом! И я уйдй из этого жуткого места!"
    m "Мне нечего делать здесь!"

# Боб отвечает что Мистер Маркус занят и пока не может встретиться с ней.
# Ей надо подождать его дольше.
# Моника возмущается как это так?! Ей что, ждать его здесь, в камере?!
# Боб отвечает что это не его дело. Она арестант и сидит в камере.
# Боб собирается уходить
# Моника останавливает Боба и берет еду
    overseer "Мистер Маркус еще занят и он не может встретиться с тобой."
    overseer "Тебе надо подождать его дольше."
    m "Как это так?! Мне что, ждать его здесь, в камере?!"
    overseer "Это не мое дело. Ты арестант и сидишь в камере."
    # уходит
    m "Стой!"
    m "Боб..."
    overseer "Чего тебе?"
    m "Боб... Дай сюда еду..."

# Моника думает что же ей делать. Какой ужас и тд
# Моника может позвать Боба, но он не подходит
    mt "Что же мне делать?"
    mt "Какой ужас! Я пришла к Маркусу, чтобы поговорить с ним."
    mt "А, вместо этого, снова оказалась здесь, в этой жуткой камере."
    mt "Мне надо добиться этой встречи! Я сделаю это!"
    mt "Я не останусь здесь!"

    mt "Он не подходит..."
    mt "Он не слышит или не желает подходить..."
    mt "А это кто?"
    mt "Похоже это детектив, который встречал меня вчера..."
    mt "Что он делает здесь?"

# Вечером перед сном Монику окликивают заключенные
# Моника с ужасом видит что они у ее решетки
# Моника спрашивает что вы делаете здесь?! Как Вы сюда попали?
    prisoner1 "Эй, подойди сюда!"
    m "Что? Кто это зовет меня?"
    prisoner1 "Подойди сюда! Мы тебя ждем!"

    m "Что?! Заключенные?!"
    m "Что Вы делаете здесь?! Как Вы сюда попали?!"

# Заключенные отвечают что Боб разрешает выходить на прогулку перед сном.
# Моника спрашивает где Боб, они отвечают что его нет, он вернется позднее.
    prisoner1 "Мы на прогулке!"
    prisoner1 "Боб разрешает нам выходить на прогулку перед сном."
    m "Где Боб?!"
    prisoner1 "Боба нет. Он вернется позднее."

# Моника с ужасом говорит что вы же раньше не гуляли здесь. Уйдите отсюда!
# Те отвечают что Боб разрешил им гулять, потому что ему не удалось выполнить условие их молчания
# Какое еще условие?
# Заключенный спрашивает что шлюха что, забыла?
    m "Вы же раньше не гуляли здесь! Уйдите отсюда!"
    m "Немедленно!"
    prisoner1 "Боб разрешил нам гулять, потому что ему не удалось выполнить условие нашего молчания. Хе-хе."
    m "Какое еще условие?"
    prisoner1 "Шлюха, ты что, забыла?"

# Боб обещал им веселье с Моникой за то что те молчат и не надоедают Бобу своим шумом
# Вы не зайдете сюда!
# Заключенный отвечает что мы зайдем к тебе. Жаль что после этого Боб, скорее всего, запретит им гулять.
# Но это веселье того стоит!
    prisoner1 "Боб обещал нам веселье с тобой!"
    prisoner1 "За то что мы будем тихо себя вести и не надоедать Бобу своим шумом."
    m "Вы не зайдете сюда!"
    prisoner1 "Мы зайдем к тебе, шлюха!"
    prisoner1 "После выполнения этого условия, Боб, скорее всего, запретит нам гулять и впредь."
    prisoner1 "Но это веселье того стоит!"
# Моника отвечает что никогда! Она должна встретиться с Мистером Маркусом и они не смеют трогать ее!
# Заключенные отвечают что Боб уже пообещал, что она будет принадлежать им сразу после встречи с Мистером Маркусом
# Моника отвечает что они не дождутся! Она не вернется сюда после встречи с ним!
# Заключенные смеются а куда же ты денешься?
    m "Никогда! Никогда этого не будет!"
    m "Я скоро встречусь с Мистером Маркусом. Он ждет меня!"
    m "И Вы не смеете трогать меня!"
    prisoner1 "Да, верно! Боб нам обещал тебя сразу после твоей встречи с Мистером Маркусом!"
    prisoner1 "Скоро ты будешь принадлежать нам!"
    m "Не дождетесь! Я не вернусь сюда после встречи с ним!"
    prisoner1 "Ха-ха-ха! А куда же ты денешься?"

# Про себя думает О Боже! Я не поеду на ферму!
# Отвечает что она вернется на свободу после Мистера Маркуса и никогда не увидит эти отвратительные морды!
    mt "Куда я денусь..."
    mt "Куда?"
    mt "О БОЖЕ! Я не поеду на ферму, клянусь!"
    m "После встречи с Мистером Маркусом я выйду на свободу!"
    m "И больше никогда не увижу ваших отвратительных морд! Вы бы только посмотрели на себя! Фи!"

# Заключенный отвечает чтобы она попросила прощения у них за свои слова!
# Моника отвечает что не собирается! У них действительно отвратительные морды!
# И они даже не представляют с кем разговаривают сейчас!
# Заключенный отвечает что они разговаривают со шлюхой.
    prisoner1 "Попроси прощения за свои слова."
    m "И не собираюсь! У Вас действительно отвратительные морды!"
    m "Вы выглядите как жалкие гниющие червяки!"
    m "Вы даже не представляете с кем разговариваете сейчас!"
    prisoner1 "Мы?!"
    prisoner1 "Мы разговариваем со шлюхой."
# Только они пока не решили хорошая шлюха или плохая.
# ЧТООО?! Да как ты смеешь, урод, называть меня так!
# Заключенный отвечает, что шлюха, похоже, забыла, что хотела сбежать отсюда.
# Сегодня с утра приходил детектив от Мистера Маркуса и спрашивал про тебя, нарушала-ли ты какие-нибудь правила?
    prisoner1 "Только мы пока не решили хорошая шлюха или плохая."
    m "ЧТООО?! Да как ты смеешь, урод, называть меня так!"
    prisoner1 "Похоже шлюха забыла, что хотела сбежать отсюда!"
    prisoner1 "Сегодня с утра приходил детектив от Мистера Маркуса и спрашивал про тебя..."
    prisoner1 "Нарушала-ли ты какие-нибудь правила?"
# Не нарушала-ли дисциплину здесь или что-нибудь еще?
# Моника в шоке
# Шлюхой очень интересуются. А шлюха, в то же время, вступила в сговор с надзирателем с целью побега.
# Моника отвечает что они ничего не докажут!
# Заключенные отвечают что запомнили дни, когда Боб отлучался в банк и встречался с риелтором.
    prisoner1 "Не нарушала-ли дисциплину здесь или что-нибудь еще?"
    m "!!!"
    prisoner1 "Шлюхой очень интересуются..."
    prisoner1 "А шлюха, в то же время, вступила в сговор с надзирателем с целью побега."
    m "Вы ничего не докажете!"
    prisoner1 "Мы запомнили дни, когда Боб отлучался в банк и встречался с риелтором."
    prisoner1 "Мы все слышали!"
# Детектив проведет расследование и быстро расколет Боба.
# Тогда Боба заменят и они будут этому рады. Другой надзиратель будет поумнее и с ним будет проще договориться.
# А заключенным увеличат паек, они уверены в этом. Паек, да! Паек!
    prisoner1 "Детектив проведет расследование и быстро расколет Боба."
    prisoner1 "Тогда Боба заменят и мы будем этому рады!"
    prisoner1 "Другой надзиратель будет поумнее и нам с ним будет проще договориться."
    prisoner1 "А нам, за сотрудничество, увеливат паек! Мы уверены в этом!"
    prisoners "Паек, Да! Паек!"

# Так что пусть шлюха хорошенько подумает и ответит какая она? Хорошая или плохая?
# Плохая шлюха хотела сбежать, плохая шлюха нам не нужна здесь!
    prisoner1 "Так что пусть шлюха хорошенько подумает и ответит... Какая она?"
    prisoner1 "Хорошая или плохая?"
    prisoner1 "Плохая шлюха хотела сбежать, плохая шлюха не нужна нам здесь!"

# Моника в шоке смотрит
    m "!!!"

# Итак, отвечай!
    prisoner1 "Итак, отвечай!"

# Моника думает что это ужас!
# Они расскажут Маркусу про то что она собиралась сбежать отсюда.
# Судя по тому, что здесь рыскает детектив, они так и ищут способ отправить Монику на ферму.
# Но, видимо, у них нет зацепок, чтобы сделать это.
# И, если заключенные все расскажут, то это будет конец!
# О БОЖЕ, Моника! Что же мне делать?
    mt "О УЖАС!"
    mt "Они расскажут Маркусу про то что я собиралась сбежать отсюда!"
    mt "Судя по тому, что здесь рыскает детектив, они так и ищут способ отправить меня на ту ферму!"
    mt "..."
    mt "Но, видимо, у них нет зацепок, чтобы сделать это."
    mt "Но, если заключенные им расскажут про мои попытки сбежать, то это будет конец!"
    mt "О БОЖЕ, Моника! Что же мне делать?"

# Неужели мне придется притворяться какой-то шлюхой здесь?!
# Но иначе мне не выжить! Это вопрос жизни и смерти.
# А, судя по словам Мелани, может быть и еще похуже смерти.
    mt "Неужели мне придется притворяться какой-то шлюхой здесь?!"
    mt "..."
    mt "Но иначе мне не выжить! Это вопрос жизни и смерти."
    mt "А, судя по словам Мелани, может быть и еще похуже смерти..."

# Что же мне делать?
    mt "Что же мне делать?"
# Выбор:
# Притворяться шлюхой.
# Поставить их на место!
    menu:
        "Притворяться шлюхой.":
            pass
        "Поставить их на место!":
# Если поставить на место, то Моника говорит чтобы они заткнулись!
# Они сами нарушают правила тем, что заключают сделки с надзирателем.
# Гуляют здесь без разрешения администрации.
            m "Слышите, Вы?!"
            m "Вы сами нарушаете правила!"
            m "Нарушаете тем, что заключаете сделки с надзирателем!"
            m "Гуляете здесь без разрешения администрации."
# И, как к ним будет относиться другой надзиратель. Учитывая что они заложили предыдущего!
# Вы ни о чем с ним не договоритесь! Вы будете гнить в камерах, никогда не выходя из них!
            m "И, подумайте! Как к Вам будет относиться другой надзиратель, учитывая что Вы заложили предыдущего!"
            m "Вы ни о чем с ним не договоритесь!"
            m "Вы будете гнить в камерах, никогда не выходя из них!"
            m "И будете вспоминать доброго Боба!"
            prisoner "..."
            m "Давайте! Зовите сюда детектива! Мне есть что сказать ему!"
# Заключенные боятся
# Говорят что ладно, ладно, мы пошутили.
# Моника говорит что теперь пошли отсюда вон!
# Заключенные уходят
            prisoners "Она расскажет?"
            prisoners "Она расскажет про нас?"
            prisoner1 "Ладно, ладно... Мы пошутили..."
            m "А теперь пошли вон отсюда!"
            prisoner1 "Ладно. Мы уходим..."
            return False

# Если притворяться шлюхой
# Заключенный спрашивает раздраженно. Ну, отвечай! Хорошая ты шлюха или плохая?!
# Моника отвечает, что она... хорошая шлюха
# Заключенные радуются: да, хорошая шлюха. Шлюха хорошая!
# Как зовут шлюху? Как у шлюхи имя?
    prisoner1 "Ну, отвечай!"
    prisoner1 "Хорошая ты шлюха или плохая?!"
    m "..."
    mt "!!!"
    m "Я... Хорошая шлюха..."
    prisoners "Да, хорошая шлюха!"
    prisoners "Шлюха хорошая!"
    prisoner1 "Как зовут шлюху? Какое у шлюхи имя?"
# Выбор
# Назвать свое имя
# Назваться Мэрилин (если открыто)
# Моника называет имя
    menu:
        "Назвать свое имя.":
            pass
        "Назваться [monica_pub_name]":
            pass

    m "Меня зовут [monica_jail_name]..."
# Заключенные кричат да! Моника Бакфетт, шлюха!
# Заключенный говорит, скажи кто ты
    prisoners "Да! [monica_jail_name]! Шлюха!"
    prisoner1 "Скажи, кто ты!"

    m "!!!"
    prisoner1 "Ну же!"
# Я... Хорошая шлюха...
# О БОЖЕ!! Какой кошмар!
    m "Я... Хорошая шлюха..."
    mt "О БОЖЕ! Какой кошмар!"

# Назови свое имя и скажи кто ты!
# ...
# Ну же!
# Меня зовут... Моника Бакфетт...
# И я... хорошая шлюха....
# Я делаю это чтобы выжить! Какой ужас!
    prisoner1 "Назови свое имя и скажи кто ты!"
    m "..."
    prisoner1 "Ну же!"
    m "Меня зовут... [monica_jail_name]..."
    m "И Я... хорошая шлюха..."
    mt "Какой ужас! Но я делаю это чтобы выжить..."

# Да! Да!
# Хорошая шлюха должна извиниться перед нами!
# И должна сказать что хочет показать нам свои сиськи!
# Да! Да! Сиськи!
    prisoners "Да! Да!"
    prisoners "Хорошая шлюха должна извиниться перед нами!"
    prisoner1 "И должна сказать что хочет показать нам свои сиськи!"
    prisoners "Да! Да!"
    prisoner1 "Сиськи!"

# Извиниться перед заключенными
# Поставить их на место!
    menu:
        "Извиниться перед заключенными.":
            pass
        "Поставить их на место!":
            return False

# Мне надо делать что они говорят, иначе конец!
# Я буду притворяться и потяну время. Сегодня Мистер Маркус не смог встретиться со мной.
# Но я уверена, что завтра я увижусь с ним и этот кошмар закончится для меня!
    mt "Мне надо делать что они говорят, иначе конец!"
    mt "Я буду притворяться и потяну время."
    mt "Сегодня Мистер Маркус не смог встретиться со мной."
    mt "Но я уверена, что завтра я увижусь с ним и этот кошмар закончится для меня!"

# Ну же!
    prisoner1 "Ну же!"

# Я... Я хорошая шлюха.
# И?!
# И я прошу прощения у вас. За то что назвала Вас некрасивыми.
# И?! Кто мы?!
    m "Я... Я хорошая шлюха..."
    prisoner1 "И?!"
    m "И я прошу прощения у Вас. За то что назвала Вас некрасивыми..."
    prisoner1 "И?! Кто Мы?!"
# Вы... Вы очень красивые мужчины и...
# И что?! Давай, шлюха! Говори это!
# И... И я хотела бы показать Вам свою грудь...
# Сиськи! Не груд, а сиськи! Скажи!
# !!!
    m "Вы... Вы очень красивые мужчина и..."
    prisoner1 "И что?! Давай, шлюха! Говори это!"
    m "И... И я хотела бы показать Вам свою грудь..."
    prisoner1 "Сиськи! Не грудь, а сиськи! Скажи!"
    mt "!!!"
# Показать Вам... свои сиськи...
# Ну же! Показывай! Давай!
# Сиськи! Сиськи!
    m "Показать Вам... свои сиськи..."
    prisoner1 "Ну же! Показывай! Давай!"
    prisoners "Сиськи! Сиськи!"

# Показать грудь
# Поставить их на место!
    menu:
        "Показать грудь.":
            pass
        "Поставить их на место!":
            pass

# Моника показывает грудь, закрывая другой рукой киску.
# Сиськи! Сиськи!
    mt "..."
    prisoners "Сиськи! Сиськи!"

# Шлюха хочет показать нам и киску!
# Да! Киску! Киску!

# Ну же, шлюха! Давай показывай!
# Киску! Киску!
    prisoner1 "Шлюха хочет показать нам и киску!"
    prisoners "Да!"
    prisoners "Киску! Киску!"

    prisoner1 "Ну же, шлюха! Давай показывай!"
    prisoners "Киску! Киску!"

# Показать свою киску
# Поставить их на место!
    menu:
        "Показать свою киску.":
            pass
        "Поставить их на место!":
            pass

# Моника поднимает вторую руку вверх, держа робу.
    m "..."

# Да! Киска! Киска! Да!
    prisoners "Да! Киска!"
    prisoner1 "Киска! Да!"

# Шлюха хочет показать нас свою задницу!
# Давай шлюха, спрашивай разрешения у нас! Ты хочешь показать нам свою задницу!
# Давай, спрашивай нас!
    prisoner1 "Шлюха хочет показать нам свою задницу!"
    prisoner1 "Давай, шлюха, спрашивай разрешение у нас!"
    prisoner1 "Ты хочешь показать нам свою задницу!"
    prisoner1 "Давай, спрашивай нас!"

# О БОЖЕ! Неужели мне придется сказать это?!
# Эту... гадость...
    m "О БОЖЕ! Неужели мне придется сказать это?!"
    mt "Это... гадость..."

# Попросить разрешение показать свою попу
# Поставить их на место!
    menu:
        "Попросить разрешение показать свою попу.":
            pass
        "Поставить их на место!":
            return False

# Я... Я прошу...
# Кто ты! Называй себя!
# Я... Хорошая шлюха...
# И я... прошу... разрешения показать свою спину...
    m "Я... Я прошу..."
    prisoner1 "Кто ты! Называй себя!"
    m "Я... Хорошая шлюха..."
    m "..."
    m "И Я... прошу... разрешения показать свою спину..."

# Задницу, шлюха! Свою задницу! Скажи это!
# Задницу! Да, задницу! Да!
    prisoner1 "Задницу, шлюха!"
    prisoner1 "Свою задницу!"
    prisoner1 "Скажи это!"
    prisoners "Задницу! Да, задницу!"
    prisoner1 "Да! Да!"

# Я... прошу разрешения показать свою... свою задницу...
    m "Я... прошу разрешения показать свою... свою задницу..."

# Да, jail_name хорошая шлюха! Да!
# Мы разрешаем тебе показать свою задницу, шлюха! Давай!
    prisoner1 "Да, [monica_jail_name] хорошая шлюха! Да!"
    prisoner1 "Мы разрешаем тебе показать свою задницу, шлюха! Давай!"

# Моника показывает свой зад
    m "!!!"

# Да, хорошая задница! Да!
    prisoner1 "Да, хорошая задница! Да!"

# Мы хотим потрогать ее! Да!
# Да! Потрогать! Мы хотим потрогать шлюху! Потрогать, да!
    prisoner1 "Мы хотим потрогать ее! Да!"
    prisoners "Да! Потрогать!"
    prisoners "Мы хотим потрогать шлюху!"
    prisoners "Потрогать, Да!"

# Нет! Ни за что! Я не дам Вам трогать меня!
    m "Нет! Ни за что! Я не дам Вам трогать меня!"

# Тогда ты будешь плохой шлюхой! А ты знаешь что будет с плохой шлюхой!
# Да! Плохая шлюха! Плохая! Нам не нужна плохая шлюха!
# Нам нужна хорошая шлюха, да!
    prisoner1 "Тогда ты будешь плохой шлюхой!"
    prisoner1 "А ты знаешь что будет с плохой шлюхой!"
    prisoners "Да! Плохая шлюха! Плохая!"
    prisoners "Нам не нужна плохая шлюха!"
    prisoners "Нам нужна хорошая шлюха! Да!"

# Хорошая шлюха идет к нам, чтобы мы потрогали ее, да!
    prisoners "Хорошая шлюха идет к нам, чтобы мы потрогали ее! Да!"

# Моника думает что это какой-то кошмар.
# Что чтобы выжить, ей приется дать себя облапать каким-то ничтожествам.
# Каким-то заключенным. Облапать ее, Монику Бакфетт!
# Как это может быть?! Неужели все это реальность?! О БОЖЕ!
    mt "Это какой-то кошмар... Я не могу в это поверить..."
    mt "Чтобы выжить, мне придется дать себя облапать каким-то ничтожествам..."
    mt "Каким-то заключенным... Облапать меня, Монику Бакфетт!!!"
    mt "Как такое может быть?! Неужели все это реальность?!"
    mt "О БОЖЕ!"

# Что же мне делать?!
    mt "Что же мне делать?"

# Подойти к заключенным.
# Поставить их на место!
    menu:
        "Подойти к заключенным.":
            pass
        "Поставить их на место!":
            return False

# Моника подходит к заключенным, спиной
# Ее лапают.
    m "..."
# Да! Хорошая! Шлюха!
# Шлюха хорошая! Да!
# И я хочу! И мне тоже дайте!
    prisoners "Да! Хорошая! Шлюха!"
    prisoners "Шлюха хорошая! Да!"
    prisoner3 "И я хочу! И мне тоже дайте!"
# И мне! И мне!
# Потрогать шлюху!
# О чередь! Шлюха одна, а нас много!
# Да, очередь! Очередь!
    prisoner5 "И мне!"
    prisoner6 "И мне!"
    prisoner2 "Потрогать шлюху!"
    prisoner1 "В очередь! Шлюха одна, а нас много!"
    prisoners "Да, очередь! Очередь!"

# Моника в шоке.
# Моника думает что я сплю, это какой-то кошмарный сон.
# Это не в реальности!
    mt "!!!"
    mt "Я сплю..."
    mt "Это какой-то кошмарный сон..."
    mt "Это не в реальности..."
    mt "Этого не может быть..."
    mt "Я... чувстую как каждый сантиметр моей кожи лапают эти грязные руки..."

# Кто-то кричит Боб! Боб идет!
# Быстро в камеры, ребята!
    prisoner6 "Боб! Боб идет!"
    prisoner1 "Быстро в камеры, ребята!"


# Моника может постучать в решетку и Боб кричит я занят, хватит шуметь!
    overseer "Я занят! Хватит шуметь!"
# Моника ложится спать и думает что надо заснуть, завтра я проснусь и этот кошмарный сон исчезнет.
    mt "Надо заснуть... Мне надо заснуть..."
    mt "Завтра я проснусь и этот кошмарный сон исчезнет..."

# С утра Моника встает и думает что надо позвать Боба, Мистер Маркус должен встретиться с ней!
    mt "Мне надо позвать Боба! Мистер Маркус должен встретиться со мной!"

# Приходит Боб.
# Моника спрашивает где Мистер Маркус?
# Боб отвечает что он еще занят и не распоряжался о встрече.
# Моника говорит скажите ему что я хочу встретиться с ним, пожалуйста!
    overseer "Чего тебе?"
    m "Где Мистер Маркус?"
    overseer "Мистер Маркус занят и не распоряжался о встрече."
    m "Боб, скажите ему, что я хочу встретиться с ним, пожалуйста!"
# Боб отвечает что это не его дело, но, вроде бы Мистер Маркус освободится завтра.
# И он может дать ей поесть, если та хочет.
# Либо не шуметь!
# Моника говорит что да, дай, пожалуйста, поесть. Боб уходит и приносит еду.
    overseer "Это не мое дело! Хотя, вообще-то, кажется я слышал Мистер Маркус освободится завтра."
    overseer "Я могу дать тебе поесть, если хочешь."
    overseer "Либо не шуми больше!"
    m "Да, Мистер Боб... Дайте, пожалуйста, мне поесть..."
    #Боб уходит и приносит еду.
# Итак, завтра! Завтра я встречусь с Мистером Маркусом и этот кошмар закончится, я уверена!
    mt "Итак, завтра!"
    mt "Завтра я встречусь с Мистером Маркусом и этот кошмар закончится, я уверена!"

# Моника ложится спать.
# Ее будят крики шлюха!
# Шлюха! Нам нужна наша шлюха!
    prisoners "Шлюха!"
    prisoners "Шлюха! Нам нужна наша шлюха!"

# Моника встает и кричит на них: что вам снова надо от меня!
# Нам нужна шлюха! jail_name, наша шлюха!
# Шлюха сегодня хорошая?! Или шлюха снова плохая?!
# Шлюха, отвечай!
    m "Что Вам снова надо от меня?!"
    prisoners "Нам нужна шлюха! [monica_jail_name], наша шлюха!"
    prisoner1 "Шлюха сегодня хорошая?"
    prisoner1 "Или шлюха снова плохая?!"
    prisoner1 "Шлюха, отвечай!"

# О БОЖЕ! Снова они!
# Что же мне делать?! Мне надо как-то дождать завтрашнего дня!
# Если они расскажут обо мне, то мне конец! Всего один день!
# Может быть стоит перетерпеть это? Эти унижения! Это путь к моей свободе!
# Мне надо пройти его! Но смогу-ли Я?!
    mt "О БОЖЕ! Снова они!"
    mt "Что же мне делать?! Мне надо как-то дождаться завтрашнего дня!"
    mt "Если они расскажут обо мне, то мне конец!"
    mt "Всего один день!"
    mt "..."
    mt "Может быть стоит перетерпеть это? Эти унижения..."
    mt "Это пусть к моей свободе..."
    mt "Мне надо прости его!"
    mt "Но смогу-ли Я?.."

# Притворяться шлюхой.
# Поставить их на место!
    menu:
        "Притворяться шлюхой.":
            pass
        "Поставить их на место!":
            return False

# Я... Я хорошая шлюха...
# Хорошая шлюха встанет на колени и повернется к нам задницей! Да!
# Мы предвкушаем твою задницу, шлюха!
# Достают члены
# Мы хотим получить удовольствие от нее, прямо сейчас!
    m "Я... Я хорошая шлюха..."
    prisoner1 "Хорошая шлюха встанет на колени и повернется к нам задницей! Да!"
    prisoner1 "Мы предвкушаем твою задницу, шлюха!"
# Достают члены
    prisoner1 "Мы хотим получить удовольствие от нее, прямо сейчас!"

# О БОЖЕ!
# Что Вы собираетесь делать?!
# Мы будем дрочить на тебя, шлюха! Скоро ты будешь наша!
# А пока мы хотим подрочить на твою задницу! Вставай своей задницей, сейчас же!
    mt "О БОЖЕ!"
    m "Что Вы собираетесь делать?!"
    prisoner1 "Мы будем дрочить, шлюха! Скоро ты будешь наша!"
    prisoner1 "А пока мы хотим подрочить на твою задницу!"
    prisoner1 "Вставай своей задницей, сейчас же!"

# Сделать как велят заключенные.
# Поставить их на место!
    menu:
        "Сделать как велят заключенные.":
            pass
        "Поставить их на место!":
            return False

# Моника встает на колени, голой попой к заключенным.
    m "..."
# Заключенные дрочат.
# Да, шлюха! Скажи! Скажи что эта шлюха и ее задница принадлежат нам!
# Скажи!
    prisoner1 "Да, шлюха!"
    prisoner1 "Скажи что эта шлюха и ее задница принадлежат нам!"
    prisoner1 "Скажи!"

# О БОЖЕ!! Неужели я скажу такое?!
    mt "О БОЖЕ! Неужели я скажу такое?!"

# Ну же, шлюха! Мы ждем!
    prisoner1 "Ну же, шлюха! Мы ждем!"

# Сказать что Моника шлюха и что ее задница принадлежит заключенным.
# Поставить их на место!
    menu:
        "Сказать что Моника шлюха и что ее задница принадлежит заключенным.":
            pass
        "Поставить их на место!":
            return False

# Главное - понтянуть время, Моника! Я скажу им все что угодно, чтобы выиграть время...
# Эта... Эта шлюха хорошая...
# Эта шлюха и ее задница... принадлежат вам...
    mt "Главное - потянуть время, Моника!"
    mt "Я скажу им все что угоодно, чтобы выиграть время..."
    m "Это... Эта шлюха хорошая..."
    m "Эта шлюха и ее задница... принадлежат вам..."

# Да! Хорошая шлюха!
# Хорошая шлюха, Да! Да!

# Скажи что эта задница всегда будет к нашим услугам, скажи!
# Скажи! Скажи! Задница! Скажи!
    prisoners "Да! Хорошая шлюха!"
    prisoners "Хорошая шлюха! Да! Да!"
    prisoner1 "Скажи что эта задница всегда будет к нашим услугам! Скажи!"
    prisoners "Скаж! Скажи! Задница! Скажи!"

# Сказать что попа Моники всегда к услугам заключенных.
# Поставить их на место!
    menu:
        "Сказать что попа Моники всегда к услугам заключенных.":
            pass
        "Поставить их на место!":
            return False

# Как я могу сказать такое?! Неужели я это сделаю?!
# Это все сон! Это какой-то кошмар! Я не верю в то что это происходит!
    mt "Как я могу сказать такое?! Неужели Я это сделаю?!"
    mt "Это все сон!"
    mt "Это какой-то кошмар!"
    mt "Я не верю в то что это просходит на самом деле!"

# Ну же, шлюха!
# Мы ждем!
    prisoner1 "Ну же, шлюха!"
    prisoner1 "Мы ждем!"

# Задница этой шлюхи всегда к вашим услугам...
# В любое время, шлюха! Скажи это!
    m "Задница этой шлюхи всегда к Вашим услугам..."
    prisoner1 "В любое время, шлюха! Скажи это!"

# Задница этой шлюхи всегда к вашим услугам... в лобое время...
    m "Задница этой шлюхи всегда к Вашим услугам... в любое время..."

# Да! Шлюха! Да!
# Кончают...
# Хорошая шлюха! Хорошая! Да!
# Скоро мы вставим свои члены в эту аппетитную задницу! Да!
    prisoners "Да! Шлюха! Да!"
    # Кончают...
    prisoners "Хорошая шлюха! Хорошая! Да!"
    prisoner1 "Скоро мы вставим свои члены в эту аппетитную задницу! Да!"
# Скажи, шлюха! Скажи, что ты ждешь наши члены в своей заднице!
# Скажи это, шлюха!
    prisoner1 "Скажи, шлюха! Скажи что ты ждешь наши члены в своей заднице!"
    prisoner1 "Скажи это, шлюха!"
# m "!!!"
# Нет!!!
    mt "!!!"
    m "Нет!!!"
# Скажи, шлюха! А не то ты станешь плохой шлюхой!
# Да! Да! Плохая шлюха, да!
    prisoner1 "Скажи, шлюха! А не то ты станешь плохой шлюхой!"
    prisoners "Да! Да! Плохая шлюха! Да!"

# О БОЖЕ!!! Что мне делать?!
    mt "О БОЖЕ!!! Что мне делать?!"

# Сказать что Моника ждет члены заключенных в своей попе
# Поставить их на место!
    menu:
        "Сказать что Моника ждет члены заключенных в своей попе.":
            pass
        "Поставить их на место!":
            return False

# Я... Я жду ваши члены...
# Где?! Где ты ждешь наши члены, шлюха?! Отвечай нам!
    m "Я... Я жду Ваши члены..."
    prisoner1 "Где?! Где ты ждем наши члены, шлюха?! Отвечай нам!"

# Я... Я жду ваши члены... в своей попе...
# О БОЖЕ!!!
    m "Я... Я жду Ваши члены... в своей попе..."
    mt "О БОЖЕ!!!"

# Скажи, скажи что ты хочешь, чтобы они поскорее оказались там!
# Скажи это!
    prisoner1 "Скажи, скажи что ты хочешь, чтобы они поскорее оказались там!"
    prisoner1 "Скажи это!"

# Как я могу такое сказать?! Но мне не важно что я говорю...
# Все-равно этого никогда не будет... А мне надо выиграть время...
# Всего-лишь время!
    mt "Как я могу такое сказать?! Но мне не важно что я говорю..."
    mt "Все-равно этого никогда не будет... А мне надо выиграть время..."
    mt "Всего-лишь время!"

# Я... Я жду ваши члены... в своей попе...
# Я... Я хочу, чтобы они поскорее оказались там...
    m "Я... Я жду Ваши члены... в своей попе..."
    m "Я... Я хочу, чтобы они поскорее оказались там..."

# Да, хорошая шлюха! Да! До завтра, шлюха!
# Завтра ты будешь сосать наши члены!
# У всех нас, одновременно!
# Да! Да! Хорошая шлюха!
# Одновременно, сосать, да!
    prisoner1 "Да, хорошая шлюха! Да!"
    prisoner1 "До завтра, шлюха!"
    prisoner1 "Завтра ты будешь сосать наши члены!"
    prisoner1 "У всех нас, одновременно!"
    prisoners "Да! Да! Хорошая шлюха!"
    prisoners "Одновременно, сосать, Да!"

# НЕТ!!!
# О БОЖЕ!!!
# Я не буду делать этого!!!
    m "НЕТ!!!"
    m "О БОЖЕ!!!"
    m "Я не буду делать этого!!!"

# Ты будешь! Иначе ты будешь плохой шлюхой, да!
# Скажи это! Скажи что ты будешь сосать наши члены завтра!
# Скажи! Мы хотим это услышать!
    prisoner1 "Ты будешь! Иначе ты будешь плохой шлюхой, Да!"
    prisoner1 "Скажи это! Скажи что ты будешь сосать наши члены завтра!"
    prisoner1 "Скажи! Мы хотим услышать это!"

# Да! Да!
# Услышать! Да!
    prisoners "Да! Да!"
    prisoners "Услышать! Да!"

# О БОЖЕ!
# Что мне делать?!
# Завтра Мистер Маркус примет меня.
#Мне надо сказать что угодно, чтобы они отстали от меня!
    mt "О БОЖЕ!"
    mt "Что мне делать?!"
    mt "Завтра Мистер Маркус примет меня."
    mt "Мне надо сказать что угодно, чтобы они отстали от меня!"

# Сказать что завтра Моника будет сосать члены заключенных.
# Поставить их на место!
    menu:
        "Сказать, что завтра Моника будет сосать члены заключенных.":
            pass
        "Поставить их на место!":
            return False

# Я... Я буду сосать Ваши члены... Завтра...
# Одновременно! Одновременно все наши члены! Да!
# Я... Я буду сосать завтра все Ваши члены... Одновременно...
    m "Я... Я буду сосать Ваши члены... Завтра..."
    prisoner1 "Одновременно! Одновременно все наши члены! Да!"
    m "Я... Я буду сосать завтра все Ваши члены... Одновременно..."

# Да! Хорошая шлюха!
# Да!
# Шлюха может отдыхать на сегодня! Да!
# Мы придем к шлюхе завтра! Да!
    prisoner1 "Да! Хорошая шлюха!"
    prisoners "Да!"
    prisoner1 "Шлюха может отдыхать на сегодня! Да!"
    prisoners "Мы придем к шлюхе завтра! Да!"

# О Боже! Что я сказала?!
# Но какая разница?!
# Завтра я встречусь с Маркусом и этот кошмар закончится!
# Мне надо спать! Я хочу поскорее уснуть!
    mt "О Боже! Чтоя сказала?!"
    mt "Но какая разница?!"
    mt "Завтра я встречусь с Маркусом и это кошмар закончится!"
    mt "Мне надо спать! Я хочу поскорее уснуть!"

# Моника ложится спать.
# Я наговорила кучу ерунды сегодня.
# Но это не важно. Все это не уйдет дальше этих жутких стен.
# А для меня главное - это выбраться отсюда.
# И завтра я добьюсь своей цели!
    mt "Я наговорила кучу ерунды сегодня."
    mt "Но это не важно. Все это не уйдет дальше этих жутких стен."
    mt "А для меня главное - это выбраться отсюда."
    mt "И завтра я добьюсь своей цели!"

# Утро
# Мне надо позвать Боба.
# Мне надо встретиться с Мистером Маркусом скорее!
    mt "Мне надо позвать Боба."
    mt "Мне надо встретиться с Мистером Маркусом скорее!"

# Боб приходит. Чего тебе?!
# Я хочу встретиться с Мистером Маркусом!
# Мистер Маркус сегодня снова занят.
# КАК?! НЕТ!!!
# МИСТЕР МАРКУС ДОЛЖЕН МЕНЯ СЕГОДНЯ ПРИНЯТЬ!
# ПОЖАЛУЙСТА!!!
# МИСТЕР БОБ!!!
    overseer "Чего тебе?!"
    m "Я хочу встретиться с Мистером Маркусом!"
    overseer "Мистер Маркус сегодня занят."
    m "КАК?! НЕТ!!!"
    m "МИСТЕР МАРКУС ДОЛЖЕН МеНЯ СЕГОДНЯ ПРИНЯТЬ!"
    m "ПОЖАУЛЙСТА!!!"
    m "МИСТЕР БОБ!!!"
# Мистер Маркус сказал что примет тебя завтра!
# Подожди еще один день!
# НЕТ! МИСТЕР БОБ!
# ВЫ НЕ ПОНИМАЕТЕ! МНЕ НУЖНО ВСТРЕТИТЬСЯ С НИМ СЕГОДНЯ!
# МНЕ НЕЛЬЗЯ ЖДАТЬ ЕЩЕ ОДИН ДЕНЬ!
    overseer "Мистер Маркус сказал что примет тебя завтра!"
    overseer "Подожди еще один день."
    m "НЕТ! МИСТЕР БОБ!"
    m "ВЫ НЕ ПОНИМАЕТЕ! МНЕ НУЖНО ВСТРЕТИТЬСЯ С НИМ СЕГОДНЯ!"
    m "МНЕ НЕЛЬЗЯ ЖДАТЬ ЕЩЕ ОДИН ДЕНЬ!"
# Это меня не касается!
# Ты будешь жрать или нет?!
# Я... Я... Что?
# Я спрашиваю ты будешь жрать?! Или мне уйти?!
# Да, мистер Боб... Спасибо...
    overseer "Это меня не касается!"
    overseer "Ты будешь жрать или нет?!"
    m "Я... Я... Что?"
    overseer "Я спрашиваю ты будешь жрать?! Или мне уйти?"
    m "Да, Мистер Боб... Спасибо..."

# О БОЖЕ!
# Еще один день!
# Мне надо пораньше лечь спать. Этот день быстро пролетит.
# Еще одна ночь и я встречусь с Мистером Маркусом.
# И все это закончится!
    mt "О БОЖЕ!"
    mt "Еще один день!"
    mt "Мне надо пораньше лечь спать."
    mt "Этот день быстро пролетит."

# Я лягу спать пораньше...

# Моника ложится спать. Просыпается от шума заключенных.

# Шлюха! Шлюха! Мы пришли к тебе!
# Шлюха!

# О БОЖЕ!!! Я совсем забыла!
# Они снова пришли!
# Я... О БОЖЕ!!! Что я пообещала им вчера?!
# Что же мне делать?!

# Что Вам снова надо?! Зачем Вы снова пришли сюда!
# Уходите!

# Мы пришли к нашей шлюхе! Да!
# К хорошей шлюхе! Которая будет сосать наши члены сегодня!
# Достают члены
# Да! Да! Сосать!

# Я не буду делать этого! Никогда, Вы слышите?!
# Ты будешь сосать! Будешь! Иначе ты плохая шлюха!
# Да!
# Ты надоела нам! Если ты будешь плохой шлюхой, мы все расскажем детективу про тебя!

# НЕТ! Вы не сделаете этого!

# Если шлюха будет хорошей, мы не будем этого делать!
# Садись на колени и соси наши члены!
# Будь хорошей шлюхой, jail_name

# НЕТ! Я не буду! Ни за что!!!

# Тогда мы уходим! Позовите детектива, ребята!
# Да, мы пошли звать детектива.
# Плохая шлюха!

# Уходят

# Нет! Стойте!
# Не делайте этого!

# Мы сделаем это! Ты плохая шлюха!
# Да! Да!
# Мы сделаем это!

# Не делайте!
# Я... Я...

# Возвращаются
# Ты? Что ты?!
# Мы знаем что ты шлюха!
# Но ты хорошая шлюха или плохая?!
# Отвечай!

# Сделать что они хотят.
# Поставить их на место!

# Я... Я...
# Ну же!
# Я... Я хорошая шлюха...

# Вставай на колени и соси наши члены!
# Хорошая шлюха обещала сосать их сегодня!

# Я...

# Всавай на колени!

# Моника встает на колени

# Принимай мой член! Давай, скорее!
# А то я сейчас кончу тебе на лицо.

# Что здесь за беспорядок?! Заходит Боб.
# Боб, мы пришли к нашей шлюхе! Ты обещал, Боб!

# Я пущу Вас к ней после того, как она побывает у Мистера Маркуса!
# Но Боб! Мы не занимаемся с ней сексом! Она просто сосет наши члены!
# Она сама хочет этого!
# Сама?
# Да, эта шлюха сама этого хочет!
# Да, шлюха?! Отвечай!
# Я... Я...
# Отвечай, шлюха! Ты знаешь что надо ответить, чтобы быть хорошей шлюхой!
# И ты знаешь что будет с плохой шлюхой!
# Ты знаешь это!
# Я... Я...
# Мистер Боб... Я... Их члены...
# Ну же, шлюха!
# Я хочу их члены... сосать...
# Видишь, Боб?
# Она сама хочет! Открой нам дверь!
# Мы хотим попасть к ней! Это неудобно делать через решетку!
# Наши члены не такие длинные! Нам неудобно, Боб!
# overseer "И что, ты правда сама этого хочешь?"
# Тебя никто не заставлял?
# Нннет... Мистер Боб...
# Мммменя... Никто... Не заставлял...
# Ну хорошо, я открою. Только давайте быстро! Скоро отбой!
# И у меня начинает болеть голова из-за вас!
# У Вас есть 10 минут!
# Да! Ура! Ребята, залетай!

# Да, хорошая шлюха! Соси! Соси наши члены!
# Да!
# Давай, да!
# Моника сосет кучу членов.
# Эй, моя очередь.
# Эй, посторонись, дай мне тоже вставить член ей в ротик.
# Да, какой ротик.
# Как приятно, ребята, да!
# ААааахххх!
# Эй! Кончай на нее! Не разбрызгивай на нас!
# Моя очередь!
# ААааааааххх!
# Эй! Подвинься!
# Продвигайтесь быстрее! Мы тоже ждем!
# ААааааааххх!
# Следующий!
# Кто закончил, отходите в сторону!
# ААааааааххх!
# Не задерживайте очередь!
# Ну же! Кончай скорее!
# Я почти!
# Давай! Долби ее активнее!
# ААааааааххх!
# Следующий!
# Эй! Ты куда лезешь!
# Ты после меня!
# ААааааааххх!
# Время!
# Скорее, скорее!
# Дай мне!
# Я еще не все!
# Дай я тогда тоже засуну!
# Я должен успеть!
# Да, давай, растягивай ей ротик!
# ААааааааххх!
# ААааааааххх!
# Все, брысь отсюда!
# О БОЖЕ!!! Что это было...
# У меня сводит челюсть, я не могу пошевелить ей...
# А это что?! # Боб стоит с членом
# Боб?!
# Ну ты любишь делать это... Ты сама сказала...
# И я подумал, что...
# Уйди отсюда, Боб!
# Никогда в жизни я не буду этого делать!
# Мерзавцы!
# Твари!
# Ладно, ладно, ухожу...

# Моника ложится спать...
# Я не могу поверить... Их... Столько...
# Я...
# Как такое могло случиться...
# И... Как я выдержала это...
# Мне надо лечь спать...
# Не могу поверить что я решилась на это...
# Как такое могло случиться?
# Мне лучше об этом забыть...
# Я сплю...

# Утро
# Мне надо позвать Боба. Мистер Маркус должен встретиться со мной!
# Мистер Маркус ждет тебя!
# Иди за мной!
# Ура! Наконец-то!
# Наконец-то я покину это жуткое место!
# Наконец-то!

# Моника идет вдоль заключенных. Они кричат хорошая шлюха (или молчат)












#
