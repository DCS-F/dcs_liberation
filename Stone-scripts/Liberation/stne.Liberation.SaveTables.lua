local Cfg = {
--#################################################################################################
--
--  Liberation: SaveTables
--
--  Persistent save for lua tables with CTLD support.
--
--#################################################################################################
--##  CONFIGURATION START  ##  DO NOT EDIT ABOVE THIS LINE  #######################################
--#################################################################################################
    Debug = false,                                  -- Debug mode, true/false
    Folder = 'C:\\DCS_save\\Liberation\\Stne.Liberation.Save', -- Save folder, drive:\\folder\\folder
    File = 'SaveData.Tables.lua',                   -- Save file name
    Timer = 60,                                     -- Save scheduler, in seconds. 0 = save only when mission end
    ResetFlag = 667,                                -- Flag to reset save data
--#################################################################################################
--##  CONFIGURATION END  ##  DO NOT EDIT BELOW THIS LINE  #########################################
--#################################################################################################
}

-- File
local LuaFile = 'stne.Liberation.SaveTables.lua'
local Version = '220215'
local FileVer = LuaFile..'/'..Version
env.info('FILE: '..FileVer..' START')

-- Override configuration
if STNE_Config_Liberation_SaveTables then
    for key, value in pairs(STNE_Config_Liberation_SaveTables) do
        Cfg[key] = value
    end
end

-- Read config table
BASE:E({FileVer,Cfg=Cfg})
local Debug = Cfg.Debug
local SaveFolder = Cfg.Folder
local SaveFile = Cfg.File
local SaveTimer = Cfg.Timer
local ResetFlag = Cfg.ResetFlag

-- Load save
STNE.Liberation.API.LoadSave(SaveFolder, SaveFile)

-- Process savedata
if STNE.Liberation.Save.Tables ~= nil then
    for TableName, TableData in pairs(STNE.Liberation.Save.Tables) do
        if Debug then BASE:E({FileVer,Name=TableName,Data=TableData}) end
        if TableName == 'ctld' then
            for key, value in pairs(TableData) do
                ctld[key] = value
            end
        end
    end
end

--- Save data to file
local function SaveDataToFile()
    -- Prepare table
    if STNE.Liberation.Save.Tables == nil then STNE.Liberation.Save.Tables = {} end
    if ctld ~= nil then
        STNE.Liberation.Save.Tables.ctld = {
            droppedTroopsRED = ctld.droppedTroopsRED,
            droppedTroopsBLUE = ctld.droppedTroopsBLUE,
            droppedVehiclesRED = ctld.droppedVehiclesRED,
            droppedVehiclesBLUE = ctld.droppedVehiclesBLUE,
            droppedFOBCratesRED = ctld.droppedFOBCratesRED,
            droppedFOBCratesBLUE = ctld.droppedFOBCratesBLUE,
        }
    end
    -- Save data
    local SaveData = "STNE.Liberation.Save.Tables = "
    SaveData = SaveData..STNE.Liberation.API.TableToSave(STNE.Liberation.Save.Tables)
    STNE.Liberation.API.SaveData(SaveFolder, SaveFile, SaveData, ResetFlag)
end

-- End mission eventhandler for save data
if STNE.EventHandler == nil then STNE.EventHandler = {} end
if STNE.EventHandler.Save == nil then STNE.EventHandler.Save = {} end
STNE.EventHandler.Save.Tables = EVENTHANDLER:New()
STNE.EventHandler.Save.Tables:HandleEvent(world.event.S_EVENT_MISSION_END)
-- On mission end event
function STNE.EventHandler.Save.Tables:OnEventMissionEnd(EventData)
    SaveDataToFile()
end

-- Scheduler
if SaveTimer > 0 then
    if Debug then BASE:E({FileVer,Scheduler='enabled'}) end
    SCHEDULER:New(nil, function()
        SaveDataToFile()
    end, {}, SaveTimer, SaveTimer)
else
    if Debug then BASE:E({FileVer,Scheduler='disabled'}) end
end

-- EOF
env.info('FILE: '..FileVer..' END')