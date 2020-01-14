default streetJuliaHomeMonicaSuffix = 1
default streetJuliaHomeJuliaSuffix = 1

label street_juliahome:
    $ print "enter_street_juliahome"
    $ miniMapData = []

    $ sceneIsStreet = True

    $ scene_image = "scene_Street_JuliaHome[day_suffix]"
    if day_time == "day":
        music street4
    else:
        if rand(1,4) > 1:
            music street_evening3
        else:
            music street13_ambulance
    return


label street_juliahome_init:
    $ add_object_to_scene("Monica", {"type":2, "base":"Street_JuliaHome_Monica_[cloth]_[streetPhilipHomeMonicaSuffix][day_suffix]", "click" : "street_juliahome_environment", "actions" : "l", "zorder" : 10}, scene="street_juliahome")
    $ add_object_to_scene("Julia", {"type":2, "base":"Street_JuliaHome_Julia_[streetJuliaHomeJuliaSuffix][day_suffix]", "click" : "street_juliahome_environment", "actions" : "lt", "zorder" : 5, "active":False}, scene="street_juliahome")

    $ add_object_to_scene("JuliaHome", {"type":2, "base":"Street_JuliaHome_JuliaHome", "click" : "street_juliahome_teleport", "actions" : "lw", "zorder" : 0, "group":"environment", "teleport":True}, scene="street_juliahome")
    $ add_object_to_scene("JuliaCafe", {"type":2, "base":"Street_JuliaHome_Cafe", "click" : "street_juliahome_teleport", "actions" : "lw", "zorder" : 0, "group":"environment", "teleport":True}, scene="street_juliahome")

    $ add_object_to_scene("Teleport_StreetCorner", {"type":3, "text" : _("УГОЛ УЛИЦЫ"), "larrow" : "arrow_right_2", "base":"Street_JuliaHome_Teleport_StreetEdge", "click" : "street_juliahome_teleport", "xpos" : 1613, "ypos" : 1003, "zorder":15, "teleport":True}, scene="street_juliahome")
    return

label street_juliahome_teleport:
    if obj_name == "Teleport_StreetCorner":
        call change_scene("street_corner", "Fade_long", "snd_walk_barefoot")
        return
    return

label street_juliahome_environment:
    if obj_name == "Monica":
        mt "Здесь живет Юлия..."
    return
