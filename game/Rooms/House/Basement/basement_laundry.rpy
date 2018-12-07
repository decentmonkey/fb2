label basement_laundry:
    $ print "enter_basement_laundry"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_image = "scene_Laundry1"

    $ basementHoleIncomingDirection = "Laundry"
    music Mandeville
    return

label basement_laundry_init:
    $ add_object_to_scene("Accessories1", {"type":2, "base":"Basement_Laundry_Accessories1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Accessories2", {"type":2, "base":"Basement_Laundry_Accessories2", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Basket1", {"type":2, "base":"Basement_Laundry_Basket1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Basket2", {"type":2, "base":"Basement_Laundry_Basket2", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Cloth1", {"type":2, "base":"Basement_Laundry_Cloth1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Drying_Machine", {"type":2, "base":"Basement_Laundry_Drying_Machine", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Rags1", {"type":2, "base":"Basement_Laundry_Rags1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Toilet_Paper", {"type":2, "base":"Basement_Laundry_Toilet_Paper", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Towels1", {"type":2, "base":"Basement_Laundry_Towels1", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Washer", {"type":2, "base":"Basement_Laundry_Washer", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})
    $ add_object_to_scene("Clothes_Pin", {"type":2, "base":"Basement_Laundry_Clothes_Pin", "click" : "basement_laundry_environment", "actions" : "l", "zorder" : 0, "group":"environment", "active":False})



    $ add_object_to_scene("Teleport_Box1", {"type":2, "base":"Basement_Laundry_Box1", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0, "group":"laundry_teleport", "active":False})
    $ add_object_to_scene("Teleport_Box2", {"type":2, "base":"Basement_Laundry_Box2", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0, "group":"laundry_teleport", "active":False})
    $ add_object_to_scene("Teleport_Box3", {"type":2, "base":"Basement_Laundry_Box3", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0, "group":"laundry_teleport", "active":False})
    $ add_object_to_scene("Teleport_Box4", {"type":2, "base":"Basement_Laundry_Box4", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0, "group":"laundry_teleport", "active":False})
    $ add_object_to_scene("Teleport_Box5", {"type":2, "base":"Basement_Laundry_Box5", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0, "group":"laundry_teleport", "active":False})
    $ add_object_to_scene("Teleport_Box6", {"type":2, "base":"Basement_Laundry_Box6", "click" : "basement_laundry_teleport", "actions" : "l", "zorder" : 0, "group":"laundry_teleport", "active":False})

    $ add_object_to_scene("Teleport_Basement_Hole", {"type":3, "text" : _("В ПОДВАЛ"), "larrow" : "arrow_dl", "base":"empty", "click" : "basement_laundry_teleport", "xpos" : 183, "ypos" : 873, "zorder":11, "teleport":True})
    $ add_object_to_scene("Teleport_Basement_Pool", {"type":3, "text" : _("НАЗАД К БАССЕЙНУ"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "basement_laundry_teleport", "xpos" : 960, "ypos" : 956, "zorder":11, "teleport":True})

    return

label basement_laundry_teleport:
    if obj_name == "Teleport_Basement_Pool":
        call change_scene("basement_pool")
        return
    if obj_name == "Teleport_Basement_Hole":
        $ basementHoleIncomingDirection = "Laundry"
        call change_scene("basement_hole")
        return
    if obj_name == "Teleport_Basement_Ironing_Board":
        call change_scene("basement_laundry2")
        return
    if laundryBoxesActive == False:
        m "Мне ничего не надо в этом ящике."
        return
    if obj_name == "Teleport_Box1":
        call change_scene("basement_laundry_box1", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box2":
        call change_scene("basement_laundry_box2", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box3":
        call change_scene("basement_laundry_box3", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box4":
        call change_scene("basement_laundry_box4", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box5":
        call change_scene("basement_laundry_box5", "Fade", "desk_open")
        return
    if obj_name == "Teleport_Box6":
        call change_scene("basement_laundry_box6", "Fade", "desk_open")
        return
    return

label basement_laundry_environment:
    if obj_name == "Accessories1":
        m "Какие-то щетки и моющие средства."
    if obj_name == "Accessories2":
        m "Какие-то гели и губки."
    if obj_name == "Clothes_Pin":
        m "ЧТО??"
        "Прищепки для белья?
        Деревянные???"
    if obj_name == "Basket1":
        m "Эта корзина пустая."
    if obj_name == "Basket2":
        m "Мне не дотянуться до этих корзин.
        Что там в них?"
    if obj_name == "Washer":
        m "Машина для сушки белья..."
        "Пустая..."
    if obj_name == "Cloth1":
        m "Какие-то тряпки.
        Я не могу назвать это одеждой."
        "Наверное это что-то из одежды Юлии.
        Фи!"
    if obj_name == "Rags1":
        m "Какие-то тряпки.
        Это явно не мое платье!"
    if obj_name == "Toilet_Paper":
        m "Туалетная бумага?!
        И я тянулась туда чтобы об этом узнать?!"
    if obj_name == "Towels1":
        m "Какие-то полотенца, но мне толком не разглядеть отсюда."
    if obj_name == "Drying_Machine":
        m "Судя по всему это стиральная машина..."
        "Пустая..."

    return
