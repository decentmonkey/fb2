default monicaEatedLastDay = 0
default monicaEatedLastDayTime = "day"
default monicaCantSleepHungry = True

default monicaCleaningRoomsAmount = 2
default monicaCleaningInProgress = False
default monicaCleaningObject = ""

default monicaLastCleaningCompletedDay = 0 #Последний день, когда Моника убиралась в доме
default monicaLastCleaningOfferedDay = -1 #День, когда Монике предлагалась уборка в доме (предлагается один раз в день)

default monicaLastPissedDay = 0 # Последний день, когда Моника писала
default monicaLastPissedDayTime = "day"
default monicaLastShowerDay = 0 # Последний день, когда Моника принимала душ
default monicaLastShowerDayTime = ""

default monicaStoleFoodGasStationAmount = 0
default monicaStoleFoodTotal = 0
default monicaKebabWorkAmount = 0

default melanieOffended2 = False # Моника съязвила Мелани в фотостудии при встрече после Бифа
default monicaTalkedToMelanie1 = False
default monicaTryToDickBlowjob = False # Моника пыталась сделать Дику миньет

default hotelStaffOffended1 = False # Моника ругалась на hotelStaff за то что постер с ее изображением заслонен одеждой

default monicaOfferedBlowjobForBigMoney = False #Моника предложила сделать минет за $30 млн

label monicaEat: #кормим Монику
    $ monicaEatedLastDay = day #кормим Монику
    $ monicaEatedLastDayTime = day_time
    return
