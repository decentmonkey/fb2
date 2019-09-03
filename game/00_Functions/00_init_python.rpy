python early:
    import re
    import os
    import binascii
    import time
    import pygame.scrap
    import random
    import math
    import json
    import copy
    import pygame
    import types
    from random import shuffle

    dialogue_active_flag = False
    list_files = []
    list_files_dict = {}
    list_files_parsed = False
    list_files_scene_drop_flag = False
    last_renpy_files_list_crc = 0

    list_files_active = True

    def missing_filename_callback(image):
        global episode
        if episode == 1:
#            emptyFileName = get_image_filename("empty.png")
            return im.Image("images/icons/empty.png")
        return None

    def refresh_list_files():
        global list_files, list_files_active
        global list_files_dict, list_files_parsed, list_files_scene_drop_flag, last_renpy_files_list_crc
        if list_files_active == False:
            return False
#        if list_files_parsed == True:
#            if list_files_scene_drop_flag == True:
#                return False
#            list_files = renpy.list_files()
#            crc = 0
#            for filename in list_files:
#                crc += binascii.crc32(filename)
#            if crc == last_renpy_files_list_crc and len(list_files_dict) > 0:
#                list_files_scene_drop_flag = True
#                return False
#            last_renpy_files_list_crc = crc
#        else:
#            list_files = renpy.list_files()
        list_files = renpy.list_files()
        for filename in list_files:
            baseName = os.path.basename(os.path.splitext(filename)[0]).lower()
            list_files_dict[baseName] = filename
        list_files_parsed = True
        list_files_scene_drop_flag = True
        list_files_active = False
        return

    def refresh_list_files_forced():
        global list_files
        global list_files_dict, list_files_parsed, list_files_scene_drop_flag, last_renpy_files_list_crc

        for filename in list_files:
            baseName = os.path.basename(os.path.splitext(filename)[0]).lower()
            list_files_dict[baseName] = filename
        list_files_parsed = True
        list_files_scene_drop_flag = True
        return

    def get_image_filename(in_filename, warning=False, retry=False):
        in_filename = in_filename.lower()
        if list_files_dict.has_key(in_filename):
            return list_files_dict[in_filename]
#        for filename in list_files:
#            get_file_basename(filename)
#            if in_filename == os.path.basename(os.path.splitext(filename)[0]).lower():
#                return filename.lower()
        if retry == False:
            refresh_list_files()
            return get_image_filename(in_filename, warning, True)
        if warning == True:
            ui.text("Image not found!\n" + in_filename + "\nScene name: " + scene_name, size=40, xalign=0.5, yalign=0.5)
            renpy.pause()
        return False

    def get_filename(in_filename, retry=False):
        in_filename = in_filename.lower()
        if list_files_dict.has_key(in_filename):
            return list_files_dict[in_filename]
#        for filename in list_files:
#            if in_filename == os.path.basename(os.path.splitext(filename)[0]).lower():
#                return filename.lower()
        if retry == False:
            refresh_list_files()
            return get_filename(in_filename, True)
        return False

    def get_image_filename_deprecated(in_filename):
        directories_list = ["", "Sprites/", "Masks/", "Overlays/"];
        for dir1 in directories_list:
            if renpy.loadable(dir1 + in_filename + ".png"): return (dir1 + in_filename + ".png").lower()
            if renpy.loadable(dir1 + in_filename + ".jpg"): return (dir1 + in_filename + ".jpg").lower()
#        print renpy.loadable("Sprites/DickSecretary_Dick_Secretary.png")
        return False


    def img_find_path(var):
        checkPath = get_image_filename("img_" + str(var))
        if checkPath != False: return checkPath
        checkPath = get_image_filename("zimg_" + str(var))
        if checkPath != False: return checkPath
        checkPath = get_image_filename(str(var))
        if checkPath != False: return checkPath
        return str(var)

    def img_find_path_ext(var):
        checkPath = get_image_filename("img_" + str(var))
        if checkPath != False: return [checkPath, "img_" + str(var)]
        checkPath = get_image_filename("zimg_" + str(var))
        if checkPath != False: return [checkPath, "zimg_" + str(var)]
        checkPath = get_image_filename(str(var))
        if checkPath != False: return [checkPath, str(var)]
        return str(var)

    def sortBySceneDataZOrder(obj_name):
        return obj_name

    def hide_screens_for_scene():
        global dialogue_active_flag
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        dialogue_active_flag = False
#        renpy.hide_screen("show_image_screen")
        renpy.hide_screen("dialogue_image_right")
        renpy.hide_screen("dialogue_image_left")
        renpy.hide_screen("dialogue_image_center")

    def get_resolution_x(x_pos):
        return int(float(x_pos) / 1920.0 * config.screen_width)
    def get_resolution_y(y_pos):
        return int(float(y_pos) / 1080.0 * config.screen_height)

    def getImageSize(img, imageName):
        global imagesSizesCache
        if imagesSizesCache.has_key(imageName):
            return imagesSizesCache[imageName]
        imageSize = im.cache.get(img).get_size()
        imagesSizesCache[imageName] = imageSize
        return imageSize

    def imageSizeClearCache():
        global imagesSizesCache
        imagesSizesCache = {}
        return

    def parseFileNameResSuffix(fileName):
        global gui, res
        if gui.flag720 == False:
            return fileName.replace("_720p", "")
        if fileName.find(res.suffix) != -1:
            return fileName
        splittedFileName = fileName.split(".")
        splittedFileName[-2] = splittedFileName[-2] + res.suffix
        return ".".join(splittedFileName)

init -3 python:
    if persistent.lang is None:
        persistent.lang = "english"


    lang = persistent.lang

init python:
    config.main_menu.insert(3, (u'Language', "language_chooser", "True"))
