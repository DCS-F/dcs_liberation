from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons


from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons


class WeaponsF16:
    CFT_Conformal_Fuel_Tank = {
        "clsid": "{VSN_CFT_PTB}",
        "name": "CFT Conformal Fuel Tank",
        "weight": 1150,
    }
    Fuel_Tank_330_gallons = {
        "clsid": "{VSN_F16C_PTB}",
        "name": "Fuel Tank 330 gallons",
        "weight": 1150,
    }
    Fuel_Tank_330_gallons_and_CFT_Conformal_Fuel_Tank = {
        "clsid": "{VSN_F16CCFT_PTB}",
        "name": "Fuel Tank 330 gallons and CFT Conformal Fuel Tank",
        "weight": 1150,
    }
    Fuel_Tank_zenter_330_gallons = {
        "clsid": "{VSN_F16C2_PTB}",
        "name": "Fuel Tank zenter 330 gallons",
        "weight": 1150,
    }


inject_weapons(WeaponsF16)


@planemod
class VSN_F16A(PlaneType):
    id = "VSN_F16A"
    flyable = True
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    Liveries = Liveries()[id]

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            1,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        GBU_10___2000lb_Laser_Guided_Bomb = (
            2,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            2,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        AGM_119B_Penguin_ASM = (2, Weapons.AGM_119B_Penguin_ASM)
        LAU_117_AGM_65H = (2, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            2,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            2,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            2,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            2,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        Fuel_Tank_330_gallons = (2, WeaponsF16.Fuel_Tank_330_gallons)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            3,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)

    class Pylon4:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            4,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (4, Weapons.AIM_9M_Sidewinder_IR_AAM)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            4,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            4,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        AGM_119B_Penguin_ASM = (4, Weapons.AGM_119B_Penguin_ASM)
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (4, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (4, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            4,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            4,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            4,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            4,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        _2xGBU_12___500lb_Laser_Guided_Bomb = (
            4,
            Weapons._2xGBU_12___500lb_Laser_Guided_Bomb,
        )
        AGM_154C___JSOW_Unitary_BROACH = (4, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            4,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )

    class Pylon5:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            5,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )

    class Pylon6:
        ALQ_131___ECM_Pod = (6, Weapons.ALQ_131___ECM_Pod)
        Fuel_Tank_zenter_330_gallons = (6, WeaponsF16.Fuel_Tank_zenter_330_gallons)

    class Pylon7:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            7,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            8,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            8,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            8,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        AGM_119B_Penguin_ASM = (8, Weapons.AGM_119B_Penguin_ASM)
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (8, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            8,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            8,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            8,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            8,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            8,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        _2xGBU_12___500lb_Laser_Guided_Bomb = (
            8,
            Weapons._2xGBU_12___500lb_Laser_Guided_Bomb,
        )
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            8,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            9,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)

    class Pylon10:
        GBU_10___2000lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_12___500lb_Laser_Guided_Bomb,
        )
        Mk_84___2000lb_GP_Bomb_LD = (10, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            10,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        AGM_119B_Penguin_ASM = (10, Weapons.AGM_119B_Penguin_ASM)
        LAU_117_AGM_65H = (10, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            10,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (10, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            10,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            10,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            10,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        Fuel_Tank_330_gallons = (10, WeaponsF16.Fuel_Tank_330_gallons)

    class Pylon11:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (
            11,
            Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM,
        )
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            11,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance,
        task.GroundAttack,
        task.CAS,
    ]
    task_default = task.FighterSweep


@planemod
class VSN_F16AMLU(PlaneType):
    id = "VSN_F16AMLU"
    flyable = True
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    Liveries = Liveries()[id]

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        Fuel_Tank_330_gallons = (2, WeaponsF16.Fuel_Tank_330_gallons)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon4:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (4, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (4, Weapons.AIM_9P_Sidewinder_IR_AAM)
        MXU_648_TP = (4, Weapons.MXU_648_TP)

    class Pylon6:
        ALQ_131___ECM_Pod = (6, Weapons.ALQ_131___ECM_Pod)
        ALQ_184 = (6, Weapons.ALQ_184)
        Fuel_Tank_zenter_330_gallons = (6, WeaponsF16.Fuel_Tank_zenter_330_gallons)

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        MXU_648_TP = (8, Weapons.MXU_648_TP)

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon10:
        Fuel_Tank_330_gallons = (10, WeaponsF16.Fuel_Tank_330_gallons)

    class Pylon11:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (
            11,
            Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (11, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons = {1, 2, 3, 4, 6, 8, 9, 10, 11}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance,
        task.GroundAttack,
        task.CAS,
    ]
    task_default = task.FighterSweep


@planemod
class VSN_F16CBL50(PlaneType):
    id = "VSN_F16CBL50"
    flyable = True
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    Liveries = Liveries()[id]

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            1,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        GBU_10___2000lb_Laser_Guided_Bomb = (
            2,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            2,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_117_AGM_65H = (2, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            2,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            2,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            2,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            2,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            2,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        CBU_87___202_x_CEM_Cluster_Bomb = (2, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (2, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (
            2,
            Weapons.CBU_103___202_x_CEM__CBU_with_WCMD,
        )
        CBU_105___10_x_SFW__CBU_with_WCMD = (
            2,
            Weapons.CBU_105___10_x_SFW__CBU_with_WCMD,
        )
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            2,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )
        Fuel_Tank_330_gallons = (2, WeaponsF16.Fuel_Tank_330_gallons)

    class Pylon3:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            3,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)

    class Pylon4:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            4,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (4, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (4, Weapons.AIM_9P_Sidewinder_IR_AAM)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            4,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_88_with_3_x_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            4,
            Weapons.LAU_88_with_3_x_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            4,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            4,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (4, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (4, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            4,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            4,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            4,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            4,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            4,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (
            4,
            Weapons.CBU_103___202_x_CEM__CBU_with_WCMD,
        )
        CBU_105___10_x_SFW__CBU_with_WCMD = (
            4,
            Weapons.CBU_105___10_x_SFW__CBU_with_WCMD,
        )
        _2xGBU_12___500lb_Laser_Guided_Bomb = (
            4,
            Weapons._2xGBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            4,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )
        AGM_154C___JSOW_Unitary_BROACH = (4, Weapons.AGM_154C___JSOW_Unitary_BROACH)

    class Pylon5:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            5,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )

    class Pylon6:
        ALQ_131___ECM_Pod = (6, Weapons.ALQ_131___ECM_Pod)
        Fuel_Tank_zenter_330_gallons = (6, WeaponsF16.Fuel_Tank_zenter_330_gallons)
        Fuel_Tank_330_gallons_and_CFT_Conformal_Fuel_Tank = (
            6,
            WeaponsF16.Fuel_Tank_330_gallons_and_CFT_Conformal_Fuel_Tank,
        )
        CFT_Conformal_Fuel_Tank = (6, WeaponsF16.CFT_Conformal_Fuel_Tank)

    class Pylon7:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            7,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )

    class Pylon8:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            8,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            8,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_88_with_3_x_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            8,
            Weapons.LAU_88_with_3_x_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            8,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            8,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (8, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            8,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            8,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            8,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            8,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            8,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            8,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        CBU_87___202_x_CEM_Cluster_Bomb = (8, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (8, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (
            8,
            Weapons.CBU_103___202_x_CEM__CBU_with_WCMD,
        )
        CBU_105___10_x_SFW__CBU_with_WCMD = (
            8,
            Weapons.CBU_105___10_x_SFW__CBU_with_WCMD,
        )
        _2xGBU_12___500lb_Laser_Guided_Bomb = (
            8,
            Weapons._2xGBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            8,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)

    class Pylon9:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            9,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)

    class Pylon10:
        GBU_10___2000lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_12___500lb_Laser_Guided_Bomb,
        )
        Mk_84___2000lb_GP_Bomb_LD = (10, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            10,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_117_AGM_65H = (10, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            10,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (10, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            10,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            10,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            10,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            10,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        CBU_87___202_x_CEM_Cluster_Bomb = (10, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (10, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (
            10,
            Weapons.CBU_103___202_x_CEM__CBU_with_WCMD,
        )
        CBU_105___10_x_SFW__CBU_with_WCMD = (
            10,
            Weapons.CBU_105___10_x_SFW__CBU_with_WCMD,
        )
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            10,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )
        Fuel_Tank_330_gallons = (10, WeaponsF16.Fuel_Tank_330_gallons)

    class Pylon11:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (
            11,
            Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM,
        )
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            11,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance,
    ]
    task_default = task.FighterSweep


@planemod
class VSN_F16CBL52D(PlaneType):
    id = "VSN_F16CBL52D"
    flyable = True
    height = 5.63
    width = 13.05
    length = 19.43
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 90
    flare = 45
    charge_total = 180
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    Liveries = Liveries()[id]

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        AGM_154C___JSOW_Unitary_BROACH = (2, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            2,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            2,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_117_AGM_65H = (2, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            2,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            2,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            2,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            2,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            2,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        CBU_87___202_x_CEM_Cluster_Bomb = (2, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (2, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (
            2,
            Weapons.CBU_103___202_x_CEM__CBU_with_WCMD,
        )
        CBU_105___10_x_SFW__CBU_with_WCMD = (
            2,
            Weapons.CBU_105___10_x_SFW__CBU_with_WCMD,
        )
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            2,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )
        Fuel_Tank_330_gallons = (2, WeaponsF16.Fuel_Tank_330_gallons)

    class Pylon3:
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)

    class Pylon4:
        AIM_9M_Sidewinder_IR_AAM = (4, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (4, Weapons.AIM_9P_Sidewinder_IR_AAM)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            4,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            4,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_117_AGM_65H = (4, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (4, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (4, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            4,
            Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (4, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            4,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            4,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            4,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            4,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            4,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (
            4,
            Weapons.CBU_103___202_x_CEM__CBU_with_WCMD,
        )
        CBU_105___10_x_SFW__CBU_with_WCMD = (
            4,
            Weapons.CBU_105___10_x_SFW__CBU_with_WCMD,
        )
        _2xGBU_12___500lb_Laser_Guided_Bomb = (
            4,
            Weapons._2xGBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            4,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )
        AGM_154C___JSOW_Unitary_BROACH = (4, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            4,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )

    class Pylon5:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            5,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )
        L_081_Fantasmagoria_ELINT_pod = (5, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon6:
        ALQ_131___ECM_Pod = (6, Weapons.ALQ_131___ECM_Pod)
        ALQ_184 = (6, Weapons.ALQ_184)
        Fuel_Tank_zenter_330_gallons = (6, WeaponsF16.Fuel_Tank_zenter_330_gallons)
        Fuel_Tank_330_gallons_and_CFT_Conformal_Fuel_Tank = (
            6,
            WeaponsF16.Fuel_Tank_330_gallons_and_CFT_Conformal_Fuel_Tank,
        )
        CFT_Conformal_Fuel_Tank = (6, WeaponsF16.CFT_Conformal_Fuel_Tank)

    class Pylon7:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            7,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )
        L_081_Fantasmagoria_ELINT_pod = (7, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon8:
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_88_with_3_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            8,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            8,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_117_AGM_65H = (8, Weapons.LAU_117_AGM_65H)
        LAU_88_AGM_65H_2_L = (8, Weapons.LAU_88_AGM_65H_2_L)
        LAU_88_AGM_65H_3 = (8, Weapons.LAU_88_AGM_65H_3)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_ = (
            8,
            Weapons.LAU_88_with_2_x_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (8, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            8,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            8,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            8,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            8,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            8,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            8,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        CBU_87___202_x_CEM_Cluster_Bomb = (8, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (8, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (
            8,
            Weapons.CBU_103___202_x_CEM__CBU_with_WCMD,
        )
        CBU_105___10_x_SFW__CBU_with_WCMD = (
            8,
            Weapons.CBU_105___10_x_SFW__CBU_with_WCMD,
        )
        _2xGBU_12___500lb_Laser_Guided_Bomb = (
            8,
            Weapons._2xGBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            8,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            8,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )

    class Pylon9:
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)

    class Pylon10:
        AGM_154C___JSOW_Unitary_BROACH = (10, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_12___500lb_Laser_Guided_Bomb,
        )
        Mk_84___2000lb_GP_Bomb_LD = (10, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (
            10,
            Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_117_AGM_65H = (10, Weapons.LAU_117_AGM_65H)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (
            10,
            Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_,
        )
        LAU_117_AGM_65G = (10, Weapons.LAU_117_AGM_65G)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (
            10,
            Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_,
        )
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            10,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD = (
            10,
            Weapons.BRU_42_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bombs_HD,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            10,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        CBU_87___202_x_CEM_Cluster_Bomb = (10, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (10, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        CBU_103___202_x_CEM__CBU_with_WCMD = (
            10,
            Weapons.CBU_103___202_x_CEM__CBU_with_WCMD,
        )
        CBU_105___10_x_SFW__CBU_with_WCMD = (
            10,
            Weapons.CBU_105___10_x_SFW__CBU_with_WCMD,
        )
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            10,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )
        Fuel_Tank_330_gallons = (10, WeaponsF16.Fuel_Tank_330_gallons)

    class Pylon11:
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (11, Weapons.AIM_9P_Sidewinder_IR_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance,
        task.GroundAttack,
        task.CAS,
    ]
    task_default = task.FighterSweep
