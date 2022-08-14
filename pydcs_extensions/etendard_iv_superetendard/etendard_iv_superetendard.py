from enum import Enum

from dcs import task, unittype
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod, shipmod
from pydcs_extensions.weapon_injector import inject_weapons


class WeaponsSuperEtendardClemenceau:
    RADAR_ANEMONE = {
        "clsid": "{RADAR_ANEMONE}",
        "name": "RADAR_ANEMONE",
        "weight": 1.4789,
    }
    Reservoir_SEM = {
        "clsid": "{Reservoir_SEM}",
        "name": "Reservoir_SEM",
        "weight": 1102,
    }

    AS_30L = {"clsid": "{AS_30L}", "name": "AS_30L", "weight": 292}
    Exocet = {"clsid": "{Exocet}", "name": "Exocet", "weight": 640}


inject_weapons(WeaponsSuperEtendardClemenceau)


@planemod
class SEM(PlaneType):
    id = "SEM"
    flyable = True
    height = 5.2
    width = 9.13
    length = 14.36
    fuel_max = 3165
    max_speed = 2376
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:
        class USSR(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Georgia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Venezuela(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Australia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Israel(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Combined_Joint_Task_Forces_Blue(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Sudan(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Norway(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Romania(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Iran(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Ukraine(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Libya(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Belgium(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Slovakia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Greece(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class UK(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Third_Reich(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Hungary(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Abkhazia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Morocco(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class United_Nations_Peacekeepers(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Switzerland(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class SouthOssetia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Vietnam(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class China(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Yemen(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Kuwait(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Serbia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Oman(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class India(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Egypt(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class TheNetherlands(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Poland(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Syria(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Finland(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Kazakhstan(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Denmark(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Sweden(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Croatia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class CzechRepublic(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class GDR(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Yugoslavia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Bulgaria(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class SouthKorea(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Tunisia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Combined_Joint_Task_Forces_Red(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Lebanon(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Portugal(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Cuba(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Insurgents(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class SaudiArabia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class France(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class USA(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Honduras(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Qatar(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Russia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class United_Arab_Emirates(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Italian_Social_Republi(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Austria(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Bahrain(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Italy(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Chile(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Turkey(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Philippines(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Algeria(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Pakistan(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Malaysia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Indonesia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Iraq(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Germany(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class South_Africa(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Jordan(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Mexico(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class USAFAggressors(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Brazil(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Spain(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Belarus(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Canada(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class NorthKorea(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Ethiopia(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Japan(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

        class Thailand(Enum):
            _01_SEM_11_F_CAMO_1 = "01 SEM 11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE___Antenne = "03 FRANCE MARINE - Antenne"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_FRANCE_MARINE = "09 FRANCE MARINE"
            _10_Flotille_17f = "10 Flotille 17f"

    class Pylon1:
        GBU_12___500lb_Laser_Guided_Bomb = (1, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        # ERRR {GBU_49}
        Mk_84___2000lb_GP_Bomb_LD = (1, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Matra_Type_155_Rocket_Pod = (1, Weapons.Matra_Type_155_Rocket_Pod)
        R550_Magic_2_IR_AAM = (1, Weapons.R550_Magic_2_IR_AAM)
        BLG_66_AC_Belouga = (1, Weapons.BLG_66_AC_Belouga)
        AS_30L = (1, WeaponsSuperEtendardClemenceau.AS_30L)

    class Pylon2:
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BLG_66_AC_Belouga = (2, Weapons.BLG_66_AC_Belouga)
        AS_30L = (2, WeaponsSuperEtendardClemenceau.AS_30L)
        Exocet = (2, WeaponsSuperEtendardClemenceau.Exocet)
        Reservoir_SEM = (2, WeaponsSuperEtendardClemenceau.Reservoir_SEM)

    # ERRR {GBU_49}

    class Pylon3:
        AUF2_BLG_66_AC_x_2 = (3, Weapons.AUF2_BLG_66_AC_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (3, Weapons.AUF2_MK_82_Snakeyes_x_2)

    class Pylon4:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            4,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )
        Mercury_LLTV_Pod = (4, Weapons.Mercury_LLTV_Pod)
        RADAR_ANEMONE = (4, WeaponsSuperEtendardClemenceau.RADAR_ANEMONE)

    class Pylon5:
        AUF2_BLG_66_AC_x_2 = (5, Weapons.AUF2_BLG_66_AC_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (5, Weapons.AUF2_MK_82_Snakeyes_x_2)

    class Pylon6:
        BLG_66_AC_Belouga = (6, Weapons.BLG_66_AC_Belouga)
        AS_30L = (6, WeaponsSuperEtendardClemenceau.AS_30L)
        Exocet = (6, WeaponsSuperEtendardClemenceau.Exocet)
        Reservoir_SEM = (6, WeaponsSuperEtendardClemenceau.Reservoir_SEM)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)

    # ERRR {GBU_49}
    # ERRR {GBU_49}

    class Pylon7:
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Matra_Type_155_Rocket_Pod = (7, Weapons.Matra_Type_155_Rocket_Pod)
        R550_Magic_2_IR_AAM = (7, Weapons.R550_Magic_2_IR_AAM)
        BLG_66_AC_Belouga = (7, Weapons.BLG_66_AC_Belouga)
        AS_30L = (7, WeaponsSuperEtendardClemenceau.AS_30L)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.GroundAttack,
        task.CAS,
        task.AFAC,
        task.RunwayAttack,
        task.AntishipStrike,
    ]
    task_default = task.CAP


@planemod
class ETENDARD_IV(PlaneType):
    id = "ETENDARD_IV"
    flyable = True
    height = 5.2
    width = 9.13
    length = 14.36
    fuel_max = 3165
    max_speed = 2376
    chaff = 48
    flare = 48
    charge_total = 96
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:
        class USSR(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Georgia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Venezuela(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Australia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Israel(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Combined_Joint_Task_Forces_Blue(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Sudan(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Norway(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Romania(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Iran(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Ukraine(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Libya(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Belgium(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Slovakia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Greece(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class UK(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Third_Reich(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Hungary(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Abkhazia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Morocco(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class United_Nations_Peacekeepers(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Switzerland(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class SouthOssetia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Vietnam(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class China(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Yemen(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Kuwait(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Serbia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Oman(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class India(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Egypt(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class TheNetherlands(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Poland(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Syria(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Finland(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Kazakhstan(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Denmark(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Sweden(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Croatia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class CzechRepublic(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class GDR(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Yugoslavia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Bulgaria(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class SouthKorea(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Tunisia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Combined_Joint_Task_Forces_Red(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Lebanon(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Portugal(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Cuba(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Insurgents(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class SaudiArabia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class France(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class USA(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Honduras(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Qatar(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Russia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class United_Arab_Emirates(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Italian_Social_Republi(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Austria(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Bahrain(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Italy(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Chile(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Turkey(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Philippines(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Algeria(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Pakistan(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Malaysia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Indonesia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Iraq(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Germany(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class South_Africa(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Jordan(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Mexico(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class USAFAggressors(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Brazil(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Spain(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Belarus(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Canada(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class NorthKorea(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Ethiopia(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Japan(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

        class Thailand(Enum):
            _01_Flotille11_F_CAMO_1 = "01 Flotille11-F CAMO 1"
            _02_Flotille_11F_Camo_2 = "02 Flotille 11F Camo 2"
            _03_FRANCE_MARINE = "03 FRANCE MARINE"
            _04_Marine_blue_56 = "04 Marine blue 56"
            _05_Marine_Grey_30_11F = "05 Marine Grey 30-11F"
            _06_Flotille_17F_Camo = "06 Flotille 17F Camo"
            _07_Flottille_14F = "07 Flottille 14F"
            _08_REPUBLICA_Argentina = "08 REPUBLICA Argentina"
            _09_Flotille_17f = "09 Flotille 17f"

    class Pylon1:
        GBU_12___500lb_Laser_Guided_Bomb = (1, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        # ERRR {GBU_49}
        Mk_84___2000lb_GP_Bomb_LD = (1, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Matra_Type_155_Rocket_Pod = (1, Weapons.Matra_Type_155_Rocket_Pod)
        R550_Magic_2_IR_AAM = (1, Weapons.R550_Magic_2_IR_AAM)
        BLG_66_AC_Belouga = (1, Weapons.BLG_66_AC_Belouga)
        AS_30L = (1, WeaponsSuperEtendardClemenceau.AS_30L)

    class Pylon2:
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        BLG_66_AC_Belouga = (2, Weapons.BLG_66_AC_Belouga)
        AS_30L = (2, WeaponsSuperEtendardClemenceau.AS_30L)
        Exocet = (2, WeaponsSuperEtendardClemenceau.Exocet)
        Reservoir_SEM = (2, WeaponsSuperEtendardClemenceau.Reservoir_SEM)

    # ERRR {GBU_49}

    class Pylon3:
        AUF2_BLG_66_AC_x_2 = (3, Weapons.AUF2_BLG_66_AC_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (3, Weapons.AUF2_MK_82_Snakeyes_x_2)

    class Pylon4:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            4,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )
        Mercury_LLTV_Pod = (4, Weapons.Mercury_LLTV_Pod)
        RADAR_ANEMONE = (4, WeaponsSuperEtendardClemenceau.RADAR_ANEMONE)

    class Pylon5:
        AUF2_BLG_66_AC_x_2 = (5, Weapons.AUF2_BLG_66_AC_x_2)
        AUF2_MK_82_Snakeyes_x_2 = (5, Weapons.AUF2_MK_82_Snakeyes_x_2)

    class Pylon6:
        BLG_66_AC_Belouga = (6, Weapons.BLG_66_AC_Belouga)
        AS_30L = (6, WeaponsSuperEtendardClemenceau.AS_30L)
        Exocet = (6, WeaponsSuperEtendardClemenceau.Exocet)
        Reservoir_SEM = (6, WeaponsSuperEtendardClemenceau.Reservoir_SEM)
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)

    # ERRR {GBU_49}
    # ERRR {GBU_49}

    class Pylon7:
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Matra_Type_155_Rocket_Pod = (7, Weapons.Matra_Type_155_Rocket_Pod)
        R550_Magic_2_IR_AAM = (7, Weapons.R550_Magic_2_IR_AAM)
        BLG_66_AC_Belouga = (7, Weapons.BLG_66_AC_Belouga)
        AS_30L = (7, WeaponsSuperEtendardClemenceau.AS_30L)

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.GroundAttack,
        task.CAS,
        task.AFAC,
        task.RunwayAttack,
        task.AntishipStrike,
    ]
    task_default = task.CAP


@shipmod
class Clemenceau(unittype.ShipType):
    id = "Clemenceau"
    name = "CLEMENCEAU CLASS"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 30000
    threat_range = 15000
    air_weapon_dist = 15000
