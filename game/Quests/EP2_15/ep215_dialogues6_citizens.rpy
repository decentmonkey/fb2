# алкоголик (citizen11) предлагает Монике дать место, чтобы ему выпить. Иначе его может забрать полиция
# Моника приводит его домой, недовольная, говорит что сама не пьет, хотя он предлагает выпить с ним
# Предлагает Монике доллар за то, чтобы выпила
# Затем еще доллар, затем еще
# Моника напивается ничего не помнит, просыпается голая на кровати, а между ног голова алкаша и он спит
# Моника в ужасе прогоняет его


label citizen11_dialogue11111:
    citizen11 "Ох...моя прекрасная спасительница!"
    citizen11 "Смотри что у меня есть..."
    # показывает деньги
    citizen11 "Я сегодня богат...могу себе позволить снять хату со шлюхой и выпивкой..."
    citizen11 "Но я подумал...почему бы мне не разделить эту радось с моей спасительницей?"
    citizen11 "Заодно сэкономлю на хате и на шлюхе...м?"
    # подмигивает Монике
    m "Я не шлюха, а моя квартира не притон для алкашей, иди в Shiny Hole место как раз для тебя."
    m "Или можешь пить на улице, как раньше!"
    citizen11 "Чего ты обижаешься?"
    citizen11 "Я же сказал, хочу разделить эту радось с моей спасительницей."
    citizen11 "А на улицу мне нельзя...копы сказали что загребут, если увидят меня пьющим на тратуаре."
    mt "Если я соглашусь, этот алкаш может решить что сможет использовать мою квартиру, как место для пьянства.."
    mt "Этого еще не хватало..."
    citizen11 "Я могу вознаградить тебя за помощь..."
    menu:
        mt "Мне не нужны проблемы ни с алкашом ни с копами.":
            m "Мой дом не место для алкашей с улицы!"
            citizen11 "Видимо тебе не нужны ни деньги, ни хороая выпивка."
            # алкаш уходит. прекращение квеста.
            return

        mt "Хммм...деньги за то что бы ему было где выпить - лучше, чем танцевать у пилона.":
            m "Идем..."
            return
return

label citizen11_dialogue11111:
    # в квартире Моники
    m "Пей там..."
    # указывает на столик рядом с раскладушкой
    mt "Нужно следить что бы этот алкаш не стал здесь все громить, когда напьется и не украл ни чего..."
    citizen11 "А ты что так и будешь стоять в стороне? Иди я угощу тебя чудесным напитком..."
    m "Я не пью..."
    citizen11 "Я не предлагаю тебе пить, просто составь мне компанию. И я буду платить по 1 $ за каждую выпитую рюмку..."
    mt "1 $ за то что бы я вливала эти помои в свое прекрасное тело?"
    mt "Моника, стоит ли это того?"
    mt "Я и этот алкаш - отброс общества..."
    mt "Такая богиня как я привыкла вкушать изысканные шампанские вина среди элиты общества..."
    mt "А это пойло совсем не для леди с прекрасными манерами и утонченным вкусом ..."
    citizen11 "Одна стопка-1 $."
    menu:
        m "Я же сказала что не пью...":
            m "Тебе нужно было место для пьянки, так что сиди и пей..."
            m "И больше не предлагай мне эти дешевые помои."
            citizen11 "Ты мне портишь весь натсрой."
            citizen11 "Я пожалуй найду более приветливого компаньона."
            # алкаш уходит. прекращение квеста.
            return

        mt "Видимо этот алкаш не отстанет от меня...":
            mt "Выпью одну и он от меня отстанет."
            citizen11 "Вот, держи одна стопка - 1 $ как договаривались."
            # Моника выпивает и морщится
            mt "ФИ! Эти помои ещё хуже чем я предполагала..."
            mt "Кажется я сейчас же умру от отравления..."
            mt "Ох ...какое-то старнное ощущение..."
            # алкаш на заднем плане бормочет
            citizen11 "...вот...и я значит ему говорю ...ик..."
            citizen11 "...ты ...ик...рыбу вислом по башке...ик..."
            citizen11 "Вот, ещё одна стопка - 1 $..."

            menu:
                mt "Нужно прогнать этого алкаша пока не поздно.":
                    m "Забирай свое пойло и уходи..."
                    citizen11 "Кудаж я пойду...я уже и по второй нам налил."
                    m "ВОН!!!НЕМЕДЛЕННО!!!"
                    m "Ох, что-то мне плохо."
                    citizen11 "Шлюха -предательница, а не спасительница..."
                    # алкаш уходит.
                    # моника отрубается, прекращение квеста.
                    return

                mt "Что это он бормочет...и что суёт мне?":
                    m "Я хотела сказать..."
                    citizen11 "Да...помню я, милая...помню... одна стопка - 1 $..."
                    m "Что......?"
                    mt "Что это за мерзость? Почему она так воняет?..."
                    mt "Или..."
                    citizen11 "Да-да...пей, давай я помогу...и....ик...мы пошли значит с этой ...ик.. старой шлюхой..."
                    # мон выпивает вторую рюмку
                    m "Я...что...."
                    citizen11 "А у неё....ик....и сиьки...у тебя ...это ик...сколько..."
                    mt "Что за странный привкус во рту..?"
                    mt "И почему вся комната....ик....ой."
                    # алкаш даёт третью рюмку
                    citizen11 "Ты это...ик....быстро что-то....на."
                    mt "Что проис... что это ....ик....льёт меня...ик."
                    # мон выпивает третью рюмку
                    # затемнение
                    # Моника просыпается голая на кровати, а между ног голова алкаша и он спит
                    # рядом валяется пустая бутылка
                    # Моника ВСКАКИВАЕТ И В УЖАСЕ ХВАТАЕТСЯ ЗА ГОЛОВУ
                    mt "О УЖАС!!!!! ЧТО ЗДЕСЬ ПРОИЗОШЛО!?!?!?"
                    mt "КАЖЕТСЯ Я УПАЛА НА САМОЕ ДНО !!!"
                    mt "МОЯ ЖИЗНЬ ПРЕВРАТИЛАСЬ В БЕСКОНЕЧНЫЙ КОШМАР!!!!"
                    mt "КОШМАР КОТОРЫЙ НИ КОГДА НЕ ЗАКОНЧИТСЯ...."
                    mt "И Я.....Я.....О БОЖЕ!!!"
                    mt "Я ДОЛЖНА СОБРАТЬСЯ!!!!"
                    mt "ЭТО СКОРО ВСЁ ЗАКОНЧИТСЯ!!! ЭТО ВРЕМЕННЫЕ ТРУДНОСТИ!!!"
                    mt "Я - МОНИКА БАКФФЕТ!!! Я- БИЗНЕС ЛЕДИ!!!"
                    mt "Я ПОЛОЖУ ЭТОМУ КОНЕЦ!!!"
                    mt "И начну я с этого грязного отродья!!!"
                    # Моника даёт поджопник пьяному алкашу
                    # алках подскакивает и пытается прийти в себя
                    m "ПРОВАЛИВАЙ ИЗ МОЕЙ КВАРТИРЫ!!!МЕРЗКИЙ АЛКАШ!!!!!"
                    m "ТЫ РЕШИЛ ВОСПОЛЬЗОВАТЬСЯ СНАЧАЛА МОЕЙ ДОБРАТОЙ, А ПОТОМ И МОИМ ТЕЛОМ!"
                    m "ПРОВАЛИВАЙ ГРЯЗНОЕ ЖИВОТНОЕ!!!!"
                    # алкаш полупьяный
                    citizen11 "Я хотел вознаградить...ик...как договар..."
                    # алкаш болтает языком верх-вниз намекая на куни
                    m "А НУ ПРОВАЛИВАЙ!!!!!"
                    # Моника даёт ЕЩЁ поджопник
                    # алкаш убегает
                    # Моника в гневе
                    mt "КОГДА Я ВЕРНУ СЕБЕ СВОЮ ЖИЗНЬ!!!! Я СРАВНЯЮ ЭТОТ РАЙОН С ЗЕМЛЕЙ! И ВСЕХ ЕГО ОБИТАТЕЛЕЙ."
                    m "ААААААААААААААААААААААААААААААААААААААААААААААА!!!!!!!!!!!!!!!!!!"

                    return
    return




# у пилона
# любитель заключать сделки, лысый, в черном
label ep215_dialogues6_citizens_1:
    menu:
        "Пригласить к себе.":
            pass
    citizen8 "У меня для тебя есть предложение."
    m "Что еще за предложение?"
    citizen8 "Я предлагаю вывести нашу сделку на новый уровень."
    m "Что это значит?"
    citizen8 "Ты устроишь для меня что-то вроде привата..."
    citizen8 "А я готов щедро заплатить за эту сделку."
    citizen8 "Что скажешь?"
    menu:
        "Согласиться.":
            # если Моника не арендует квартиру у Джека
            if monicaShawarmaApartment5 == False:
                mt "Щедро заплатить?"
                mt "..."
                mt "А если эта старая карга увидит, что я работаю здесь?!"
                mt "Хммм..."
                mt "Может быть..."
                mt "А что, если я сделаю это, но не здесь..."
                mt "Черт! Но мне больше некуда пойти!"
                mt "А здесь я это делать не собираюсь!"
                m "Нет! Я не собираюсь заключать никакие сделки!!"
                $ notif(t_("Монике некуда вести клиентов."))
                return
            # если арендует квартиру у Джека
            if monicaShawarmaApartment5 == True and monicaShawarmaApartment9 == False:

                pass
        "Хватит с тебя того, что ты уже видел!":
            mt "Я не могу себе этого позволить!"
            mt "Я еще не настолько опустилась!"
            mt "И, надеюсь, этого не произойдет НИКОГДА!"
            m "Нет! Я не собираюсь заключать никакие сделки!!"
            return
    # Моника в сомнениях
    mt "Вот дьявол!"
    mt "Если я ему откажу сейчас, то вообще ничего не заработаю..."
    mt "А мне нужны деньги..."

    #
    $ notif(_("Моника должна выплачивать Перри долг в размере $ 50 000."))
    mt "Я должна выплачивать долг этой мерзкой извращенке Перри!"
    #

    # если Монику выгнали с эскорта
    #
    $ notif(_("Моника больше не работает в ВИП-эскорте."))
    #
    mt "Я могла бы заработать в ВИП-эскорте, но меня туда больше не пустят..."
    #

    mt "Моника, что же делать?"
    mt "Этот клиент сказал, что он щедро заплатит..."
    mt "Хммм..."
    mt "Может быть..."
    mt "А что, если я сделаю это, но не здесь..."
    mt "А в той ужасной дыре, которую я арендую у придурка Джека?!"
    mt "Там тебя точно никто не увидит!"
    mt "И ты сможешь заработать денег!"
    # лысый ее спрашивает
    citizen8 "Ну? Заключаем сделку?"
    m "Я не буду делать этого здесь."
    m "У меня есть место..."
    m "И можно пойти туда..."
    citizen8 "Пошли!"
    # затемнение
    # смена кадра, апартаменты Моники
    # лысый осматривается с недоумением
    citizen8 "Не думал, что ты живешь в такой дыре..."
    # Моника говорит с деловым видом
    m "Вообще-то, это не моя квартира..."
    citizen8 "А что это тогда?"
    citizen8 "Эта дыра даже на место для проституток не тянет."
    m "!!!"
    citizen8 "Ты могла бы своим телом зарабатывать очень много денег..."
    citizen8 "И ни в чем не нуждаться."
    mt "Какие все вокруг умные!"
    mt "Я посмотрела бы на тебя, придурок, если бы ты оказался в моем положении!"
    mt "!!!"
    citizen8 "Я могу тебя научить, как это нужно делать."
    citizen8 "Сегодня у нас будет первый урок."
    m "Урок?!"
    citizen8 "Да."
    citizen8 "Предложи мне себя так, чтобы я захотел купить тебя."
    citizen8 "Если у тебя получится, я заплачу тебе $ 50."
    # Моника немного столбенеет
    mt "Я еще и стараться должна для того..."
    mt "Чтобы у какого-то никчемного неудачника встал его отросток?!"
    mt "Да он вообще знает, кто перед ним стоит?!"
    mt "Я само совершенство!"
    mt "Мужчины теряют голову от одного лишь взгляда на мою восхитительную фигуру!"
    mt "И мне не приходится даже ничего делать для этого!"
    mt "О каких уроках говорит мне этот идиот?!"
    mt "?!"
    menu:
        "Мне нужны деньги.":
            pass
        "Отказаться.":
            m "Нет!"
            m "Я не собираюсь заниматься тут какими-то глупостями!!"
            m "У меня есть более важные дела!!!"
            citizen8 "Ты отказываешься от такой хорошей сделки?"
            m "Да! Отказываюсь!"
            m "Убирайся вон отсюда!!!"
            mt "Никчемный неудачник!!!"
            mt "!!!"
            # он уходит
            return
    # Моника в задумчивости
    mt "Он хочет, чтобы я покривлялась перед ним за $ 50?!"
    mt "Черт!"
    mt "Возможно, этому извращенцу достаточно будет того, чтобы он просто посмотрел на меня?"

    # если Моника танцует в пабе на сцене
    mt "Как тем неудачникам, которые ходят в грязную дыру Shiny Hole..."
    mt "Интересно, он бывает там?"
    mt "Может, он видел мои выступления?"

    mt "Мне придется согласиться, чтобы заработать деньги."
    mt "В конце концов, мне нужны деньги, чтобы скорее вернуть себе свою роскошную жизнь!"
    mt "И забыть все, что со мной происходит сейчас, как страшный сон!"
    mt "!!!"
    # лысый видит ступор Моники
    citizen8 "Не знаешь, с чего начать?"
    citizen8 "Так и быть... Я дам тебе подсказку."
    # он садится на стул, осматривает Монику оценивающе
    citizen8 "Танцуй и снимай свою ужасную одежду!"
    citizen8 "Я хочу увидеть твое тело."
    # Моника танцует и постепенно снимает свою одежду
    # потом танцует перед ним в одних туфлях, принимает различные позы, как в танцах на приватах
    # когда она полностью раздевается, он говорит
    citizen8 "Изобретательность с твоей стороны будет вознаграждена в денежном эквиваленте."
    citizen8 "Сделай так, чтобы я захотел тебя трахнуть."
    mt "Что?!"
    mt "Грязный извращенец!"
    mt "!!!"
    citizen8 "Потрогай свою киску..."
    citizen8 "Я хочу посмотреть, как ты это делаешь."
    citizen8 "Я заплачу тебе за это на $ 10 больше."
    mt "Черт!"
    mt "Моника, как же все это омерзительно!"
    mt "Но мне нужны эти деньги!"
    mt "!!!"
    # Моника раздвигает ноги и прикасается к своей киске
    # лысый пристально наблюдает и заводится
    citizen8 "Продолжай!"
    citizen8 "У тебя не так уж и плохо выходит..."
    citizen8 "Дааа..."
    citizen8 "А теперь подойди поближе."
    # тогда Моника подходит к лысому сидящему в кресле, ставит одну ногу на полокотник
    # продолжает мастурбировать, а он смотрит на это
    citizen8 "Хорошо..."
    citizen8 "Следующий этап нашей сегодняшней сделки..."
    # Моника отходит от него, он встает и расстегивает штаны
    citizen8 "Ложись на постель и открывай рот."
    # Моника медлит
    mt "Твою мать!"
    mt "!!!"
    mt "Он собирается заняться со мной ЭТИМ?!"
    mt "Моника, неужели ты опустилась до такого?!"
    mt "Боже, какой кошмар!"
    mt "!!!"
    mt "Но он обещал мне заплатить целых $ 60!"
    mt "Я не могу сейчас отказаться от этих денег!"
    mt "Черт! Черт! Черт!"
    mt "!!!"
    # Моника ложится на кушетку лицом вверх и открывает рот (головой не к стене, а к другому краю кушетки)
    # у Моники голова немного свисает сниз с края кушетки, рот открыт
    # лысый встает над ее лицом и с положения стоя вводит свой член глубоко в горло, при этом придерживает ее за шею
    # Моника давится, но не может пошевелить головой или сопротивляться
    m "!!!"
    m "ХПФМММ!"
    m "ММПППХХХФФФФ!!!"
    # минет
    citizen8 "Ммммм..."
    citizen8 "Хорошая сделка... Даааа..."
    citizen8 "Аааа..."
    citizen8 "Люблю, когда сделки такие хорошие..."
    citizen8 "Оооо..."
    menu:
        "Кончить в рот Моники.":
            citizen8 "ДАААА..."
            citizen8 "АААААААА!!!"
            m "!!!"
            m "ХПФМММ!"
            pass
        "Кончить на лицо Моники.":
            citizen8 "ДАААА..."
            citizen8 "АААААААА!!!"
            mt "ФУУУ!!!"
            mt "!!!"
            pass
        "Кончить на грудь Моники.":
            citizen8 "ДАААА..."
            citizen8 "АААААААА!!!"
            mt "ФУУУ!!!"
            mt "!!!"
            pass
    mt "Мерзко!"
    mt "Грязно!"
    mt "Отвратительно!!!"
    mt "!!!"
    # затемнение
    # лысый и Моника одетые
    # лысый протягивает ей деньги
    citizen8 "Вот твои $ 60."
    citizen8 "Ты их сегодня неплохо отработала."
    citizen8 "Подумай, что ты сможешь предложить для следующей нашей сделки..."
    citizen8 "Чтобы заинтересовать меня..."
    citizen8 "Сегодняшняя сделка закрыта."
    # уходит
    mt "Это было ужасно!"
    mt "Мое горло..."
    mt "У меня все болит внетри!"
    mt "О какой следующей сделке говорил этот придурок?!"
    mt "Никаких сделок!!!"
    mt "Грязное животное!"
    mt "Ненавижу!!!"
    mt "!!!"
    return
