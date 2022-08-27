from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod


@planemod
class VSN_TornadoIDS(PlaneType):
    id = "VSN_TornadoIDS"
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

    class Liveries:
        class USSR(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Georgia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Venezuela(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Australia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Israel(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Combined_Joint_Task_Forces_Blue(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Sudan(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Norway(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Romania(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Iran(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Ukraine(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Libya(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Belgium(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Slovakia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Greece(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class UK(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Third_Reich(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Hungary(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Abkhazia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Morocco(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class United_Nations_Peacekeepers(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Switzerland(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class SouthOssetia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Vietnam(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class China(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Yemen(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Kuwait(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Serbia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Oman(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class India(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Egypt(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class TheNetherlands(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Poland(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Syria(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Finland(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Kazakhstan(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Denmark(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Sweden(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Croatia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class CzechRepublic(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class GDR(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Yugoslavia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Bulgaria(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class SouthKorea(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Tunisia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Combined_Joint_Task_Forces_Red(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Lebanon(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Portugal(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Cuba(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Insurgents(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class SaudiArabia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class France(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class USA(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Honduras(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Qatar(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Russia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class United_Arab_Emirates(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Italian_Social_Republi(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Austria(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Bahrain(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Italy(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Chile(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Turkey(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Philippines(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Algeria(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Pakistan(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Malaysia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Indonesia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Iraq(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Germany(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class South_Africa(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Jordan(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Mexico(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class USAFAggressors(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Brazil(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Spain(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Belarus(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Canada(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class NorthKorea(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Ethiopia(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Japan(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

        class Thailand(Enum):
            aufklarungsgeschwader_51__immelmann__jagel_ab_luftwaffe = (
                "aufklarungsgeschwader 51 `immelmann` jagel ab luftwaffe"
            )
            jagdbombergeschwader_31__boelcke__norvenich_ab_luftwaffe = (
                "jagdbombergeschwader 31 `boelcke` norvenich ab luftwaffe"
            )
            jagdbombergeschwader_32_lechfeld_ab_luftwaffe = (
                "jagdbombergeschwader 32 lechfeld ab luftwaffe"
            )
            jagdbombergeschwader_33_buchel_ab_no__43_19_experimental_scheme = (
                "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme"
            )
            marinefliegergeschwader_2_eggebek_ab_marineflieger = (
                "marinefliegergeschwader 2 eggebek ab marineflieger"
            )

    class Pylon1:
        BOZ_107___Countermeasure_Dispenser = (
            1,
            Weapons.BOZ_107___Countermeasure_Dispenser,
        )
        Sky_Shadow_ECM_Pod = (1, Weapons.Sky_Shadow_ECM_Pod)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)

    class Pylon2:
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            2,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        Kormoran___ASM = (2, Weapons.Kormoran___ASM)
        TORNADO_Fuel_tank = (2, Weapons.TORNADO_Fuel_tank)

    class Pylon3:
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon4:
        GBU_16___1000lb_Laser_Guided_Bomb = (
            4,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            4,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        Kormoran___ASM = (4, Weapons.Kormoran___ASM)

    class Pylon5:
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        L_081_Fantasmagoria_ELINT_pod = (6, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon7:
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon8:
        GBU_16___1000lb_Laser_Guided_Bomb = (
            8,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            8,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        Kormoran___ASM = (8, Weapons.Kormoran___ASM)

    class Pylon9:
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon10:
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            10,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        Kormoran___ASM = (10, Weapons.Kormoran___ASM)
        TORNADO_Fuel_tank = (10, Weapons.TORNADO_Fuel_tank)

    class Pylon11:
        BOZ_107___Countermeasure_Dispenser = (
            11,
            Weapons.BOZ_107___Countermeasure_Dispenser,
        )
        Sky_Shadow_ECM_Pod = (11, Weapons.Sky_Shadow_ECM_Pod)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [
        task.Reconnaissance,
        task.GroundAttack,
        task.AFAC,
        task.AntishipStrike,
        task.PinpointStrike,
        task.SEAD,
    ]
    task_default = task.GroundAttack


@planemod
class VSN_TornadoGR4(PlaneType):
    id = "VSN_TornadoGR4"
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

    class Liveries:
        class USSR(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Georgia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Venezuela(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Australia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Israel(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Combined_Joint_Task_Forces_Blue(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Sudan(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Norway(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Romania(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Iran(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Ukraine(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Libya(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Belgium(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Slovakia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Greece(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class UK(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Third_Reich(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Hungary(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Abkhazia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Morocco(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class United_Nations_Peacekeepers(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Switzerland(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class SouthOssetia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Vietnam(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class China(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Yemen(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Kuwait(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Serbia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Oman(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class India(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Egypt(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class TheNetherlands(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Poland(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Syria(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Finland(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Kazakhstan(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Denmark(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Sweden(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Croatia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class CzechRepublic(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class GDR(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Yugoslavia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Bulgaria(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class SouthKorea(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Tunisia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Combined_Joint_Task_Forces_Red(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Lebanon(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Portugal(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Cuba(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Insurgents(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class SaudiArabia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class France(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class USA(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Honduras(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Qatar(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Russia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class United_Arab_Emirates(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Italian_Social_Republi(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Austria(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Bahrain(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Italy(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Chile(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Turkey(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Philippines(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Algeria(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Pakistan(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Malaysia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Indonesia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Iraq(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Germany(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class South_Africa(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Jordan(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Mexico(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class USAFAggressors(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Brazil(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Spain(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Belarus(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Canada(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class NorthKorea(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Ethiopia(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Japan(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

        class Thailand(Enum):
            bb_of_14_squadron_raf_lossiemouth = "bb of 14 squadron raf lossiemouth"
            no__12_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 12 squadron raf lossiemouth ab (morayshire)"
            )
            no__14_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 14 squadron raf lossiemouth ab (morayshire)"
            )
            no__617_squadron_raf_lossiemouth_ab__morayshire = (
                "no. 617 squadron raf lossiemouth ab (morayshire)"
            )
            no__9_squadron_raf_marham_ab__norfolk = (
                "no. 9 squadron raf marham ab (norfolk)"
            )
            o_of_ii__ac__squadron_raf_marham = "o of ii (ac) squadron raf marham"

    class Pylon1:
        BOZ_107___Countermeasure_Dispenser = (
            1,
            Weapons.BOZ_107___Countermeasure_Dispenser,
        )
        Sky_Shadow_ECM_Pod = (1, Weapons.Sky_Shadow_ECM_Pod)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)

    class Pylon2:
        TORNADO_Fuel_tank = (2, Weapons.TORNADO_Fuel_tank)

    class Pylon3:
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        ALARM = (3, Weapons.ALARM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon4:
        GBU_16___1000lb_Laser_Guided_Bomb = (
            4,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        ALARM = (4, Weapons.ALARM)
        Sea_Eagle___ASM = (4, Weapons.Sea_Eagle___ASM)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            4,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )

    class Pylon5:
        GBU_12___500lb_Laser_Guided_Bomb = (5, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        AN_AAQ_28_LITENING___Targeting_Pod = (
            5,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )

    class Pylon6:
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        L_081_Fantasmagoria_ELINT_pod = (6, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon7:
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)

    class Pylon8:
        GBU_16___1000lb_Laser_Guided_Bomb = (
            8,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        ALARM = (8, Weapons.ALARM)
        Sea_Eagle___ASM = (8, Weapons.Sea_Eagle___ASM)
        GBU_27___2000lb_Laser_Guided_Penetrator_Bomb = (
            8,
            Weapons.GBU_27___2000lb_Laser_Guided_Penetrator_Bomb,
        )

    class Pylon9:
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        ALARM = (9, Weapons.ALARM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon10:
        TORNADO_Fuel_tank = (10, Weapons.TORNADO_Fuel_tank)

    class Pylon11:
        BOZ_107___Countermeasure_Dispenser = (
            11,
            Weapons.BOZ_107___Countermeasure_Dispenser,
        )
        Sky_Shadow_ECM_Pod = (11, Weapons.Sky_Shadow_ECM_Pod)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [
        task.Reconnaissance,
        task.GroundAttack,
        task.AFAC,
        task.AntishipStrike,
        task.PinpointStrike,
        task.SEAD,
    ]
    task_default = task.GroundAttack
