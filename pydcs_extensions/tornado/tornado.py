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

    livery_name = "VSN_TornadoIDS"  # from type

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

    livery_name = "VSN_TornadoGR4"  # from type

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
