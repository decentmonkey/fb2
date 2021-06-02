default monicaRyanStudioPhotoshoot1 = 0 # Моника пошла в студию Райена
default monicaRyanStudioPhotoshoot2 = 0 # Моника согласилась сняться для коллекции Райена
default monicaRyanStudioPhotoshoot3 = 0 # Моника согласилась на откровенный кадр у Райена
default monicaRyanStudioPhotoshoot4 = 0 # Моника пошла в студию Райена повторно после отказа от съемки

default ep22_5_dialogues4_rayan_1_repeat = False
default ep22_5_dialogues4_rayan_2_repeat = False
default PS12_shoots_array = []
define monicaPhotoshootRyanStudioCorruptionRequired1 = 700 # Моника согласилась сняться для коллекции Райена
define monicaPhotoshootRyanStudioCorruptionRequired2 = 750 # Моника согласилась на откровенный кадр у Райена

#call ep22_5_dialogues4_rayan_1() # в офисе Моники перед поездкой в студию Райена
#call ep22_5_dialogues4_rayan_3() # студия Райена
#call ep22_5_dialogues4_rayan_4() # мысли, если Моника отказалась от фотосессии у Райена, на следующий рабочий день
#call ep22_5_dialogues4_rayan_5() # мысли, если сорвала съемку у Райена, после того, как вышла от него
#call ep22_5_dialogues4_rayan_6() # мысли, если закончила съемку у Райена и отсортировала снимки

# при условии, что было свидание с Мэйсоном в ресторане
# при клике на стол в рабочем кабинете Моники
label ep22_5_dialogues4_rayan_1:
    music Groove2_85
    imgf 40291
    w
    if ep22_5_dialogues4_rayan_1_repeat == True:
        menu:
            "Пойти в студию Райена.":
                $ monicaRyanStudioPhotoshoot4 = day # Моника пошла в студию Райена повторно после отказа от съемки
                pass
            "Не сегодня.":
                music Stealth_Groover
                imgd 20362
                mt "Я обязательно схожу... Позже..."
                mt "Этот жалкий фотограф никуда не денется."
                mt "А у меня есть более важные дела сегодня."
                return False
#    if ep22_5_dialogues4_rayan_1_repeat == False:
        imgd 40291
        mt "Если я не договорюсь с никчемным фотографом Райеном - он отправит мои откровенные снимки Бифу."
        mt "А этот придурок с радостью пустит их в печать!"
        mt "Мне нельзя допустить этого!"
        mt "!!!"
        mt "Возможно, стоит пойти в студию к этому Райену?.."
        mt "Он обещал, что на кадрах для его коллекции не будет видно моего лица... И что я буду в маске..."
        mt "..."
        # вечером переход на фотосессию в студии Райена
        return


    # Моника сидит в кресле за своим рабочим столом с задумчивым видом
    music Groove2_85
    imgd 21989
    mt "Свидание с этим никчемным Мэйсоном прошло по плану..."
    # если работает в эскорте и был шантаж от Дэниела
    if monica_escort_service_started == True:
        mt "За исключением некоторых моментов, о которых я даже думать не хочу."
        #
    music Stealth_Groover
    imgf 20269
    mt "Теперь он у меня на крючке."
    mt "Иначе и быть не могло!"
    mt "Перед такой шикарной женщиной, как Я, не устоит ни один мужчина!"
    mt "!!!"
    mt "Насчет того, как дальше использовать Мэйсона..."
    mt "Я подумаю немного позже."
    music Groove2_85
    imgd 40291
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
    if monicaJuliaLoveStory7 == True:
        #
        $ notif(_("Моника состоит в отношениях с Юлией."))
        #
        imgf 30586
        m "Юлия, милая..."
        # Юлия игриво улыбается ей
        julia "Да, Миссис Бакфетт?"
        julia "Вы по мне соскучились и хотите поцеловать меня?"
        # Моника закатывает глаза
        img 44837
        mt "!!!"
        # потом притворяясь, улыбается ей
        music Hidden_Agenda
        sound2 highheels_run2
        imgd 40265
        m "Да, милая! Очень хочу!"
        # Юлия подходит к ней и чмокает в губы
        sound highheels_short_walk
        imgf 40268
        julia "Мммм..."
        music Loved_Up
        imgd 40272
        julia "Я тоже соскучилась, Миссис Бакфетт..."
        imgf 40274
        sound snd_kiss2
        w
        music Groove2_85
        imgd 40270
        m "Милая... Я хотела тебя кое о чем попросить..."
        m "У меня назначена важная рабочая встреча с фотографом Райеном."
        m "Найди его номер телефона, предупреди о моем визите и узнай адрес его студии."
        imgf 30628
        julia "Хорошо, Миссис Бакфетт."
        julia "Еще один поцелуй и будет сделано."
        # снова чмокает ее в губы
        imgd 40274
        sound snd_kiss2
        w
        imgf 40275
        sound highheels_short_walk
        julia "Обожаю вас, Миссис Бакфетт!"
        m "И я тебя, милая..."
        m "Позвони, пожалуйста, Райену. Это действительно важная встреча..."
        julia "Да-да, я сейчас все сделаю."
        # Юлия выходит из кабинета, игриво оглядываясь на Монику и подмигивая ей
        #
    # если нет отношений
    else:
        imgf 20887
        m "Юлия! Подойди сюда! Быстро!"
        # Юлия испуганно подбегает
        sound highheels_run2
        imgd 20888
        julia "Да, Миссис Бакфетт?"
        m "У меня важная рабочая встреча с фотографом Райеном."
        m "Найди его номер телефона, предупреди о моем визите и узнай адрес его студии."
        imgd 20889
        julia "Хорошо, Миссис Бакфетт."
        m "И поторопись! Это очень важно!"
        julia "Да-да, я сейчас все сделаю."
        # Юлия убегает из кабинета
        #
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Stealth_Groover
    imgfl 20251
    mt "Никчемная помощница!"
    mt "Такая же никчемная, как и все остальные работнички!"
    mt "Бесполезные муравьишки!"
    mt "!!!"
    #    return
    sound highheels_short_walk
    imgf 20272
    mt "Мне нужно как можно скорее забрать снимки у никчемного фотографа Райена."
    mt "Если я этого не сделаю - он отправит их Бифу."
    mt "Мне нельзя допустить этого!"
    mt "!!!"
    imgd 20274
    mt "Я уверена, что это не займет много времени."
    mt "Этот фотограф готов сделать все так, как скажу Я."
    mt "Ведь Я - глава журнала, а он - всего лишь какой-то жалкий фотограф..."
    mt "Да, Моника, нужно закрыть вопрос с этими гребаными снимками! Сегодня же!"
    mt "!!!"
    $ ep22_5_dialogues4_rayan_1_repeat = True
    return


label ep22_5_dialogues4_rayan_1a:
    menu:
        "Пойти в студию Райена.":
            $ monicaRyanStudioPhotoshoot1 = day # Моника пошла в студию Райена
            pass
        "Не сегодня.":
#            music Stealth_Groover
#            imgd 21989
            mt "Я обязательно схожу... Позже..."
            mt "Этот жалкий фотограф в любом случае не посмеет ослушаться меня..."
            mt "И будет ждать моего визита."
            mt "Никуда он не денется."
            mt "А у меня есть более важные дела сегодня."
            return False
    return True

label ep22_5_dialogues4_rayan_1b:
    mt "Мне нужно как можно скорее забрать снимки у никчемного фотографа Райена."
    mt "Если я этого не сделаю - он отправит их Бифу."
    mt "Мне нельзя допустить этого!"
    return

label ep22_5_dialogues4_rayan_1c:
    mt "Мне нечего здесь делать сейчас..."
    return False

# апартаменты Райена
label ep22_5_dialogues4_rayan_3:
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(_("СТУДИЯ РАЙАНА...")) from _rcall_textonblack_97
    scene black_screen
    with Dissolve(1)
    sound snd_lift
    pause 2.0
    sound highheels_short_walk
    pause 1.5
    if ep22_5_dialogues4_rayan_2_repeat == False:
        music Groove2_85
        # звук лифта
        # Моника заходит в его апартаменты
        imgfl 44807
        mt "Это что, его апартаменты?!"
        mt "Какого черта?!"
        mt "Я у этой никчемной помощницы просила узнать адрес студии, а не апартаментов!"
        mt "Юлия - идиотка!"
        mt "Ни на что не способная бывшая гувернантка!"
        mt "!!!"
        # Райен выходит навстречу Монике
        sound man_steps
        imgf 44808
        ryan "Миссис Бакфетт, добрый вечер!"
        # целует ей руку, как обычно
        imgd 44809
        ryan "Я несказанно рад вашему визиту!"
        imgd 44810
        sound snd_kiss2
        ryan "Это честь для меня, принимать такого статусного гостя в моей скромной студии!"
        # Моника с надменным видом
        imgf 44811
        m "Это твоя студия, Райен?"
        m "Я решила, что это твой дом..."
        # Райен улыбается
        imgd 44812
        ryan "Все верно, Миссис Бакфетт."
        ryan "Моя студия находится в моих апартаментах."
        ryan "Я здесь и живу, и занимаюсь творчеством."
        # приглашает ее жестом войти
        sound Jump1
        imgd 44813
        ryan "Проходите, Миссис Бакфетт."
        ryan "Чай, кофе? Может, чего-то покрепче?"
        # Моника высокомерно
        music Stealth_Groover
        imgf 44814
        m "Нет, спасибо, Райен."
        m "Ничего не нужно. Давай сразу перейдем к делу..."
        m "У меня мало времени. Ты же понимаешь, что я очень занятая леди."
        imgd 44815
        ryan "Да, конечно, Миссис Бакфетт..."
        # затемнение, каблуки
        # они проходят в студию
        # Моника осматривается со снобским выражением на лице
        fadeblack
        sound highheels_short_walk
        pause 2.0
        music Stealth_Groover
        imgfl 44749
        w
        imgf 44750
        w
        imgd 44751
        mt "Что это еще такое?"
        mt "Это разве студия?!"
        imgd 44752
        mt "Какая-то непонятная каморка! Фи!"
        mt "Как будто в каком-то подвале!"
        mt "Другое дело - студия в офисе моего журнала!"
        # Райен подходит к ней и загадочно улыбается
        music Groove2_85
        imgf 44753
        ryan "Миссис Бакфетт..."
        ryan "Не обращайте внимания, у меня тут всегда небольшой творческий беспорядок."
        sound vjuh3
        imgd 44754
        ryan "Можете присесть вот на этот стул..."
        # указывает рукой на реквизит для фотосъемки, стул стоит посреди полотна
        imgf 44755
        sound highheels_short_walk
        m "..."
        # Моника с важным видом садится на него
        imgd 44756
        w
        fadeblack 1.5
        music Groove2_85
        imgf 44757
        m "Райен, я хотела бы посмотреть снимки с рамой Кэмпбелла..."
        m "У меня нет времени на светскую болтовню."
        # Райен чешет затылок
        imgd 44758
        ryan "Кхм..."
        ryan "Понимаете, в чем дело, Миссис Бакфетт..."
        ryan "Я... Я сначала хотел бы рассказать вам о своем проекте."
        music Stealth_Groover
        imgd 44759
        mt "Этот придурок думает, что меня это должно интересовать?!"
        mt "Какое мне дело до его жалких делишек?!"
        mt "Но, видимо, мне придется сделать заинтересованный вид..."
        mt "Чтобы добраться, наконец, до этих чертовых снимков!"
        # делает притворно-заинтересованное лицо
        music Hidden_Agenda
        imgd 44760
        m "У тебя есть свой проект?"
        m "Как интересно, Райен..."
        # Райен улыбается
        music Groove2_85
        imgf 44761
        ryan "Да, Миссис Бакфетт."
        ryan "Я являюсь большим ценителем женской красоты."
        ryan "И стараюсь отразить эту свою страсть в своих работах."
        ryan "У меня есть уже целая коллекция работ, посвященных изяществу женского тела."
        imgd 44762
        ryan "И для завершения моей коллекции мне не хватает лишь одной..."
        ryan "Которая станет вишенкой на торте, так сказать."
        imgd 44763
        w
        img 44764
        m "..."
        imgf 44765
        ryan "Совсем скоро у меня будет выставка..."
        ryan "Она будет проходить не только в нашем городе, но и по всей стране."
        ryan "Мои работы увидит весь мир, Миссис Бакфетт!"
        imgd 44766
        mt "А я тут при чем?!"
        mt "Зачем мне вся эта лишняя информация?!"
        mt "!!!"
        # Райен пристально на нее смотрит и улыбается
        imgd 44767
        ryan "Вы, наверное, не понимаете, зачем я все это вам рассказываю?"
        m "..."
        m "Зачем же?.."
        ryan "Вишенка на торте - это фотосессия с вашим участием, Миссис Бакфетт..."
        music stop
        sound plastinka1b
        img 44768 hpunch
        m "С моим?!"
        m "?!"
        music Groove2_85
        imgd 44769
        ryan "Да, Миссис Бакфетт."
        ryan "Кто, как не глава журнала о моде..."
        ryan "Которая не только поддерживает новый курс своего журнала, снимаясь в пикантных фотосессиях..."
        ryan "Но также является самой красивой женщиной... И смелой... И притягательной..."
        # Моника смотрит на него, подозрительноп прищурившись
        imgd 44770
        mt "Бред какой-то!"
        mt "С какой стати я должна сниматься для его дурацкой выставки?!"
        mt "Он что, думает, я получаю удовольствие от этих пошлых фотосессий?!"
        mt "Такой же фотограф-извращенец, как и Алекс!"
        mt "!!!"
        # Моника принимает высокомерный вид
        music Stealth_Groover
        imgf 44771
        m "Райен..."
        m "Назови мне хотя бы одну причину..."
        m "Из-за которой Я, Моника Бакфетт, глава известного журнала..."
        m "Владелица многомиллионного бизнеса..."
        m "И весьма занятая бизнес-леди..."
        m "Должна дать согласие на съемку перед объективом твоей камеры."
        # насмешливо приподнимает уголок губ в улыбке
        imgd 44772
        ryan "Причина есть."
        ryan "Снимки с фотосессии в офисе Мистера Кэмпбелла..."
        # Моника встакивает со стула
        music Pyro_Flow
        sound2 Jump2
        img 44773 vpunch
        m "Что?!"
        m "Мы с тобой не так договаривались, Райен!!!"
        m "Ты мне сказал, что..."
        imgd 44774
        ryan "Что буду рад вашему визиту в свою студию."
        ryan "И, поверьте, это действительно так, Миссис Бакфетт."
        img 44775 hpunch
        m "Хватит заговаривать мне зубы!"
        m "Меня интересуют только снимки! Никаких фотосессий!!!"
        m "!!!"
        # Райен абсолютно спокоен
        music Groove2_85
        imgf 44776
        ryan "Вам совсем необязательно давать согласие именно сейчас, Миссис Бакфетт."
        ryan "Я задержу снимки у себя еще на несколько дней и пока не буду посылать их в ваш журнал."
        ryan "Но только на несколько дней, не больше."
        ryan "Потом я буду вынужден их отправить, так как не смею нарушать приказ Мистера Кэмпбелла."
        ryan "Все-таки он очень важный клиент, сами понимаете..."
        music Power_Bots_Loop
        img 44777 hpunch
        m "Для тебя, Райен, нет более важного клиента, чем Я!"
        m "!!!"
        music Groove2_85
        imgd 44778
        ryan "Миссис Бакфетт, вы - модель."
        ryan "Приглашенная модель для фотосессии, за которую Мистер Кэмпбелл весьма щедро заплатил мне."
        ryan "Так что, повторюсь, его приказ я не могу нарушить."
        ryan "Но я могу послать не все снимки, Миссис Бакфетт..."
        ryan "А только те, которые отберете вы лично."
        ryan "После того, как сниметесь в фотосессии для моей коллекции..."
        imgf 44779
        m "Это твое условие, Райен?"
        ryan "Да, Миссис Бакфетт."
        imgd 44780
        mt "Черт!!!"
        menu:
            "Согласиться.":
                pass
            "Вот еще! Пошел он к черту!":
                # Моника надменно
                music Stealth_Groover
                imgd 44781
                mt "Этот никчемный жалкий фотограф решил ставить мне свои условия?!"
                mt "МНЕ?! Монике Бакфетт?!"
                mt "!!!"
                imgf 44782
                m "Я не собираюсь принимать участие ни в каких сомнительных фотосессиях!"
                ryan "Тогда я буду вынужден отказать вам в отборе снимков..."
                m "!!!"
                imgd 44783
                ryan "Притом, это не какая-нибудь сомнительная фотосессия, Миссис Бакфетт."
                ryan "Эта коллекция вполне соответствует новому курсу вашего журнала."
                img 44784
                m "И что это значит?"
                pass
        # Моника смотрит на него подозрительно
        music Groove2_85
        imgf 44785
        m "Как именно будет проходить эта фотосессия?"
        # Райен рукой указывает на стул, на котором сидела Моника
        ryan "Здесь, в моей студии, Миссис Бакфетт."
        sound Jump1
        imgd 44786
        ryan "Реквизит, как видите, я уже подготовил."
        m "Фотосессия со стулом?"
        imgd 44787
        ryan "Да, Миссис Бакфетт."
        ryan "Это будут потрясающие кадры!"
        ryan "Изящные очертания прекрасного обнаженного женского тела в приглушенном свете софитов..."
        music stop
        sound plastinka1b
        img 44788 hpunch
        m "Стоп!"
        music Power_Bots_Loop
        m "Обнаженного?!"
        m "Ты что, с ума сошел?!"
        m "Я не собираюсь раздеваться!.."
        $ ep22_5_dialogues4_rayan_2_repeat = True

    ### если приходит повторно после того, как отказала - repeat отсюда
    music Groove2_85
    imgf 44789
    ryan "На вас, Миссис Бакфетт, будет маска. Вашего лица никто не узнает."
    ryan "Тем более, фотосессия будет проходить в полумраке..."
    ryan "И сразу же по окончанию нашей съемки, я покажу вам снимки с фотосессии Кэмпбелла."
    imgd 44790
    m "..."
    # коррапшн
    $ menu_corruption = [monicaPhotoshootRyanStudioCorruptionRequired1, 0]
    menu:
        "Согласиться на фотосессию.":
            $ monicaRyanStudioPhotoshoot2 = day # Моника согласилась сняться для коллекции Райена
            pass
        "Нет!":
            # Моника надменно
            music Pyro_Flow
            imgd 44791
            mt "Нет! Я не собираюсь обнажаться для его никчемной выставки!"
            mt "Пошел он к черту со своими условиями!"
            mt "Очередной шантажист-извращенец!!!"
            mt "!!!"
            # Моника зло
            imgf 44793
            m "Нет, Райен!"
            m "Я не собираюсь раздеваться перед объективом твоей камеры!"
            m "Я пришла сюда, чтобы воспрепятствовать публикации моих обнаженных фото..."
            m "А ты ставишь мне условие, при котором я должна снова сниматься обнаженной!"
            m "Чтобы потом демонстрировать эту работу на весь мир!"
            m "Ты в своем уме?!"
            # Моника идет к выходу, Райен ей вслед
            imgd 44794
            ryan "Тогда я буду вынужден отказать вам в отборе снимков..."
            img 44795
            m "Мне плевать!"
            m "!!!"
            imgd 44796
            ryan "Миссис Бакефтт, я дам вам на раздумье несколько дней."
            ryan "Вы можете вернуться в любой момент."
            imgf 44797
            sound highheels_short_walk
            m "НЕТ!"
            # Моника уходит
            fadeblack
            sound highheels_short_walk
            pause 2.0
            return False
    # Моника недовольно смотрит на него
    music Pyro_Flow
    imgd 44791
    mt "Чертов фотограф-извращенец!"
    mt "Он ставит мне условие, при котором я должна снова сниматься обнаженной!"
    mt "Чтобы потом демонстрировать эту работу на весь мир!"
    mt "!!!"
    imgd 44792
    mt "С другой стороны, если моего лица и правда не будет видно."
    mt "Он говорил про полумрак и маску..."
    mt "..."
    mt "Зато я смогу сделать так, чтобы Биф не опубликовал откровенные кадры с фотосессии у Кэмпбелла."
    mt "А этот гребаный фотограф говорил, что там много таких снимков!"
    mt "Дьявол!"
    mt "!!!"
    # она решительно смотрит на Райена
    music Groove2_85
    imgf 44798
    m "Моего лица точно не будет видно?!"
    ryan "Вы сами себя не сможете узнать на этих снимках, Миссис Бакфетт."
    ryan "Я вам обещаю это!"
    imgd 44799
    ryan "Я хочу использовать только красоту вашего тела."
    ryan "А не вашу популярность как медийной личности..."
    # смотрит на него угрожающе
    img 44800
    m "Уверен?!"
    m "!!!"
    imgd 44801
    ryan "Абсолютно!"
    # грозно тычет в него пальцем
    music Power_Bots_Loop
    sound2 Jump2
    img 44802 hpunch
    m "Райен!"
    m "Если хоть одна живая душа узнает о том, что я как-то причастна к этой твоей выставке!.."
    m "Что я была у тебя в студии и снималась для твоей коллекции!.."
    m "Я тебя предупреждаю!.."
    # Райен торопливо
    music Groove2_85
    img 44803
    ryan "Никто не узнает, Миссис Бакфетт."
    ryan "Это останется только между нами."
    ryan "Это даже хорошо, что никто не будет знать, кто является моей моделью..."
    imgd 44804
    ryan "Эта загадочность добавит изюминку в нашу с вами совместную работу." # подмигивает
    sound Jump1
    img 44805
    w
    # Моника снова принимает надменный вид
    imgd 44806
    m "Давай мне эту чертову маску!"
    m "У меня мало времени, так что - за дело!"
    # затемнение
    # спустя некоторое время Моника стоит в аутфите для съемки, свет выключается
    # Райена нигде не видно
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Stealth_Groover
    imgfl 44816
    mt "Поверить не могу!"
    mt "Пришла забрать свои обнаженные снимки..."
    mt "А теперь стою голая, чтобы снова сняться!.."
    mt "Теперь для какой-то никому не нужной выставки!"
    mt "Моника, да что с тобой не так?!"
    imgf 44817
    mt "!!!"
    mt "И долго мне тут стоять?!"
    mt "Где носит этого фотографа-неудачника?!"
    mt "!!!"
    # в студии появляется голый Райен, Моника в шоке смотрит на него, а он ведет себя, как ни в чем не бывало
    fadeblack
    sound man_steps
    pause 2.0
    sound plastinka1b
    img 44818 vpunch
    m "!!!"
    img 44819
    m "!!!!"
    music Groove2_85
    imgf 44820
    ryan "Шикарный вид, Миссис Бакфетт!"
    ryan "Я не ошибся, выбрав моделью именно вас!"
    ryan "Ну что, вы готовы?"
    music Power_Bots_Loop
    img 44821 hpunch
    m "К че... К чему?.."
    m "Какого черта ты без одежды?!"
    m "Ты что, думаешь что я!.."
    # он спокойно ее перебивает
    music Groove2_85
    imgd 44822
    ryan "О, нет-нет! Ничего подобного, Миссис Бакфетт!"
    ryan "Просто я предпочитаю делать шедевры обнаженным."
    ryan "Так у меня получаются наиболее крутые работы."
    imgd 44823
    mt "И я еще думала, что Алекс извращенец?!"
    mt "!!!"
    imgd 44824
    ryan "Начнем, Миссис Бакфетт!"
    music Stealth_Groover
    $ shotsAmount = 30
    $ shotsTotalAmount = 30
    $ shots = 3
    $ arrowUp = True
    $ arrowSide = True
    $ arrowDown = True

    fadeblack 2.0
    imgfl 24529
    ryan "Миссис Бакфетт, первый кадр."
    ryan "Поставьте одну ногу на стул и откиньте назад голову."
label ep22_5_dialogues4_rayan_3_photoshoot_pose1:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose1"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose2"
    #кадр
    img 24529
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgfl 24533
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Встаньте на стул на колени и держитесь руками за спинку."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24530, 24531, 24532], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel

    if result == "up":
        #up
        sound camera_lens1
        $ photoImage = 24530
        img 24530
        with Dissolve(0.2)
        w
        m "Чтобы получше было видно мою грудь?!"
        mt "Извращенец!"
        mt "!!!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_99
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24531
        img 24531
        with Dissolve(0.2)
        w
        ryan "Миссис Бакфетт, никто не будет знать, что это ваша грудь."
        ryan "На вас маска, не переживайте."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_100
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24532
        img 24532
        with Dissolve(0.2)
        w
        ryan "Потрясающе!"
        ryan "Этот приглушенный свет создает такую интимную атмосферу..."
        ryan "И так выгодно подчеркивает вашу женственность!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_101
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    # 1-й кадр (Z MC 06 Genesis 3 Female)
    # Моника вредничает
    # Моника принимает позу, Райен делает кадры

label ep22_5_dialogues4_rayan_3_photoshoot_pose2:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose2"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose3"

    #кадр
    img 24533
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgfl 24537
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Опустите одну ногу на пол."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24534, 24535, 24536], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel

    if result == "up":
        #up
        sound camera_lens1
        $ photoImage = 24534
        img 24534
        with Dissolve(0.2)
        w
        mt "Я что, должна всю фотосессию смотреть, как он носится тут со своим торчащим отростком?!"
        mt "Хоть бы прикрылся ради приличия, придурок!"
        mt "!!!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_102
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24535
        img 24535
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_103
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24536
        img 24536
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_104
        w
        ryan "Шикарно, Миссис Бакфетт!"
        ryan "Великолепные кадры!"
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    # 2-й кадр (Z MC 02 Genesis 3 Female)
    # Моника недовольно смотрит на его причиндалы
    # Райен фоткает ее со стояком


label ep22_5_dialogues4_rayan_3_photoshoot_pose3:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose3"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose4"
    #кадр
    img 24537
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgfl 24541
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Сядьте на стул, лицом к спинке стула. Ноги по сторонам от спинки и облокотитесь на нее."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24538, 24539, 24540], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel

    if result == "up":
        #up
        sound camera_lens1
        $ photoImage = 24538
        img 24538
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_105
        w
        m "Райен, снимай так, чтобы мое лицо было в тени!"
        m "Я не хочу, чтобы кто-то узнал меня!"
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24539
        img 24539
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_106
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24540
        img 24540
        with Dissolve(0.2)
        w
        ryan "Конечно, Миссис Бакфетт!"
        ryan "Вашего лица практически не различить в полумраке."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_107
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    # 3-й кадр (Z MC 09 Genesis 3 Female Mirror)
    # Моника ворчит
    # Райен фоткает

label ep22_5_dialogues4_rayan_3_photoshoot_pose4:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose4"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose5"
    #кадр
    img 24541
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        music Loved_Up
        imgf 36003
        ryan "Шедеврально!"
        sound drkanje5
        imgd 36004
        sound2 camera_lens1
        w
        sound drkanje5
        imgd 36003
        ryan "Моей выставке гарантирован успех!"
        sound drkanje5
        imgd 36004
        sound2 camera_lens1
        ryan "Вы самая лучшая модель, с которой я когда-либо работал!"
        fadeblack 1.5

        imgfl 24546
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Оставайтесь в этой же позе, но отклонитесь немного назад."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24542, 24543, 24545], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel

    if result == "up":
        #up
        sound camera_lens1
        $ photoImage = 24542
        img 24542
        with Dissolve(0.2)
        w
        m "Ты что, хочешь чтобы я еще и ноги раздвинула?!"
        m "Если ты не заметил, Райен, вообще-то, на мне нет трусиков!!!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_108
        w
        ryan "Ну все равно же никто не узнает, что это вы, Миссис Бакфетт..."
        ryan "Тем более, я постараюсь не делать слишком откровенных ракурсов."
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24543
        img 24543
        with Dissolve(0.2)
        w
        ryan "Все-таки я делаю работу для выставки..."
        m "Постарайся, Райен!"
        m "И не вздумай пялиться на мою!.. На меня!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_109
        w
        ryan "Конечно, Миссис Бакфетт..."
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 24544
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_44
        w
        sound camera_lens1
        $ photoImage = 24545
        img 24545
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_110
        w
        # 4-й кадр (Z MC 03 Genesis 3 Female)
        # Моника возмущенно
        # Райен фоткает и иногда, пока Моника не видит, немного подрачивает себе

        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel

label ep22_5_dialogues4_rayan_3_photoshoot_pose5:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose5"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose6"
    #кадр
    img 24546
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        # Райен фоткает и подрачивает
        music Loved_Up
        imgf 36005
        ryan "Мммм..."
        sound drkanje5
        imgd 36006
        sound2 camera_lens1
        w
        sound drkanje5
        imgd 36005
        w
        sound drkanje5
        imgd 36006
        sound2 camera_lens1
        ryan "Какие потрясающие кадры!.."
        ryan "Великолепно!"
        fadeblack 1.5

        imgfl 24550
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Оставайтесь в этой же позе, только руки держите над головой."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24547, 24548, 24549], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel


    if result == "up":
        #up
        sound camera_lens1
        $ photoImage = 24547
        img 24547
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_111
        w
        mt "А вдруг он мне наврал про выставку?.."
        mt "..."
        mt "Он тут бегает передо мной со своим торчащим отростком..."
        mt "Значит, ему нравится сам процесс съемки..."
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24548
        img 24548
        with Dissolve(0.2)
        w
        mt "Нет, он просто пялится на меня!"
        mt "И затеял все только ради того, чтобы поглазеть на мою совершенную красоту!"
        mt "Мерзкий извращенец, вот он кто!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_112
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24549
        img 24549
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_113
        w
        # 5-й кадр (Z MC 04 Genesis 3 Female)
        # Моника ворчит про себя

        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel

label ep22_5_dialogues4_rayan_3_photoshoot_pose6:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose6"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose7"
    #кадр
    img 24550
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgfl 24554
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Сядьте, облокотившись спиной на спинку стула и немного прогнитесь."
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24551, 24552, 24553], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel

    if result == "up":
        #up
        sound camera_lens1
        $ photoImage = 24551
        img 24551
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_114
        w
        m "Райен! Не вздумай рассматривать меня!!!"
        m "Если я узнаю, что нет никакой выставки и ты меня обманул!.."
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24552
        img 24552
        with Dissolve(0.2)
        w
        ryan "Выставка - это не моя выдумка, Миссис Бакфетт."
        ryan "Хотите, я вас приглашу на нее, чтобы вы смогли в этом удостовериться?"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_115
        w
        m "Нет! У меня нет на это времени!"
        m "Тем более, не пристало такой популярной личности как Я, ходить по малоизвестным выставкам..."
        mt "Не хватало еще, чтобы кто-то подумал, что я причастна к этой пошлой извращенской коллекции!"
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        $ photoImage = 24553
        img 24553
        with Dissolve(0.2)
        w
        ryan "Дааа..."
        ryan "То, что надо..."
        ryan "Прекрасно!"
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_116
        w
        # 6-й кадр (Z MC 05 Genesis 3 Female Mirror)
        # грозно говорит Райену
        # Райен торопливо
        # Райен фоткает
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel


label ep22_5_dialogues4_rayan_3_photoshoot_pose7:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose7"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose8"
    #кадр
    img 24554
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgfl 24559
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Сидите также, спиной к спинке стула, но одну ногу вытяните в сторону."
        m "Никаких крупных планов!"
        m "И не вздумай направлять объектив камеры вниз!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24555, 24556, 24558], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel

    if result == "up":
        #up
        sound camera_lens1
        $ photoImage = 24555
        img 24555
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_117
        w
        ryan "Ооох, я в восторге от этой работы, Миссис Бакфетт!"
        m "По тебе заметно, Райен!" # недовольный взгляд Моники на его стояк
        ryan "Мммм... Да, я так вдохновлен!"
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        $ photoImage = 24556
        img 24556
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_118
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 24557
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_45
        w
        sound camera_lens1
        $ photoImage = 24558
        img 24558
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_119
        w
        # 7-й кадр (Z MC 08 Genesis 3 Female)
        # Райен фоткает
        imgd 36007
        m "Смотри, не переусердствуй с этим!"
        m "Не хватало мне еще наблюдать твой творческий экстаз!"
        m "!!!"
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel

label ep22_5_dialogues4_rayan_3_photoshoot_pose8:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose8"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose9"
    #кадр
    img 24559
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgfl 24565
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Ложитесь на стул, рукой держитесь за спинку и согните одну ногу."
        m "Райен, мне так неудобно!"
        m "Я сейчас упаду!"
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24560, 24561, 24564], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel

    if result == "up":
        #up
        sound camera_lens1
        $ photoImage = 24560
        img 24560
        with Dissolve(0.2)
        w
        ryan "Конечно, Миссис Бакфетт..."
        ryan "Как скажете."
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_120
        w
        ryan "О, дааа..."
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 24561
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_46
        w
        ryan "Такой интимный полумрак... И я в студии с такой прекрасной обнаженной женщиной..."
        m "Райен!"
        m "Прекрати намекать на всякие непристойности!"
        m "Вообще-то, перед тобой леди!"
        sound camera_lens1
        $ photoImage = 24562
        img 24562
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_121
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 24563
        with Dissolve(0.2)
        w
        ryan "Конечно, Миссис Бакфетт..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_47
        w
        sound camera_lens1
        $ photoImage = 24564
        img 24564
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_122
        w
        ryan "Великолепные кадры!"
        # 8-й кадр (Z MC 11 Genesis 3 Female)
        # Райен фоткает
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel

label ep22_5_dialogues4_rayan_3_photoshoot_pose9:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose9"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose10"

    #кадр
    img 24565
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        imgf 36008
        ryan "Следующий кадр, Миссис Бакфетт."
        ryan "Сядьте на стул, лицом к спинке стула. Ноги по сторонам от спинки. Облокотитесь одной рукой на спинку стула, а вторую держите у шляпы."
        m "Райен!!!"
        music Groove2_85
        imgd 36009
        m "Не вздумай фотографировать меня с этого ракурса!"
        m "Так видно всю мою!.."
        ryan "Но лица ведь не видно, Миссис Бакфетт..."
        m "!!!"
        # коррапшн
        $ menu_corruption = [monicaPhotoshootRyanStudioCorruptionRequired2, 0]
        menu:
            "Продолжить фотосессию.":
                $ monicaRyanStudioPhotoshoot3 = day # Моника согласилась на откровенный кадр у Райена
                pass
            "Уйти отсюда!":
                # Моника зло
                music Pyro_Flow
                img 36010 hpunch
                m "Нет, Райен!"
                m "Вообще-то, я пришла сюда, чтобы воспрепятствовать публикации моих обнаженных фото..."
                m "А не делать настолько откровенные кадры!"
                m "Ты в своем уме?!"
                # Моника идет к выходу, Райен ей вслед
                sound highheels_short_walk
                imgf 36011
                ryan "Тогда я буду вынужден отказать вам в отборе снимков..."
                m "Мне плевать!"
                m "!!!"
                ryan "Миссис Бакефтт, я дам вам на раздумье несколько дней."
                ryan "Вы можете вернуться в любой момент."
                m "НЕТ!"
                # Моника уходит
                fadeblack
                sound snd_fabric1
                pause 2.0
                sound highheels_short_walk
                pause 1.5
                return False
        # Моника возмущенно
        music Stealth_Groover
        imgf 24573
        m "Ты говорил, что для выставки не нужны такие откровенные кадры!"
        ryan "Я постараюсь сделать его не откровенным, а пикантным, Миссис Бакфетт..."
        ryan "С налетом легкой эротики..."
        m "!!!"
        m "Постарайся, Райен!"
        # Моника принимает позу, Райен фоткает, бросая пошлые взгляды на Монику
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24567, 24569, 24572], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel

    if result == "up":
        #up
        sound camera_lens1
        img 24566
        with Dissolve(0.2)
        w
        ryan "Я быстро сделаю несколько кадров и мы сменим позу."
        w
        call photoshop_flash() from _rcall_photoshop_flash_48
        w
        ryan "Вот так, да..."

        sound camera_lens1
        $ photoImage = 24567
        img 24567
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_123
        w
        m "Райен, долго еще!?"
        m "У меня рука затекла!"
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 24568
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_49
        w
        sound camera_lens1
        $ photoImage = 24569
        img 24569
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_124
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 24570
        with Dissolve(0.2)
        w
        ryan "Еще немного..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_50
        w
        sound camera_lens1
        img 24571
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_51
        w
        sound camera_lens1
        $ photoImage = 24572
        img 24572
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_125
        w
        ryan "Отлично!"
        m "Наконец-то!"
        # 9-й кадр (Z MC 10 Genesis 3 Female)
        # Райен фоткает
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel


label ep22_5_dialogues4_rayan_3_photoshoot_pose10:
    $ photoPoseLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose10"
    $ photoPoseNextLabel = "ep22_5_dialogues4_rayan_3_photoshoot_pose_end"
    #кадр
    img 24573
    if shots == 0 or shotsAmount == 0:
        $ shots = 3
        $ arrowUp = True
        $ arrowSide = True
        $ arrowDown = True
        hide screen photoshoot_camera_icon
        hide screen photoshoot2
        music stop
        jump expression photoPoseNextLabel

    show screen photoshoot_camera_icon(PS12_shoots_array)
    show screen photoshoot2([24575, 24577, 24581], PS12_shoots_array)
    $ result = ui.interact()
    hide screen photoshoot2
    if result == "next":
        $ shots = 0
        jump expression photoPoseLabel
    if result == "up":
        #up
        sound camera_lens1
        img 24574
        with Dissolve(0.2)
        w
        m "Не смотри ТУДА!"
        ryan "Я и не смотрю, Миссис Бакфетт..."
        ryan "Я подбираю наилучший ракурс."
        m "!!!"
        w
        call photoshop_flash() from _rcall_photoshop_flash_52
        w
        sound camera_lens1
        $ photoImage = 24575
        img 24575
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_126
        w
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "side":
        #side
        sound camera_lens1
        img 24576
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_53
        w
        ryan "О, вы просто сногсшибательно смотритесь, Миссис Бакфетт!"
        m "Я всегда сногсшибательна, Райен! Если ты не заметил!"
        sound camera_lens1
        $ photoImage = 24577
        img 24577
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_127
        w
        ryan "О, даа! Я заметил..."
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel
    if result == "down":
        #down
        sound camera_lens1
        img 24578
        with Dissolve(0.2)
        w
        ryan "Еще пара кадров..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_54
        w
        sound camera_lens1
        img 24579
        with Dissolve(0.2)
        w
        call photoshop_flash() from _rcall_photoshop_flash_55
        w
        ryan "Еще немного... Вот так, да..."
        sound camera_lens1
        img 24580
        with Dissolve(0.2)
        w
        ryan "Мммм..."
        w
        call photoshop_flash() from _rcall_photoshop_flash_56
        w
        sound camera_lens1
        $ photoImage = 24581
        img 24581
        with Dissolve(0.2)
        w
        call photoshoot_flash_count() from _rcall_photoshoot_flash_count_128
        w
        # 10-й кадр (Z MC 01 Genesis 3 Female)
        $ PS12_shoots_array.append(photoImage)
        jump expression photoPoseLabel

label ep22_5_dialogues4_rayan_3_photoshoot_pose_end:
    hide screen photoshoot_camera_icon
    hide screen photoshoot2
    music Stealth_Groover
    imgf 44825
    ryan "Мы закончили, Миссис Бакфетт!"
    # Моника с встает со стула и грозно приказывает Райену
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgf 44826
    m "Теперь неси эти чертовы снимки для рекламы Кэмпбелла!"
    m "Я и так потратила кучу своего бесценного времени здесь!"
    m "!!!"
    imgd 44827
    ryan "Да, Миссис Бакфетт, конечно!"
    ryan "Я только хотел сказать, что это была потрясающая фотосессия..."
    ryan "И я был бы не против поработать с вами еще не один раз."
    img 44828
    m "С чего бы это?!"
    m "У меня и без твоих фотосессий все дни расписаны буквально по минутам!"
    imgf 44829
    ryan "Да, и я прекрасно это понимаю."
    ryan "Я не могу вам предложить большую сумму денег за фотосессии."
    ryan "К тому же, я предполагаю, что деньги вас не интересуют..."
    ryan "У вас и так все есть - влияние, деньги, слава..."
    m "..."
    imgd 44830
    ryan "Но вы ведь творческая личность, Миссис Бакфетт."
    ryan "Я вижу, что вам нравится принимать участие в съемках подобного рода..."
    ryan "Я мог бы вам платить чисто символичесвку сумму... Скажем, триста долларов за фотосессию."
    music Power_Bots_Loop
    img 44831 vpunch
    m "Райен, ты что, издеваешься сейчас надо мной?!"
    m "?!"
    music Groove2_85
    imgd 44832
    ryan "Нет, Миссис Бакфетт, не издеваюсь, а предлагаю приятное сотрудничество."
    ryan "Просто имейте ввиду, что я буду всегда рад поработать с вами..."
    # Моника прерывает его жестом
    sound Jump1
    img 44833 hpunch
    m "Все, Райен, хватит!"
    m "Неси мне снимки!!!"
    m "!!!"
    imgd 44834
    ryan "Да, Миссис Бакфетт."
    ryan "В качестве моей благодарности за такую великолепную фотосессию..."
    ryan "Я позволю вам отобрать нужные вам снимки."
    sound Jump2
    img 44835
    m "И оденься! Хватит тут трясти передо мной своим!.. Вот этим!"
    # Райен усмехается
    imgf 44836
    ryan "Я сейчас вернусь, Миссис Бакфетт..."
    # затемнение
    fadeblack
    sound snd_fabric1
    pause 2.0
    return True

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
