label locations_init:
    #MAP
    $ add_location("map", caption="", label="map", parent="World")
    $ add_location("Monica_Office", caption="", label="empty_label", parent="World")
    $ add_location("Street_Corner", caption="", label="empty_label", parent="World")
    $ add_location("Dick_Office", caption="", label="empty_label", parent="World")
    $ add_location("Gas_Station", caption="", label="empty_label", parent="World")
    $ add_location("Police", caption="", label="empty_label", parent="World")
    $ add_location("Rich_Hotel", caption="", label="empty_label", parent="World")
    $ add_location("Fitness", caption="", label="empty_label", parent="World")
    $ add_location("Steve_Office", caption="", label="empty_label", parent="World")
    $ add_location("Bank", caption="", label="empty_label", parent="World")
    $ add_location("Cloth_Shop", caption="", label="empty_label", parent="World")
    $ add_location("Street_Corner", caption="", label="empty_label", parent="World")
    $ add_location("Hostel2", caption="", label="empty_label", parent="World")
    $ add_location("House", caption="", label="empty_label", parent="World")

    #BANK
    $ add_location("bank_office", caption=_("BANK"), label="bank_office", init_label="bank_office_init", parent="bank_office")
    $ add_location("street_bank", caption=_("BANK"), label="street_bank", init_label="street_bank_init", parent="Bank")

    #CLOTHING SHOP
    $ add_location("street_cloth_shop", caption=_("Clothing Shop"), label="street_cloth_shop", init_label="street_cloth_shop_init", parent="Cloth_Shop")

    #DICK OFFICE
    $ add_location("street_dick_office", caption=_("Dick's Office"), label="street_dick_office", init_label="street_dick_office_init", parent="Dick_Office")
    $ add_location("dick_office_cabinet", caption=_("Dick's Cabinet"), label="dick_office_cabinet", init_label="dick_office_cabinet_init", parent="dick_office_entrance")
    $ add_location("dick_office_entrance", caption=_("Dick's Office Reception"), label="dick_office_entrance", init_label="dick_office_entrance_init", parent="street_dick_office")
    $ add_location("dick_office_hall1", caption=_("Dick's Office Hall"), label="dick_office_hall1", init_label="dick_office_hall1_init", parent="dick_office_entrance")
    $ add_location("dick_office_secretary", caption=_("Dick's Secretary"), label="dick_office_secretary", init_label="dick_office_secretary_init", parent="dick_office_entrance")

    #FITNESS
    $ add_location("street_fitness", caption=_("Fitness"), label="street_fitness", init_label="street_fitness_init", parent="Fitness")

    #GAS STATION
    $ add_location("street_gas_station", caption=_("Gas Station"), label="street_gas_station", init_label="street_gas_station_init", parent="Gas_Station")
    $ add_location("gas_station_view1", caption=_("Gas Station"), label="gas_station_view1", init_label="gas_station_view1_init", parent="street_gas_station")
    $ add_location("gas_station_view2", caption=_("Gas Station"), label="gas_station_view2", init_label="gas_station_view2_init", parent="street_gas_station")
    $ add_location("gas_station_view3", caption=_("Gas Station"), label="gas_station_view3", init_label="gas_station_view3_init", parent="street_gas_station")
    $ add_location("gas_station_view4", caption=_("Gas Station"), label="gas_station_view4", init_label="gas_station_view4_init", parent="street_gas_station")
    $ add_location("gas_station_view5", caption=_("Gas Station"), label="gas_station_view5", init_label="gas_station_view5_init", parent="street_gas_station")
    $ add_location("gas_station_view6", caption=_("Gas Station"), label="gas_station_view6", init_label="gas_station_view6_init", parent="street_gas_station")
    $ add_location("gas_station_view_cashier", caption=_("Gas Station"), label="gas_station_view_cashier", init_label="gas_station_view_cashier_init", parent="street_gas_station")
    $ add_location("gas_station_view_door", caption=_("Gas Station"), label="gas_station_view_door", init_label="gas_station_view_door_init", parent="street_gas_station")

    #HOSTEL
    $ add_location("hostel_edge_1_a", caption=_("BLIND ALLEY"), label="hostel_edge_1_a", init_label="hostel_edge_1_a_init", parent="Street_Corner")
    $ add_location("hostel_edge_1_b", caption=_("BLIND ALLEY"), label="hostel_edge_1_b", init_label="hostel_edge_1_b_init", parent="Street_Corner")
    $ add_location("hostel_edge_1_c", caption=_("BLIND ALLEY"), label="hostel_edge_1_c", init_label="hostel_edge_1_c_init", parent="Street_Corner")
    $ add_location("hostel_street", caption=_("HOSTEL STREET"), label="hostel_street", init_label="hostel_street_init", parent="Street_Corner")
    $ add_location("hostel_street_door", caption=_("HOSTEL ENTRANCE"), label="hostel_street_door", init_label="hostel_street_door_init", parent="Street_Corner")
    $ add_location("hostel_street2", caption=_("DIRTY STREET"), label="hostel_street2", init_label="hostel_street2_init", parent="Street_Corner")
    $ add_location("hostel_street3", caption=_("POOR STREET"), label="hostel_street3", init_label="hostel_street3_init", parent="Street_Corner")

    #HOUSE
    $ add_location("basement_bedroom2_cupboard", caption=_("BASEMENT"), label="basement_bedroom2_cupboard", init_label="basement_bedroom2_cupboard_init", parent="basement_hole")
    $ add_location("basement_bedroom_table", caption=_("BASEMENT"), label="basement_bedroom_table", init_label="basement_bedroom_table_init", parent="basement_hole")
    $ add_location("basement_bedroom1", caption=_("BASEMENT"), label="basement_bedroom1", init_label="basement_bedroom1_init", parent="basement_hole")
    $ add_location("basement_bedroom2", caption=_("BASEMENT"), label="basement_bedroom2", init_label="basement_bedroom2_init", parent="basement_hole")
    $ add_location("basement_hole", caption=_("BASEMENT"), label="basement_hole", init_label="basement_hole_init", parent="basement_laundry")
    $ add_location("basement_laundry", caption=_("Laundry"), label="basement_laundry", init_label="basement_laundry_init", parent="basement_pool")
    $ add_location("basement_pool", caption=_("Basement Pool"), label="basement_pool", init_label="basement_pool_init", parent="floor1")
    $ add_location("bathroom_bath", caption=_("Bathroom Bath"), label="bathroom_bath", init_label="bathroom_bath_init", parent="floor1")
    $ add_location("bathroom_shower", caption=_("Bathroom Bath"), label="bathroom_shower", init_label="bathroom_shower_init", parent="floor1")

    $ add_location("bedroom1", caption=_("Bedroom"), label="bedroom1", init_label="bedroom1_init", parent="floor1")
    $ add_location("bedroom2", caption=_("Bedroom"), label="bedroom2", init_label="bedroom2_init", parent="floor1")

    $ add_location("kitchen", caption=_("Kitchen"), label="kitchen", init_label="kitchen_init", parent="floor1")
    $ add_location("kitchen2", caption=_("Kitchen"), label="kitchen2", init_label="kitchen2_init", parent="floor1")

    $ add_location("bedroom_bardie", caption=_("BARDIE'S ROOM"), label="bedroom_bardie", init_label="bedroom_bardie_init", parent="floor1")
    $ add_location("bedroom_second", caption=_("GUEST'S BEDROOM"), label="bedroom_second", init_label="bedroom_second_init", parent="floor1")

    $ add_location("living_room", caption=_("LIVING ROOM"), label="living_room", init_label="living_room_init", parent="floor1")

    $ add_location("floor1_fountain", caption=_("Fountain"), label="floor1_fountain", init_label="floor1_fountain_init", parent="floor1")
    $ add_location("floor1_stairs", caption=_("Stairs Ground Floor"), label="floor1_stairs", init_label="floor1_stairs_init", parent="floor1")
    $ add_location("floor1", caption=_("Hall Ground Floor"), label="floor1", init_label="floor1_init", parent="street_house_main_yard")
    $ add_location("floor2_mirrors", caption=_("Mirrors"), label="floor2_mirrors", init_label="floor2_mirrors_init", parent="floor1")
    $ add_location("floor2_stairs", caption=_("Stairs Top Floor"), label="floor2_stairs", init_label="floor2_stairs_init", parent="floor1")
    $ add_location("floor2", caption=_("Hall Top Floor"), label="floor2", init_label="floor2_init", parent="floor1")

    $ add_location("street_house_fence", caption=_("House Fence"), label="street_house_fence", init_label="street_house_fence_init", parent="street_house_main_yard")
    $ add_location("street_house_gate", caption=_("House Gates"), label="street_house_gate", init_label="street_house_gate_init", parent="street_house_main_yard")
    $ add_location("street_house_main_yard", caption=_("House Yard"), label="street_house_main_yard", init_label="street_house_main_yard_init", parent="House")
    $ add_location("street_house_outside", caption=_("House Outside"), label="street_house_outside", init_label="street_house_outside_init", parent="street_house_main_yard")

    # Monica's Office
    $ add_location("street_monica_office", caption=_("Monica's Office Outside"), label="street_monica_office", init_label="street_monica_office_init", parent="Monica_Office")
    $ add_location("monica_office_cabinet_table", caption=_("Monica's Office"), label="monica_office_cabinet_table", init_label="monica_office_cabinet_table_init", parent="monica_office_entrance")
    $ add_location("monica_office_cabinet", caption=_("Monica's Office"), label="monica_office_cabinet", init_label="monica_office_cabinet_init", parent="monica_office_entrance")
    $ add_location("monica_office_entrance", caption=_("Monica's Office Entrance"), label="monica_office_entrance", init_label="monica_office_entrance_init", parent="street_monica_office")
    $ add_location("monica_office_photostudio", caption=_("Photostudio"), label="monica_office_photostudio", init_label="monica_office_photostudio_init", parent="monica_office_entrance")
    $ add_location("monica_office_secretary_teatable", caption=_("Monica's Secretary"), label="monica_office_secretary_teatable", init_label="monica_office_secretary_teatable_init", parent="monica_office_entrance")
    $ add_location("monica_office_secretary", caption=_("Monica's Secretary"), label="monica_office_secretary", init_label="monica_office_secretary_init", parent="monica_office_entrance")

    # Police
    $ add_location("street_police", caption=_("Police Station"), label="street_police", init_label="street_police_init", parent="Police")
    $ add_location("police_entrance", caption=_("Police Station"), label="police_entrance", init_label="police_entrance_init", parent="street_police")

    # Rich Hotel
    $ add_location("street_rich_hotel", caption=_("Hotel Le Grand"), label="street_rich_hotel", init_label="street_rich_hotel_init", parent="Rich_Hotel")
    $ add_location("rich_hotel_event_hall", caption=_("Hotel Le Grand"), label="rich_hotel_event_hall", init_label="rich_hotel_event_hall_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_event_scene", caption=_("Hotel Le Grand"), label="rich_hotel_event_scene", init_label="rich_hotel_event_scene_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_event_sittable", caption=_("Hotel Le Grand"), label="rich_hotel_event_sittable", init_label="rich_hotel_event_sittable_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_event_sofa", caption=_("Hotel Le Grand"), label="rich_hotel_event_sofa", init_label="rich_hotel_event_sofa_init", parent="rich_hotel_reception")
    $ add_location("rich_hotel_event_tables", caption=_("Hotel Le Grand"), label="rich_hotel_event_tables", init_label="rich_hotel_event_tables_init", parent="rich_hotel_reception")

    # Steve's Office
    $ add_location("street_steve_office", caption=_("STEVE'S OFFICE"), label="street_steve_office", init_label="street_steve_office_init", parent="Steve_Office")

    # Whores place
    $ add_location("street_corner", caption=_("Street Edge"), label="street_corner", init_label="street_corner_init", parent="Street_Corner")
    $ add_location("whores_place", caption=_("Whores place"), label="whores_place", init_label="whores_place_init", parent="Street_Corner")
    $ add_location("whores_place_shawarma", caption=_("Shawarma"), label="whores_place_shawarma", init_label="whores_place_shawarma_init", parent="Street_Corner")
    $ add_location("whores_place_street1", caption=_("Dirty street"), label="whores_place_street1", init_label="whores_place_street1_init", parent="Street_Corner")

    # Dummy location
    $ add_location("empty", caption="", label="", parent="none")




    return
