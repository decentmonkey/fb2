default pubInited = False

label ep23_quests_pub_init: #инициализация локации бара
    $ pubInited = True
#    $ hostelStreetSceneName = "scene_Hostel_Street_Pub[day_suffix]"
    $ add_hook("enter_scene", "ep23_quests_pub", scene="hostel_street")
    $ add_object_to_scene("Teleport_Hostel_Pub", {"type":3, "text" : _("SHINY HOLE"), "larrow" : "arrow_down_2_a", "base":"Hostel_Street_Pub_Teleport_Pub", "click" : "hostel_street_teleport", "xpos" : 1641, "ypos" : 471, "zorder":16, "b":0.13, "tint":[1.0, 1.0, 0.7], "teleport":True, "high_sprite_hover":True}, scene="hostel_street")
    return
label ep23_quests_pub:
    $ remove_hook()
    call ep23_dialogues1_1()
    $ add_location("pub", caption=_("SHINY HOLE"), label="pub", init_label="pub_init", parent="Street_Corner")
    call Pub_Life_init()
    return
