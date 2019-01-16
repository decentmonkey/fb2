default biffMonicaCastingsEnabled = False
default biffMonicaLastCastingSkipped = False
default monicaPhotoShootInProgress = False
default monicaPhotoShootOutfitIdx = 1
define monicaOutfitsIcons = ["/Icons2/Photoshoot1_Icon", "/Icons2/Photoshoot2_Icon", "/Icons2/Photoshoot3_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon"]
default monicaOutfitsEnabled = [True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, ]

default biffWeeklyPhotoShootEnabled = True

default monicaAskBiffGiftCertificateFirstTime = True
default monicaBiffFirstPhotoShoot = True

define PS1_shots_amount = 16
default PS1_shoots_array = []
define PS2_shots_amount = 14
default PS2_shoots_array = []
define PS3_shots_amount = 14
default PS3_shoots_array = []


label biffProgressLevelUp1:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["enabled"] = False
        $ char_data["caption_diabled"] = _("Work in progress...")
    return
