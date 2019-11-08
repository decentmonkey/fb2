default dialogue_classmate_5_flag = False
default dialogue_classmate_7_flag = False

# Дом. Комната Барди. Барди и Эрик (одноклассник).
label dialogue_classmate_1:
    # Эрик сидит за столом, Барди стоит рядом. Барди с самодовольной улыбкой, Эрик внимательно рассматривает фото, где Моника с Бетти с задранными юбками
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_41
    scene black_screen
    with Dissolve(1)
    music Sneaky_Snitch
    if monicaMadeDoublePhotoBetty == True:
        img 15244
    else:
        img 22284
    with fadelong
    w
    img 15245
    eric "Не может быть, что они тебя слушаются и делают все, что ты им скажешь."
    if monicaMadeDoublePhotoBetty == True:
        img 15246
    else:
        img 22285
    with diss
    eric "Это не ты делал эту фотографию!"
    # Барди удивленно смотрит на друга
    music Groove2_85
    img 15247
    with fade
    bardie "В смысле?! Ты мне не веришь, чувак? А кто еще мог сделать эту фотку?"
    # Эрик, продолжая пялиться на фотку в ноуте Барди
    img 15248
    with diss
    eric "Откуда я знаю? Может, ты переслал ее с телефона своего отца, а мне говоришь, что ты фотографировал."
    img 15249
    with diss
    bardie "Да Бетти его скорее выгонит из дома, чем позволит сделать такую фотку!"
    if monicaMadeDoublePhotoBetty == True:
        img 15250
    else:
        img 22286
    with fade
    eric "Ага. И ты командуешь двумя взрослыми женщинами... Так я тебе и поверил!"
    img 15251
    with diss
    eric "..."
    img 15252
    bardie "!!!"
    bardie "Я тебе сейчас докажу, что они слушаются именно меня!"
    # Эрик смотрит на него вопросительно, Барди кричит с выражением лица а-ля "хозяин дома"
    img 15253
    with diss
    bardie "Гувернантка! Гувернантка!!!"
    return

label dialogue_classmate_1d:
    call dialogue_classmate_2a() from _call_dialogue_classmate_2a
    $ dialogue_classmate_1b_flag = True
    $ autorun_to_object("dialogue_classmate_1b", scene="basement_bedroom2")
    call refresh_scene_fade() from _call_refresh_scene_fade_183
    return

label dialogue_classmate_1b:
    if day_time == "evening":
        bardie "Гувернантка! Гувернантка!!!"
        mt "Меня зовет эта малявка Барди!"
        mt "Надо {c}идти к нему в комнату{/c}..."
    return

label dialogue_classmate_1c:
    mt "Меня зовет эта малявка Барди!"
    mt "Надо {c}идти к нему в комнату{/c}..."
    return False

label dialogue_classmate_1a:
    music stop
    img black_screen
    with diss
    pause 2.0
    # через несколько минут Моника заходит к нему в комнату, смотрит на Эрика, тот заинтересованно смотрит на нее
    music Groove2_85
    img 15254
    with fadelong
    mt "Этот малявка привел в дом еще одного такого же озабоченного мелкого извращенца, как он сам."
    # переводит взгляд на Барди
    img 15255
    with diss
    m "Да? Ты звал меня?"
    # Барди с серьезным лицом говорит Монике
    img 15256
    bardie "Гувернантка, мне надо проверить, соблюдаешь ли ты правила этого дома!"
    music Power_Bots_Loop
    img 15257
    with hpunch
    m "Что, прямо сейчас? При твоем друге?!" # удивленно
    m "???"
    # Барди все с такой же серьезной миной
    music Groove2_85
    img 15258
    with fade
    bardie "Да, мне нужно проверить прямо сейчас, гувернантка."
    # Моника зло
    img 15259
    with diss
    m "В мои обязанности это не входит! Я не собираюсь проходить эту проверку при твоем друге!"
    m "!!!"
    # Барди с угрозой
    img 15260
    with fade
    bardie "Если ты хорошая гувернантка и соблюдаешь правила, то делай, что тебе говорят!"
    img 15261
    with diss
    m "..."
    img 15262
    with fade
    bardie "Или ты отказываешься и хочешь, чтобы я тебя наказал?"
    # Моника злится, но молчит
    img 15263
    with diss
    mt "!!!"
    mt "Ненавижу эту малявку!"
    img 15264
    with fade
    bardie "Ну? Я долго должен ждать?"
    if monicaUnder != "Nude":
        img 15265
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        img 15266
        with fade
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        music stop
        img black_screen
        with diss
        sound highheels_run2
        pause 2.0
        return False
    img 15267
    with diss
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            img 15266
            with fade
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            music stop
            img black_screen
            with diss
            sound highheels_run2
            pause 2.0
            return False
    # Моника с недовольным лицом задирает юбку, Эрик сидит офигевший и пялится на нее, Барди самодовольно ему говорит
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15268
    with fadelong
    w
    img 15270
    with diss
    bardie "Ну что? Теперь ты убедился, что я не врал?"
    img 15269
    with diss
    eric "..."
    music Groove2_85
    img 15271
    with fade
    bardie "Я выиграл спор! С тебя домашка на месяц вперед!"
    # Моника опускает юбку, недовольно смотрит на Барди
    img 15272
    with diss
    mt "Они спорили на домашку? Детский сад!"
    mt "Теперь он, наконец, отвяжется от меня?"
    # Эрик продолжает пялиться на Монику
    img 15273
    with fade
    eric "Н-нет..."
    # Барди и Моника вопросительно смотрят на Эрика
    img 15274
    with diss
    bardie "Что 'нет'? Мы с тобой договаривались!"
    img 15275
    with fade
    eric "Я... Хм... Спор не выигран."
    eric "Потому что я... Я не рассмотрел..."
    img 15276
    with diss
    m "Что значит 'не рассмотрел'?! Я все сделала, как сказал Барди."
    # Эрик смотрит на юбку Моники, но обращается к Барди
    img 15277
    with fade
    eric "Если твоя гувернантка задерет юбку еще раз и... даст посмотреть поближе, тогда я буду делать тебе домашку 2 месяца."
    # Моника офигевает
    music Power_Bots_Loop
    img 15278
    with hpunch
    mt "!!!"
    mt "Эти две малявки спорят на какую-то глупость! А я должна тут стоять перед ними полуголая!!!"
    # Барди поворачивается к Монике и смотрит вопросительно, Моника смотрит на него зло, но ничего не делает
    music Groove2_85
    img 15279
    with fade
    bardie "Чего ты ждешь, гувернантка? Ты не слышала что-ли? Подойди поближе к нам и подними юбку еще раз!"
    img 15272
    with diss
    mt "Ненавижу эту малявку! И его озабоченного друга!"
    mt "Если я этого не сделаю, он не отвяжется от меня."
    img 15280
    with fade
    bardie "Я жду."
    # Моника подходит ближе к  Эрику, и снова задирает юбку, Эрик с тупым выражением лица пялится на ее киску
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Loved_Up
    img 15281
    with fadelong
    w
    img 15282
    with diss
    w
    img 15283
    with diss
    eric "Я... Я вообще ничего не могу рассмотреть."
    # Барди смотрит на Монику, Моника взглядом готова убить Эрика
    img 15284
    with fade
    bardie "Гувернантка, расставь ноги шире!"
    # Моника зло смотрит на него, но подчиняется и ставит ноги шире
    img 15285
    mt "!!!"
    # Моника снова испепеляет взглядом Эрика, а он пристально разглядывает
    img 15286
    with fade
    w
    img 15287
    with diss
    w
    img 15288
    with diss
    w
    music Groove2_85
    img 15289
    with fade
    eric "Я хочу увидеть еще ближе. Пусть твоя гувернантка сядет на кровать. Тогда я смогу все рассмотреть."
    # Моника злится
    img 15291
    m "!!!"
    img 15290
    with diss
    menu:
        "Сесть на кровать.":
            pass
        "Отказаться. Эти малявки совсем обнаглели!":
            music Power_Bots_Loop
            img 15292
            with fade
            m "Я не буду этого делать! Все итак слишком далеко зашло!!!"
            # Барди угрожающе
            img 15293
            with diss
            bardie "Гувернантка не хочет быть хорошей? Она забыла, что может сделать хозяин, если она не будет слушаться его?"
            img 15272
            with diss
            mt "Черт!"
            img 15294
            with diss
            m "..."
            music Groove2_85
#            return 1
    # Моника садится на край кровати, а Барди и Эрик смотрят на нее
#    img 15295
    music stop
    img black_screen
    with diss
    pause 1.5
    music Groove2_85
    img 22048
    with fadelong
    w
    img 22049
    with diss
#    img 15296
    bardie "Подними юбку."
    # Моника слушается
#    img 15297
    img 22050
    with diss
    m "!!!"
#    img 15298
    sound snd_fabric1
    img 22051
    with diss
    w
    img 22052
    with diss
    w
    img 22053
    with diss
    bardie "Раздвинь ноги."
    img 22054
    w
    # Моника раздвигает их, совсем немного
    img 22055
    with fade
    w
    img 22056
    with diss
    w
    img 22057
    with diss
    w
    img 22058
    with fade
    w
    img 22059
    with diss
    bardie "Eще шире! Ему же ничего не видно так."
    # Барди с Эриком внимательно смотрят, Моника подчиняется
    img 22060
    mt "Я когда-нибудь задушу эту мерзкую малявку! И почему он прицепился именно ко мне, а не к Бетти?!"
    img 22061
    with diss
    mt "!!!"
    img 22062
    with fade
    w
    img 22063
    with diss
    w
    # Эрик наклоняется над кроватью близко от киски Моники и разглядывает ее в упор
    sound Jump1
    img 22064
    with diss
    w
    img 22065
    with diss
    w
    m "!!!"
    music Loved_Up
    img 22066
    with fade
    eric "Чувак, я видел в порно, как лижут киски и всегда хотел попробовать. Ты же не против?"
    # Барди удивленно смотрит на него
    img 22067
    with diss
    bardie "???"
    music Groove2_85
    img 22068
    with fade
    bardie "Окей."
    # Моника возмущается
    img 22069
    with diss
    m "Какого черта?! А меня ты не хочешь спросить? Я не хочу, чтобы ты ко мне прикасался!"
    # Барди, смотря не на нее, а на киску
    img 22070
    with fade
    bardie "Он только потрогает языком и не будет больше ничего делать."
    bardie "Зато за хозяина будут делать домашние задания целых два месяца."
    img 22071
    with diss
    bardie "Хорошая гувернантка должна быть рада пойти на такие маленькие жертвы ради своего хозяина."
    img 22072
    with fade
    mt "Какой ужас! Мне что, приходится раздвигать ноги перед кем-то ради домашних заданий этого сопляка?"
    mt "Мне?! Монике Бакфетт! Самой богатой и влиятельной женщине этого города!"

    # Моника негодует, но продолжает сидеть с развинутыми ногами
    music Power_Bots_Loop
    img 22073
    with hpunch
    m "Только попробуй коснуться меня там пальцами или чем-либо еще!"
    m "!!!"
    music Groove2_85
    img 22074
    with fade
    bardie "Да, Эрик! Не трогай ее там пальцами или чем-то еще. Это МОЯ гувернантка."
    bardie "Не забывай это!"
    # Эрик все это время глаз не отводит от ее киски
    music Loved_Up
    img 22075
    with diss
    eric "..."
    # лицо Эрика все ближе к киске Моники, на лице Моники отвращение
    music Groove2_85
    img 22076
    with fade
    mt "Фу, как это мерзко! Но если я не послушаюсь Барди..."
    mt "Я тогда остановила его прямо в полиции. Еще несколько минут и он был бы у Маркуса."
    mt "Боже! Даже боюсь думать о последствиях."
    mt "У меня сейчас нет другого выхода, кроме того, как перетерпеть эту мерзость."
    # Эрик высовывает свой язык и касается им киски Моники
#    music Loved_Up
    #видео erick licking monica
    music v_Monica_Eric_Licking_1_1
    img 22079
    with diss
    w
    img 22077
    with diss
    w
    img 22078
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Licking_1_1 = Movie(play="video/v_Monica_Eric_Licking_1_1.mkv", fps=30)
    show videov_Monica_Eric_Licking_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Licking_1_2 = Movie(play="video/v_Monica_Eric_Licking_1_2.mkv", fps=30)
    show videov_Monica_Eric_Licking_1_2
    with fadelong
    wclean
#    music v_Monica_Eric_Licking_1_1
    img 22080
    with diss
    w
    img 22082
    with diss
    w
    img 22081
    with diss
    mt "По крайней мере, это не так неприятно как я думала."
    mt "Но это все-равно отвратительно!"
    mt "Когда же он уже закончит все это?!"
    music Groove2_85
    img 22083
    with fade
    bardie "Эй, чувак! У нас точно все в силе? Ты мне будешь делать домашку?"
    music Turbo_Tornado
    img 22084
    with diss
    eric "Да буду, буду!"
    # тут Эрик присасывается к Монике, Барди в шоке смотрит на это
    sound Jump2
    #sound звук эрик присосался к Монике
    img 22085 # присосался
    with hpunch
    w
    img 22086
    with diss
    m "!!!"
    img 22087
    with diss
    bardie "Эй-эй, чувак. Полегче..."
    # Эрик делает еще несколько движений языком и поворачивается к Барди
    img 22088
    with fade
    eric "Лизать самому намного прикольнее, чем просто смотреть на это!"
    eric "А ты пробовал?"
    img 22089
    with diss
    bardie "Не, даже не думал об этом."
    img 22090
    with fade
    eric "Давай, чувак, попробуй."
    img 22091
    with diss
    bardie "Прямо сейчас?"
    eric "Ага. Это правда прикольно."
    # Барди смотрит на Монику, та на него смотрит испепеляющим взглядом, но молчит
    img 22092
    with diss
    bardie "..."
    img 22093
    with diss
    m "!!!"
    img 22095
    with diss
    w
    sound plastinka1b
    music stop
    img 22094
    with diss
    m "!!!"
    # Эрик отстраняется от Моники, Барди наклоняется к ней
    music Sneaky_Snitch
    img 22096
    with fade
    bardie_t "Хм. Надо хотя бы разочек попробовать, каково это лизать киску."
    img 22097
    with diss
    bardie_t "..."
    # наклоняется еще ближе и проводит языком, лицо Эрика совсем близко и когда Барди останавливается и поднимает голову, то тоже проводит языком
    music Groove2_85
    img 22098
    with fade
    bardie "Хорошая гувернантка поднимает юбку!"
    sound Jump1
    img 22099
    with diss
    w
    img 22100
    with diss
    w
    img 22101
    m "!!!"
    img 22102
    with fade
    bardie "Плохая гувернантка будет наказана штрафом..."
    menu:
        "Сделать что говорит Барди.":
            pass
    img 22103
    with diss
    mt "Какой кошмар! Что эти озабоченные малявки творят?!"
    sound snd_fabric1
    img 22104
    with fade
    mt "Что вообще у них в голове творится? Как можно было до такого додуматься?"
    img 22105
    with diss
    w
    mt "!!!"
    img 22106
    with diss
    w
    mt "Почему я должна это терпеть?!"
    music stop
    img black_screen
    with diss
    pause 1.5
#    music Loved_Up
    music v_Monica_Eric_Bardie_Licking_1_1
    img 22107
    with fadelong
    w
    #видео monica eric bardie licking
    img 22108
    with diss
    mt "Черт! Как же щекотно..."
    img 22109
    with diss
    w
    img 22110
    with diss
    w
    img 22111
    with diss
    w
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Bardie_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Bardie_Licking_1_1 = Movie(play="video/v_Monica_Eric_Bardie_Licking_1_1.mkv", fps=30)
    show videov_Monica_Eric_Bardie_Licking_1_1
    with fadelong
    wclean
    img black_screen
    with diss
    music stop
    stop music
    play music "<from " + str((float(rand(1,3))*1.66666)) + " loop 0.0>Sounds/v_Monica_Eric_Bardie_Licking_1_1.ogg"
    scene black
    image videov_Monica_Eric_Bardie_Licking_1_2 = Movie(play="video/v_Monica_Eric_Bardie_Licking_1_2.mkv", fps=30)
    show videov_Monica_Eric_Bardie_Licking_1_2
    with fadelong
    wclean
    music v_Monica_Eric_Bardie_Licking_1_1
    img 22112
    with diss
    mt "..."
    img 22113
    with diss
    w
    img 22114
    with diss
    sound ahhh11
    mt "Странные ощущения какие-то..."
    img 22115
    with diss
    w

    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up2
    img 22116
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    eric "Ааааааа..."

    sound bulk1
    img 22117
    sound man_moan6
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    eric "Ааааааахххх!!!"
    # парни в это время продолжают лизать, сначала один, потом его сменяет другой. Эрик достает свой член из штанов
    # Эрик смотрит, как лижет Барди, проводит по своему члену рукой пару раз и кончает
    # Барди видит это и делает то же самое со своим членом, и кончает на живот Моники
    img 22118
    with diss
    m "Эй, что ты делаешь?! Фуууу!!!"
    img 22120
    with diss
    m "Не смей!"
    sound bulk1
    img 22119 # звук кончания
    sound man_moan1
    show screen photoshot_screen()
    with hpunch
    pause 0.7
    hide screen photoshot_screen
    w
    #sound звук спермы на живот
    sound hlup2
    img 22121 # прилетает сперма Монике на живот
    with diss
    w
    img 22122
    with diss
    mt "!!!"
    # Моника сдвигает ноги и опускает юбку
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 22123
    with fadelong
    mt "Наконец-то, это закончилось!"
    # вопросительно смотрит на Барди, тот расслаблен и доволен
    img 22124
    with diss
    bardie "Гувернантка хорошая. Гувернантка помогла хозяину выиграть спор."
    img 22125
    mt "!!!"
    # смотрит на Эрика
    img 22126
    with fade
    bardie "Эй, чувак, что там с домашкой?"
    # Эрик тоже расслаблен и доволен
    eric "Окей. Ты выиграл два месяца домашки."
    # Барди радостный, поворачивается к Монике
    sound highheels_run2
    img 22127
    with diss
    bardie "Можешь идти, гувернантка. На сегодня ты свободна."
    music stop
    img black_screen
    with diss
    pause 1.5
    return True

label dialogue_classmate_1b1:
    # Моника встает с кровати, поправляет юбку
    mt "Что же за странные такие ощущения у меня были? Не понимаю..."
    mt "Это, наверное, связано с нервным срывом из-за всего, что присходит в последнее время."
    mt "Мне нужно обратиться к хорошему психотерапевту..."
    mt "Когда весь этот кошмар закончится..."
    # Моника уходит
    return True

# Дом. Второй этаж. Моника пытается зайти в комнату Барди после квеста.
label dialogue_classmate_1_1:
    mt "Я не собираюсь заходить к этой малявке! Сейчас снова пристанет со своими глупостями!"
    return False

# Дом. Второй этаж. Барди зовет Монику.
label dialogue_classmate_1_2:
    bardie "Гувернантка! Гувернантка!!!"
    return

# Дом. Комната Барди. Барди, Моника и Эрик.
label dialogue_classmate_2a:
    music stop
    img black_screen
    with diss
    pause 1.5
    music Sneaky_Snitch
    img 15180
    with fadelong
    bardie "Гувернантка! Гувернантка!!!"
    return

label dialogue_classmate_2:
    # Барди стоит в своей комнате, Эрик валяется на его кровати, Барди орет
    music Sneaky_Snitch
    img 15180
    with hpunch
    bardie "Гувернантка! Гувернантка!!!"
    # спустя несколько минут Моника заходит к нему в комнату
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Groove2_85
    img 15182
    with fade
    m "Что случилось? Зачем так кричать?"
    # Барди ей с улыбочкой
    img 15181
    with diss
    bardie "Гувернантка, смотри, кто пришел. Эрику понравилось у нас в гостях."
    bardie "Аха-ха!"
    # Моника поворачивается и видит Эрика
    music Power_Bots_Loop
    img 15183
    with fade
    mt "Ну что за мелкие извращенцы! Опять, как в прошлый раз?"
    mt "И долго все это будет продолжаться"
    # Барди с улыбочкой, Эрик все это время смотрит на нее
    music Groove2_85
    img 15184
    with diss
    bardie "Гувернантка, я хочу проверить, придерживаешься ли ты правил этого дома."
    if monicaUnder != "Nude":
        img 15185
        with fade
        mt "Черт!!! Я в трусиках. Он снова накажет меня!"
        mt "Хотя... Что он мне сделает? Я же послушаю его приказа поднять юбку." #поднимает юбку с трусиками, с вызовом на него смотрит
        # Барди с угрозой
        music stop
        img black_screen
        with diss
        sound snd_fabric1
        pause 1.5
        music Loved_Up
        if monicaBettyPanties == False:
            img 15186
        else:
            if monicaBettyPantiesId == 1:
                img 15239
            if monicaBettyPantiesId == 2:
                img 15240
            if monicaBettyPantiesId == 3:
                img 15241
            if monicaBettyPantiesId == 4:
                img 15242
            if monicaBettyPantiesId == 5:
                img 15243
        with fadelong
        w
        img 15187
        with diss
        bardie "Ты плохая гувернантка!"
        bardie "В качестве наказания гувернантке нужно будет кое-что сделать для хозяина."
    else:
        img 15188
        with diss
        menu:
            "Сделать, как требует Барди.":
                # Поднимает юбку без трусиков
                # Барди с довольным лицом
                music stop
                img black_screen
                with diss
                sound snd_fabric1
                pause 1.5
                music Loved_Up
                img 15193
                with fadelong
                w
                img 15194
                with diss
                w
                img 15195
                with diss
                bardie "Хорошая гувернантка. Именно поэтому у меня есть к гувернантке серьезное задание."
                pass
            "Отказаться. Эти малявки совсем обнаглели!":
                music Power_Bots_Loop
                img 15189
                with fade
                m "Я не буду этого делать! Тем более при твоем друге!"
                # Барди угрожающе
                music Groove2_85
                img 15190
                with diss
                bardie "Гувернантка не хочет быть хорошей?"
                bardie "Она забыла, что может сделать хозяин, если она не будет слушаться его?"
                img 15192
                with fade
                mt "Черт!"
                img 15191
                with diss
                m "..."
                # Поднимает юбку без трусиков
                # Барди с довольным лицом
                music stop
                img black_screen
                with diss
                sound snd_fabric1
                pause 1.5
                music Loved_Up
                img 15193
                with fadelong
                w
                img 15194
                with diss
                w
                img 15195
                with diss
                bardie "Хорошая гувернантка. Именно поэтому у меня есть к гувернантке серьезное задание."
                pass
    # Моника опускает юбку и смотрит на него с подозрением
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 1.5
    music Groove2_85
    img 15196
    with fadelong
    m "???"
    img 15183
    with diss
    mt "Что еще он придумал?"
    mt "Хотя, от этих двух озабоченных можно ожидать только одного..."
    # Барди с улыбочкой
    music Sneaky_Snitch
    img 15197
    with fade
    bardie "Эрику нужна мама."
    # Моника в шоке, смотрит на Эрика вопросительно, потом снова на Барди
    music Power_Bots_Loop
    img 15198
    with hpunch
    m "Что значит 'нужна мама'? И причем здесь Я?!"
    img 15199
    with diss
    bardie "Ты будешь его мамой!"
    # Моника ошарашена
    img 15200
    with fade
    m "И как это понимать?"
    music Sneaky_Snitch
    img 15201
    with diss
    bardie "У Эрика небольшая проблема с учительницей по плаванию. Это дошло до классного руководителя."
    bardie "Он вызывает родителей Эрика в колледж, но им нельзя туда идти."
    img 15202
    with fade
    m "???"
    m "Почему это его родителям нельзя идти к его учителю?"
    m "И, вообще, какое мне дело до этого!"
    img 15203
    with diss
    w
    img 15204
    with diss
    bardie "Ты должна притвориться мамой Эрика и пойти поговорить с классным руководителем."
    bardie "Его родителям нельзя, так как тема очень деликатная."
    bardie "Эрик не хотел бы, что бы его родители узнали, что он сделал."
    # Моника поворачивается к Эрику и
    music Groove2_85
    img 15205
    with fade
    m "Что ты там натворил? Почему твоим родителям нельзя об этом знать?"
    # Эрик опускает взгляд
    img 15206
    with diss
    eric "Нуууу... Я... Как сказать..."
    eric "..."
    # Моника снова поворачивается к Барди
    img 15207
    with fade
    m "Как ты себе это представляешь? С чего это вдруг я должна идти в колледж и обманывать преподавателя?"
    img 15208
    with diss
    bardie "Никто ничего не заподозрит, гувернантка. Этот учитель у нас совсем недавно, но с ним можно договориться."
    img 15209
    with fade
    m "???"
    music Sneaky_Snitch
    img 15210
    with diss
    bardie "У Бетти получилось решить с ним очень сложный вопрос. У тебя тем более получится решить эту маленькую проблемку Эрика."
    # Моника смотрит на него, как на придурка
    music Power_Bots_Loop
    img 15211
    with hpunch
    m "Я никуда не собираюсь идти! Все это глупости!"
    # Барди с лицом а-ля хозяин дома отдает приказ
    img 15212
    with fade
    bardie "Это не просьба, гувернантка! Это приказ хозяина дома."
    bardie "А спорить с хозяином, тем более при гостях, тебе запрещено!"
    # Моника зло
    img 15213
    with diss
    m "Я работаю здесь просто гувернанткой! Быть чьей-то мамой я не нанималась!"
    m "Я не знаю, как и что делать! И вообще, я не похожа на чью-либо маму!"
    img 15214
    m "!!!"
    # Барди ей с улыбочкой
    music Sneaky_Snitch
    img 15215
    with fade
    bardie "Бетти тоже не знала, но разобралась на месте. И ты разберешься, гувернантка."
    bardie "А вот насчет того, что непохожа на маму - это да. Нужно платье нормальное."
    img 15216
    with diss
    bardie "Ты должна идти не в униформе гувернантки."
    bardie "У тебя хорошая униформа и мне она нравится. Хотя, я думаю, что твоя униформа тебе не очень удобна."
    img 15217
    with fade
    m "Чем это она неудобна?"
    music Groove2_85
    img 15218
    with diss
    bardie "В этой униформе гувернантке приходится делать лишние движения... чтобы показать, что она соблюдает правила дома."
    bardie "А хозяину и без лишних движений должно быть видно, насколько ты хорошая гувернантка."
    # Моника зло на него смотрит
    img 15219
    with fade
    m "Мне есть, что надеть, кроме этой дурацкой униформы!"
    # Барди издевательски смеется
    img 15220
    with diss
    bardie "Какая у тебя одежда? Та, в которой ты пришла на работу к нам устраиваться?"
    bardie "Аха-ха-ха!!!"
    bardie "Учитель подумает, что ты какая-нибудь разносчица флаеров или продавщица кебабов."
    #
    if monicaHasCasualDress1 == True:
        img 15221
        with diss
        bardie "Или то красное платье, в котором ты незаметно пробираешься в дом изо дня в день?"
    #
    img 15222
    with diss
    bardie "Аха-ха!!!"
    img 15223
    with fade
    mt "!!!"
    # Моника злится
    img 15224
    with diss
    bardie "Ты должна выглядеть, как Бетти. Нужно платье, похожее на ее наряд."
    # Моника пренебрежительно
    music Groove2_85
    img 15225
    with fade
    m "Я никогда не буду носить такую дурацкую одежду, как у Бетти!"
    img 15226
    with diss
    mt "Фи! Провинциалка!"
    music Sneaky_Snitch
    img 15227
    with diss
    bardie "Тогда гувернантка должна купить себе такое платье. Встретиться с учителем нужно чем быстрее, тем лучше."
    sound Jump1
    img 14581
    with diss
    w
    img 15228
    with fade
    m "..."
    img 15229
    with diss
    bardie "Гувернантка должна внимательно его выслушать и извиниться за Эрика."
    bardie "Потом сказать, что ты обязательно поговоришь с сыном и такого больше не повторится."
    img 15230
    with fade
    m "..."
    img 15231
    with diss
    bardie "Если учитель попросит тебя что-нибудь сделать для нужд класса, то соглашайся. Это поможет Эрику избежать наказания."
    # Моника недовольно
    music Groove2_85
    img 15232
    with fade
    m "С чего бы это я должна буду еще что-то делать?"
    img 15233
    with diss
    bardie "Потому что я тебе это сказал! И не спорь!"
    bardie "Если ты все хорошо сделаешь, то я, хозяин дома, буду очень доволен."
    bardie "Ты же хочешь, чтобы хозяин был доволен, гувернантка?"
    img 15234
    with diss
    bardie "И запомни, что для учителя ты - миссис Бейкер, а Эрик Бейкер - твой сын."
    bardie "Учителя зовут мистер Эдвардс. Все запомнила, гувернантка?"
    # Моника смотрит зло
    img 15228
    with fade
    m "..."
    img 15235
    with diss
    bardie "Теперь иди покупай платье."
    img 15236
    with fade
    m "У меня нет денег на платье!"
    img 15237
    with diss
    bardie "Не ври! Бетти говорит, что ты получаешь большую зарплату здесь. Так что найдешь несколько баксов, чтобы купить платье."
    bardie "Мы с Эриком будем ждать тебя здесь. Надеюсь, ты вернешься из колледжа с хорошими новостями."
    music Power_Bots_Loop
    img 15238
#    with fade
    mt "Ненавижу все эту семейку, которая поселилась в моем доме! И Я еще должна молча все это терпеть!"
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    # Моника смотрит на Барди зло и уходит
    return

# Дом. Второй этаж. Моника, выйдя из комнаты Барди.
label dialogue_classmate_2_1:
    # не рендерить!
    mt "Мне снова надо будет идти в этот чертов магазин, фи!"
    mt "Но лучше я сделаю, как хочет эта малявка Барди. Иначе он пойдет к Маркусу и расскажет, где я живу."
    mt "Боюсь даже думать о том, что он пришлет полицейских и они заберут меня... и снова посадят в эту камеру..."
    mt "!!!"
    mt "Мне надо скорее идти в магазин!"
    return

label dialogue_classmate_2_1a:
    mt "Мне лучше идти туда в уличной одежде, которая наиболее подходит для этого жуткого района..."
    return

# Город. Магазин одежды. Моника перед магазином одежды.
label dialogue_classmate_3:
    if cloth != "Whore":
        return
    $ remove_hook()
    # не рендерить!
    mt "В этот раз мне не составит труда подобрать себе платье... Ведь там полный магазин дурацкой одежды."
    # если Вивьен приставала е Монике
    mt "Надеюсь, эта лесбиянка не будет приставать ко мне. Как вспомню... Фу, это было так мерзко!"
    return

# Город. Магазин одежды. Моника в магазине.
label dialogue_classmate_3_1:
    # Моника заходит в магазин
#    mt "Я надену это платье всего один раз и выброшу."
#    mt "Как такое вообще можно носить? Ни одна леди себе такого не позволит."
#    mt "А я леди. Мне просто надо перетерпеть все эти временные трудности..."

    # Если Моника толкала Вивиен.
    if monicaKickedVivianForDress == True: # Моника ударила Вивиен
        mt "В прошлый раз я не очень-то поладила с продавцом этого магазина."
        mt "Стоит-ли мне рисковать заходить туда?"
        menu:
            "Зайти в магазин.":
                pass
            "Уйти":
                return 0

        mt "Черт... Надеюсь она меня не вспомнит..." # Если толкала Вивиен


    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    # Моника подходит к Вивьен, ведет себя высокомерно
    music Groove2_85
    img 22233
    with fadelong
    m "Я хочу купить обычную одежду, которую носят домохозяйки!"

    if monicaNeedToSellDress == False: # Моника не продавала платье манекеном
    # если Моника хорошо обращалась с Вивиан и не было сцен (покупала платье)
        img 22234
        with diss
        cashier "Здравствуйте! Да, конечно!"
        cashier "Пройдемте за мной."
        music stop
        img black_screen
        with diss
        sound highheels_run2
        pause 2.0
        music Groove2_85
        img 22236
        with fadelong
        cashier "Вот, пожалуйста..."
        if monicaKickedVivianForDress == True: # Моника ударила Вивиен
            mt "Кажется, она не помнит меня..."
            mt "Видимо я хорошо приложила эту дуру в прошлый раз..."
    else:
        # Если Моника толкала Вивиан
        if monicaKickedVivianForDress == True: # Моника ударила Вивиен
            mt "Кажется, она не помнит меня..."
            mt "Видимо я хорошо приложила эту дуру в прошлый раз..."
    #    cashier "Я сейчас вам принесу."
    #

    # если Моника работала манекеном
        sound highheels_short_walk
        img 22235
        with diss
        $ notif(_("Моника работала манекеном"))
        cashier "О, это ты? Хочешь 'купить' одежду, как в прошлый раз?"
        mt "На что эта лесбиянка намекает?"
        mt "???"

        music stop
        img black_screen
        with diss
        pause 2.0
        music Groove2_85
        img 22236
        with fadelong
        cashier "У меня есть подходящий костюм."
        sound highheels_short_walk
        img 22237
        with diss
        cashier "Можешь отработать этот костюм манекеном. У меня есть еще товар, который надо продать."
        music Loved_Up
        sound highheels_short_walk
        img 22238
        with fadelong
        cashier "Или могу предложить другой вариант."
        cashier "Я сделаю большую скидку, если ты мне сделаешь что-нибудь приятное."
        mt "..."
        #
    if clothShopCashierOffended2 == False and clothShopCashierOffended3ReturnDress == False and clothShopCashierFirstNightOffended == False:
        $ schoolOutfitPrice = monicaEricCollegeDressPriceDiscount
        $ notif(_("Моника вела себя с Вивиан вежливо."))
    else:
        $ schoolOutfitPrice = monicaEricCollegeDressPriceRegular
        $ notif(_("Моника была недостаточно добра к продавцу."))
    $ menu_price = [schoolOutfitPrice, 0, monicaEricCollegeDressPriceLickingDiscount]
    music Groove2_85
    menu:
        "Купить костюм.":
            # Вивьен оформляет покупку, отдает костюм с улыбкой, Моника держится высокомерно
            # Моника в примерочной меряет платье
            call dialogue_classmate_3_1_7() from _call_dialogue_classmate_3_1_7
            img black_screen
            with diss
            sound highheels_short_walk
            pause 1.5
#            music Road_Trip
            img 22269
            with fadelong
            m "Я беру его."
#            cashier "Пожалуйста, ваш костюм."

            # Если Моника вела себя хорошо с Вивиан
            img 22270
            if clothShopCashierOffended2 == False and clothShopCashierOffended3ReturnDress == False and clothShopCashierFirstNightOffended == False:
                $ notif(_("Моника вела себя с Вивиан вежливо."))
                cashier "Специально для Вас скидка 50 процентов."
            $ add_money(-schoolOutfitPrice)

            cashier "Приходите к нам еще. Мы всегда рады вас видеть."
            #
            m "Спасибо. Обязательно."
            return 1
        "Получить костюм бесплатно." if monicaNeedToSellDress == True:
            # если Моника работала манекеном
            mt "Я могу получить этот костюм бесплатно, если соглашусь работать манекеном."
            mt "Но у меня нет времени на это."
            mt "Малявка сказал, что чем быстрее я поговорю с учителем, тем лучше."
            mt "..."
            return 2
        "Получить скидку на костюм." if monicaNeedToSellDress == True:
            # если Моника работала манекеном
            pass

    # Моника подозрительно
    img 22239
    with diss
    mt "..."
    mt "Большая скидка? Хм."
    m "И что же я должна буду сделать?"

    # Вивьен с многозначительной улыбочкой
    music stop
    img black_screen
    with diss
    pause 2.0
    music Loved_Up
    img 22241
    with fadelong
    cashier "Я знала, что тебе понравится этот вариант."
    img 22242
    with diss
    mt "!!!"
    img 22243
    with fade
    cashier "Просто поцелуй мой животик."
    music Groove2_85
    img 22244
    with diss
    mt "???"
    img 22245
    with fade
    m "Просто поцеловать?"
    # Вивьен приподнимает топ, улыбается
    img 22246
    with diss
    mt "..."
    img 22247
    with fade
    mt "Фу! Она снова принуждает меня делать всякие мерзости."
    mt "!!!"
    img 22248
    with diss
    cashier "Да. Давай, просто сделай это и заберешь костюм со скидкой."
    # Моника с недовольным видом наклоняется и целует ее в живот, Вивьен довольно улыбается и приспускает шорты
    $ menu_corruption = [monicaVivianSchoolOutfitLick1]
    menu:
        "Поцеловать животик.":
            pass
        "Уйти.":
            m "Я не собираюсь продолжать это!"
            return 3
    sound highheels_short_walk
    music Loved_Up
    img 22249
    with fadelong
    w
    img 22250
    with diss
    w
    sound snd_kiss2
    img 22251
    with diss
    w
    sound snd_fabric1
    img 22252
    with fade
    cashier "Давай, еще один разочек немного ниже."
    music Groove2_85
    img 22253
    with diss
    m "Ты говорила про один поцелуй!" #возмущенно
    cashier "Я не уточнила сколько раз нужно поцеловать мой животик."
    img 22254
    with diss
    mt "!!!"
    $ menu_corruption = [monicaVivianSchoolOutfitLick2]
    menu:
        "Поцеловать животик ниже.":
            pass
        "Уйти.":
            m "Я не собираюсь продолжать это!"
            return 3
    # Моника снова с отвращением целует ее живот, Вивьен еще ниже приспускает шорты
    music Loved_Up
    sound snd_kiss2
    img 22255
    with diss
    w
    #sound звук мммммм
    img 22256
    with fade
    cashier "Ммм..."
    sound snd_fabric1
    img 22257
    with diss
    cashier "И еще..."
    music Groove2_85
    img 22258
    with fade
    mt "Да она издевается!"
    img 22259
    with diss
    m "Я не буду больше этого делать!" #снова возмущенно
    img 22260
    with fade
    cashier "Последний раз и все. Иначе никакой скидки!"
    img 22261
    with diss
    $ menu_corruption = [monicaVivianSchoolOutfitLick3]
    menu:
        "Поцеловать животик еще ниже.":
            pass
        "Уйти.":
            m "Я не собираюсь продолжать это!"
            return 3
    mt "Какая мерзость!"
    sound snd_kiss3
    music Loved_Up2
    img 22262 # целует
    with diss
    w
    sound Jump1
    img 22263
    with diss
    mt "!!!"
    # Моника злится, но целует, на лице отвращение
    img 22264
    with fade
    cashier "Ммм... Это было приятно." #Вивьен довольна
    cashier "Теперь можешь купить этот костюм со скидкой."
    music Groove2_85
    img 22265
    with diss
    mt "Ну наконец-то!"

    call dialogue_classmate_3_1_7() from _call_dialogue_classmate_3_1_7_1
    # Вивьен оформляет покупку, отдает костюм с улыбкой, Моника держится высокомерно
    music stop
    img black_screen
    with diss
    pause 2.0
    music Road_Trip
    $ add_money(-monicaEricCollegeDressPriceLickingDiscount)
    img 22269
    with fadelong
    m "Я беру его."
    img 22270 #?
    with diss
    cashier "Твой костюм. Надеюсь, ты скоро придешь снова."
    sound highheels_short_walk
    img 22271
    with diss
    cashier "Тебе же понравился мой индивидуальный подход к постоянным клиентам?" #многозначительно улыбается
    sound jump2
    img 22272
    with diss
    w
    music Groove2_85
    sound Jump1
    img 22273
    with fade
    m "Очень!" #зло
    # Моника забирает покупку
    $ monicaBoughtSchoolOutfitByLicking = True
    return 4

label dialogue_classmate_3_1_1a:
    if cloth_type == "SchoolOutfit":
        mt "В этой районе одни извращенцы."
        mt "Которые только и мечтают, чтобы изнасиловать приличную домохозяйку..."
        mt "Я не пойду туда!"
        return False
    return


label dialogue_classmate_3_1_1b:
    mt "!!!"
    mt "Чертова лесбиянка!"
    return


label dialogue_classmate_3_1_1c:
    mt "Я не хочу шататься по городу в таком провинциальном виде..."
    mt "Фи!"
    return

# Моника в магазине одежды выбирает платье.
label dialogue_classmate_3_1_1:
    # не рендерить!
    mt "Фи! Неужели такое кто-то покупает?"
    return
# Моника в магазине одежды выбирает платье.
label dialogue_classmate_3_1_2:
    # не рендерить!
    mt "А это платье я не взяла бы даже бесплатно."
    return
# Моника в магазине одежды выбирает платье.
label dialogue_classmate_3_1_3:
    # не рендерить!
    mt "Как такое можно надеть на себя?"
    return
# Моника в магазине одежды выбирает платье.
label dialogue_classmate_3_1_4:
    # не рендерить!
    mt "В этом магазине нет ни одного приличного платья для деревенщин."
    return
# Моника в магазине одежды выбирает платье.
label dialogue_classmate_3_1_5:
    # не рендерить!
    mt "Какая безвкусица! Фи!"
    return
# Моника в магазине одежды нашла подходящий наряд.
label dialogue_classmate_3_1_6:
    # не рендерить??? костюм
    mt "Хм. Это, конечно, выглядит ужасно, но... Может, стоить примерить?"
    return
# Моника в примерочной, костюм с шортами
label dialogue_classmate_3_1_7:
    # Моника надевает в примерочной шортики и блузку, смотрит на себя в этом костюме
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Road_Trip
    img 22266
    with fadelong
    mt "Какой ужас!"
    img 22267
    with diss
    mt "..."
    mt "Я в нем похожа на маму?"
    mt "По крайней мере, выгляжу получше, чем эта деревенщина в своем ужасном платье."
    img 22268
    with diss
    mt "Думаю, что не найду ничего более приемлимого в этом магазине. Только время зря потрачу."
    mt "Это, конечно, лучше, чем тот ужас, в котором я хожу по этому району, но все-же..."
    return

# Моника пришла в магазин вечером
label dialogue_classmate_3_2a:
    # не рендерить!!!
    mt "Странно. Магазин закрыт. Интересно почему?"
    mt "Может быть стоит {c}придти сюда днем{/c}?"
    return

# Моника пришла на локацию колледжа в красивом платье
label dialogue_classmate_3_2b:
    # не рендерить!!!
    mt "В этом платье я больше похожа на директора колледжа."
    mt "Учитель не поверит, что у этого бестолкового Эрика такая сногсшибательная мама..."
    return

# Моника пришла на локацию колледжа в одежде шлюхи
label dialogue_classmate_3_2bb:
    # не рендерить!!!
    mt "Возможно, мать этого сопляка и пошла бы в колледж в таком виде..."
    mt "Но не Я!"
    return

# Моника пришла в колледж вечером
label dialogue_classmate_3_2c:
    # не рендерить!!!
    mt "Мне нечего там делать вечером."
    return

# Моника пытается зайти в школу, когда там нет квеста
label dialogue_classmate_3_2d:
    # не рендерить!!!
    mt "Что я там забыла?!"
    return

# Город. Моника, выйдя из магазина одежды.
label dialogue_classmate_3_2:
    # не рендерить!!!
#    mt "Сейчас мне нужно переодеться и идти в колледж."
    mt "Надеюсь, что мне больше не придется возвращаться в этот магазин с дурацкой одеждой для людей без вкуса."
    mt "И общаться с НЕЙ!"
    mt "Фи!"
    mt "..."
    mt "Сейчас мне нужно идти в колледж."
    mt "Если я сделаю что-то не так, Барди меня накажет и снова будет угрожать Маркусом."
    mt "Лучше лишний раз не связываться с этой малявкой."
    return

# Город. Моника, выйдя из магазина одежды, не сделав покупку.
label dialogue_classmate_3_2e:
    # не рендерить!!!
    m "У меня нет времени на подобные глупости!"
    return


# Дом. Подвал. Моника надевает костюм мамы для колледжа.
label dialogue_classmate_3_3:
    # не рендерить!!!
    mt "Дурацкий костюм. Надеюсь, я в нем похожа на маму?"
    mt "По крайней мере, выгляжу получше, чем эта деревенщина Бетти в своем ужасном платье. Фи!"
    return

# мысли Моники в колледже
label dialogue_classmate_3_3a:
    # если вышла с колледжа и хочет снова туда зайти
    mt "Я сегодня уже достаточно наговорилась с учителем. Нужно не забыть рассказать малявке, как все прошло."
    return
label dialogue_classmate_3_3b:
    # смотрит на учителя
    mt "Этот Мистер Эдвардс и правда такой солидный и уважаемый учитель, каким хочет казаться?"
    return
label dialogue_classmate_3_3c:
    # осматривает школьный класс окна
    mt "Очень неплохой дизайн кабинета. Окна делают его очень светлым и уютным."
    return
label dialogue_classmate_3_3d:
    # осматривает школьный класс, полки с книгами
    mt "Столько книг... Для таких озабоченных малявок, как Барди, это просто куча бумаги."
    return
label dialogue_classmate_3_3e:
    # осматривает школьный класс, доска
    mt "Хм, я знаю одного студента в этом классе, который дважды два не вычислит..."
    return
label dialogue_classmate_3_3f:
    # осматривает школьный класс, карта мира
    mt "Смотрится неплохо. Когда верну себе свой журнал, повешу такую же карту у себя в кабинете."
    return
label dialogue_classmate_3_3g:
    # осматривает школьный класс, парты
    mt "У Барди в классе все такие же наглые и озабоченные малявки, как он? Судя по Эрику - да."
    return
label dialogue_classmate_3_3h:
    # осматривает школьный класс, формулы на стене (картины)
    mt "Можно всю жизнь учить эти дурацкие формулы и все равно не стать успешным и богатым... Такой, как я."
    return
label dialogue_classmate_3_3i:
    # смотрит на колледж (глазик)
    mt "Поверить не могу! Я, Моника Бакфетт, должна идти в этот дурацкий колледж!"
    mt "Да еше и притворяться там матерью какого-то малявки!!!"
    return

# Город. Школьный двор. Моника перед колледжем.
label dialogue_classmate_4:
    # не рендерить!
    # Моника одета в костюм мамы, чем очень недовольна
    if day_time != "evening":
        $ remove_hook()
        mt "Чувствую себя ужасно в этом наряде. Как эта деревенщина Бетти может подобное надевать?"
        mt "Поверить не могу! Я, Моника Бакфетт, буду притворяться какой-то миссис Б..."
        mt "Забыла... Вот черт. Что-то на Б..."
        mt "А учитель, по-моему, Эдвардс. Надеюсь, у меня получится все быстро сделать. И поскорее забыть об этих глупостях малявок."
        mt "Как-будто у меня своих проблем мало! Еще этот Барди со своим другом..."
        mt "Так, Моника, соберись! Нужно сделать все, как хочет Барди, иначе проблем станет еще больше."
        return False
    return

label dialogue_classmate_4a:
    # Моника говорит при входе в калитку дома (если одето schooloutfit)
    mt "Мне лучше не показываться в этом провинциальном наряде перед Бетти."
    mt "Эта дура подумает что я хочу занять ее место рядом с Ральфом."
    mt "Нет, Я, конечно, хочу занять ее место, потому что оно МОЕ!"
    mt "Но без этого тюфяка Ральфа."
    mt "Это мой дом! И только мой!"
    return

# Колледж. Класс. Разговор Моники и учителя.
label dialogue_classmate_5:
    if dialogue_classmate_5_flag == False:
        # Моника стоит у дверей, учитель сидит за учительским столом
        music Groove2_85
        img 14944
        with fadelong
        w
        img 14945
        with diss
        w
        sound highheels_short_walk
        img 14946
        with diss
        mt "Это учитель? Надеюсь, разговор с ним не займет у меня много времени."
        img 14947
        with fade
        m "Мистер Эд... Эдвардс?"
        # учитель поворачивается к ней с серьезным лицом
        img 14948
        with diss
        teacher "Да. Миссис Бейкер, я полагаю?"
        img 14949
        with diss
        mt "Точно. Бейкер. Как я могла забыть?"
        img 14950
        with fade
        m "Да, мистер Эдвардс. Я пришла поговорить про моего сына Эрика."
        img 14951
        with diss
        mt "Мелкого озабоченного извращенца..."
        img 14952
        with fade
        teacher "Проходите, миссис Бейкер. Присаживайтесь." #предлагает ей стул сбоку от учительского стола
        # учитель общается очень вежливо, с выражением лица 'солидный учитель', Моника спокойно его слушает
        music stop
        img black_screen
        with diss
        pause 1.5
        sound highheels_short_walk
        music Groove2_85
        img 14953
        with fadelong
        teacher "Эрик - один из лучших студентов в классе и никогда с ним не было проблем. Но вот на днях..."
        teacher "На днях Эрик залез в шкафчик с одеждой тренера по плаванию. И она его застала за тем, что он дро... хм-м, что он мастурбировал, используя ее нижнее белье."
        sound Jump2
        img 14954
        with hpunch
        mt "И почему я не удивлена?.." #Моника продолжает его спокойно слушать с непроницаемым лицом
        img 14956
        with fade
        teacher "Тренер очень возмущена и собирается идти к директору. Она будет требовать у директора наказать Эрика."
        teacher "Но я ее уговорил немного подождать, так как хотел поговорить сначала с вами."
        sound Jump1
        img 14955
        with diss
        teacher "Возможно, мы с вами сможем уладить этот вопрос без вмешательства директора."
        teacher "Я не хотел бы, чтобы у Эрика была плохая характеристика. И чтобы об этом инциденте узнал весь колледж."
        img 14957
        with diss
        mt "Какая-нибудь мама на моем месте, наверное, была бы в шоке."
        mt "Нужно сказать этому мистеру Эдвардсу что-нибудь эмоционально. Как там Барди мне говорил?"
        # Моника делает удивленное лицо
        music Hidden_Agenda
        img 14958
        with fade
        m "Мистер Эдвардс, я просто шокирована поступком Эрика! Я обязательно серьезно поговорю с ним!"
        m "Такого больше не повторится, мистер Эдвардс. И я предпочла бы, чтобы не было никакой огласки."
        # учитель с серьезным лицом
        img 14959
        with diss
        teacher "Я абсолютно с вами согласен, миссис Бейкер."
        img 14960
        with diss
        mt "Отлично!"
        # Моника встает со стула, смотрит на учителя
        sound highheels_short_walk
        img 14961
        with fade
        m "Значит, мы с вами все уладили? Я тогда пойду."
        # учитель отводит взгляд, потом снова смотрит на нее
        music Groove2_85
        img 14962
        with diss
        teacher "Нет, миссис Бейкер. Не торопитесь. Мы не уладили..."
        img 14963
        mt "???"
        # Моника вопросительно смотрит на него, садится обратно
        sound highheels_short_walk
        img 14964
        with fade
        teacher "Видите ли, миссис Бейкер, основная сложность - это успокоить учителя по плаванию."
        teacher "Мисс Мэнсфилд сильно рассержена на Эрика..."
        img 14965
        with diss
        m "..."
        img 14966
        with fade
        teacher "И я даже не знаю, как это сделать."
        teacher "Она очень строгая и так просто с ней не договориться."
        img 14967
        with diss
        teacher "Если у меня получится, тогда с Эриком все будет в порядке. Никто ничего не узнает."
        teacher "Но это будет крайне сложно сделать..."
        img 14968
        with fade
        m "Мистер Эдвардс, есть ли у вас какие-нибудь идеи? Как вы сможете договориться с ней?" #с досадой
        img 14969
        with diss
        teacher "Да, идея есть. Она хочет номинироваться на преподавателя года."
        teacher "Для этого ей нужна не только физическая форма и успехи в педагогике..."
        teacher "Но и солидный объем теоретической работы."
        img 14970
        with diss
        teacher "Она должна предложить какую-нибудь прогрессивную методику преподавания. Таковой у нее нет."
        teacher "А у меня как раз есть кое-какие наработки по современной методике преподавания. И я мог бы передать их мисс Мэнсфилд." #все это с очень важным видом
        teacher "Но, понимаете, миссис Бейкер... Просто так я это сделать не могу. Я потратил немало времени на эту работу."
        img 14971
        with diss
        teacher "Если вы меня поддержите, миссис Бейкер, то я сегодня же поговорю с ней. И предложу помочь мисс Мэнсфилд с этой методикой."
        # Моника удивляется
        music Hidden_Agenda
        img 14972
        with fade
        m "Каким образом я могу вас поддержать, мистер Эдвардс? Что мне нужно сделать?"
        img 14973
        with diss
        mt "Хоть на этот раз обойдется без сомнительных просьб в мой адрес..."
        mt "Это все-таки учитель. Он должен быть высокоморальным человеком и примером для своих учеников."
        # учитель, смущенно улыбаясь
        music Groove2_85
        img 14974
        with fade
        teacher "Мне не совсем удобно, миссис Бейкер..."
        teacher "Но дело уж очень деликатное..."
        teacher "Я вынужден попросить вас о небольшом одолжении. Это все же делается ради вашего сына, миссис Бейкер."
        # Моника с серьезным лицом
        music Hidden_Agenda
        img 14976
        with diss
        m "Каком одолжении, мистер Эдвардс? Я сделаю, что нужно."
        # учитель, смущенно
        music Groove2_85
        img 14975
        with fade
        teacher "Если бы вы, миссис Бейкер, смогли показать мне хотя бы свою грудь..."
        teacher "То я был бы очень рад этому."
        teacher "Это очень поддержало бы меня морально."
        # Моника в шоке
        music Power_Bots_Loop
        img 14977
        with hpunch
        mt "!!!"
        img 14978
        with diss
    else:
        music Groove2_85
        img 14983
        with fadelong
        teacher "А, миссис Бейкер! Это вы? Ну как, вы надумали?" #с улыбочкой

    if dialogue_classmate_5_flag == False:
        $ menu_corruption = [0, monicaTeacherCorruption2, monicaTeacherCorruption1]
    else:
        $ menu_corruption = [0, monicaTeacherCorruption4, monicaTeacherCorruption3]
    $ dialogue_classmate_5_flag = True
    menu:
        "Убежать.":
            img 14979
            with fadelong
            m "Я не буду этого делать!!!"
            return False
        "Постараться договориться с учителем без этих извращений.":
            music Groove2_85
            img 14980
            with fade
            m "Мистер Эдвардс! Я не ожидала, что вы можете предложить мне подобное!"
            m "Я же мать вашего ученика. Как так можно?"
            # Моника вскакивает со стула, учитель ей, с сожалением
            img 14981
            with diss
            teacher "Тогда у меня, к сожалению, никак не выйдет договориться с мисс Мэнсфилд."
            teacher "И она создаст Эрику большие проблемы."
            img 14982
            with diss
            teacher "..."
        "Если это поможет быстро решить проблему малявки, то, возможно, стоит потерпеть...":
            pass

    # Моника стоит у учителького стола сбоку
    music Hidden_Agenda
    img 14984
    with diss
    mt "Мне нужно всего лишь показать грудь. А она у меня действительно великолепна."
    mt "В принципе, если это все, что от меня требуется..."
    mt "И этим я смогу отделаться от надоедливого Барди... то, возможно, стоит пойти на это."
    img 14985
    with diss
    mt "Он же хочет, чтобы я просто показала грудь. На большее не намекает."
    mt "Хотя мог бы воспользоваться ситуацией."
    mt "Я уже насмотрелась на разных извращенцев и этот мистер Эдвардс не похож на них."
    music Groove2_85
    img 14986
    with fade
    m "Хорошо, мистер Эдвардс. Я покажу грудь, но только прикасаться ко мне я не позволю."
    m "Можно только посмотреть!" #строго
    # учитель, довольно улыбаясь, встает со своего стула
    img 14987
    with diss
    teacher "Конечно! Я только посмотрю."
    teacher "Это и правда мне очень поможет, миссис Бейкер."
    # Моника с недовольным лицом приспускает блузку и оголяет грудь, учитель пялиться на нее
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Loved_Up
    img 14988
    with fadelong
    m "..."
    img 14989
    with diss
    teacher "Вы потрясающе красивая женщина, миссис Бейкер! Я никогда не видел более красивой груди!"
    img 14990
    with diss
    mt "Еще бы! Я владелица модного журнала и самая красивая женщина в этом городе!"
    mt "Или, вообще, во всей этой стране!"
    img 14991
    with fade
    teacher "Можно я прикоснусь совсем немного?"
    music Groove2_85
    img 14992
    with hpunch
    m "Нет, мы так не договаривались. Вы достаточно посмотрели, мистер Эдвардс?" #строго
    img 14993
    with fade
    teacher "Да, спасибо, миссис Бейкер. Я уверен, что у меня теперь все получится."
    # Моника приводит блузку в порядок
    music stop
    img black_screen
    with diss
    sound snd_fabric1
    pause 2.0
    music Groove2_85
    img 14994
    with fadelong
    m "Мистер Эдвардс, как я узнаю, что у вас получилось все уладить с мисс Мэнсфилд?"
    m "Я должна быть уверена в положительном результате."
    img 14995
    with diss
    teacher "Я позвонил бы вам, но так как дело очень деликатное и я боюсь огласки..."
    teacher "Будет лучше, если вы снова придете ко мне. И тогда я вам лично все сообщу, миссис Бейкер." #с улыбочкой
    # Моника недовольна
    music Hidden_Agenda
    img 14998
    with fade
    mt "Черт! Мне снова нужно будет приходить сюда!"
    mt "..."
    img 14999
    with diss
    mt "А если что-то у учителя пойдет не так?"
    mt "То у Эрика будут проблемы. И у меня тогда тоже... с Барди."
    music Groove2_85
    img 14996
    with fade
    m "Договорились, мистер Эдвардс. Буду надеяться на успешное решение этой проблемы."
    m "До встречи."
    img 14997
    with diss
    teacher "До свидания, миссис Бейкер."
    teacher "Приятно было с вами познакомиться."
    # Моника уходит
#    $ log1 = _("Барди совсем обнаглел и заставляет меня быть мамой для своего одноклассника. Такого же неудачника как он сам!")
    return

# Город. Школьный двор. Моника, выйдя с колледжа.
label dialogue_classmate_5_1:
    # не рендерить!
    mt "Этот учитель не такая уж сволочь... как остальные люди, которые меня окружают"
    mt "Он попросил меня об этом только под давлением обстоятельств."
    mt "Буду надеяться, что у него все получится."
    mt "Нужно будет не забыть зайти к малявке и сказать, что результат будет позже."
    return

# Город. Школьный двор. Моника, выйдя с колледжа. Если она убежала от Эдвардса.
label dialogue_classmate_5_1a:
    # не рендерить!
    mt "Как он мог мне такое предложить?!"
    mt "Он же учитель! Он должен подавать пример своим ученикам!"
    mt "Я больше не хочу разговаривать с ним! Пусть эти малявки сами разбираются!!!"
    mt "Нужно будет зайти к малявке и сказать, что ноги моей больше не будет в этом колледже."
    return False

# Дом. Комната Барди. Барди, Моника.
label dialogue_classmate_5_1b: # если ушла от учителя
    # Моника заходит в комнату Барди, тот сидит на кровати, залипнув в телефон
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 15145
    with fadelong
    w
    img 15146
    with diss
    mt "Ненавижу эту малявку! Он меня достал уже со своими глупостями!"
    # Барди вопросительно смотрит на нее
    img 15147
    with fade
    bardie "Ну как сходила, гувернантка? Надеюсь, у тебя все получилось уладить?"
    # Моника недовольно
    img 15148
    with diss
    m "Если бы твой друг включил мозг, когда надумал залезть в шкафчик мисс Мэнсфилд. То проблем бы никаких не было."
    # Барди смотрит на Монику
    img 15149
    with fade
    bardie "И? Проблема решена?"
    # Моника орет
    music Power_Bots_Loop
    img 15150
    m "Нет! И я не собираюсь заниматься этими глупостями!"
    m "Я не пойду больше в этот твой чертов колледж! Разбирайтесь сами!"
    # Барди угрожающе
    music Groove2_85
    img 15151
    with fade
    bardie "Гувернантка забыла, что Эрик делает хозяину домашку?"
    music Power_Bots_Loop
    img 15152
    m "Да какое мне дело до этого?!" #возмущенно
    m "Пусть сам решает свои проблемы!!!"
    music Groove2_85
    img 15153
    with fade
    bardie "Гувернантка плохая! Ее надо наказать!"

    music stop
    img black_screen
    with Dissolve(2.0)
    call textonblack(_("5 минут спустя...")) from _call_textonblack_42
    img black_screen
    with Dissolve(2.0)
    music Groove2_85

    if monicaUnder != "Nude":
        sound snd_fabric1
        if monicaBettyPanties == False:
            if monicaUnder != "Nude":
                img 10272
        else:
            if monicaBettyPantiesId == 1:
                #betty
                img 10273
            if monicaBettyPantiesId == 2:
                img 10274
            if monicaBettyPantiesId == 3:
                img 10275
            if monicaBettyPantiesId == 4:
                img 10276
            if monicaBettyPantiesId == 5:
                img 10277
        with fadelong
        bardie "Покажи мне, как хорошо ты соблюдаешь правила этого дома!"
        sound snd_fabric1
        if monicaBettyPanties == False:
            if monicaUnder != "Nude":
                #governess
                img 10292
                with diss
                w
                img 10293
                with diss
                w
        else:
            if monicaBettyPantiesId == 1:
                #betty
                img 10295
                with diss
                w
                img 10294
                with diss
                w
                img 10305
                with diss
                w
        #
            if monicaBettyPantiesId == 2:
                img 10296
                with diss
                w
                img 10297
                with diss
                w
                img 10306
                with diss
                w
        #
            if monicaBettyPantiesId == 3:
                img 10299
                with diss
                w
                img 10298
                with diss
                w
                img 10307
                with diss
                w
        #
            if monicaBettyPantiesId == 4:
                img 10300
                with diss
                w
                img 10301
                with diss
                w
                img 10308
                with diss
                w
        #
            if monicaBettyPantiesId == 5:
                img 10303
                with diss
                w
                img 10302
                with diss
                w
                img 10304
                with diss
                w
    else:
        img 10281
        with fadelong
        bardie "Покажи мне, как хорошо ты соблюдаешь правила этого дома!"
    img 10309
    with fade
    w
    img 10310
    with fade
    w
    img 10311
    with fade
    mt "Ненавижу его!"
    img 10312
    with fade
    w
    img 10313
    with fade
    mt "Он меня этим не напугает и не заставит идти к учителю!"
    img 10314
    with fade
    w
    img 10315
    with fade
    mt "Он все равно не добьется своего!"
    img 10316
    with fade
    w
    img 10317
    with fade
    mt "Я не пойду в этот чертов колледж! Я не хочу!!!"
    img 10318
    with fade
    w
    img 10319
    with fade
    w


label dialogue_classmate_5_1b_loop1:
    # Барди шлепает Монику

    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_1 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_1.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_1
    wclean
    stop music

    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_2 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_2.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_2
    bardie "Гувернантка ослушалась приказа хозяина!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_3 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_3.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_3

    bardie "Получай!"
    bardie "Плохая гувернантка!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_4 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_4.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_5 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_5.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_5
    bardie "Гувернантка поняла, что вела себя плохо?"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_6 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_6.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_6
    bardie "Гувернантка больше не будет так делать и выполнит все, что скажет хозяин?"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Basement_Bardie_Monica_Spanking_1.mp3"
    scene black
    image videov_Basement_Bardie_Monica_Spanking_1_7 = Movie(play="video/v_Basement_Bardie_Monica_Spanking_1_7.mkv", fps=30)
    show videov_Basement_Bardie_Monica_Spanking_1_7
    bardie "Гувернантка должна пойти в колледж и решить проблему Эрика!"
    wclean
    stop music

    music Power_Bots_Loop
    mt "Черт! Как больно! Когда он уже остановится?!"
    menu:
        "Отпусти меня немедленно, малявка!":
            img 10320
            with fade
#            m "!!!"
            m "Я хорошая гувернантка!"
            m "Но я не пойду в колледж!"
            m "Отпусти меня немедленно, малявка!"
#            mt "Нет! Я не пойду туда больше!"
            jump dialogue_classmate_5_1b_loop1
        "Я поняла! Я буду слушаться хозяина!":
            pass


    music Groove2_85
    img 10321
    with fade
    m "Я поняла! Я буду слушаться хозяина!"
    img 10322
    with fade
    m "Я хорошая гувернантка! Я поговорю с учителем еще раз!"
    img 10323
    with fade
    bardie "Так-то лучше!"
    img 10324
    with diss
    bardie "Если будешь себя снова плохо вести, получишь еще!"
    img 10325
    with fade
    bardie "Гувернантка, можешь продолжать работать..."
    bardie "Ты мне пока не нужна."

    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Pyro_Flow
    img 10326
    with fadelong
    mt "Не могу поверить!"
    mt "Этот малявка отшлепал меня словно я маленький ребенок!"

    #Если повтор
    if bardieMonicaPunishmentCount > 1:
        img 10327
        with fade
        mt "И уже не первый раз!!!"
        #
        img 10327
        mt "В моем же доме!"
        mt "Отшлепали! Меня!!!"
        mt "Монику Бакфетт!!!"
        #

    img 10328
    with fade
    mt "У меня попа горит!"
    img 10329
    with diss
    mt "Что этот Барди себе позволяет?!"

    music stop
    img black_screen
    with diss
    pause 1.0
    music Groove2_85
    img 10330
    with fadelong
    mt "Как унизительно!"
    mt "Мне надо как-то избавиться от него!"


#    img 14596
#    m "!!!" # зло смотрит на него
#    img 15154
#    mt "Надеюсь, после этого он, наконец, отстанет от меня."
    # поднимает юбку БАРДИ НАКАЗЫВАЕТ МОНИКУ - ШЛЕПАЕТ ПО ПОПЕ
#    bardie "Гувернантка ослушалась приказа хозяина!"
#    bardie "Плохая гувернантка!"
#    bardie "Гувернантка поняла, что вела себя плохо?"
#    bardie "Гувернантка больше не будет так делать и выполнит все, что скажет хозяин?"
#    bardie "Гувернантка должна пойти в колледж и решить проблему Эрика!"


    return

# Дом. Комната Барди. Барди, Моника и Эрик.
label dialogue_classmate_6: # Моника успешно сходила к учителю
    # Моника заходит в комнату Барди, Эрик сидит на стуле возле ноута, Барди стоит рядом
    music stop
    img black_screen
    with diss
    sound highheels_short_walk
    pause 1.5
    music Groove2_85
    img 22277
    with fadelong
    mt "Ненавижу этих двух малявок! Надеюсь, сегодня обойдется без уроков по вылизыванию меня там..."
    # Барди и Эрик вопросительно смотрят
    img 22278
    with diss
    bardie "Ну как сходила, гувернантка? Надеюсь, у тебя все получилось уладить?"
    # Моника недовольно
    img 22279
    with fade
    m "Если бы твой друг включил мозг, когда надумал залезть в шкафчик мисс Мэнсфилд. То проблем бы никаких не было."
    # Эрик снова залипает в ноут, теряя интерес, Барди смотрит на Монику
    img 22280
    with diss
    m "А теперь мне и учителю приходится думать о том, как это уладить!" #возмущенно
    m "Мистер Эдвардс сказал, что поговорит с мисс Мэнсфилд. Как будет результат, он мне сообщит."
    m "Из-за этого мне снова придется идти в колледж."
    m "А это никак не входило в мои планы!"
    # Барди
    img 22281
    with fade
    bardie "Гувернантка хорошая! Я вижу, что она старается."
    bardie "Если у нее получится все уладить, то я буду очень доволен своей гувернанткой!"
    img 22282
    with diss
    mt "..."
    img 22283
    with fade
    bardie "Теперь можешь идти, гувернантка."
    bardie "Ты на сегодня свободна."
    music stop
    img black_screen
    with diss
    sound highheels_run2
    pause 2.0
    music Mandeville
    return

label dialogue_classmate_6a:
    mt "Черт, мне снова придется надевать этот дурацкий костюм для провинциалок. Фи!"
    return

# Город. Школьный двор. Моника перед колледжем.
label dialogue_classmate_7:
    $ dialogue_classmate_7_flag = True
    # не рендерить!
    # Моника, как в прошлый раз, одета в костюм мамы
    mt "Чувствую себя ужасно в этом костюме. Как эта деревенщина Бетти может подобное надевать?"
    mt "Надеюсь, у учителя все получилось, и мне не придется возвращаться сюда снова."
    mt "Нужно сделать все, чтобы у этого мелкого озабоченного извращенца не было проблем в колледже."
    mt "Иначе у меня возникнут проблемы посерьезнее, чем есть сейчас."
    return False

# Колледж. Класс. Разговор Моники и учителя.
label dialogue_classmate_8:
    # Моника заходит в кабинет, стоит у дверей, учитель сидит за учительским столом
    img 15000
    w
    img 15001
    mt "Надеюсь, в этот раз мне не придется вдохновлять его своей голой грудью..."
    img 15002
    m "Мистер Эдвардс, добрый день."
    # учитель поворачивается к ней, с улыбочкой
    img 15003
    teacher "Здавствуйте, миссис Бейкер. Я вас ждал. Присаживайтесь."
    # Моника садится на стул рядом с его столом
    img 15004
    m "Удалось ли вам договориться с мисс Мэнсфилд?" #с серьезным выражением лица
    img 15005
    teacher "Да, я поговорил с ней, миссис Бейкер."
    teacher "И у меня почти получилось с ней договориться, но..."
    img 15006
    m "???"
    m "Но?.."
    img 15007
    teacher "Она осталась не совсем довольна тем, что мою методику преподавания ей нужно дорабатывать."
    teacher "Но мисс Мэнсфилд согласна подождать, когда я закончу работу."
    teacher "Только после этого она согласна забыть про случай с Эриком."
    img 15008
    m "Когда вы сможете закончить эту работу, мистер Эдвардс?."
    img 15009
    teacher "Я уже провел кое-какую работу над своей методикой."
    teacher "Думаю, теперь мисс Мэнсфилд будет ею довольна."
    img 15010
    teacher "..."
    teacher "Знаете, миссис Бейкер... Мне очень сложно отдавать свои труды мисс Мэнсфилд..."
    img 15011
    m "???"
    img 15012
    mt "Сейчас он снова будет просить о поддержке..." #недовольно
    mt "Извращенец..."
    img 15013
    teacher "Если бы вы, миссис Бейкер, смогли показать мне снова свою грудь."
    teacher "И дать ее потрогать совсем немного."
    teacher "То я смогу найти в себе силы сделать это." #с улыбочкой
    img 15014
    m "..." #недовольно
    img 15015
    mt "Мне нужно показать грудь, как в прошлый раз."
    mt "Он ее уже видел. Но вот прикасаться ко мне!.."
    mt "..."
    img 15016
    menu:
        "Убежать.":
            img 15017
            m "Я не буду этого делать!!!"
            return False
        "Постараться договориться с учителем без этих извращений.":
            img 15018
            m "Мистер Эдвардс, я не хочу, чтобы вы трогали меня!"
            m "Показать повторно грудь - это одно дело. Но прикосновения - это уже чересчур!"
            # Моника вскакивает со стула, учитель ей, с сожалением
            img 15019
            teacher "Тогда у меня, к сожалению, никак не выйдет договориться с мисс Мэнсфилд."
            # учитель отворачивается и начинает просматривать какие-то бумаги на столе, работать
            img 15020
            teacher "..."
            return 1
        "Если это поможет быстрее решить проблему малявки, то, возможно, стоит потерпеть...":
            pass



    # Моника смотрит на него с раздражением
    img 15021
    mt "Это отвратительно! Почему все вокруг хотят сделать со мной что-то непристойное?!"
    mt "!!!"
    img 15022
    mt "С другой стороны, если он просто потрогает немного... А я как-нибудь перетерплю это, то..."
    mt "То, вероятно, вопрос с малявкой будет закрыт совсем скоро."
    mt "И я, наконец, смогу отделаться от надоедливого Барди и его друга."
    img 15023
    m "..."
    img 15024
    m "Потрогать можно совсем немного, мистер Эдвардс!" #недовольно
    # учитель смотрит на нее и расплывается в улыбке
    img 15025
    teacher "Конечно, миссис Бейкер! Это и правда мне очень поможет!"
    # Моника встает, с недовольным лицом приспускает блузку, учитель пялиться на нее, потом подходит и трогает ее
    img 15026
    w
    img 15027
    w
    img 15028
    teacher "Я никогда не видел более красивой женщины, чем вы, миссис Бейкер!"
    img 15029
    w
    img 15030
    m "Я знаю, мистер Эдвардс! Достаточно!" #с раздражением
    # учитель убирает руки и неотрывно смотрит на грудь, пока Моника приводит в порядок блузку
    img 15031
    teacher "Спасибо, миссис Бейкер. Вы мне очень помогли. Я отдам свою методику мисс Мэнсфилд в ближайшее время."
    img 15032
    m "Как я узнаю, что у вас получилось договориться с ней, мистер Эдвардс?"
    img 15033
    teacher "Будет лучше, если вы снова придете ко мне. И тогда я вам лично все сообщу, миссис Бейкер." #с улыбочкой
    # Моника недовольна
    img 14998
    mt "Черт! Мне снова нужно будет приходить сюда!"
    mt "..."
    img 14999
    mt "А если что-то у учителя пойдет не так?"
    mt "То у Эрика будут проблемы."
    mt "И у меня тогда тоже... с Барди."
    img 14996
    m "Договорились, мистер Эдвардс. Буду надеяться на успешное решение этой проблемы."
    m "До встречи."
    img 14997
    teacher "До свидания, миссис Бейкер."
    teacher "Буду рад видеть вас снова."

    $ log1 = _("Сообщить Барди о визите в колледж")
    $ log1 = _("Идти в колледж, притворившись мамой Эрика")
    return

# Город. Школьный двор. Моника, выйдя с колледжа.
label dialogue_classmate_8_1:
    # не рендерить!
    mt "Буду надеяться, что у него все получится."
    mt "Нужно будет не забыть зайти к малявке и сказать, что результат будет позже."
    return

# Колледж. Класс. Разговор учителя и мисс Мэнсфилд.
label dialogue_classmate_8_2:
    # в кабинет к Эдвардсу заходит мисс Мэнсфилд, в руках нагайка, учитель вскакивает со своего стула, широко улыбается
    img 22558
    w
    img 22559
    w
    img 22560
    teacher "Вы сегодня восхитительно выглядите, мисс Мэнсфилд."
    teacher "Рад вас видеть! Присаживайтесь."
    # училка делает несколько шагов по кабинету, останавливается, стоит в уверенной позе с надменным выраженем лица
    img 22561
    mansfield "Давайте, ближе к делу, мистер Эдвардс!"
    # Эдвардс, посерьезнев
    img 22562
    teacher "Да, конечно. Я доработал методику для вас. Осталось внести всего несколько поправок."
    img 22563
    mansfield "..."
    img 22564
    teacher "Завтра утром я ее вам отдам, мисс Мэнсфилд."
    img 22565
    mansfield "В таком случае до завтра, мистер Эдвардс!" #строго
    # училка поворачивается, чтобы уйти, Эдвардс ей вслед
    img 22566
    teacher "Мисс Мэнсфилд?!"
    # она поворачивается, вопросительно смотрит на него
    img 22567
    mansfield "???"
    img 22568
    teacher "Я... для вас..."
    teacher "Я очень старался для вас, мисс Мэнсфилд." #волнуясь
    teacher "Это лучшая прогрессивная методика преподавания."
    teacher "Я проделал огромную работу..."
    img 22569
    teacher "Я был бы очень рад угостить вас ужином, мисс Мэнсфилд."
    teacher "Для меня это будет лучшая благодарность с вашей стороны."
    # училка подходит к нему, тыкает своей нагайкой ему в грудь и со строгим фейсом
    img 22570
    mansfield "Мистер Эдвардс! Сколько раз можно заводить этот разговор про ужин?"
    mansfield "Ответ тот же..."
    img 22571
    mansfield "НЕТ!"
    img 22572
    mansfield "Уясните, меня это НЕ ИНТЕРЕСУЕТ!"
    mansfield "Меня ВЫ не интересуете!"
    img 22573
    teacher "Тогда, можеть быть... Кофе?" #растерянно
    teacher "Составите мне компанию, мисс Мэнсфилд?"
    img 22574
    mansfield "Ответ НЕТ."
    # убирает нагайку с его груди, он держится за это место, она ему с насмешкой
    img 22575
    mansfield "И о какой благодарности с моей стороны может быть речь?!"
    mansfield "Вообще-то, это Я вам сделала одолжение, мистер Эдвардс!"
    img 22576
    teacher "???" #удивленно
    img 22577
    mansfield "Я не рассказала про вашего студента директору..."
    mansfield "По вашей просьбе."
    img 22578
    teacher "..."
    img 22579
    mansfield "Не знаю, зачем вы так за него заступаетесь..."
    teacher "Он... Я..." #растерянно
    img 22580
    mansfield "Надеюсь, вас за это хорошо отблагодарили, мистер Эдвардс."
    img 22581
    teacher "!!!" #он офигел
    # училка поворачивается и уходя, тыча в его сторону нагайкой, строго
    img 22582
    mansfield "Жду мою методику завтра!"
    # хлопает дверью, Эдвардс стоит расстроенный
    return

# Дом. Комната Барди. Барди и Моника
label dialogue_classmate_9_1:
    # Моника заходит в комнату Барди, тот сидит у ноута, Моника смотрит на него с неприязнью
    img 15156
    w
    img 15157
    mt "Противная малявка! Сколько же проблем он мне создает своим существованием в моем доме."
    # Барди поворачивается к ней и с улыбочкой
    img 15158
    bardie "Ну как сходила, гувернантка?"
    "Надеюсь, у тебя все получилось уладить?"
    # Моника недовольно
    img 15159
    m "Учитель сказал, что у него пока не получилось."
    "Он поговорит с мисс Мэнсфилд в ближайшие дни."
    m "Он сообщит мне результат, когда договорится с ней."
    img 15160
    m "Поэтому мне снова придется идти в этот чертов колледж."
    # Барди довольно
    img 13018
    bardie "Гувернантка хорошая. Можешь идти, гувернантка."
    bardie "Жду тебя с окончательным положительным результатом."
    img 13060
    mt "Черт, мне снова придется надевать этот дурацкий костюм для провинциалок. Фи!"
    return

# Город. Школьный двор. Моника перед колледжем.
label dialogue_classmate_10:
    # не рендерить!
    # Моника, как в прошлый раз, одета в костюм для мам
    mt "Чувствую себя ужасно в этом наряде. Как эта деревенщина Бетти может такое надевать?"
    mt "Надеюсь, у учителя все получилось и мне не придется возвращаться сюда снова."
    mt "Нужно сделать все, чтобы у этого мелкого озабоченного извращенца не было проблем в колледже."
    mt "Иначе у меня возникнут проблемы посерьезнее, чем есть сейчас."
    return

# Колледж. Класс. Разговор Моники и учителя.
label dialogue_classmate_11:
    # Моника заходит в кабинет, стоит у дверей, учитель сидит за учительским столом
    img 15034
    w
    img 15035
    w
    img 15036
    m "Мистер Эдвардс, добрый день."
    # учитель поворачивается к ней, с улыбочкой
    img 15037
    teacher "Здавствуйте, миссис Бейкер."
    teacher "Я вас ждал. Присаживайтесь."
    # Моника садится на стул рядом с его столом
    img 15038
    m "Удалось ли вам договориться с мисс Мэнсфилд?" #с серьезным выражением лица
    img 15039
    teacher "Видите ли, с мисс Мэнсфилд не так просто договориться."
    teacher "Она снова нашла недочеты в моей работе."
    img 15040
    m "..."
    img 14740
    teacher "Но, благодаря вам, миссис Бейкер, я превзошел сам себя и доделал свою методику." #улыбаясь
    teacher "Теперь она точно будет довольна!"
    img 14954
    mt "Наконец-то, проблема решена!"
    # учитель делает задумчивое лицо
    img 14953
    teacher "Но теперь я сомневаюсь, стоит ли мне отдавать свою методику ей..."
    img 15041
    mt "!!!" #удивленно
    img 15042
    m "Я очень рада, что у вас все получилось с вашей работой, мистер Эдвардс, но..."
    m "Надеюсь, что я не зря прихожу к вам уже третий раз."
    m "Я ожидаю, что вы все-таки договоритесь с мисс Мэнсфилд."
    # вопросительно смотрит на него, учитель серьезно
    img 15043
    teacher "Мне будет очень непросто это сделать, миссис Бейкер."
    teacher "Ведь я сам могу стать номинантом! Я считаю, что моя работа достойна этого."
    teacher "Все зависит от того, насколько вы, миссис Бейкер, готовы поддержать меня..." #улыбочка
    # Моника  в шоке, возмущается
    img 15044
    m "Вы в своем уме?! Как вы можете мне такое предлагать?!"
    m "Если бы я знала, что в итоге вы потребуете от меня ТАКОГО. Я бы отказалась вообще от вашей помощи!"
    m "!!!"
    img 15045
    teacher "Вы не совсем так меня поняли, миссис Бейкер."
    teacher "Я хочу, чтобы вы просто потрогали меня рукой. Не более того."
    img 15046
    teacher "А без моей помощи вы бы вовсе не смогли уладить эту ситуацию, миссис Бейкер."
    # Моника зло на него смотрит
    img 15047
    m "!!!"
    # учитель продолжает говорить спокойно
    img 15048
    teacher "После этого я сразу же отдам свою работу мисс Мэнсфилд."
    teacher "И вопрос будет закрыт."
    # он при этом встает и расстегивает штаны, Моника зло на него смотрит, сидя на стуле
    img 15050
    mt "Он снова пытается склонить меня к сексуальным действиям!"
    mt "Я не собираюсь этого делать!!!"
    mt "Пусть этот учитель катится к черту! С меня хватит!"
    img 15049
    mt "Пусть идет и рассказывает хоть всему колледжу об этом придурке Эрике!"
    mt "!!!"
    mt "Только что я скажу потом Барди?"
    img 15051
    mt "..."
    mt "Черт! Ненавижу эту малявку!"
    mt "Он же устроит мне массу проблем посерьезнее, чем потрогать член учителя."
    # Моника возмущается
    img 15052
    m "Я пожалуюсь на вас вашему руководству!"
    m "Или в полицию!"
    img 15053
    teacher "Я уважаемый педагог с хорошей репутацией. Вам будет крайне сложно меня обвинить в подобном."
    teacher "Вам просто не поверят, миссис Бейкер."
    img 15054
    teacher "Тем более, что на меня пожалуется мать студента, который сам замечен в аморальном поведении."
    teacher "Вам должно быть стыдно, миссис Бейкер."
    teacher "..."
    # Моника возмущенно смотрит на него, но молчит, сидит на стуле
    img 15055
    mt "Сомневаюсь, что руководство колледжа мне поверит..."
    mt "В полицию мне нельзя..."
    mt "Что же мне делать?"
    mt "..."
    img 15056
    menu:
        "Убежать.":
            img 15017
            m "Я не буду этого делать!!!"
            return False
        "Постараться договориться с учителем без этих извращений.":
            img 15018
            m "Я не занимаюсь такими вещами, мистер Эдвардс!"
            img 15019
            teacher "Я сделал все зависящее от меня, миссис Бейкер. Я пошел на такие жертвы." #спокойно и уверенно
            teacher "И все ради вас..."
            teacher "В таком случае, у меня не получится решить проблему вашего сына, миссис Бейкер."
            # учитель отворачивается и начинает просматривать какие-то бумаги на столе, работать
            img 15020
            teacher "..."
            return 1
        "Если это поможет быстрее решить проблему малявки, то, возможно, стоит потерпеть...":
            pass
    img 15057
    mt "Если все что нужно этому извращенцу - это потрогать его член... И ничего более..."
    mt "Возможно, мне стоит потерпеть и это все закончится, наконец-то?"
    # учитель подходит к ней, достает свой стояк и выжидательно смотрит на нее
    img 15058
    w
    img 15060
    w
    img 15059
    teacher "Просто приласкайте его, миссис Бейкер..."
    img 15061
    m "..." #зло
    img 15062
    # Моника с отвращением протягивает руку, прикасается к нему пальцами
    img 15063
    w
    img 15064
    teacher "Обхватите его рукой, миссис Бейкер..."
    # Моника делает, как он просит, учитель кладет свою руку поверх ее и начинает двигать вверх-вниз
    img 15065
    w
    img 15067
    teacher "Ммм... Да-а-а, как же хорошо..."
    img 15068
    mt "Какой кошмар! Что я делаю?! Как это все мерзко!!!"
    img 15069
    teacher "Ммммммм..."
    # учитель ускоряет движения и со стоном кончает на блузку Моники
    img 15066
    w
    img 15070
    w
    img 14800
    teacher "ОООООО!!!"
    w
    img 15071
    w
    img 15383
    mt "Фуууу!!! Какая гадость!"
    mt "Какого черта?! Он меня испачкал!"
    # Моника оттирает блузку и зло смотрит на учителя, он застегивает штаны, садится за свой стол, улыбается
    img 15384
    teacher "Я весьма рад, миссис Бейкер... Мы с вами весьма успешно закрыли проблему с Эриком."
    img 15311
    mt "Он такой же извращенец, как и все."
    mt "Только притворяется благородным и высокоморальным."
    mt "А сам готов меня склонить к сексу!"
    img 15385
    mt "!!!" #смотрит на него зло
    img 14994
    m "Проблема с Эриком точно решена, мистер Эдвардс?"
    m "Мне не придется приходить сюда снова, чтобы удостовериться в этом?"
    img 14995
    teacher "Абсолютно точно, миссис Бейкер. Можете не переживать."
    teacher "Я прямо сейчас отнесу методику мисс Мэнсфилд."
    img 14996
    m "Хорошо. До свидания, мистер Эдвардс." #недовольно
    img 14997
    teacher "Всегда к вашим услугам, миссис Бейкер."
    # Моника уходит
    return

# Город. Школьный двор. Моника, выйдя с колледжа.
label dialogue_classmate_11_1:
    # не рендерить!
    mt "Наконец-то, я решила этот вопрос!"
    mt "Хорошо, что я больше не увижу этого благородного и высокоморального учителя!"
    mt "Это было ужасно!"
    mt "Какой пример такой учитель может подать своим студентам?!"
    mt "Неудивительно, что Барди и Эрик такие озабоченные малявки, у которых только одно на уме!"
    mt "Мне надо сегодня зайти к Барди и сказать, что я решила проблему его друга."
    return

# Дом. Комната Барди. Барди и Моника (если Моника решила проблему Эрика).
label dialogue_classmate_9_2:
    # Моника заходит в комнату Барди, тот сидит у ноута, Моника смотрит на него с неприязнью
    img 15156
    w
    img 15157
    mt "Противная малявка! Сколько же проблем он мне создает своим существованием в моем доме."
    # Барди поворачивается к ней и с улыбочкой
    img 15158
    bardie "Ну как сходила, гувернантка? Надеюсь, у тебя все получилось уладить?"
    # Моника зло
    img 15159
    m "Да, проблема Эрика решена."
    m "Никаких последствий после его поступка в раздевалке не будет..."
    # Барди очень доволен
    img 15161
    bardie "Гувернантка хорошая! Хозяин дома очень доволен ею!"
    bardie "На днях придет в гости Эрик, чтобы поблагодарить гувернантку..."
    # Моника зло
    img 15162
    m "Я обойдусь без его благодарностей."
    m "Самой лучшей благодарностью будет, если ты перестанешь приставать ко мне!"
    m "!!!"
    # Барди с угрозой
    img 13026
    bardie "Гувернантке не нравится, что хозяин дома доволен ею?"
    bardie "Ей больше нравится получать наказания от него?"
    bardie "Я это могу быстро устроить! Мне не нравится, что гувернантка отказывается от благодарности друга хозяина."
    # Моника с ненавистью
    img 13060
    mt "Этот малявка совсем обнаглел!"
    img 15163
    m "Я сделала достаточно для того, чтобы ты не наказывал меня!"
    m "Именно это и будет лучшая благодарность!"
    # зло смотрит на него и уходит, не дожидаясь ответа
    return

# Дом. Комната Барди. Барди и Моника.
label dialogue_classmate_12:
    # Барди возле своего ноута, орет
    img 15164
    bardie "Гувентантка!!!"
    # спустя несколько минут Моника заходит к нему в комнату, недовольно
    img 15165
    m "Что случилось? Зачем ты так кричишь?"
    img 15157
    mt "Что этому мелкому извращенцу от меня опять надо?"
    # Барди с улыбкой
    img 15166
    bardie "Гувентантка, я хочу проверить, придерживаешься ли ты правил этого дома."
    img 15167
    m "..."
    if monicaUnder != "Nude":
        img 15168
        mt "Черт!!!"
        mt "Он увидит, что я в трусиках и снова накажет меня!"
        img 15169
        m "Я хорошая гувернантка! Но я не буду этого делать!"
        return False
    img 15170
    menu:
        "Сделать, как требует Барди.":
            pass
        "Убежать.":
            img 15169
            m "Я хорошая гувернантка! Но я не буду этого делать!"
            return False
    # Моника с недовольным лицом поднимает юбку
    img 13001
    w
    img 15171
    w
    img 12991
    bardie "Хорошая гувернантка. Хозяин ею доволен. Поэтому может доверить ей одно дело."
    img 12995
    mt "Только не это!"
    img 15172
    bardie "Гувернантка, у Эрика снова проблемы в колледже."
    bardie "Учитель вызывает его мать к себе, срочно."
    bardie "Гувернантка должна снова притвориться мамой Эрика и пойти поговорить с учителем."
    img 15173
    mt "Не дождешься, малявка!" #с ненавистью
    img 15174
    m "Что он на этот раз натворил? Почему я опять должна идти решать его проблемы?!"
    img 13080
    bardie "В прошлый раз ты достаточно быстро решила его проблему."
    bardie "В этот раз тебе придется сделать также."
    img 15175
    bardie "Эрик делает домашние задания для хозяина, если ты помнишь..."
    bardie "Поэтому в твоих интересах, чтобы у него не было проблем в колледже!"
    # Моника злится
    img 15176
    m "Я не собираюсь идти туда!"
    m "Раз у твоего друга нет мозгов, чтобы не встревать во всякие глупые ситуации... То я тут ничем не смогу помочь!"
    m "Я что, каждый раз теперь буду ходить в колледж из-за него?"
    # Барди с фейсом а-ля хозяин дома
    img 12998
    bardie "Это не просьба, гувернантка! Это приказ хозяина дома!"
    bardie "А спорить с хозяином гувернантке запрещено!"
    img 13009
    bardie "Ты должна снова поговорить с учителем и извиниться за Эрика."
    bardie "Скажешь ему, что ты обязательно поговоришь с сыном и такого больше не повторится."
    img 13082
    m "Я уже обещала подобное! И что в итоге?!" #зло
    m "!!!"
    img 15177
    mt "Черт!!! Мне снова придется разговаривать с этим высокоморальным извращенцем!"
    img 12994
    bardie "Если ты все хорошо сделаешь и в этот раз, гувернантка...То я, хозяин дома, буду очень доволен."
    bardie "Ты же хочешь, чтобы хозяин был доволен, гувернантка?"
    # Моника молча на него смотрит и тихо ненавидит
    img 15178
    bardie "Я буду ждать тебя здесь. Надеюсь, ты вернешься из колледжа с хорошими новостями..." #улыбается
    img 15179
    mt "Как же я устала выполнять глупые приказы этого малявки!"
    mt "!!!"
    mt "Скорее бы вернуть этот дом себе и выкинуть эту ненормальную семейку отсюда!"
    # смотрит на мелкого зло и уходит
    return

# Дом. Второй этаж. Моника, выйдя из комнаты Барди.
label dialogue_classmate_12_1:
    # не рендерить!
    mt "Мне снова надо будет идти в этот чертов колледж!"
    mt "Но лучше я сделаю, как хочет эта малявка Барди. Иначе он пойдет к Маркусу и расскажет, где я живу."
    mt "Боюсь даже думать о том, что он пришлет полицейских и они заберут меня..."
    mt "И снова посадят в эту камеру..."
    mt "А потом отправят в то жуткое место... Нет-нет!"
    mt "Боже, не хочу об этом думать!"
    mt "!!!"
    mt "Мне надо скорее идти в колледж. И не забыть надеть тот дурацкий костюм для деревенщин."
    return

# Город. Школьный двор. Моника перед колледжем.
label dialogue_classmate_13:
    # не рендерить!
    # Моника одета в костюм мамы, чем очень недовольна
    mt "Чувствую себя ужасно в этом костюме. Как эта деревенщина Бетти может такое надевать?!"
    mt "Надеюсь, этот мистер Эдвардс не будет от меня требовать всяких своих извращенских штук..."
    mt "Как-будто у меня своих проблем мало..."
    mt "Так, Моника, тебе нужно успокоить этого малявку Барди... Иначе проблем станет еще больше."
    return

# Колледж. Класс. Разговор Моники и учителя.
label dialogue_classmate_14:
    # Моника заходит в кабинет, стоит у дверей, учитель сидит за учительским столом
    img 15301
    w
    img 15302
    w
    img 14947
    m "Мистер Эдвардс, добрый день."
    # учитель поворачивается к ней, с улыбочкой
    img 15303
    teacher "Здавствуйте, миссис Бейкер. Я вас ждал."
    teacher "Присаживайтесь."
    # Моника садится на стул рядом с его столом
    img 14965
    m "Что натворил Эрик в этот раз, мистер Эдвардс?!" #с серьезным выражением лица
    img 14964
    teacher "Вы не поверите, миссис Бейкер..."
    teacher "Он снова залез в шкафчик к тренеру по плаванью..."
    teacher "И сделал то же самое."
    img 15304
    m "ЧТО?!" #офигевает
    m "!!!"
    img 14956
    teacher "Да. Мисс Мэнсфилд это снова увидела." #с сожалением
    teacher "У меня есть подозрения, что Эрик делает это постоянно."
    teacher "Просто Мисс Мэнсфилд это не всегда замечает."
    # Моника в шоке
    img 15305
    m "..."
    img 14959
    teacher "В любом случае, Мисс Мэнсфилд была очень злая на него..."
    img 15306
    m "Была?.."
    img 14770
    teacher "Да, она очень злилась. И я с ней уже договорился."
    teacher "Мне пришлось составить для нее несколько педагогических отчетов, но..."
    img 14955
    teacher "Как вы понимаете, миссис Бейкер, мне пришлось проделать огромную работу."
    teacher "Поэтому я надеюсь на особую благодарность с вашей стороны, миссис Бейкер."
    img 15307
    mt "Ну вот, опять он начинает..." #раздраженно
    mt "!!!"
    mt "С другой стороны, вопрос с мисс Мэнсфилд уже улажен..."
    img 15038
    m "И что я должна сделать, мистер Эдвардс?" #с подозрением
    img 15308
    mt "Учитель на этот раз все очень быстро решил."
    mt "И в итоге поставил меня перед фактом, что я ему должна."
    mt "Высокоморальная сволочь!"
    # учитель с улыбочкой, поднимается со стула и встает напротив Моники
    img 15309
    teacher "Я уже видел вашу прекрасную грудь, миссис Бейкер."
    teacher "Теперь я хочу посмотреть на вашу попку..."
    teacher "И потрогать ее."
    # Моника в шоке
    img 15310
    m "Мистер Эдвардс, вам не кажется, что это уже слишком?!"
    m "Я не собираюсь показывать вам то, что у меня под шортами!"
    img 15311
    mt "Ведь проблема уже решена. Зачем мне соглашаться на это?"
    img 15312
    menu:
        "Отказаться и уйти!":
            # Моника встает со своего стула
            img 15313
            m "Мистер Эдвардс, я не буду вам ничего показывать!"
            m "На этот раз вы зашли слишком далеко!"
            img 15053
            teacher "Миссис Бейкер, я же только посмотрю..."
            # учитель подходит к Монике и кладет руки ей на ягодицы
            img 15314
            teacher "И совсем немного потрогаю..."
            # Моника в шоке
            img 15315
            w
            img 15316
            m "Не смей прикасаться ко мне, извращенец!!!"
            # ударяет учителя коленом между ног, тот скрючивается и орет
            img 15317
            w
            img 15318
            w
            img 15319
            teacher "АААААА!"
            img 15320
            m "И только попробуй предложить мне еще раз подобное!"
            m "Весь колледж узнает о том, какая ты озабоченная сволочь!"
            # Моника уходит
            return False
        "Постараться договориться с учителем без этих извращений.":
            img 15321
            m "Я не занимаюсь такими вещами, мистер Эдвардс!"
            img 15322
            teacher "Мисс Мэнсфилд может и передумать..." #говорит многозначительно
            teacher "..."
            # учитель отворачивается и начинает просматривать какие-то бумаги на столе, работать
            return 1
        "Если это поможет быстрее решить проблему малявки, то, возможно, стоит потерпеть...":
            pass

    # Моника злится
    img 15323
    mt "!!!"
    img 15324
    m "Я не собираюсь этого делать!!!"
    img 15325
    teacher "Я сделал все зависящее от меня..." #с укором
    teacher "Пошел на такие жертвы..."
    img 15326
    teacher "И очень быстро все уладил."
    teacher "И все ради вас, миссис Бейкер!"
    img 15327
    m "..." #зло смотрит
    img 15307
    mt "Учитель может сделать так, что о дебильном поступке Эрика узнают все."
    mt "Тогда Барди точно разозлится и устроит мне массу проблем."
    img 15328
    mt "Если потрогать мою изумительную попу - это все о чем он просит..."
    mt "Возможно, после этого он отстанет от меня..."
    # Моника возмущенно смотрит на него, но молчит, затем встает со стула, учитель подходит к ней ближе, она поворачивается к нему спиной и снимает шорты, она в трусиках Юлии
    img 15329
    w
    img 15331
    w
    img 15330
    w
    img 15332
    w
    img 15333
    w
    img 15334
    W
    img 15335
    mt "Я, Моника Бакфетт, стою с голым задом перед учителем в колледже!"
    mt "Какой кошмар!!!"
    # учитель смотрит на ее зад
    img 15336
    teacher "Миссис Бейкер, я не видел ничего красивее в своей жизни!"
    img 15337
    mt "Еще бы! Об этой попе мечтают миллионы мужчин!"
    mt "Знал бы он, кто я такая на самом деле..."
    # учитель кладет ладони на ее ягодицы, гладит, потом снимает с нее трусики
    img 15338
    w
    img 15339
    w
    img 15340
    w
    img 15341
    m "Этого можно было и не делать, мистер Эдвардс!"
    m "В них и так все прекрасно видно было!" # возмущенно
    # учитель ее не слушает и начинает целовать ее ягодицы, присев за ней
    img 15342
    w
    img 15344
    w
    img 15343
    m "Ай, что вы делаете?!" # удивленно
    # учитель продолжает, потом встает, кладет ей руку на спину и наклоняет ее на свой стол, затем снова тянется к ее попе и целует ягодицы, потом начинает лизать ее киску
    img 15345
    w
    img 15346
    m "Ч-что вы д-делаете?! Нет-нет!!!"
    m "Остановитесь, м-мы договаривались не так!"
    img 15347
    mt "Что этот извращенец творит?! Как он смеет так поступать со мной?!"
    # учитель, не слушая ее продолжает лизать и раздвигает ее ноги шире
    img 15348
    w
    img 15349
    m "!!!"
    m "Прекратите это немедленно!"
    m "Мистер Эдвардс!!!"
    # но сама продолжает стоять в этой позе, оперевшись об стол
    img 15350
    w
    img 15351
    w
    img 15352
    w
    img 15353
    mt "!!!"
    mt "Фу, неужели ему приятно делать такие мерзкие вещи?!"
    img 15354
    mt "Это так... Так щекотно..."
    mt "..."
    # учитель прекращает лизать, проводит по киске пальцем и погружает его в Монику
    img 15355
    w
    img 15356
    m "Ай! Нет!"
    m "Прекратите!!!"
    m "Уберите сейчас же!"
    w
    img 15357
    w
    img 15358
    w
    img 15359
    mt "Боже, что же мне делать?"
    mt "Мне надо остановить его!"
    # учитель начинает двигать пальцем туда-сюда, он уже расстегнул брюки себе, член в полной готовности
    img 15360
    mt "Надо... Остановить."
    img 15361
    mt "Сейчас же..."
    mt "Почему такое чувство, как-будто... Как-будто..."
    # учитель продолжает ласкать ее рукой, встает, приближает свой член к киске, уже почти прикоснулся
    img 15362
    w
    img 15363
    mt "Что за странное ощущение?"
    mt "Не понимаю, что со мной... Надо прекратить это немедленно..."
    img 15364
    w
    img 15365
    m "Мне это совсем не нравится! Не смейте этого делать!"
    m "Прекратите!!!"
    img 15366
    teacher "Да, конечно, миссис Бейкер... Еще несколько минут и я прекращу..."
    # и вводит головку в нее
    # Моника в панике
    img 15367
    m "АААА!"
    m "НЕЕЕЕТ!"
    # но вырваться не пытается, ноги послушно раздвинуты, учитель входит в нее полностью
    w
    img 15382
    w
    img 15368
    mt "Черт! Черт!"
    img 15369
    m "Ах!"
    img 15370
    mt "Я чувствую ЭТО в себе!!!"
    mt "Черт! Нет!"
    m "!!!"
    # учитель подается назад, почти выходит из нее, но не до конца, потом снова входит
    img 15371
    m "Ох!"
    img 15372
    mt "Какое непонятное чувство... Что-то внизу живота и... ТАМ!"
    mt "Что он со мной делает?!"
    mt "Я хочу, чтобы он... Ах! ...чтобы он остановился!"
    # учитель ускоряется, Моника удивлена и испугана новыми ощущениями
    # в итоге сцены секса Моника не кончает, учитель кончит ей на ягодицы
    # Моника спешит одеться, ее бомбит, паника еще не прекратилась
    img 15373
    mt "!!!"
    img 15374
    w
    img 15375
    mt "Фуууу!!! Он испачкал меня!"
    mt "Долбанный высокоморальный извращенец!!! Что он натворил?!"
    img 15376
    mt "!!!"
    mt "..."
    mt "Чувствую себя также непонятно, как после вылизываний Барди и его друга..."
    img 15377
    mt "..."
    mt "Похоже это нервный срыв из-за всего за последнее время...!"
    # учитель застегивает штаны и садится за свой стол, довольный собой
    img 15378
    teacher "Я весьма рад такой благодарности от вас, миссис Бейкер!"
    teacher "Я давно хотел это сделать."
    # Моника убивает его взглядом
    img 15379
    mt "Он занялся со мной сексом (!!!) в классе, где сидят студенты!"
    mt "Я не хочу больше видеть этого учителя! Никогда! Ненавижу его!"
    mt "Ненавижу их всех! Больше никому не позволю прикасаться ко мне!!!"
    mt "!!!"
    img 15380
    teacher "Надеюсь, мы с вами еще увидимся, миссис Бейкер?" #широко улыбаясь
    # Моника еще раз убивает его взглядом
    img 15381
    mt "!!!"
    # Моника молча уходит
    return

# Город. Школьный двор. Моника, выйдя с колледжа.
label dialogue_classmate_14_1:
    # не рендерить!
    mt "Моей ноги больше не будет в этом чертовом колледже!"
    mt "!!!"
    mt "Надо сказать Барди, что я решила проблему!"
    return

# Дом. Комната Барди. Барди и Моника.
label dialogue_classmate_15:
    # Моника заходит в комнату Барди, тот сидит у ноута, Моника смотрит на него с неприязнью
    img 15156
    ц
    img 15157
    mt "Противная малявка! Сколько же проблем он мне создает своим существованием в моем доме."
    # Барди поворачивается к ней и с улыбочкой
    img 15158
    bardie "Ну как сходила, гувернантка? Надеюсь, у тебя все получилось уладить?"
    # Моника кипит от злости
    img 15159
    m "Да! Проблема Эрика решена!"
    m "Больше я в этот мерзкий колледж ни ногой! Ни при каких условиях!"
    m "Еще раз твой друг вляпается, сами будете разбираться!!!"
    # зло смотрит на него и уходит, не дожидаясь ответа
    return

label dialogue_classmate_15a:
    mt "Ненавижу эту малявку!"
    return
