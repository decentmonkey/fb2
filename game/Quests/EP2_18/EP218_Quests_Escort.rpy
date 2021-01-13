default ep218_quests_meeting1_planned = False

label ep218_quests_escort_check1:
    if ep217_party_day > 0 and monicaCandiseHotelMeetingPlanned == False and monicaAbbyHotelMeetingPlanned == False:
        # встретились и с Кэндис и с Эбби
        $ questHelp("escort_21")
        $ ep218_quests_meeting1_planned = True
    return

label ep218_quests_escort2_meeting: # встреча с Кэндис
    $ ep218_quests_meeting1_planned = False
    $ remove_hook(label="ep218_quests_escort_resume")
    call ep218_dialogues3_escort_1()
    if _return == -1:
        $ questHelp("escort_21", False)
        $ add_hook("Visitor1", "ep218_quests_escort2_meeting", scene="rich_hotel_restaurant", label="ep218_quests_escort_resume")
        return False

    return False
