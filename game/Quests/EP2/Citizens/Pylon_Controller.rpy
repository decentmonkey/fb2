define boobsImages = [8506, 8507, 8508, 8509, 8510, 8511, 8512, 8513, 8514, 8515]
define boobsImagesTonque = [8516, 8517]
define assImages = [8518, 8519, 8520, 8521, 8522, 8523, 8524, 8525, 8526, 8527]
define pylonClothDanceImages = [8518, 8519]
define nakedboobsImages = [8528, 8529]

default pylonLastCamera = 1

init python:
    def pylon_controller_get_object_path(assetName, suffix1 = ""):
        assetsList = []
        imageFileName = get_image_filename(assetName + suffix1)
        if imageFileName != False:
            assetsList.append([assetName + suffix1, imageFileName])
#        overlayFileName = get_image_filename()
        return assetsList

label pylonController(citizenBehaviorSuffix, monicaBehaviorSuffix, cameraIn = False):
    if cameraIn != False:
        $ camera = cameraIn
    else: #сменяем камеру каждый вызов
        if pylonLastCamera == 1:
            $ camera = 2
        if pylonLastCamera == 2:
            $ camera = 1

    $ pylonLastCamera = camera
    if pylonPreset == 1:
        if camera == 1:
            $ cameraId = 1
        if camera == 2:
            $ cameraId = 2
    if pylonPreset == 2:
        if camera == 1:
            $ cameraId = 2
        if camera == 2:
            $ cameraId = 1

    $ sceneImage = get_image_filename("scene_Hostel_Edge_Camera" + str(cameraId))
    $ monicaAssetName = "Hostel_Edge_Pylon_Monica_" + str(monicaBehaviorSuffix) + "_c" + str(cameraId)
    $ citizenAssetName = "Dial_Citizen_Pylon_" + str(citizenId) + "_" + str(citizenBehaviorSuffix) + "_c" + str(cameraId)

    $ objectsList = []
    if cameraId == 1:
        python:
            objectsList = objectsList + pylon_controller_get_object_path(monicaAssetName, "_overlay") + pylon_controller_get_object_path(citizenAssetName, "_overlay")
            objectsList = objectsList + pylon_controller_get_object_path(monicaAssetName) + pylon_controller_get_object_path(citizenAssetName)

    if cameraId == 2:
        python:
            objectsList = objectsList + pylon_controller_get_object_path(citizenAssetName, "_overlay") + pylon_controller_get_object_path(monicaAssetName, "_overlay")
            objectsList = objectsList + pylon_controller_get_object_path(citizenAssetName) + pylon_controller_get_object_path(monicaAssetName)

    $ renpy.scene()
    show screen pylon_screen(sceneImage, objectsList)
    $ print "objectsList"
    $ print objectsList
    return
