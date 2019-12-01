default ep29_revenge_quest1_inited = False

label ep29_revenge_quest1_init:
    if ep29_revenge_quest1_inited == True:
        return
    $ ep29_revenge_quest1_inited = True
    # вешаем проверку на revenge quest при входе в спальню
    $ add_hook("before_open", "ep29_revenge_quest1_check", scene="basement_bedroom2", label="ep29_revenge_quest1_check", quest="revenge_quest")
    if marcus_visit1_completed == True:
        call basement_bedroom2_init2() # Оставляем в basement_bedroom2 анальную пробку
        return
    return
label ep29_revenge_quest1_check:
    if cloth != "Governess":
        return
    m "here"
    if marcus_visit1_completed != True:
        pass
    return
