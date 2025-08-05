import caengine

def hat(bistate):
    return (# contraction
            ((bistate & 68718489600) == 13743697920) or
            ((bistate & 4278251775) == 855650355) or
            ((bistate & 15794175) == 3158835) or
            ((bistate & 68466774000) == 13693354800) or

            # contraction
            ((bistate & 68718489600) == 13743718400) or
            ((bistate & 4278251775) == 855650435) or
            ((bistate & 15794175) == 8401715) or
            ((bistate & 68466774000) == 15035532080) or

            # reflection
            ((bistate & 68718489600) == 13748940800) or
            ((bistate & 4278251775) == 2197827635) or
            ((bistate & 15794175) == 3179315) or
            ((bistate & 68466774000) == 13693354880) or

            # contraction
            ((bistate & 68718489600) == 13748961280) or
            ((bistate & 4278251775) == 2197827715) or
            ((bistate & 15794175) == 8422195) or
            ((bistate & 68466774000) == 15035532160) or

            # contraction
            ((bistate & 68718489600) == 13827584000) or
            ((bistate & 4278251775) == 855650360) or
            ((bistate & 15794175) == 3160115) or
            ((bistate & 68466774000) == 35168191280) or

            # reflection
            ((bistate & 68718489600) == 35218534400) or
            ((bistate & 4278251775) == 939536435) or
            ((bistate & 15794175) == 3158840) or
            ((bistate & 68466774000) == 13693356080) or

            # contraction
            ((bistate & 68718489600) == 13827604480) or
            ((bistate & 4278251775) == 855650440) or
            ((bistate & 15794175) == 8402995) or
            ((bistate & 68466774000) == 36510368560) or

            # reflection
            ((bistate & 68718489600) == 35223777280) or
            ((bistate & 4278251775) == 2281713715) or
            ((bistate & 15794175) == 3179320) or
            ((bistate & 68466774000) == 13693356160) or

            # contraction
            ((bistate & 68718489600) == 13832826880) or
            ((bistate & 4278251775) == 2197827640) or
            ((bistate & 15794175) == 3180595) or
            ((bistate & 68466774000) == 35168191360) or

            # reflection
            ((bistate & 68718489600) == 35218554880) or
            ((bistate & 4278251775) == 939536515) or
            ((bistate & 15794175) == 8401720) or
            ((bistate & 68466774000) == 15035533360) or

            # contraction
            ((bistate & 68718489600) == 13832847360) or
            ((bistate & 4278251775) == 2197827720) or
            ((bistate & 15794175) == 8423475) or
            ((bistate & 68466774000) == 36510368640) or

            # reflection
            ((bistate & 68718489600) == 35223797760) or
            ((bistate & 4278251775) == 2281713795) or
            ((bistate & 15794175) == 8422200) or
            ((bistate & 68466774000) == 15035533440) or

            # contraction
            ((bistate & 68718489600) == 15085875200) or
            ((bistate & 4278251775) == 855670835) or
            ((bistate & 15794175) == 3158915) or
            ((bistate & 68466774000) == 13698597680) or

            # contraction
            ((bistate & 68718489600) == 15085895680) or
            ((bistate & 4278251775) == 855670915) or
            ((bistate & 15794175) == 8401795) or
            ((bistate & 68466774000) == 15040774960) or

            # reflection
            ((bistate & 68718489600) == 15091118080) or
            ((bistate & 4278251775) == 2197848115) or
            ((bistate & 15794175) == 3179395) or
            ((bistate & 68466774000) == 13698597760) or

            # contraction0
            ((bistate & 68718489600) == 15091138560) or
            ((bistate & 4278251775) == 2197848195) or
            ((bistate & 15794175) == 8422275) or
            ((bistate & 68466774000) == 15040775040) or

            # contraction1
            ((bistate & 68718489600) == 15169761280) or
            ((bistate & 4278251775) == 855670840) or
            ((bistate & 15794175) == 3160195) or
            ((bistate & 68466774000) == 35173434160) or

            #1 reflection
            ((bistate & 68718489600) == 36560711680) or
            ((bistate & 4278251775) == 939556915) or
            ((bistate & 15794175) == 3158920) or
            ((bistate & 68466774000) == 13698598960) or

            # contraction2
            ((bistate & 68718489600) == 15169781760) or
            ((bistate & 4278251775) == 855670920) or
            ((bistate & 15794175) == 8403075) or
            ((bistate & 68466774000) == 36515611440) or

            #2 reflection
            ((bistate & 68718489600) == 36565954560) or
            ((bistate & 4278251775) == 2281734195) or
            ((bistate & 15794175) == 3179400) or
            ((bistate & 68466774000) == 13698599040) or

            # contraction3
            ((bistate & 68718489600) == 15175004160) or
            ((bistate & 4278251775) == 2197848120) or
            ((bistate & 15794175) == 3180675) or
            ((bistate & 68466774000) == 35173434240) or

            #3 reflection
            ((bistate & 68718489600) == 36560732160) or
            ((bistate & 4278251775) == 939556995) or
            ((bistate & 15794175) == 8401800) or
            ((bistate & 68466774000) == 15040776240) or

            # contraction4
            ((bistate & 68718489600) == 15175024640) or
            ((bistate & 4278251775) == 2197848200) or
            ((bistate & 15794175) == 8423555) or
            ((bistate & 68466774000) == 36515611520) or

            #4 reflection
            ((bistate & 68718489600) == 36565975040) or
            ((bistate & 4278251775) == 2281734275) or
            ((bistate & 15794175) == 8422280) or
            ((bistate & 68466774000) == 15040776320) or

            # contraction5
            ((bistate & 68718489600) == 35302420480) or
            ((bistate & 4278251775) == 939536440) or
            ((bistate & 15794175) == 3160120) or
            ((bistate & 68466774000) == 35168192560) or

            # contraction6
            ((bistate & 68718489600) == 35302440960) or
            ((bistate & 4278251775) == 939536520) or
            ((bistate & 15794175) == 8403000) or
            ((bistate & 68466774000) == 36510369840) or

            #6 reflection
            ((bistate & 68718489600) == 35307663360) or
            ((bistate & 4278251775) == 2281713720) or
            ((bistate & 15794175) == 3180600) or
            ((bistate & 68466774000) == 35168192640) or

            # contraction7
            ((bistate & 68718489600) == 35307683840) or
            ((bistate & 4278251775) == 2281713800) or
            ((bistate & 15794175) == 8423480) or
            ((bistate & 68466774000) == 36510369920) or

            # contraction8
            ((bistate & 68718489600) == 36644597760) or
            ((bistate & 4278251775) == 939556920) or
            ((bistate & 15794175) == 3160200) or
            ((bistate & 68466774000) == 35173435440) or

            # contraction9
            ((bistate & 68718489600) == 36644618240) or
            ((bistate & 4278251775) == 939557000) or
            ((bistate & 15794175) == 8403080) or
            ((bistate & 68466774000) == 36515612720) or

            #9 reflection
            ((bistate & 68718489600) == 36649840640) or
            ((bistate & 4278251775) == 2281734200) or
            ((bistate & 15794175) == 3180680) or
            ((bistate & 68466774000) == 35173435520) or

            # contraction0
            ((bistate & 68718489600) == 36649861120) or
            ((bistate & 4278251775) == 2281734280) or
            ((bistate & 15794175) == 8423560) or
            ((bistate & 68466774000) == 36515612800)
    )

def corner1(bistate):
    return (# contraction1
            ((bistate & 68702760975) == 13740552195) or
            ((bistate & 251723775) == 50344755) or
            ((bistate & 64440242175) == 12888048435) or
            ((bistate & 68718432000) == 13743686400) or

            # contraction2
            ((bistate & 68702760975) == 13740552200) or
            ((bistate & 251723775) == 50346035) or
            ((bistate & 64440242175) == 34362884915) or
            ((bistate & 68718432000) == 13827572480) or

            #2 reflection
            ((bistate & 68718432000) == 13743687680) or
            ((bistate & 68702760975) == 35215388675) or
            ((bistate & 251723775) == 134230835) or
            ((bistate & 64440242175) == 12888048440) or

            # contraction3
            ((bistate & 68702760975) == 13740572675) or
            ((bistate & 251723775) == 50344835) or
            ((bistate & 64440242175) == 12893291315) or
            ((bistate & 68718432000) == 15085863680) or

            #3 reflection
            ((bistate & 68718432000) == 13748929280) or
            ((bistate & 68702760975) == 15082729475) or
            ((bistate & 251723775) == 50365235) or
            ((bistate & 64440242175) == 12888048515) or

            # contraction4
            ((bistate & 68702760975) == 13740572680) or
            ((bistate & 251723775) == 50346115) or
            ((bistate & 64440242175) == 34368127795) or
            ((bistate & 68718432000) == 15169749760) or

            #4 reflection
            ((bistate & 68718432000) == 13748930560) or
            ((bistate & 68702760975) == 36557565955) or
            ((bistate & 251723775) == 134251315) or
            ((bistate & 64440242175) == 12888048520) or

            # contraction5
            ((bistate & 68702760975) == 13824438275) or
            ((bistate & 251723775) == 50344760) or
            ((bistate & 64440242175) == 12888049715) or
            ((bistate & 68718432000) == 35218522880) or

            # contraction6
            ((bistate & 68702760975) == 13824438280) or
            ((bistate & 251723775) == 50346040) or
            ((bistate & 64440242175) == 34362886195) or
            ((bistate & 68718432000) == 35302408960) or

            #6 reflection
            ((bistate & 68718432000) == 35218524160) or
            ((bistate & 68702760975) == 35299274755) or
            ((bistate & 251723775) == 134230840) or
            ((bistate & 64440242175) == 12888049720) or

            # contraction7
            ((bistate & 68702760975) == 13824458755) or
            ((bistate & 251723775) == 50344840) or
            ((bistate & 64440242175) == 12893292595) or
            ((bistate & 68718432000) == 36560700160) or

            #7 reflection
            ((bistate & 68718432000) == 35223765760) or
            ((bistate & 68702760975) == 15166615555) or
            ((bistate & 251723775) == 50365240) or
            ((bistate & 64440242175) == 12888049795) or

            # contraction8
            ((bistate & 68702760975) == 13824458760) or
            ((bistate & 251723775) == 50346120) or
            ((bistate & 64440242175) == 34368129075) or
            ((bistate & 68718432000) == 36644586240) or

            #8 reflection
            ((bistate & 68718432000) == 35223767040) or
            ((bistate & 68702760975) == 36641452035) or
            ((bistate & 251723775) == 134251320) or
            ((bistate & 64440242175) == 12888049800) or

            # contraction9
            ((bistate & 68702760975) == 15082729480) or
            ((bistate & 251723775) == 50366515) or
            ((bistate & 64440242175) == 34362884995) or
            ((bistate & 68718432000) == 13832815360) or

            #9 reflection
            ((bistate & 68718432000) == 15085864960) or
            ((bistate & 68702760975) == 35215409155) or
            ((bistate & 251723775) == 134230915) or
            ((bistate & 64440242175) == 12893291320) or

            # contraction0
            ((bistate & 68702760975) == 15082749955) or
            ((bistate & 251723775) == 50365315) or
            ((bistate & 64440242175) == 12893291395) or
            ((bistate & 68718432000) == 15091106560) or

            # contraction1
            ((bistate & 68702760975) == 15082749960) or
            ((bistate & 251723775) == 50366595) or
            ((bistate & 64440242175) == 34368127875) or
            ((bistate & 68718432000) == 15174992640) or

            #1 reflection
            ((bistate & 68718432000) == 15091107840) or
            ((bistate & 68702760975) == 36557586435) or
            ((bistate & 251723775) == 134251395) or
            ((bistate & 64440242175) == 12893291400) or

            # contraction2
            ((bistate & 68702760975) == 15166615560) or
            ((bistate & 251723775) == 50366520) or
            ((bistate & 64440242175) == 34362886275) or
            ((bistate & 68718432000) == 35307651840) or

            #2 reflection
            ((bistate & 68718432000) == 36560701440) or
            ((bistate & 68702760975) == 35299295235) or
            ((bistate & 251723775) == 134230920) or
            ((bistate & 64440242175) == 12893292600) or

            # contraction3
            ((bistate & 68702760975) == 15166636035) or
            ((bistate & 251723775) == 50365320) or
            ((bistate & 64440242175) == 12893292675) or
            ((bistate & 68718432000) == 36565943040) or

            # contraction4
            ((bistate & 68702760975) == 15166636040) or
            ((bistate & 251723775) == 50366600) or
            ((bistate & 64440242175) == 34368129155) or
            ((bistate & 68718432000) == 36649829120) or

            #4 reflection
            ((bistate & 68718432000) == 36565944320) or
            ((bistate & 68702760975) == 36641472515) or
            ((bistate & 251723775) == 134251400) or
            ((bistate & 64440242175) == 12893292680) or

            # contraction5
            ((bistate & 68702760975) == 35215388680) or
            ((bistate & 251723775) == 134232115) or
            ((bistate & 64440242175) == 34362884920) or
            ((bistate & 68718432000) == 13827573760) or

            # contraction6
            ((bistate & 68702760975) == 35215409160) or
            ((bistate & 251723775) == 134232195) or
            ((bistate & 64440242175) == 34368127800) or
            ((bistate & 68718432000) == 15169751040) or

            #6 reflection
            ((bistate & 68718432000) == 13832816640) or
            ((bistate & 68702760975) == 36557565960) or
            ((bistate & 251723775) == 134252595) or
            ((bistate & 64440242175) == 34362885000) or

            # contraction7
            ((bistate & 68702760975) == 35299274760) or
            ((bistate & 251723775) == 134232120) or
            ((bistate & 64440242175) == 34362886200) or
            ((bistate & 68718432000) == 35302410240) or

            # contraction8
            ((bistate & 68702760975) == 35299295240) or
            ((bistate & 251723775) == 134232200) or
            ((bistate & 64440242175) == 34368129080) or
            ((bistate & 68718432000) == 36644587520) or

            #8 reflection
            ((bistate & 68718432000) == 35307653120) or
            ((bistate & 68702760975) == 36641452040) or
            ((bistate & 251723775) == 134252600) or
            ((bistate & 64440242175) == 34362886280) or

            # contraction9
            ((bistate & 68702760975) == 36557586440) or
            ((bistate & 251723775) == 134252675) or
            ((bistate & 64440242175) == 34368127880) or
            ((bistate & 68718432000) == 15174993920) or

            # contraction0
            ((bistate & 68702760975) == 36641472520) or
            ((bistate & 251723775) == 134252680) or
            ((bistate & 64440242175) == 34368129160) or
            ((bistate & 68718432000) == 36649830400)
            )

def corner2(bistate, state):
    return (
        # contraction
        (((bistate & 68702760975) == 13740552195) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50344755) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12888048435) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 13743686400) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # contraction
        (((bistate & 68702760975) == 13740552200) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50346035) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34362884915) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 13827572480) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # reflection
        (((bistate & 68718432000) == 13743687680) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 35215388675) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134230835) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12888048440) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction
        (((bistate & 68702760975) == 13740572675) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50344835) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12893291315) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 15085863680) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # reflection
        (((bistate & 68718432000) == 13748929280) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 15082729475) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50365235) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12888048515) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction
        (((bistate & 68702760975) == 13740572680) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50346115) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34368127795) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 15169749760) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # reflection
        (((bistate & 68718432000) == 13748930560) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 36557565955) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134251315) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12888048520) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction
        (((bistate & 68702760975) == 13824438275) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50344760) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12888049715) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 35218522880) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # contraction
        (((bistate & 68702760975) == 13824438280) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50346040) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34362886195) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 35302408960) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # reflection
        (((bistate & 68718432000) == 35218524160) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 35299274755) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134230840) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12888049720) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction
        (((bistate & 68702760975) == 13824458755) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50344840) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12893292595) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 36560700160) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # reflection
        (((bistate & 68718432000) == 35223765760) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 15166615555) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50365240) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12888049795) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction
        (((bistate & 68702760975) == 13824458760) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50346120) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34368129075) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 36644586240) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # reflection
        (((bistate & 68718432000) == 35223767040) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 36641452035) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134251320) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12888049800) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction0
        (((bistate & 68702760975) == 15082729480) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50366515) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34362884995) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 13832815360) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        #0 reflection
        (((bistate & 68718432000) == 15085864960) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 35215409155) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134230915) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12893291320) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction1
        (((bistate & 68702760975) == 15082749955) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50365315) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12893291395) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 15091106560) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # contraction2
        (((bistate & 68702760975) == 15082749960) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50366595) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34368127875) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 15174992640) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        #2 reflection
        (((bistate & 68718432000) == 15091107840) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 36557586435) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134251395) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12893291400) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction3
        (((bistate & 68702760975) == 15166615560) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50366520) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34362886275) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 35307651840) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        #3 reflection
        (((bistate & 68718432000) == 36560701440) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 35299295235) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134230920) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12893292600) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction4
        (((bistate & 68702760975) == 15166636035) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50365320) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12893292675) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 36565943040) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # contraction5
        (((bistate & 68702760975) == 15166636040) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 50366600) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34368129155) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 36649829120) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        #5 reflection
        (((bistate & 68718432000) == 36565944320) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 36641472515) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134251400) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 12893292680) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction6
        (((bistate & 68702760975) == 35215388680) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134232115) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34362884920) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 13827573760) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # contraction7
        (((bistate & 68702760975) == 35215409160) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134232195) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34368127800) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 15169751040) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        #7 reflection
        (((bistate & 68718432000) == 13832816640) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 36557565960) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134252595) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34362885000) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction8
        (((bistate & 68702760975) == 35299274760) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134232120) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34362886200) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 35302410240) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # contraction9
        (((bistate & 68702760975) == 35299295240) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134232200) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34368129080) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 36644587520) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        #9 reflection
        (((bistate & 68718432000) == 35307653120) and caengine.areLive(cur_state=state, cells=[6,8,9])) or
        (((bistate & 68702760975) == 36641452040) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134252600) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34362886280) and caengine.areLive(cur_state=state, cells=[2,3,6])) or

        # contraction0
        (((bistate & 68702760975) == 36557586440) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134252675) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34368127880) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 15174993920) and caengine.areLive(cur_state=state, cells=[6,8,9])) or

        # contraction1
        (((bistate & 68702760975) == 36641472520) and caengine.areLive(cur_state=state, cells=[4,7,8])) or
        (((bistate & 251723775) == 134252680) and caengine.areLive(cur_state=state, cells=[1,2,4])) or
        (((bistate & 64440242175) == 34368129160) and caengine.areLive(cur_state=state, cells=[2,3,6])) or
        (((bistate & 68718432000) == 36649830400) and caengine.areLive(cur_state=state, cells=[6,8,9])))

def antiloop1(bistate): #Dealing with loops
    return (# contraction1
            ((bistate & 64425492480) == 60130328576) or
            ((bistate & 252641280) == 252510208) or
            ((bistate & 983055) == 917516) or
            ((bistate & 986880) == 986368) or
            
            #1 reflection
            ((bistate & 252641280) == 235667456) or
            ((bistate & 983055) == 851983) or
            ((bistate & 986880) == 920576) or
            ((bistate & 64425492480) == 55835557888) or
            
            # contraction2
            ((bistate & 4027514880) == 3758882816) or
            ((bistate & 1044480) == 913408) or
            ((bistate & 983280) == 917696) or
            ((bistate & 16711680) == 14614528) or

            # contraction3
            ((bistate & 252641280) == 235667456) or
            ((bistate & 983055) == 851983) or
            ((bistate & 986880) == 920576) or
            ((bistate & 64425492480) == 55835557888) or

            #3 reflection
            ((bistate & 64425492480) == 60130328576) or
            ((bistate & 252641280) == 252510208) or
            ((bistate & 983055) == 917516) or
            ((bistate & 986880) == 986368) or

            # contraction4
            ((bistate & 64425492480) == 55835361280) or
            ((bistate & 252641280) == 235732992) or
            ((bistate & 983055) == 917519) or
            ((bistate & 986880) == 986112) or

            #4 reflection
            ((bistate & 252641280) == 252444672) or
            ((bistate & 983055) == 851980) or
            ((bistate & 986880) == 920832) or
            ((bistate & 64425492480) == 60130525184)
            )

def antiloop2(bistate): # Alternate antiloop, only tracks direct opposition
    return (# contraction1
            ((bistate & 64425492480) == 60130328576) or
            ((bistate & 252641280) == 252510208) or
            ((bistate & 983055) == 917516) or
            ((bistate & 986880) == 986368) or
            
            #1 reflection
            ((bistate & 252641280) == 235667456) or
            ((bistate & 983055) == 851983) or
            ((bistate & 986880) == 920576) or
            ((bistate & 64425492480) == 55835557888) or
            
            # contraction2
            ((bistate & 4027514880) == 3758882816) or
            ((bistate & 1044480) == 913408) or
            ((bistate & 983280) == 917696) or
            ((bistate & 16711680) == 14614528) or

            # contraction3
            ((bistate & 252641280) == 235667456) or
            ((bistate & 983055) == 851983) or
            ((bistate & 986880) == 920576) or
            ((bistate & 64425492480) == 55835557888) or

            #3 reflection
            ((bistate & 64425492480) == 60130328576) or
            ((bistate & 252641280) == 252510208) or
            ((bistate & 983055) == 917516) or
            ((bistate & 986880) == 986368)
    )

def knight1(bistate, state): #Contracting open spaces from the edges
    return( # contraction5
            (((bistate & 68466773760) == 15035532032) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
            (((bistate & 68702760960) == 13740572672) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
            (((bistate & 251719935) == 50344067) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
            (((bistate & 15732735) == 8389427) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

            #5 reflection
            (((bistate & 4278251535) == 2197827587) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
            (((bistate & 65535) == 33587) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
            (((bistate & 64440242160) == 12888048512) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
            (((bistate & 68718428160) == 13748928512) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

            # contraction6
            (((bistate & 68466773760) == 15035533312) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
            (((bistate & 68702760960) == 35215409152) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
            (((bistate & 251719935) == 134230147) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
            (((bistate & 15732735) == 8389432) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

            #6 reflection
            (((bistate & 4278251535) == 2197827592) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
            (((bistate & 65535) == 34867) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
            (((bistate & 64440242160) == 34362884992) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
            (((bistate & 68718428160) == 13832814592) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

            # contraction7
            (((bistate & 68466773760) == 15040774912) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
            (((bistate & 68702760960) == 15082749952) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
            (((bistate & 251719935) == 50364547) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
            (((bistate & 15732735) == 8389507) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

            #7 reflection
            (((bistate & 4278251535) == 2197848067) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
            (((bistate & 65535) == 33667) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
            (((bistate & 64440242160) == 12893291392) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
            (((bistate & 68718428160) == 15091105792) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

            # contraction8
            (((bistate & 68466773760) == 15040776192) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
            (((bistate & 68702760960) == 36557586432) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
            (((bistate & 251719935) == 134250627) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
            (((bistate & 15732735) == 8389512) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

            #8 reflection
            (((bistate & 4278251535) == 2197848072) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
            (((bistate & 65535) == 34947) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
            (((bistate & 64440242160) == 34368127872) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
            (((bistate & 68718428160) == 15174991872) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

            # contraction9
            (((bistate & 68466773760) == 36510368512) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
            (((bistate & 68702760960) == 13824458752) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
            (((bistate & 251719935) == 50344072) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
            (((bistate & 15732735) == 8390707) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

            #9 reflection
            (((bistate & 4278251535) == 2281713667) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
            (((bistate & 65535) == 33592) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
            (((bistate & 64440242160) == 12888049792) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
            (((bistate & 68718428160) == 35223764992) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

            # contraction0
            (((bistate & 68466773760) == 36510369792) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
            (((bistate & 68702760960) == 35299295232) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
            (((bistate & 251719935) == 134230152) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
            (((bistate & 15732735) == 8390712) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

            #0 reflection
            (((bistate & 4278251535) == 2281713672) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
            (((bistate & 65535) == 34872) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
            (((bistate & 64440242160) == 34362886272) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
            (((bistate & 68718428160) == 35307651072) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

            # contraction1
            (((bistate & 68466773760) == 36515611392) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
            (((bistate & 68702760960) == 15166636032) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
            (((bistate & 251719935) == 50364552) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
            (((bistate & 15732735) == 8390787) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

            #1 reflection
            (((bistate & 4278251535) == 2281734147) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
            (((bistate & 65535) == 33672) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
            (((bistate & 64440242160) == 12893292672) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
            (((bistate & 68718428160) == 36565942272) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

            # contraction2
            (((bistate & 68466773760) == 36515612672) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
            (((bistate & 68702760960) == 36641472512) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
            (((bistate & 251719935) == 134250632) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
            (((bistate & 15732735) == 8390792) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

            #2 reflection
            (((bistate & 4278251535) == 2281734152) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
            (((bistate & 65535) == 34952) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
            (((bistate & 64440242160) == 34368129152) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
            (((bistate & 68718428160) == 36649828352) and caengine.areLive(cur_state=state, cells=[6,7,8,9]))
            )

def knight2(bistate, state): # Alternate Knight's Move
    return (
        # contraction5
        (((bistate & 68466773760) == 13693354752) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 13740552192) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 50343987) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 3146547) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #5 reflection
        (((bistate & 4278251535) == 855650307) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 13107) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 12888048432) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 13743685632) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction6
        (((bistate & 68466773760) == 13693356032) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 35215388672) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 134230067) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 3146552) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #6 reflection
        (((bistate & 4278251535) == 855650312) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 14387) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 34362884912) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 13827571712) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction7
        (((bistate & 68466773760) == 13698597632) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 15082729472) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 50364467) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 3146627) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #7 reflection
        (((bistate & 4278251535) == 855670787) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 13187) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 12893291312) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 15085862912) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction8
        (((bistate & 68466773760) == 13698598912) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 36557565952) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 134250547) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 3146632) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #8 reflection
        (((bistate & 4278251535) == 855670792) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 14467) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 34368127792) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 15169748992) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction9
        (((bistate & 68466773760) == 15035532032) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 13740572672) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 50344067) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 8389427) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #9 reflection
        (((bistate & 4278251535) == 2197827587) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 33587) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 12888048512) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 13748928512) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction0
        (((bistate & 68466773760) == 15035533312) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 35215409152) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 134230147) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 8389432) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #0 reflection
        (((bistate & 4278251535) == 2197827592) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 34867) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 34362884992) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 13832814592) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction1
        (((bistate & 68466773760) == 15040774912) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 15082749952) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 50364547) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 8389507) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #1 reflection
        (((bistate & 4278251535) == 2197848067) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 33667) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 12893291392) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 15091105792) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction2
        (((bistate & 68466773760) == 15040776192) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 36557586432) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 134250627) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 8389512) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #2 reflection
        (((bistate & 4278251535) == 2197848072) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 34947) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 34368127872) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 15174991872) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction3
        (((bistate & 68466773760) == 35168191232) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 13824438272) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 50343992) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 3147827) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #3 reflection
        (((bistate & 4278251535) == 939536387) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 13112) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 12888049712) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 35218522112) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction4
        (((bistate & 68466773760) == 35168192512) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 35299274752) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 134230072) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 3147832) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #4 reflection
        (((bistate & 4278251535) == 939536392) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 14392) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 34362886192) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 35302408192) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction5
        (((bistate & 68466773760) == 35173434112) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 15166615552) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 50364472) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 3147907) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #5 reflection
        (((bistate & 4278251535) == 939556867) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 13192) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 12893292592) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 36560699392) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction6
        (((bistate & 68466773760) == 35173435392) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 36641452032) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 134250552) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 3147912) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #6 reflection
        (((bistate & 4278251535) == 939556872) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 14472) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 34368129072) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 36644585472) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction7
        (((bistate & 68466773760) == 36510368512) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 13824458752) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 50344072) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 8390707) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #7 reflection
        (((bistate & 4278251535) == 2281713667) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 33592) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 12888049792) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 35223764992) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction8
        (((bistate & 68466773760) == 36510369792) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 35299295232) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 134230152) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 8390712) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #8 reflection
        (((bistate & 4278251535) == 2281713672) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 34872) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 34362886272) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 35307651072) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction9
        (((bistate & 68466773760) == 36515611392) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 15166636032) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 50364552) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 8390787) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #9 reflection
        (((bistate & 4278251535) == 2281734147) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 33672) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 12893292672) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 36565942272) and caengine.areLive(cur_state=state, cells=[6,7,8,9])) or

        # contraction0
        (((bistate & 68466773760) == 36515612672) and caengine.areLive(cur_state=state, cells=[3,6,8,9])) or
        (((bistate & 68702760960) == 36641472512) and caengine.areLive(cur_state=state, cells=[4,7,8,9])) or
        (((bistate & 251719935) == 134250632) and caengine.areLive(cur_state=state, cells=[1,2,4,7])) or
        (((bistate & 15732735) == 8390792) and caengine.areLive(cur_state=state, cells=[1,2,3,6])) or

        #0 reflection
        (((bistate & 4278251535) == 2281734152) and caengine.areLive(cur_state=state, cells=[1,3,6,7])) or
        (((bistate & 65535) == 34952) and caengine.areLive(cur_state=state, cells=[1,2,3,4])) or
        (((bistate & 64440242160) == 34368129152) and caengine.areLive(cur_state=state, cells=[2,3,6,9])) or
        (((bistate & 68718428160) == 36649828352) and caengine.areLive(cur_state=state, cells=[6,7,8,9]))
    )