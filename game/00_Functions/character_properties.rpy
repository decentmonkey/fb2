init python:
    def get_bitchmeter_description():
        global bitchmeterValue, maxBitchness, monicaBitch
        bitchmeter_captions = ["Shy Girl", "Decent Girl", "Casual Girl", "Hot-Tempered", "Bitch", "Complete Bitch", "Bitch from the Hell"]

        if bitchmeterValue <= maxBitchness / 2:
            monicaBitch = False
        else:
            monicaBitch = True

#        if bitchmeterValue < float(maxBitchness) / 100 * 20:
        if bitchmeterValue <= 153:
            return bitchmeter_captions[0]
        if bitchmeterValue <= float(maxBitchness) / 100 * 49:
            return bitchmeter_captions[1]
        if bitchmeterValue <= float(maxBitchness) / 100 * 51:
            return bitchmeter_captions[2]
        if bitchmeterValue < float(maxBitchness) / 100 * 60:
            return bitchmeter_captions[3]
        if bitchmeterValue < float(maxBitchness) / 100 * 80:
            return bitchmeter_captions[4]
        if bitchmeterValue < float(maxBitchness) / 100 * 100:
            return bitchmeter_captions[5]
        if bitchmeterValue >= maxBitchness:
            return bitchmeter_captions[6]

    def check_object_has_character(obj_name):
        global char_info
        if char_info.has_key(obj_name) == True:
            return True
        return False


label bitch(amount, place=False):
    $ global bitchmeter_places
    if place != False:
        if bitchmeter_places.has_key(place):
            return
        $ bitchmeter_places[place] = amount


    if bitchmeterValue > maxBitchness / 2 and amount < 0:
        $ amount *= 3
    if bitchmeterValue <= maxBitchness / 2 and amount > 0:
        $ amount *= 3

    $ bitchmeterValue += amount
    if amount > 0:
        show screen notify ("Bitchness increased!")
    else:
        show screen notify ("Bitchness decreased!")
    return
