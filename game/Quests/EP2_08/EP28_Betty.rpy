label ep28_betty_init:
    $ add_hook("change_owner", "change_owner_default", scene="global", label="change_owner_default_hook")
    $ streetHouseMainYardBettySuffix = 1
    $ add_object_to_scene("Betty", {"type" : 2, "active":False, "base" : "Street_House_Betty_[streetHouseMainYardBettySuffix][day_suffix]", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, scene="street_house_main_yard")
    $ floor1BettySuffix = 1
    $ add_object_to_scene("Betty", {"type" : 2, "active":False, "base" : "Floor1_Betty_[floor1BettySuffix][day_suffix]", "click" : "floor1_environment", "actions" : "l", "zorder":10}, scene="floor1")
    $ livingRoomBettySuffix = 1
    $ add_object_to_scene("Betty", {"type" : 2, "active":False, "base" : "House_LivingRoom_Betty_[livingRoomBettySuffix][day_suffix]", "click" : "living_room_environment", "actions" : "l", "zorder":11}, scene="living_room")

#    $ move_object("Betty", "street_house_main_yard")
    $ set_active("Betty", True, scene="World", recursive=True)
    $ add_hook("Betty", "dialogue_betty_college_1_1a", scene="street_house_main_yard", label="betty_college1", owner="Betty")
    $ add_hook("Betty", "dialogue_betty_college_1_1a", scene="floor1", label="betty_college1", owner="Betty")
    $ add_hook("Betty", "dialogue_betty_college_1_1a", scene="living_room", label="betty_college1", owner="Betty")

    $ add_hook("Teleport_Gate", "ep28_betty_teleport_map", scene="street_house_main_yard", label=["betty_college1", "betty_college_map_teleport"], owner="Betty")
    $ add_hook("Teleport_House", "ep28_betty_teleport_floor1", scene="street_house_main_yard", label="betty_college1", owner="Betty")
    $ add_hook("Teleport_Street", "house_out_others", scene="floor1", label="betty_college1", owner="Betty")
    $ add_hook("Teleport_LivingRoom", "ep28_betty_teleport_living_room", scene="floor1", label="betty_college1", owner="Betty")
    $ add_hook("Teleport_Floor1", "ep28_betty_teleport_floor1", scene="living_room", label="betty_college1", owner="Betty")

#    $ add_hook("Close", "ep28_betty_map_close", scene="map", label="map_owner_betty", owner="Betty")


#    $ set_var("Close", owners_visible_forced = True, scene="map")
    $ add_hook("enter_scene", "dialogue_betty_college_1_1i", scene="floor1", owner="Betty", once=True)
    $ add_hook("Chandelier", "ep28_betty_house_comment1", scene="floor1", label="betty_house_comments1", owner="Betty")
    $ add_hook("Curtains", "ep28_betty_house_comment1", scene="floor1", label="betty_house_comments1", owner="Betty")
    $ add_hook("Lamps", "ep28_betty_house_comment1", scene="floor1", label="betty_house_comments1", owner="Betty")
    $ add_hook("Picture", "ep28_betty_house_comment1", scene="floor1", label="betty_house_comments1", owner="Betty")
    $ add_hook("Furniture", "ep28_betty_house_comment1", scene="floor1", label="betty_house_comments1", owner="Betty")

    $ add_hook("Ralph", "ep28_betty_ralph", scene="living_room", label="betty_college1", owner="Betty")

    call change_owner("Betty")
    $ map_objects = {
            "Teleport_College" : {"text" : _("КОЛЛЕДЖ"), "xpos" : 174, "ypos" : 579, "base" : "map_marker", "state" : "visible", "owner":"Betty"},
            "Teleport_House" : {"text" : _("ДОМ МОНИКИ"), "xpos" : 105, "ypos" : 798, "base" : "map_marker_house", "state" : "active", "owner":"Betty"}
    }
    $ set_active("Betty", True, scene="House", recursive=True)

    $ hudDaySkipToEveningEnabled = False
    call change_scene("street_house_main_yard")
    return

label ep28_betty_teleport_floor1:
    call change_scene("floor1")
    return

label ep28_betty_teleport_living_room:
    call change_scene("living_room")
    return

label ep28_betty_ralph:
    if act=="l":
        call dialogue_betty_college_1_1e() # Смотрит на Ральфа
        return
    call dialogue_betty_college_1_1f() # Говорит с Ральфом

    return

label ep28_betty_teleport_map:
    call map_show()
    return


label ep28_betty_map_close:
    call map_close()
    return

label ep28_betty_house_comment1:
    call dialogue_betty_college_1_1j()
    return
