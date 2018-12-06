define bettyCleaningProgessAmount = 20 #5 #Прогресс с Бетти за уборку
define bettyCleaningProgessRegressAmount = -10 # Насколько убавляется прогресс с Бетти если Моника пропустила уборку
define bettyTryOutInGovernessClothRegressAmount = -10 # Насколько убавляется прогресс с Бетти если Моника пытается выйти за пределы дома в одежде гувернантки
define bardieCleaningUpskirtTry = 60 #15 #Прогресс с Барди за попытку подсмотреть во время уборки (начальная стадия)
define bardieCleaningUpskirtTryCorruption = 0 # Увеличение corruption, когда Барди подсматривает под юбку Моники
define monicaCleaningAddCorruptionPerCleaning = 1 #Увеличение corruption за одну уборку
define monicaKebabWorkFlyersAmount = 5 # Количество флаеров, которые надо раздать Монике
define monicaKebabWorkFlyersAmountRandomDiff = 1 #Рандом, в котором будет делаться отклонение от monicaKebabWorkFlyersAmount


default persistent.pause_before_change_slide = False
default persistent.auto_clipboard = False

default map_enabled = True
default map_disabled_forced = False

define fadehold = Fade(0.5, 1.0, 0.5)
define fadelong = Fade(0.5, 0.5, 0.5)
default streetFunMusic = "road_trip"
default casualMusic = "Stealth_Groover"

default define_version = 1
default define_version_current = 0

default text_button_default_layout = "default"

default clickHoldMode = True #блокировка клика после диалога, если мышкой не двигали
default clickHoldFlag = False
default clickHoldLastTime = 0
default clickHoldLastMouseX = 0
default clickHoldLastMouseY = 0
default screenActionHappened = False

default bitchmeterValue = 0
default bitchmeter_places = {}
default corruption = 0
default corruptionMax = 1000
default corruption_places = {}
default char_progress_stored = {}
default char_data = False

define imagesSizesCache = {}

label characters_init:
    $ char_info = {
        "Monica":{"name": _("Бетти Робертс"), "enabled":True, "face":"Face_Betty", "style":"char_face_style1_red",  "bar_suffix": "red", "level":1, "current_progress":0, "caption": _("Бетти ждет что Моника будет регулярно убираться в доме."), "max_progress":100, "uplevel_label":"bettyProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Beef":{"name": _("Биф"), "enabled":True, "face":"Face_Beef", "style":"char_face_style1_orange",  "bar_suffix": "orange", "level":1, "current_progress":0, "caption": _("Биф обещал взять Монику работать в офис."), "max_progress":100, "uplevel_label":"beefProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Betty":{"name": _("Бетти Робертс"), "enabled":True, "face":"Face_Betty", "style":"char_face_style1_red",  "bar_suffix": "red", "level":1, "current_progress":0, "caption": _("Бетти ждет что Моника будет регулярно убираться в доме."), "max_progress":100, "uplevel_label":"bettyProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Bardie":{"name": _("Барди"), "enabled":True, "face":"Face_Bardie", "style":"char_face_style1_blue",  "bar_suffix": "blue", "level":1, "current_progress":0, "caption": _("Барди ищет способ заглянуть Монике под юбку."), "max_progress":100, "uplevel_label":"bardieProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "AlexPhotograph":{"name": _("Фотограф Алекс"), "enabled":False, "face":"Face_AlexPhotograph", "style":"char_face_style1_orange",  "bar_suffix": "orange", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"alexPhotographProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Cashier":{"name": _("Вивиан"), "enabled":False, "face":"Face_Cashier", "style":"char_face_style1_pink",  "bar_suffix": "pink", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"cashierProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "DickSecretary":{"name": _("Виктория"), "enabled":False, "face":"Face_DickSecretary", "style":"char_face_style1_pink",  "bar_suffix": "pink", "level":1, "current_progress":0, "caption": _("Виктория видит в Монике угрозу."), "max_progress":100, "uplevel_label":"dickSecretaryProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Driver":{"name": _("Водитель Фред"), "enabled":False, "face":"Face_Driver", "style":"char_face_style1_blue",  "bar_suffix": "blue", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"driverProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "GasSalesWoman":{"name": _("Кристина"), "enabled":False, "face":"Face_GasSaleswoman", "style":"char_face_style1_pink",  "bar_suffix": "pink", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"gasSalesWomanProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Jane":{"name": _("Джейн"), "enabled":False, "face":"Face_Jane", "style":"char_face_style1_pink",  "bar_suffix": "pink", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"janeProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Marcus":{"name": _("Маркус"), "enabled":False, "face":"Face_Marcus", "style":"char_face_style1_red",  "bar_suffix": "red", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"marcusProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Melanie":{"name": _("Модель Мелани"), "enabled":False, "face":"Face_Melanie", "style":"char_face_style1_green",  "bar_suffix": "green", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"melanieProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Mommy":{"name": _("Мамочка"), "enabled":False, "face":"Face_Mommy", "style":"char_face_style1_orange",  "bar_suffix": "orange", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"mommyProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Neighbor":{"name": _("Сосед"), "enabled":False, "face":"Face_Neighbor", "style":"char_face_style1_blue",  "bar_suffix": "blue", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"neighborProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Perry":{"name": _("Перри"), "enabled":False, "face":"Face_Perry", "style":"char_face_style1_pink",  "bar_suffix": "pink", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"perryProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Ralph":{"name": _("Ральф Робертс"), "enabled":False, "face":"Face_Ralph", "style":"char_face_style1_blue",  "bar_suffix": "blue", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"ralphProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Rebecca":{"name": _("Ребекка"), "enabled":False, "face":"Face_Rebecca", "style":"char_face_style1_pink",  "bar_suffix": "pink", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"rebeccaProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "ReceptionGirl":{"name": _("Рецепшин Администратор"), "enabled":False, "face":"Face_RichHotelReception", "style":"char_face_style1_orange",  "bar_suffix": "orange", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"receptionGirlProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Shawarma_Trader":{"name": _("Продавец шавермы"), "enabled":False, "face":"Face_ShawarmaTrader", "style":"char_face_style1_blue",  "bar_suffix": "blue", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"shawarma_TraderProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Stephanie":{"name": _("Стефани"), "enabled":False, "face":"Face_Stephanie", "style":"char_face_style1_pink",  "bar_suffix": "pink", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"stephanieProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Steve":{"name": _("Партнер Стив"), "enabled":False, "face":"Face_Steve", "style":"char_face_style1_blue",  "bar_suffix": "blue", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"steveProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
        "Tiffany":{"name": _("Тиффани"), "enabled":False, "face":"Face_Tiffany", "style":"char_face_style1_pink",  "bar_suffix": "pink", "level":1, "current_progress":0, "caption": _(""), "max_progress":100, "uplevel_label":"tiffanyProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")}
#        "Monica":{"name": _("Betty Roberts"), "enabled":True, "face":"Face_Betty", "style":"char_face_style1",  "bar_suffix": "red", "level":1, "current_progress":0, "caption": _("Бетти ждет что Моника будет регулярно убираться в доме."), "max_progress":100, "uplevel_label":"bettyProgressLevelUp", "progress_label":False, "progress_caption":"Progress lvl.", "caption_diabled":_("Work in progress...")},
    }

    $ char_progress_stored = {}
    return

label define_autorun:
    $ print "autorun!"

    $ define_version_current = define_version



    $ actions_objects = { #иконки действий
        "l" : {
            "description" : _("Смотреть"),
            "label_suffix" : "_use",
            "icon" : "/Icons/eye" + res.suffix + ".png",
        },
        "h" : {
            "description" : _("Взять"),
            "label_suffix" : "_hand",
            "icon" : "/Icons/hand" + res.suffix + ".png"
        },
        "t" : {
            "description" : _("Говорить"),
            "label_suffix" : "_talk",
            "icon" : "/Icons/talk3" + res.suffix +".png",
        },
        "w" : {
            "description" : _("Идти"),
            "label_suffix" : "_walk",
            "icon" : "/Icons/walk" + res.suffix + ".png",
        },
        "i" : {
            "description" : _("Инфо"),
            "label_suffix" : "_info",
            "icon" : "/Icons/info" + res.suffix + ".png",
        }

    }


    $ text_button_layouts = {
        "default": {
            "text_button.spacing1" : gui.resolution.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.text_button.spacing2,
            "text_button.style" : gui.resolution.text_button.style,
            "text_button.force_hovered.style" : gui.resolution.text_button.force_hovered.style,
            "text_button.padding" : gui.resolution.text_button.padding
        },

        "map" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_disabled" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_disabled.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_disabled.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_active" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_active.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_active.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_house" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_active.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_active.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        }
    }

    call define_hudpresets() from _call_define_hudpresets

    $ calendar_days = [_("Пн"), _("Вт"), _("Ср"), _("Чт"), _("Пт"), _("Сб"), _("Вс")]
    return

label define_hudpresets:
    $ hud_presets = {
        "default" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : True,
            "display_scene_map" : True,
            "display_bitchmeter" : True,
            "display_closemap" : True
        },
        "default_map_disabled" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : True,
            "display_scene_map" : False,
            "display_bitchmeter" : True,
            "display_closemap" : True
        },
        "map": {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : False,
            "display_scene_map" : False,
            "display_bitchmeter" : False,
            "display_closemap" : True
        },
        "map_locked" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : False,
            "display_scene_map" : False,
            "display_bitchmeter" : False,
            "display_closemap" : False
        },

    }
    return

label run_after_load:
    $ print "after load!"
    return

label game_init:
    $ image_screen_scene_flag = False
    $ show_scene_loop_flag = False
    $ interface_blocked_flag = False
    define dissolve1 = Dissolve(0.5)
    define dialogue_active_flag = False
    define last_dialogue_character = "m"

    $ width_half = config.screen_width / 2

    $ preferences.show_empty_window = False
#    $ config.keymap["game_menu"].remove("mouseup_3")
#    $ print(config.keymap["game_menu"])
#    $ print(config.keymap)
    $ config.log = True

    call define_autorun()

#    $ bitchmeter_places = {}

#    $ objectives_list = []

#    $ map_enabled = False

    $ define_inventory_object("papers", {"description" : _("Papers"), "label_suffix" : "_use_papers", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/big_papers" + res.suffix + ".png"})
    $ define_inventory_object("phone", {"description" : _("Телефон"), "label_suffix" : "_use_phone", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/cell_phone" + res.suffix + ".png"})
    $ define_inventory_object("shovel", {"description" : "Shovel", "label_suffix" : "_use_shovel", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/shovel" + res.suffix + ".png"})
    $ define_inventory_object("journal", {"description" : _("Журнал Моды"), "label_suffix" : "_use_journal", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/journal" + res.suffix + ".png"})
    $ define_inventory_object("hairdye", {"description" : _("Краска для волос"), "label_suffix" : "_use_hairdye", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/hairdye" + res.suffix + ".png"})
    $ define_inventory_object("crumpled_dress", {"description" : _("Мятое платье"), "label_suffix" : "_use_crumpled_dress", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/crumpled_dress" + res.suffix + ".png"})

    $ scene_transition = False
    $ scene_sound = False
#    $ add_inventory("phone", 5, True)
#    $ add_inventory("shovel", 5, True)
#    $ remove_inventory("papers", 3, True)


#    call showLog("here!")
#    $ renpy.log("here!")
    return

label showLog(str):
    show screen notify(str)

    return
