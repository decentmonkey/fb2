default monicaBettyLiamFred1 = False # Бетти пошла к соседу забирать свой утюг
default monicaBettyLiamFred2 = False # Бетти согласилась помочь соседу с утюгом
default monicaBettyLiamFred3 = False # Бетти согласилась на секс с соседом (DP с Фредом)



# при условии, что Бетти уже помогла соседу
# при переходе Моники на какую-нибудь локацию
# показываем Бетти в доме
label ep217_dialogues3_betty_1:
    # тем временем
    # Бетти стоит у зеркала и смотрит на себя
    betty_t "Этот Лиам так переживает из-за своей проблемы..."
    betty_t "Кто та черствая женщина, кто мог поселить в нем такую неуверенность?"
    betty_t "Сразу видно, что это была непорядочная женщина."
    betty_t "Не то, что я!"
    betty_t "Я ему помогла, потому что я добрая и отзывчивая."
    betty_t "Он хороший сосед, а соседям нужно помогать!"
    betty_t "И с утюгом я ему помогла! Я не могла поступить иначе."
    betty_t "Ведь я хорошая хозяйка!"
    betty_t "Только... Надо бы забрать у него мой утюг..."
    betty_t "Как я могла его забыть? Все из-за Фреда!"
    betty_t "Еще несколько секунд и он увидел бы, что я помогала Лиаму."
    betty_t "Водителю совсем необязательно знать, чем занимается хозяйка дома!"
    betty_t "Это мое личное дело - помогать соседу или нет!"
    betty_t "И вообще! Лиам мог бы и сам принести утюг!"
    betty_t "Теперь мне приходится тратить на это свое время!"
    menu:
        "Сходить к соседу за утюгом.":
            $ monicaBettyLiamFred1 = True # Бетти пошла к соседу забирать свой утюг
            pass
        "Не ходить. (прерывание квеста)":
            betty_t "Хотя..."
            betty_t "Достаточно того, что я уже ему помогла!"
            betty_t "Пусть сам принесет мне мой утюг!"
            betty_t "А у меня есть другие важные дела!"
            return False
    # Бетти выходит из комнаты
    # затемнение
    # Бетти выходит во двор, и с деловым видом идет в сторону ворот
    fred "Добрый день, Миссис Робертс!"
    betty "Здравствуй, Фред."
    # Бетти проходит мимо него
    # Фред за ней наблюдает, смотрит ей вслед, многозначительно улыбаясь
    return

# дом соседа, при клике на входную дверь
label ep217_dialogues3_betty_2:
    # затемнение, стук в верь, звук двери, шаги
    # Бетти и Лиам стоят в его гостиной
    # сосед удивлен ее визиту
    liam "Мэм, рад вас видеть!"
    betty "Лиам, здравствуйте."
    betty "Я в прошлый раз так торопилась, что..."
    betty "Забыла у вас утюг."
    # он делает удивленный вид
    liam "Правда, Мэм?"
    liam "Я даже не обратил внимания на это..."
    # Бетти с соседом смотрят на стол, на нем расстелены штаны и рядом стоит утюг, продукты со стола, которые мешают, можно убрать. Остальные оставить
    betty "Не обратил внимания?"
    liam "Да, Мэм..."
    liam "Я даже не знаю, как просить вас об этом..."
    liam "Но мне снова нужна ваша помощь, Мэм..."
    betty "Какая еще помощь?"
    liam "Мне нужно погладить штаны, а я забыл, как пользоваться этим сложным механизмом..."
    liam "Со множеством кнопок..."
    liam "Вы же знаете, я бы предпочел одну большую кнопку для управления всеми функциями."
    betty "Лиам, я же вам все показала в прошлый раз..."
    betty "Там нет ничего сложного."
    liam "Если Мэм мне напомнит, я ей буду очень благодарен за помощь."
    menu:
        "Помочь Лиаму.":
            $ monicaBettyLiamFred2 = True # Бетти согласилась помочь соседу с утюгом
            pass
        "Сам разберется! (прерывание квеста)":
            betty "Там нет ничего сложного, поэтому вы сами сможете разобраться!"
            liam "Хорошо, я попробую, Мэм..."
            # Бетти разворачивается и уходит, а он смотрит ей вслед
            return False
    # Бетти задумчиво
    betty_t "Если я сейчас откажу ему, это будет грубостью с моей стороны..."
    betty_t "Ведь в прошлый раз я помогла ему."
    betty_t "По-соседски."
    betty "Да, Лиам, я помогу вам."
    # Бетти идет в сторону стола, берет в руку утюг
    # Бетти стоит спиной к нему и объясняет как пользоваться утюгом
    betty "Включаете утюг..."
    betty "Потом эту кнопку поворачиваете сюда..."
    betty "А потом нажимаете вот сюда."
    # сосед подходит к ней сзади и прижимается
    liam "Ох, Мэм..."
    liam "Я готов вечно смотреть на ваши волшебные ручки."
    liam "Как ловко вы ими управляете."
    liam "И вы такая добрая и отзывчивая, Мэм..."
    # Бетти делает вид, что не замечает его прикосновений
    betty "Да, Лиам, я знаю..."
    betty "Я хорошая хозяйка и у меня всегда все получается."
    betty "За что бы я ни бралась..."
    liam "Да, Мэм, я заметил это в прошлый раз..."
    liam "Вы мне очень помогли не только с утюгом."
    #
    $ notif(_("Бетти помогла соседу, проверив, достаточно ли твердый у него член."))
    #
    betty "Да?"
    liam "Это правда, Мэм..."
    # он проводит руками по ее попе, талии
    liam "Мне перестали сниться кошмары по ночам."
    liam "И я чувствую себя немного увернее, но..."
    betty "Что?"
    liam "Я тут подумал, а вдруг это была простая случайность?"
    betty_t "Какая еще случайность?"
    betty_t "Что он несет?"
    betty "Случайность?"
    liam "Да..."
    liam "Ведь вполне может быть, что..."
    liam "Мой член всего один раз был такой твердый..."
    liam "И больше такого не повторится."
    liam "Я теперь очень переживаю из-за этого."
    # Бетти поворачивает голову и смотрит на него подозрительно, не отстраняется
    betty_t "На что это он намекает?"
    betty_t "Он что, хочет, чтобы я снова ему помогала?"
    betty "Уверена, что это была не случайность, Лиам."
    betty "Ваш член был очень твердый. Это не может быть случайностью..."
    liam "Все же эти навязчивые мысли мешают мне..."
    liam "Если вы, Мэм, как моя хорошая и добрая соседка еще раз мне поможете..."
    liam "И я смогу убедиться, что это была не случайность..."
    liam "Тогда я буду самым счастливым мучиной на свете!"
    betty "Помочь еще раз?!"
    liam "Да. Это как прийти к врачу после выздоровления."
    liam "Чтобы убедиться, что ты выздоровел."
    liam "Вы же не бросите меня, терзающегося в сомнениях соседа?"
    liam "Ведь я ни к кому больше не могу обратиться с этой проблемой..."
    liam "Я доверился вам одной..."
    liam "Что скажете, Мэм?"
    menu:
        "Я верная жена!":
            $ monicaBettyLiamFred3 = True # Бетти согласилась на секс с соседом (DP с Фредом)
            pass
        "Нет! Я не буду этого делать! (прерывание квеста)":
            # Бетти отстраняется от него, встает руки в боки, возмущенно
            betty "Как вы можете мне предлагать подобные вещи?!"
            betty "Я верная жена и порядочная женщина!"
            betty "Вы придумали сами себе какую-то нелепую проблему!"
            betty "Вот сами с этим и разбирайтесь!"
            # Бетти разворачивается и уходит возмущенно, а он смотрит ей вслед
            return False
    # Бетти поворачивается к нему, начинает ломаться
    betty "Лиам..."
    betty "Я верная жена и порядочная женщина..."
    betty "А вы просите меня о подобном..."
    liam "Мэм, у вас поистине целебные ручки."
    liam "Я был под таким впечатлением от них, что долго не мог прийти в себя..."
    liam "Теперь Мэм мне снится каждую ночь."
    betty "Правда? Я вам снюсь?"
    # достает свой стояк
    # Бетти снова на него залипает
    betty "Но... На вид он достаточно упругий и твердый..."
    betty "Не думаю, что нужна моя помощь..."
    liam "Он только кажется таким, Мэм."
    liam "На самом деле, я думаю, что у меня вряд ли получится..."
    # Бетти 'отлипает' от его стояка, как бы приходит в себя
    # пытается возмущаться
    betty "Лиам, я не собраюсь делать этого!"
    betty "Мой дом буквально в двух шагах отсюда!"
    betty "И меня ждет мой муж!"
    betty "Тем более, мой водитель чуть не увидел нас в прошлый раз!"
    # берет в руку его член и продолжает ломаться
    betty "Я еще раз вам повторяю, что я верная жена!"
    liam "Вашему мужу очень повезло с такой красивой и верной женой, Мэм!"
    liam "Я искренне ему завидую!"
    liam "У вас такой богатый дом!"
    betty "Да! Я хозяйка богатого дома!"
    betty "И я не собираюсь ему изменять!"
    liam "Мэм, ваша помощь - это не измена."
    liam "Вы просто очень хорошая соседка. Поэтому и помогаете мне."
    # Бетти начинает водить рукой по его члену
    betty "Он твердый, как и в прошлый раз!"
    betty "Я уверена, что не нужно ничего больше проверять!"
    liam "Я ведь сосвем чуть-чуть, Мэм..."
    liam "Просто чтобы проверить..."
    liam "И сразу уберу его."
    betty "Нет, я не собираюсь делать этого, Лиам!"
    betty "Вы злоупотребляете тем, что у вас такая хорошая соседка!"
    # Бетти идет к дивану, держа соседа за член и ведя таким образом за собой
    # сосед садится на диван, Бетти наклоняется над ним и приближает лицо к его члену
    betty_t "Я просто прикоснусь к нему немного..."
    betty_t "Хоть мне это и не нравится."
    betty_t "Но прикосновение - это не измена..."
    betty "Не вижу необходимости какой-либо проверки!"
    # проводит языком по члену
    betty "И вообще!"
    betty "Я никогда не делаю подобного с дургими мужчинами, кроме своего мужа!"
    betty "И вы, Лиам, не исключение!"
    # берет его член в рот, начинает водить голвоой вверх-вниз
    liam "Мээээммммм..."
    liam "Мммммм..."
    # Бетти отстраняется, встает
    betty "Думаю, что этого будет достаточно!"
    liam "Но Мэм..."
    liam "А как же..."
    # пока Лиам мямлит, шуршание одежды, кадр на пол, там лежит платье Бетти
    betty_t "Отказывать в помощи соседу, когда он так нуждается в ней - это не по-соседски..."
    betty_t "Я быстренько помогу ему и пойду домой."
    betty_t "Мне еще нужно приготовить Ральфу обед..."
    betty "Лиам, только совсем чуть-чуть!"
    betty "И быстро!"
    liam "Да, Мэм... Я только попробую, как в прошлый раз!"
    # Бетти сама лезет на соседа, раскорячивается над ним и садится на его член
    # начинает двигаться
    liam "Оооо, как же хорошо у вас внутри, Мэм..."
    liam "Мне так нравится быть с вами!"
    liam "Как же мне повезло, что у меня такая соседка!"
    betty "Хорошая и порядочная..."
    liam "Да..."
    liam "Еще и хорошая хозяйка..."
    betty "Да... И верная жена своего мужа..."
    betty "Поэтому не позволяйте при мне всякие пошлости!"
    liam "О да, Мэм! Ему очень повезло с такой женой, как вы..."
    liam "Оооо, еще!!"
    # в самый разгар секса затемнение
    # звук скрип двери
    # смена кадра - в дверь заходит Фред со своей профессиональной улыбочкой
    # Лиам Фреда увидел сразу и самодовольно улыбается ему
    fred "..."
    liam "..."
    # Фред наблюдает с улыбочкой за Бетти и расстегивает штаны
    # Бетти его не замечает и продолжает скакать на Лиаме
    betty "Мммм..."
    betty "Ох..."
    betty "Я думаю, что эта проверка..."
    betty "Пройдет успешно... Оооо..."
    # Фред подходит к Бетти
    # Лиам приподнимает Бетти за бедра, она прогибается в спине и Фреду открывается доступ к попе
    # Фред пристраивает член к попе Бетти и вводит его немного
    # Бетти останавливается
    betty "АЙ!!! ЧТО ЭТО?!"
    betty "!!!"
    # Бетти возмущенно оглядывается
    betty "Фред! Что ты делаешь?!! Не смей!!!"
    betty "Быстро убери из меня ЭТО!!!"
    # Фред вводит член и спокойно говорит, улыбаясь
    fred "Миссис Робертс..."
    fred "Я как ответственный работник..."
    fred "Нахожу своей профессиональной обязанностью..."
    fred "Не допустить того, чтобы моя хозяйка осталась неудовлетворенной..."
    betty "Нет!!! Не смей!!!"
    betty "Не трогай меня!!!"
    betty "Твоя хозяйка тебе приказывает!"
    # Фреду по фиг
    fred "Миссис Робертс, сначала я выполню свои профессиональные обязанности."
    fred "А потом, с чувством выполненного профессионального долга, покину это помещение."
    fred "Уверен, Лиам не против того, чтобы я проявил свой профессионализм и помог ему..."
    # Лиам молча улыбается и делает несколько движений бедрами, двигаясь в Бетти
    # она плывет от этого
    betty "Ооох..."
    betty "Ааах, перестань, Фред!"
    # уже менее уверенно говорит Фреду
    betty "Фред, я приказываю тебе..."
    betty "Мммм..."
    betty "Иди... Оооох..."
    # Фред уже пялит ее
    betty "Нееет... Не надоооо..."
    betty "Я не собираюсь делать этогоооо..."
    liam "Все в порядке, Мэм..."
    liam "Вам понравится..."
    fred "Я ведь профессионал..."
    betty "Фред, не смей! Ооооо!!!"
    betty "ОООООО!!!"
    betty "Я не разрешалаааааа..."
    betty "ААААА!!!"
    betty "Я приказываю!"
    fred "Мэм, мне его вынуть из вас?"
    betty "Что? Нет, не надо вынимать! АААААА!"
    liam "О, Мэээм..."
    liam "Это чертовски охренительно, Мэээм!!"
    fred "Дааа, черт!"
    fred "Мммм..."
    betty "Ооооох!!!"
    betty "ОООООО!!!"
    betty "Я так долго не смогууу!!!"
    fred "Кончайте, Миссис Робертс!!"
    liam "Да!"
    betty "Яяяаааа... Кончу сейчааааас!!!"
    # Бетти кончает
    betty "Ааааах!!!"
    betty "АААААХ!!!"
    betty "АААААААА!!!"
    menu:
        "Кончить внутрь Бетти.":
            # Фред и Лиам кончают внутрь Бетти
            liam "Я тоже..."
            liam "Кончаааааю!!!"
            liam "ААА!"
            liam "АААААА!!"
            fred "МММММММ!!!"
            pass
        "Кончить на Бетти.":
            # Фред и Лиам кончают на киску и на попу Бетти
            liam "Я тоже..."
            liam "Кончаааааю!!!"
            liam "ААА!"
            liam "АААААА!!"
            fred "МММММММ!!!"
            pass
    # затемнение, шуршание одежды
    # голая Бетти лежит на диване в гостиной у соседа в отключке
    # Фред и Лиам стоят уже одетые
    liam "А она горячая штучка..."
    fred "Да, горячая. Это точно."
    liam "А почему ты называешь ее хозяйкой?"
    liam "Раньше ведь была другая..."
    # если Моника закатила соседу иск
    liam "Какая-то стерва, которая мне закатила огромный иск за царапину на заборе."
    liam "Как ее там звали? Бакфетт что-ли?"
    # Фред усмехается
    fred "Да. Миссис Бакфетт."
    liam "А где она?"
    # если Моника закатила соседу иск
    liam "Из-за нее у меня чуть не отняли мой дом!"
    #
    fred "О, Лиам."
    fred "Это очень интересная история..."
    fred "Как-нибудь я тебе расскажу ее..."
    # затемнение, спустя несколько минут
    # Бетти, Фред и Лиам стоят в гостиной соседа, Бетти уже в одежде
    betty "Фред! Лиам!"
    fred "Да, Миссис Робертс?"
    betty "Фред, ты все не так понял, Я не изменяю своему мужу!"
    fred "Ну разве это измена, Миссис Робертс?"
    fred "Вы просто немного отдыхаете от домашних забот..."
    fred "Вы настолько хорошая хозяйка, что у вас совсем нет времени на отдых."
    # Бетти надменно
    betty "Да, это так! Я хорошая хозяйка и порядочная женщина!"
    betty "И вообще, я пришла сюда, чтобы забрать мой утюг!"
    # она подходит к столу и тянет руку к утюгу
    # крупным планом показываем, как рука Фреда ложится на ее руку, не давая взять утюг
    fred "Миссис Робертс, я думаю, что вам нужно оставить это здесь..."
    # Бетти непонимающе на него смотрит
    betty "Зачем?"
    fred "Вашему соседу в любой момент может понадобится ваша помощь..."
    fred "Ведь он совсем не умеет гладить этим утюгом..."
    # Бетти косится на фреда, на соседа (они улыбаются), а потом смущенно опускает глаза, убирая руку от утюга
    betty "Я..."
    fred "Да, Мэм?"
    betty "Нет, ничего! Мне пора готовить обед для своего мужа!"
    # выбегает из гостиной
    return


# после этого игра переключается на события с Моникой
