default pubMonicaSuffix = 1
default pubBartenderSuffix = 1
default pubBartenderWaitressSuffix = 1
default pubStripteaseGirl1Suffix = 1
default pubStripteaseGirl2Suffix = 1
default pubVisitor1Suffix = ""
default pubVisitor2Suffix = ""
default pubVisitor3Suffix = ""
default pubVisitor4Suffix = ""
default pubVisitor5Suffix = ""
default pubVisitor6Suffix = ""
default pubVisitor7Suffix = ""
default pubVisitor8Suffix = ""
default pubVisitor9Suffix = ""
default pubVisitor10Suffix = ""
default pubVisitor11Suffix = ""
default pubVisitor12Suffix = ""

label pub:
    $ print "enter_pub"
    $ miniMapData = []

    $ scene_image = "scene_pub"

    $ pubStripteaseGirl1Suffix = rand(1,4)
    $ pubStripteaseGirl2Suffix = rand(1,4)

    if get_active_objects("Pub_StripteaseGirl1", scene="pub") != False or get_active_objects("Pub_StripteaseGirl2", scene="pub") != False:
        music RocknRoll_loop
    else:
        music Indo_Rock2

    if get_active_objects(scene="pub", group="visitors") != False:
        music2 pub_noise1

    return
label pub_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"pub_Monica_[cloth][pubMonicaSuffix]", "click" : "pub_environment", "actions" : "l", "zorder" : 200})
#    $ add_object_to_scene("Teleport_pub_Door", {"type":2, "base":"pub_Teleport_pub2", "click" : "pub_teleport", "actions" : "lw", "zorder" : 0, "b":0.13, "tint":[1.0, 1.0, 0.7], "teleport":True})

    $ add_object_to_scene("Bartender", {"type" : 2, "base" : "Pub_Bartender[pubBartenderSuffix]", "click" : "pub_environment", "actions" : "lt", "zorder":30, "icon_t":"/Icons/talk" + res.suffix +".png"})
    $ add_object_to_scene("Bartender_Waitress", {"type" : 2, "base" : "Pub_Bartender_Waitress[pubBartenderWaitressSuffix]", "click" : "pub_environment", "actions" : "lt", "zorder":30})

    $ add_object_to_scene("Pub_StripteaseGirl1", {"type" : 2, "base" : "Pub_StripteaseGirl1_[pubStripteaseGirl1Suffix]", "click" : "pub_environment", "actions" : "lw", "zorder":0})
    $ add_object_to_scene("Pub_StripteaseGirl2", {"type" : 2, "base" : "Pub_StripteaseGirl2_[pubStripteaseGirl2Suffix]", "click" : "pub_environment", "actions" : "lw", "zorder":0})

    $ add_object_to_scene("Pub_Visitor1", {"type" : 2, "base" : "Pub_Visitor1[pubVisitor1Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":30, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})
    $ add_object_to_scene("Pub_Visitor2", {"type" : 2, "base" : "Pub_Visitor2[pubVisitor2Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":60, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})
    $ add_object_to_scene("Pub_Visitor3", {"type" : 2, "base" : "Pub_Visitor3[pubVisitor3Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":0, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"strip_lookers"})
    $ add_object_to_scene("Pub_Visitor4", {"type" : 2, "base" : "Pub_Visitor4[pubVisitor4Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":110, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})
    $ add_object_to_scene("Pub_Visitor5", {"type" : 2, "base" : "Pub_Visitor5[pubVisitor5Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":100, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})
    $ add_object_to_scene("Pub_Visitor6", {"type" : 2, "base" : "Pub_Visitor6[pubVisitor6Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":40, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})
    $ add_object_to_scene("Pub_Visitor7", {"type" : 2, "base" : "Pub_Visitor7[pubVisitor7Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":20, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"strip_lookers"})
    $ add_object_to_scene("Pub_Visitor8", {"type" : 2, "base" : "Pub_Visitor8[pubVisitor8Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":10, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors", "group2":"strip_lookers"})
    $ add_object_to_scene("Pub_Visitor9", {"type" : 2, "base" : "Pub_Visitor9[pubVisitor9Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":80, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})
    $ add_object_to_scene("Pub_Visitor10", {"type" : 2, "base" : "Pub_Visitor10[pubVisitor10Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":70, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})
    $ add_object_to_scene("Pub_Visitor11", {"type" : 2, "base" : "Pub_Visitor11[pubVisitor11Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":50, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})
    $ add_object_to_scene("Pub_Visitor12", {"type" : 2, "base" : "Pub_Visitor12[pubVisitor12Suffix]", "click" : "pub_visitors_default", "actions" : "lw", "zorder":90, "icon_t":"/Icons/talk" + res.suffix +".png", "group":"visitors"})

#    $ add_object_to_scene("Car", {"type":2, "base":"pub_Car", "click" : "pub_environment", "actions" : "l", "zorder" : 0})

    $ add_object_to_scene("Teleport_Hostel_Street", {"type":3, "text" : _("ВЫХОД ИЗ HOLE"), "rarrow" : "arrow_right_2", "base":"Pub_Teleport_Hostel_Street", "click" : "pub_teleport", "xpos" : 1379, "ypos" : 1023, "zorder":250, "teleport":True, "high_sprite_hover":True})

    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label pub_teleport:
    if obj_name == "Teleport_Hostel_Street":
        music2 stop
        call change_scene("hostel_street")
    return
label pub_environment:
    if obj_name == "Monica":
        pass

    return
