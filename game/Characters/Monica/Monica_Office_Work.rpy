default cloth_before_work = False # одежда перед входом на работу
default cloth_type_before_work = False
default officeWorkingLog = []

init python:
    def add_office_working_day(status): #True - был рабочий день, #False - не было рабочего дня
        global cleaningLog
        officeWorkingLog.insert(0, status)
        return

    def get_office_working_status(days): # Подсчитывает кол-во пропусков работы за последние days дней
        # На входе необходимое кол-во дней
        if len(officeWorkingLog) < days:
            return False
#        need_amount = days
        working_days_amount = 0
        for idx1 in range(0,days):
            if officeWorkingLog[idx1] == True:
                working_days_amount = working_days_amount + 1
        return working_days_amount



label put_work_clothes:
    if cloth_type != "WorkingOutfit":
        $ cloth_before_work = cloth
        $ cloth_type_before_work = cloth_type
        $ cloth = "WorkingOutfit1"
        $ cloth_type = "WorkingOutfit"
    return
label putoff_work_clothes:
    $ cloth = cloth_before_work
    $ cloth_type = cloth_type_before_work
    return


label office_work_init:
    # Первичная инициализация

    # жизнь офиса
    $ add_hook("change_time_day", "office_life_day", scene="global")
    $ add_hook("change_time_evening", "office_life_evening", scene="global")
    $ add_hook("office_life_day", "office_life_day1", scene="global")
    $ add_hook("office_life_evening", "office_life_evening1", scene="global")
    call process_hooks("office_life_evening", "global")

    # вход/выход из офиса
    $ add_hook("Teleport_Monica_Office_Entrance", "office_work_lift", scene="monica_office_secretary", label="office_lift")
    $ add_hook("Teleport_Monica_Office_Secretary", "office_work_lift", scene="monica_office_entrance", label="office_lift")
    $ add_hook("Teleport_Monica_Office_Lift", "office_work_lift", scene="working_office", label="office_lift")

    $ add_hook("change_time_day", "office_work_init_next_morning", scene="global")

    # Инициализация локаций
    call locations_init_working_office()

    # Инициализация мини-карты
    $ miniMapOfficeActivated = True
    return

label office_work_init_next_morning:
    $ remove_hook()
    $ questLog(43, True)
    return

label office_life_day:
    call process_hooks("office_life_day", "global")
    return True


label office_life_evening:
    call process_hooks("office_life_evening", "global")
    return True

label office_life_day1:
#    $ move_object("Biff", "empty")
    return

label office_life_evening1:
    return


label office_work_lift:
    call ep26_dialogues6_office2_1_lift()
    if _return == 1:
        if scene_name == "monica_office_secretary":
            return False
        # Этаж модного журнала
        if cloth_type != "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call put_work_clothes()
        call change_scene("monica_office_secretary", "Fade_long", "snd_lift")
        return False
    if _return == 2:
        # Отдел Моники
        if scene_name == "working_office":
            return False
        if cloth_type != "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call put_work_clothes()
        call change_scene("working_office", "Fade_long", "snd_lift")
        return False
    if _return == 3:
        # Вестибюль
        if scene_name == "monica_office_entrance":
            return False
        if cloth_type == "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call putoff_work_clothes()
        call change_scene("monica_office_entrance", "Fade_long", "snd_lift")
        return False
    return

label office_work_minimap_teleport:
    #minimapCell["teleport_scene_name"]
    $ target_scene = minimapCell["teleport_scene_name"]
    $ print target_scene
    if target_scene == scene_name:
        call refresh_scene_fade()
        return
    if target_scene == "monica_office_entrance":
        if cloth_type == "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call putoff_work_clothes()
    if scene_name == "monica_office_entrance":
        if cloth_type != "WorkingOutfit":
            img black_screen
            with diss
            sound snd_fabric1
            pause 1.0
            call put_work_clothes()
    if (target_scene == "monica_office_photostudio" or target_scene == "monica_office_cabinet_table" or target_scene == "monica_office_secretary" or target_scene=="monica_office_secretary_teatable" or target_scene == "monica_office_makeup_room") and (scene_name == "monica_office_photostudio" or scene_name == "monica_office_cabinet_table" or scene_name == "monica_office_secretary" or scene_name=="monica_office_secretary_teatable" or scene_name == "monica_office_makeup_room"):
        call change_scene(target_scene, "Fade_long")
        return
    if (target_scene == "working_office" or target_scene == "working_office2" or target_scene == "working_office_cabinet" or target_scene =="working_office_cabinet2") and (scene_name == "working_office" or scene_name == "working_office2" or scene_name == "working_office_cabinet" or scene_name =="working_office_cabinet2"):
        call change_scene(target_scene, "Fade_long")
        return
    call change_scene(target_scene, "Fade_long", "snd_lift")
    return
