default ep22_quests_biff_init_flag = False
default ep22_quests_biff1_day = 0
default ep22_quests_biff2_day = 0

default ep22_quests_monica_agreed_change_cloth = False
default ep22_quests_monica_presentation_completed = False

label ep22_quests_biff_init:
    call ep210_dialogues1_office_biff_1()
    if _return == False:
        return
    $ ep22_quests_monica_agreed_change_cloth = True
    $ add_objective("visit_biff_tomorrow", _("Зайти завтра к Бифу, узнать про работу."), c_blue, 35)
    $ add_hook("Biff", "ep22_quests_biff1", scene="monica_office_cabinet_table", label="ep22_quests_biff1")
    $ add_hook("Secretary", "ep22_quests_biff1_secretary", scene="monica_office_secretary", label="ep22_quests_biff1_secretary")
    $ add_hook("Teleport_Street_Monica_Office", "ep210_dialogues1_office_biff_2a", scene="monica_office_entrance", label=["ep22_quests_biff1_exit", "ep22_quests_biff1"])
    $ ep22_quests_biff1_day = day
    $ ep22_quests_biff_init_flag = True
    return

label ep22_quests_biff1:
    # Второй день (разговор о презентации)
    if act=="l":
        return
    if ep22_quests_biff1_day == day:
        call ep210_dialogues1_office_biff_2b()
        call change_scene("monica_office_cabinet")
        return False
    $ remove_objective("visit_biff_tomorrow")
    $ remove_hook(label="ep22_quests_biff1_exit") # Разблокируем выход независимо от результата разговора
    call ep210_dialogues1_office_biff_3()
    if _return == False:
        call change_scene("monica_office_cabinet")
        return False

    $ ep22_quests_biff2_day = day
    $ add_objective("visit_biff_presentation", _("Провести презентацию журнала в кабинете Бифа."), c_orange, 55)
    $ add_hook("before_open", "ep22_quests_biff2", scene="monica_office_cabinet_table", label="ep22_quests_biff2")
    $ add_hook("before_open", "ep22_quests_biff2", scene="monica_office_cabinet", label="ep22_quests_biff2")
    $ add_hook("Teleport_Street_Monica_Office", "ep210_dialogues1_office_biff_3a", scene="monica_office_entrance", label=["ep22_quests_biff2_exit", "ep22_quests_biff2"])

    $ remove_hook(label="ep22_quests_biff1")
    call change_scene("monica_office_cabinet")
    return False

label ep22_quests_biff1_secretary: # После переодевания Моника подходит к секретарше
    if act=="l":
        return
    $ remove_hook()
    if day - ep22_quests_biff1_day < 3: # Подошла к ней в ближайшие дни
        call ep210_dialogues1_office_biff_2()
    return False


label ep22_quests_biff2:
    # Третий день (презентация)
    if ep22_quests_biff2_day == day or get_active_objects("Biff", scene="monica_office_cabinet") == False:
        return
    call ep210_dialogues1_office_biff_4()
    call ep210_dialogues1_office_biff_5() # Разговор с Бифом
    $ ep22_quests_monica_presentation_completed = True
    $ biffLevel3Opened = True
    $ remove_objective("visit_biff_presentation")
    $ add_char_progress("Biff", 10, "ep22_quests_monica_presentation_completed")
    $ char_info["Biff"]["enabled"] = True
    $ char_info["Biff"]["caption"] = _("Мне надо развлекать этого мерзавца, чтобы он меня не выгнал с работы...")
    call change_scene("monica_office_secretary", "Fade_long")
    $ remove_hook(label="ep22_quests_biff2")
    return False


















#
