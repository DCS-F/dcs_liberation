local Cfg = {
--#################################################################################################
--
--  Liberation: API
--
--  API functions for Liberation mission.
--
--#################################################################################################
--##  CONFIGURATION START  ##  DO NOT EDIT ABOVE THIS LINE  #######################################
--#################################################################################################
    Debug = false,                                  -- Debug mode, true/false
--#################################################################################################
--##  CONFIGURATION END  ##  DO NOT EDIT BELOW THIS LINE  #########################################
--#################################################################################################
}

-- File
local LuaFile = 'stne.Liberation.API.lua'
local Version = '220215'
local FileVer = LuaFile..'/'..Version
env.info('FILE: '..FileVer..' START')

-- Override configuration
if STNE_Config_Liberation_API then
    for key, value in pairs(STNE_Config_Liberation_API) do
        Cfg[key] = value
    end
end

-- Read config table
BASE:E({FileVer,Cfg=Cfg})
local Debug = Cfg.Debug

-- Prepare global variables
if STNE == nil then STNE = {} end
if STNE.Liberation == nil then STNE.Liberation = {} end
if STNE.Liberation.API == nil then STNE.Liberation.API = {} end
if STNE.Liberation.Save == nil then STNE.Liberation.Save = {} end
if STNE.Liberation.Flags == nil then STNE.Liberation.Flags = {} end
if STNE.Liberation.EventHandler == nil then STNE.Liberation.EventHandler = {} end

-- MOOSE settings
_SETTINGS:SetPlayerMenuOff()
_SETTINGS:SetImperial()

--- API: Heading fix for unit heading
--- @param Heading number
function STNE.Liberation.API.HeadingFix(Heading)
    local Hdg
    if Heading <= 180 then
        Hdg = math.rad(Heading)
    else
        Hdg = -math.rad(360 - Heading)
    end
    return Hdg
end

--- API: Load saved data if io enabled
--- @param SaveFolder string
--- @param SaveFile string
function STNE.Liberation.API.LoadSave(SaveFolder, SaveFile)
    local Load_Data = loadfile(SaveFolder..'\\'..SaveFile)
    if Load_Data then
        Load_Data()
        if Debug then BASE:E({FileVer,SaveFile..' loaded'}) end
    end
end

--- API: Save data if io enabled
--- @param SaveFolder string
--- @param SaveFile string
--- @param SaveData string
--- @param ResetFlag number
function STNE.Liberation.API.SaveData(SaveFolder, SaveFile, SaveData, ResetFlag)
    if io then
        local ResetValue = trigger.misc.getUserFlag(ResetFlag)
        if ResetValue ~= 0 then
            SaveData = '-- Reset save data, flag: '..ResetFlag..' value: '..ResetValue
            if Debug then BASE:E({FileVer,SaveFile..' reset savedata'}) end
        end
        local Save_File = assert(io.open(SaveFolder..'\\'..SaveFile, "w"))
        if Save_File then
            Save_File:write(SaveData)
            Save_File:close()
            if Debug then BASE:E({FileVer,SaveFile..' save success'}) end
        else
            if Debug then BASE:E({FileVer,SaveFile..' save failed'}) end
        end
    else
        MESSAGE:New('INFO: SAVE OPTION DISABLED - '..SaveFile..'\nYou need to enable IO command in MissionScripting.lua to enable persistent save.', 600):ToAll()
    end
end

--- API: Find string from string
--- @param FindString string
--- @param FromString table
function STNE.Liberation.API.FindString(FindString, FromString)
    if string.find(FromString:lower(), FindString:lower()) ~= nil then
        return true
    end
    return false
end

--- API: CTLD JTAC
--- @param GroupName string
function STNE.Liberation.API.AddJTAC(GroupName)
    if ctld ~= nil and ctld.jtacGeneratedLaserCodes ~= nil then
        if STNE.Liberation.API.FindString('JTAC', GroupName) then
            local LaserCode = table.remove(ctld.jtacGeneratedLaserCodes, 1)
            table.insert(ctld.jtacGeneratedLaserCodes, LaserCode)
            ctld.JTACAutoLase(GroupName, LaserCode)
            if Debug then BASE:E({FileVer,AddJTAC=GroupName,LaserCode=LaserCode}) end
        end
    end
end

--- API: CTLD Register crate
--- @param Template string
function STNE.Liberation.API.RegisterCrate(Template)
    if ctld ~= nil then
        local CrateType = ctld.crateLookupTable[tostring(Template.units[1].mass)]
        if Template.coalitionId == 1 then
            ctld.spawnedCratesRED[Template.name] = CrateType
        else
            ctld.spawnedCratesBLUE[Template.name] = CrateType
        end
        if Debug then BASE:E({FileVer,RegisterCrate=Template.name}) end
    end
end

--- API: Convert table to string
--- @param Tbl table
function STNE.Liberation.API.TableToSave(Tbl)
    if Debug then BASE:E({FileVer,'STNE.Liberation.API.TableToSave'}) end
    local ReT = '{'
    --- Sub function for convert table to string for save
    --- @param Tbl table
    --- @param Indx number
    local function SubTableToSave(Tbl, Indx)
        local Tabs = Indx or 1
        local Tab = ''
        local SubReT = ''
        for i = 1, Tabs, 1 do
            if i <= Tabs then
                Tab = Tab..'    '
            end
        end
        for key, value in pairs(Tbl) do
            -- Keys
            if type(key) == 'number' then
                key = '\n'..Tab..'['..tostring(key)..'] = '
            elseif type(key) == 'string' then
                key = "\n"..Tab..'["'..tostring(key)..'"] = '
            end
            -- Values
            if type(value) == 'string' then
                value = '"'..tostring(value)..'",'
            elseif type(value) == 'number' then
                value = tostring(value)..','
            elseif type(value) == 'boolean' then
                value = tostring(value)..','
            elseif type(value) == 'function' then
                value = nil --value = 'f(),'
            elseif type(value) == 'table' then
                value = '{'..tostring(SubTableToSave(value, Tabs + 1))..'\n'..Tab..'},'
            else
                value = nil
            end
            if value ~= nil then
                SubReT = SubReT..key..tostring(value)
            end
        end
        return tostring(SubReT)
    end
    local SubReT = SubTableToSave(Tbl)
    ReT = ReT..SubReT..'\n}'
    return tostring(ReT)
end

-- EOF
env.info('FILE: '..FileVer..' END')