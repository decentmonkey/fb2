default publicEvent2MonicaSuffix = 1
label public_event2:
    $ print "enter_public_event2"
    $ miniMapData = []
    $ scene_image = "scene_PublicEvent2"

    music Stealth_Groover
    return

label public_event2_init:
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "PublicEvent2_Monica[publicEvent2MonicaSuffix]", "click" : "public_event2_environment", "actions" : "l", "zorder":16}, scene="public_event2")

    $ add_object_to_scene("Biff", {"type" : 2, "base" : "PublicEvent2_Biff", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("FitnessRebecca", {"type" : 2, "base" : "PublicEvent2_FitnessRebecca", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("FitnessStephanie", {"type" : 2, "base" : "PublicEvent2_FitnessStephanie", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("Investor1", {"type" : 2, "base" : "PublicEvent2_Investor1", "click" : "public_event2_environment", "actions" : "lt", "zorder":15}, scene="public_event2")
    $ add_object_to_scene("PublicGuest1", {"type" : 2, "base" : "PublicEvent2_PublicGuest1", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest2", {"type" : 2, "base" : "PublicEvent2_PublicGuest2", "click" : "public_event2_environment", "actions" : "lt", "zorder":11}, scene="public_event2")
    $ add_object_to_scene("PublicGuest3", {"type" : 2, "base" : "PublicEvent2_PublicGuest3", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest4", {"type" : 2, "base" : "PublicEvent2_PublicGuest4", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest5", {"type" : 2, "base" : "PublicEvent2_PublicGuest5", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest6", {"type" : 2, "base" : "PublicEvent2_PublicGuest6", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest7", {"type" : 2, "base" : "PublicEvent2_PublicGuest7", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    $ add_object_to_scene("PublicGuest8", {"type" : 2, "base" : "PublicEvent2_PublicGuest8", "click" : "public_event2_environment", "actions" : "lt", "zorder":10}, scene="public_event2")
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label public_event2_teleport:
    if obj_name == "Teleport_Bathroom":
        call change_scene("juliahome_bathroom")
    return
label public_event2_environment:
    if obj_name == "Monica":
        pass
    if obj_name == "Biff":
        pass
    if obj_name == "FitnessRebecca":
        pass
    if obj_name == "FitnessStephanie":
        pass
    if obj_name == "Investor1":
        pass
    if obj_name == "PublicGuest1":
        pass
    if obj_name == "PublicGuest2":
        pass
    if obj_name == "PublicGuest3":
        pass
    if obj_name == "PublicGuest4":
        pass
    if obj_name == "PublicGuest5":
        pass
    if obj_name == "PublicGuest6":
        pass
    if obj_name == "PublicGuest7":
        pass
    if obj_name == "PublicGuest8":
        pass
    return
