define offsets_blink = {
#offsets_blink_start
    "megaimage" : {"monica":[10,20,10,30]},
    "megaimage2" : {"monica":[10,20,10,30]},
    "megaimage3" : {"monica":[10,20,10,30]},
    "img_20001" : {"Monica":[588,380,5,"1"]},
    "img_40974" : {"Monica":[482,298,5,"1"]},
    "img_41083" : {"Monica":[480,160,5,"1"]},
    "img_41013" : {"Monica":[962,180,5,"1"]},
    "img_41088" : {"Monica":[876,114,5,"1"]},
    "img_41129" : {"Monica":[410,114,5,"1"]},
    "img_41163" : {"Monica":[800,150,5,"1"]},
    "img_41205" : {"Monica":[864,270,5,"1"]},
    "img_41223" : {"Monica":[914,220,5,"1"]},
    "img_41366" : {"Monica":[466,186,5,"1"]},
    "img_15869" : {"Monica":[774,298,5,"1"]},
    "img_32870" : {"Monica":[912,84,5,"1"]},
    "img_32872" : {"Betty":[950,180,5,"1"]},
    "img_32916" : {"Betty":[826,430,5,"1"]},
    "img_33004" : {"Monica":[552,206,5,"1"]},
    "img_33066" : {"Monica":[606,210,5,"1"]},
    "img_33120" : {"Monica":[576,130,5,"1"]},
    "img_33165" : {"Monica":[582,220,5,"1"]},
    "img_33191" : {"Monica":[726,170,5,"1"]},
    "img_33204" : {"Monica":[488,214,5,"1"]},
    "img_33265" : {"Monica":[854,410,5,"1"]},
    "img_33618" : {"Monica":[1124,270,5,"1"]},
    "img_33684" : {"JuliaGoverness":[1000,230,5,"1"],"Monica":[1026,120,5,"1"]},
    "img_33707" : {"JuliaGoverness":[770,190,5,"1"],"Monica":[1100,130,5,"1"]},
    "img_33732" : {"JuliaGoverness":[734,270,5,"1"],"Monica":[1378,186,5,"1"]},
    "img_33807" : {"Monica":[964,166,5,"1"]},
    "img_33818" : {"JuliaGoverness":[810,220,5,"1"],"Monica":[1210,98,5,"1"]},
    "img_33936" : {"Melanie":[884,210,5,"1"]},
    "img_33958" : {"BartenderWaitress":[1590,300,5,"1"],"Monica":[898,320,5,"1"]},
    "img_34118" : {"BartenderWaitress":[1102,250,5,"1"]},
    "img_34326" : {"Monica":[876,344,5,"1"]},
    "img_34436" : {"Monica":[1130,180,5,"1"]},
    "img_34445" : {"Bill":[130,606,5,"1"],"Monica":[1036,240,5,"1"]},
    "img_34492" : {"Monica":[1040,290,5,"1"]},
    "img_34505" : {"Bill":[1110,270,5,"1"],"Monica":[746,410,5,"1"]},
    "img_34512" : {"Monica":[514,308,5,"1"]},
    "img_34565" : {"Monica":[996,340,5,"1"]},
    "img_34631" : {"Monica":[450,170,5,"1"]},
    "img_34688" : {"Monica":[950,215,5,"1"]},
    "img_34855" : {"Monica":[1155,220,5,"1"]},
    "img_34866" : {"Monica":[943,172,5,"1"]},
    "img_34881" : {"JuliaGoverness":[685,130,5,"1"],"Monica":[1150,120,5,"1"]},
    "img_34905" : {"Monica":[604,200,5,"1"]},
    "img_34927" : {"Monica":[1162,216,5,"1"]},
    "img_35066" : {"Monica":[724,320,5,"1"]},
    "img_35138" : {"Monica":[810,334,5,"1"]},
    "img_40776" : {"Monica":[406,188,5,"1"]},
    "img_41276" : {"Monica":[336,266,5,"1"]},
    "img_41309" : {"Monica":[360,240,5,"1"]},
    "img_44245" : {"Monica":[949,185,5,"1"],"RichHotelReception":[210,180,5,"1"],"Visitor1":[530,170,5,"1"],"Visitor2":[1625,150,5,"1"],"Visitor3":[1315,145,5,"1"],"Visitor4":[810,125,5,"1"]}
#offsets_blink_finish
}


define blink_presets = {
    "1": [[1.5, 0.2, 0.2, 0.3], [3.0, 0.2, 0.2, 0.3], [2.5, 0.2, 0.2, 0.3], [2.0, 0.2, 0.2, 0.3], [0.1, 0.1, 0.1, 0.1]], # спокойное
    "2": [[1.5, 0.03, 0.01, 0.03], [0.01, 0.03, 0.01, 0.03], [0.01, 0.03, 0.01, 0.03]], # частое моргание, растерянность # переименовать отсюда, 1 не трогаем
    "3": [[2.5, 0.2, 0.3, 0.1], [3.0, 0.02, 0.3, 0.1], [3.0, 0.02, 0.3, 0.1], [4.5, 0.03, 0.3, 0.01]], # редко
    "4": [[4.5, 0.2, 0.3, 0.1], [5.0, 0.02, 0.3, 0.1], [2.0, 0.02, 0.3, 0.1], [3.5, 0.03, 0.3, 0.01]], # сконцентрирована на чем-то
    "5": [[4.5, 0.2, 0.3, 0.1], [5.0, 0.02, 0.3, 0.1], [2.0, 0.02, 0.3, 0.1], [3.5, 0.03, 0.3, 0.01]]
}

init python:
    blink_preset = False
    blink_preset2 = False
    blink_preset3 = False
    blink_preset4 = False
    blink_preset5 = False
    blink_preset6 = False
