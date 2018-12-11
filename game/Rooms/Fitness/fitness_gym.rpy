
label fitness_gym:
    $ print "enter_fitness_gym"
    $ miniMapData = []

    $ scene_name = "fitness_gym"
    $ scene_caption = _("Fitness Gym")
    $ scene_image = "scene_Fitness_Gym"

label fitness_gym_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Fitness_Gym_Trainer_Monica_" + cloth, "click" : "fitness_gym_environment", "actions" : "l", "zorder" : 12})
    $ add_object_to_scene("Trainer", {"type":2, "base":"Fitness_Gym_Trainer", "click" : "fitness_gym_environment", "actions" : "lt", "zorder" : 10, "icon_t":"/Icons/talk" + res.suffix +".png"})

    $ add_object_to_scene("Pictures", {"type":2, "base":"Fitness_Gym_Pictures", "click" : "fitness_gym_environment", "actions" : "l", "zorder" : 0})
    $ add_object_to_scene("Fitness_Equipment", {"type":2, "base":"Fitness_Gym_Fitness_Equipment", "click" : "fitness_gym_environment", "actions" : "l", "zorder" : 0, "tint": [1.0, 1.0, 0.8]})
    $ add_object_to_scene("Yoga_Carpet", {"type":2, "base":"Fitness_Gym_Yoga_Carpet", "click" : "fitness_gym_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Locker_1", {"type":3, "text" : _("В РАЗДЕВАЛКУ"), "rarrow" : "arrow_right_2", "base":"Fitness_Teleport_Locker_1", "click" : "fitness_gym_teleport", "xpos" : 609, "ypos" : 117, "zorder":11})
    $ add_object_to_scene("Teleport_Outside", {"type":3, "text" : _("НА УЛИЦУ"), "larrow" : "arrow_left_2", "base":"Fitness_Teleport_Outside", "click" : "fitness_gym_teleport", "xpos" : 1278, "ypos" : 91, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label fitness_gym_teleport:
    if obj_name == "Teleport_Outside":
        call change_scene("street_fitness")
        return
    if obj_name == "Teleport_Locker_1":
        call change_scene("fitness_locker_1")
        return

    return
label fitness_gym_environment:

    return
