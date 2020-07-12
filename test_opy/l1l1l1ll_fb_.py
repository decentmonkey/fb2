# coding: UTF-8
import sys
l111llll_fb_ = sys.version_info [0] == 2
l11l1l1_fb_ = 2048
l1lll1l11_fb_ = 7
def l111l1_fb_ (l1lllll_fb_):
    global l111l1l1_fb_
    l11lll11_fb_ = ord (l1lllll_fb_ [-1])
    l1111lll_fb_ = l1lllll_fb_ [:-1]
    l1ll1ll1_fb_ = l11lll11_fb_ % len (l1111lll_fb_)
    l1ll111_fb_ = l1111lll_fb_ [:l1ll1ll1_fb_] + l1111lll_fb_ [l1ll1ll1_fb_:]
    if l111llll_fb_:
        l1l1ll_fb_ = unicode () .join ([unichr (ord (char) - l11l1l1_fb_ - (l1l1llll_fb_ + l11lll11_fb_) % l1lll1l11_fb_) for l1l1llll_fb_, char in enumerate (l1ll111_fb_)])
    else:
        l1l1ll_fb_ = str () .join ([chr (ord (char) - l11l1l1_fb_ - (l1l1llll_fb_ + l11lll11_fb_) % l1lll1l11_fb_) for l1l1llll_fb_, char in enumerate (l1ll111_fb_)])
    return eval (l1l1ll_fb_)
    def l1lllll11_fb_(l1ll1l11_fb_):
        l11111l_fb_ = l1ll1l11_fb_.l1l1_fb_()
        l1l11l1_fb_ = l1ll1l11_fb_.l1l1_fb_()
        return (l11111l_fb_, l1l11l1_fb_)
    def l1lll11ll_fb_(l1llll1l_fb_):
        l11lll1l_fb_, l1l1111_fb_ = l1llll1l_fb_
        try:
            l11ll111_fb_ = l1lllll1_fb_(str(l1ll11ll_fb_.eval(l11lll1l_fb_)) + l111l1_fb_ (u"ࠦࡤࡵࡶࡦࡴࡶࡴࡷ࡯ࡴࡦࠤࠀ"))
        except:
            l11ll111_fb_ = l1lllll1_fb_(str(l11lll1l_fb_) + l111l1_fb_ (u"ࠧࡥ࡯ࡷࡧࡵࡷࡵࡸࡩࡵࡧࠥࠁ"))
        if l11ll111_fb_[0] == False:
            l11111l1_fb_ = l111l1_fb_ (u"ࠨࡩ࡮ࡣࡪࡩࡸ࠵ࡓ࡭࡫ࡧࡩࡸ࠵ࡩ࡮ࡩࡢࠦࠂ") + l11ll111_fb_[1] + l111l1_fb_ (u"ࠢ࠯࡬ࡳ࡫ࠧࠃ")
        else:
            l11111l1_fb_ = l11ll111_fb_[0]
            l11lll1l_fb_ = l11ll111_fb_[1]
        try:
            l1l1111_fb_ = l1ll11ll_fb_.eval(l1l1111_fb_)
        except:
            l1l1111_fb_ = l1l1111_fb_
        l111l1ll_fb_ = l1111l1_fb_(l11lll1l_fb_)
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠣࡵ࡫ࡳࡼࡥࡩ࡮ࡣࡪࡩࡤࡹࡣࡳࡧࡨࡲࡤ࡯࡭ࡢࡩࡨࡣࡴࡼࡥࡳ࡮ࡤࡽࠧࠄ"), l11111l1_fb_, l111l1ll_fb_, l1l1111_fb_)
        return
    def l1ll1_fb_(l1llll1l_fb_):
        l11lll1l_fb_, l1l1111_fb_ = l1llll1l_fb_
        try:
            l11ll111_fb_ = l1lllll1_fb_(str(l1ll11ll_fb_.eval(l11lll1l_fb_)) + l111l1_fb_ (u"ࠤࡢࡳࡻ࡫ࡲࡴࡲࡵ࡭ࡹ࡫ࠢࠅ"))
        except:
            l11ll111_fb_ = l1lllll1_fb_(str(l11lll1l_fb_) + l111l1_fb_ (u"ࠥࡣࡴࡼࡥࡳࡵࡳࡶ࡮ࡺࡥࠣࠆ"))
        if l11ll111_fb_[0] == False:
            l11111l1_fb_ = l111l1_fb_ (u"ࠦ࡮ࡳࡡࡨࡧࡶ࠳ࡘࡲࡩࡥࡧࡶ࠳࡮ࡳࡧࡠࠤࠇ") + l11ll111_fb_[1] + l111l1_fb_ (u"ࠧ࠴ࡪࡱࡩࠥࠈ")
        else:
            l11lll1l_fb_ = l11ll111_fb_[1]
            l11111l1_fb_ = l11ll111_fb_[0]
        return [l111111_fb_(l11111l1_fb_)]
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠨ࡯ࡷࡧࡵࡰࡦࡿࠢࠉ"), parse=l1lllll11_fb_, l11l1l_fb_=l1lll11ll_fb_, l11l1lll_fb_=l1ll1_fb_) #кастомный l1l11l1_fb_
    def l1111ll1_fb_(l):
        return (l.l1l1_fb_(), l.rest())
#        return l.string()
    def l1lll1l_fb_(l):
        return (l.l1l1_fb_(), l111l1_fb_ (u"ࠢࡥࠤࠊ"))
    def l11111_fb_(l):
        return (l.l1l1_fb_(), l111l1_fb_ (u"ࠣࡨࠥࠋ"))
    def l1111l_fb_(l):
        return (l.l1l1_fb_(), l111l1_fb_ (u"ࠤࡩࡰࠧࠌ"))
    def l1l1ll1_fb_(l111ll11_fb_):
        global l1llll_fb_, l1ll111l_fb_, l11l_fb_
#        l11l_fb_.l1111l1l_fb_ = False
#        l11l_fb_.l1ll11l_fb_ = False
        s = l111ll11_fb_[0]
        l1llllll_fb_ = l111ll11_fb_[1]
        try:
            l11ll111_fb_ = l1lllll1_fb_(l1ll11ll_fb_.eval(s))
        except:
            l11ll111_fb_ = l1lllll1_fb_(s)
        if l11ll111_fb_[0] == False:
            l11111l1_fb_ = l111l1_fb_ (u"ࠥ࡭ࡲࡧࡧࡦࡵ࠲ࡗࡱ࡯ࡤࡦࡵ࠲࡭ࡲ࡭࡟ࠣࠍ") + l11ll111_fb_[1] + l111l1_fb_ (u"ࠦ࠳ࡰࡰࡨࠤࠎ")
        else:
            l11111l1_fb_ = l11ll111_fb_[0]
        l111ll1_fb_(l11ll111_fb_[1])
        if (l1ll11ll_fb_.l1l1l111_fb_(l111l1_fb_ (u"ࠧࡹࡡࡺࠤࠏ")) != None or l1ll11ll_fb_.l1l1l111_fb_(l111l1_fb_ (u"ࠨࡣࡩࡱ࡬ࡧࡪࠨࠐ")) != None or l1ll11ll_fb_.l1l1l111_fb_(l111l1_fb_ (u"ࠢࡸ࡫ࡱࡨࡴࡽࠢࠑ")) != None or l1llll_fb_ == True) and l1lll1l1l_fb_.l1ll11_fb_ == True and l1ll11ll_fb_.l1l1l111_fb_(l111l1_fb_ (u"ࠣࡵ࡫ࡳࡼࡥࡩ࡮ࡣࡪࡩࡤࡹࡣࡳࡧࡨࡲࡤ࡯࡭ࡢࡩࡨࠦࠒ")) != None:
            l1ll11ll_fb_.l11l1111_fb_(l111l1_fb_ (u"ࠤࡶࡥࡾࠨࠓ"))
            l1ll11ll_fb_.l11l1111_fb_(l111l1_fb_ (u"ࠥࡧ࡭ࡵࡩࡤࡧࠥࠔ"))
            l1ll11ll_fb_.l1l11ll_fb_(l111l1_fb_ (u"ࠦࡼ࡯࡮ࡥࡱࡺࠦࠕ"))
            l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠧࡪࡩࡢ࡮ࡲ࡫ࡺ࡫࡟ࡥࡱࡺࡲࡤࡧࡲࡳࡱࡺࠦࠖ"))
            l1ll11ll_fb_.l1lll_fb_()
            l1ll11ll_fb_.l11l1111_fb_(l111l1_fb_ (u"ࠨࡤࡪࡣ࡯ࡳ࡬ࡻࡥࡠࡦࡲࡻࡳࡥࡡࡳࡴࡲࡻࠧࠗ"))
            l1llll_fb_ = False
        l1ll11ll_fb_.l1ll1lll_fb_()
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠢࡴࡪࡲࡻࡤ࡯࡭ࡢࡩࡨࡣࡸࡩࡲࡦࡧࡱࡣ࡮ࡳࡡࡨࡧࠥ࠘"), l11111l1_fb_)
        l1l111l1_fb_ = False
        l1ll111l_fb_ = True
        if l1llllll_fb_ and l1llllll_fb_ != l111l1_fb_ (u"ࠣࠤ࠙"):
            l1l1111l_fb_ = {
                l111l1_fb_ (u"ࠤࡩࠦࠚ"): l11l1_fb_,
                l111l1_fb_ (u"ࠥࡨࠧࠛ"): ll_fb_,
                l111l1_fb_ (u"ࠦ࡫ࡲࠢࠜ"): l1l1l_fb_
            }
            if l1l1111l_fb_.has_key(l1llllll_fb_):
                l1llllll_fb_ = l1l1111l_fb_[l1llllll_fb_]
            else:
                try:
                    l1llllll_fb_ = l1ll11ll_fb_.eval(l1llllll_fb_)
                except:
                    l1llllll_fb_ = l1llllll_fb_
            l1ll11ll_fb_.l1ll1l1_fb_(l1llllll_fb_)
        return
    def l1llll1ll_fb_(l111ll11_fb_):
        s, l1llllll_fb_ = l111ll11_fb_
        try:
            l11ll111_fb_ = l1lllll1_fb_(l1ll11ll_fb_.eval(s))
        except:
            l11ll111_fb_ = l1lllll1_fb_(s)
        if l11ll111_fb_[0] == False:
            l11111l1_fb_ = l111l1_fb_ (u"ࠧ࡯࡭ࡢࡩࡨࡷ࠴࡙࡬ࡪࡦࡨࡷ࠴࡯࡭ࡨࡡࠥࠝ") + l11ll111_fb_[1] + l111l1_fb_ (u"ࠨ࠮࡫ࡲࡪࠦࠞ")
        else:
            l11111l1_fb_ = l11ll111_fb_[0]
        return [l111111_fb_(l11111l1_fb_)]
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠢࡪ࡯ࡪࠦࠟ"), parse=l1111ll1_fb_, l11l1l_fb_=l1l1ll1_fb_, l11l1lll_fb_=l1llll1ll_fb_) #кастомный l1ll1lll_fb_
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠣ࡫ࡰ࡫ࡩࠨࠠ"), parse=l1lll1l_fb_, l11l1l_fb_=l1l1ll1_fb_, l11l1lll_fb_=l1llll1ll_fb_)
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠤ࡬ࡱ࡬࡬ࠢࠡ"), parse=l11111_fb_, l11l1l_fb_=l1l1ll1_fb_, l11l1lll_fb_=l1llll1ll_fb_)
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠥ࡭ࡲ࡭ࡦ࡭ࠤࠢ"), parse=l1111l_fb_, l11l1l_fb_=l1l1ll1_fb_, l11l1lll_fb_=l1llll1ll_fb_)
    def l1lll1ll1_fb_(s):
        global l1llll_fb_, l1ll111l_fb_
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠦࡩ࡯ࡡ࡭ࡱࡪࡹࡪࡥࡩ࡮ࡣࡪࡩࡤࡨ࡬ࡢࡥ࡮ࡣࡴࡼࡥࡳ࡮ࡤࡽࠧࠣ"))
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠧࡪࡩࡢ࡮ࡲ࡫ࡺ࡫࡟ࡪ࡯ࡤ࡫ࡪࡥ࡬ࡦࡨࡷࠦࠤ"), l1l11ll1_fb_(s), l11l_fb_.l1ll1l_fb_ / 2, l11l_fb_.l1lll1111_fb_)
        l1ll111l_fb_ = True
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠨࡩ࡮ࡩ࡯ࠦࠥ"), parse=l1111ll1_fb_, l11l1l_fb_=l1lll1ll1_fb_, l11l1lll_fb_=l1llll1ll_fb_)
    def l1l1l1l1_fb_(s):
        global l1llll_fb_, l1ll111l_fb_
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠢࡥ࡫ࡤࡰࡴ࡭ࡵࡦࡡ࡬ࡱࡦ࡭ࡥࡠࡤ࡯ࡥࡨࡱ࡟ࡰࡸࡨࡶࡱࡧࡹࠣࠦ"))
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠣࡦ࡬ࡥࡱࡵࡧࡶࡧࡢ࡭ࡲࡧࡧࡦࡡࡵ࡭࡬࡮ࡴࠣࠧ"), l1l11ll1_fb_(s), l11l_fb_.l1ll1l_fb_ / 2, l11l_fb_.l1lll1111_fb_)
        l1ll111l_fb_ = True
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠤ࡬ࡱ࡬ࡸࠢࠨ"), parse=l1111ll1_fb_, l11l1l_fb_=l1l1l1l1_fb_, l11l1lll_fb_=l1llll1ll_fb_)
    def l11ll1ll_fb_(s):
        global l1llll_fb_, l1ll111l_fb_
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠥࡨ࡮ࡧ࡬ࡰࡩࡸࡩࡤ࡯࡭ࡢࡩࡨࡣࡧࡲࡡࡤ࡭ࡢࡳࡻ࡫ࡲ࡭ࡣࡼࠦࠩ"))
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠦࡩ࡯ࡡ࡭ࡱࡪࡹࡪࡥࡩ࡮ࡣࡪࡩࡤࡩࡥ࡯ࡶࡨࡶࠧࠪ"), l1l11ll1_fb_(s), l11l_fb_.l1ll1l_fb_ / 2, l11l_fb_.l1lll1111_fb_)
        l1ll111l_fb_ = True
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠧ࡯࡭ࡨࡥࠥࠫ"), parse=l1111ll1_fb_, l11l1l_fb_=l11ll1ll_fb_, l11l1lll_fb_=l1llll1ll_fb_)
    def l1l1ll1l_fb_(l1ll1l11_fb_):
        l1lllllll_fb_ = l1ll1l11_fb_.l1l1_fb_()
        what = l1ll1l11_fb_.l1l1_fb_()
#        what = l1ll1l11_fb_.string()
        if what == None:
            what = l1lllllll_fb_
            l1lllllll_fb_ = l111l1_fb_ (u"ࠨࡎࡰࡱࡱࡩࠧࠬ")
        return (l1lllllll_fb_,what)
    def l1111_fb_(l1llll1l_fb_):
        l1lllllll_fb_, what = l1llll1l_fb_
        try:
            eval(l1lllllll_fb_)
        except:
            l1ll11ll_fb_.error(l111l1_fb_ (u"ࠢࡄࡪࡤࡶࡦࡩࡴࡦࡴࠣࡲࡴࡺࠠࡥࡧࡩ࡭ࡳ࡫ࡤ࠻ࠢࠨࡷࠧ࠭") % l1lllllll_fb_)
        l111_fb_ = l1ll11ll_fb_.l11lll1_fb_(what)
        if l111_fb_:
            l1ll11ll_fb_.error(l111_fb_)
    def l111lll1_fb_(l1llll1l_fb_):
        global l1llll111_fb_
        global l1llll_fb_, l1ll111l_fb_, l11l_fb_
        l1lllllll_fb_, what = l1llll1l_fb_
        if l1lllllll_fb_ == l111l1_fb_ (u"ࠣࡐࡲࡳࡳ࡫ࠢ࠮"):
            l1lllllll_fb_ = l1llll111_fb_
        else:
            l1llll111_fb_ = l1lllllll_fb_
#        l1lllllll_fb_ = t__(eval(l1lllllll_fb_).name)
        what = what[1:-1]
#        what = re.sub(l111l1_fb_ (u"ࡴࠪࡠࡳ࠭࠯") , l111l1_fb_ (u"ࠪࡠࡸ࠭࠰"), what)
        l1llll_fb_ = True
        l1ll111l_fb_ = True
        if l1lll1l1l_fb_.l1l11111_fb_ == True:
            l1l1l1_fb_ = re.sub(l111l1_fb_ (u"ࠦࡡࠧ࡜ࡴࡽ࠴࠰ࢂࠨ࠱"), l111l1_fb_ (u"ࠧࠧ࡜࡯ࠤ࠲"), what)
            l1l1l1_fb_ = re.sub(l111l1_fb_ (u"ࠨ࡜ࡀ࡞ࡶࡿ࠶࠲ࡽࠣ࠳"), l111l1_fb_ (u"ࠢࡀ࡞ࡱࠦ࠴"), l1l1l1_fb_)
            l1l1l1_fb_ = re.sub(l111l1_fb_ (u"ࠣ࡞࠱ࡠࡸࢁ࠱࠭ࡿࠥ࠵"), l111l1_fb_ (u"ࠤ࠱ࡠࡳࠨ࠶"), l1l1l1_fb_)
            l1llll11l_fb_(l1l1l1_fb_) #l1111111_fb_ l1lll111_fb_ l11ll11_fb_
        l111lll_fb_ = l1lll1_fb_.key.l111l11_fb_()
        if l111lll_fb_[l1lll1_fb_.l11ll1l1_fb_]:
            return
        what = re.sub(l111l1_fb_ (u"ࡵࠫ࠭ࡢ࡮࡝ࡵ࠭࠭ࠬ࠷"), l111l1_fb_ (u"ࠦࠥࠨ࠸"), what)
        what = t__(what)
        what = what.replace(l111l1_fb_ (u"ࠧࢦࠢ࠹"), l111l1_fb_ (u"ࠨࠠࠣ࠺"))
        what = re.sub(l111l1_fb_ (u"ࠢ࡝ࠣ࡟ࡷࢀ࠷ࠬࡾࠤ࠻"), l111l1_fb_ (u"ࠣࠣ࡟ࡲࠧ࠼"), what)
        what = re.sub(l111l1_fb_ (u"ࠤ࡟ࡃࡡࡹࡻ࠲࠮ࢀࠦ࠽"), l111l1_fb_ (u"ࠥࡃࡡࡴࠢ࠾"), what)
        what = re.sub(l111l1_fb_ (u"ࠦࡡ࠴࡜ࡴࡽ࠴࠰ࢂࠨ࠿"), l111l1_fb_ (u"ࠧ࠴࡜࡯ࠤࡀ"), what)
        what = re.sub(l111l1_fb_ (u"ࠨࡍࡳ࡞࠱ࡠࡡࡴࠢࡁ"), l111l1_fb_ (u"ࠢࡎࡴ࠱ࠤࠧࡂ"), what)
        what = re.sub(l111l1_fb_ (u"ࠣࡏࡵࡷࡡ࠴࡜࡝ࡰࠥࡃ"), l111l1_fb_ (u"ࠤࡐࡶࡸ࠴ࠠࠣࡄ"), what)
        what = re.sub(l111l1_fb_ (u"ࠥࡑࡸࡢ࠮࡝࡞ࡱࠦࡅ"), l111l1_fb_ (u"ࠦࡒࡹ࠮ࠡࠤࡆ"), what)
        l1ll11ll_fb_.l11l11ll_fb_(l1lllllll_fb_, what)
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠧࠨࡇ"), parse=l1l1ll1l_fb_, l11l1l_fb_=l111lll1_fb_, l1l11l1l_fb_ = l1111_fb_, l111ll_fb_=True) #враппер для l11l11ll_fb_, чтобы подымать флаг активного диалога
    def l1l11l11_fb_(l):
        return None
    def l111l11l_fb_(l1llll1l_fb_):
        global l1llll_fb_, l1ll111l_fb_
        l1ll11ll_fb_.l11l1111_fb_(l111l1_fb_ (u"ࠨࡳࡢࡻࠥࡈ"))
        l1ll11ll_fb_.l11l1111_fb_(l111l1_fb_ (u"ࠢࡤࡪࡲ࡭ࡨ࡫ࠢࡉ"))
        l1ll11ll_fb_.l1l11ll_fb_(l111l1_fb_ (u"ࠣࡹ࡬ࡲࡩࡵࡷࠣࡊ"))
        l1ll11ll_fb_.l11ll1_fb_(l111l1_fb_ (u"ࠤࡧ࡭ࡦࡲ࡯ࡨࡷࡨࡣࡩࡵࡷ࡯ࡡࡤࡶࡷࡵࡷࠣࡋ"))
        l1llll_fb_ = True
        l111lll_fb_ = l1lll1_fb_.key.l111l11_fb_()
        if not l111lll_fb_[l1lll1_fb_.l11ll1l1_fb_]:
            l1ll11ll_fb_.l1lll_fb_()
        l1llll_fb_ = False
        l1ll11ll_fb_.l11l1111_fb_(l111l1_fb_ (u"ࠥࡨ࡮ࡧ࡬ࡰࡩࡸࡩࡤࡪ࡯ࡸࡰࡢࡥࡷࡸ࡯ࡸࠤࡌ"))
        l1llll_fb_ = False
        l1ll111l_fb_ = True
    def l1lll11_fb_(l1llll1l_fb_):
        global l1llll_fb_, l1ll111l_fb_
        l1ll11ll_fb_.l11l1111_fb_(l111l1_fb_ (u"ࠦࡸࡧࡹࠣࡍ"))
        l1ll11ll_fb_.l11l1111_fb_(l111l1_fb_ (u"ࠧࡩࡨࡰ࡫ࡦࡩࠧࡎ"))
        l1ll11ll_fb_.l1l11ll_fb_(l111l1_fb_ (u"ࠨࡷࡪࡰࡧࡳࡼࠨࡏ"))
        l1llll_fb_ = True
        l1ll11ll_fb_.l1lll_fb_()
        l1llll_fb_ = False
        l1ll111l_fb_ = True
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠢࡸࠤࡐ"), parse=l1l11l11_fb_, l11l1l_fb_=l111l11l_fb_) #l1lll1ll_fb_ - оператор ожидания с мигающей стрелкой
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠣࡹࡦࡰࡪࡧ࡮ࠣࡑ"), parse=l1l11l11_fb_, l11l1l_fb_=l1lll11_fb_) #l1lll1ll_fb_ - оператор ожидания с мигающей стрелкой
    def l1lll1l1_fb_(l1llll1l_fb_):
        global l1llll_fb_
        l1llll_fb_ = False
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠤࡺࡧࠧࡒ"), parse=l1l11l11_fb_, l11l1l_fb_=l1lll1l1_fb_) #wait l1l11lll_fb_ clear, удаляет флаг того что висит открытый диалог (для пикч)
    def l1l111ll_fb_(l):
        return l.l1l1_fb_()
    def l1111ll_fb_(l1llll1l_fb_):
        try:
            l1l_fb_ = l1ll11ll_fb_.eval(l1llll1l_fb_)
        except:
            l1l_fb_ = l1llll1l_fb_
        l1llllll1_fb_ = l111l1_fb_ (u"ࠥࡗࡴࡻ࡮ࡥࡵ࠲ࠦࡓ") + str(l1l_fb_) + l111l1_fb_ (u"ࠦ࠳ࡵࡧࡨࠤࡔ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠧࡹ࡯ࡶࡰࡧࠦࡕ"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠨࡓࡰࡷࡱࡨࡸ࠵ࠢࡖ") + str(l1l_fb_) + l111l1_fb_ (u"ࠢ࠯ࡹࡤࡺࠧࡗ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠣࡵࡲࡹࡳࡪࠢࡘ"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠤࡖࡳࡺࡴࡤࡴ࠱࡙ࠥ") + str(l1l_fb_) + l111l1_fb_ (u"ࠥ࠲ࡲࡶ࠳࡚ࠣ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠦࡸࡵࡵ࡯ࡦ࡛ࠥ"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠧࡓࡵࡴ࡫ࡦ࠳ࠧ࡜") + str(l1l_fb_) + l111l1_fb_ (u"ࠨ࠮ࡰࡩࡪࠦ࡝")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠢࡴࡱࡸࡲࡩࠨ࡞"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠣࡏࡸࡷ࡮ࡩ࠯ࠣ࡟") + str(l1l_fb_) + l111l1_fb_ (u"ࠤ࠱ࡻࡦࡼࠢࡠ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠥࡷࡴࡻ࡮ࡥࠤࡡ"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠦࡒࡻࡳࡪࡥ࠲ࠦࡢ") + str(l1l_fb_) + l111l1_fb_ (u"ࠧ࠴࡭ࡱ࠵ࠥࡣ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠨࡳࡰࡷࡱࡨࠧࡤ"))
            return
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠢࡴࡱࡸࡲࡩࠨࡥ"), parse=l1l111ll_fb_, l11l1l_fb_=l1111ll_fb_) #l11llll1_fb_ - оператор воспроизведения звука
    def l111111l_fb_(l):
        return l.l1l1_fb_()
    def l111l111_fb_(l1llll1l_fb_):
        try:
            l1llll1l1_fb_ = l1ll11ll_fb_.eval(l1llll1l_fb_)
        except:
            l1llll1l1_fb_ = l1llll1l_fb_
        l1llllll1_fb_ = l111l1_fb_ (u"ࠣࡕࡲࡹࡳࡪࡳ࠰ࠤࡦ") + str(l1llll1l1_fb_) + l111l1_fb_ (u"ࠤ࠱ࡳ࡬࡭ࠢࡧ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠥࡷࡴࡻ࡮ࡥ࠴ࠥࡨ"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠦࡘࡵࡵ࡯ࡦࡶ࠳ࠧࡩ") + str(l1llll1l1_fb_) + l111l1_fb_ (u"ࠧ࠴ࡷࡢࡸࠥࡪ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠨࡳࡰࡷࡱࡨ࠷ࠨ࡫"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠢࡔࡱࡸࡲࡩࡹ࠯ࠣ࡬") + str(l1llll1l1_fb_) + l111l1_fb_ (u"ࠣ࠰ࡰࡴ࠸ࠨ࡭")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠤࡶࡳࡺࡴࡤ࠳ࠤ࡮"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠥࡑࡺࡹࡩࡤ࠱ࠥ࡯") + str(l1llll1l1_fb_) + l111l1_fb_ (u"ࠦ࠳ࡵࡧࡨࠤࡰ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠧࡹ࡯ࡶࡰࡧ࠶ࠧࡱ"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠨࡍࡶࡵ࡬ࡧ࠴ࠨࡲ") + str(l1llll1l1_fb_) + l111l1_fb_ (u"ࠢ࠯ࡹࡤࡺࠧࡳ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠣࡵࡲࡹࡳࡪ࠲ࠣࡴ"))
            return
        l1llllll1_fb_ = l111l1_fb_ (u"ࠤࡐࡹࡸ࡯ࡣ࠰ࠤࡵ") + str(l1llll1l1_fb_) + l111l1_fb_ (u"ࠥ࠲ࡲࡶ࠳ࠣࡶ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠦࡸࡵࡵ࡯ࡦ࠵ࠦࡷ"))
            return
    l1ll11ll_fb_.l1l1l11l_fb_.l1_fb_(l111l1_fb_ (u"ࠧࡹ࡯ࡶࡰࡧ࠶ࠧࡸ"), l111l1_fb_ (u"ࠨࡳࡧࡺࠥࡹ"), False)
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠢࡴࡱࡸࡲࡩ࠸ࠢࡺ"), parse=l111111l_fb_, l11l1l_fb_=l111l111_fb_) #l1llll1_fb_ - оператор воспроизведения звука
    def l11l11l_fb_(l):
        return (l.l1l1_fb_(), l.rest())
    def l1ll11l1_fb_(l11l111_fb_):
        global l1lllll1l_fb_, l1llll11_fb_
        l1llll1l_fb_, l1l1ll11_fb_ = l11l111_fb_
        if l1llll1l_fb_ == l111l1_fb_ (u"ࠣࡵࡷࡳࡵࠨࡻ"):
            l1lllll1l_fb_ = False
            l1llll11_fb_ = 0
            l1ll11ll_fb_.l1l1l11l_fb_.stop(l1111l11_fb_=l111l1_fb_ (u"ࠩࡰࡹࡸ࡯ࡣࠨࡼ"), l11l11_fb_=1.0)
            return
        try:
            l1lll11l_fb_ = l1ll11ll_fb_.eval(l1llll1l_fb_)
        except:
            l1lll11l_fb_ = l1llll1l_fb_
        if l1lll11l_fb_ == l1lllll1l_fb_:
            return
        try:
            l11l1l11_fb_ = int(l1l1ll11_fb_)
        except ValueError:
            l11l1l11_fb_ = 0
        if str(l1l1ll11_fb_) == l111l1_fb_ (u"ࠥࡰࡴࡽࠢࡽ"):
            l11l1l11_fb_ = 0
        if str(l1l1ll11_fb_) == l111l1_fb_ (u"ࠦ࡭࡯ࡧࡩࠤࡾ"):
            l11l1l11_fb_ = 10
        if l11l1l11_fb_ < l1llll11_fb_:
            return
        l1lllll1l_fb_ = l1lll11l_fb_
        l1llll11_fb_ = l11l1l11_fb_
        l1llllll1_fb_ = l111l1_fb_ (u"ࠧࡓࡵࡴ࡫ࡦ࠳ࠧࡿ") + str(l1lll11l_fb_) + l111l1_fb_ (u"ࠨ࠮ࡰࡩࡪࠦࢀ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            print l111l1_fb_ (u"ࠢࡱ࡮ࡤࡽࠦࠨࢁ") + str(l1llllll1_fb_)
            l1ll11ll_fb_.l1l1l11l_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠣ࡯ࡸࡷ࡮ࡩࠢࢂ"), l11ll11l_fb_=True, l11l11_fb_=1.0, l1l111_fb_=1.0)
        else:
            l1llllll1_fb_ = l111l1_fb_ (u"ࠤࡖࡳࡺࡴࡤࡴ࠱ࠥࢃ") + str(l1lll11l_fb_) + l111l1_fb_ (u"ࠥ࠲ࡴ࡭ࡧࠣࢄ")
            if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
                l1ll11ll_fb_.l1l1l11l_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠦࡲࡻࡳࡪࡥࠥࢅ"), l11ll11l_fb_=True, l11l11_fb_=1.0, l1l111_fb_=1.0)
        return
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠧࡳࡵࡴ࡫ࡦࠦࢆ"), parse=l11l11l_fb_, l11l1l_fb_=l1ll11l1_fb_) #l1l1l11l_fb_ - оператор воспроизведения музыки
    def l1l1l1l_fb_(l):
        return (l.rest())
    def l11_fb_(l11l111_fb_):
        l1ll11l1_fb_((l111l1_fb_ (u"ࠨࡳࡵࡱࡳࠦࢇ"), l111l1_fb_ (u"ࠢࠣ࢈")))
        l1l1ll1_fb_((l111l1_fb_ (u"ࠣࡤ࡯ࡥࡨࡱ࡟ࡴࡥࡵࡩࡪࡴࠢࢉ"), l111l1_fb_ (u"ࠤࡧࠦࢊ")))
        try:
            if float(l11l111_fb_) > 0:
                l1ll11ll_fb_.l1lll_fb_(float(l11l111_fb_))
        except:
            return
        return
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠥࡪࡦࡪࡥࡣ࡮ࡤࡧࡰࠨࢋ"), parse=l1l1l1l_fb_, l11l1l_fb_=l11_fb_) #l1l1lll1_fb_ - оператор затухания экрана
    def l11l1ll_fb_():
        global l11lllll_fb_, l1lllll1l_fb_, l1llll11_fb_
        l11lllll_fb_.insert(0, l1lllll1l_fb_)
        l1l11_fb_.insert(0, l1llll11_fb_)
        return
    def l111l1l_fb_():
        global l11lllll_fb_, l1lllll1l_fb_, l1llll11_fb_
        l1l111l_fb_ = False
        if len(l11lllll_fb_) > 0:
            l1l111l_fb_ = l11lllll_fb_.pop(0)
            l11ll1l_fb_ = l1l11_fb_.pop(0)
        if l1l111l_fb_ == False:
#            l1ll11ll_fb_.l1l1l11l_fb_.stop(l1111l11_fb_=l111l1_fb_ (u"ࠫࡲࡻࡳࡪࡥࠪࢌ"), l11l11_fb_=1.0)
            return
        if l1l111l_fb_ == l1lllll1l_fb_:
            return
        l1lllll1l_fb_ = l1l111l_fb_
        l1llll11_fb_ = l11ll1l_fb_
        l1llllll1_fb_ = l111l1_fb_ (u"ࠧࡓࡵࡴ࡫ࡦ࠳ࠧࢍ") + str(l1lllll1l_fb_) + l111l1_fb_ (u"ࠨ࠮ࡰࡩࡪࠦࢎ")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
            l1ll11ll_fb_.l1l1l11l_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠢ࡮ࡷࡶ࡭ࡨࠨ࢏"), l11ll11l_fb_=True, l11l11_fb_=1.0, l1l111_fb_=1.0)
        return
    def l1l11l_fb_():
        l11lllll_fb_ = []
        l1llll11_fb_ = 0
        return
    def l1ll1111_fb_(l11l111_fb_):
        global l11llll_fb_
        l1llll1l_fb_, l1l1ll11_fb_ = l11l111_fb_
        if l1llll1l_fb_ == l111l1_fb_ (u"ࠣࡵࡷࡳࡵࠨ࢐"):
            l11llll_fb_ = False
            l1ll11ll_fb_.l1l1l11l_fb_.stop(l1111l11_fb_=l111l1_fb_ (u"ࠩࡰࡹࡸ࡯ࡣ࠳ࠩ࢑"), l11l11_fb_=1.0)
            return
        try:
            l1lll11l_fb_ = l1ll11ll_fb_.eval(l1llll1l_fb_)
        except:
            l1lll11l_fb_ = l1llll1l_fb_
        if l1lll11l_fb_ == l11llll_fb_:
            return
        l11llll_fb_ = l1lll11l_fb_
        l1llllll1_fb_ = l111l1_fb_ (u"ࠥࡑࡺࡹࡩࡤ࠱ࠥ࢒") + str(l1lll11l_fb_) + l111l1_fb_ (u"ࠦ࠳ࡵࡧࡨࠤ࢓")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
#            print l111l1_fb_ (u"ࠧࡶ࡬ࡢࡻࠣࡱࡺࡹࡩࡤ࠼ࠣࠦ࢔") + l1llllll1_fb_
            l1ll11ll_fb_.l1l1l11l_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠨ࡭ࡶࡵ࡬ࡧ࠷ࠨ࢕"), l11ll11l_fb_=True, l11l11_fb_=1.0, l1l111_fb_=1.0)
        else:
            l1llllll1_fb_ = l111l1_fb_ (u"ࠢࡔࡱࡸࡲࡩࡹ࠯ࠣ࢖") + str(l1lll11l_fb_) + l111l1_fb_ (u"ࠣ࠰ࡲ࡫࡬ࠨࢗ")
            if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
                l1ll11ll_fb_.l1l1l11l_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠤࡰࡹࡸ࡯ࡣ࠳ࠤ࢘"), l11ll11l_fb_=True, l11l11_fb_=1.0, l1l111_fb_=1.0)
        return
    l1ll11ll_fb_.l1l1l11l_fb_.l1_fb_(l111l1_fb_ (u"ࠥࡱࡺࡹࡩࡤ࠴࢙ࠥ"), l111l1_fb_ (u"ࠦࡲࡻࡳࡪࡥ࢚ࠥ"), True)
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠧࡳࡵࡴ࡫ࡦ࠶࢛ࠧ"), parse=l11l11l_fb_, l11l1l_fb_=l1ll1111_fb_) #l1l1l11l_fb_ - оператор воспроизведения музыки
    def l111l_fb_(l11l111_fb_):
        global l1lll111l_fb_
        l1llll1l_fb_, l1l1ll11_fb_ = l11l111_fb_
        if l1llll1l_fb_ == l111l1_fb_ (u"ࠨࡳࡵࡱࡳࠦ࢜"):
            l1lll111l_fb_ = False
            l1ll11ll_fb_.l1l1l11l_fb_.stop(l1111l11_fb_=l111l1_fb_ (u"ࠧ࡮ࡷࡶ࡭ࡨ࠹ࠧ࢝"), l11l11_fb_=1.0)
            return
        try:
            l1lll11l_fb_ = l1ll11ll_fb_.eval(l1llll1l_fb_)
        except:
            l1lll11l_fb_ = l1llll1l_fb_
        if l1lll11l_fb_ == l1lll111l_fb_:
            return
        l1lll111l_fb_ = l1lll11l_fb_
        l1llllll1_fb_ = l111l1_fb_ (u"ࠣࡏࡸࡷ࡮ࡩ࠯ࠣ࢞") + str(l1lll11l_fb_) + l111l1_fb_ (u"ࠤ࠱ࡳ࡬࡭ࠢ࢟")
        if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
#            print l111l1_fb_ (u"ࠥࡴࡱࡧࡹࠡ࡯ࡸࡷ࡮ࡩ࠺ࠡࠤࢠ") + l1llllll1_fb_
            l1ll11ll_fb_.l1l1l11l_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠦࡲࡻࡳࡪࡥ࠶ࠦࢡ"), l11ll11l_fb_=True, l11l11_fb_=1.0, l1l111_fb_=1.0)
        else:
            l1llllll1_fb_ = l111l1_fb_ (u"࡙ࠧ࡯ࡶࡰࡧࡷ࠴ࠨࢢ") + str(l1lll11l_fb_) + l111l1_fb_ (u"ࠨ࠮ࡰࡩࡪࠦࢣ")
            if l1ll11ll_fb_.l1lll1lll_fb_(l1llllll1_fb_):
                l1ll11ll_fb_.l1l1l11l_fb_.l11111ll_fb_(l1llllll1_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠢ࡮ࡷࡶ࡭ࡨ࠹ࠢࢤ"), l11ll11l_fb_=True, l11l11_fb_=1.0, l1l111_fb_=1.0)
        return
    l1ll11ll_fb_.l1l1l11l_fb_.l1_fb_(l111l1_fb_ (u"ࠣ࡯ࡸࡷ࡮ࡩ࠳ࠣࢥ"), l111l1_fb_ (u"ࠤࡰࡹࡸ࡯ࡣࠣࢦ"), True)
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠥࡱࡺࡹࡩࡤ࠵ࠥࢧ"), parse=l11l11l_fb_, l11l1l_fb_=l111l_fb_) #l1l1l11l_fb_ - оператор воспроизведения музыки
    def l11lll_fb_(l):
        return l.l1l1_fb_()
    def l11ll_fb_(l1llll1l_fb_):
        try:
            l1l1l11_fb_ = l1ll_fb_(l1ll11ll_fb_.eval(l1llll1l_fb_))
        except:
            l1l1l11_fb_ = l1ll_fb_(l1llll1l_fb_)
        print(l1l1l11_fb_)
        l1lll11l1_fb_ = l11l1ll1_fb_(l11111ll_fb_=l1l1l11_fb_, l1111l11_fb_=l111l1_fb_ (u"ࠦࡲࡵࡶࡪࡧࠥࢨ")) #?????
    l1ll11ll_fb_.l1ll1ll_fb_(l111l1_fb_ (u"ࠧࡼࡩࡥࡧࡲࠦࢩ"), parse=l11lll_fb_, l11l1l_fb_=l11ll_fb_) #l1l1lll_fb_ - оператор воспроизведения видео
    def l11l111l_fb_(l11l11l1_fb_, l11l1l1l_fb_, l111ll1l_fb_):
        return [
                (l1ll11ll_fb_.l1ll1l1l_fb_, l111l1_fb_ (u"ࡻࠢࡤࡱ࡯ࡳࡷࡃࠣࡦ࠺ࡥ࠵࠸࠷ࠢࢪ")),
            ] + l111ll1l_fb_ + [
                (l1ll11ll_fb_.l1ll1l1l_fb_, l111l1_fb_ (u"ࡵࠣ࠱ࡦࡳࡱࡵࡲࠣࢫ")),
            ]