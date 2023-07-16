from typing import Any, Dict, Set

from dcs import task
from dcs.helicopters import HelicopterType
from dcs.weapons_data import Weapons

from game.modsupport import helicoptermod
from pydcs_extensions.weapon_injector import inject_weapons


class WeaponsUH1M:
    M3_RocketPodL_24_FFAR_HEI_ = {
        "clsid": "{M3RocketPodL}",
        "name": "M3 RocketPodL 24 FFAR(HEI)",
        "weight": 161,
    }
    M3_RocketPodR_24_FFAR_HEI_ = {
        "clsid": "{M3RocketPodR}",
        "name": "M3 RocketPodR 24 FFAR(HEI)",
        "weight": 161,
    }
    UH1CMinigunL = {"clsid": "{UH1C_minigunL}", "name": "UH1CMinigunL", "weight": 100}
    UH1CMinigunR = {"clsid": "{UH1C_minigunR}", "name": "UH1CMinigunR", "weight": 100}
    XM16_Weapon_System = {
        "clsid": "{XM16RocketPodR}",
        "name": "XM16 Weapon System",
        "weight": 78.2,
    }
    XM16_Weapon_System_ = {
        "clsid": "{XM16RocketPodL}",
        "name": "XM16 Weapon System",
        "weight": 78.2,
    }
    XM16_Weapon_System__ = {
        "clsid": "{XM16TwinM60L}",
        "name": "XM16 Weapon System",
        "weight": 70,
    }
    XM16_Weapon_System___ = {
        "clsid": "{XM16TwinM60R}",
        "name": "XM16 Weapon System",
        "weight": 70,
    }
    XM5_2_M2_Browning = {
        "clsid": "{UH1CTwinMGsChin}",
        "name": "XM5 2*M2 Browning",
        "weight": 100,
    }
    XM5_Grenade_launcher = {
        "clsid": "{UH1C40mmLauncher}",
        "name": "XM5 Grenade launcher",
        "weight": 63,
    }


inject_weapons(WeaponsUH1M)


@helicoptermod
class UH1M(HelicopterType):
    id = "UH1M"
    flyable = True
    height = 3.69
    width = 13.4
    length = 11.75
    fuel_max = 631
    max_speed = 240
    chaff = 120
    flare = 120
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Air"  # {828CEADE-3F1D-40aa-93CE-8CDB73FE2710}
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {6: 41, 2: 31, 8: 50, 3: 32, 1: 30, 4: 33, 5: 40, 7: 42},
        },
    }

    livery_name = "UH1M"  # from type

    class Pylon1:
        UH1CMinigunL = (1, WeaponsUH1M.UH1CMinigunL)
        XM16_Weapon_System__ = (1, WeaponsUH1M.XM16_Weapon_System__)

    class Pylon2:
        UH1CMinigunR = (2, WeaponsUH1M.UH1CMinigunR)
        XM16_Weapon_System___ = (2, WeaponsUH1M.XM16_Weapon_System___)

    class Pylon3:
        XM16_Weapon_System_ = (3, WeaponsUH1M.XM16_Weapon_System_)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            3,
            Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        M3_RocketPodL_24_FFAR_HEI_ = (3, WeaponsUH1M.M3_RocketPodL_24_FFAR_HEI_)

    class Pylon4:
        XM16_Weapon_System = (4, WeaponsUH1M.XM16_Weapon_System)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
            4,
            Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        )
        M3_RocketPodR_24_FFAR_HEI_ = (4, WeaponsUH1M.M3_RocketPodR_24_FFAR_HEI_)

    class Pylon5:
        XM5_Grenade_launcher = (5, WeaponsUH1M.XM5_Grenade_launcher)
        XM5_2_M2_Browning = (5, WeaponsUH1M.XM5_2_M2_Browning)

    class Pylon6:
        M60_SIDE_L = (6, Weapons.M60_SIDE_L)
        M134_SIDE_L = (6, Weapons.M134_SIDE_L)

    class Pylon7:
        M60_SIDE_R = (7, Weapons.M60_SIDE_R)
        M134_SIDE_R = (7, Weapons.M134_SIDE_R)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.Transport]
    task_default = task.CAS
