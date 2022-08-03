local Cfg = {
--#################################################################################################
--
--  Liberation: SaveGroups
--
--  Persistent save for groups.
--
--#################################################################################################
--##  CONFIGURATION START  ##  DO NOT EDIT ABOVE THIS LINE  #######################################
--#################################################################################################
    Debug = false,                                  -- Debug mode, true/false
    Folder = 'C:\\DCS_save\\Liberation\\Stne.Liberation.Save', -- Save folder, drive:\\folder\\folder
    File = 'SaveData.Groups.lua',                   -- Save file name
    Timer = 60,                                     -- Save scheduler, in seconds. 0 = save only when mission end
    Prefix = {                                      -- GROUP prefixes, save only these groups
        'CTLD|',
    },
    ResetFlag = 667,                                -- Flag to reset save data
--#################################################################################################
--##  CONFIGURATION END  ##  DO NOT EDIT BELOW THIS LINE  #########################################
--#################################################################################################
}

-- File
local LuaFile = 'stne.Liberation.SaveGroups.lua'
local Version = '20220215'
local FileVer = LuaFile..'/'..Version
env.info('FILE: '..FileVer..' START')

-- Override configuration
if STNE_Config_Liberation_SaveGroups then
    for key, value in pairs(STNE_Config_Liberation_SaveGroups) do
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
if STNE.Liberation.Save.Groups ~= nil then
    for _, Template in pairs(STNE.Liberation.Save.Groups) do
        if Debug then BASE:E({FileVer,dynAdd=Template.name}) end
        mist.dynAdd(Template)
        STNE.Liberation.API.AddJTAC(Template.name)
    end
end

--- Prepare groups data for save
local function PrepareGroups()
    STNE.Liberation.Save.Groups = {}
    local Set_Group = SET_GROUP:New()
    Set_Group:FilterPrefixes(PrefixNames)
    Set_Group:FilterOnce()
    Set_Group:ForEachGroupAlive(
        function(GroupObj)
            local GroupName = GroupObj:GetName()
            local GroupTemplate = mist.getGroupData(GroupName)
            if GroupTemplate then
                local UnitsNew = {}
                for _, UnitTemplate in ipairs(GroupTemplate.units) do
                    local UnitObj = UNIT:FindByName(UnitTemplate.unitName)
                    if UnitObj and UnitObj:IsAlive() then
                        local Coord = UnitObj:GetCoordinate()
                        UnitTemplate.alt = Coord.y
                        UnitTemplate.x = Coord.x
                        UnitTemplate.y = Coord.z
                        local Heading = UnitObj:GetHeading()
                        UnitTemplate.heading = STNE.Liberation.API.HeadingFix(Heading)

                        if UnitTemplate.type == "BTR-80" then
                            UnitTemplate.livery_id = "Green summer"
                        elseif UnitTemplate.type == "BTR-82A" then
                            UnitTemplate.livery_id = "Green summer"
                        elseif UnitTemplate.type == "VAB_Mephisto" then
                            UnitTemplate.livery_id = "woodland_Spring"
                        end

                        table.insert(UnitsNew, UnitTemplate)
                    end
                end
                GroupTemplate.units = UnitsNew
                table.insert(STNE.Liberation.Save.Groups, GroupTemplate)
            end
        end
    )
    if Debug then BASE:E({FileVer,PrepareGroups=#STNE.Liberation.Save.Groups}) end
end

--- Save data to file
local function SaveDataToFile()
    -- Prepare group data for save
    PrepareGroups()
    -- Save data
    local SaveData = "STNE.Liberation.Save.Groups = "
    SaveData = SaveData..STNE.Liberation.API.TableToSave(STNE.Liberation.Save.Groups)
    STNE.Liberation.API.SaveData(SaveFolder, SaveFile, SaveData, ResetFlag)
end

-- End mission & land eventhandler for save data
if STNE.Liberation.EventHandler == nil then STNE.Liberation.EventHandler = {} end
if STNE.Liberation.EventHandler.Save == nil then STNE.Liberation.EventHandler.Save = {} end
STNE.Liberation.EventHandler.Save.Groups = EVENTHANDLER:New()
STNE.Liberation.EventHandler.Save.Groups:HandleEvent(world.event.S_EVENT_MISSION_END)
-- OnEventMissionEnd
function STNE.Liberation.EventHandler.Save.Groups:OnEventMissionEnd(EventData)
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