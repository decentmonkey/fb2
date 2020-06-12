label activation_menu1:
    python:
        activationComplete = False
        codeStr = getLocalCode()
        code1 = codeStr[0:4]
        code2 = codeStr[4:8]
        code3 = codeStr[8:12]
        code4 = codeStr[12:16]
        acode1 = ""
        acode2 = ""
        acode3 = ""
        acode4 = ""
        entered_code = "                "
        entered_code_idx = 0
        acolor = c_orange
    sound click1
    hide screen noactivation_overlay
    hide screen noactivation_overlay2




label activation_menu1_loop1:
    python:
        acode1 = entered_code[0:4]
        acode2 = entered_code[4:8]
        acode3 = entered_code[8:12]
        acode4 = entered_code[12:16]
    show screen activationmenu_screen(code1, code2, code3, code4, acode1, acode2, acode3, acode4, acolor)
    $ interact_data = None
    $ interact_data = ui.interact()
    if interact_data != None:
        if interact_data == "empty":
            jump activation_menu1_loop1
        if interact_data == "Close":
            sound click1
        if interact_data >= "0" and  interact_data <= "9":
            if entered_code_idx == 16:
                sound click_denied
                jump activation_menu1_loop1
            $ entered_code = entered_code[0:entered_code_idx] + str(interact_data) + entered_code[entered_code_idx+1:]
            $ entered_code_idx += 1

            if entered_code_idx == 16:
                $ checkst = decodes(entered_code, language_dict["checkactivation"][1][1:])
                if checkst != "activation complete":
                    $ print "denied!"
                    $ acolor = c_red
                    sound snd_ui_not_working
                    jump activation_menu1_loop1
                else:
                    $ print "approved!"
                    $ acolor = c_green
                    sound level_up
                    $ store_music()
                    music cat_purr
                    if persistent.enckey is None:
                        $ persistent.enckey = {}
                    $ persistent.enckey[config.version] = entered_code
                    $ activationComplete = True
                    jump activation_menu1_loop1


            $ acolor = c_orange
            sound snd_ui_not_working
            jump activation_menu1_loop1
        if interact_data == "Clear":
            $ acolor = c_orange
            sound click_denied
            if entered_code_idx > 0:
                $ entered_code_idx -= 1
            $ entered_code = entered_code[0:entered_code_idx] + " " + entered_code[entered_code_idx+1:]
            jump activation_menu1_loop1

    hide screen activationmenu_screen
    if activationComplete == False:
        show screen noactivation_overlay()
        show screen noactivation_overlay2()
    else:
        $ restore_music()

    return None
