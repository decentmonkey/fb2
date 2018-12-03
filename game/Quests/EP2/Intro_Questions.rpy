label intro_questions:
    img 1201
    with fadelong
    help "Прежде чем начать игру, пожалуйста, напомните, как вела себя Моника в Эпизоде 1?"
    menu:
        "Ответить очень кратко.":
            call intro_questions_short()
        "Ответить очень подробно.":
            call intro_questions_long()
label intro_questions_long:
    img 1105
    with fadelong
    menu:
        "Моника общалась с соседом":
            $ neighborAsked = True
            $ neighborCalled = True
            menu:
                "Моника поздоровалась с соседом.":
                    call bitch(-2, "neighbor_dial1")

                "Моника не стала здороваться.":
                    call bitch(2, "neighbor_dial1")
                    $ neighborOffended1 = True

            menu:
                "Монике было все-равно что сосед чуть не погиб.":
                    $ neighborOffended2 = True
                    call bitch(2, "neighbor_dial2")
                "Моника проявила обеспокоенность.":
                    call bitch(-2, "neighbor_dial2")
            menu:
                "Моника сказала что сосед грязный.":
                    call bitch(2, "neighbor_dial3")
                    $ neighborOffended3 = True
                "Нет."
                    call bitch(-2, "neighbor_dial3")

            menu:
                "Ох ничего себе! Он сломал мне забор!":
                    call bitch(5, "neighbor_dial4")
                    $ neighborOffended4 = True
                "Эту царапину еле видно! Из-за чего весь шум?":
                    call bitch(-5, "neighbor_dial4")
            menu:
                "Моника прогнала соседа.":
                    $ neighborOffended5 = True
                "Моника закатила соседу большой иск.":
                    call bitch(10, "neighbor_suebig")
                    $ neighborOffendedSue = True
                    $ neighborOffendedSueBig = True
                    menu:
                        "Моника высказалась по поводу фермы соседа.":
                            $ neighborOffendedFarm = True
                            call bitch(3, "neighbor_offendfarm")
                        "Нет.":
                            pass
                "Моника решила отсудить маленькую сумму.":
                    $ neighborOffendedSue = True

        "Моника не видела соседа:":
            pass

    img 1035
    with fadelong
    menu:
        "Моника обращается с Юлией криком":
            $ juliaMonicaYell = True
            call bitch(5, "call_julia1")
        "Моника общается более вежливо.":
            call bitch(-5, "call_julia1")

    img 1080
    with fadelong
    menu:
        "Юлия наказана и убирает пятно все время.":
            $ juliaPunished = True
            call bitch(10, "monica_julia_revenge_punished")
            menu:
                "Моника простила Юлию после строгого наказания.":
                    $ juliaMonicaForgivenessAfterPunishment = True
                    call bitch(-20, "juliaMonicaForgivenessAfterPunishment")
                "Нет.":
                    pass
        "Юлия наказана криком, но пятно можно не убирать.":
            call bitch(-10, "monica_julia_revenge_punished")
            $ juliaPunishedLow = True
        "Юлия наказана и убирает пятно в свободное время."
            $ juliaPunishedVoluntarily = True
            call bitch(5, "monica_julia_revenge_punished_voluntarily")
        "Юлию не наказана за пятно никак."
            $ juliaPunishedNone = True
            call bitch(-10, "monica_julia_revenge_punished")
            call bitch(-5, "monica_julia_revenge_punished_voluntarily")

    menu:
        "Моника соврала про то что пятно поставила она."
            $ juliaMonicaLied = True
            call bitch(5, "monica_julia_revenge_lie")
        "Моника сказала правду про пятно."
            pass

    img 4082
    with fadelong
    menu:
        "Юлии пришлось заняться сексом со Фредом.":
            $ juliaHasSexInPool = True
            img 4090
            with fadelong
            menu:
                "Юлия не стала говорить Фреду что секс ей не понравился.":
                    $ juliaBasementSexLiked = True
                "Юлия взывала к совести Фреда.":
                    pass
        "Юлия не решилась на это...":
            pass

    img 1328
    with fadelong
    menu:
        "Моника сказала Стиву по телефону что он мешок с дерьмом.":
            $ steveOffended1 = True
            call bitch(2, "steve_offended1")
        "Нет.":

    img 1198
    with fadelong
    menu:
        "Моника обозвала моделей мартышками.":
            $ monkeysOffended1 = True
            call bitch(2, "monkeys_offend1")
        "Моника повела себя вежливо.":
            call bitch(-8, "monkeys_offend1")

    menu:
        "Моника заставила моделей полностью раздеться.":
            $ monkeysOffended2 = True
            $ monkeysOffended3 = True
            call bitch(2, "monkeys_offend2")
            call bitch(8, "monkeys_offend3")
        "Моника не стала издеваться на моделями.":
            pass

    img 1299
    with fadelong
    menu:
        "Моника показала моделям фотосессию Мелани.":
            $ melaniePhotoShotProcessed = True
            menu:
                "Моника накричала на моделей после фотосессии.":
                    $ monkeysOffended4 = True
                    call bitch(2, "monkeys_offend4")
        "Моника сказал моделям уйти.":
            pass
    img 1880
    with fadelong
    menu:
        "Моника смеялась над моделью, когда увидела ее работающей проституткой.":
            $ grayMouse2WhoreOffended = True
            call bitch(8, "dress_return_whore1")
        "Моника не стала смеяться над ней.":
            pass

    img 1308
    with fadelong
    menu:
        "Моника сказала Мелани, чтобы та следила за своей фигурой, иначе может уволить ее.":
            $ melanieOffended1 = True
            call bitch(2, "melanie_offended1")
        "Моника похвалила Мелани.":
            call bitch(-2, "melanie_offended1")

    menu:
        "Моника сказала Алексу, что он будет уволен если продолжит брать пикантные ракурсы.":
            $ alexPhotographOffended1 = True
            call bitch(2, "alexphotograph_offended1")
        "Моника попросила Алекса войти в ее положение.":
            call bitch(-2, "alexphotograph_offended1")


    img 1328
    with fadelong
    menu:
        "Моника сказала Дику что вокруг одни идиоты.":
            call bitch(2, "dick_phone_call1_dial1")
            $ dickMonicaIdiotsAround = True
        "Моника сказала Дику что она самостоятельная.":
            call bitch(-2, "dick_phone_call1_dial1")


    menu:
        "Моника сказала что не любит общаться с Диком.":
            $ dickMonicaOffended1 = True
            call bitch(2, "dick_phone_call1_dial2")
        "Моника согласилась на встречу.":
            pass


    img black_screen
    imgc 1390
    with fadelong
    menu:
        "Моника все время ругалась на Фреда.":
            call bitch(1, "fred_monica_office1")
            call bitch(1, "fred_monica_office2")
            call bitch(1, "fred_monica_office3")
            call bitch(1, "fred_monica_office4")
            call bitch(1, "fred_monica_fuel1")
            call bitch(2, "fred_monica_fuel2")
            call bitch(1, "fredOffendedDriveFitness1")
            call bitch(1, "fredOffendedDriveFitness2")
            call bitch(1, "fredOffendedDriveFitness4")
            call bitch(1, "fredOffendedDriveFitness3")

            $ fredOffendedRefuel = True
            $ fredOffendedRefuel2 = True
            $ fredOffendedDriveFitness1 = False # Едут на фитнесс. Фред, ты говоришь как болван.
            $ fredOffendedDriveFitness2 = False # У тебя есть в машине керосин?
            $ fredOffendedDriveFitness3 = False # Почти мне не интересно. Когда приедем, тогда скажи.
            $ fredOffendedDriveFitness4 = False # Продолжить задирать Фреда
            $ fredOffendedDriveReturnDress1 = False # И в этом другом мире нет всех этих нищих! Ты зеленый помидор, раздавленный на дороге!
        "Моника иногда ругалась на Фреда.":
            call bitch(1, "fred_monica_office4")
            call bitch(1, "fred_monica_fuel1")
            call bitch(2, "fred_monica_fuel2")
            call bitch(1, "fredOffendedDriveFitness1")
            call bitch(1, "fredOffendedDriveFitness2")
            $ fredOffendedRefuel = True
            $ fredOffendedDriveFitness1 = False # Едут на фитнесс. Фред, ты говоришь как болван.
            $ fredOffendedDriveFitness2 = False # У тебя есть в машине керосин?
        "Моника не ругалась на Фреда никогда.":
            pass

    img Gas_Station_Monica_OilTrader_18
    with fadelong
    menu:
        "Моника позвала продавщицу на заправке.":
            $ gasStationSaleswomanCalledOut = True
            call bitch(-10, "gas_saleswoman_decision")
        "Моника разбила бутылку, чтобы привлечь внимание.":
            $ gasStationSaleswomanMischiefed = True
            $ gasStationSaleswomanAlmostCummed = True
            call bitch(7, "gas_saleswoman_decision")
            menu:
                "Моника обвинила в этом кассиршу.":
                    $ gasStationMonicaLied = True
                    call bitch(10, "gas_station_monicalied")
                "Моника согласилась возместить ущерб.":
                    call bitch(-5, "gas_station_monicalied")


    img 1394
    with fadelong
    menu:
        "Моника при покупке платья общалась в продавцом грубо":
            $ clothShopCashierOffended2 = True
            call bitch(2, "clothShopCashierOffended2")
        "Вежливо.":
            call bitch(-2, "clothShopCashierOffended2")

    menu:
        "Моника заплатила за платье сама.":
            $ dressMonicaPaid = True
            call bitch(1, "dick_cloth_shop_peeping_dialogue3")
            $ dickClothShopOffended3 = True
            call bitch(1, "dick_cloth_shop_peeping_dialogue3")
        "За платье заплатил Дик.":
            pass
    menu:
        "Моника грубила когда возвращала платье.":
            $ clothShopCashierOffended3ReturnDress = True
            call bitch(3, "clothShopCashierOffended3ReturnDress")
        "Моника общалась вежливо.":
            call bitch(-3, "clothShopCashierOffended3ReturnDress")

    img 5640
    with fadelong
    menu:
        "Моника ругалась на продавца когда та застала ее утром в примерочной":
            $ clothShopCashierFirstNightOffended = True
            call bitch(5, "clothShopCashierFirstNightOffended")
        "Моника выкрутилась за счет вежливости.":
            call bitch(-5, "clothShopCashierFirstNightOffended")

    img 1437
    with fadelong
    menu:
        "Моника ругалась на Дика в машине и не стала подвозить его.":
            $ dickDriveDialOffend1 = True
            call bitch(1, "dickDriveDialOffend1")
            $ dickCarKickedOut = True
            call bitch(5, "dickCarKickedOut")
            $ dickDriveRestaurantOffended1 = True
            call bitch(1, "dickDriveRestaurantOffended1")
        "Моника общалась с Диком мило.":
            call bitch(-2, "dickCarKickedOut")

    menu:
        "Моника сказала Дику что он уродливый.":
            $ dickClothShopOffended1 = True
            call bitch(5, "dick_cloth_shop_peeping_dialogue1")
            $ dickClothShopOffended2 = TRUE
            call bitch(5, "dick_cloth_shop_peeping_dialogue2")
        "Моника только пошутила насчет галстука.":
            pass

    menu:
        "Моника назвала Дика плюшевым мишкой и сказала что он смешной.":
            $ dickClothShopOffended4 = True
            call bitch(1, "dickClothShopOffended4")
            $ richHotelRestaurantDickOffended1ChoiceMade = True
            call bitch(5, "richHotelRestaurantDickOffended1")
        "Моника назвала Дика кавалером.":
            call bitch(-1, "dickClothShopOffended4")

    img 1427
    menu:
        "Дик собирается помочь подать иск на соседа.":
            $ dickHelpsMoniceSue = True
        "Нет.":
            pass


    menu:
        "Дик проговорился что хочет Мелани.":
            $ richHotelRestaurantDickOffended1 = True
        "Нет.":
            pass

    menu:
        "Моника ругалась на официантку и сказала Дику ее уволить.":
            $ waitressMonicaOffended1 = True
            call bitch(3, "waitressMonicaOffended1")
            $ waitressMonicaFired = True
            call bitch(5, "waitressMonicaFired")
        "Моника попросила Дика оставить официантке чаевые.":
            call bitch(-3, "waitressMonicaOffended1")
            $ waitressMonicaTips = True
            call bitch(-5, "waitressMonicaTips")


    menu:
        "Моника сказала Фреду что Дик жирный урод.":
            call bitch(1, "dickMonicaSaidToFredOffend")
            $ dickMonicaSaidToFredOffend = True
        "Моника сказала Фреду что Дик старался угодить ей.":
            call bitch(-1, "dickMonicaSaidToFredOffend")


    img 4591
    with fadelong
    menu:
        "У Фреда был секс с Кристиной.":
            $ christineFuckedByFred = True
            img 4621
            with fadelong
            menu:
                "У Фреда с Кристиной был миньет и анал.":
                    $ christineFuckedByFredBlowjob = True
                    $ christineFuckedByFredAnal = True
                "Кристина не выдержала и убежала.":
        "Нет.":
            pass

    img 1646
    with fadelong
    menu:
        "Моника грубо отшила инструктора по фитнесу":
            call bitch(1, "fitness_trainer1")
            $ fitness1_trainer_talk2_choice_rough = True
        "Вежливо отказала.":
            call bitch(-1, "fitness_trainer1")
    img 4757
    menu:
        "У Stephanie был секс с инструктором":
            $ stephanieFitnessJustSex = True
        "Нет.":
            pass

    img 1667
    with fadelong
    menu:
        "Моника ругалась на клерка в банке.":
            $ clerksOffended = True
            call bitch(2, "bank_office1")
        "Моника вошла в положение.":
            call bitch(-2, "bank_office1")

    img 1822
    menu:
        "Моника сказала Стиву что он отсосет у собаки если соврал.":
            $ monicaSteveDogOffended = True
            call bitch(4, "steve_dog_offend")
        "Моника не стала такого говорить.":
            pass

    img 1974
    with fadelong
    menu:
        "Моника решила уволилить Юлию":
            $ juliaFirePlanned = True
            call bitch(5, "juliaFirePlanned")
            menu:
                "Моника в итоге пожалела Юлию и не стала увольнять ее":
                    $ juliaFireCancelled = True
                    call bitch(-3, "julia_firing")
                "Уволила.":
                    pass

        "Нет.":
            call bitch(-5, "juliaFirePlanned")

    menu:
        "Моника запланировала уволить Тиффани и Джейн":
            $ janeTiffanyFirePlanned = True
            call bitch(5, "janeTiffanyFirePlanned")
        "Моника решила еще проследить за ними.":
            call bitch(-5, "janeTiffanyFirePlanned")


    menu:
        "Моника запланировала уволить Фреда":
            $ fredFirePlanned = True
            call bitch(5, "fredFirePlanned")
        "Моника решила еще подумать над этим.":
            call bitch(-5, "fredFirePlanned")


    if bitchmeterValue <= maxBitchness_EP1 / 2:
        img 5176
        with fadelong
        menu:
            "Моника показывала Бобу грудь за еду.":
                $ jailBoobsForFoodShowed = True
            "Моника показала грудь заключенным, чтобы узнать имя Боба":
                $ jailCageShowedBoobsForBobName = True

    img 5338
    with fadelong
    menu:
        "Моника показала заключенным грудь во время шантажа.":
            $ jailCageBlackmailBoobsShowed = True
            img 5406
            with fadelong
            menu:
                "Моника показала заключенным зад.":
                    $ jailCageBlackmailAssShowed = True
                    img 5412
                    with fadelong
                    menu:
                        "Моника сказала что она хорошая шлюха.":
                            $ jailCageBlackmailMonicaSaidSheIsAWhore = True
                        "Моника отказалась это говорить.":
                            pass
                "Моника поставила заключенных на место.":
                    pass

        "Моника поставила заключенных на место.":
            pass

    img 3114
    with fadelong
    menu:
        "Моника накричала на Дика в его кабинете.":
            $ dickMonicaCabinetOffended = True
            call bitch(2, "dickMonicaCabinetOffended")
        "Моника пробовала уговорить Дика.":
            call bitch(-1, "dickMonicaCabinetOffended")

    img 5900
    menu:
        "Моника делала миньет Фреду.":
            $ monicaFredWasForcedBlowjob = True
            img 5904
            menu:
                "Моника проглотила сперму Фреда.":
                    $ monicaFredWasSpermEat = True
                "Моника выплюнула сперму Фреда.":
        "Моника обошлась без миньета.":
            pass


    return

label intro_questions_short:
    img 1200
    with fadelong
    menu:
        "Моника вела себя как сучка!":
            $ neighborAsked = True
            $ neighborCalled = True
            $ neighborOffended1 = True
            call bitch(2, "neighbor_dial1")
            $ neighborOffended2 = True
            call bitch(2, "neighbor_dial2")
            $ neighborOffended3 = True
            call bitch(2, "neighbor_dial3")
            $ neighborOffended4 = True
            call bitch(5, "neighbor_dial4")
            call bitch(10, "neighbor_suebig")
            $ neighborOffendedSue = True
            $ neighborOffendedSueBig = True
            $ neighborOffendedFarm = True

            call bitch(3, "neighbor_offendfarm")
            $ juliaMonicaYell = True
            call bitch(5, "call_julia1")
            $ juliaPunished = True
            call bitch(10, "monica_julia_revenge_punished")
            $ juliaMonicaLied = True
            call bitch(5, "monica_julia_revenge_lie")
            $ juliaHasSexInPool = True
            $ juliaBasementSexLiked = True
            $ steveOffended1 = True
            call bitch(2, "steve_offended1")
            $ monkeysOffended1 = True
            call bitch(2, "monkeys_offend1")
            $ monkeysOffended2 = True
            $ monkeysOffended3 = True
            call bitch(2, "monkeys_offend2")
            call bitch(8, "monkeys_offend3")
            $ melaniePhotoShotProcessed = True
            $ monkeysOffended4 = True
            call bitch(2, "monkeys_offend4")
            $ grayMouse2WhoreOffended = True
            call bitch(8, "dress_return_whore1")
            $ melanieOffended1 = True
            call bitch(2, "melanie_offended1")
            $ alexPhotographOffended1 = True
            call bitch(2, "alexphotograph_offended1")
            call bitch(2, "dick_phone_call1_dial1")
            $ dickMonicaIdiotsAround = True
            $ dickMonicaOffended1 = True
            call bitch(2, "dick_phone_call1_dial2")
            call bitch(1, "fred_monica_office1")
            call bitch(1, "fred_monica_office2")
            call bitch(1, "fred_monica_office3")
            call bitch(1, "fred_monica_office4")
            call bitch(1, "fred_monica_fuel1")
            call bitch(2, "fred_monica_fuel2")
            call bitch(1, "fredOffendedDriveFitness1")
            call bitch(1, "fredOffendedDriveFitness2")
            call bitch(1, "fredOffendedDriveFitness4")
            call bitch(1, "fredOffendedDriveFitness3")

            $ fredOffendedRefuel = True
            $ fredOffendedRefuel2 = True
            $ fredOffendedDriveFitness1 = False # Едут на фитнесс. Фред, ты говоришь как болван.
            $ fredOffendedDriveFitness2 = False # У тебя есть в машине керосин?
            $ fredOffendedDriveFitness3 = False # Почти мне не интересно. Когда приедем, тогда скажи.
            $ fredOffendedDriveFitness4 = False # Продолжить задирать Фреда
            $ fredOffendedDriveReturnDress1 = False # И в этом другом мире нет всех этих нищих! Ты зеленый помидор, раздавленный на дороге!
            $ gasStationSaleswomanMischiefed = True
            $ gasStationSaleswomanAlmostCummed = True
            call bitch(7, "gas_saleswoman_decision")
            call bitch(10, "gas_station_monicalied")
            $ gasStationMonicaLied = True
            $ clothShopCashierOffended2 = True
            call bitch(2, "clothShopCashierOffended2")
            $ dressMonicaPaid = True
            call bitch(1, "dick_cloth_shop_peeping_dialogue3")
            $ dickClothShopOffended3 = True
            call bitch(1, "dick_cloth_shop_peeping_dialogue3")
            $ clothShopCashierOffended3ReturnDress = True
            call bitch(3, "clothShopCashierOffended3ReturnDress")
            $ clothShopCashierFirstNightOffended = True
            call bitch(5, "clothShopCashierFirstNightOffended")
            $ dickDriveDialOffend1 = True
            call bitch(1, "dickDriveDialOffend1")
            $ dickCarKickedOut = True
            call bitch(5, "dickCarKickedOut")
            $ dickDriveRestaurantOffended1 = True
            call bitch(1, "dickDriveRestaurantOffended1")
            $ dickClothShopOffended1 = True
            call bitch(5, "dick_cloth_shop_peeping_dialogue1")
            $ dickClothShopOffended2 = TRUE
            call bitch(5, "dick_cloth_shop_peeping_dialogue2")
            $ dickClothShopOffended4 = True
            call bitch(1, "dickClothShopOffended4")
            $ richHotelRestaurantDickOffended1ChoiceMade = True
            call bitch(5, "richHotelRestaurantDickOffended1")
            $ dickHelpsMoniceSue = True
            $ richHotelRestaurantDickOffended1 = True
            $ waitressMonicaOffended1 = True
            call bitch(3, "waitressMonicaOffended1")
            $ waitressMonicaFired = True
            call bitch(5, "waitressMonicaFired")
            call bitch(1, "dickMonicaSaidToFredOffend")
            $ dickMonicaSaidToFredOffend = True
            $ christineFuckedByFred = True
            $ christineFuckedByFredBlowjob = True
            $ christineFuckedByFredAnal = True
            call bitch(1, "fitness_trainer1")
            $ fitness1_trainer_talk2_choice_rough = True
            $ stephanieFitnessJustSex = True
            $ clerksOffended = True
            call bitch(2, "bank_office1")
            $ monicaSteveDogOffended = True
            call bitch(4, "steve_dog_offend")
            $ juliaFirePlanned = True
            call bitch(5, "juliaFirePlanned")
            $ janeTiffanyFirePlanned = True
            call bitch(5, "janeTiffanyFirePlanned")
            $ fredFirePlanned = True
            call bitch(5, "fredFirePlanned")
            $ jailCageBlackmailBoobsShowed = True
            $ jailCageBlackmailAssShowed = True
            $ jailCageBlackmailMonicaSaidSheIsAWhore = True
            $ dickMonicaCabinetOffended = True
            call bitch(2, "dickMonicaCabinetOffended")
            $ monicaFredWasForcedBlowjob = True
            $ monicaFredWasSpermEat = True
        "Моника старалась быть вежливой насколько умеет...":
            $ neighborAsked = True
            $ neighborCalled = True
            call bitch(-2, "neighbor_dial1")
            call bitch(-2, "neighbor_dial2")
            call bitch(-2, "neighbor_dial3")
            call bitch(-5, "neighbor_dial4")
            call bitch(-5, "call_julia1")
            $ juliaPunishedNone = True
            call bitch(-10, "monica_julia_revenge_punished")
            call bitch(-5, "monica_julia_revenge_punished_voluntarily")
            $ juliaHasSexInPool = True
            $ juliaBasementSexLiked = True
            call bitch(-8, "monkeys_offend1")
            $ melaniePhotoShotProcessed = True
            call bitch(-2, "melanie_offended1")
            call bitch(-2, "alexphotograph_offended1")
            call bitch(-2, "dick_phone_call1_dial1")
            $ gasStationSaleswomanCalledOut = True
            call bitch(-10, "gas_saleswoman_decision")
            call bitch(-2, "clothShopCashierOffended2")
            call bitch(-3, "clothShopCashierOffended3ReturnDress")
            call bitch(-5, "clothShopCashierFirstNightOffended")
            call bitch(-2, "dickCarKickedOut")
            call bitch(-1, "dickClothShopOffended4")
            call bitch(-3, "waitressMonicaOffended1")
            $ waitressMonicaTips = True
            call bitch(-5, "waitressMonicaTips")
            call bitch(-1, "dickMonicaSaidToFredOffend")
            call bitch(-1, "fitness_trainer1")
            $ stephanieFitnessJustSex = True
            call bitch(-2, "bank_office1")
            call bitch(-5, "juliaFirePlanned")
            call bitch(-5, "janeTiffanyFirePlanned")
            call bitch(-5, "fredFirePlanned")
            $ jailBoobsForFoodShowed = True
            $ jailCageShowedBoobsForBobName = True
            $ jailCageBlackmailBoobsShowed = True
            $ jailCageBlackmailAssShowed = True
            $ jailCageBlackmailMonicaSaidSheIsAWhore = True
            call bitch(-1, "dickMonicaCabinetOffended")
            $ monicaFredWasForcedBlowjob = True
            $ monicaFredWasSpermEat = True
    return
