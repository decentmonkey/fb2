default monicaEatedLastDay = 0
default monicaEatedLastDayTime = "day"
define monicaCantSleepHungry = False

default monicaCleaningRoomsAmount = 2
default monicaCleaningInProgress = False
default monicaCleaningObject = ""

default monicaLastCleaningCompletedDay = 0 #Последний день, когда Моника убиралась в доме
default monicaLastCleaningOfferedDay = -1 #День, когда Монике предлагалась уборка в доме (предлагается один раз в день)

default monicaLastPissedDay = 0 # Последний день, когда Моника писала
default monicaLastPissedDayTime = "day"
default monicaLastShowerDay = 0 # Последний день, когда Моника принимала душ
default monicaLastShowerDayTime = ""

label monicaEat: #кормим Монику
    $ monicaEatedLastDay = day #кормим Монику
    $ monicaEatedLastDayTime = day_time
    return
