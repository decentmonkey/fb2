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
    "img_41366" : {"Monica":[466,186,5,"1"]}
#offsets_blink_finish
}


define blink_presets = {
    "1": [[1.5, 0.2, 0.2, 0.3], [3.0, 0.2, 0.2, 0.3], [2.5, 0.2, 0.2, 0.3], [2.0, 0.2, 0.2, 0.3], [0.1, 0.1, 0.1, 0.1]], # спокойное
    "2": [[1.5, 0.03, 0.01, 0.03], [0.01, 0.03, 0.01, 0.03], [0.01, 0.03, 0.01, 0.03]], # частое моргание, растерянность # переименовать отсюда, 1 не трогаем
    "3": [[1.5, 0.2, 0.2, 0.5], [2.0, 0.02, 0.01, 0.1], [2.5, 0.03, 0.01, 0.03]] # тест
}

init python:
    blink_preset = False
    blink_preset2 = False
    blink_preset3 = False
    blink_preset4 = False
    blink_preset5 = False
    blink_preset6 = False
