local FileVer = 'stne.Config.lua/210421'
env.info('FILE: '..FileVer..' START')
--#################################################################################################
--
--  Config
--
--  Override local configuration settings.
--
--  Usage: (check drive:/folder, load before other lua files)
--
--      MISSION EDITOR -> TRIGGERS -> MISSION START -> DO SCRIPT ->
--
--          assert(loadfile('C:/Folder/stne.Config.lua'))()
--
--  or copy global variables of your choice with your custom settings: (load before lua file)
--
--      MISSION EDITOR -> TRIGGERS -> MISSION START -> DO SCRIPT ->
--
--          STNE_Config_EndMission = {
--              End_Flag = 666,
--              Mission_Time = 3600,
--              Warnings = {900, 600, 300, 60, 30},
--          }
--
--#################################################################################################
--##  CONFIGURATION START  ##  DO NOT EDIT ABOVE THIS LINE  #######################################
--#################################################################################################
STNE_Config_LuaLoader = {                               -- stne.LuaLoader.lua
    Folder = 'C:/DCS_save/Stone-scripts',                  -- Folder
    Scripts = {                                         -- Lua scripts, check proper loading order

        --'Skynet/mist_4_4_90.lua',
        --'Moose.lua',
        'Moose.lua',
        --'Skynet/skynet-iads-compiled.lua',
        --'Skynet/stne.SimpleSkynetSetup.lua',
        --'GitHub/Moose/stne.MooseSettings.lua',
        --'GitHub/API/stne.API.lua',

        'GitHub/Liberation/stne.Liberation.API.lua',
        'GitHub/Liberation/stne.Liberation.SaveGroups.lua',
        'GitHub/Liberation/stne.Liberation.SaveStatics.lua',
        'GitHub/Liberation/stne.Liberation.SaveTables.lua',

        --'GitHub/Mission/stne.MissionEnd.lua',
        --'GitHub/Mission/stne.GroupCache.lua',
        --'GitHub/Mission/stne.Statistics.lua',
        --'GitHub/Mission/stne.ParkingData.lua',


        --'GitHub/Save/stne.SaveGroups.lua',
        --'GitHub/Save/stne.SaveStatics.lua',
        --'GitHub/Save/stne.SaveFlags.lua',
        --'GitHub/Save/stne.SaveTables.lua',

        --'GitHub/Operation/stne.CarrierRecovery.lua',
        --'GitHub/Operation/stne.CSAR.lua',
        --'GitHub/Operation/stne.SceneryDestruction.lua',
        --'GitHub/Operation/stne.SimpleArtillery.lua',
        --'GitHub/Operation/stne.SlingloadLogistic.lua',
        --'GitHub/Operation/stne.RandomTraffic.lua',
        --'GitHub/Operation/stne.OperationFlagsMarkers.lua',
        --'GitHub/Operation/stne.RadioStation.lua',
        --'GitHub/Operation/stne.Intel.lua',
        --'GitHub/Operation/stne.OperationAssets.lua',
        --'GitHub/Operation/stne.OperationMissions.lua',
        --'GitHub/Operation/stne.SimplePilotRecovery.lua',

        --'GitHub/Training/stne.MissileTrainer.lua',
        --'GitHub/Training/stne.TargetRange.lua',

        --'GitHub/Utils/stne.Utils.lua',
        --'GitHub/Utils/stne.Ziili.lua',
        'GitHub/Utils/stne.MissionTools.lua',

        --'GitHub/SyriaTrap/stne.SyriaTrap.lua',
        --'GitHub/SyriaTrap/stne.SyriaTrapFSM.lua',

        --'Test/TestCode.lua',
        --'Test/stne.RadioMenus.lua',

        --'Unfinished/stne.Warehouse.lua',
        --'Unfinished/stne.WarehouseLog.lua',
        --'Unfinished/stne.WarehouseCmd.lua',
        --'Unfinished/stne.WarehouseFSM.lua',
        --'Unfinished/stne.WarehouseAir.lua',
        --'Unfinished/stne.WarehouseGrpSave.lua', -- Check _AID in alias name error ? WAREHOUSE:_OnEventBirth
        --'Unfinished/stne.SimpleZoneWars.lua',
        --'Unfinished/stne.AirRace.lua',
        --'Unfinished/stne.Mantis.lua',

    },
}
--#################################################################################################
--##  CONFIGURATION END  ##  DO NOT EDIT BELOW THIS LINE  #########################################
--#################################################################################################
env.info('FILE: '..FileVer..' END')