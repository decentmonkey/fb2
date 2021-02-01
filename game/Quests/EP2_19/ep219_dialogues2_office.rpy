define ryan = Character(_("Райен"), who_color=c_blue)  # Guest4 (Ryan), фотограф Кэмпбелла
define beatrice = Character(_("Беатрис"), who_color=c_blue)  # Beatrice, ассистентка Кэмпбелла

default monicaCampbellOfficePhotoshoot1 = 0 # Моника сразу согласилась поехать на фотосессию в офис Кэмпбелла
default monicaCampbellOfficePhotoshoot2 = 0 # Моника согласилась поехать на фотосессию в офис Кэмпбелла со 2-го раза
default monicaCampbellOfficePhotoshoot3 = 0 # Моника согласилась на фотосессию в раме
default monicaCampbellOfficePhotoshoot4 = 0 # сотрудники Моники сплетничают о фотосессии в раме


# при условии, что была встреча с инвестором и Линдой в кабинете Бифа
# Моника в др. день заходит к Бифу
label ep219_dialogues2_office_1:
	# как обычно подходит к нему
    m "Биф..."
    m "Ты говорил, что есть работа для меня..."
    # Биф нетерпеливо перебивает ее
    biff "Да-да!"
    biff "Для тебя, цыпочка, сегодня есть очень важная работа!"
    mt "Мне это уже не нравится!"
    mt "!!!"
    m "Что за работа?"
    m "Снова какая-нибудь дурацкая презентация?!"
    # Биф наставническим тоном
    biff "Что значит, дурацкая презентация?"
    biff "Ну хорошо, папочка добрый сегодня..."
    biff "Поэтому он будет терпеливым и попытается донести до цыпочки всю важность..."
    m "Я знаю, Биф!"
    m "Давай к делу!"
    m "Что за важная работа?!"
    # Биф недоволен, что она его перебила
    biff "Фотосессия."
    m "Так бы сразу и сказал, Биф."
    m "Тогда я пошла в фотостудию."
    # Моника разворачивается, чтобы уйти, но Биф ее останавливает
    biff "А ну-ка стой!!!"
    # Моника закатывает глаза
    mt "Чего еще этому недоумку нужно от меня?!"
    mt "!!!"
    # поворачивается к Бифу
    m "Что?"
    biff "Что-то я не понял!.."
    biff "Ты чего тут строишь из себя важную персону, а?"
    biff "Настолько вошла в роль?!"
    biff "Посидела своей двадцатидолларовой задницей в МОЕМ кресле..."
    biff "И думаешь, что ты можешь себя вести как настоящая Бакфетт?!"
    biff "Ты совсем охренела, кукла, так со мной разговаривать?!"
    biff "Зазвездившаяся дешевая уличная шлюшка!"
    m "Хватит называть меня так, Биф! Я не!.."
    biff "Молчать!!!"
    biff "Здесь Я решаю, кого и как мне называть!"
    biff "Я здесь БОСС!!!"
    m "!!!"
    biff "Какого черта ты уходишь из моего кабинета, не дослушав меня?!"
    m "..."
    biff "Вот и правильно! Стой и молчи!"
    biff "Намного умнее выглядишь, когда не открываешь свой рот!"
    m "!!!"
    # Биф снова расслаблено откидывается на кресло и объясняет Монике ее работу
    biff "В общем, слушай, кукла..."
    biff "Как ты знаешь, наш многоуважаемый Мистер Кэмпбелл является владельцем крупной дизайнерской студии."
    biff "Он уже предоставлял великолепную дизайнерскую одежду нам для работы..."
    m "Мне что, снова нужно будет надевать его пошлые костюмы?!"
    m "Я не!.."
    # Биф на нее рявкает
    biff "Закрой свой рот!"
    biff "Еще раз перебьешь меня - накажу!"
    m "!!!"
    biff "Мистер Кэмпбелл обратился ко мне с интересным предложением."
    biff "Так как его студия занимается дизайном не только одежды, но и разными другими дизайнерскими штуками..."
    biff "Он мне предложил помочь ему в создании рекламного проекта какой-то очередной ерунды, которую он выпустил."
    biff "Я не вдавался в подробности, что это. Но точно знаю, что не одежда."
    biff "В общем, тебе нужно будет сделать снимки для рекламы этой ерунды."
    biff "И часть из этих снимков мы разместим в моем журнале..."
    biff "Тебе все ясно, кукла?"
    m "Нет!"
    m "Вообще ничего не ясно!"
    m "В каком формате будет проходить фотосессия и с каким реквизитом?"
    biff "Вот только не надо тут корчить из себя всезнающую модель!"
    biff "Приедем и разберемся на месте!"
    m "В смысле? Куда приедем?"
    m "Это что, выездная фотосессия?"
    biff "Ага..."
    biff "Собирайся и поехали."
    biff "Мистер Кэмбелл нас уже ждет в своем офисе."
    m "Он что, будет присутствовать на фотосессии?"
    biff "Ты совсем глупая, кукла?!"
    biff "Ты думаешь, что тебе выдадут эту дизайнерскую хреновину и дадут в руки камеру, чтобы ты сама сделала селфи?!"
    m "!!!"
    biff "Конечно, он будет присутствовать! Мистер Кэмпбелл лично будет контролировать ход фотосессии!"
    biff "Какая же ты безмозглая, я удивляюсь!"
    biff "Тебе с твоими мозгами, вернее с их полным отсутствием, до настоящей Бакфетт далеко!"
    mt "Скотина!"
    mt "!!!"
    #corruption
    menu:
        "Поехать на фотосессию.":
            $ monicaCampbellOfficePhotoshoot1 = day # Моника сразу согласилась поехать на фотосессию в офис Кэмпбелла
            pass
        "Отказаться.":
            mt "Черт! Выездная фотосессия в офисе Кэмпбелла!"
            mt "Не нравится мне все это!"
            mt "Тут однозначно есть какой-то подвох!"
            mt "Лучше я откажусь сразу от этой очередной бредовой идеи Бифа!"
            mt "!!!"
            m "Биф, я не буду проводить фотосессию в присутствии этого инвестора!"
            m "Тем более, в его офисе!"
            m "Я не хочу, чтобы он на меня пялился!"
            m "Почему я?! Почему не Мелани?"
            biff "Потому что Мистер Кэмпбелл так хочет."
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            mt "Чертов Мистер Кэмпбелл! Чертов Биф! Ненавижу их всех!"
            mt "!!!"
            # Моника уходит (Биф не будет давать ей фотосессии, пока она не проведет эту)
            return False
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "А мне нужны деньги..."
    mt "Где я смогу заработать $ 5 000 в месяц для сучки Виктории?"
    mt "К тому же я решила притворяться перед Бифом, что я слушаюсь его..."
    mt "Чтобы усыпить его бдительность и, перехитрив его в подходящий момент, выгнать вон из моего офиса!"
    mt "..."
    m "Я проведу эту фотосессию..."
    # довольный Биф встает с кресла и подходит к Монике
    biff "Отлично. Папочка доволен, что цыпочка решила стать снова хорошей..."
    biff "И перестала спорить с папочкой."
    menu:
        "Сказать, что Моника хорошая цыпочка.":
            m "Да..."
            m "Я хорошая цыпочка..."
            pass
        "Промолчать.":
            mt "Да пошел ты, придурок!"
            m "..."
            pass
    # Биф хлопает Монику по попе
    m "!!!"
    biff "Поехали, цыпочка."
    biff "Мистер Кэмпбелл звонил и сказал, что фотограф уже на месте."
    m "???"
    m "Какой еще фотограф? Алекс?"
    biff "Нет, Алекс не работает у Кэмпбелла, если ты не заметила, кукла."
    biff "Фотосессию будет проводить другой фотограф, которого специально для этой фотосессии нанял Мистер Кэмпбелл."
    biff "Все, хватит болтать! Нас ждут."
    biff "Иди за мной!"
    mt "Черт!"
    mt "Что еще за фотограф?!"
    mt "Не нравится мне все это..."
    return


# если Моника отказалась фотографироваться в этом платье и оказалась на улице, но потом передумала и пришла к Бифу
# офис, кабинет Бифа
label ep219_dialogues2_office_2:
    m "Биф..."
    m "Мне нужна работа."
    biff "Если цыпочка хочет работать, она сделает фотосессию."
    biff "В офисе Мистера Кэмпбелла и в его присутствии."
    m "..."
    biff "Ты согласна?"
    mt "!!!"
    #corruption
    menu:
        "Поехать на фотосессию.":
            $ monicaCampbellOfficePhotoshoot2 = day # Моника согласилась поехать на фотосессию в офис Кэмпбелла со 2-го раза
            pass
        "Отказаться.":
            mt "Черт! Выездная фотосессия в офисе Кэмпбелла!"
            mt "Не нравится мне все это!"
            mt "Тут однозначно есть какой-то подвох!"
            mt "!!!"
            m "Биф, я не буду проводить фотосессию в присутствии этого инвестора!"
            m "Тем более, в его офисе!"
            m "Я не хочу, чтобы он на меня пялился!"
            m "Почему я?! Почему не Мелани?"
            biff "Потому что Мистер Кэмпбелл так хочет."
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            mt "Чертов Мистер Кэмпбелл! Чертов Биф! Ненавижу их всех!"
            mt "!!!"
            # Моника уходит
            return
    mt "Дъявол!"
    mt "Он вышвырнет меня с работы, если я откажусь."
    mt "А мне нужны деньги."
    mt "Где я смогу заработать $ 5 000 в месяц для сучки Виктории?"
    mt "К тому же я решила притворяться перед Бифом, что я слушаюсь его..."
    mt "Чтобы усыпить его бдительность и, перехитрив его в подходящий момент, выгнать вон из моего офиса!"
    mt "..."
    m "Я проведу эту фотосессию..."
    # Биф встает с кресла и подходит к Монике
    biff "Отлично. Папочка доволен, что цыпочка решила стать снова хорошей..."
    biff "И перестала спорить с папочкой."
    menu:
        "Сказать, что Моника хорошая цыпочка.":
            m "Да..."
            m "Я хорошая цыпочка..."
            pass
        "Промолчать.":
            mt "Да пошел ты, придурок!"
            m "..."
            pass
    # Биф хлопает Монику по попе
    m "!!!"
    biff "Поехали, цыпочка."
    biff "Я сейчас позвоню Мистеру Кэмпеллу и предупрежу, что мы едем."
    biff "Надеюсь, фотограф успеет прибыть к нашему приезду."
    # если Моника сорвала фотосессию в первый раз, то просто уходят
    biff "Все, хватит болтать! Нас ждут."
    biff "Иди за мной!"
    mt "Черт!"
    mt "!!!"
    #
    # если еще не была в офисе Кэмпбелла, то говорят про фотографа
    m "???"
    m "Какой еще фотограф? Алекс?"
    biff "Нет, Алекс не работает у Кэмпбелла, если ты не заметила, кукла."
    biff "Фотосессию будет проводить другой фотограф, которого специально для этой фотосессии нанял Мистер Кэмпбелл."
    biff "Все, хватит болтать! Нас ждут."
    biff "Иди за мной!"
    mt "Черт!"
    mt "Что еще за фотограф?!"
    mt "Не нравится мне все это..."
    # затемнение, звук мотора
    return

# фотостудия Кэмпбелла
label ep219_dialogues2_office_3:
    # спустя некоторое время Моника с Бифом заходят в студию Кэмпбелла
    # к ним с важным видом подходит ассистентка Кэмпбелла, она в очках, в руках папка
    beatrice "Добрый день! Миссис Бакфетт, полагаю?"
    # Биф, жадно пожирая ее глазами
    biff "Добрый день, Мисс!"
    biff "Передайте Мистеру Кэмпбеллу, что прибыла Миссис Бакфетт и Мистер Биф..."
    # секретарша продолжает важно
    beatrice "Я Беатрис. Являюсь ассистентом Мистера Кэмпбелла."
    beatrice "Я тоже буду присутствовать на сегоднящней фотосессии." # она неприязненно смотрит на Монику
    mt "!!!"
    mt "А ей какого черта нужно присутствовать?!"
    mt "Может, вообще весь коллектив соберется?!"
    mt "Что за бред?!"
    # Беатрис разворачивается и говорит на ходу
    beatrice "Пойдемте за мной. Я проведу вас."
    # Биф смотрит на ее попу и шепчет Монике
    biff "Вот это ассистентка!"
    biff "Вот бы мне такую! На место Сиськи, например..."
    m "Биф!"
    mt "Похотливое животное!"
    mt "!!!"
    # Биф смотрит на Монику
    biff "Пошли, цыпочка."
    biff "И я тебя предупреждаю сразу! Никаких глупостей!"
    biff "Эта фотосессия должна пройти без накладок!"
    biff "Если ты сделаешь что-то не так и сорвешь ее..."
    biff "Дорогу в мой офис можешь забыть!"
    biff "Поняла меня?!"
    m "..."
    menu:
        "Да.":
            m "Да..."
            pass
        "Промолчать.":
            mt "Да пошел ты, придурок!"
            m "..."
            pass
    biff "Все, пошли!"
    # они идут вслед за Беатрис
    # затемнение, звук шагов
    # смена кадра на конференц-зал
    # Беатрис, Моника и Биф выходят на сцену, где их стоят и ждут Кэмпбелл и фотограф Райен (Guest4 с паблик ивента)
    # на сцене уже все готово для фотосессии, в т.ч. рама
    # Моника в недоумении оглядывается
    # Беатрис с важным видом подходит к Кэмпбеллу
    beatrice "Мистер Кэмпбелл, они прибыли..."
    campbell "Спасибо, Беатрис."
    # Биф, следом Моника тоже подходят к нему
    biff "Здравствуйте, Мистер Кэмпбелл!"
    biff "Очень рад встрече с вами и..."
    # пялясь на Беатрис
    biff "И вашими сотрудниками!"
    campbell "Здравствуйте, Мистер Биф."
    campbell "Миссис Бакфетт, рад, что вы согласились на эту фотосессию."
    # Кэмпбелл делает жест рукой в сторону Райена
    campbell "Сегодня мы будем сотрудничать с одним из лучших фотографов нашего города."
    campbell "Знакомтесь, Мистер Райен."
    ryan "Добрый день, Миссис Бакфетт."
    ryan "Рад встрече с вами."
    m "Здравствуй, Райен..."
    mt "Вот черт!"
    mt "Этот никчемный Райен будет проводить фотосессию?!"
    mt "В прошлый раз он взял на себя наглость критиковать работу Алекса!"
    #
    $ notif(_("Моника разговаривала с Райеном на мероприятии в клубе Кэмпбелла."))
    #
    mt "А потом говорил, что видел мои снимки с закрытой фотосессии!!"
    mt "Самодовольный индюк!"
    ryan "Давно мечтал поработать с вами, Миссис Бакфетт."
    # Кэмпбелл говорит Райену
    campbell "Райен, можете приступать к работе."
    campbell "Мы с Мистером Бифом и Беатрис будем наблюдать за процессом с зала." # показывает на кресла в первом ряду перед сценой
    # потом поворачивается к Монике
    campbell "Миссис Бакфетт, скорее всего, Мистер Биф рассказал вам, какого рода снимки мне нужны..."
    campbell "Но я уточню, что это..." # показывает рукой на раму
    campbell "Это очень дорогая дизайнерская рама для картины."
    campbell "Мои лучшие дизайнеры провели тщательную и кропотливую работу..."
    campbell "Чтобы сделать ее неповторимой и потрясающе прекрасной."
    campbell "Это ваш реквизит для съемок, Миссис Бакфетт."
    # Моника с недоумением смотрит на раму
    mt "Обычная рама... Не вижу в ней ничего потрясающего и неповторимого."
    mt "Моника Бакфетт снимается для рекламы дурацкой рамы!"
    mt "Какой-то идиотизм!"
    mt "И еще этот Райен! Он меня раздражает!"
    mt "Одно дело работать с Алексом. Ему можно сказать, чтобы он не брал какие-то определенные ракурсы..."
    mt "Может, у меня получится также руководить и этим Райеном?.."
    # Кэмпбелл прерывает ее мысли
    campbell "Можете приготовиться к съемке, Миссис Бакфетт..."
    m "А где я могу переодеться и где костюм для съемки?"
    campbell "Мистер Биф не сказал вам?"
    campbell "Рама - единственный ваш реквизит. Никакой одежды."
    m "?!"
    m "В смысле?"
    campbell "Миссис Бакфетт, это реклама рамы, а не одежды."
    campbell "Любая одежда будет только отвлекать от изысканного дизайна рамы."
    m "!!!"
    campbell "Готовьтесь к съемке, Миссис Бакфетт. Мы скоро начинаем."
    campbell "Пойдем, Беатрис. Мистер Биф, присоединяйтесь к нам в зале."
    biff "Одну минуту, Мистер Кэмпбелл..."
    # Кэмпбелл идет к выходу со сцены, чтобы сесть в зрительном зале
    # Беатрис говорит Монике
    beatrice "И поаккуратнее с реквизитом, Миссис Бакфетт!"
    beatrice "Эта рама стоит целое состояние!"
    m "!!!"
    # потом с гордым видом идет вслед за Кэмпбеллом
    # Моника все еще пребывает в шоке, смотрит им вслед
    # Райен отходит к оборудованию и реквизиту, подготавливая камеру
    # Биф подбегает к Монике, они разговаривают в стороне от всех, так что их никто не слышит
    biff "Так, цыпочка!"
    biff "Ты все слышала."
    biff "Давай, раздевайся и за работу! Не заставляй папочку и Мистера Кэмбелла ждать!"
    m "Раздеваться?!"
    m "Какого черта, Биф, я узнаю об этом здесь?!"
    m "?!"
    biff "Это твоя работа! Ты получаешь за это немаленькие деньги!"
    biff "А если будешь спорить!.."
    biff "Я не заплачу тебе ни цента!"
    biff "Так что не порть папочке настроение!"
    biff "Если хочешь и дальше зарабатывать неоправданно большие деньги..."
    biff "Только за то, что кривляешься перед камерой!"
    biff "То закрой свой рот и будь хорошей цыпочкой!"
    biff "Сорвешь съемку - сразу же позвоню охране в мой офис и тебя туда больше не пустят!"
    biff "Поняла меня?"
##### с этого момента начинается сцена, если Моника сорвала съемку в первый раз + # некоторое время спустя
    biff "Раздевайся! Тебя все ждут!"
    m "!!!"
    #corruption
    menu:
        "Провести фотосессию.":
            $ monicaCampbellOfficePhotoshoot3 = day # Моника согласилась на фотосессию в раме
            pass
        "Отказаться!":
            m "Биф, я не буду фотографироваться голой!"
            m "Да еще в присутствии этого инвестора и этого фотографа!"
            m "И этой жирной коровы!"
            m "Я не хочу, чтобы они на меня пялились!"
            m "И указывали мне, что делать!"
            biff "Ты не получишь никакую другую работу..."
            biff "Пока не проведешь эту фотосессию!"
            biff "Кукла безмозглая!"
            biff "Если будешь и дальше спорить со мной..."
            biff "Я заставлю тебя фотографироваться с членом во рту!"
            # Моника идет к выходу
            m "Да пошел ты!!!"
            m "!!!"
            # Моника оказывается на улице
            # Биф не дает ей работу, пока она не сделает эту фотосессию
            return
    # Моника зло смотрит на него
    mt "Гребаный Биф!"
    mt "Убью его!"
    mt "!!!"
    mt "Я, Моника Бакфетт, буду сниматься обнаженной!"
    mt "В какой-то безвкусной, отвратительной раме!!!"
    mt "Что делать, Моника?!"
    mt "Сволочь Биф сказал, что не пустит меня в офис!"
    mt "Черт-черт-черт!!!"
    mt "!!!"
    # задумчиво смотрит на раму
    mt "Может, я смогу принимать такие позы, в которых из-за чертовой рамы ничего не будет видно?.."
    mt "И попрошу этого придурка Райена делать соответствующие кадры..."
    mt "..."
    mt "Я не могу из-за какой-то фотосессии сорвать свой план!"
    mt "Мне нужно вернуть себе все, что у меня отняли!"
    mt "А для этого необходимо мое присутствие в моем офисе!"
    mt "В конце концов, это МОЙ офис и МОЙ журнал!"
    mt "!!!"
    # Моника зло говорит Бифу
    m "Я проведу эту фотосессию!"
    # Биф радостно
    biff "Отлично, цыпочка!"
    biff "Папочка рад, что у тебя хватило мозгов не сорвать съемку!"
    biff "Раздевайся и лезь в эту дизайнерскую хреновину!"
    # Биф уходит, Моника с ненавистью смотрит ему вслед
    # затемнение, звук одежды
    # смена кадра
    # Моника стоит на сцене, на съемочной площадке голая, прикрываясь руками
    # Биф с самодовольной миной смотрит на нее из зала, сидя рядом с Кэмпбеллом
    # Кэмпбелл сидит в центре, сбоку Биф, со второго боку - Беатрис
    # Беатрис смотрит на Монику с неприязнью
    mt "Боже! Чувствую себя отвратительно!"
    mt "!!!"
    # если танцевала на сцене паба голой
    mt "Конечно, мне не впервые находиться на сцене без одежды..."
    mt "Но в этой грязной дыре, которую извращенка Эшли называет баром..."
    mt "Никто не знает, кто я такая на самом деле."
    mt "А здесь!.."
    #
    mt "Так, Моника, соберись! Возьми себя в руки!"
    mt "Ты профессионал! Ты справишься!"
    # Райен держит камеру в руках, с улыбкой
    ryan "Миссис Бакфетт, начнем?"
    ryan "Сначала сделаем кадр, как-будто вы..."
    # Моника перебивает его
    m "Райен..."
    menu:
        "Попросить фотографа не делать откровенных кадров.":
            pass
    ryan "Да, Миссис Бакфетт?"
    m "Я хотела бы попрочить тебя..."
    m "Не брать крупных ракурсов и..."
    # теперь он ее перебивает
    ryan "Миссис Бакфетт, я чувствую, что вы нервничаете."
    ryan "Вы ведете себя скованно и это будет усложнять процесс съемки."
    ryan "Мои снимки шедевральны, Миссис Бакфетт. Это искусство."
    ryan "Вы не найдете в моей работе никакой пошлости, не переживайте."
    m "Ты уверен, Райен?"
    m "Ничего лишнего не будет видно?"
    ryan "Я абсолютно уверен."
    m "..."
    ryan "Приступим?"
    menu:
        "Да.":
            pass
    mt "Черт!"
    m "Да..."

    # 1-й кадр (поза № 1 со ссылки https://www.daz3d.com/z-framed--prop-and-poses-for-genesis-3-and-8-female)
    ryan "Миссис Бакфетт, первый кадр."
    ryan "Присядьте позади рамы, придеживайте ее руками и повернитесь ко мне немного боком."
    m "Райен, я боюсь, что так будет видно мою..."
    ryan "Нет, все в порядке, Миссис Бакфетт."
    ryan "Ничего лишнего в кадре не будет видно."
    # Моника принимает позу, Райен делает кадры
    ryan "Потрясающе!"
    ryan "Я завидую Алексу, что он работает с вами!"
    ryan "Хотел бы я оказаться на его месте..."
    # кадр на зал, где сидит Биф с Кэмпбеллом
    beatrice "Мистер Кэмпбелл, эта модель закрывает своей рукой часть рамы!"
    campbell "Все в порядке, Беатрис."
    campbell "Это всего лишь небольшой фрагмент рамы."
    # кадр на съемочную площадку

    # 2-й кадр (поза № 2)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Встаньте на колени."
    # кадр на зал, где сидит Биф с Кэмпбеллом
    campbell "Мистер Биф, надеюсь, что фотосессия пройдет успешно и..."
    campbell "Мы подберем подходящие кадры для моей рекламной компании."
    biff "Да, Мистер Кэмпбелл, не сомневайтесь."
    biff "Миссис Бакфетт профессионал, она знает, что делать на съемочной площадке."
    # Беатрис недовольно
    beatrice "Главное, чтобы она не повредила раму!"
    campbell "Да, Беатрис, безусловно. Мы доверили Миссис Бакфетт очень ценную вещь."
    # кадр на съемочную площадку
    # Моника встает в нужную позу
    # Райен делает снимки с разных ракурсов
    ryan "Миссис Бакфетт, кадры получаются шикарные!"
    ryan "Расслабтесь немного, я чувствую ваше напряжение."
    mt "Посмотрела бы я на тебя, кретин, если бы тебя голого поставили в эту дурацкую рамку!"

    # 3-й кадр (поза № 3)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Одной рукой придерживайте раму, а второй обопритесь о пол по другую сторону."
    # Моника принимает позу, Райен делает кадры
    ryan "Отлично!"
    m "Райен, не нужно так близко брать..."
    ryan "Я фотограф и я вижу, как будет лучше, Миссис Бакфетт."
    mt "Сволочь!"
    mt "!!!"
    ryan "Еще пара кадров..."
    # кадр на зал, где сидит Биф с Кэмпбеллом
    beatrice "Мистер Кэмпбелл, она бросает тень на раму!"
    beatrice "Из-за этого становися не виден потрясающий рельеф рамы!"
    campbell "Беатрис, не переживай."
    campbell "Мы выберем те кадры, которые лучше всего передадут изяществ рамы."
    beatrice "Хорошо, Мистер Кэмпбелл."
    # кадр на съемочную площадку

    # 4-й кадр (поза № 4)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Теперь вам нужно лечь на бок и взять раму обеими руками."
    # Моника принимает позу, Райен делает кадры
    ryan "Хорошо, Миссис Бакфетт..."
    ryan "Вы просто созданы быть моделью!"
    ryan "Камера любит вас!"
    mt "Я создана быть Большим Боссом и миллионером, придурок!"
    mt "!!!"
    ryan "Еще пара кадров..."
    # кадр на зал, где сидит Биф с Кэмпбеллом
    campbell "Мистер Биф, после того, как мы с Беатрис подберем подходящие нам кадры..."
    campbell "Оставшиеся вы можете использовать для журнала Миссис Бакфетт."
    campbell "Но только после запуска моей рекламной компании, иначе ее эффективность значительно снизиться."
    biff "Мы с удовольствием опубликуем эти кадры, Мистер Кэмпбелл!"
    # Беатрис недовольно смотрит на Монику
    # кадр на съемочную площадку

    # 5-й кадр (поза № 5)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Поставьте ноги по другую сторону и закиньте одну ногу на другую."
    # Моника принимает позу
    m "Но так будет видно всю мою!.."
    ryan "Миссис Бакфетт, все в порядке."
    ryan "Видно только ваши шикарные ноги, ничего более."
    m "Ты уверен, Райен?"
    ryan "Да, Миссис Бакфетт..."
    # Райен фотографирует
    # кадр на зал, где сидит Биф с Кэмпбеллом
    biff "А когда планируется запуск вашей рекламы, Мистер Кэмпбелл?"
    campbell "На днях."
    campbell "Я проведу презентацию этой рамы перед полным залом."
    biff "Здесь? В этом зале?"
    campbell "Да, все верно, в этом зале."
    campbell "Я буду выступать на сцене, а кадры будут транслироваться на экране позади меня."
    beatrice "Да, это будет отличная презентация нашего дизайнерского шедевра."
    campbell "Да, Беатрис. Я не сомневаюсь в успехе нашей рекламной компании."
    # кадр на съемочную площадку

    # 6-й кадр (поза № 8)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Садитесь так, чтобы ноги были по разные стороны рамы."
    # Моника принимает позу, пяткой упирается в раму
    m "Райен, вся моя грудь видна!"
    ryan "Миссис Бакфетт, я сделаю так, что вашу прекрасную грудь не будет видно."
    ryan "Хотя, честно признаться, мне не хотелось бы этого делать..."
    m "Райен!.."
    ryan "Только ради вашей просьбы, Миссис Бакфетт..."
    # кадр на зал, где сидит Биф с Кэмпбеллом
    # Бетрис снова недовольно смотрит на Монику
    beatrice "Эта модель своей ступней опирается на нашу раму!"
    beatrice "Она испортит ее!"
    beatrice "Как можно настолько небрежно обращаться с таким ценным реквизитом?!"
    beatrice "Я подойду и скажу ей, чтоб так не делала, Мистер Кэмпбелл!"
    # Беатрис встает со своего места и идет к Монике
    ryan "Бетрис, что ты?.."
    beatrice "Одну секунду, Райен..."
    # она говорит Монике, наклонившись к ней
    beatrice "Буду признательна, если вы не будете упираться в раму своими ногами!"
    beatrice "Уберите ногу с рамы!"
    beatrice "Вы хоть представляете, сколько она стоит?!"
    beatrice "Вы делаете снимки для рекламы этого шедевра!"
    beatrice "А не для рекламы себя!"
    # Моника в афиге
    m "!!!"
    m "Что?!"
    m "Да ты!..."
    # та недослушав Монику. уже более вежливо обращается к Райену
    beatrice "Можешь работать дальше, Райен."
    beatrice "И, пожалуйста, следи, чтобы эта модель не заляпала раму и не закрывала собой ее."
    ryan "Конечно, Беатрис, без проблем." # улыбается
    # Беатрис уходит к Кэмпбеллу
    mt "Вот сучка!!!"
    mt "Как она, какая-то ничтожная секретарша, смеет так разговаривать со МНОЙ?!"
    mt "!!!"
    ryan "Миссис Бакфетт, уберите, пожалуйста, вашу ногу с рамы."
    ryan "И продолжим."
    mt "!!!"
    # Моника немного сдвигает ногу
    # Райен фотографирует
    ryan "Прекрасные кадры!"
    ryan "Еще один снимок..."


    # 7-й кадр (поза № 10)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Поставьте ноги по другую сторону рамы."
    # кадр на зал, где сидит Биф с Кэмпбеллом
    campbell "Мистер Биф, все хотел поинтересоваться у вас..."
    campbell "Миссис Бакфетт принимает участие в откровенных фотосъемках своего журнала..."
    biff "Да."
    campbell "Ей это действительно нравится?"
    campbell "Или это выгодно ей в финансовом плане, так как значительно возрастают продажи?"
    campbell "Думаю, вы, как ее личный ассистент в курсе этого..."
    biff "Миссис Бакфетт мне говорила, что получает от съемок огромное удовольствие..."
    campbell "Интересно, а согласилась бы Миссис Бакфетт на съемку полностью обнаженной..."
    campbell "Без присутствия на съемочной площадке реквизитов, подобных раме, которая частично прикрывает ее наготу..."
    biff "У вас имеются какие-либо идеи по поводу будущих фотосессий с Миссис Бакфетт?"
    campbell "Да, я тут обдумываю один проект..."
    campbell "Вполне возможно, что я снова обращусь к вам, Мистер Биф, чтобы договориться о фотосессии."
    biff "Всегда рад сотрудничеству с вами, Мистер Кэмпбелл!"
    campbell "Да, я тоже. Как показала практика, это сотрудничество весьма взаимовыгодно..."
    # Беатрис продолжает прожигать Монику взглядом
    beatrice "!!!"
    # кадр на съемочную площадку
    # Райен фотографирует
    ryan "Миссис Бакфетт, кадры будут шедевральными."
    ryan "Вы шикарно смотритесь, Миссис Бакфетт."
    mt "Я всегда великолепна в кадре!"
    mt "!!!"

    # 8-й кадр (поза № 11)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Миссис Бакфетт, теперь вы как-будто выглядываете из рамы."
    # Моника принимает позу
    # кадр на зал, где сидит Биф с Кэмпбеллом
    # Беатрис недовольно ворчит
    beatrice "Да аккуратнее же с реквизитом!"
    beatrice "!!!"
    # кадр на съемочную площадку, Райен фотографирует
    ryan "Восхитительно!"
    ryan "Еще пара кадров..."
    ryan "Прекрасно!"

    # 9-й кадр (поза № 13)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Вы хотите выбраться из рамы..."
    # Моника принимает позу
    m "Райен, мою грудь не будет видно?"
    ryan "Нет-нет, Миссис Бакфетт."
    ryan "Все в порядке."
    # фотографирует
    mt "Сейчас эта жирная корова снова начнет орать, что я закрываю реквизит!"
    mt "Как можно так цепляться из-за какой-то дурацкой рамы!"
    mt "!!!"
    # кадр на злую Беатрис
    beatrice "!!!"
    # и на Бифа, который сидит и косится на ее грудь через Кэмпбелла
    biff "!!!"
    # кадр на съемочную площадку, Райен фотографирует
    ryan "Еще пара кадров..."
    ryan "Отлично!"

    # 10-й кадр (поза № 14)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Сядь красиво за рамой и удерживайте ее руками."
    # Моника принимает позу
    ryan "Хорошо..."
    m "Райен, ты..."
    ryan "Я помню, Миссис Бакфетт. Вашу грудь не будет видно... Почти..."
    mt "Мерзавец!"
    mt "Говорит одно, а делает по-своему!"
    mt "Такой же обманщик, как Алекс!"
    mt "Все эти фотографы такие извращенцы?!"
    mt "?!"
    ryan "Прекрасно!"

    # 11-й кадр (поза № 18)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Вы почти полностью выбираетесь из рамы."
    # Моника принимает позу
    ryan "Ноги немного шире, Миссис Бакфетт."
    m "Но..."
    ryan "Никаких пошлых кадров. Помню-помню..."
    m "!!!"
    # Моника раздвигает ноги пошире
    # кадр на зал, где сидит Биф с Кэмпбеллом
    beatrice "Мистер Кэмпбелл, эта модель закрыла собой почти половину рамы!"
    beatrice "Она что, совсем не понимает, что делает?"
    beatrice "Как можно показывать такой непрофессионализм?!"
    beatrice "Над этим потрясающим рельефом работали лучшие ваши дизайнеры, а она что делает?!"
    campbell "Беатрис, все хорошо."
    campbell "Мы возьмем не все кадры, а только те, на которых отчетливо видна наша рама."
    beatrice "..."
    # кадр на съемочную площадку
    # Райен фотографирует
    m "Райен, если я увижу на снимках, что ты меня обманываешь..."
    m "Когда говоришь, что ничего пошлого не будет на них..."
    m "Я с тобой больше никогда не соглашусь работать!"
    m "И всем буду говорить, что ты отвратительный фотограф!"
    ryan "Уверен, вам понравится моя работа!"
    ryan "Вы захотите со мной работать снова. Я в этом не сомневаюсь!"
    mt "Какая самоуверенность!!!"
    mt "!!!"

    # 12-й кадр (поза № 25)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Вам нужно встать в полный рост..."
    m "Нет, Райен!"
    m "Вообще-то, я обнажена!"
    m "Как ты себе это представляешь?!"
    m "Я не буду делать этого!"
    ryan "Но, Миссис Бакфетт, это будут последние кадры..."
    ryan "Я возьму такие ракурсы, что..."
    m "Я сказала НЕТ!"
    m "!!!"
    # Райен растерянно оглядывается на Бифа
    # тот вскакивает со своего места и идет к Монике, шепчет ей зло, наклонившись
    biff "Слышишь ты, кукла безмозглая!"
    biff "Что еще за капризы ты тут показываешь?!"
    biff "Быстро встала и сделала так, как тебе говорит Райен!"
    biff "Не заставляй меня нервничать!"
    biff "Не хочешь в полный рост - не оплачу эту съемку и выгоню с моего офиса на улицу!"
    biff "Будешь снова сосать члены прохожим за 20 баксов, шлюха, как ты это привыкла делать!"
    mt "Черт!!!"
    mt "Я что, терпела всю эту кошмарную фотосессию..."
    mt "Чтобы из-за одного кадра лишиться денег за нее?!"
    mt "Моника, это будет неумный поступок с твоей стороны!"
    mt "..."
    mt "А с мерзавцем Бифом ты разберешься! Ты заставишь его отвечать за все эти унижения!"
    mt "Только нужно набраться терпения и делать вид, что слушаешься его!"
    mt "!!!"
    menu:
        "Принять позу, которую просит фотограф.":
            pass
    # Моника принимает нужную позу, Биф отходит в сторону
    # Райен делает снимки
    ryan "О, Миссис Бакфетт, вы великолепны!"
    ryan "Теперь с этого ракурса..."
    ryan "Шикарный кадр!"
    ryan "Да, отлично!"

    # после последнего отснятого кадра
    ryan "Съемка окончена!"
    # Моника прикрывается руками
    ryan "Миссис Бакфетт, приятно было с вами поработать..."
    ryan "Надеюсь, что это не последняя наша совместная фотосессия."
    # Моника недовольно молчит
    m "..."
    # затемнение
    # звук одежды, шаги
    # смена кадра
    # на сцене стоят одетая Моника, фотограф, Кэмпбелл, Беатрис и Биф
    campbell "Миссис Бакфетт, благодарю вас за сегодняшнюю фотосессию."
    ryan "Это была одна из лучших моих фотосессий, Миссис Бакфетт!"
    mt "Ужасная фотосессия в какой-то дурацкой рамке!"
    mt "Носятся с ней, как с какой-то ценностью..."
    mt "Кому эта рамка вообще нужна?! Хлам!"
    mt "Идиоты!"
    mt "!!!"
    campbell "Вы прекрасно справились с работой."
    campbell "Уверен, что это будут отличные кадры."
    beatrice "Далеко не все..." # Беатрис с ухмылкой
    campbell "Мы с Беатрис отберем наиболее подходящие для нашей рекламной компании снимки..."
    campbell "Остальные Райен пришлет вам для публикации в вашем журнале, Миссис Бакфетт."
    m "Я..."
    # Биф перебивает
    biff "Спасибо вам больше, Мистер Кэмпбелл. Будем ждать с нетерпением!"
    biff "Надеюсь ваша рекламная компания пройдет успешно!"
    campbell "Я думаю, что успех гарантирован..."
    campbell "Вы только посмотрите на этот восхитительный дизайн!"
    # он и Беатрис с восхищением смотрят на рамку, Биф с Млникой с недоумением
    campbell "Только человек, не обладающий вкусом и не разбирающийся в искусстве..."
    campbell "Не увидит в этой прекрасной дизайнерской раме ничего необычного."
    campbell "Вы согласны со мной, Миссис Бакфетт?"
    campbell "Вы, как творческий человек, должны были оценить эту вещь по достоинству."
    m "Мммм..."
    m "Да..."
    m "Уверена, что любой коллекционер изящных дизайнерских предметов..."
    m "Мечтал бы заполучить ее, Мистер Кэмпбелл."
    campbell "Я знал, что вам понравится, Миссис Бакфетт."
    campbell "А сейчас я вынужден вас покинуть, к сожалению."
    campbell "Я уже опаздываю на важную встречу."
    campbell "Надеюсь, до скорой встречи."
    biff "До свидания, Мистер Кэмпбелл."
    biff "Мисс Беатрис..." # целует ей руку и жадно ее рассматривает
    # они уходят
    return


# мысли Моники, когда вышла из офиса после проведения фотосессии
label ep219_dialogues2_office_4:
    # не рендерить!
    mt "Моника, я не могу поверить, что ты сделала ЭТО!!!"
    mt "Ты согласилась на фотосессию в обнаженном виде!!!"
    mt "Еще и перед этим никчменым самодовольным индюком Райеном!"
    mt "И перед инвестором с его мерзкой помощницей!"
    mt "Кошмар! Я надеюсь, что рекламная компания Кэмпбелла пройдет в узком кругу людей и не предастся широкой огласке!"
    mt "!!!"
    mt "Мне нужно придумать, как прекратить это издевательство Бифа!"
    mt "Это не может продолжаться бесконечно!"
    mt "Я должна отомстить ему!"
    mt "И забрать обратно МОЙ журнал!!!"
    mt "!!!"
    return


# при условии, что у Моники была фотосессия в раме
# через неделю Моника приходит на работу в отдел отчетов
# кадр на сотрудников отдела отчетов
label ep219_dialogues2_office_5:
    # близняшки и Лин, наклонившись друг к другу, шепчутся, сплетничают
    w7 "Девочки, помните, мы с вами удивлялись..." # Лин
    w7 "Что наша начальница фотографировалась для нашего журнала с голой грудью?"
    w3 "Да, не просто с голой грудью, а еще и перед какими-то мужчинами!"  # одна близняшка
    w4 "Перед толпой мужчин! И почти голая! Кошмар!"  # вторая близняшка
    w7 "Я сегодня увидела новый выпуск журнала..."
    w7 "А там!.." # делает фейспалм или закатывает глаза
    w4 "Что? Ну говори скорее, Лин!"
    w7 "Ой, девочки, вы сейчас будете в шоке!"
    w7 "Хи-хи-хи!"
    w3 "Ну, Лин!!!"
    w7 "Наша Миссис Бакфетт снялась для рекламы Кэмпбелла!"
    w7 "Об этом пишут во всех изданиях! И обсуждают все!"
    w4 "Что за реклама?"
    w7 "Какая-то дизайнерская рама для картины. Ничего интересного..."
    w7 "Интересен другой факт!"
    # близняшки смотрят на нее, сгорая от любопытства
    w3 "ЛИН!!!"
    w7 "Миссис Бакфетт на снимках голая! Абсолютно! В полный рост!"
    w4 "Совсем голая?!"
    w7 "Да!"
    w3 "Да ладно?!"
    w4 "Не может быть!"
    w7 "Да, девочки!"
    w7 "Я сама не поверила бы, если не увидела бы своими глазами!"
    w4 "Как вы думаете, может она и правда получает от этого удовольствие?"
    w4 "Как там таких извращенцев называют? Экбиги... Черт, не могу запомнить это слово..."
    w3 "Эксгибиционистка!"
    w4 "Да, точно!"
    w7 "Миллионерша-извращенка! Хи-хи-хи!"
    w3 "Хи-хи-хи!"
    # подкрадывается серая мышка в очках
    w1 "Вы о ком?"
    w3 "О нашей начальнице!"
    w1 "Миссис Бакфетт? А что случилось?"
    w4 "Она по ходу совсем с катушек съехала!"
    w4 "Фотографируется уже не просто полуобнаженная, а голая! Представляешь?!"
    w1 "Серьезно?!"
    # Лин резко
    w7 "Девочки! Бакфетт идет!"
    w1 "ОЙ!!!" # убегает
    w3 "Черт!"
    w4 "По местам!!!"
    # все разбегаются по местам и в этот момент заходит злая Моника
    # как обычно, с ней все здороваются, а она зло всех игнорит
    w1 "Добрый день, Миссис Бакфетт!"
    w3 "Здравствуйте!"
    w6 "Миссис Бакфетт, здравствуйте!"
    # Моника, не глядя ни на кого недовольно шагает в свой кабинет
    mt "Бесполезные муравьишки!"
    mt "Сидят занимаются своими мелкими заботами!"
    mt "Никому не нужными!"
    mt "Никчемные!"
    mt "!!!"
    return
