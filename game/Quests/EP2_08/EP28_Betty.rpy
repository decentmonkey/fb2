label ep28_betty_init:
    $ add_hook("change_owner", "change_owner_default", scene="global", label="change_owner_default_hook")
    $ streetHouseMainYardBettySuffix = 1
    $ add_object_to_scene("Betty", {"type" : 2, "active":False, "base" : "Street_House_Betty_[streetHouseMainYardBettySuffix][day_suffix]", "click" : "street_house_main_yard_environment", "actions" : "l", "zorder":10, "tint": monica_tint}, scene="street_house_main_yard")
    $ floor1BettySuffix = 1
    $ add_object_to_scene("Betty", {"type" : 2, "active":False, "base" : "Floor1_Betty_[floor1BettySuffix][day_suffix]", "click" : "floor1_environment", "actions" : "l", "zorder":10}, scene="floor1")
    $ livingRoomBettySuffix = 1
    $ add_object_to_scene("Betty", {"type" : 2, "active":False, "base" : "House_LivingRoom_Betty_[livingRoomBettySuffix][day_suffix]", "click" : "living_room_environment", "actions" : "l", "zorder":11}, scene="living_room")

    $ move_object("Betty", "street_house_main_yard")
    $ add_hook("Betty", "dialogue_betty_college_1_1a", scene="street_house_main_yard", label="betty_college1", owner="Betty")
    $ add_hook("Betty", "dialogue_betty_college_1_1a", scene="floor1", label="betty_college1", owner="Betty")
    $ add_hook("Betty", "dialogue_betty_college_1_1a", scene="living_room", label="betty_college1", owner="Betty")

    $ add_hook("Teleport_House", "ep28_betty_teleport_floor1", scene="street_house_main_yard", label="betty_college1", owner="Betty")
    $ add_hook("Teleport_Street", "house_out_others", scene="floor1", label="betty_college1", owner="Betty")
    $ add_hook("Teleport_LivingRoom", "ep28_betty_teleport_living_room", scene="floor1", label="betty_college1", owner="Betty")
    $ add_hook("Teleport_Floor1", "ep28_betty_teleport_floor1", scene="living_room", label="betty_college1", owner="Betty")
    $ add_hook("Ralph", "ep28_betty_ralph", scene="living_room", label="betty_college1", owner="Betty")

    call change_owner("Betty")

    $ set_active("Betty", True, scene="House", recursive=True)

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
