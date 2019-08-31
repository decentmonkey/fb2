default visitorsVisits = {}

label ep27_pub_visitors_init:
    if get_pub_visitor_visits("Pub_Visitor9") > 0:
        $ pubVisitor9Suffix = "_Food"
    return

label ep27_pub_visitors_click:
    if act=="l":
        return
#    if obj_name in pubMonicaWaitressVisitorsServed:
#        call ep27_dialogues7_pub19()
#        return False
    music2 pub_noise1_low
    $ visitsCount = get_pub_visitor_visits(obj_name)
    if obj_name == "Pub_Visitor1":
        pass
    if obj_name == "Pub_Visitor2":
        pass
    if obj_name == "Pub_Visitor3":
        pass
    if obj_name == "Pub_Visitor4":
        pass
    if obj_name == "Pub_Visitor5":
        if visitsCount == 0:
            call customer5_1stmeeting()
            $ pubVisitor5Suffix = "_Food"
        if visitsCount > 0:
            call customer5_serve1()
            $ pubVisitor5Suffix = "_Food"
        $ autorun_to_object("customer5_afterserve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor6":
        call customer6_serve1()
        $ autorun_to_object("customer6_afterserve1", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor7":
        pass
    if obj_name == "Pub_Visitor8":
        pass
    if obj_name == "Pub_Visitor9":
        if visitsCount == 0:
            call customer9_1stmeeting()
            $ autorun_to_object("customer9_afterserve1", scene=scene_name)
        if visitsCount > 0:
            call customer9_serve1()
            if _return == False:
                $ autorun_to_object("customer9_afterserve1", scene=scene_name)
            else:
                $ autorun_to_object("customer9_afterserve2", scene=scene_name)
        pass
    if obj_name == "Pub_Visitor10":
        pass
    if obj_name == "Pub_Visitor11":
        call customer11_1stmeeting()
        $ pubVisitor11Suffix = "_Food"
    if obj_name == "Pub_Visitor12":
        if visitsCount == 0:
            call customer12_1stmeeting()
        if visitsCount > 0:
            call customer12_serve1()
            $ pubVisitor12Suffix = "_Food"
        $ autorun_to_object("customer12_afterserve1", scene=scene_name)
        pass

    $ pubMonicaWaitressVisitorsServed.append(obj_name)
    $ increment_pub_visitor_visits(obj_name)
    $ pubMonicaWaitressServedCustomersToday += 1
    $ pubMonicaWaitressServedCustomersTotal += 1
    if pubMonicaWaitressServedCustomersToday >= pubMonicaWaitressVisitorsPerDay:
        call ep27_quests_pub_work5() # Заканчиваем работу
        return False
    $ scene_sound = "highheels_short_walk"
    call refresh_scene_fade()
    return False

init python:
    def get_pub_visitor_visits(obj_name):
        global visitorsVisits
        if visitorsVisits.has_key(obj_name):
            return visitorsVisits[obj_name]
        return 0

    def increment_pub_visitor_visits(obj_name):
        global visitorsVisits
        if visitorsVisits.has_key(obj_name):
            visitorsVisits[obj_name] += 1
        else:
            visitorsVisits[obj_name] = 1
        return

    def add_tips(amount):
        global pubMonicaWaitressTips
        pubMonicaWaitressTips += amount
        add_money(amount)
        return
