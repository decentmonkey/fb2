default monicaLiamBettyHousemaid1 = 0 # Бетти психанула и пошла забирать утюг у Лиама
default monicaLiamBettyHousemaid2 = 0 # Бетти согласилась переодеться в фартук

#call ep22_4_dialogues1_betty_1() # прачечная, Бетти собирается к соседу
#call ep22_4_dialogues1_betty_2() # дом соседа, уборка

# бывший дом Моники, прачечная
# после сцены с Ральфом в спальне, на другой день
label ep22_4_dialogues1_betty_1:
    # Бетти стоит недовольная, смотрит на гладильную доску
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Утро...")) from _rcall_textonblack_85
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgfl 35252
    w
    imgf 35253
    betty_t "Мне это надоело!"
    betty_t "Почему я не могу в собственном доме погладить вещи?!"
    betty_t "И все из-за какого-то дурацкого соседа!!!"
    imgd 35254
    betty_t "С чего он вообще взял, что может просто так взять и завладеть МОЕЙ вещью?!"
    betty_t "Что это вообще за глупости?!"
    betty_t "!!!"
    menu:
        "Забрать утюг у соседа.":
            $ monicaLiamBettyHousemaid1 = day # Бетти психанула и пошла забирать утюг у Лиама
            pass
        "Нет!":
            music Stealth_Groover
            imgf 35255
            betty_t "Хм... Но если так подумать..."
            betty_t "Я, Бетти Робертс!.."
            betty_t "Я хозяйка богатого дома и верная жена своего мужа!.."
            betty_t "Почему это Я должна сама ходить в нему за МОИМ утюгом?!"
            imgd 35256
            betty_t "Я не собираюсь больше поддаваться на эти глупые провокации!"
            betty_t "Каждый мой визит в его дом всегда заканчивается одинаково!"
            betty_t "С меня хватит!"
            betty_t "Я Лиаму итак достаточно помогла в решении его проблемы!"
            imgd 35257
            betty_t "И не допущу, чтобы он злоупотреблял моей добротой и порядочностью!"
            betty_t "Пусть сам принесет этот дурацкий утюг!!!"
            betty_t "И вообще! Я могу себе позволить купить новый!"
            # выходит из прачечной, затемнение
            fadeblack
            sound highheels_short_walk
            pause 2.0
            return False
    music Stealth_Groover
    imgf 35256
    betty_t "Я не допущу чтобы мною, хозякой богатого дома и порядочной женщиной!.."
    betty_t "Манипулировал какой-то там сосед, используя МОЙ утюг!"
    betty_t "Мне нужно прекратить весь этот цирк!"
    return True
label ep22_4_dialogues1_betty_1a:
    betty_t "Я простой пойду и заберу у него то, что принадлежит МНЕ!"
    return True
label ep22_4_dialogues1_betty_1b:
    # затемнение, смена кадра
    # Бетти стоит перед домом соседа и стучится в дверь
    # затемнение, звук двери, каблуки
    # смена кадра, злая Бетти стоит в гостиной, Лиам с довольной улыбкой смотрит на нее
    # утюг, как обычно, на столе
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 32877
    w
    sound highheels_short_walk
    imgf 32878
    sound2 snd_door_knock
    w
    fadeblack
    sound man_steps
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    imgfl 35258
    w
    imgf 35260
    w
    imgd 35261
    liam "О, Мэм!"
    liam "Как я рад, что вы зашли ко мне!"
    # Бетти с наездом
    imgd 35259
    w
    imgd 35262
    betty "Лиам, верните мне МОЙ утюг!!!"
    img 35263
    liam "Да, Мэм, конечно я его верну..."
    liam "Немного позже..."
    liam "Если он вам так нужен, то вы можете приходить ко мне и гладить вещи здесь."
    # Бетти возмущенно
    music Pyro_Flow
    img 35264 vpunch
    betty "Еще чего?! Это МОЙ утюг!"
    betty "И я буду гладить свои вещи у себя дома!"
    music Groove2_85
    liam "Конечно, будете, Мэм..."
    liam "Но мне так нравится смотреть на вас, когда вы держите в руках утюг..."
    imgd 35265
    liam "Вы так умело управляетесь со всеми кнопками, Мэм!"
    liam "Я готов вечно смотреть на это! Так что можете делать это у меня дома..."
    betty "Лиам, я!.."
    # Лиам озадаченно перебивает ее
    imgf 35266
    liam "Мэм..."
    liam "Я хотел бы попросить вас о помощи..."
    music Power_Bots_Loop
    img 35267 hpunch
    betty "Что?! Опять?!"
    betty "Знаете что, Лиам, мне кажется, что все ваши проблемы с недостаточно твердым членом надуманы!.."
    # он ее перебивает, примирительно подняв руки
    music Groove2_85
    sound2 Jump2
    img 35268
    liam "Нет-нет, Мэм!"
    liam "С этим теперь все в полном порядке!"
    sound Jump1
    imgd 35269
    liam "И все благодаря вашим умелым ручкам, Мэм!" # подмигивает
    imgf 35270
    betty "Да! Благодаря мне!"
    betty "И больше меня не тревожьте подобными просьбами!"
    liam "Конечно, Мэм!"
    liam "Мне нужна помощь совсем не в этом!"
    music Hidden_Agenda
    imgd 35271
    liam "Я знаю, что вы добрая соседка..."
    liam "К тому же еще и замечательная хозяйка..."
    # Бетти подозрительно смотрит на него
    img 35262
    betty "Лиам... К чему вы клоните?!"
    imgf 35271
    liam "Мэм..."
    liam "Дело в том, Мэм, что я давно живу один..."
    imgd 35272
    liam "И у меня такой беспорядок в доме."
    liam "У меня совсем не получается убраться, как следует..."
    liam "Я тут подумал, раз у меня по соседству живет такая замечательная и хозяйственная соседка..."
    music Groove2_85
    imgd 35273
    betty "Лиам, вы что, намекаете мне на то, чтобы я помогла вам с уборкой в доме?!"
    betty "Я такой работой не занимаюсь, Лиам!"
    betty "Я хозяйка богатого дома и у меня для этого есть гувернантка!"
    liam "О, в таком случае, не могли бы вы мне одолжить вашу гувернантку, Мэм?"
    music stop
    sound plastinka1b
    img 35267 hpunch
    betty "Что?! Одолжить мою гувернантку?! Еще чего?!"
    music Stealth_Groover
    betty "Я, конечно, хорошая соседка, но не до такой степени, Лиам!"
    betty "Я не собираюсь отдавать вам свою гувернантку!"
    imgd 35270
    betty "Тем более, что она плохо делает свою работу!"
    betty "А с уборкой я и сама могу прекрасно справиться!"
    music Groove2_85
    liam "Правда?!"
    liam "О, Мэм, какая же вы хорошая соседка! И такая добрая!"
    sound man_steps
    imgf 35274
    liam "Мне так с вами повезло!"
    betty "Да, я такая!"
    sound vjuh3
    imgd 35275
    liam "Если Мэм сможет выбрать время, например, завтра..."
    liam "И помочь мне с уборкой, то я буду очень-очень признателен Мэм!"
    # он достает свой стояк и показывает ей
    sound Jump2
    img 35276 vpunch
    liam "Возможно, я даже смогу ее отблагодарить..."
    liam "А потом и утюг отдам..."
    imgd 35277
    betty "!!!"
    menu:
        "Отказать ему!":
            pass
    # Бетти с оскорбленным видом
    music Pyro_Flow
    sound2 Jump2
    img 35278 hpunch
    betty "Я вам не какая-нибудь уборщица, Лиам!"
    betty "С какой стати вы решили, что я буду убираться у вас дома?!"
    betty "Вообще-то, вы разговариваете с супругой богатого мужчины!"
    imgd 35279
    betty "Как вы себе это представляете, чтобы я оставила свой роскошный дом и пришла наводить порядок здесь?!"
    betty "Это какой-то бред!"
    betty "Я даже слышать не хочу больше подобных просьб с вашей стороны, Лиам!"
    betty "!!!"
    sound highheels_short_walk
    imgf 35280
    w
    fadeblack
    sound highheels_short_walk
    pause 2.0
    # Бетти уходит с высокомерным лицом
    # Лиам с улыбкой смотрит на ее ноги или попу
    return

# на следующий день
# Бетти стоит возле дома соседа
label ep22_4_dialogues1_betty_2:
    scene black_screen
    with Dissolve(1)
    music stop
    call textonblack(t_("Утро...")) from _rcall_textonblack_86
    scene black_screen
    with Dissolve(1)
    music Groove2_85
    imgf 32877
    w
    imgd 35281
    betty_t "Я это сделаю, чтобы забрать свой утюг!"
    betty_t "Меня совсем не интересует его благодарность!"
    betty_t "Я верная жена своего мужа!"
    betty_t "И мне абсолютно безразлично, как он собирается меня благодарить!"
    betty_t "Помогу с уборокой, заберу свой утюг и все!"
    sound highheels_short_walk
    imgf 32878
    sound2 snd_door_knock
    w
    fadeblack
    sound man_steps
    pause 2.0
    sound snd_door_open1
    pause 1.5
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    # затемение, стук в дверь, звук двери, каблуки
    # смена кадра на гостиную соседа
    # Бетти с деловым видом заходит, Лиам радостно
    imgfl 35282
    liam "Мэм, я так рад, что вы пришли!"
    betty "Лиам, давайте сразу к делу! Я тороплюсь!"
    betty "Я очень занятая женщина!"
    betty "И мне с большим трудом удалось выделить время на помощь вам!"
    imgf 35283
    liam "Да, я знаю, Мэм..."
    liam "Конечно, вы правы!"
    liam "Проходите..."
    betty "Где у вас тут ведро, Лиам?!"
    # он неуверенно смотрит на ее платье
    imgd 35284
    liam "О, Мэм... Я тут подумал..."
    liam "У вас такое красивое платье... Оно так идет вам."
    betty "И?.."
    liam "Я боюсь, что вы его запачкаете во время уборки."
    # Бетти смотрит на свое платье
    imgf 35285
    w
    imgd 35286
    betty "..."
    # Лиам торопливо
    img 35287
    liam "Но не переживайте за платье, Мэм!"
    liam "Лиам позаботился заранее о платье своей замечательной соседки!"
    betty "Позаботился?"
    liam "Да, Мэм! В гараже я нашел фартук! Cпециально для вас!"
    music Stealth_Groover
    imgd 35288
    betty "Я не собираюсь надевать какой-то там фартук!"
    betty "Я, скорее, испачкаю свою платье этим дурацким фартуком, чем уборкой!"
    imgd 35289
    betty_t "Наверняка, это грязный вонючий фартук того торговца рыбой с рынка! Фу!"
    music Hidden_Agenda
    imgf 35290
    liam "Мэм, ваше платье точно останется чистым..."
    liam "Если вы его снимете и наденете только фартук..."
    music Pyro_Flow
    img 35296 hpunch
    betty "Что?!"
    betty "!!!"
    menu:
        "Я не собираюсь надевать какой-то дурацкий фартук!":
            $ monicaLiamBettyHousemaid2 = day # Бетти согласилась переодеться в фартук
            pass
        "Уйти отсюда! (прерывание сцены)":
            imgd 35292
            betty_t "Я, Бетти Робертс!.."
            betty_t "Я хозяйка богатого дома и верная жена своего мужа!.."
            betty_t "Почему это Я должна убираться у какого-то там соседа?!"
            betty_t "Да еще и в одном фартуке! Без одежды!!!"
            imgd 35293
            betty_t "Я не собираюсь больше поддаваться на эти глупые провокации!"
            betty_t "Каждый мой визит в его дом всегда заканчивается одинаково!"
            sound highheels_short_walk
            imgf 35294
            betty "С меня хватит, Лиам!"
            betty "Я вам итак достаточно помогла в решении вашей проблемы!"
            betty "И не допущу, чтобы вы злоупотребляли моей добротой и порядочностью!"
            ## фраза соседа "Мэм, но как же Ваш утюг" или что-то типа того
            liam "Но, Мэм!.. А как же утюг?"
            imgd 35295
            betty "Оставьте себе этот дурацкий утюг!!!"
            betty "Я могу себе позволить купить новый!"
            fadeblack
            sound highheels_short_walk
            pause 2.0
            # уходит
            return False
    # Бетти сердито
    imgd 35291
    betty "Знаете что, Лиам?!"
    betty "Я не собираюсь надевать какой-то дурацкий фартук!"
    betty "У меня нет времени на все эти глупости!"
    liam "Но, Мэм..."
    imgd 35288
    betty "Давайте мне ведро и швабру!"
    music Groove2_85
    sound2 man_steps
    imgf 35297
    w
    imgd 35298
    w
    fadeblack
    sound snd_door_open1
    pause 1.5
    music Groove2_85
    # Лиам выходит, затемнение
    # возвращается с ведром и губкой
    imgfl 35299
    w
    imgf 35300
    liam "Вот, Мэм..."
    liam "Я все для вас приготовил."
    sound Jump2
    img 35301 vpunch
    betty "Это еще что такое?!"
    betty "Я что, должна этим делать уборку?!"
    music Hidden_Agenda
    imgd 35302
    liam "Мэм, ну вы же такая замечательная хозяйка!"
    liam "Я уверен, что у вас отлично получится навести порядок."
    # она выхватывает у него ведро
    sound vjuh3
    img 35303
    betty "Да, я замечательная хозяйка!"
    betty "С этим не сможет не справиться только какая-нибудь некомпетентная уборщица!"
    betty "Вроде моей непутевой горничной!"
    liam "Да, Мэм, вы правы!"
    imgd 35304
    betty "Где ваш дурацкий фартук?!"
    betty "Я не хочу его надевать!.."
    betty "Но этим я точно испорчу свое платье во время уборки!"
    # сосед довольно улыбается
    liam "Фартук на диване, Мэм..."
    # Бетти с деловым видом шагает к дивану
#    music Groove2_85
    sound highheels_short_walk
    imgf 35305
    w
    imgd 35306
    betty "!!!"
    # затемнение, шуршание одежды
    # Бетти стоит голая, в одном фартуке, чепчике и туфлях
    fadeblack
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    imgfl 35307
    w
    imgf 35308
    w
    imgd 35309
    liam "О, Мэээм!.."
    liam "У меня просто нет слов, как вам идет этот наряд!"
    imgd 35310
    liam "Вы такая!.. Такая!.."
    # кладет руку на свою ширинку
    music Stealth_Groover
    imgf 35311
    betty "Я знаю, Лиам!"
    betty "Красивой женщине любой наряд к лицу!"
    sound Jump2
    imgd 35312
    betty "А теперь не мешайте мне!"
    betty "Можете вообще выйти отсюда, я вас позову, когда закончу."
    # он, продолжая теребить ширинку
    music Groove2_85
    imgd 35313
    liam "Я вам не буду мешать, Мэм."
    liam "Я останусь, чтобы помогать вам..."
    # с этими словами идет и садится на диван, пошло поглядывая на Бетти
    sound man_steps
    imgf 35314
    w
    # она с деловым видом начинает тереть журнальный столик напротив дивана, на котором лежат книги
    # он достает член и начинает ленико водить по стволу одной рукой
    music2 snd_scrub
    imgd 35316
    w
    imgf 35315
    liam "Как у вас хорошо получается, Мэм!"
    betty "Иначе и быть не могло у такой хорошей хозяйки, как я!"
    imgd 35317
    liam "Да, я вижу, что вы просто отличная хозяйка, Мэм!"
    imgd 35318
    betty "Да, это так!"
    liam "Протрите еще с той стороны стол, Мэм." # указывает другой рукой
    liam "Вам нужно нагнуться немного, иначе вы не дотянетесь."
    betty "!!!" # Бетти делает, при этом сверкая попой
    imgf 35319
    w
    imgd 35320
    w
    music2 stop
    imgd 35321
    w
    imgf 35330
    w
    sound drkanje5
    imgd 35329
    w
    sound drkanje5
    imgd 35330
    w
    sound drkanje5
    imgd 35329
    w
    sound drkanje5
    imgd 35330
    w
    sound drkanje5
    imgd 35329
    w
    # потом Бетти начинает протирать шкаф, где стоит телек
    # Лиам также сидит на диване, лениво подрачивая
    fadeblack
    sound highheels_short_walk
    pause 2.0
    music Groove2_85
    music2 snd_scrub
    imgfl 35322
    w
    imgf 35323
    liam "О, как чисто становится, Мэм..."
    liam "У вас и правда очень умелые ручки!"
    liam "Вон там еще протрите, Мэм."
    music2 stop
    imgd 35324
    betty "Лиам, я лучше знаю!.." # поворачиваясь к нему
    # замолкает, увидев член
    music stop
    sound plastinka1b
    img 35325 vpunch
    betty "!!!"
    # отворачивается и указывает рукой
    music Hidden_Agenda
    imgf 35323
    betty "Здесь?"
    liam "Немного правее..."
    imgd 35326
    betty "Здесь?" # указывает в другое место
    liam "Ниже, Мэм..."
    imgd 35327
    liam "Да, здесь."
    music2 snd_scrub
    imgf 35328
    liam "Вот теперь идеально чисто, Мэм!"
    imgd 35329
    w
    sound drkanje5
    imgd 35330
    w
    sound drkanje5
    imgd 35329
    w
    sound drkanje5
    imgd 35330
    w
    music2 stop
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    # Бетти идет к столу, на котором утюг, и начинает протирать его
    # Лиам продолжает командовать, сидя на диване
    imgfl 35331
    w
    sound highheels_short_walk
    imgf 35332
    w
    imgd 35333
    liam "Мэм, мне кажется, что лучше сначала помыть пол."
    # Бетти косится на его член и ворчит, продолжая убираться
    sound Jump1
    img 35334
    betty "Лиам, я сама знаю, как лучше убираться!"
    imgf 35335
    music2 snd_scrub
    w
    imgd 35336
    w
    imgd 35335
    w
    imgd 35336
    w
    music2 stop
    imgf 35334
    betty "Вы думаете, если у меня есть горничная, то я ничего не умею?"
    liam "Я так не думаю, Мэм..."
    liam "Я вижу, что в ваших умелых ручках любая работа получается на отлично!"
    betty "Да, Лиам!"
    # он указывает рукой на подоконник
    sound vjuh3
    imgd 35337
    liam "Мэм, вы вот здесь еще не протирали пыль."
    betty "Где?"
    liam "Вот здесь..."
    # она, поглядывая на его член, идет к подоконнику
    # упирается коленом на диван, наклоняется и протирает подоконник
    # продолжая при этом ворчать
    fadeblack 1.5
    music Stealth_Groover
    sound2 highheels_short_walk
    imgfl 35338
    w
    imgf 35339
    w
    imgd 35340
    w
    imgf 35341
    betty "И вообще!"
    betty "С такой некомпетентной горничной, как у меня..."
    imgd 35342
    betty "Которая вообще ничего не умеет делать..."
    betty "Мне приходится самой выполнять всю работу по дому!"
    music2 snd_scrub
    imgf 35343
    liam "Как я вас понимаю, Мэм..."
    liam "Наверное, тяжело содержать в порядке такой огромный дом, как у вас?"
    imgd 35344
    betty "Конечно, это непросто, Лиам!"
    imgf 35345
    betty "Вы хоть представляете, сколько там работы?!"
    # он указывает рукой на пол
    sound vjuh3
    imgd 35346
    liam "Осталось вымыть пол, Мэм."
    music2 stop
    # она, продолжая ворчать, встает на четвереньки и начинает тереть губкой пол
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    imgf 35347
    betty "Я сама закупаю продукты, убираюсь и стираю!.."
    sound Jump2
    img 35348 vpunch
    betty "Сама готовлю еду для своего мужа!.."
    # он довольно рассматривает ее и продолжает дрочить
    imgf 35329
    w
    sound drkanje5
    imgd 35330
    w
    sound drkanje5
    imgd 35329
    w
    sound drkanje5
    imgd 35330
    w
    imgf 35349
    liam "Вы еще и готовить умеете, Мэм?!"
    sound vjuh3
    imgd 35350
    music2 snd_scrub
    betty "Конечно, я умею готовить!"
    betty "И очень вкусно!"
    liam "Без сомнения, Мэм! У вас просто золотые ручки!"
    liam "Как же повезло вашему мужу!"
    imgf 35351
    betty "Да, ему очень повезло с такой женой, как я!"
    imgd 35352
    betty "Я красивая, умная..."
    imgf 35353
    w
    imgd 35354
    w
    imgd 35353
    w
    imgd 35354
    betty "Хозяйственная..."
    imgf 35355
    liam "Заботливая и порядочная."
    betty "Да. И еще верная!"
    liam "Да, Мэм!"
    sound Jump1
    img 35356 hpunch
    liam "Вы не протерли пол еще вон там." # указывает рукой
    music2 stop
    # Бетти смотрит на него, потом на член
    imgf 35357
    betty "Я сейчас все протру, Лиам."
    # переползает на другое место и начинает тереть там, он дрочит
    imgd 35329
    w
    sound drkanje5
    imgd 35330
    w
    sound drkanje5
    imgd 35329
    w
    sound drkanje5
    imgd 35330
    w
    fadeblack 1.5
    music Groove2_85
    music2 snd_scrub
    imgf 35358
    liam "Вы уже почти закончили, Мэм?"
    betty "Да, осталось немного."
    liam "Видите, как хорошо, что я позаботился о вашем платье?"
    liam "Сейчас оно, наверняка, испачкалось бы."
    imgd 35359
    liam "А вам так идет этот наряд, Мэм!"
    betty "Да, Лиам. Я знаю."
    music Hidden_Agenda
    liam "Мне уже не терпится отблагодарить вас, Мэм, за вашу помощь..."
    # она косится на его член
    music2 stop
    sound vjuh3
    imgf 35360
    betty "Мне не нужна никакая благодарность, Лиам!"
    betty "Я согласилась вам помочь, потому что я хорошая соседка!"
    imgd 35361
    liam "Вы самая лучшая соседка, Мэм!"
    imgd 35362
    betty "Да, я такая!"
    sound highheels_short_walk
    imgf 35363
    liam "Мэм, вы же не откажетесь мне помочь с уборкой в следующий раз?"
    betty "Лиам! Вы же знаете, какая я занятая женщина!"
    betty "Вы думаете, что..."
    img 35364
    liam "Я буду вам очень-очень благодарен!"
    liam "Такая замечательная женщина, как вы, не откажет мне, вашему хорошему соседу."
    # она смотрит на него, он дрочит
    # Бетти залипает на его член, смотрит, как загипнотизированная
    music Groove2_85
    imgf 35365
    w
    imgd 35340
    betty "Лиам..."
    imgf 35366
    liam "Мэм так отлично справилась с уборкой."
    liam "Я и мечтать не мог о такой чистоте в своем доме!"
    liam "Сразу видна рука прекрасной хозяйки!"
    music Hidden_Agenda
    imgd 35367
    liam "Посмотрите, Мэм, насколько я впечатлен вашей работой..."
    betty "Я..."
    liam "Вы не поймете, пока не потрогаете его." # указывает на свой член
    # Бетти очухивается от гипноза
    imgf 35368
    w
    sound Jump2
    img 35369 vpunch
    betty "Вы же знаете, что я порядочная женщина!"
    betty "Я не изменяю своему мужу!"
    imgf 35370
    betty "Как вы можете предлагать мне прикасаться к вашему?.."
    liam "Ну вы же просто потрогаете, чтобы понять, насколько я вам благодарен..."
    liam "Разве это измена, Мэм?"
    # Бетти снова залипает на члене соседа
    music Loved_Up
    sound2 Jump2
    img 35371 hpunch
    betty "..."
    liam "Просто потрогайте его..."
    imgd 35372
    w
    fadeblack
    sound highheels_short_walk
    pause 1.5
    music Loved_Up
    imgfl 35373
    w
    img black_screen
    music stop
    pause 1.0
    music v_Betty_Neighbour_Blowjob2_1
    pause 4.0
    music stop
    pause 2.0
    # Бетти встает с пола и подходит к нему
    # показываем, как она с желанием смотрит на член
    # потом она протягивает руку и обхватывает член
    # затемнение, ритмичные звуки минета и охи на темном фоне
    return
