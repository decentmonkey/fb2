python early:
    language_dict = json.loads(renpy.file("language_dict.json").read())
#    language_dict = renpy.file("language_dict.json").read()
    language_fields = {None:1, "english":2, "german":3, "spain":4, "chinese":5}

#    open(config.basedir + "/game/update_data.json", "wb").write(str)
    def parse_tstr(str1):
        result = re.findall(r'\[(.*?)\]', str1)
        for var1 in result:
            if globals().has_key(var1):
                str1 = str1.replace("[" + var1 + "]", str(globals()[var1]))
            else:
                str1 = str1.replace("[" + var1 + "]", "{c}" + var1 + "{/c}")
        return str1
    def t_(s):
        return s
#        global _preferences, language_fields, language_dict
#        lang = _preferences.language
#        if language_dict.has_key(s):
#            s = language_dict[s][language_fields[lang]]
#        return parse_tstr(s)
    def t__(s):
        global _preferences, language_fields, language_dict
        lang = _preferences.language
        st = s
        if language_dict.has_key(s):
            st = language_dict[s][language_fields[lang]]
            if st == "":
                st = language_dict[s][language_fields["english"]]
                if st == "":
                    st = s
        return parse_tstr(st)
