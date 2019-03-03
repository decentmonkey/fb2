﻿# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       defaults.rpy [デフォルト]
#                                                                                                       作成者： Andrea Rubenstein
#                                                                                                       作成日：2011/07/19
#                                                                                                       更新日：2011/09/28 (アンディ)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

init -1000 python:
    DEFAULT_LANG = "en"

##############################################################################
#       関数
##############################################################################

##################################################
#　クラス名：set_default_langauge
#　説　明　：言語のデフォルトを設定する処理
##################################################
    def set_default_langauge(lang):
         DEFAULT_LAN = lang

#EOF
