local Cfg = {
--#################################################################################################
--
--  Liberation: SaveStatics
--
--  Persistent save for statics.
--
--#################################################################################################
--##  CONFIGURATION START  ##  DO NOT EDIT ABOVE THIS LINE  #######################################
--#################################################################################################
    Debug = false,                                  -- Debug mode, true/false
    Folder = 'C:\\DCS_save\\Liberation\\Stne.Liberation.Save', -- Save folder, drive:\\folder\\folder
    File = 'SaveData.Statics.lua',                  -- Save file name
    Timer = 60,                                     -- Save scheduler, in seconds. 0 = save only when mission end
    Prefix = {                                      -- STATIC prefixes, save only these statics
        'CTLD|',
    },
    ResetFlag = 667,                                -- Flag to reset save data
--#################################################################################################
--##  CONFIGURATION END  ##  DO NOT EDIT BELOW THIS LINE  #########################################
--#################################################################################################
}

-- File
local LuaFile = 'stne.Liberation.SaveStatics.lua'
local Version = '220215'
local FileVer = LuaFile..'/'..Version
env.info('FILE: '..FileVer..' START')

-- Override configuration
if STNE_Config_Liberation_SaveStatics then
    for key, value in pairs(STNE_Config_Liberation_SaveStatics) do
        Cfg[key] = value
    end
end

-- Read config table
BASE:E({FileVer,Cfg=Cfg})
local Debug = Cfg.Debug
local SaveFolder = Cfg.Folder
local SaveFile = Cfg.File
local SaveTimer = Cfg.Timer
local PrefixNames = Cfg.Prefix
local ResetFlag = Cfg.ResetFlag

-- Load save
STNE.Liberation.API.LoadSave(SaveFolder, SaveFile)

-- Process savedata
if STNE.Liberation.Save.Statics ~= nil then
    for _, Template in pairs(STNE.Liberation.Save.Statics) do
        if Debug then BASE:E({FileVer,dynAddStatic=Template.name}) end
        mist.dynAddStatic(Template)
        STNE.Liberation.API.RegisterCrate(Template)
        _DATABASE:AddStatic(Template.name)
    end
end

--- Prepare statics data for save
local function PrepareStatics()
    STNE.Liberation.Save.Statics = {}
    for _, Template in pairs(mist.DBs.dynGroupsAdded) do
        if Template.category == 'static' then
            if STATIC:FindByName(Template.name, false) == nil then
                _DATABASE:AddStatic(Template.name)
            end
        end
    end
    local Set_Static = SET_STATIC:New()
    Set_Static:FilterPrefixes(PrefixNames)
    Set_Static:FilterOnce()
    Set_Static:ForEachStatic(
        function(StaticObj)
            if StaticObj and StaticObj:IsAlive() then
                local StaticName = StaticObj:GetName()
                local StaticTemplate = mist.getGroupData(StaticName)
                if StaticTemplate then
                    local Coord = StaticObj:GetCoordinate()
                    StaticTemplate['units'][1].alt = Coord.y
                    StaticTemplate['units'][1].x = Coord.x
                    StaticTemplate['units'][1].y = Coord.z
                    local Heading = StaticObj:GetHeading()
                    StaticTemplate['units'][1].heading = STNE.Liberation.API.HeadingFix(Heading)
                    table.insert(STNE.Liberation.Save.Statics, StaticTemplate)
                end
            end
        end
    )
    if Debug then BASE:E({FileVer,PrepareStatics=#STNE.Liberation.Save.Statics}) end
end

--- Save data to file
local function SaveDataToFile()
    -- Prepare static data for save
    PrepareStatics()
    -- Save data
    local SaveData = "STNE.Liberation.Save.Statics = "
    SaveData = SaveData..STNE.Liberation.API.TableToSave(STNE.Liberation.Save.Statics)
    STNE.Liberation.API.SaveData(SaveFolder, SaveFile, SaveData, ResetFlag)
end

-- End mission & land eventhandler for save data
if STNE.Liberation.EventHandler == nil then STNE.Liberation.EventHandler = {} end
if STNE.Liberation.EventHandler.Save == nil then STNE.Liberation.EventHandler.Save = {} end
STNE.Liberation.EventHandler.Save.Statics = EVENTHANDLER:New()
STNE.Liberation.EventHandler.Save.Statics:HandleEvent(world.event.S_EVENT_MISSION_END)
-- OnEventMissionEnd
function STNE.Liberation.EventHandler.Save.Statics:OnEventMissionEnd(EventData)
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