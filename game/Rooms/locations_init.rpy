label locations_init:
    $ add_location("bank_office", caption=_("BANK"), label="bank_office", init_label="bank_office_init", parent="Bank")
    $ add_location("street_bank", caption=_("BANK"), label="bank_office", init_label="bank_office_init", parent="Bank")

    $ add_location("street_cloth_shop", caption=_("Clothing Shop"), label="street_cloth_shop", init_label="street_cloth_shop_init", parent="Cloth_Shop")
    $ add_location("street_dick_office", caption=_("Dick's Office"), label="street_dick_office", init_label="street_dick_office_init", parent="Dick_Office")
    $ add_location("dick_office_cabinet", caption=_("Dick's Cabinet"), label="dick_office_cabinet", init_label="dick_office_cabinet_init", parent="street_dick_office")
    $ add_location("dick_office_entrance", caption=_("Dick's Office Reception"), label="dick_office_entrance", init_label="dick_office_entrance_init", parent="street_dick_office")
    $ add_location("dick_office_hall1", caption=_("Dick's Office Hall"), label="dick_office_hall1", init_label="dick_office_hall1_init", parent="street_dick_office")
    $ add_location("dick_office_secretary", caption=_("Dick's Secretary"), label="dick_office_secretary", init_label="dick_office_secretary_init", parent="street_dick_office")

    $ add_location("street_fitness", caption=_("Fitness"), label="street_fitness", init_label="street_fitness_init", parent="Fitness")

    $ add_location("street_gas_station", caption=_("Gas Station"), label="street_gas_station", init_label="street_gas_station_init", parent="Gas_Station")
    $ add_location("gas_station_view1", caption=_("Gas Station"), label="gas_station_view1", init_label="gas_station_view1_init", parent="street_gas_station")
    $ add_location("gas_station_view2", caption=_("Gas Station"), label="gas_station_view2", init_label="gas_station_view2_init", parent="street_gas_station")
    $ add_location("gas_station_view3", caption=_("Gas Station"), label="gas_station_view3", init_label="gas_station_view3_init", parent="street_gas_station")
    $ add_location("gas_station_view4", caption=_("Gas Station"), label="gas_station_view4", init_label="gas_station_view4_init", parent="street_gas_station")
    $ add_location("gas_station_view5", caption=_("Gas Station"), label="gas_station_view5", init_label="gas_station_view5_init", parent="street_gas_station")
    $ add_location("gas_station_view6", caption=_("Gas Station"), label="gas_station_view6", init_label="gas_station_view6_init", parent="street_gas_station")
    $ add_location("gas_station_view_cashier", caption=_("Gas Station"), label="gas_station_view_cashier", init_label="gas_station_view_cashier_init", parent="street_gas_station")
    $ add_location("gas_station_view_door", caption=_("Gas Station"), label="gas_station_view_door", init_label="gas_station_view_door_init", parent="street_gas_station")

    $ add_location("hostel_edge_1_a", caption=_("BLIND ALLEY"), label="hostel_edge_1_a", init_label="hostel_edge_1_a_init", parent="Street_Corner")
    $ add_location("hostel_edge_1_b", caption=_("BLIND ALLEY"), label="hostel_edge_1_b", init_label="hostel_edge_1_b_init", parent="Street_Corner")
    $ add_location("hostel_edge_1_c", caption=_("BLIND ALLEY"), label="hostel_edge_1_c", init_label="hostel_edge_1_c_init", parent="Street_Corner")
    $ add_location("hostel_street", caption=_("HOSTEL STREET"), label="hostel_street", init_label="hostel_street_init", parent="Street_Corner")
    $ add_location("hostel_street_door", caption=_("HOSTEL ENTRANCE"), label="hostel_street_door", init_label="hostel_street_door_init", parent="Street_Corner")
    $ add_location("hostel_street2", caption=_("DIRTY STREET"), label="hostel_street2", init_label="hostel_street2_init", parent="Street_Corner")
    $ add_location("hostel_street3", caption=_("DIRTY STREET"), label="hostel_street3", init_label="hostel_street3_init", parent="Street_Corner")


    return
