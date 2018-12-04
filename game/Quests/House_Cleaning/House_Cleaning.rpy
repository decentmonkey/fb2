label house_cleaning:
    # хук проверки на начало уборки
    if monicaCleaningInProgress == True:
        return
    if monicaLastCleaningOfferedDay == day:
        return

    $ monicaLastCleaningOfferedDay = day
    menu:
        "Начать уборку в доме.":
            call house_cleaning_start()
            return
        "Не убираться сегодня...":
            return
    return

label house_cleaning_start:
    # старт уборки
    $ monicaCleaningInProgress = True
    
    return
