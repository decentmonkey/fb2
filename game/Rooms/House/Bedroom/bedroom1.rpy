label bedroom1:
    $ print "enter_bedroom1"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_image = "scene_Bedroom1[day_suffix]"
    return

label bedroom1_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Bedroom1_Monica_[cloth][day_suffix]", "click" : "bedroom2_environment", "actions" : "l", "zorder":10}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom1_Monica_[cloth]_Cleaning_[monicaCleaningObject]"}})

#    if bettyLocation == "Bedroom1":
#        if day_time == "day":
    $ add_object_to_scene("Betty", {"type" : 2, "base" : "Bedroom1_Betty", "click" : "bettyInteract1", "actions" : "lt", "zorder":10, "active":False}, {"day_time":{"v":"evening", "base":"empty"}})

    $ add_object_to_scene("Chair", {"type":2, "base":"Bedroom1_Chair", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom1_Chair_Dust"}})
    $ add_object_to_scene("Chair2", {"type":2, "base":"Bedroom1_Chair2", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom1_Chair2_Dust"}})
    $ add_object_to_scene("Bed", {"type":2, "base":"Bedroom1_Bed", "click" : "bedroom1_environment", "actions" : "lh", "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom1_Bed_Dust", "actions":"l"}})
    $ add_object_to_scene("Curtains", {"type":2, "base":"Bedroom1_Curtains", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Flowers", {"type":2, "base":"Bedroom1_Flowers", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "b":0.12, "group":"environment"})
    $ add_object_to_scene("Lamp", {"type":2, "base":"Bedroom1_Lamp", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Mess", {"type":2, "base":"Bedroom1_Mess", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom1_Mess_Dust"}})
    $ add_object_to_scene("Mirror", {"type":2, "base":"Bedroom1_Mirror", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 11, "group":"environment"})
    $ add_object_to_scene("Table", {"type":2, "base":"Bedroom1_Table", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment"})
    $ add_object_to_scene("Windows", {"type":2, "base":"Bedroom1_Windows", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "c":1.0, "b":0.1, "group":"environment"})
    $ add_object_to_scene("Carpet", {"type":2, "base":"Bedroom1_Carpet", "click" : "bedroom1_environment", "actions" : "l", "zorder" : 0, "group":"environment", "cleaning_group":True}, {"monicaCleaningInProgress":{"v":True, "base":"Bedroom1_Carpet_Dust"}})

#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3
    $ add_object_to_scene("Teleport_Bedroom2", {"type":3, "text" : _("ГАРДЕРОБ"), "rarrow" : "arrow_right_2", "base":"Screen_Right_Arrow_Tight", "click" : "bedroom1_teleport", "xpos" : 1630, "ypos" : 920, "zorder":11, "teleport":True})
    return
#    jump show_scene

label bedroom1_teleport:
    if obj_name == "Teleport_Bedroom2":
        call change_scene("bedroom2")
    return

label bedroom1_environment:
    if obj_name == "Chair":
        mt "Мой любимый удобный стул... Эхххх...."
        return
    if obj_name == "Chair2":
        mt "Один из моих бывших стульев..."
        return
    if obj_name == "Bed":
        mt "Моя любимая кроватка!"
        "Она такая удобная!"
        "Как я скучаю по ней!"
        "Я ВЕРНУ ЕЕ!!!"
        return
    if obj_name == "Curtains":
        mt "Я помню как эти шторы спасали меня от солнечного света..."
        return

    if obj_name == "Flowers":
        mt "Мои цветы! Мои любимые цветы!"
        return
    if obj_name == "Lamp":
        mt "Я помню каждую лампу в моем доме..."
        return
    if obj_name == "Mess":
        mt "Я складывала сюда свои длинные ножки..."
        "Красивые, не то что у этой Бетти!"
        return
    if obj_name == "Mirror":
        mt "Я уверена что я скоро увижу себя в этом зеркале снова в дорогом платье!"
        return
    if obj_name == "Table":
        mt "Этот столик такой романтичный."
        "Я оставлю его после того как сменю дизайн этого дома."
        return
    if obj_name == "Windows":
        mt "Я помню вид из своего окна..."
        return
    if obj_name == "Carpet":
        mt "Мой коврик..."
        return
    elif obj_name == "none":
        "none ((("

    return
