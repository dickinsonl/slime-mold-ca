def check1(bistate):
    return (# contraction rule 1 from spreadsheet
            ((bistate & 68718489600) == 13743697920) or
            ((bistate & 4278251775) == 855650355) or
            ((bistate & 15794175) == 3158835) or
            ((bistate & 68466774000) == 13693354800) or

            # contraction rule 2
            ((bistate & 68718489600) == 13743685632) or
            ((bistate & 4278251775) == 855650307) or
            ((bistate & 15794175) == 13107) or
            ((bistate & 68466774000) == 12888048432) or

            # rule 2 reflections
            ((bistate & 68718489600) == 13740552192) or
            ((bistate & 4278251775) == 50343987) or
            ((bistate & 15794175) == 3146547) or
            ((bistate & 68466774000) == 13693354752) or

            # contraction rule 3
            ((bistate & 68718489600) == 13740539904) or
            ((bistate & 4278251775) == 50343939) or
            ((bistate & 15794175) == 819) or
            ((bistate & 68466774000) == 12888048384) or

            # contraction rule 4
            ((bistate & 68718489600) == 13693366272) or
            ((bistate & 4278251775) == 855650352) or
            ((bistate & 15794175) == 3158067) or
            ((bistate & 68466774000) == 808452912) or

            # rule 4 reflections
            ((bistate & 68718489600) == 858796032) or
            ((bistate & 4278251775) == 805318707) or
            ((bistate & 15794175) == 3158832) or
            ((bistate & 68466774000) == 13693354032) or

            # contraction rule 5
            ((bistate & 68718489600) == 13693353984) or
            ((bistate & 4278251775) == 855650304) or
            ((bistate & 15794175) == 12339) or
            ((bistate & 68466774000) == 3146544) or

            # rule 5 reflections
            ((bistate & 68718489600) == 855650304) or
            ((bistate & 4278251775) == 12339) or
            ((bistate & 15794175) == 3146544) or
            ((bistate & 68466774000) == 13693353984) or

            # contraction rule 6
            ((bistate & 68718489600) == 13690220544) or
            ((bistate & 4278251775) == 50343984) or
            ((bistate & 15794175) == 3145779) or
            ((bistate & 68466774000) == 808452864) or

            # rule 6 reflections
            ((bistate & 68718489600) == 858783744) or
            ((bistate & 4278251775) == 805318659) or
            ((bistate & 15794175) == 13104) or
            ((bistate & 68466774000) == 12888047664) or

            # contraction rule 7
            ((bistate & 68718489600) == 13690208256) or
            ((bistate & 4278251775) == 50343936) or
            ((bistate & 15794175) == 51) or
            ((bistate & 68466774000) == 3146496) or

            # rule 7 reflections
            ((bistate & 68718489600) == 855638016) or
            ((bistate & 4278251775) == 12291) or
            ((bistate & 15794175) == 816) or
            ((bistate & 68466774000) == 12888047616) or

            # contraction rule 8
            ((bistate & 68718489600) == 12938391552) or
            ((bistate & 4278251775) == 855638067) or
            ((bistate & 15794175) == 3158787) or
            ((bistate & 68466774000) == 13690209072) or

            # contraction rule 9
            ((bistate & 68718489600) == 12938379264) or
            ((bistate & 4278251775) == 855638019) or
            ((bistate & 15794175) == 13059) or
            ((bistate & 68466774000) == 12884902704) or

            # rule 9 reflections
            ((bistate & 68718489600) == 12935245824) or
            ((bistate & 4278251775) == 50331699) or
            ((bistate & 15794175) == 3146499) or
            ((bistate & 68466774000) == 13690209024) or

            # contraction rule 10
            ((bistate & 68718489600) == 12935233536) or
            ((bistate & 4278251775) == 50331651) or
            ((bistate & 15794175) == 771) or
            ((bistate & 68466774000) == 12884902656) or

            # contraction rule 11
            ((bistate & 68718489600) == 12888059904) or
            ((bistate & 4278251775) == 855638064) or
            ((bistate & 15794175) == 3158019) or
            ((bistate & 68466774000) == 805307184) or

            # rule 11 reflections
            ((bistate & 68718489600) == 53489664) or
            ((bistate & 4278251775) == 805306419) or
            ((bistate & 15794175) == 3158784) or
            ((bistate & 68466774000) == 13690208304) or

            # contraction rule 12
            ((bistate & 68718489600) == 12888047616) or
            ((bistate & 4278251775) == 855638016) or
            ((bistate & 15794175) == 12291) or
            ((bistate & 68466774000) == 816) or

            # rule 12 reflections
            ((bistate & 68718489600) == 50343936) or
            ((bistate & 4278251775) == 51) or
            ((bistate & 15794175) == 3146496) or
            ((bistate & 68466774000) == 13690208256) or

            # contraction rule 13
            ((bistate & 68718489600) == 12884914176) or
            ((bistate & 4278251775) == 50331696) or
            ((bistate & 15794175) == 3145731) or
            ((bistate & 68466774000) == 805307136) or

            # rule 13 reflections
            ((bistate & 68718489600) == 53477376) or
            ((bistate & 4278251775) == 805306371) or
            ((bistate & 15794175) == 13056) or
            ((bistate & 68466774000) == 12884901936) or

            # contraction rule 14
            ((bistate & 68718489600) == 12884901888) or
            ((bistate & 4278251775) == 50331648) or
            ((bistate & 15794175) == 3) or
            ((bistate & 68466774000) == 768) or

            # rule 14 reflections
            ((bistate & 68718489600) == 50331648) or
            ((bistate & 4278251775) == 3) or
            ((bistate & 15794175) == 768) or
            ((bistate & 68466774000) == 12884901888) or

            # contraction rule 15
            ((bistate & 68718489600) == 808464384) or
            ((bistate & 4278251775) == 805318704) or
            ((bistate & 15794175) == 3158064) or
            ((bistate & 68466774000) == 808452144) or

            # contraction rule 16
            ((bistate & 68718489600) == 808452096) or
            ((bistate & 4278251775) == 805318656) or
            ((bistate & 15794175) == 12336) or
            ((bistate & 68466774000) == 3145776) or

            # rule 16 reflections
            ((bistate & 68718489600) == 805318656) or
            ((bistate & 4278251775) == 12336) or
            ((bistate & 15794175) == 3145776) or
            ((bistate & 68466774000) == 808452096) or

            # contraction rule 17
            ((bistate & 68718489600) == 805306368) or
            ((bistate & 4278251775) == 12288) or
            ((bistate & 15794175) == 48) or
            ((bistate & 68466774000) == 3145728) or

            # contraction rule 18
            ((bistate & 68718489600) == 3158016) or
            ((bistate & 4278251775) == 805306416) or
            ((bistate & 15794175) == 3158016) or
            ((bistate & 68466774000) == 805306416) or

            # contraction rule 19
            ((bistate & 68718489600) == 3145728) or
            ((bistate & 4278251775) == 805306368) or
            ((bistate & 15794175) == 12288) or
            ((bistate & 68466774000) == 48) or

            # rule 19 reflections
            ((bistate & 68718489600) == 12288) or
            ((bistate & 4278251775) == 48) or
            ((bistate & 15794175) == 3145728) or
            ((bistate & 68466774000) == 805306368) or

            # contraction rule 20
            ((bistate & 68718489600) == 0) or
            ((bistate & 4278251775) == 0) or
            ((bistate & 15794175) == 0) or
            ((bistate & 68466774000) == 0)
            )

def check2(bistate):
    return (# contraction rule 21
            ((bistate & 68702760975) == 13740552195) or
            ((bistate & 251723775) == 50344755) or
            ((bistate & 64440242175) == 12888048435) or
            ((bistate & 68718432000) == 13743686400) or

            # contraction rule 22
            ((bistate & 68702760975) == 13740552192) or
            ((bistate & 251723775) == 50343987) or
            ((bistate & 64440242175) == 3146547) or
            ((bistate & 68718432000) == 13693354752) or

            # rule 22 reflections
            ((bistate & 68718432000) == 13743685632) or
            ((bistate & 68702760975) == 855650307) or
            ((bistate & 251723775) == 13107) or
            ((bistate & 64440242175) == 12888048432) or

            # contraction rule 23
            ((bistate & 68702760975) == 13740539907) or
            ((bistate & 251723775) == 50344707) or
            ((bistate & 64440242175) == 12884902707) or
            ((bistate & 68718432000) == 12938380032) or

            # rule 23 reflections
            ((bistate & 68718432000) == 13740540672) or
            ((bistate & 68702760975) == 12935245827) or
            ((bistate & 251723775) == 50332467) or
            ((bistate & 64440242175) == 12888048387) or

            # contraction rule 24
            ((bistate & 68702760975) == 13740539904) or
            ((bistate & 251723775) == 50343939) or
            ((bistate & 64440242175) == 819) or
            ((bistate & 68718432000) == 12888048384) or

            # rule 24 reflections
            ((bistate & 68718432000) == 13740539904) or
            ((bistate & 68702760975) == 50343939) or
            ((bistate & 251723775) == 819) or
            ((bistate & 64440242175) == 12888048384) or

            # contraction rule 25
            ((bistate & 68702760975) == 13690220547) or
            ((bistate & 251723775) == 50344752) or
            ((bistate & 64440242175) == 12888047667) or
            ((bistate & 68718432000) == 858784512) or

            # contraction rule 26
            ((bistate & 68702760975) == 13690220544) or
            ((bistate & 251723775) == 50343984) or
            ((bistate & 64440242175) == 3145779) or
            ((bistate & 68718432000) == 808452864) or

            # rule 26 reflections
            ((bistate & 68718432000) == 858783744) or
            ((bistate & 68702760975) == 805318659) or
            ((bistate & 251723775) == 13104) or
            ((bistate & 64440242175) == 12888047664) or

            # contraction rule 27
            ((bistate & 68702760975) == 13690208259) or
            ((bistate & 251723775) == 50344704) or
            ((bistate & 64440242175) == 12884901939) or
            ((bistate & 68718432000) == 53478144) or

            # rule 27 reflections
            ((bistate & 68718432000) == 855638784) or
            ((bistate & 68702760975) == 12884914179) or
            ((bistate & 251723775) == 50332464) or
            ((bistate & 64440242175) == 12888047619) or

            # contraction rule 28
            ((bistate & 68702760975) == 13690208256) or
            ((bistate & 251723775) == 50343936) or
            ((bistate & 64440242175) == 51) or
            ((bistate & 68718432000) == 3146496) or

            # rule 28 reflections
            ((bistate & 68718432000) == 855638016) or
            ((bistate & 68702760975) == 12291) or
            ((bistate & 251723775) == 816) or
            ((bistate & 64440242175) == 12888047616) or

            # contraction rule 29
            ((bistate & 68702760975) == 12935245824) or
            ((bistate & 251723775) == 50331699) or
            ((bistate & 64440242175) == 3146499) or
            ((bistate & 68718432000) == 13690209024) or

            # rule 29 reflections
            ((bistate & 68718432000) == 12938379264) or
            ((bistate & 68702760975) == 855638019) or
            ((bistate & 251723775) == 13059) or
            ((bistate & 64440242175) == 12884902704) or

            # contraction rule 30
            ((bistate & 68702760975) == 12935233539) or
            ((bistate & 251723775) == 50332419) or
            ((bistate & 64440242175) == 12884902659) or
            ((bistate & 68718432000) == 12935234304) or

            # contraction rule 31
            ((bistate & 68702760975) == 12935233536) or
            ((bistate & 251723775) == 50331651) or
            ((bistate & 64440242175) == 771) or
            ((bistate & 68718432000) == 12884902656) or

            # rule 31 reflections
            ((bistate & 68718432000) == 12935233536) or
            ((bistate & 68702760975) == 50331651) or
            ((bistate & 251723775) == 771) or
            ((bistate & 64440242175) == 12884902656) or

            # contraction rule 32
            ((bistate & 68702760975) == 12884914176) or
            ((bistate & 251723775) == 50331696) or
            ((bistate & 64440242175) == 3145731) or
            ((bistate & 68718432000) == 805307136) or

            # rule 32 reflections
            ((bistate & 68718432000) == 53477376) or
            ((bistate & 68702760975) == 805306371) or
            ((bistate & 251723775) == 13056) or
            ((bistate & 64440242175) == 12884901936) or

            # contraction rule 33
            ((bistate & 68702760975) == 12884901891) or
            ((bistate & 251723775) == 50332416) or
            ((bistate & 64440242175) == 12884901891) or
            ((bistate & 68718432000) == 50332416) or

            # contraction rule 34
            ((bistate & 68702760975) == 12884901888) or
            ((bistate & 251723775) == 50331648) or
            ((bistate & 64440242175) == 3) or
            ((bistate & 68718432000) == 768) or

            # rule 34 reflections
            ((bistate & 68718432000) == 50331648) or
            ((bistate & 68702760975) == 3) or
            ((bistate & 251723775) == 768) or
            ((bistate & 64440242175) == 12884901888) or

            # contraction rule 35
            ((bistate & 68702760975) == 855650304) or
            ((bistate & 251723775) == 12339) or
            ((bistate & 64440242175) == 3146544) or
            ((bistate & 68718432000) == 13693353984) or

            # contraction rule 36
            ((bistate & 68702760975) == 855638016) or
            ((bistate & 251723775) == 12291) or
            ((bistate & 64440242175) == 816) or
            ((bistate & 68718432000) == 12888047616) or

            # rule 36 reflections
            ((bistate & 68718432000) == 13690208256) or
            ((bistate & 68702760975) == 50343936) or
            ((bistate & 251723775) == 51) or
            ((bistate & 64440242175) == 3146496) or

            # contraction rule 37
            ((bistate & 68702760975) == 805318656) or
            ((bistate & 251723775) == 12336) or
            ((bistate & 64440242175) == 3145776) or
            ((bistate & 68718432000) == 808452096) or

            # contraction rule 38
            ((bistate & 68702760975) == 805306368) or
            ((bistate & 251723775) == 12288) or
            ((bistate & 64440242175) == 48) or
            ((bistate & 68718432000) == 3145728) or

            # rule 38 reflections
            ((bistate & 68718432000) == 805306368) or
            ((bistate & 68702760975) == 12288) or
            ((bistate & 251723775) == 48) or
            ((bistate & 64440242175) == 3145728) or

            # contraction rule 39
            ((bistate & 68702760975) == 50331648) or
            ((bistate & 251723775) == 3) or
            ((bistate & 64440242175) == 768) or
            ((bistate & 68718432000) == 12884901888) or

            # contraction rule 40
            ((bistate & 68702760975) == 0) or
            ((bistate & 251723775) == 0) or
            ((bistate & 64440242175) == 0) or
            ((bistate & 68718432000) == 0)
            )

def check3(bistate): #Dealing with loops
    return (# contraction rule 41
            ((bistate & 64425492480) == 60130328576) or
            ((bistate & 252641280) == 252510208) or
            ((bistate & 983055) == 917516) or
            ((bistate & 986880) == 986368) or
            
            # rule 41 reflection
            ((bistate & 252641280) == 235667456) or
            ((bistate & 983055) == 851983) or
            ((bistate & 986880) == 920576) or
            ((bistate & 64425492480) == 55835557888) or
            
            # contraction rule 42
            ((bistate & 4027514880) == 3758882816) or
            ((bistate & 1044480) == 913408) or
            ((bistate & 983280) == 917696) or
            ((bistate & 16711680) == 14614528) or

            # contraction rule 43
            ((bistate & 252641280) == 235667456) or
            ((bistate & 983055) == 851983) or
            ((bistate & 986880) == 920576) or
            ((bistate & 64425492480) == 55835557888) or

            # rule 43 reflection
            ((bistate & 64425492480) == 60130328576) or
            ((bistate & 252641280) == 252510208) or
            ((bistate & 983055) == 917516) or
            ((bistate & 986880) == 986368) or

            # contraction rule 44
            ((bistate & 64425492480) == 55835361280) or
            ((bistate & 252641280) == 235732992) or
            ((bistate & 983055) == 917519) or
            ((bistate & 986880) == 986112) or

            # rule 44 reflection
            ((bistate & 252641280) == 252444672) or
            ((bistate & 983055) == 851980) or
            ((bistate & 986880) == 920832) or
            ((bistate & 64425492480) == 60130525184)
            )

def check4(bistate): #Contracting open spaces from the edges
    return(# contraction rule 45
            ((bistate & 4278251535) == 50343939) or
            ((bistate & 65535) == 819) or
            ((bistate & 64440242160) == 12888048384) or
            ((bistate & 68718428160) == 13740539904) or

            # rule 45 reflections
            ((bistate & 68466773760) == 12888048384) or
            ((bistate & 68702760960) == 13740539904) or
            ((bistate & 251719935) == 50343939) or
            ((bistate & 15732735) == 819) or

            # contraction rule 46
            ((bistate & 4278251535) == 50343936) or
            ((bistate & 65535) == 51) or
            ((bistate & 64440242160) == 3146496) or
            ((bistate & 68718428160) == 13690208256) or

            # rule 46 reflections
            ((bistate & 68466773760) == 12888047616) or
            ((bistate & 68702760960) == 855638016) or
            ((bistate & 251719935) == 12291) or
            ((bistate & 15732735) == 816) or

            # contraction rule 47
            ((bistate & 4278251535) == 50331651) or
            ((bistate & 65535) == 771) or
            ((bistate & 64440242160) == 12884902656) or
            ((bistate & 68718428160) == 12935233536) or

            # rule 47 reflections
            ((bistate & 68466773760) == 12884902656) or
            ((bistate & 68702760960) == 12935233536) or
            ((bistate & 251719935) == 50331651) or
            ((bistate & 15732735) == 771) or

            # contraction rule 48
            ((bistate & 4278251535) == 50331648) or
            ((bistate & 65535) == 3) or
            ((bistate & 64440242160) == 768) or
            ((bistate & 68718428160) == 12884901888) or

            # rule 48 reflections
            ((bistate & 68466773760) == 12884901888) or
            ((bistate & 68702760960) == 50331648) or
            ((bistate & 251719935) == 3) or
            ((bistate & 15732735) == 768) or

            # contraction rule 49
            ((bistate & 4278251535) == 12291) or
            ((bistate & 65535) == 816) or
            ((bistate & 64440242160) == 12888047616) or
            ((bistate & 68718428160) == 855638016) or

            # rule 49 reflections
            ((bistate & 68466773760) == 3146496) or
            ((bistate & 68702760960) == 13690208256) or
            ((bistate & 251719935) == 50343936) or
            ((bistate & 15732735) == 51) or

            # contraction rule 50
            ((bistate & 4278251535) == 12288) or
            ((bistate & 65535) == 48) or
            ((bistate & 64440242160) == 3145728) or
            ((bistate & 68718428160) == 805306368) or

            # rule 50 reflections
            ((bistate & 68466773760) == 3145728) or
            ((bistate & 68702760960) == 805306368) or
            ((bistate & 251719935) == 12288) or
            ((bistate & 15732735) == 48) or

            # contraction rule 51
            ((bistate & 4278251535) == 3) or
            ((bistate & 65535) == 768) or
            ((bistate & 64440242160) == 12884901888) or
            ((bistate & 68718428160) == 50331648) or

            # rule 51 reflections
            ((bistate & 68466773760) == 768) or
            ((bistate & 68702760960) == 12884901888) or
            ((bistate & 251719935) == 50331648) or
            ((bistate & 15732735) == 3) or

            # contraction rule 52
            ((bistate & 4278251535) == 0) or
            ((bistate & 65535) == 0) or
            ((bistate & 64440242160) == 0) or
            ((bistate & 68718428160) == 0) or

            # rule 52 reflections
            ((bistate & 68466773760) == 0) or
            ((bistate & 68702760960) == 0) or
            ((bistate & 251719935) == 0) or
            ((bistate & 15732735) == 0))
