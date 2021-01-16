init python:
    achievements_categories = [
        ["Betty", t_("Betty"), c_green],
        ["PublicEvents", t_("Public Events"), c_white],
        ["Pub", t_("Shiny Hole"), c_pink],
        ["Slums", t_("Slums"), c_orange],
        ["EscortService", t_("Escort Service"), c_pink],
        ["Victoria", t_("Victoria"), c_red],
        ["Julia", t_("Julia"), c_green],
        ["Philip", t_("Philip"), c_red]
    ]
    achievements_list = {
        "Betty" : [
            ["32915", "", "gallery_32915"],
            ["32951", "", "gallery_32951"],
            ["42337", "", "gallery_42337"],
            ["33546", "", "gallery_33546"],
            ["33434", "", "gallery_33434"]
        ],

        "PublicEvents" : [
            ["41618", "", "gallery_41618"],
            ["41671", "", "gallery_41671"],
#            ["41678", "", "gallery_41678"],
            ["41700", "", "gallery_41700"]
        ],

        "Pub" : [
            ["40832", "", "gallery_40832"],
            ["40905", "", "gallery_40905"],
            ["32762", "", "gallery_32762"],
            ["32862", "", "gallery_32862"],
            ["34190", "", "gallery_34190"],
            ["33991", "", "gallery_33991"],
            ["34020", "EXTRA", "gallery_34020"],
            ["34061", "", "gallery_34020"],
            ["34102", "", "gallery_34102"],
            ["34124", "", "gallery_34124"],
            ["34160", "EXTRA", "gallery_34160"]
        ],

        "Slums" : [
            ["33215", "EXTRA", "gallery_33215"],
            ["33250", "", "gallery_33250"],
            ["33282", "", "gallery_33282"],
            ["33311", "", "gallery_33311"],
            ["33320", "", "gallery_33320"],
            ["33340", "", "gallery_33340"],
            ["33383", "", "gallery_33383"],
            ["33397", "", "gallery_33397"],
            ["41489", "", "gallery_41489"],
            ["41497", "", "gallery_41497"]
        ],

        "EscortService" : [
            ["40948", "", "gallery_40948"],
            ["41016", "", "gallery_41016"],
            ["41136", "", "gallery_41136"],
            ["41152", "EXTRA", "gallery_41152"],
            ["41184", "", "gallery_41184"],
            ["41324", "", "gallery_41324"],
            ["41407", "", "gallery_41407"],
            ["41413", "", "gallery_41413"],
            ["41987", "", "gallery_41987"],
            ["42044", "", "gallery_42044"],
            ["42017", "", "gallery_42017"],
            ["42180", "", "gallery_42180"],
            ["42116", "", "gallery_42116"]
        ],

        "Victoria" : [
            ["42603", "", "gallery_42603"],
            ["42445", "", "gallery_42445"],
            ["42504", "", "gallery_42504"],
            ["33913", "EXTRA", "gallery_33913"],
            ["33931", "EXTRA", "gallery_33931"]
        ],

        "Julia" : [
            ["33610", "", "gallery_33610"],
            ["33720", "", "gallery_33720"],
            ["33769", "", "gallery_33769"],
            ["33782", "", "gallery_33782"],
            ["33867", "", "gallery_33867"],
            ["33810", "", "gallery_33810"]
        ],

        "Philip": [
            ["33039", "", "gallery_33039"],
            ["33129", "", "gallery_33129"],
            ["33152", "EXTRA", "gallery_33152"],
            ["33076", "", "gallery_33076"]
        ]
    }
    achievements_labels = {
        "img_32915" : "32915",
        "img_32951" : "32951",
        "img_41618" : "41618",
        "img_41671" : "41671",
#        "img_41678" : "41678",
        "img_41700" : "41700",
        "img_40832" : "40832",
        "img_40905" : "40905",
        "img_32762" : "32762",
        "img_32862" : "32862",
        "img_33215" : "33215",
        "img_33250" : "33250",
        "img_33282" : "33282",
        "img_33311" : "33311",
        "img_33320" : "33320",
        "img_33340" : "33340",
        "img_33383" : "33383",
        "img_33397" : "33397",
        "img_41489" : "41489",
        "img_41497" : "41497",
        "img_40948" : "40948",
        "img_41016" : "41016",
        "img_41136" : "41136",
        "img_41152" : "41152",
        "img_41184" : "41184",
        "img_41324" : "41324",
        "img_41407" : "41407",
        "img_41413" : "41413",
        "img_33039" : "33039",
        "img_33129" : "33129",
        "img_33152" : "33152",
        "img_33076" : "33076",
        "img_42337" : "42337",
        "img_33546" : "33546",
        "img_33434" : "33434",
        "img_34190" : "34190",
        "img_33991" : "33991",
        "img_34020" : "34020",
        "img_34061" : "34061",
        "img_34102" : "34102",
        "img_34124" : "34124",
        "img_34160" : "34160",
        "img_41987" : "41987",
        "img_42044" : "42044",
        "img_42017" : "42017",
        "img_42180" : "42180",
        "img_42116" : "42116",
        "img_42603" : "42603",
        "img_42445" : "42445",
        "img_42504" : "42504",
        "img_33913" : "33913",
        "img_33931" : "33931",
        "img_33610" : "33610",
        "img_33720" : "33720",
        "img_33769" : "33769",
        "img_33782" : "33782",
        "img_33867" : "33867",
        "img_33810" : "33810"

    }

init python:
    if persistent.achievements is None:
        persistent.achievements = {}

    def check_achievement(str):
        if achievements_labels.has_key(str):
            achLabel = achievements_labels[str]
            if persistent.achievements.has_key(achLabel) == False:
                persistent.achievements[achLabel] = True
#                renpy.save_persistent()
                print "Achievement reached!"
            return True
        return False

    def get_achievement(achLabel):
        if persistent.achievements.has_key(achLabel) and persistent.achievements[achLabel] == True:
            return True
        return False







#
