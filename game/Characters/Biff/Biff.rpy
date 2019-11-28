default monicaWorkingAtBiffOffice = False
default biffMonicaCastingsEnabled = False
default biffMonicaLastCastingSkipped = False
default photoShootDisabledNextWeek = False
default monicaPhotoShootInProgress = False
default monicaPhotoShootOutfitIdx = 1
default monicaOutfitsIcons = ["/Icons2/Photoshoot1_Icon", "/Icons2/Photoshoot2_Icon", "/Icons2/Photoshoot3_Icon", "/Icons2/Photoshoot4_Icon", "/Icons2/Photoshoot5_Icon", "/Icons2/Photoshoot6_Icon", "/Icons2/Photoshoot7_Icon", "/Icons2/Photoshoot8_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon"]
default monicaOutfitsEnabled = [True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, ]

default melanieOutfitsIcons = ["/Icons2/Photoshoot_Melanie_1_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon"]
default melanieOutfitsEnabled = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, ]

default biffWeeklyPhotoShootEnabled = True

default monicaAskBiffGiftCertificateFirstTime = True
default monicaBiffFirstPhotoShoot = True

define PS1_shots_amount = 16
default PS1_shoots_array = []
define PS2_shots_amount = 14
default PS2_shoots_array = []
define PS3_shots_amount = 14
default PS3_shoots_array = []
define PS4_shots_amount = 18
default PS4_shoots_array = []
define PS5_shots_amount = 27
default PS5_shoots_array = []
define PS6_shots_amount = 22
default PS6_shoots_array = []
define PS7_shots_amount = 22
default PS7_shoots_array = []
define PS8_shots_amount = 16
default PS8_shoots_array = []

define PS_Melanie_1_shots_amount = 24
default PS_Melanie_1_shoots_array = []

label biffProgressLevelUp1:
    $ char_data["level"] = char_data["level"] + 1
    if char_data["level"] == 2:
        $ char_data["enabled"] = False
        $ char_data["caption_diabled"] = _("Work in progress...")
    return

label biffInitOutfitIcons:
    $ monicaOutfitsIcons2 = ["/Icons2/Photoshoot1_Icon", "/Icons2/Photoshoot2_Icon", "/Icons2/Photoshoot3_Icon", "/Icons2/Photoshoot4_Icon", "/Icons2/Photoshoot5_Icon", "/Icons2/Photoshoot6_Icon", "/Icons2/Photoshoot7_Icon", "/Icons2/Photoshoot8_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon"]
    return

label biffInitMelanieOutfitIcons:
    $ melanieOutfitsIcons = ["/Icons2/Photoshoot_Melanie_1_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon", "/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon","/Icons2/Photoshoot_Empty_Icon"]
    return
