# при условии, что у Виктории уже был визит в офис Моники
# спустя несколько дней Моника приходит в будний день на работу
label ep215_dialogues4_julia_1:
    # при клике в меню на рабочий кабинет Моники, показываем, как Моника заходит в отдел отчетов
    # ей со всех сторон летит
    w3 "Добрый день, Миссис Бакфетт!"
    w5 "Здравствуйте, Миссис Бакфетт!"
    w1 "Добрый день!"
    # она сделала лицо кирпичом и не глядя ни на кого идет в свой кабинет
    mt "Никчемные людишки. Сидят занимаются никому ненужной никчемной работой!"
    mt "!!!"
    # проходит мимо айтишника, также не глядя на него
    # показываем кадр со спины айтишника, виден его монитор
    # у него на мониторе трансляция видео со скрытой камеры с комнаты отдыха
    # вид из-под стола - две пары женских ног, сидят рядом друг с другом, обе без трусиков (Виктория и Юлия)
    # айтишник про себя думает,
    w2_t "Нужно расставить камеры и под другими столами в офисе..."
    w2_t "И почему я раньше до этого не додумался?"
    # затемнение, смена кадра на кабинет Моники
    return

    # m - Моника говорит
    # mt - Моника думает
    # w2 - айтишник говорит
    # w2_t - айтишник думает
    # julia - Юлия говорит, она не думает
    # victoria - Виктория говорит, она не думает
    # w1  - серая мышка в очках
    # w3 - одна близняшка
    # w4  - вторая близняшка
    # w5  - подхалим
    # w6 - Грета
    # w7 - Лин
    # w7t - Лин думает

label ep215_dialogues4_julia_2:
    # смена кадра - Моника заходит в свой рабочий кабинет
    # смотрит на рабочий стол Юлии, а ее нет на месте
    # Моника думает про себя, куда делась эта никчемная помощница
    # если есть отношения с Юлией, то Моника с облегчением думает, что она спокойно проведет день, без этой дурочки
    # Моника идет к своему столу и тут поворачивает голову в сторону комнаты отдыха
    # в это время в комнате отдыха Виктория встает из-за стола и обращается к Юлии (на Монику они не смотрят)
    # Виктория - Юлия, дорогая, спасибо за чай. мне пора идти по делам
    # Юлия смотрит на нее с обожанием - приходите почаще Мисс Виктория, мне так нравится проводить с вами время
    # Юлия - в следующий раз угощу вас прекрасным зеленым чаем и постараюсь купить что-нибудь вкусное к чаю
    # Юлия встает, Виктория своим привычным жестом указывает на свою щеку, Юлия  наклоняется к ней и чмокает в щечку
    # Виктория - спасибо, Юлия. ты такая милая! обязательно загляну к тебе скоро
    # камера на Монику, у нее шок
    # мысли Моники - КАКОГО ЧЕРТА?!!!?!?!!! ЧТО??? ЭТА ДРЯНЬ!!! ТУТ ДЕЛАЕТ?!?!?!?!
    # кадр на комнату отдыха
    # Виктория направляется к выходу
    # кадр на кабинет Моники и на Монику
    # Виктория проходит мимо нее, Моника смотрит на нее со злым недоумением
    # Виктория с ехидной улыбочкой говорит ей - привет, подружка Моника
    # я знаю, что ты хотела бы поболтать со мной, но у меня дела
    # в следующий раз я обязательно уделю тебе внимание
    # и, кстати, моя ценная вещь все еще у тебя?
    # Моника - да.
    # Виктория - хорошо. скоро я ее заберу. смотри, не потеряй
    # ну все, подружка, пока. передавай привет нашей подружке Мелани. хи-хи.
    # Виктория уходит
    # Моника в шоке смотрит на Юлию, та убирает чашки со стола
    # Моника думает, что Виктория здесь делала? зачем она приходила к Юлии?
    # если отношений с Юлией нет, то Моника рявкает на нее, чтоб та занималась работой на работе, а не всякой ерундой
    # если отношения с Юлией есть, то Моника думает, что надо спросить у этой влюбленной дурочки, о чем они говорили с Викторией
    # Моника подходит к Юлии, обнимает за талию и спрашивает - милая, смотрю, вы подружились с Мисс Викторией
    # Юлия начинает восторженно рассказывать, какая Мисс Виктория классная, и почему Моника раньше ее с ней не познакомила
    # Юлия говорит, что ей Мисс Виктория очень нравится. она такая милая и добрая...
    # Моника притворно улыбается, говорит - да, Юлия, Мисс Виктория очень милая и добрая девушка. с этим не поспоришь
    # про себя думает - ААААА!!! лицемерная сучка!!! притворяется перед Юлией белой овечкой! а сама разнюхивает тут что-то!!
    # снова притворно улыбается, целует Юлию и говорит, что пора идти работать
    # возвращается на свое рабочее место, Юлия - на свое
    return

# при условии, что у Моники была фотосессия перед толпой инвесторов
# через неделю Моника приходит в офис и при клике в меню быстрого перемещения на отдел отчетов
# кадр на сотрудников отдела отчетов
# близняшки и Лин, наклонившись друг к другу, шепчутся, сплетничают
# где-то сбоку от них стоит серая мышь и периодически пытается участвовать в разговоре
# 1-я близняшка - помните, я говорила вам, что та обложка, где она в красном платье и с голой грудью - это только начало?
# Лин - да.
# 1-я близняшка - недавно было фотосессия, где она позировала перед толпой каких-то мужчин почти голая! представляете?!
# 2-я близняшка - ого! серьезно?!
# Лин - да ладно! не может такого быть!
# 1-я близняшка - это информация из проверенного источника. 100 процентов
# 2-я близняшка - что, прямо перед толпой мужчин? а кто они такие?
#не знаю, говорят что какие-то богачи!
#но зачем ей это делать? ради денег?
#да ну, какие-то глупые слухи. у нее у самой куча денег, больше чем у каких-либо богачей
#да не, это правда!
#Но зачем ей это? Ведь деньги ей не нужны
#Не знаю, но зачем-то она делает это! Может быть ей это нравится! Может она извращенка!
#Хорошо что она тебя сейчас не слышит!
# если Моника работала манекеном в магазине одежды
# Лин говорит, что она вообще ее уже где-то видела
# в смысле где? на обложке журнала, где же еще? ну или в интервью
# кстати! я видела интерьвю с ней на приеме у Кэмпбелла, она говорила, что никогда не стала бы делать подобное
# я не верю в эти слухи!
# да я тебе говорю, что информация из достоверного источника
# да ну, бред какой-то. это же сама Миссис Моника Бакфетт! как вообще такое можно было придумать?! тебе наврали. это твой люовник что-ли?
# какой-нибудь младший помощник какого-нибудь начальника в каком-нибудь мелком отделе? я даже знаю такого, этажом ниже
# я как-то видела тебя с ним...
# нет! что ты такое говоришь?! что бы я с ним! ни за что! ты так говоришь, потому что мне завидуешь и сама хотела бы быть с ним!
# с ним?! фу! конечно, нет!
# кадр на Гретту
# она с грозным видом смотрит на сплетничающих сотрудниц
# говорит, что они обе дуры, и чтоб они прекратили спорить
# сотрудницы межу собой переглядываются - достала уже эта жирная корова! везде свой нос сует!
# Гретта - так! вы на работу пришли делом заниматься или сплетничать?!
# близняшки и Лин переглянулись
# тут кто-то из них - Бакфетт идет!!!
# все испуганно разбегаются
