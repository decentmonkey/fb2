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




# алкоголик предлагает Монике дать место, чтобы ему выпить. Иначе его может забрать полиция
# Моника приводит его домой, недовольная, говорит что сама не пьет, хотя он предлагает выпить с ним
# Предлагает Монике доллар за то, чтобы выпила
# Затем еще доллар, затем еще
# Моника напивается ничего не помнит, просыпается голая на кровати, а между ног голова алкаша и он спит
# Моника в ужасе прогоняет его



# сцены с ситизенами в квартире у Моники

# гей (citizen13)
# гей по дружбе предлагает Монике хорошо заработать
# в ее квартире он говорит, что у него никогда не было секса с женщиной
# и он хочет ощутить то чувство, когда член находится в женской киске
# он просит Монику за деньги сначала дать ему рассмотреть ее в подробностях и потрогать пальцем
# делает это с большим интересом
# в итоге его научной деятельности у него встает
# Моника смотрит на его маленький член и смоневается, что вообще что-то может получиться
# он тыкается в ее киску членом, но у него ничего не получается
# он пытается уговорить ее на анал, т.к. уверен, что с этим проблем у него не возникнет
# но она все равно отказывается, в итоге он с горем пополам все-таки входит в нее
# секс, оплата 30 долларов

# любитель заключать сделки, лысый, в черном (citizen8)
# предлагает выести их сделку на новый уровень и устроить что-то вроде привата
# готов щедро заплатить за эту сделку
# в ее квартире осматривается с недоумением - не думал, что ты живешь в такой дыре
# Моника говорит, что это не ее квартира
# а что это тогда? эта дыра даже на место для проституток не тянет.
# ты могла бы своим телом зарабатывать очень много денег и вообще ни в чем не нуждаться
# я могу тебя научить, как это нужно делать
# сегодня будет урок первый
# предложи мне себя так, чтобы я тебя захотел купить
# если у тебя получится, я заплачу тебе не менее 50 долларов
# Моника немного столбенеет
# m "Я ещё и исхищряться должна что бы у него встал?"
# m "Я столь прекрасна и изысканна, что мужчины теряют голову от одного лишь взгляда и мне не приходится даже ни чего делать для этого"
# m "Но я даже и предположит не могу что такого извращенного ожидает от меня этот извращенец"
# лысый видит ступор моники и говорит что ему нравятся её чулки и она может поиграться с ними.
# изобретательность с твоей стороны будет также вознаграждена в денежном эквиваленте
# Мон сначала танцует перед ним в одних чулках и туфлях, затем снимает чулки и протягивает их себе между ног (подрочить чулками)
# лысый заводится и говорит что бы она продолжала и что у неё не так уж и плохо выходит, но пока  ещё она не отработала свой 50
# тогда Моника подходит к лысому сидящему в кресле , ставит одну ногу на полокотник,
# лысый тянется к ней что бы сделать куни, но мон накидывает ему на шею чулок , как шарф и тянет чулки вверх и назад,
#  он дрочит и делает ей куни, в то время, как она его немного придушивает
# мон кончает ( ей нравится опять быть главной), а лысый одивает чулок на член и Мон делает ему минет в чулке
# ИЛИ в итоге Моника по его просьбе мастурбирует, а он смотрит на это
# потом заставляет ее открыть рот и сделать ему минет, продолжая мастурбировать
# оплата 50 долларов

# парень с завышенным ЧСВ, лысый, в голубой куртке (citizen15)
# говорит ей, что если она попросит его, то он готов ее трахнуть
# с ним она узнает, что такое секс с настоящим самцом, все девочки от меня без ума
# я тебе даже заплачу за это, детка
# потом, когда ты почувствуешь, что такое настоящий секс, ты меня сама будешь умолять о встрече
# в ее квартире он брезгливо смотрит на мебель
# у тебя что, нет другой хаты? да ладно! ни за что не поверю, что телка с такими сиськами живет тут
# тут постель хоть чистая? нет, я не буду на это ложиться
# слушай, детка, давай ты сначала помоешься в душе с мылом, а потом я тобой займусь
# я должен быть уверен, что ты не грязная. черт его знает, кого ты еще сюда приводила, детка
# Моника психует, но идет в душ, только встает под воду, он голый приходит за ней
# я решил, что помогу тебе помыться
# намыливает ее тело, уделяя особое внимание интимным частям
# а теперь вставай раком, сейчас ты познаешь настоящего мужчину
# секс в душе
# оплата 25 долларов (- 5 баксов за то, что я тебя помыл, детка)
