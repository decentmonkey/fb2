define neighbor2 = Character(_("Сосед Эбби"), who_color=c_red)  # сосед Эбби
define brian = Character(_("Брайан"), who_color=c_orange)  # клиент Эбби вне эскорта

default monicaAbbyNoEscortClient1 = 0 # Моника согласилась поехать домой к Эбби и встретиться с ее клиентом вне эскорта
default monicaAbbyNoEscortClient2 = 0 # Моника изменила свое решение и согласилась работать с клиентами Эбби
default monicaAbbyNoEscortClient3 = 0 # Моника согласилась на секс с клиентом Эбби, не стала выгонять его
default monicaAbbyNoEscortClient4 = 0 # Моника не оставила Эбби процент, забрала все деньги
default monicaAbbyNoEscortClient5 = 0 # Моника оставила Эбби процент

define v_Monica_AbbyCustomer_Blowjob1_1_15_sound_name = "v_MonicaHome_Jack_Blowjob1_1"
define v_Monica_AbbyCustomer_Blowjob1_1_25_sound_name = "v_MonicaHome_Jack_Blowjob1_1"
define v_Monica_AbbyCustomer_Sex1_1_25_sound_name = "v_Citizen15_ShopVisitor7_Sex2_1"
define v_Monica_AbbyCustomer_Sex1_1_sound_name = "v_Citizen15_ShopVisitor7_Sex2_1"
define v_Monica_AbbyCustomer_Sex2_1_25_sound_name = "v_Citizen15_ShopVisitor7_Sex2_1"
define v_Monica_AbbyCustomer_Sex2_1_sound_name = "v_Citizen15_ShopVisitor7_Sex2_1"

# при условии, если Моника была в гостях у Эбби
# ресторан отеля Ле Гранд
label ep22_4_dialogues5_escort_1:
    # у входа в ресторан, перед столиками Моника видит Эбби
    img 30003
    w
    img 30005
    abby "[monica_hotel_name], привет."
    abby "Как у тебя дела?"
    mt "Какая ей разница, как у меня дела?!"
    mt "!!!"
    img 35044
    mt "Так, Моника, нужно быть более осторожной с этой Эбби."
    mt "Во-первых, она знает, кто главный в ВИП-эскорте."
    mt "Если я сделаю так, что она начнет мне доверять..."
    mt "То она поделится со мной этой информацией."
    # если была в гостях у Линды
    img 17527
    mt "Надеюсь, что она не знает о моей 'дружбе' с лицемерками Линдой и Мирандой."
    mt "Если она что-то заподозрит, то ни о каком доверии и речи быть не может."
    # если Моника сука
    img 30015
    mt "Я сделаю все, чтобы обыграть этих проституток-эскортниц!"
    mt "Я здесь самая умная и только я достойна занять место администраторши!"
    # если бичность низкая
    img 30015
    mt "Не известно, насколько верно я поступаю, обманывая этих проституток..."
    mt "Но пока у меня нет иного выхода..."
    mt "Я вынуждена притворяться их подругой."
    #
    # Моника притворно
    img 30004
    m "Привет, Эбби."
    m "Все нормально. Как у тебя дела?"
    abby "У меня всегда все окей."
    abby "Я хотела спросить тебя..."
    # если Моника согласилась работать с клиентами Эбби
    # if monicaAbbyRentHelp7 > 0:
    img 41422
    abby "Как у тебя с доходами от работы в эскорте?"
    m "Могло быть и лучше..."
    abby "Отлично. Значит, ты будешь заинтересована в подработке..."
    label ep22_4_dialogues5_escort_1a:
    img 30006
    abby "Мне сегодня позвонил один из моих клиентов вне ВИП-эскорта."
    abby "Хочет встретиться, а у меня на него нет времени."
    abby "Да и желания особого нет с ним встречаться..."
    img 41424
    m "Что за клиент?"
    abby "Да он нормальный чувак. Жадный немного, но в целом пойдет... Если совсем нет денег."
    abby "Короче, я сейчас ему позвоню и скажу, что его обслужит моя напарница, то есть ты."
    img 35045
    m "Подожди-подожди! Что, прямо сегодня?!"
    abby "Ага."
    m "А где?"
    abby "У меня дома. Я встречаюсь с этими клиентами только там."
    abby "В ВИП-эскорте никто об этом не должен узнать."
    img 35046
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
            img 35047
            mt "Я не собираюсь возиться с этими извращенцами!"
            mt "Еще и дома у этой проститутки-эскортницы!"
            mt "Не смотря на то, что мне нужны деньги, я не хочу идти на это!"
            mt "По крайней мере, не сегодня!"
            img 41426
            m "Нет, Эбби! На сегодня у меня другие планы!"
            m "Возможно, в следующий раз..."
            img 41425
            abby "Окей. Как знаешь."
            abby "Если что - обращайся."
            # Эбби отходит от Моники
            return
    # если Моника в первый раз отказалась работать с клиенами Эбби
    # else:
    img 41422
    abby "Ты не передумала насчет моего предложения?"
    m "Какого предложения?"
    abby "Хорош тупить, [monica_hotel_name]!"
    m "!!!"
    img 30006
    abby "Я про своих клиентов вне ВИП-эскорта..."
    abby "Может, ты передумала и хочешь, чтобы я поделилась с тобой ими?"
    m "..."
    menu:
        "Отказаться!":
            # Моника задумчиво
            img 35047
            mt "Она предлагает мне обслуживать каких-то нищебродов за гроши?!"
            mt "А сама хочет занять место на ресепшене?!"
            mt "Хитрая дешевая подстилка!"
            mt "!!!"
            mt "Это Я стану главной и буду решать, когда и под кого ты будешь ложиться!"
            mt "Сучка!!!"
            # Моника притворно улыбается
            img 41426
            m "Мне хватает того, что я зарабатываю в отеле..."
            m "А когда ты станешь... Кхм... Главной..."
            m "Я буду зарабатывать еще лучше."
            m "Спасибо, что предложила."
            img 41425
            m "Если я по какой-то причине изменю свое решение, я дам тебе знать."
            abby "Окей. Как знаешь."
            abby "Если что - обращайся."
            # Эбби отходит от Моники
            img 30007
            mt "Не хватало мне еще возиться с каким-то жалким отребьем!"
            mt "Я найду способ заработать деньги без этой гадости!"
            mt "!!!"
            return
        "Согласиться.":
            $ monicaAbbyNoEscortClient2 = day # Моника изменила свое решение и согласилась работать с клиентами Эбби
            img 35047
            mt "Черт!"
            mt "Я должна каждую неделю отдавать этой мерзкой сикалявке Виктории $ 5 000!"
            # если должна Перри
            mt "И еще выплачивать долг мерзкой Перри!"
            # если арендует апартаменты у Джека
            mt "И платить за грязную дыру, которую мне сдает Джек!"
            #
            img 41429
            mt "Мне нужны эти деньги!"
            mt "Но, Моника, неужели ты ради денег..."
            mt "Будешь обслуживать каких-то жалких, никчемных отбросов от Эбби?!"
            mt "Ты готова пойти на это?!"
            mt "?!?!?!"
            mt "Черт!!!"
            img 41426
            m "Я... Я думаю, что..."
            m "Что я попробую..."
            img 41425
            abby "Окей!"
            abby "Ты приняла верное решение, [monica_hotel_name]."
            jump ep22_4_dialogues5_escort_1a
    label ep22_4_dialogues5_escort_1b:
    # Моника задумчиво
    img 35048
    mt "Если я сейчас откажусь от встречи с ее гребаным клиентом..."
    mt "То рискую вообще ничего не заработать сегодня."
    mt "А мне нужны деньги."
    mt "Но это так отвратительно!"
    mt "!!!"
    img 35049
    mt "С другой стороны, возможно, мне стоит попробовать?"
    mt "Всего один раз..."
    mt "Зато я смогу заработать."
    mt "А если мне что-то не понравится..."
    mt "То я просто пошлю эту Эбби с ее дурацкими клиентами ко всем чертям!"
    mt "Да, я думаю, что это самое верное решение!"
    # Моника, притворно улыбаясь
    img 35050
    m "Да, Эбби. Я поеду."
    abby "Окей. Я тогда сейчас позвоню клиенту."
    abby "Короче, слушай..."
    abby "Сейчас поедешь ко мне домой."
    img 35051
    abby "Первое правило - ты должна принять душ до работы с клиентом."
    m "Не логичнее это сделать после?"
    abby "Нет! Вообще-то, ты будешь обслуживать его на моей постели!"
    abby "Так что, сначала в душ, а потом - трах с ним."
    img 35052
    mt "Фу, как грубо!"
    mt "!!!"
    img 35053
    abby "И клиента, кстати, тоже отправь в душ! Это обязательно!"
    abby "Полотенце для душа можешь взять мое. Я его, по-моему, на кровати оставила."
    img 35052
    mt "Надеюсь, оно чистое!"
    mt "!!!"
    abby "К клиенту обращайся по имени. Его зовут Брайан."
    # Моника язвительно
    img 35054
    m "Постараюсь не перепутать и не назвать его другим именем."
    m "Какие-то еще инструкции будут?"
    abby "Да. У меня через стену живет один придурок."
    abby "Везде сует свой нос. Любитель поскандалить и поворчать."
    abby "На него внимания не обращай."
    img 35055
    abby "Если он будет надоедать, скажи ему 'пошел на хрен отсюда, трахаюсь с кем хочу' и он отстанет."
    m "Что, так и сказать?!"
    m "Это же не прилично!"
    abby "Клиентов домой водить тоже неприлично."
    img 35056
    abby "Я снимаю всего-лишь одну комнату в общей квартире."
    abby "И ты, между прочим, не высокосветская леди, так что можно обойтись без реверансов."
    m "!!!" # зло
    # Эбби сосредоточенно
    abby "Так, вроде бы я все тебе сказала."
    img 35057
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
    img 35058
    w
    img 35059
    m "Привет, Эбби."
    abby "[monica_hotel_name], привет."
    abby "Что насчет подработки?"
    abby "Я с тем клиентом так и не встретилась."
    img 35048
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
            img 35047
            mt "Я не собираюсь возиться с этими извращенцами!"
            mt "Еще и дома у этой проститутки-эскортницы!"
            mt "Не смотря на то, что мне нужны деньги, я не хочу идти на это!"
            mt "По крайней мере, не сегодня!"
            img 35046
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
    img 35063
    w
    img 35064
    mt "Детская комната!.."
    mt "В которой гребаная Эбби обслуживает своих гребаных клиентов!"
    mt "И теперь ты, Моника, будешь делать то же самое! Кошмар!"
    mt "Зачем я только согласилась на это безумие?!"
    mt "!!!"
    img 35065
    mt "Так, что мне нужно сделать сначала?"
    mt "Что там говорила эта проститутка Эбби?"
    mt "Принять самой душ, потом отправить туда клиента..."
    mt "Называть клиента только по имени."
    img 35066
    mt "Хмм... По-моему, я забыла его имя..."
    mt "Неважно! Обойдется!"
    mt "Еще я не обращалась по имени ко всяким ничтожествам!"
    mt "!!!"
    menu:
        "Принять душ.":
            pass
    # Моника подходит к кровати и смотрит на полотенце
    img 35067
    mt "Это же то полотенце, в котором проститутка Эбби брила свою... В общем, брилась."
    mt "Я к этому полотенцу даже прикасаться не хочу!.."
    mt "А мне придется воспользоваться им после душа! Фи!"
    # Моника тянет руку к полотенцу
    # затемение, шуршание одежы, шаги босиком
    # смена кадра
    # душ, Моника заходит и брезгливо оглядывается
    img 35068
    w
    img 35069
    w
    img 35070
    w
    img 35071
    mt "Фууу!!!"
    mt "Это что, общий душ?!"
    mt "Здесь такое все!.. Грязное!"
    img 35072
    mt "Моника, постарайся ни к чему не прикасаться!"
    mt "Ты сейчас быстро примешь душ и пойдешь в комнату..."
    # затемнение, кран, шум воды
    # Моника стоит в душе
    img 35073
    w
    img 35074
    mt "Как же все-таки приятно..."
    img 35075
    mt "Мне вода всегда помогала успокоиться..."
    img 35076
    mt "Очистить голову от лишних мыслей..."
    img 35077
    mt "Расслабиться..."
    img 35078
    mt "Мммм..."
    # хлопает дверь
    # Моника испуганно открывает глаза
    img 35079
    mt "Это еще что такое?!"
    mt "Я что, не закрыла дверь?!"
    img 35080
    m "Кто там?!"
    m "Вообще-то, здесь занято!"
    # к душевой кабинете подходит сосед Эбби
    img 35081
    neighbor2 "А ты кто такая?"
    neighbor2 "Что ты здесь делаешь?!"
    # Моника прикрывается руками или хватает полотенце и прикрывается им
    img 35082
    m "Отвернулся быстро!"
    m "Ты что, не видишь, что перед тобой дама?!"
    neighbor2 "Тоже мне дама нашлась!"
    neighbor2 "Чего я там не видел?!"
    m "Отвернись!!!"
    img 35083
    neighbor2 "Еще чего!!!"
    neighbor2 "Это не твой душ! Ты чего сюда приперлась?!"
    m "Я!.. Мне!.."
    m "Мне Эбби разрешила!"
    neighbor2 "Эбби?! Шлюшка из соседней комнаты?!"
    img 35084
    neighbor2 "Так значит, ты ее подружка будешь?!"
    neighbor2 "Или коллега?!"
    m "Не твое дело!"
    neighbor2 "Вот именно, что МОЕ дело!"
    img 35085
    neighbor2 "Устроили тут проститутошную, а я должен все это терперть?!"
    neighbor2 "Я буду жаловаться хозяину апартаментов!"
    neighbor2 "Какие-то дешевые шлюхи таскают сюда своих клиентов!"
    img 35086
    neighbor2 "Идите на улице работать, проститутки!"
    neighbor2 "Я у себя же дома отлить не могу спокойно сходить из-за вас!"
    # Монику бомбит
    img 35087
    m "Ты где здесь проститутку увидел, придурок?!"
    m "Пошел вон отсюда, пока я полицию не вызвала!!!"
    img 35085
    neighbor2 "Вызывай! Полиция мне поверит, а не какой-то шлюхе!"
    img 35088
    m "Я не шлюха!!!"
    m "Я скажу, что ты меня домогался и тебя посадят за решетку!"
    img 35089
    neighbor2 "Я?! Что я домогался тебя?!"
    neighbor2 "Нужна ты мне больно, грязная шлюшка."
    m "Кретин!!!"
    # сосед осматривает Монику с головы до ног
    img 35090
    w
    img 35091
    w
    img 35092
    neighbor2 "Если хочешь, чтоб я ушел, покажи мне свои сиськи."
    img 35093
    m "ЧТООО?!"
    m "Совсем охренел, старый извращенец?!"
    m "А ну-ка пошел вон отсюда!"
    neighbor2 "Покажешь сиськи - не буду жаловаться хозяину апартаментов."
    # Моника зло его выталкивает из ванной комнаты
    img 35094
    w
    img 35095
    m "ВООООН!"
    img 35096
    m "!!!"
    # остается одна
    img 35097
    mt "Какое-то безумие!!!"
    mt "Грязные отбросы общества позволяют себя так вести с тобой, Моника!"
    mt "Как он мог?!"
    mt "Мерзкий, противный старикашка!!!"
    mt "!!!"
    img 35098
    w
    img 35099
    mt "Нужно быстрее уходить отсюда!"
    mt "Вдруг он вернется! Не хочу видеть его..."
    # Моника прерывается на полуслове, т.к. в ванную комнату заходит клиент Эбби, Брайан
    img 35100
    w
    img 35101
    mt "!!!"
    mt "!!!!"
    brian "Ох ни хрена себе, какая у меня сегодня девка!"
    img 35102
    brian "Крошка Эбби не обманула, сказав, что мне понравится!"
    mt "О, нет! Это и есть клиент Эбби?!"
    brian "Познакомимся или сразу возьмешься за работу, а? Хе-хе!"
    # Моника растерянно
    img 35104
    m "Я..."
    m "Я [monica_hotel_name]..."
    brian "Зови меня Брайан."
    brian "Покажешь, что ты там прячешь под своим полотенцем?"
    img 35103
    m "Н-нет!"
    m "Сначала душ!"
    brian "Какая стеснительная малышка. Хе-хе-хе!"
    brian "Сегодня у Брайана будет отличный секс с новой телкой!"
    img 35105
    m "!!!"
    img 35106
    m "Я подожду тебя в коридоре!"
    img 35107
    # Моника выбегает
    # затемнение, коридор возле душа
    # Моника стоит у стены, придерживая полотенце
    img 35108
    w
    img 35109
    mt "Что-то я все меньше уверена в своей адекватности..."
    mt "В тот момент, когда приняла предложение гребанной Эбби..."
    mt "Зачем я согласилась на это?!"
    mt "Что мне сейчас..."
    img 35110
    neighbor2 "Ага!"
    img 35111
    neighbor2 "Попалась, проститутка!"
    # сосед появляется неожиданно, Моника пугается
    m "!!!"
    m "!!!!"
    m "!!!!!"
    img 35112
    m "Напугал меня!"
    m "Идиот!"
    neighbor2 "Думала, так легко от меня избавишься?!"
    m "Чего тебе нужно от меня?!"
    img 35113
    neighbor2 "Покажешь?"
    m "Что тебе показать?"
    neighbor2 "Свои сиськи."
    m "НЕТ!"
    # он зло на нее смотрит
    img 35114
    neighbor2 "Какая-то проститутка строит из себя леди!"
    img 35115
    mt "Я и есть Леди!"
    mt "Знал бы этот недоумок, кто перед ним стоит!"
    mt "!!!"
    img 35116
    neighbor2 "Только поглядите на нее!"
    neighbor2 "Кто там в душе сейчас? А?"
    neighbor2 "Очередной твой хмырь?"
    m "Сам ты хмырь!"
    neighbor2 "Собралась трахаться с ним?"
    img 35117
    m "Тебя это не касается! Иди, куда шел!"
    neighbor2 "Невозможно больше жить в таких условиях!"
    neighbor2 "Устроили бордель!"
    neighbor2 "Спят с незнакомыми мужиками за деньги!"
    mt "Все! Он меня достал!"
    img 35118
    m "Ты!"
    m "Импотент гребаный!"
    m "Тащи свою задницу подальше отсюда!"
    m "Пока я сама не нажаловалась на тебя хозяину апартаментов Гарри!"
    img 35119
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
    img 35120
    neighbor2 "Не надо ничего говорить Гарри."
    neighbor2 "Я пойду... У меня еще столько дел, а ты меня отвлекаешь своими пустыми разговорами..."
    # уходит и про себя ворчит, не смотря на Монику
    img 35121
    neighbor2 "Какая-то проститутка знает Гарри..."
    neighbor2 "Гарри хороший парень и не водится с такими, как она..."
    neighbor2 "С Гарри она дружит..."
    neighbor2 "Так я и поверил!.."
    img 35122
    mt "Какой же этот сосед отвратительный тип!"
    mt "ААААА!!!"
    mt "Ненавижу!!!"
    mt "!!!"
    # из ванной комнаты выходит клиент
    img 35123
    brian "Малышка! Я готов!"
    img 35124
    m "Наконец-то!"
    brian "Тебе так не терпится? Хе-хе!"
    brian "Пошли скорее!" # хлопает Монику по попе
    img 35125
    w
    img 35126
    m "!!!"
    # затемнение
    # смена кадра, комната Эбби
    # заходит Моника, следом клиент
    # он тянет ее за руку к себе
    img 35127
    w
    img 35128
    w
    img 35129
    w
    img 35130
    brian "Иди сюда, малышка!"
    # начинает лапать за попу, грудь
    img 35131
    w
    img 35132
    w
    img 35133
    w
    img 35134
    brian "Сейчас я с тобой буду делать все, что захочу!"
    img 35135
    brian "Какая ты сексуальная! Мммм!"
    # лезет рукой под полотенце на попе
    img 35136
    w
    img 35137
    brian "Такая аппетитная! Идем скорее на кровать!"
    img 35138
    mt "Боже, как все это мерзко и грязно!"
    mt "Я вижу его впервые в своей жизни и даже не запомнила его имени!"
    mt "А он меня уже всю облапал своими ручищами!"
    mt "Грязный никчемный людишка!"
    mt "!!!"
    # коррапшн
    menu:
        "Терпеть клиента Эбби.":
            pass
        "Выгнать его!":
            img 35139
            mt "Я, Моника Бакфетт!"
            mt "Леди из высшего общества и владелица многомиллионного бизнеса!"
            mt "Я мечта любого мужчины этого города и даже страны!"
            mt "И я не позволю какому-то грязному отребью прикасаться ко мне!"
            # Моника его отталкивает
            img 35140
            m "Хватит!"
            img 35141
            m "Убери свои руки!"
            img 35142
            brian "Эй, малышка! Ты чего?!"
            m "Ничего! Я не буду работать!"
            img 35143
            brian "В смысле?! Ты прикалываешься?!"
            img 35144
            m "Уходи!"
            brian "Но как же?.. Ведь Эбби..."
            img 35145
            m "Мне наплевать, что тебе пообещала Эбби!"
            m "Я не буду работать!"
            m "Пошел вон отсюда!!!"
            img 35146
            brian "Дура!"
            return
    # клиент продолжает лапать Монику и ведет ее к кровати
    img 35147
    w
    img 35148
    mt "Мне нужно успокоиться!"
    mt "Глубокий вдох - выдох..."
    img 35149
    mt "Скоро, совсем скоро, этот кошмарный сон закончится!"
    mt "Если я все сделаю правильно, то совсем скоро Я буду зарабатывать деньги на том..."
    img 35150
    mt "Что эти проститутки будут обслуживать разных козлов!"
    mt "И буду штрафовать их! Всех! Особенно, Эбби!"
    mt "!!!"
    # он валит ее на кровать и срывает полотенце
    img 35151
    brian "Ну что, малышка! С чего начнем, а?"
    # Моника молча зло на него смотрит
    img 35152
    m "!!!"
    brian "Скажи мне для начала, как ты хочешь мой член!"
    # Моника продолжает зло молчать
    img 35153
    mt "Ни за что!"
    mt "Озабоченное грязное животное!"
    mt "!!!"
    img 35154
    brian "Говори! Я хочу услышать это!"
    brian "Хочешь его? Посмотри!"
    # достает свой стояк
    img 35155
    brian "Смотри, какой он огромный!"
    img 35156
    brian "Тебе ведь не терпится ощутить его внутри, да?"
    # Моника зло на него смотрит
    img 35157
    mt "Никто и никогда не слышал от Моники Бакфетт эти слова!"
    mt "И не услышит!!!"
    mt "!!!"
    img 35158
    brian "Вижу по глазам, что не терпится! Хе-хе!"
    brian "Все девки, как только видят его, готовы сразу раздвинуть ноги!"
    brian "И ты тоже хочешь!"
    img 35159
    mt "Фу! Нет!"
    mt "Мразь!"
    img 35160
    brian "Сейчас я удовлетворю тебя, малышка!"
    brian "Я буду трахать тебя, как никто и никогда, да!"
    brian "Раком!"
    img 35161
    m "Что?!"
    brian "Повернулась ко мне задом и встала раком! Быстро!"
    mt "!!!"
    # коррапшн
    menu:
        "Сделать, как говорит клиент.":
            $ monicaAbbyNoEscortClient3 = day # Моника согласилась на секс с клиентом Эбби, не стала выгонять его
            pass
        "Выгнать его!":
            img 35162
            mt "Я, Моника Бакфетт!"
            mt "Леди из высшего общества и владелица многомиллионного бизнеса!"
            mt "Я мечта люього мужчины этого города и даже страны!"
            img 35163
            mt "И я не позволю какому-то грязному отребью прикасаться ко мне!"
            # Моника его отталкивает
            img 35164
            m "Хватит!"
            img 35165
            m "Убери свои руки!"
            brian "Эй, малышка! Ты чего?!"
            m "Ничего! Я не буду работать!"
            img 35166
            brian "В смысле?! Ты прикалываешься?!"
            m "Уходи!"
            img 35167
            brian "Но как же?.. Ведь Эбби..."
            m "Мне наплевать, что тебе пообещала Эбби!"
            img 35168
            m "Я не буду работать!"
            m "Пошел вон отсюда!!!"
            img 35169
            brian "Дура!"
            return
    # Моника недовольно
    img 35162
    mt "Грубый, неотесанный мужлан!"
    mt "Теперь я понимаю, почему гребаная Эбби не хочет с ним сама работать!"
    mt "Подсунула мне этого идиота! Сучка Эбби!"
    mt "!!!"
    img 35163
    mt "Так, Моника, если уж ты решилась на это..."
    mt "То нужно быть сильной и довести это дело до конца!"
    mt "Думай о том, что скоро все это закончится..."
    mt "А в твоем кармане станет больше денег!"
    # Моника встает в коленно-локтевую, лицо злое
    img 35170
    w
    img 35171
    w
    img 35158
    brian "О, дааа! Какая послушгая малышка!"
    # он лапает ее попу
    img 35172
    brian "Какая у тебя бархатная кожа... Мммм..."
    img 35173
    brian "Как ты обалденно пахнешь..."
    img 35172
    w
    img 35173
    w
    img 35174
    brian "Кайфовая шлюшка от Эбби! Хе-хе!"
    brian "Как там тебя зовут? Напомни, я забыл."
    mt "Ты не достоин произносить мое имя, никчемный неудачник!"
    mt "Даже дышать на меня не достоин, тварь!"
    img 35175
    brian "Имя!"
    brian "Иначе буду называть грязной шлюшкой или сучкой!"
    # шлепает ее по попе
    img 35176
    w
    img 35177
    w
    img 35178
    m "Ай! [monica_hotel_name]!"
    brian "Другое дело!"
    brian "Кайфовая шлюшка [monica_hotel_name]..."
    brian "Сейчас я войду в тебя своим огромным членом!"
    # пристраивает член к киске Моники
    img 35179
    w
    img 35181
    brian "Ты жаждешь почувствовать его?"
    brian "Да, ты мечтаешь о нем!"
    # входит в нее
    img 35179
    w
    img 35180
    brian "Дааа!"
    img 35182
    w
    img 35183
    w

    # video
    #1 -25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_AbbyCustomer_Sex1_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_1_25= Movie(play="video/v_Monica_AbbyCustomer_Sex1_1_25.mkv")
    show videov_Monica_AbbyCustomer_Sex1_1_25
    with fade
    brian "О, какая бархатная киска у шлюшки [monica_hotel_name]!"
    wclean
    brian "Еееее!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # начинает пялить ее, жестко
    img 35184
    w

    #2 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_2_25= Movie(play="video/v_Monica_AbbyCustomer_Sex1_2_25.mkv")
    show videov_Monica_AbbyCustomer_Sex1_2_25
    with fade
    brian "Не будь ты шлюшкой, я всегда бы тебя трахал!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35185
    brian "Дааа!"
    img 35186
    w

    #3 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_3_25= Movie(play="video/v_Monica_AbbyCustomer_Sex1_3_25.mkv")
    show videov_Monica_AbbyCustomer_Sex1_3_25
    with fade
    brian "Теперь я твой постоянный клиент!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35187
    w

    # video
    #4
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_AbbyCustomer_Sex1_1_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_4= Movie(play="video/v_Monica_AbbyCustomer_Sex1_4.mkv")
    show videov_Monica_AbbyCustomer_Sex1_4
    with fade
    brian "Буду покупать тебя и трахать!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35188
    w

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_5= Movie(play="video/v_Monica_AbbyCustomer_Sex1_5.mkv")
    show videov_Monica_AbbyCustomer_Sex1_5
    with fade
    brian "Трахать-трахать!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex1_6= Movie(play="video/v_Monica_AbbyCustomer_Sex1_6.mkv")
    show videov_Monica_AbbyCustomer_Sex1_6
    with fade
    brian "Аааа!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # хватает ее за волосы на затылке (как у товарища ICSTOR'a)
    # продолжает пялить и держать за волосы
    img 35189
    w
    img 35190
    w
    img 35251
    w
    img 35191
    m "Что ты делаешь?!"
    img 35192
    m "Мне больно!!!"
    brian "Аааа!!!"
    brian "Кааайф!"
    img 35193
    w

    # video
    #1 -25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_AbbyCustomer_Sex2_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_1_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_1_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_1_25
    with fade
    m "Хватит! Ааай!!!"
    wclean
    brian "Поверещи еще, шлюшка [monica_hotel_name]! Меня это заводит еще больше!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35194
    w

    #2 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_2_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_2_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_2_25
    with fade
    brian "ДАА!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35195
    w
    img 35196
    w
    img 35197
    w
    img 35198
    w

    #3 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_3_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_3_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_3_25
    with fade
    brian "Чертовски охренительно!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35199
    mt "Грязная скотина!"
    mt "Чертов садист!"
    mt "Ублюдок!!!"
    mt "!!!"
    # внезапно в дверь раздается громкий стук
    img 35200
    w

    #4 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_4_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_4_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_4_25
    with fade
    mt "!!!!"
    wclean
    mt "!!!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #5 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_5_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_5_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_5_25
    with fade
    neighbor2 "Развели тут бордель!"
    wclean
    mt "!!!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35245
    neighbor2 "Устроили проститутошную!"
    img 35246
    neighbor2 "Хватит так скрипеть кроватью!"

    #6 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_6_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_6_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_6_25
    with fade
    brian "Ееее!"
    wclean
    neighbor2 "На весь этаж вас слышно, бесстыдники!"
    mt "!!!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35201
    w

    $ ep22_4_dialogues5_escort_4_loop1_flag = False
label ep22_4_dialogues5_escort_4_loop1:

    #7 -25
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Sex2_7_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_7_25.mkv")
    show videov_Monica_AbbyCustomer_Sex2_7_25
    with fade
    m "Чеееерт!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    menu:
        "Уйди вон!":
            img 35202
            m "Уйди вон!"
            img 35247
            neighbor2 "Я не уйду! Это возмутительно!"
            jump ep22_4_dialogues5_escort_4_loop1
        "Я сейчас полицию вызову!":
            img 35203
            m "Я сейчас полицию вызову!"
            img 35248
            neighbor2 "Я сам тебя в полицию сдам, проститутка окаянная!"
            jump ep22_4_dialogues5_escort_4_loop1
        "Отстань от меня, старый извращенец!":
            img 35202
            m "Отстань от меня, старый извращенец!"
            img 35249
            neighbor2 "Устроила тут проститутошную, а меня извращенцем называет!"
            neighbor2 "Бесстыдница!!!"
            jump ep22_4_dialogues5_escort_4_loop1
        "Ты меня достал! Отвали!":
            $ ep22_4_dialogues5_escort_4_loop1_flag = True
            img 35203
            w

            #8 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_8_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_8_25.mkv")
            show videov_Monica_AbbyCustomer_Sex2_8_25
            with fade
            brian "ДАА!!!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            #9 -25
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_9_25= Movie(play="video/v_Monica_AbbyCustomer_Sex2_9_25.mkv")
            show videov_Monica_AbbyCustomer_Sex2_9_25
            with fade
            m "Ты меня достал! Отвали!"
            wclean
            neighbor2 "Окаянная шлюха!"
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            img 35250
            neighbor2 "Весь этаж слышит, что ты тут устроила!"
            jump ep22_4_dialogues5_escort_4_loop1
        "Пошел на хрен отсюда! Трахаюсь, с кем хочу!" if ep22_4_dialogues5_escort_4_loop1_flag == True:
            img 35204
            w

            # video
            #10
            $ localSoundVolume = 1.0
            $ localSoundName = v_Monica_AbbyCustomer_Sex2_1_sound_name
            img black_screen
            with diss
            stop music2
            $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
            $ renpy.music.set_volume(0.2, 0.5, channel="music")
            play music2 "<from " + str(float(rand(0,4))*1.16666667) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
            scene black
            image videov_Monica_AbbyCustomer_Sex2_10= Movie(play="video/v_Monica_AbbyCustomer_Sex2_10.mkv")
            show videov_Monica_AbbyCustomer_Sex2_10
            with fade
            m "Пошел на хрен отсюда! Трахаюсь, с кем хочу!"
            wclean
            stop music2
            $ renpy.music.set_volume(1.0, 0.5, channel="music2")
            $ renpy.music.set_volume(1.0, 0.5, channel="music")

            pass
    # стук замолкает
    img 35199
    mt "Старый извращенец!!!"
    mt "!!!"
    # он резко выходит из нее и, продолжая держать за волосы, подставляет к ее губам свой член
    img 35180
    w
    img 35179
    w
    img 35205
    w
    img 35206
    brian "Оближи его! Быстро!"
    img 35207
    mt "Дьявол!"
    mt "Он толко что был внутри моей... Внутри меня!"
    mt "Я должна теперь это все слизать?!"
    img 35208
    m "Но!.."
    # он водит членом по лицу Моники
    img 35207
    w
    img 35209
    mt "Фууу!"
    brian "Бери его в рот! Выполняй!"
    menu:
        "Сделать, как говорит клиент.":
            pass
    # Моника открывает рот
    img 35212
    brian "В глаза мне смотри, шлюшка [monica_hotel_name]!"
    # Моника поднимает взгляд и с ненавистью смотрит на него
    img 35210
    brian "Вот тааак!"
    # он резко и глубоко вводит свой член
    # Моника давится
    img 35211
    m "Мммпфф!!!"
    img 35213
    w
    img 35214
    m "Мпфхфпфф!!!"
    brian "Ееее! Каааайф!"
    img 35215
    w

    # video
    #1 -15
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_AbbyCustomer_Blowjob1_1_15_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*2.33333333) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Blowjob1_1_15= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_1_15.mkv")
    show videov_Monica_AbbyCustomer_Blowjob1_1_15
    with fade
    brian "Давай, работай!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35216
    w

    #2 -15
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*2.33333333) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Blowjob1_2_15= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_2_15.mkv")
    show videov_Monica_AbbyCustomer_Blowjob1_2_15
    with fade
    brian "Ооо, какая шлюшкааа!"
    wclean
    brian "Дааа!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    # video
    #3 -25
    $ localSoundVolume = 1.0
    $ localSoundName = v_Monica_AbbyCustomer_Blowjob1_1_25_sound_name
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Blowjob1_3_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_3_25.mkv")
    show videov_Monica_AbbyCustomer_Blowjob1_3_25
    with fade
    brian "Оооо, какая ты клевая!"
    wclean
    brian "Ммммм..."
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35217
    w

    #4
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Blowjob1_4_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_4_25.mkv")
    show videov_Monica_AbbyCustomer_Blowjob1_4_25
    with fade
    brian "Каааайф!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    #5
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Blowjob1_5_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_5_25.mkv")
    show videov_Monica_AbbyCustomer_Blowjob1_5_25
    with fade
    brian "Давай, шлюшка, соси старательнее!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35213
    w
    img 35214
    w

    #6
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Blowjob1_6_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_6_25.mkv")
    show videov_Monica_AbbyCustomer_Blowjob1_6_25
    with fade
    brian "Вижу, как ты тащишься от моего огромного члена!"
    wclean
    m "Мпфхфпфф!!!"
    brian "Дааа!"
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    img 35218
    w

    #7
    img black_screen
    with diss
    stop music2
    $ renpy.music.set_volume(localSoundVolume, 0.5, channel="music2")
    $ renpy.music.set_volume(0.2, 0.5, channel="music")
    play music2 "<from " + str(float(rand(0,4))*1.4) + " loop 0.0>Sounds/" + localSoundName + ".ogg"
    scene black
    image videov_Monica_AbbyCustomer_Blowjob1_7_25= Movie(play="video/v_Monica_AbbyCustomer_Blowjob1_7_25.mkv")
    show videov_Monica_AbbyCustomer_Blowjob1_7_25
    with fade
    brian "Еще немного!!! Ооооо!!!"
    wclean
    stop music2
    $ renpy.music.set_volume(1.0, 0.5, channel="music2")
    $ renpy.music.set_volume(1.0, 0.5, channel="music")

    menu:
        "Кончить в рот Моники.":
            img 35217
            brian "Аааа! Сейчас я кончу тебе в рот, шлюшка [monica_hotel_name]!"
            img 35214
            brian "Даааа!!!"
            img 35219
            brian "АААААА!!"
            img 35220
            w
            img 35221
            brian "Глотай!"
            menu:
                "Проглотить.":
                    img 35222
                    mt "Фууу!"
                    img 35223
                    mt "Мерзость!!!"
                    img 35224
                    mt "Меня сейчас стошнит!"
                "Выплюнуть!":
                    img 35225
                    mt "Фууу!"
                    img 35226
                    w
                    img 35227
                    mt "Мерзость!!!"
            pass
        "Кончить на лицо Моники.":
            img 35217
            brian "Аааа! Хочу обкончать твое лицо, шлюшка [monica_hotel_name]!"
            img 35214
            w
            img 35228
            brian "Даааа!!!"
            img 35229
            brian "АААААА!!"
            img 35230
            pass
        "Кончить на грудь Моники.":
            img 35217
            brian "Аааа! Сейчас я кончу тебе на сиськи, шлюшка [monica_hotel_name]!"
            img 35211
            w
            img 35231
            brian "Даааа!!!"
            img 35232
            brian "АААААА!!"
            img 35233
            pass
    # он довольно отстраняется от нее, Моника злая
    img 35234
    mt "Сволочь!!!"
    mt "!!!"
    img 35235
    brian "Повторим, малышка?"
    brian "Хочу еще раз войти в твою киску."
    m "Нет!!!"
    m "Твое время вышло!!!"
    img 35236
    m "А благотворительностью я не занимаюсь!!!"
    m "Деньги на стол и иди отсюда!"
    brian "Хе-хе! Какая ты строптивая, шлюшка [monica_hotel_name]..."
    brian "Мне это нравится!"
    img 35237
    brian "Я к тебе вернусь совсем скоро. Хе-хе!"
    # затемнение, шаги, дверь
    # Моника стоит посередине комнаты, одетая
    img 35238
    mt "Поверить не могу, что я сделала это!"
    mt "Терпеть такое унижение ради заработка!.."
    mt "Разве эта цель оправдывает средства?"
    img 35239
    mt "Это было омерзительно!!!"
    mt "Гадко!!!"
    mt "Тошнотворно!!!"
    mt "!!!"
    # Моника смотрит на стол, на котором лежат деньги
    img 35240
    mt "Хмм..."
    mt "Интересно, сколько этот неудачник-садист оставил денег?"
    # подходит к тумбочке
    img 35241
    mt "150 долларов?!"
    mt "Всего?! За то, что мне пришлось вытерпеть?!"
    mt "Жадный ублюдок!!!"
    mt "Урод! Скотина!"
    img 35242
    mt "Ненавижу, тварь!"
    mt "!!!"
    mt "И мне еще треть отдавать гребаной Эбби?!"
    mt "..."
    # бичность
    menu:
        "Оставить $ 50 на столе и уйти.":
            $ monicaAbbyNoEscortClient5 = day # Моника оставила Эбби процент
            img 35244
            mt "Пусть эта никчемная проститутка Эбби подавится своими $ 50!"
            mt "Придет время и я отомщу ей за это!"
            mt "Будет обслуживать самых грязных извращенцев за копейки!!!"
            mt "!!!"
            # оставляет 50 баксов, себе забирает 100
            # затемнение
            pass
        "Забрать все деньги и уйти.":
            $ monicaAbbyNoEscortClient4 = day # Моника не оставила Эбби процент, забрала все деньги
            img 35243
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

# мысли Моники после встречи с клиентом Эбби, хочет вернуться или пришла в любой другой день
label ep22_4_dialogues5_escort_7:
    # не рендерить!!
    mt "Мне нечего здесь делать сейчас..."
    return

# Моника пришла в эскорт после того, как отработала с клиентом Эбби
label ep22_4_dialogues5_escort_8:
    # Эбби встречает ее на входе в ресторан
    img 35058
    w
    img 35059
    m "Привет, Эбби."
    abby "[monica_hotel_name], привет."
    abby "Как ты отработала с Брайаном? Все окей?"
    # если Моника выгнала клиента и не стала с ним работать и если отработала и забрала все деньги себе
    if monicaAbbyNoEscortClient3 == 0 or monicaAbbyNoEscortClient4 > 0:
        img 35060
        m "Ничего не окей!"
        m "Я этого мерзкого неотесанного типа выгнала!"
        m "И не стала с ним работать!"
        abby "Выгнала?"
        m "Да!"
        img 35061
        abby "И ты ничего не заработала?"
        m "Конечно, ничего! Он не заплатил мне ни цента!"
        m "Мало того, что он грубый мужлан, так еще и жадный!"
        abby "Ладно, если он мне позвонит, я с ним сама буду работать."
        img 35062
        m "И сосед у тебя придурок!"
        abby "Да, я в курсе. Везде сует свой нос. Достал уже!"
        abby "Раз у тебя не получилось поработать с Брайаном, то..."
    # если оставила треть заработка Эбби
    if monicaAbbyNoEscortClient5 > 0:
        img 35060
        m "Я еле вытерпела этого придурка!"
        m "Какой же он отвратительный тип! Мерзкий грубый мужлан!"
        m "К тому же еще и жадный!!!"
        m "Он мне заплатил всего $ 150!!!"
        img 35061
        abby "Это он еще щедро. Ха-ха!"
        abby "Видимо, ему понравилось."
        abby "Оставила мой процент, как я просила, [monica_hotel_name]?"
        img 35062
        m "Да, оставила на столике."
        abby "Отлично, [monica_hotel_name]!"
        abby "Ты хорошо справилась."
    img 30006
    abby "Когда мне позвонит еще кто-нибудь из моих клиентов..."
    abby "Я тебе дам еще возможность подзаработать."
    abby "Ты же не против будешь?"
    img 41426
    m "Я подумаю..."
    abby "Уверена, ты примешь верное решение."
    abby "Ладно, [monica_hotel_name], мне пора бежать работать."
    abby "До встречи!"
    # уходит
    # если Моника выгнала клиента и не стала с ним работать
    if monicaAbbyNoEscortClient4 > 0:
        img 35057
        mt "Эта идиотка Эбби поверила мне, что клиент ничего не заплатил!"
        mt "Отлично!"
        mt "Я считаю, что не должна делиться с ней этими деньгами!"
        mt "Они все мои! Я их заработала!"
    # если Моника отработала и забрала все деньги себе
    if monicaAbbyNoEscortClient3 == 0:
        img 35052
        mt "Пошла она к черту со своими клиентами-идиотами!"
        mt "Пусть сама с ними делает всякие грязные извращенства!"
        mt "Я не собираюсь терперть подобного!"
    # если Моника оставила треть заработка Эбби
    if monicaAbbyNoEscortClient5 > 0:
        img 35044
        mt "$ 150 - это щедро?!"
        mt "Из них я заработала всего $ 100!"
        mt "Пусть эта никчемная проститутка Эбби подавится своими $ 50!"
        mt "Придет время и я отомщу ей за это!"
    return
