define offsets_blink = {
#offsets_blink_start
    "megaimage" : {"monica":[10,20,10,30]},
    "megaimage2" : {"monica":[10,20,10,30]},
    "megaimage3" : {"monica":[10,20,10,30]},
    "img_20001" : {"Monica":[588,380,5,"1"]}
#offsets_blink_finish
}


define blink_presets = {
    "1": [[1.5, 0.2, 0.2, 0.3], [3.0, 0.2, 0.2, 0.3], [2.5, 0.2, 0.2, 0.3], [2.0, 0.2, 0.2, 0.3], [0.1, 0.1, 0.1, 0.1]], # спокойное
    "2": [[1.5, 0.03, 0.01, 0.03], [0.01, 0.03, 0.01, 0.03], [0.01, 0.03, 0.01, 0.03]], # частое моргание, растерянность # переименовать отсюда, 1 не трогаем
    "3": [[1.5, 0.2, 0.2, 0.5], [2.0, 0.02, 0.01, 0.1], [2.5, 0.03, 0.01, 0.03]] # тест
}

#    show screen blink_screen1(offsets_blink["img_20001"]["Monica"], blink_presets["2"])


#screen blink_screen1(blink_offset, blink_preset):
#    layer "master"
#    zorder 16
#    $ blink1 = BlinkStrip("images/Blink/img_20001_blink_Monica.png", blink_offset[2], blink_preset)
#    fixed:
##        add "images/Blink/img_20001_blink_Monica.png":
#
#        add blink1:
#            xpos blink_offset[0]
#            ypos blink_offset[1]

init python:
    blink_preset = False
    blink_preset2 = False
    blink_preset3 = False
