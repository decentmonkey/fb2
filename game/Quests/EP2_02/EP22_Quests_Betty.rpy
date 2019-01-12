default ep22_quest_flag1 = False
default ep22_fitness_gym_inited = False

label EP22_Quests_Betty1: #init quest
    $ add_hook("Betty_Life_day", "EP22_Quests_Betty2", scene="global", label="betty_fitness_days")
    $ add_hook("Betty", "EP22_Quests_Betty3", scene="floor2")
    return

label EP22_Quests_Betty2: #определение дня фитнеса
    if week_day == 2 or week_day == 4:
        $ bettyFitnessToday = True
        $ move_object("Betty", "floor2")
        return False
    else:
        $ bettyFitnessToday = False
    return

label EP22_Quests_Betty3:
    if act=="l":
        return
    call ep22_dialogues4_1()
    if _return == False:
        if bettyFitnessToday == True:
            $ add_object_to_scene("Car", {"type" : 2, "base" : "Street_House_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":0, "b":0.15}, {"driverOnHouseYard":{"v":False, "active":False}}, scene="street_house_main_yard")
            $ move_object("Betty", "empty")
            $ move_object("Driver", "empty")
            call refresh_scene_fade()
        return False
    $ add_cleaning(True)
    $ add_hook("open", "EP22_Quests_Betty4", scene="street_fitness")
    call change_scene("street_fitness", "Fade_long", "snd_car_engine")
    return False

label EP22_Quests_Betty4: #инитим улицу у фитнеса
    $ fitnessStreetStoredScene = store_scene("street_fitness", recursive=True)
    $ add_hook("Teleport_Inside", "EP22_Quests_Betty5", scene="street_fitness")
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Street_Betty_Monica", "click" : "ep22_dialogues4_2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ add_object_to_scene("Betty", {"type":2, "base":"Fitness_Street_Betty", "click" : "ep22_dialogues4_2", "actions" : "l", "zorder" : 10}, scene="street_fitness")
    $ add_object_to_scene("Car", {"type":2, "base":"Street_Fitness_Car", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder" : 3}, scene="street_fitness")
    $ add_object_to_scene("Driver", {"type":2, "base":"Street_Fitness_Driver", "click" : "street_house_main_yard_environment", "actions" : "lt", "zorder" : 5, "icon_t":"/Icons/talk" + res.suffix +".png", "b":0.2, "s":1.3, "tint":[1.0, 1.0, 0.8]}, scene="street_fitness")
    $ map_enabled = False
    $ scene_image = "scene_Fitness_Street_Driver"
    $ autorun_to_object("ep22_dialogues4_1a", scene="street_fitness")
    if ep22_fitness_gym_inited == False:
        call fitness_gym_init()
        $ add_hook("Teleport_Outside", "ep22_dialogues4_2a", scene="fitness_gym")
        $ add_hook("Trainer", "ep22_dialogues4_4", scene="fitness_gym")
        $ add_hook("Monica", "ep22_dialogues4_4", scene="fitness_gym")
        $ add_hook("Betty", "ep22_dialogues4_4", scene="fitness_gym")
        $ ep22_fitness_gym_inited = True
#    $ restore_scene(fitnessStreetStoredScene)
    return

label EP22_Quests_Betty5:
    call change_scene("fitness_gym")
    return
