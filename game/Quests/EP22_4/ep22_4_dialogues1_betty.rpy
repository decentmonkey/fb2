default monicaLiamBettyHousemaid1 = 0 # Бетти психанула и пошла забирать утюг у Лиама
default monicaLiamBettyHousemaid2 = 0 # Бетти согласилась переодеться в фартук


# бывший дом Моники, прачечная
# после сцены с Ральфом в спальне, на другой день
label ep22_4_dialogues1_betty_1:
    # Бетти стоит недовольная, смотрит на гладильную доску
    betty_t "Мне это надоело!"
    betty_t "Почему я не могу в собственном доме погладить вещи?!"
    betty_t "И все из-за какого-то дурацкого соседа!!!"
    betty_t "С чего он вообще взял, что может просто так взять и завладеть МОЕЙ вещью?!"
    betty_t "Что это вообще за глупости?!"
    betty_t "!!!"
    menu:
        "Забрать утюг у соседа.":
            $ monicaLiamBettyHousemaid1 = day # Бетти психанула и пошла забирать утюг у Лиама
            pass
        "Нет!":
            betty_t "Хм... Но если так подумать..."
            betty_t "Я, Бетти Робертс!.."
            betty_t "Я хозяйка богатого дома и верная жена своего мужа!.."
            betty_t "Почему это Я должна сама ходить в нему за МОИМ утюгом?!"
            betty_t "Я не собираюсь больше поддаваться на эти глупые провокации!"
            betty_t "Каждый мой визит в его дом всегда заканчивается одинаково!"
            betty_t "С меня хватит!"
            betty_t "Я Лиаму итак достаточно помогла в решении его проблемы!"
            betty_t "И не допущу, чтобы он злоупотреблял моей добротой и порядочностью!"
            betty_t "Пусть сам принесет этот дурацкий утюг!!!"
            betty_t "И вообще! Я могу себе позволить купить новый!"
            # выходит из прачечной, затемнение
            return
    betty_t "Я не допущу чтобы мною, хозякой богатого дома и порядочной женщиной!.."
    betty_t "Манипулировал какой-то там сосед, используя МОЙ утюг!"
    betty_t "Мне нужно прекратить весь этот цирк!"
    betty_t "Я простой пойду и заберу у него то, что принадлежит МНЕ!"
    # затемнение, смена кадра
    # Бетти стоит перед домом соседа и стучится в дверь
    # затемнение, звук двери, каблуки
    # смена кадра, злая Бетти стоит в гостиной, Лиам с довольной улыбкой смотрит на нее
    # утюг, как обычно, на столе
    liam "О, Мэм!"
    liam "Как я рад, что вы зашли ко мне!"
    # Бетти с наездом
    betty "Лиам, верните мне МОЙ утюг!!!"
    liam "Да, Мэм, конечно я его верну..."
    liam "Немного позже..."
    liam "Если он вам так нужен, то вы можете приходить ко мне и гладить вещи здесь."
    # Бетти возмущенно
    betty "Еще чего?! Это МОЙ утюг!"
    betty "И я буду гладить свои вещи у себя дома!"
    liam "Конечно, будете, Мэм..."
    liam "Но мне так нравится смотреть на вас, когда вы держите в руках утюг..."
    liam "Вы так умело управляетесь со всеми кнопками, Мэм!"
    liam "Я готов вечно смотреть на это! Так что можете делать это у меня дома..."
    betty "Лиам, я!.."
    # Лиам озадаченно перебивает ее
    liam "Мэм..."
    liam "Я хотел бы попросить вас о помощи..."
    betty "Что?! Опять?!"
    betty "Знаете что, Лиам, мне кажется, что все ваши проблемы с недостаточно твердым членом надуманы!.."
    # он ее перебивает, примирительно подняв руки
    liam "Нет-нет, Мэм!"
    liam "С этим теперь все в полном порядке!"
    liam "И все благодаря вашим умелым ручкам, Мэм!" # подмигивает
    betty "Да! Благодаря мне!"
    betty "И больше меня не тревожьте подобными просьбами!"
    liam "Конечно, Мэм!"
    liam "Мне нужна помощь совсем не в этом!"
    liam "Я знаю, что вы добрая соседка..."
    liam "К тому же еще и замечательная хозяйка..."
    # Бетти подозрительно смотрит на него
    betty "Лиам... К чему вы клоните?!"
    liam "Мэм..."
    liam "Дело в том, Мэм, что я давно живу один..."
    liam "И у меня такой беспорядок в доме."
    liam "У меня совсем не получается убраться, как следует..."
    liam "Я тут подумал, раз у меня по соседству живет такая замечательная и хозяйственная соседка..."
    betty "Лиам, вы что, намекаете мне на то, чтобы я помогла вам с уборкой в доме?!"
    betty "Я такой работой не занимаюсь, Лиам!"
    betty "Я хозяйка богатого дома и у меня для этого есть гувернантка!"
    liam "О, в таком случае, не могли бы вы мне одолжить вашу гувернантку, Мэм?"
    betty "Что?! Одолжить мою гувернантку?! Еще чего?!"
    betty "Я, конечно, хорошая соседка, но не до такой степени, Лиам!"
    betty "Я не собираюсь отдавать вам свою гувернантку!"
    betty "Тем более, что она плохо делает свою работу!"
    betty "А с уборкой я и сама могу прекрасно справиться!"
    liam "Правда?!"
    liam "О, Мэм, какая же вы хорошая соседка! И такая добрая!"
    liam "Мне так с вами повезло!"
    betty "Да, я такая!"
    liam "Если Мэм сможет выбрать время, например, завтра..."
    liam "И помочь мне с уборкой, то я буду очень-очень признателен Мэм!"
    # он достает свой стояк и показывает ей
    liam "Возможно, я даже смогу ее отблагодарить..."
    liam "А потом и утюг отдам..."
    betty "!!!"
    menu:
        "Отказать ему!":
            pass
    # Бетти с оскорбленным видом
    betty "Я вам не какая-нибудь уборщица, Лиам!"
    betty "С какой стати вы решили, что я буду убираться у вас дома?!"
    betty "Вообще-то, вы разговариваете с супругой богатого мужчины!"
    betty "Как вы себе это представляете, чтобы я оставила свой роскошный дом и пришла наводить порядок здесь?!"
    betty "Это какой-то бред!"
    betty "Я даже слышать не хочу больше подобных просьб с вашей стороны, Лиам!"
    betty "!!!"
    # Бетти уходит с высокомерным лицом
    # Лиам с улыбкой смотрит на ее ноги или попу
    return

# на следующий день
# Бетти стоит возле дома соседа
label ep22_4_dialogues1_betty_2:
    betty_t "Я это сделаю, чтобы забрать свой утюг!"
    betty_t "Меня совсем не интересует его благодарность!"
    betty_t "Я верная жена своего мужа!"
    betty_t "И мне абсолютно безразлично, как он собирается меня благодарить!"
    betty_t "Помогу с уборокой, заберу свой утюг и все!"
    # затемение, стук в дверь, звук двери, каблуки
    # смена кадра на гостиную соседа
    # Бетти с деловым видом заходит, Лиам радостно
    liam "Мэм, я так рад, что вы пришли!"
    betty "Лиам, давайте сразу к делу! Я тороплюсь!"
    betty "Я очень занятая женщина!"
    betty "И мне с большим трудом удалось выделить время на помощь вам!"
    liam "Да, я знаю, Мэм..."
    liam "Конечно, вы правы!"
    liam "Проходите..."
    betty "Где у вас тут ведро, Лиам?!"
    # он неуверенно смотрит на ее платье
    liam "О, Мэм... Я тут подумал..."
    liam "У вас такое красивое платье... Оно так идет вам."
    betty "И?.."
    liam "Я боюсь, что вы его запачкаете во время уборки."
    # Бетти смотрит на свое платье
    betty "..."
    # Лиам торопливо
    liam "Но не переживайте за платье, Мэм!"
    liam "Лиам позаботился заранее о платье своей замечательной соседки!"
    betty "Позаботился?"
    liam "Да, Мэм! В гараже я нашел фартук! Cпециально для вас!"
    betty "Я не собираюсь надевать какой-то там фартук!"
    betty "Я, скорее, испачкаю свою платье этим дурацким фартуком, чем уборкой!"
    betty_t "Наверняка, это грязный вонючий фартук того торговца рыбой с рынка! Фу!"
    liam "Мэм, ваше платье точно останется чистым..."
    liam "Если вы его снимете и наденете только фартук..."
    betty "Что?!"
    betty "!!!"
    menu:
        "Я не собираюсь надевать какой-то дурацкий фартук!":
            $ monicaLiamBettyHousemaid2 = day # Бетти согласилась переодеться в фартук
            pass
        "Уйти отсюда! (прерывание сцены)":
            betty_t "Я, Бетти Робертс!.."
            betty_t "Я хозяйка богатого дома и верная жена своего мужа!.."
            betty_t "Почему это Я должна убираться у какого-то там соседа?!"
            betty_t "Да еще и в одном фартуке! Без одежды!!!"
            betty_t "Я не собираюсь больше поддаваться на эти глупые провокации!"
            betty_t "Каждый мой визит в его дом всегда заканчивается одинаково!"
            betty "С меня хватит, Лиам!"
            betty "Я вам итак достаточно помогла в решении вашей проблемы!"
            betty "И не допущу, чтобы вы злоупотребляли моей добротой и порядочностью!"
            betty "Оставьте себе этот дурацкий утюг!!!"
            betty "Я могу себе позволить купить новый!"
            # уходит
            return
    # Бетти сердито
    betty "Знаете что, Лиам?!"
    betty "Я не собираюсь надевать какой-то дурацкий фартук!"
    betty "У меня нет времени на все эти глупости!"
    liam "Но, Мэм..."
    betty "Давайте мне ведро и швабру!"
    # Лиам выходит, затемнение
    # возвращается с ведром и губкой
    liam "Вот, Мэм..."
    liam "Я все для вас приготовил."
    betty "Это еще что такое?!"
    betty "Я что, должна этим делать уборку?!"
    liam "Мэм, ну вы же такая замечательная хозяйка!"
    liam "Я уверен, что у вас отлично получится навести порядок."
    # она выхватывает у него ведро
    betty "Да, я замечательная хозяйка!"
    betty "С этим не сможет не справиться только какая-нибудь некомпетентная уборщица!"
    betty "Вроде моей непутевой горничной!"
    liam "Да, Мэм, вы правы!"
    betty "Где ваш дурацкий фартук?!"
    betty "Я не хочу его надевать!.."
    betty "Но этим я точно испорчу свое платье во время уборки!"
    # сосед довольно улыбается
    liam "Фартук на диване, Мэм..."
    # Бетти с деловым видом шагает к дивану
    betty "!!!"
    # затемнение, шуршание одежды
    # Бетти стоит голая, в одном фартуке, чепчике и туфлях
    liam "О, Мэээм!.."
    liam "У меня просто нет слов, как вам идет этот наряд!"
    liam "Вы такая!.. Такая!.."
    # кладет руку на свою ширинку
    betty "Я знаю, Лиам!"
    betty "Красивой женщине любой наряд к лицу!"
    betty "А теперь не мешайте мне!"
    betty "Можете вообще выйти отсюда, я вас позову, когда закончу."
    # он, продолжая теребить ширинку
    liam "Я вам не буду мешать, Мэм."
    liam "Я останусь, чтобы помогать вам..."
    # с этими словами идет и садится на диван, пошло поглядывая на Бетти
    # она с деловым видом начинает тереть журнальный столик напротив дивана, на котором лежат книги
    # он достает член и начинает ленико водить по стволу одной рукой
    liam "Как у вас хорошо получается, Мэм!"
    betty "Иначе и быть не могло у такой хорошей хозяйки, как я!"
    liam "Да, я вижу, что вы просто отличная хозяйка, Мэм!"
    betty "Да, это так!"
    liam "Протрите еще с той стороны стол, Мэм." # указывает другой рукой
    liam "Вам нужно нагнуться немного, иначе вы не дотянетесь."
    betty "!!!" # Бетти делает, при этом сверкая попой
    # потом Бетти начинает протирать шкаф, где стоит телек
    # Лиам также сидит на диване, лениво подрачивая
    liam "О, как чисто становится, Мэм..."
    liam "У вас и правда очень умелые ручки!"
    liam "Вон там еще протрите, Мэм."
    betty "Лиам, я лучше знаю!.." # поворачиваясь к нему
    # замолкает, увидев член
    betty "!!!"
    # отворачивается и указывает рукой
    betty "Здесь?"
    liam "Немного правее..."
    betty "Здесь?" # указывает в другое место
    liam "Ниже, Мэм..."
    liam "Да, здесь."
    liam "Вот теперь идеально чисто, Мэм!"
    # Бетти идет к столу, на котором утюг, и начинает протирать его
    # Лиам продолжает командовать, сидя на диване
    liam "Мэм, мне кажется, что лучше сначала помыть пол."
    # Бетти косится на его член и ворчит, продолжая убираться
    betty "Лиам, я сама знаю, как лучше убираться!"
    betty "Вы думаете, если у меня есть горничная, то я ничего не умею?"
    liam "Я так не думаю, Мэм..."
    liam "Я вижу, что в ваших умелых ручках любая работа получается на отлично!"
    betty "Да, Лиам!"
    # он указывает рукой на подоконник
    liam "Мэм, вы вот здесь еще не протирали пыль."
    betty "Где?"
    liam "Вот здесь..."
    # она, поглядывая на его член, идет к подоконнику
    # упирается коленом на диван, наклоняется и протирает подоконник
    # продолжая при этом ворчать
    betty "И вообще!"
    betty "С такой некомпетентной горничной, как у меня..."
    betty "Которая вообще ничего не умеет делать..."
    betty "Мне приходится самой выполнять всю работу по дому!"
    liam "Как я вас понимаю, Мэм..."
    liam "Наверное, тяжело содержать в порядке такой огромный дом, как у вас?"
    betty "Конечно, это непросто, Лиам!"
    betty "Вы хоть представляете, сколько там работы?!"
    # он указывает рукой на пол
    liam "Осталось вымыть пол, Мэм."
    # она, продолжая ворчать, встает на четвереньки и начинает тереть губкой пол
    betty "Я сама закупаю продукты, убираюсь и стираю!.."
    betty "Сама готовлю еду для своего мужа!.."
    # он довольно рассматривает ее и продолжает дрочить
    liam "Вы еще и готовить умеете, Мэм?!"
    betty "Конечно, я умею готовить!"
    betty "И очень вкусно!"
    liam "Без сомнения, Мэм! У вас просто золотые ручки!"
    liam "Как же повезло вашему мужу!"
    betty "Да, ему очень повезло с такой женой, как я!"
    betty "Я красивая, умная..."
    betty "Хозяйственная..."
    liam "Заботливая и порядочная."
    betty "Да. И еще верная!"
    liam "Да, Мэм!"
    liam "Вы не протерли пол еще вон там." # указывает рукой
    # Бетти смотрит на него, потом на член
    betty "Я сейчас все протру, Лиам."
    # переползает на другое место и начинает тереть там, он дрочит
    liam "Вы уже почти закончили, Мэм?"
    betty "Да, осталось немного."
    liam "Видите, как хорошо, что я позаботился о вашем платье?"
    liam "Сейчас оно, наверняка, испачкалось бы."
    liam "А вам так идет этот наряд, Мэм!"
    betty "Да, Лиам. Я знаю."
    liam "Мне уже не терпится отблагодарить вас, Мэм, за вашу помощь..."
    # она косится на его член
    betty "Мне не нужна никакая благодарность, Лиам!"
    betty "Я согласилась вам помочь, потому что я хорошая соседка!"
    liam "Вы самая лучшая соседка, Мэм!"
    betty "Да, я такая!"
    liam "Мэм, вы же не откажетесь мне помочь с уборкой в следующий раз?"
    betty "Лиам! Вы же знаете, какая я занятая женщина!"
    betty "Вы думаете, что..."
    liam "Я буду вам очень-очень благодарен!"
    liam "Такая замечательная женщина, как вы, не откажет мне, вашему хорошему соседу."
    # она смотрит на него, он дрочит
    # Бетти залипает на его член, смотрит, как загипнотизированная
    betty "Лиам..."
    liam "Мэм так отлично справилась с уборкой."
    liam "Я и мечтать не мог о такой чистоте в своем доме!"
    liam "Сразу видна рука прекрасной хозяйки!"
    liam "Посмотрите, Мэм, насколько я впечатлен вашей работой..."
    betty "Я..."
    liam "Вы не поймете, пока не потрогаете его." # указывает на свой член
    # Бетти очухивается от гипноза
    betty "Вы же знаете, что я порядочная женщина!"
    betty "Я не изменяю своему мужу!"
    betty "Как вы можете предлагать мне прикасаться к вашему?.."
    liam "Ну вы же просто потрогаете, чтобы понять, насколько я вам благодарен..."
    liam "Разве это измена, Мэм?"
    # Бетти снова залипает на члене соседа
    betty "..."
    liam "Просто потрогайте его..."
    # Бетти встает с пола и подходит к нему
    # показываем, как она с желанием смотрит на член
    # потом она протягивает руку и обхватывает член
    # затемнение, ритмичные звуки минета и охи на темном фоне
    return
