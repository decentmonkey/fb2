default monicaRyanStudioPhotoshoot1 = 0 # Моника пошла в студию Райена
default monicaRyanStudioPhotoshoot2 = 0 # Моника согласилась сняться для коллекции Райена
default monicaRyanStudioPhotoshoot3 = 0 # Моника согласилась на откровенный кадр у Райена
default monicaRyanStudioPhotoshoot4 = 0 # Моника пошла в студию Райена повторно после отказа от съемки

default ep22_5_dialogues4_rayan_1_repeat = False

# при условии, что было свидание с Мэйсоном в ресторане
# при клике на стол в рабочем кабинете Моники
label ep22_5_dialogues4_rayan_1:
    if ep22_5_dialogues4_rayan_1_repeat == True:
        menu:
            "Пойти в студию Райена.":
                $ monicaRyanStudioPhotoshoot4 = day # Моника пошла в студию Райена повторно после отказа от съемки
                pass
            "Не сегодня.":
                mt "Я обязательно схожу... Позже..."
                mt "Этот жалкий фотограф никуда не денется."
                mt "А у меня есть более важные дела сегодня."
                return False
    if ep22_5_dialogues4_rayan_1_repeat == False:
        mt "Если я этого не сделаю - он отправит мои откровенные снимки Бифу."
        mt "А этот придурок с радостью пустит их в печать!"
        mt "Мне нельзя допустить этого!"
        mt "!!!"
        mt "Возможно, стоит пойти в студию к этому Райену?.."
        mt "Он обещал, что на кадрах для его коллекции не будет видно моего лица... И что я буду в маске..."
        mt "..."

        menu:
            "Пойти в студию Райена.":
                $ monicaRyanStudioPhotoshoot1 = day # Моника пошла в студию Райена
                pass
            "Не сегодня.":
                mt "Я обязательно схожу... Позже..."
                mt "Этот жалкий фотограф в любом случае не посмеет ослушаться меня..."
                mt "И будет ждать моего визита."
                mt "Никуда он не денется."
                mt "А у меня есть более важные дела сегодня."
                return False
        # Моника сидит в кресле за своим рабочим столом с задумчивым видом
        mt "Свидание с этим никчемным Мэйсоном прошло по плану..."
        # если работает в эскорте и был шантаж от Дэниела
        mt "За исключением некоторых моментов, о которых я даже думать не хочу."
        #
        mt "Теперь он у меня на крючке."
        mt "Иначе и быть не могло!"
        mt "Перед такой шикарной женщиной, как Я, не устоит ни один мужчина!"
        mt "!!!"
        mt "Насчет того, как дальше использовать Мэйсона..."
        mt "Я подумаю немного позже."
        mt "Сейчас у меня есть одно более важное дело - фотографии с дурацкой рамой Кэмпбелла."
        mt "Мне нельзя допустить того, чтобы они попали в руки придурка Бифа!"
        mt "Я на этих кадрах голая! Абсолютно!"
        mt "А этот идиот с радостью опубликует их!"
        mt "Нет-нет!"
        mt "Моя голая попа в раме не выйдет в печать!"
        mt "Я должна поехать к этому никчемному фотографу Райену..."
        mt "И отобрать для Бифа снимки поприличнее."
        mt "И лучше не затягивать с этим!"
        mt "!!!"
        # поворачивается к Юлии
        # если есть отношения с ней
    	#
    	$ notif(_("Моника состоит в отношениях с Юлией."))
    	#
        m "Юлия, милая..."
        # Юлия игриво улыбается ей
        julia "Да, Миссис Бакфетт?"
        julia "Вы по мне соскучились и хотите поцеловать меня?"
        # Моника закатывает глаза
        mt "!!!"
        # потом притворяясь, улыбается ей
        m "Да, милая! Очень хочу!"
        # Юлия подходит к ней и чмокает в губы
        julia "Мммм..."
        julia "Я тоже соскучилась, Миссис Бакфетт..."
        m "Милая... Я хотела тебя кое о чем попросить..."
        m "У меня назначена важная рабочая встреча с фотографом Райеном."
        m "Найди его номер телефона, предупреди о моем визите и узнай адрес его студии."
        julia "Хорошо, Миссис Бакфетт."
        julia "Еще один поцелуй и будет сделано."
        # снова чмокает ее в губы
        julia "Обожаю вас, Миссис Бакфетт!"
        m "И я тебя, милая..."
        m "Позвони, пожалуйста, Райену. Это действительно важная встреча..."
        julia "Да-да, я сейчас все сделаю."
        # Юлия выходит из кабинета, игриво оглядываясь на Монику и подмигивая ей
        #
        # если нет отношений
        m "Юлия! Подойди сюда! Быстро!"
        # Юлия испуганно подбегает
        julia "Да, Миссис Бакфетт?"
        m "У меня важная рабочая встреча с фотографом Райеном."
        m "Найди его номер телефона, предупреди о моем визите и узнай адрес его студии."
        julia "Хорошо, Миссис Бакфетт."
        m "И поторопись! Это очень важно!"
        julia "Да-да, я сейчас все сделаю."
        # Юлия убегает из кабинета
        #
        mt "Никчемная помощница!"
        mt "Такая же никчемная, как и все остальные работнички!"
        mt "Бесполезные муравьишки!"
        mt "!!!"
    #    return

        mt "Мне нужно как можно скорее забрать снимки у никчемного фотографа Райена."
        mt "Если я этого не сделаю - он отправит их Бифу."
        mt "Мне нельзя допустить этого!"
        mt "!!!"
        mt "Я уверена, что это не займет много времени."
        mt "Этот фотограф готов сделать все так, как скажу Я."
        mt "Ведь Я - глава журнала, а он - всего лишь какой-то жалкий фотограф..."
        mt "Да, Моника, нужно закрыть вопрос с этими гребаными снимками! Сегодня же!"
        mt "!!!"
        $ ep22_5_dialogues4_rayan_1_repeat = True
    return

# апартаменты Райена
label ep22_5_dialogues4_rayan_3:
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(_("СТУДИЯ РАЙАНА..."))
    scene black_screen
    with Dissolve(1)

    # звук лифта
    # Моника заходит в его апартаменты
    img 44807
    mt "Это что, его апартаменты?!"
    mt "Какого черта?!"
    mt "Я у этой никчемной помощницы просила узнать адрес студии, а не апартаментов!"
    mt "Юлия - идиотка!"
    mt "Ни на что не способная бывшая гувернантка!"
    mt "!!!"
    # Райен выходит навстречу Монике
    img 44808
    ryan "Миссис Бакфетт, добрый вечер!"
    # целует ей руку, как обычно
    img 44809
    ryan "Я несказанно рад вашему визиту!"
    img 44810
    ryan "Это честь для меня, принимать такого статусного гостя в моей скромной студии!"
    # Моника с надменным видом
    img 44811
    m "Это твоя студия, Райен?"
    m "Я решила, что это твой дом..."
    # Райен улыбается
    img 44812
    ryan "Все верно, Миссис Бакфетт."
    ryan "Моя студия находится в моих апартаментах."
    ryan "Я здесь и живу, и занимаюсь творчеством."
    # приглашает ее жестом войти
    img 44813
    ryan "Проходите, Миссис Бакфетт."
    ryan "Чай, кофе? Может, чего-то покрепче?"
    # Моника высокомерно
    img 44814
    m "Нет, спасибо, Райен."
    m "Ничего не нужно. Давай сразу перейдем к делу..."
    m "У меня мало времени. Ты же понимаешь, что я очень занятая леди."
    img 44815
    ryan "Да, конечно, Миссис Бакфетт..."
    # затемнение, каблуки
    # они проходят в студию
    # Моника осматривается со снобским выражением на лице
    img 44749
    w
    img 44750
    w
    img 44751
    mt "Что это еще такое?"
    mt "Это разве студия?!"
    mt "Какая-то непонятная каморка! Фи!"
    mt "Как будто в каком-то подвале!"
    img 44752
    mt "Другое дело - студия в офисе моего журнала!"
    # Райен подходит к ней и загадочно улыбается
    img 44753
    ryan "Миссис Бакфетт..."
    ryan "Не обращайте внимания, у меня тут всегда небольшой творческий беспорядок."
    img 44754
    ryan "Можете присесть вот на этот стул..."
    # указывает рукой на реквизит для фотосъемки, стул стоит посреди полотна
    img 44755
    m "..."
    # Моника с важным видом садится на него
    img 44756
    w
    img 44757
    m "Райен, я хотела бы посмотреть снимки с рамой Кэмпбелла..."
    m "У меня нет времени на светскую болтовню."
    # Райен чешет затылок
    img 44758
    ryan "Кхм..."
    ryan "Понимаете, в чем дело, Миссис Бакфетт..."
    ryan "Я... Я сначала хотел бы рассказать вам о своем проекте."
    img 44759
    mt "Этот придурок думает, что меня это должно интересовать?!"
    mt "Какое мне дело до его жалких делишек?!"
    mt "Но, видимо, мне придется сделать заинтересованный вид..."
    mt "Чтобы добраться, наконец, до этих чертовых снимков!"
    # делает притворно-заинтересованное лицо
    img 44760
    m "У тебя есть свой проект?"
    m "Как интересно, Райен..."
    # Райен улыбается
    img 44761
    ryan "Да, Миссис Бакфетт."
    ryan "Я являюсь большим ценителем женской красоты."
    ryan "И стараюсь отразить эту свою страсть в своих работах."
    ryan "У меня есть уже целая коллекция работ, посвященных изяществу женского тела."
    img 44762
    ryan "И для завершения моей коллекции мне не хватает лишь одной..."
    ryan "Которая станет вишенкой на торте, так сказать."
    img 44763
    w
    img 44764
    m "..."
    img 44765
    ryan "Совсем скоро у меня будет выставка..."
    ryan "Она будет проходить не только в нашем городе, но и по всей стране."
    ryan "Мои работы увидит весь мир, Миссис Бакфетт!"
    img 44766
    mt "А я тут при чем?!"
    mt "Зачем мне вся эта лишняя информация?!"
    mt "!!!"
    # Райен пристально на нее смотрит и улыбается
    img 44767
    ryan "Вы, наверное, не понимаете, зачем я все это вам рассказываю?"
    m "..."
    m "Зачем же?.."
    ryan "Вишенка на торте - это фотосессия с вашим участием, Миссис Бакфетт..."
    img 44768
    m "С моим?!"
    m "?!"
    img 44769
    ryan "Да, Миссис Бакфетт."
    ryan "Кто, как не глава журнала о моде..."
    ryan "Которая не только поддерживает новый курс своего журнала, снимаясь в пикантных фотосессиях..."
    ryan "Но также является самой красивой женщиной... И смелой... И притягательной..."
    # Моника смотрит на него, подозрительноп прищурившись
    img 44770
    mt "Бред какой-то!"
    mt "С какой стати я должна сниматься для его дурацкой выставки?!"
    mt "Он что, думает, я получаю удовольствие от этих пошлых фотосессий?!"
    mt "Такой же фотограф-извращенец, как и Алекс!"
    mt "!!!"
    # Моника принимает высокомерный вид
    img 44771
    m "Райен..."
    m "Назови мне хотя бы одну причину..."
    m "Из-за которой Я, Моника Бакфетт, глава известного журнала..."
    m "Владелица многомиллионного бизнеса..."
    m "И весьма занятая бизнес-леди..."
    m "Должна дать согласие на съемку перед объективом твоей камеры."
    # насмешливо приподнимает уголок губ в улыбке
    img 44772
    ryan "Причина есть."
    ryan "Снимки с фотосессии в офисе Мистера Кэмпбелла..."
    # Моника встакивает со стула
    img 44773
    m "Что?!"
    m "Мы с тобой не так договаривались, Райен!!!"
    m "Ты мне сказал, что..."
    img 44774
    ryan "Что буду рад вашему визиту в свою студию."
    ryan "И, поверьте, это действительно так, Миссис Бакфетт."
    img 44775
    m "Хватит заговаривать мне зубы!"
    m "Меня интересуют только снимки! Никаких фотосессий!!!"
    m "!!!"
    # Райен абсолютно спокоен
    img 44776
    ryan "Вам совсем необязательно давать согласие именно сейчас, Миссис Бакфетт."
    ryan "Я задержу снимки у себя еще на несколько дней и пока не буду посылать их в ваш журнал."
    ryan "Но только на несколько дней, не больше."
    ryan "Потом я буду вынужден их отправить, так как не смею нарушать приказ Мистера Кэмпбелла."
    ryan "Все-таки он очень важный клиент, сами понимаете..."
    img 44777
    m "Для тебя, Райен, нет более важного клиента, чем Я!"
    m "!!!"
    img 44778
    ryan "Миссис Бакфетт, вы - модель."
    ryan "Приглашенная модель для фотосессии, за которую Мистер Кэмпбелл весьма щедро заплатил мне."
    ryan "Так что, повторюсь, его приказ я не могу нарушить."
    ryan "Но я могу послать не все снимки, Миссис Бакфетт..."
    ryan "А только те, которые отберете вы лично."
    ryan "После того, как сниметесь в фотосессии для моей коллекции..."
    img 44779
    m "Это твое условие, Райен?"
    ryan "Да, Миссис Бакфетт."
    img 44780
    mt "Черт!!!"
    menu:
        "Согласиться.":
            pass
        "Вот еще! Пошел он к черту!":
            # Моника надменно
            img 44781
            mt "Этот никчемный жалкий фотограф решил ставить мне свои условия?!"
            mt "МНЕ?! Монике Бакфетт?!"
            mt "!!!"
            img 44782
            m "Я не собираюсь принимать участие ни в каких сомнительных фотосессиях!"
            ryan "Тогда я буду вынужден отказать вам в отборе снимков..."
            m "!!!"
            img 44783
            ryan "Притом, это не какая-нибудь сомнительная фотосессия, Миссис Бакфетт."
            ryan "Эта коллекция вполне соответствует новому курсу вашего журнала."
            img 44784
            m "И что это значит?"
            pass
    # Моника смотрит на него подозрительно
    img 44785
    m "Как именно будет проходить эта фотосессия?"
    # Райен рукой указывает на стул, на котором сидела Моника
    ryan "Здесь, в моей студии, Миссис Бакфетт."
    img 44786
    ryan "Реквизит, как видите, я уже подготовил."
    m "Фотосессия со стулом?"
    img 44787
    ryan "Да, Миссис Бакфетт."
    ryan "Это будут потрясающие кадры!"
    ryan "Изящные очертания прекрасного обнаженного женского тела в приглушенном свете софитов..."
    img 44788
    m "Стоп!"
    m "Обнаженного?!"
    m "Ты что, с ума сошел?!"
    m "Я не собираюсь раздеваться!.."
    ### если приходит повторно после того, как отказала - repeat отсюда
    img 44789
    ryan "На вас, Миссис Бакфетт, будет маска. Вашего лица никто не узнает."
    ryan "Тем более, фотосессия будет проходить в полумраке..."
    ryan "И сразу же по окончанию нашей съемки, я покажу вам снимки с фотосессии Кэмпбелла."
    img 44790
    m "..."
    # коррапшн
    menu:
        "Согласиться на фотосессию.":
            $ monicaRyanStudioPhotoshoot2 = day # Моника согласилась сняться для коллекции Райена
            pass
        "Нет!":
            # Моника надменно
            img 44791
            mt "Нет! Я не собираюсь обнажаться для его никчемной выставки!"
            mt "Пошел он к черту со своими условиями!"
            mt "Очередной шантажист-извращенец!!!"
            mt "!!!"
            # Моника зло
            img 44793
            m "Нет, Райен!"
            m "Я не собираюсь раздеваться перед объективом твоей камеры!"
            m "Я пришла сюда, чтобы воспрепятствовать публикации моих обнаженных фото..."
            m "А ты ставишь мне условие, при котором я должна снова сниматься обнаженной!"
            m "Чтобы потом демонстрировать эту работу на весь мир!"
            m "Ты в своем уме?!"
            # Моника идет к выходу, Райен ей вслед
            img 44794
            ryan "Тогда я буду вынужден отказать вам в отборе снимков..."
            img 44795
            m "Мне плевать!"
            m "!!!"
            img 44796
            ryan "Миссис Бакефтт, я дам вам на раздумье несколько дней."
            ryan "Вы можете вернуться в любой момент."
            img 44797
            m "НЕТ!"
            # Моника уходит
            return
    # Моника недовольно смотрит на него
    img 44791
    mt "Чертов фотограф-извращенец!"
    mt "Он ставит мне условие, при котором я должна снова сниматься обнаженной!"
    mt "Чтобы потом демонстрировать эту работу на весь мир!"
    mt "!!!"
    img 44792
    mt "С другой стороны, если моего лица и правда не будет видно."
    mt "Он говорил про полумрак и маску..."
    mt "..."
    mt "Зато я смогу сделать так, чтобы Биф не опубликовал откровенные кадры с фотосессии у Кэмпбелла."
    mt "А этот гребаный фотограф говорил, что там много таких снимков!"
    mt "Дьявол!"
    mt "!!!"
    # она решительно смотрит на Райена
    img 44798
    m "Моего лица точно не будет видно?!"
    ryan "Вы сами себя не сможете узнать на этих снимках, Миссис Бакфетт."
    ryan "Я вам обещаю это!"
    img 44799
    ryan "Я хочу использовать только красоту вашего тела."
    ryan "А не вашу популярность как медийной личности..."
    # смотрит на него угрожающе
    img 44800
    m "Уверен?!"
    m "!!!"
    img 44801
    ryan "Абсолютно!"
    # грозно тычет в него пальцем
    img 44802
    m "Райен!"
    m "Если хоть одна живая душа узнает о том, что я как-то причастна к этой твоей выставке!.."
    m "Что я была у тебя в студии и снималась для твоей коллекции!.."
    m "Я тебя предупреждаю!.."
    # Райен торопливо
    img 44803
    ryan "Никто не узнает, Миссис Бакфетт."
    ryan "Это останется только между нами."
    ryan "Это даже хорошо, что никто не будет знать, кто является моей моделью..."
    img 44804
    ryan "Эта загадочность добавит изюминку в нашу с вами совместную работу." # подмигивает
    img 44805
    # Моника снова принимает надменный вид
    img 44806
    m "Давай мне эту чертову маску!"
    m "У меня мало времени, так что - за дело!"
    # затемнение
    # спустя некоторое время Моника стоит в аутфите для съемки, свет выключается
    # Райена нигде не видно
    
    mt "Поверить не могу!"
    mt "Пришла забрать свои обнаженные снимки..."
    mt "А теперь стою голая, чтобы снова сняться!.."
    mt "Теперь для какой-то никому не нужной выставки!"
    mt "Моника, да что с тобой не так?!"
    mt "!!!"
    mt "И долго мне тут стоять?!"
    mt "Где носит этого фотографа-неудачника?!"
    mt "!!!"
    # в студии появляется голый Райен, Моника в шоке смотрит на него, а он ведет себя, как ни в чем не бывало
    m "!!!"
    m "!!!!"
    ryan "Шикарный вид, Миссис Бакфетт!"
    ryan "Я не ошибся, выбрав моделью именно вас!"
    ryan "Ну что, вы готовы?"
    m "К че... К чему?.."
    m "Какого черта ты без одежды?!"
    m "Ты что, думаешь что я!.."
    # он спокойно ее перебивает
    ryan "О, нет-нет! Ничего подобного, Миссис Бакфетт!"
    ryan "Просто я предпочитаю делать шедевры обнаженным."
    ryan "Так у меня получаются наиболее крутые работы."
    mt "И я еще думала, что Алекс извращенец?!"
    mt "!!!"
    ryan "Начнем, Миссис Бакфетт!"

    #кадр
    img 24529
    #up
    img 24530
    #side
    img 24531
    #down
    img 24532
    # 1-й кадр (Z MC 06 Genesis 3 Female)
    ryan "Миссис Бакфетт, первый кадр."
    ryan "Поставьте одну ногу на стул и откиньте назад голову."
    # Моника вредничает
    m "Чтобы получше было видно мою грудь?!"
    mt "Извращенец!"
    mt "!!!"
    ryan "Миссис Бакфетт, никто не будет знать, что это ваша грудь."
    ryan "На вас маска, не переживайте."
    # Моника принимает позу, Райен делает кадры
    ryan "Потрясающе!"
    ryan "Этот приглушенный свет создает такую интимную атмосферу..."
    ryan "И так выгодно подчеркивает вашу женственность!"

    #кадр
    img 24533
    #up
    img 24534
    #side
    img 24535
    #down
    img 24536
    # 2-й кадр (Z MC 02 Genesis 3 Female)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Встаньте на стул на колени и держитесь руками за спинку."
    # Моника недовольно смотрит на его причиндалы
    mt "Я что, должна всю фотосессию смотреть, как он носится тут со своим торчащим отростком?!"
    mt "Хоть бы прикрылся ради приличия, придурок!"
    mt "!!!"
    # Райен фоткает ее со стояком
    ryan "Шикарно, Миссис Бакфетт!"
    ryan "Великолепные кадры!"

    #кадр
    img 24537
    #up
    img 24538
    #side
    img 24539
    #down
    img 24540
    # 3-й кадр (Z MC 09 Genesis 3 Female Mirror)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Опустите одну ногу на пол."
    # Моника ворчит
    m "Райен, снимай так, чтобы мое лицо было в тени!"
    m "Я не хочу, чтобы кто-то узнал меня!"
    # Райен фоткает
    ryan "Конечно, Миссис Бакфетт!"
    ryan "Вашего лица практически не различить в полумраке."

    #кадр
    img 24541
    #up
    img 24542
    #side
    img 24543
    #down
    img 24544
    img 24545
    # 4-й кадр (Z MC 03 Genesis 3 Female)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Сядьте на стул, лицом к спинке стула. Ноги по сторонам от спинки и облокотитесь на нее."
    # Моника возмущенно
    m "Ты что, хочешь чтобы я еще и ноги раздвинула?!"
    m "Если ты не заметил, Райен, вообще-то, на мне нет трусиков!!!"
    ryan "Ну все равно же никто не узнает, что это вы, Миссис Бакфетт..."
    ryan "Тем более, я постараюсь не делать слишком откровенных ракурсов."
    ryan "Все-таки я делаю работу для выставки..."
    m "Постарайся, Райен!"
    m "И не вздумай пялиться на мою!.. На меня!"
    ryan "Конечно, Миссис Бакфетт..."
    # Райен фоткает и иногда, пока Моника не видит, немного подрачивает себе
    ryan "Шедеврально!"
    ryan "Моей выставке гарантирован успех!"
    ryan "Вы самая лучшая модель, с которой я когда-либо работал!"

    #кадр
    img 24546
    #up
    img 24547
    #side
    img 24548
    #down
    img 24549
    # 5-й кадр (Z MC 04 Genesis 3 Female)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Оставайтесь в этой же позе, но отклонитесь немного назад."
    # Моника ворчит про себя
    mt "А вдруг он мне наврал про выставку?.."
    mt "..."
    mt "Он тут бегает передо мной со своим торчащим отростком..."
    mt "Значит, ему нравится сам процесс съемки..."
    mt "Нет, он просто пялится на меня!"
    mt "И затеял все только ради того, чтобы поглазеть на мою совершенную красоту!"
    mt "Мерзкий извращенец, вот он кто!"
    # Райен фоткает и подрачивает
    ryan "Мммм..."
    ryan "Какие потрясающие кадры!.."
    ryan "Великолепно!"

    #кадр
    img 24550
    #up
    img 24551
    #side
    img 24552
    #down
    img 24553
    # 6-й кадр (Z MC 05 Genesis 3 Female Mirror)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Оставайтесь в этой же позе, только руки держите над головой."
    # грозно говорит Райену
    m "Райен! Не вздумай рассматривать меня!!!"
    m "Если я узнаю, что нет никакой выставки и ты меня обманул!.."
    # Райен торопливо
    ryan "Выставка - это не моя выдумка, Миссис Бакфетт."
    ryan "Хотите, я вас приглашу на нее, чтобы вы смогли в этом удостовериться?"
    m "Нет! У меня нет на это времени!"
    m "Тем более, не пристало такой популярной личности как Я, ходить по малоизвестным выставкам..."
    mt "Не хватало еще, чтобы кто-то подумал, что я причастна к этой пошлой извращенской коллекции!"
    # Райен фоткает
    ryan "Дааа..."
    ryan "То, что надо..."
    ryan "Прекрасно!"

    #кадр
    img 24554
    #up
    img 24555
    #side
    img 24556
    #down
    img 24557
    img 24558
    # 7-й кадр (Z MC 08 Genesis 3 Female)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Сядьте, облокотившись спиной на спинку стула и немного прогнитесь."
    # Райен фоткает
    ryan "Ооох, я в восторге от этой работы, Миссис Бакфетт!"
    m "По тебе заметно, Райен!" # недовольный взгляд Моники на его стояк
    ryan "Мммм... Да, я так вдохновлен!"
    m "Смотри, не переусердствуй с этим!"
    m "Не хватало мне еще наблюдать твой творческий экстаз!"
    m "!!!"

    #кадр
    img 24559
    #up
    img 24560
    #side
    img 24561
    img 24562
    #down
    img 24563
    img 24564
    # 8-й кадр (Z MC 11 Genesis 3 Female)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Сидите также, спиной к спинке стула, но одну ногу вытяните в сторону."
    m "Никаких крупных планов!"
    m "И не вздумай направлять объектив камеры вниз!"
    # Райен фоткает
    ryan "Конечно, Миссис Бакфетт..."
    ryan "Как скажете."
    ryan "О, дааа..."
    ryan "Такой интимный полумрак... И я в студии с такой прекрасной обнаженной женщиной..."
    m "Райен!"
    m "Прекрати намекать на всякие непристойности!"
    m "Вообще-то, перед тобой леди!"
    ryan "Конечно, Миссис Бакфетт..."
    ryan "Великолепные кадры!"

    #кадр
    img 24565
    #up
    img 24566
    img 24567
    #side
    img 24568
    img 24569
    #down
    img 24570
    img 24571
    img 24572
    # 9-й кадр (Z MC 10 Genesis 3 Female)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Ложитесь на стул, рукой держитесь за спинку и согните одну ногу."
    m "Райен, мне так неудобно!"
    m "Я сейчас упаду!"
    # Райен фоткает
    ryan "Я быстро сделаю несколько кадров и мы сменим позу."
    ryan "Вот так, да..."
    m "Райен, долго еще!?"
    m "У меня рука затекла!"
    ryan "Еще немного..."
    ryan "Отлично!"
    m "Наконец-то!"

    #кадр
    img 24573
    #up
    img 24574
    img 24575
    #side
    img 24576
    img 24577
    #down
    img 24578
    img 24579
    img 24580
    img 24581
    # 10-й кадр (Z MC 01 Genesis 3 Female)
    ryan "Следующий кадр, Миссис Бакфетт."
    ryan "Сядьте на стул, лицом к спинке стула. Ноги по сторонам от спинки. Облокотитесь одной рукой на спинку стула, а вторую держите у шляпы."
    m "Райен!!!"
    m "Не вздумай фотографировать меня с этого ракурса!"
    m "Так видно всю мою!.."
    ryan "Но лица ведь не видно, Миссис Бакфетт..."
    m "!!!"
    # коррапшн
    menu:
        "Продолжить фотосессию.":
            $ monicaRyanStudioPhotoshoot3 = day # Моника согласилась на откровенный кадр у Райена
            pass
        "Уйти отсюда!":
            # Моника зло
            m "Нет, Райен!"
            m "Вообще-то, я пришла сюда, чтобы воспрепятствовать публикации моих обнаженных фото..."
            m "А не делать настолько откровенные кадры!"
            m "Ты в своем уме?!"
            # Моника идет к выходу, Райен ей вслед
            ryan "Тогда я буду вынужден отказать вам в отборе снимков..."
            m "Мне плевать!"
            m "!!!"
            ryan "Миссис Бакефтт, я дам вам на раздумье несколько дней."
            ryan "Вы можете вернуться в любой момент."
            m "НЕТ!"
            # Моника уходит
            return
    # Моника возмущенно
    m "Ты говорил, что для выставки не нужны такие откровенные кадры!"
    ryan "Я постараюсь сделать его не откровенным, а пикантным, Миссис Бакфетт..."
    ryan "С налетом легкой эротики..."
    m "!!!"
    m "Постарайся, Райен!"
    # Моника принимает позу, Райен фоткает, бросая пошлые взгляды на Монику
    m "Не смотри ТУДА!"
    ryan "Я и не смотрю, Миссис Бакфетт..."
    ryan "Я подбираю наилучший ракурс."
    m "!!!"
    ryan "О, вы просто сногсшибательно смотритесь, Миссис Бакфетт!"
    m "Я всегда сногсшибательна, Райен! Если ты не заметил!"
    ryan "О, даа! Я заметил..."
    ryan "Еще пара кадров..."
    ryan "Еще немного... Вот так, да..."
    ryan "Мммм..."

    ryan "Мы закончили, Миссис Бакфетт!"
    # Моника с встает со стула и грозно приказывает Райену
    m "Теперь неси эти чертовы снимки для рекламы Кэмпбелла!"
    m "Я и так потратила кучу своего бесценного времени здесь!"
    m "!!!"
    ryan "Да, Миссис Бакфетт, конечно!"
    ryan "Я только хотел сказать, что это была потрясающая фотосессия..."
    ryan "И я был бы не против поработать с вами еще не один раз."
    m "С чего бы это?!"
    m "У меня и без твоих фотосессий все дни расписаны буквально по минутам!"
    ryan "Да, и я прекрасно это понимаю."
    ryan "Я не могу вам предложить большую сумму денег за фотосессии."
    ryan "К тому же, я предполагаю, что деньги вас не интересуют..."
    ryan "У вас и так все есть - влияние, деньги, слава..."
    m "..."
    ryan "Но вы ведь творческая личность, Миссис Бакфетт."
    ryan "Я вижу, что вам нравится принимать участие в съемках подобного рода..."
    ryan "Я мог бы вам платить чисто символичесвку сумму... Скажем, триста долларов за фотосессию."
    m "Райен, ты что, издеваешься сейчас надо мной?!"
    m "?!"
    ryan "Нет, Миссис Бакфетт, не издеваюсь, а предлагаю приятное сотрудничество."
    ryan "Просто имейте ввиду, что я буду всегда рад поработать с вами..."
    # Моника прерывает его жестом
    m "Все, Райен, хватит!"
    m "Неси мне снимки!!!"
    m "!!!"
    ryan "Да, Миссис Бакфетт."
    ryan "В качестве моей благодарности за такую великолепную фотосессию..."
    ryan "Я позволю вам отобрать нужные вам снимки."
    m "И оденься! Хватит тут трясти передо мной своим!.. Вот этим!"
    # Райен усмехается
    ryan "Я сейчас вернусь, Миссис Бакфетт..."
    # затемнение
    return

# если Моника отказалась от фотосессии у Райена, на следующий рабочий день, уходя из офиса вечером
# мысли
label ep22_5_dialogues4_rayan_4:
    ## не рендерить!!
    mt "Черт! Я так и не отобрала нужные мне снимки для рекламы Кэмпбелла!"
    mt "Этот никчемный фотограф Райен посмел мне ставить свои дурацкие условия!"
    mt "Мерзавец! Жалкий фотограф!"
    mt "!!!"
    return


# мысли, если сорвала съемку у Райена
label ep22_5_dialogues4_rayan_5:
    ## не рендерить!!
    mt "Пошел этот озабоченный фотограф-извращенец к черту!"
    mt "Я не собираюсь участвовать в этой его дурацкой фотосессии!"
    mt "!!!"
    return

# мысли, если закончила съемку у Райена и отсортировала снимки
label ep22_5_dialogues4_rayan_6:
    ## не рендерить!!
    mt "Наконец-то, я закрыла вопрос с этими гребаными снимками для рекламы Кэмпбелла!"
    mt "Но, Моника! Тебе сегодня пришлось позировать обнаженной..."
    mt "Для того, чтобы твои же откровенные снимки не попали к Бифу!"
    mt "!!!"
    mt "Этот никчемный Райен посмел ставить мне свои дурацкие условия!"
    mt "Еще и обнажился передо мною!"
    mt "А после этого, имел наглость предложить мне работать с ним за $ 300!!!"
    mt "Этот идиот серьезно думает, что Я соглашусь на это?!"
    mt "Позировать голой за триста долларов?!"
    mt "Да пошел он к черту вместе со своей дряной выставкой!"
    mt "Сволочь! Озабоченная бездарность!!!"
    return
