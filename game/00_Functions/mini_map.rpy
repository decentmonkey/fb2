default miniMapData = []
default miniMapSubst = {}
default miniMapEnabledOnly = []
default miniMapDisabled = []
default miniMapDisabled2 = []
default miniMapOfficeActivated = False
default miniMapTurnedOff = False
default miniMapOpened = False
default miniMapOpenButtonImg = "Open_Button_Map1"
default miniMapOpenButtonImg2 = "Open_Button_Map2"

default miniMapHousePreset = "default"

label miniMapOpen:
    hide screen hud_minimap
    sound metal_slide
    $ miniMapOpened = True
    show screen hud_minimap(miniMapData)
    return
label miniMapClose:
    hide screen hud_minimap
    sound metal_slide
    $ miniMapOpened = False
    show screen hud_minimap(miniMapData)
    return

label miniMapHouseGenerate:
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_Map2"
    $ miniMapData = []
    if miniMapHousePreset == "default":
        $ miniMapData.append({"name":"Bedroom", "caption":_("Bedroom"), "img":"Bedroom_Map", "teleport_scene":"bedroom2", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Bathroom", "caption":_("Bathroom"), "img":"Bathroom_Map", "teleport_scene":"bathroom_bath", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Floor1", "caption":_("Down Floor"), "img":"Floor1_Map", "teleport_scene":"floor1", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Floor2", "caption":_("Up Floor"), "img":"Floor2_Map", "teleport_scene":"floor2", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Kitchen", "caption":_("Kitchen"), "img":"Kitchen_Map", "teleport_scene":"kitchen2", "teleport_type":"scene"})
    #    $ miniMapData.append({"name":"Basement", "caption":_("Basement"), "img":"Basement_Map", "teleport_scene":"basement_pool", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Street_Yard", "caption":_("Street Yard"), "img":"Street_Yard_Map", "teleport_scene":"house_out", "teleport_type":"function"})
        $ miniMapData.append({"name":"Basement", "caption":_("Basement"), "img":"Basement_Bedroom_Map", "teleport_scene":"basement_bedroom2", "teleport_type":"scene"})
    if miniMapHousePreset == "laundry":
        $ miniMapData.append({"name":"Bedroom", "caption":_("Bedroom"), "img":"Bedroom_Map", "teleport_scene":"bedroom2", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Bathroom", "caption":_("Bathroom"), "img":"Bathroom_Map", "teleport_scene":"bathroom_bath", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Floor1", "caption":_("Down Floor"), "img":"Floor1_Map", "teleport_scene":"floor1", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Floor2", "caption":_("Up Floor"), "img":"Floor2_Map", "teleport_scene":"floor2", "teleport_type":"scene"})
#        $ miniMapData.append({"name":"Kitchen", "caption":_("Kitchen"), "img":"Kitchen_Map", "teleport_scene":"kitchen2", "teleport_type":"scene"})
    #    $ miniMapData.append({"name":"Basement", "caption":_("Basement"), "img":"Basement_Map", "teleport_scene":"basement_pool", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Street_Yard", "caption":_("Street Yard"), "img":"Street_Yard_Map", "teleport_scene":"house_out", "teleport_type":"function"})
        $ miniMapData.append({"name":"Laundry", "caption":_("Laundry"), "img":"Basement_Laundry_Map", "teleport_scene":"basement_laundry", "teleport_type":"scene"})
        $ miniMapData.append({"name":"Basement", "caption":_("Basement"), "img":"Basement_Bedroom_Map", "teleport_scene":"basement_bedroom2", "teleport_type":"scene"})
    return

label miniMapHostelGenerate:
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_Hostel_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_Hostel_Map2"
    $ miniMapData = []
#    $ miniMapData.append({"name":"Hostel_Edge_1_c", "caption":_("BLIND ALLEY"), "img":"Hostel_Edge_1_c_Map", "teleport_scene":"enter_hostel_edge_1_c", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Street_Whores_Place_Shawarma", "caption":_("Shawarma"), "img":"Street_Whores_Place_Shawarma_Map", "teleport_scene":"whores_place_shawarma", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Street_Whores_Place_Whores", "caption":_("Whores place"), "img":"Street_Whores_Place_Whores_Map", "teleport_scene":"whores_place", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Street_Whores_Street1", "caption":_("Dirty street"), "img":"Street_Whores_Street1_Map", "teleport_scene":"whores_place_street1", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Street_Whores_Place_Car_Stop", "caption":_("Street Edge"), "img":"Street_Whores_Place_Car_Stop_Map", "teleport_scene":"street_corner", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Hostel_Street3", "caption":_("POOR STREET"), "img":"Hostel_Street3_Map", "teleport_scene":"hostel_street3", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Hostel_Street2", "caption":_("DIRTY STREET"), "img":"Hostel_Street2_Map", "teleport_scene":"hostel_street2", "teleport_type":"scene"})
    $ miniMapData.append({"name":"Hostel_Street", "caption":_("HOSTEL STREET"), "img":"Hostel_Street_Map", "teleport_scene":"hostel_street", "teleport_type":"scene"})
    return

label miniMapOfficeGenerate:
    if miniMapOfficeActivated == False:
        return
    $ miniMapOpened = False
    $ miniMapOpenButtonImg = "Open_Button_Office_Map1"
    $ miniMapOpenButtonImg2 = "Open_Button_Office_Map2"
    $ miniMapData = []
    $ miniMapData.append({"name":"Office_Biff_Cabinet", "caption":_("Biff's Office"), "img":"Office_Monica_Cabinet", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"monica_office_cabinet_table", "teleport_type":"function"})
    $ miniMapData.append({"name":"Working_Office_Cabinet", "caption":_("Monica's Office"), "img":"WorkingOfficeCabinet", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"working_office_cabinet", "teleport_type":"function"})
    $ miniMapData.append({"name":"Working_Office", "caption":_("Subordinates"), "img":"WorkingOffice", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"working_office", "teleport_type":"function"})
    $ miniMapData.append({"name":"Office_PhotoStudio", "caption":_("Photo Studiio"), "img":"Office_Monica_PhotoStudio", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"monica_office_photostudio", "teleport_type":"function"})
    $ miniMapData.append({"name":"Office_Monica_Secretary", "caption":_("Secretary"), "img":"Office_Monica_Secretary", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"monica_office_secretary", "teleport_type":"function"})
    $ miniMapData.append({"name":"Office_Entrance", "caption":_("Entrance"), "img":"Office_Entrance_Monica", "teleport_scene":"office_work_minimap_teleport", "teleport_scene_name":"monica_office_entrance", "teleport_type":"function"})
    return


label miniMapDisabled(name, minimapCell):
    sound snd_ui_not_working
    return

label miniMapAddDisabled(name):
    if name not in miniMapDisabled:
        $ miniMapDisabled.append(name)
    return

label miniMapRemoveDisabled(name):
    if name in miniMapDisabled:
        $ miniMapDisabled.remove(name)
    return

label miniMapHouseGenerateTeleport(name, minimapCell):
    $ target_scene_name = minimapCell["teleport_scene"]
    $ target_scene_parent = scene_get_parent(target_scene_name)
    call process_hooks("exit_scene", scene_name) from _call_process_hooks_25
    if _return == False:
        call refresh_scene() from _call_refresh_scene_3
        return
    $ exitHookCalled = True
    call process_hooks("mimimap_teleport", "global") from _call_process_hooks_26 #хук до инициализации сцены
    if _return == False:
        call refresh_scene() from _call_refresh_scene_4
        return
    if interface_blocked_flag == True:
        return
#    $ print renpy.get_screen("say")
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()
    $ _return = True
    if miniMapSubst.has_key("all") and miniMapSubst["all"] != False:
        call expression miniMapSubst["all"] from _call_expression_9
    if miniMapSubst.has_key(name) and miniMapSubst[name] != False:
        call expression miniMapSubst[name] from _call_expression_10
    if _return != False:
        if minimapCell["teleport_type"] == "function":
            call expression minimapCell["teleport_scene"] from _call_expression_11
        if minimapCell["teleport_type"] == "scene":
            call change_scene(minimapCell["teleport_scene"]) from _call_change_scene_150
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
