from enum import Enum
from typing import Set

from dcs import task
from dcs.liveries_scanner import Liveries
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons


class WeaponsF100:
    Fuel_tank_1000_Liter = {
        "clsid": "{VSN_F1001000_ptb}",
        "name": "Fuel tank 1000 Liter",
        "weight": 934,
    }
    Fuel_tank_500_Liter = {
        "clsid": "{VSN_F100500_ptb}",
        "name": "Fuel tank 500 Liter",
        "weight": 693,
    }
    TER_M117_F_105 = {
        "clsid": "{SB_F105_TER9A_M117_3}",
        "name": "TER M117 F-105",
        "weight": 1500,
    }
    MER_6_M117_F_105 = {
        "clsid": "{SB_F105_BRU_41A_M117_6}",
        "name": "MER*6 M117 F-105",
        "weight": 2100,
    }


inject_weapons(WeaponsF100)


@planemod
class VSN_F100(PlaneType):
    id = "VSN_F100"
    flyable = True
    height = 4.95
    width = 11.81
    length = 15
    fuel_max = 3397
    max_speed = 1702.8
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}

    class Liveries:
        class USSR(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Georgia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Venezuela(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Australia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Israel(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Combined_Joint_Task_Forces_Blue(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Sudan(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Norway(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Romania(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Iran(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Ukraine(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Libya(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Belgium(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Slovakia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Greece(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class UK(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Third_Reich(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Hungary(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Abkhazia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Morocco(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class United_Nations_Peacekeepers(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Switzerland(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class SouthOssetia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Vietnam(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class China(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Yemen(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Kuwait(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Serbia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Oman(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class India(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Egypt(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class TheNetherlands(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Poland(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Syria(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Finland(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Kazakhstan(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Denmark(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Sweden(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Croatia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class CzechRepublic(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class GDR(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Yugoslavia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Bulgaria(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class SouthKorea(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Tunisia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Combined_Joint_Task_Forces_Red(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Lebanon(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Portugal(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Cuba(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Insurgents(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class SaudiArabia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class France(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class USA(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Honduras(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Qatar(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Russia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class United_Arab_Emirates(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Italian_Social_Republi(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Austria(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Bahrain(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Italy(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Chile(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Turkey(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Philippines(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Algeria(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Pakistan(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Malaysia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Indonesia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Iraq(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Germany(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class South_Africa(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Jordan(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Mexico(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class USAFAggressors(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Brazil(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Spain(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Belarus(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Canada(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class NorthKorea(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Ethiopia(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Japan(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

        class Thailand(Enum):
            _481_TFS_63054 = "481 TFS 63054"
            AF_53_CT_318 = "AF 53 CT 318"
            Thunderbirds_No_1 = "Thunderbirds No 1"

    class Pylon2:
        L_081_Fantasmagoria_ELINT_pod = (2, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon3:
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9B_Sidewinder_IR_AAM = (3, Weapons.AIM_9B_Sidewinder_IR_AAM)
        LAU_7_with_AIM_9B_Sidewinder_IR_AAM = (
            3,
            Weapons.LAU_7_with_AIM_9B_Sidewinder_IR_AAM,
        )
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (
            3,
            Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
        )
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (3, Weapons.M117___750lb_GP_Bomb_LD)
        AGM_45A_Shrike_ARM = (3, Weapons.AGM_45A_Shrike_ARM)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (
            3,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE,
        )
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (
            3,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT,
        )
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            3,
            Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
            3,
            Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        )
        BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            3,
            Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            3,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )

    # ERRR <CLEAN>

    class Pylon4:
        AIM_9P_Sidewinder_IR_AAM = (4, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (4, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9B_Sidewinder_IR_AAM = (4, Weapons.AIM_9B_Sidewinder_IR_AAM)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (
            4,
            Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
        )
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            4,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            4,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            4,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (4, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (4, Weapons.M117___750lb_GP_Bomb_LD)
        TER_M117_F_105 = (4, WeaponsF100.TER_M117_F_105)
        AGM_45A_Shrike_ARM = (4, Weapons.AGM_45A_Shrike_ARM)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (
            4,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE,
        )
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (
            4,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT,
        )
        Fuel_tank_1000_Liter = (4, WeaponsF100.Fuel_tank_1000_Liter)

    # ERRR <CLEAN>

    class Pylon5:
        AIM_9P_Sidewinder_IR_AAM = (5, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (5, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9B_Sidewinder_IR_AAM = (5, Weapons.AIM_9B_Sidewinder_IR_AAM)
        LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM = (
            5,
            Weapons.LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM,
        )
        LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM = (
            5,
            Weapons.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM,
        )
        LAU_7_with_2_x_AIM_9L_Sidewinder_IR_AAM = (
            5,
            Weapons.LAU_7_with_2_x_AIM_9L_Sidewinder_IR_AAM,
        )
        LAU_7_with_2_x_AIM_9B_Sidewinder_IR_AAM = (
            5,
            Weapons.LAU_7_with_2_x_AIM_9B_Sidewinder_IR_AAM,
        )
        LAU_7_with_2_x_AIM_9P5_Sidewinder_IR_AAM = (
            5,
            Weapons.LAU_7_with_2_x_AIM_9P5_Sidewinder_IR_AAM,
        )
        Mk_84___2000lb_GP_Bomb_LD = (5, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (
            5,
            Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
        )
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            5,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            5,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (5, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            5,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        MER_6_M117_F_105 = (5, WeaponsF100.MER_6_M117_F_105)
        TER_M117_F_105 = (5, WeaponsF100.TER_M117_F_105)
        _3_Mk_83 = (5, Weapons._3_Mk_83)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (
            5,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE,
        )
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (
            5,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT,
        )
        BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            5,
            Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        LAU_7_with_AIM_9P_Sidewinder_IR_AAM = (
            5,
            Weapons.LAU_7_with_AIM_9P_Sidewinder_IR_AAM,
        )
        LAU_7_with_AIM_9B_Sidewinder_IR_AAM = (
            5,
            Weapons.LAU_7_with_AIM_9B_Sidewinder_IR_AAM,
        )
        LAU_118a_with_AGM_45B_Shrike_ARM__Imp_ = (
            5,
            Weapons.LAU_118a_with_AGM_45B_Shrike_ARM__Imp_,
        )

        Fuel_tank_500_Liter = (5, WeaponsF100.Fuel_tank_500_Liter)

    # ERRR <CLEAN>

    class Pylon6:
        Smoke_Generator___red_ = (6, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (6, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (6, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (6, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (6, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (6, Weapons.Smoke_Generator___orange_)

    class Pylon7:
        AIM_9P_Sidewinder_IR_AAM = (7, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (7, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9B_Sidewinder_IR_AAM = (7, Weapons.AIM_9B_Sidewinder_IR_AAM)
        LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM = (
            7,
            Weapons.LAU_105_with_2_x_AIM_9P_Sidewinder_IR_AAM,
        )
        LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM = (
            7,
            Weapons.LAU_105_with_2_x_AIM_9M_Sidewinder_IR_AAM,
        )
        LAU_7_with_2_x_AIM_9L_Sidewinder_IR_AAM = (
            7,
            Weapons.LAU_7_with_2_x_AIM_9L_Sidewinder_IR_AAM,
        )
        LAU_7_with_2_x_AIM_9B_Sidewinder_IR_AAM = (
            7,
            Weapons.LAU_7_with_2_x_AIM_9B_Sidewinder_IR_AAM,
        )
        LAU_7_with_2_x_AIM_9P5_Sidewinder_IR_AAM = (
            7,
            Weapons.LAU_7_with_2_x_AIM_9P5_Sidewinder_IR_AAM,
        )
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (
            7,
            Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
        )
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            7,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            7,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (7, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            7,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        MER_6_M117_F_105 = (7, WeaponsF100.MER_6_M117_F_105)
        TER_M117_F_105 = (7, WeaponsF100.TER_M117_F_105)
        _3_Mk_83 = (7, Weapons._3_Mk_83)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (
            7,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE,
        )
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (
            7,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT,
        )
        BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            7,
            Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        LAU_7_with_AIM_9B_Sidewinder_IR_AAM = (
            7,
            Weapons.LAU_7_with_AIM_9B_Sidewinder_IR_AAM,
        )
        LAU_7_with_AIM_9P_Sidewinder_IR_AAM = (
            7,
            Weapons.LAU_7_with_AIM_9P_Sidewinder_IR_AAM,
        )
        Fuel_tank_500_Liter = (7, WeaponsF100.Fuel_tank_500_Liter)

    # ERRR <CLEAN>

    class Pylon8:
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9B_Sidewinder_IR_AAM = (8, Weapons.AIM_9B_Sidewinder_IR_AAM)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (
            8,
            Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
        )
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            8,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            8,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            8,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (8, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (8, Weapons.M117___750lb_GP_Bomb_LD)
        TER_M117_F_105 = (8, WeaponsF100.TER_M117_F_105)
        AGM_45A_Shrike_ARM = (8, Weapons.AGM_45A_Shrike_ARM)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (
            8,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE,
        )
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (
            8,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT,
        )
        Fuel_tank_1000_Liter = (8, WeaponsF100.Fuel_tank_1000_Liter)

    # ERRR <CLEAN>

    class Pylon9:
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9B_Sidewinder_IR_AAM = (9, Weapons.AIM_9B_Sidewinder_IR_AAM)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (
            9,
            Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD,
        )
        LAU_7_with_AIM_9B_Sidewinder_IR_AAM = (
            9,
            Weapons.LAU_7_with_AIM_9B_Sidewinder_IR_AAM,
        )
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (9, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        M117___750lb_GP_Bomb_LD = (9, Weapons.M117___750lb_GP_Bomb_LD)
        AGM_45A_Shrike_ARM = (9, Weapons.AGM_45A_Shrike_ARM)
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE = (
            9,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk1__HE,
        )
        LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT = (
            9,
            Weapons.LAU_3_pod___19_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT,
        )
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            9,
            Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
            9,
            Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        )
        BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            9,
            Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            9,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )

    # ERRR <CLEAN>

    pylons: Set[int] = {2, 3, 4, 5, 6, 7, 8, 9}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance,
        task.GroundAttack,
        task.CAS,
        task.RunwayAttack,
        task.AntishipStrike,
    ]
    task_default = task.FighterSweep
