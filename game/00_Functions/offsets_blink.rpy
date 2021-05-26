define offsets_blink = {
#offsets_blink_start
    "megaimage" : {"monica":[10,20,10,30]},
    "megaimage2" : {"monica":[10,20,10,30]},
    "megaimage3" : {"monica":[10,20,10,30]},
    "img_20001" : {"Monica":[588,380,5,"1"]},
    "img_44245" : {"Monica":[949,185,5,"2"],"RichHotelReception":[210,180,5,"3"],"Visitor1":[530,170,5,"5"],"Visitor2":[1625,150,5,"1"],"Visitor3":[1315,145,5,"4"],"Visitor4":[810,125,5,"3"]},
    "img_34326" : {"RalphHusband":[454,218,5,"1"]},
    "img_35462" : {"Monica":[1034,209,5,"1"]},
    "img_35481" : {"Visitor1":[612,200,5,"2"],"Visitor4":[820,200,5,"5"]},
    "img_35492" : {"Monica":[1240,200,5,"1"],"Visitor1":[473,265,5,"5"],"Visitor4":[800,280,5,"3"]},
    "img_35510" : {"Monica":[528,73,5,"5"]},
    "img_35536" : {"Monica":[644,200,5,"3"]},
    "img_35563" : {"Monica":[941,148,5,"3"]},
    "img_35619" : {"Monica":[927,319,5,"3"]},
    "img_35621" : {"Monica":[915,238,5,"5"]},
    "img_44149" : {"Monica":[779,265,5,"3"]},
    "img_44152" : {"Monica":[622,424,5,"5"],"Visitor2":[1005,300,5,"3"]},
    "img_44160" : {"Monica":[721,255,5,"1"]},
    "img_44205" : {"Monica":[1110,105,5,"5"]},
    "img_44206" : {"Monica":[994,186,5,"1"]},
    "img_44251" : {"Monica":[465,204,5,"3"]},
    "img_44252" : {"Monica":[469,162,5,"3"]},
    "img_44330" : {"Monica":[447,194,5,"3"]},
    "img_44466" : {"Monica":[1010,203,5,"5"]},
    "img_44467" : {"Monica":[893,223,5,"3"]},
    "img_44480" : {"Monica":[902,212,5,"5"],"Visitor1":[623,190,5,"3"]},
    "img_44481" : {"Monica":[629,263,5,"1"],"Visitor3":[1523,200,5,"3"],"Visitor4":[178,185,5,"4"]},
    "img_44515" : {"Monica":[1014,86,5,"3"]},
    "img_44613" : {"Melanie":[695,145,5,"3"]},
    "img_44617" : {"Melanie":[730,200,5,"3"]},
    "img_44618" : {"Melanie":[738,170,5,"3"]},
    "img_44650" : {"Melanie":[925,160,5,"5"]},
    "img_44664" : {"Melanie":[877,134,5,"3"]},
    "img_44677" : {"Melanie":[992,159,5,"3"]},
    "img_44701" : {"Melanie":[870,175,5,"5"]},
    "img_44702" : {"Melanie":[870,140,5,"5"]},
    "img_60202" : {"Monica":[267,99,5,"1"]},
    "img_60240" : {"Monica":[1005,40,5,"3"]},
    "img_60306" : {"Monica":[322,254,5,"5"]},
    "img_60310" : {"Monica":[601,171,5,"1"]},
    "img_60326" : {"Monica":[847,0,5,"4"]}
#offsets_blink_finish
}


define blink_presets = {
    "1": [[1.5, 0.2, 0.2, 0.3], [3.0, 0.2, 0.2, 0.3], [2.5, 0.2, 0.2, 0.3], [2.0, 0.2, 0.2, 0.3], [0.1, 0.1, 0.1, 0.1]], # спокойное
    "2": [[1.5, 0.03, 0.01, 0.03], [0.01, 0.03, 0.01, 0.03], [1.5, 0.03, 0.01, 0.03], [0.01, 0.03, 0.01, 0.03]], # частое моргание, растерянность # переименовать отсюда, 1 не трогаем
    "3": [[2.5, 0.2, 0.03, 0.1], [3.0, 0.02, 0.1, 0.1], [3.0, 0.02, 0.1, 0.1], [4.5, 0.03, 0.1, 0.01], [3.0, 0.02, 0.2, 0.1], [1.5, 0.03, 0.01, 0.03]], # редко
    "4": [[4.5, 0.2, 0.03, 0.1], [5.0, 0.02, 0.1, 0.1], [2.0, 0.02, 0.03, 0.1], [2.0, 0.02, 0.03, 0.1], [3.5, 0.03, 0.1, 0.01]], # сконцентрирована на чем-то, напряжена, моргает очень редко
    "5": [[1.5, 0.02, 0.02, 0.3], [0.1, 0.1, 0.01, 0.1], [2.0, 0.02, 0.03, 0.1], [0.5, 0.02, 0.02, 0.3], [1.0, 0.02, 0.02, 0.3]] # часто

}

init python:
    blink_preset = False
    blink_preset2 = False
    blink_preset3 = False
    blink_preset4 = False
    blink_preset5 = False
    blink_preset6 = False
