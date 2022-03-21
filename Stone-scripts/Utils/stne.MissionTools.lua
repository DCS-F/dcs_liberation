local Cfg = {
--#################################################################################################
--
--  MissionTools
--
--  Admin tools for mission environment
--
--  https://flightcontrol-master.github.io/MOOSE_DOCS_DEVELOP/Documentation/
--
--#################################################################################################
--##  CONFIGURATION START  ##  DO NOT EDIT ABOVE THIS LINE  #######################################
--#################################################################################################
    Debug = true,                                   -- Debug mode, true/false
    Command = '-MissionTools',                      -- Magic command
--#################################################################################################
--##  CONFIGURATION END  ##  DO NOT EDIT BELOW THIS LINE  #########################################
--#################################################################################################
}

-- File
local LuaFile = 'stne.MissionTools.lua'
local Version = '210421'
local FileVer = LuaFile..'/'..Version
env.info('FILE: '..FileVer..' START')

-- Override configuration
if STNE_Config_MissionTools then
    for key, value in pairs(STNE_Config_MissionTools) do
        Cfg[key] = value
    end
end

-- Read config table
BASE:E({FileVer,Cfg=Cfg})
local Debug = Cfg.Debug
local Command = Cfg.Command

-- Spawned table
local SpawnedTable = {}

-- Eventhandler
if STNE == nil then STNE = {} end
if STNE.EventHandler == nil then STNE.EventHandler = {} end
if STNE.EventHandler.MissionTools == nil then STNE.EventHandler.MissionTools = {} end
STNE.EventHandler.MissionTools = EVENTHANDLER:New()
STNE.EventHandler.MissionTools:HandleEvent(world.event.S_EVENT_MARK_REMOVED)

--- Get data type from string
--- @param Value string
local function GetDataType(Value)
    local ValueObj = Value
    local ValueType = 'STRING'
    if tonumber(Value) then
        ValueObj = tonumber(Value)
        ValueType = 'NUMBER'
    elseif GROUP:FindByName(Value) ~= nil then
        ValueObj = GROUP:FindByName(Value)
        ValueType = 'GROUP'
    elseif UNIT:FindByName(Value) ~= nil then
        ValueObj = UNIT:FindByName(Value)
        ValueType = 'UNIT'
    elseif STATIC:FindByName(Value, false) ~= nil then
        ValueObj = STATIC:FindByName(Value, false)
        ValueType = 'STATIC'
    elseif AIRBASE:FindByName(Value) then
        ValueObj = AIRBASE:FindByName(Value)
        ValueType = 'AIRBASE'
    end
    if Debug then BASE:E({FileVer,Value=Value,ValueType=ValueType}) end
    return ValueObj, ValueType
end

--- Split string and get data
--- @param DataString string
local function GetDataFromString(DataString)
    local _DataString = DataString or ''
    local DataTable = UTILS.Split(_DataString, ',')
    local ReturnTable = {
        STRING = {},
        NUMBER = {},
        GROUP = {},
        UNIT = {},
        STATIC = {},
        AIRBASE = {},
    }
    for _, Value in pairs(DataTable) do
        local ValueObj, ValueType = GetDataType(Value)
        table.insert(ReturnTable[ValueType], ValueObj)
    end
    return ReturnTable
end

--- Get simple table from tables
--- @param Tables table
local function GetSimpleTable(Tables)
    local ObjectTable = {}
    for _, Table in pairs(Tables) do
        for _, Obj in pairs(Table) do
            table.insert(ObjectTable, Obj)
        end
    end
    return ObjectTable
end

--- Convert coordinate to string
--- @param Coord table
local function CoordToString(Coord)
    local CoordString = '{[y]='..Coord.y..',[x]='..Coord.x..',[z]='..Coord.z..',}'
    return CoordString
end

--- Find safe spawn index
--- @param ObjectName string
local function SafeSpawnIndex(ObjectName)
    local Idx = 1
    while GROUP:FindByName(ObjectName..'#'..Idx) ~= nil or GROUP:FindByName(ObjectName..'#0'..Idx) ~= nil or GROUP:FindByName(ObjectName..'#00'..Idx) ~= nil or STATIC:FindByName(ObjectName..'#'..Idx, false) ~= nil do
        if Debug then BASE:E({FileVer,'SafeSpawnName',AlreadyExist=ObjectName,Index=Idx}) end
        Idx = Idx + 1
    end
    return Idx
end

--- Command: explosion
--- @param Coord table
--- @param CmdData table
local function CmdExplosion(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local Force = DataTable['NUMBER'][1] or 1000
    local Object = DataTable['GROUP'][1] or DataTable['UNIT'][1] or DataTable['STATIC'][1] or nil
    if Object then
        local ObjectTable = GetSimpleTable({DataTable['GROUP'], DataTable['UNIT'], DataTable['STATIC']})
        for _, Obj in pairs(ObjectTable) do
            if Obj ~= nil and Obj:IsAlive() then
                local ObjCoord = Obj:GetCoordinate()
                ObjCoord:Explosion(Force)
                if Debug then BASE:E({FileVer,'CmdExplosion',Force=Force,Object=Obj:GetName(),Coordinate=CoordToString(ObjCoord)}) end
            end
        end
    else
        Coord:Explosion(Force)
        if Debug then BASE:E({FileVer,'CmdExplosion',Force=Force,Coordinate=CoordToString(Coord)}) end
    end
end

--- Command: flag
--- @param Coord table
--- @param CmdData table
local function CmdFlag(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local Flag = DataTable['STRING'][1] or DataTable['NUMBER'][1] or nil
    local FlagValue = nil
    if Flag then
        if type(Flag) == 'number' then
            FlagValue = DataTable['NUMBER'][2] or nil
        else
            FlagValue = DataTable['NUMBER'][1] or nil
        end
        if FlagValue then
            trigger.action.setUserFlag(Flag, FlagValue)
        else
            if not Debug then BASE:E({FileVer,Flag=Flag,Value=trigger.misc.getUserFlag(Flag)}) end
        end
    end
    if Debug then BASE:E({FileVer,'CmdFlag',Flag=Flag,Value=FlagValue}) end
end

--- Command: spawn
--- @param Coord table
--- @param CmdData table
local function CmdSpawn(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local Number1 = DataTable['NUMBER'][1] or nil
    local Number2 = DataTable['NUMBER'][2] or nil
    local Heading = nil
    local Altitude = nil
    if Number1 ~= nil and Number1 >= 0 and Number1 < 360 then Heading = Number1 end
    if Number2 ~= nil and Number2 >= 0 and Number2 < 360 then Heading = Number2 end
    if Number1 ~= nil and Number1 >= 360 then Altitude = Number1 end
    if Number2 ~= nil and Number2 >= 360 then Altitude = Number2 end
    local ObjectGroup = DataTable['GROUP'][1] or nil
    local ObjectStatic = DataTable['STATIC'][1] or nil
    -- GROUP
    if ObjectGroup then
        local ObjectName = ObjectGroup:GetName()
        local SpawnObj = SPAWN:NewWithAlias(ObjectName, ObjectName)
        local Idx = SafeSpawnIndex(ObjectName) - 1
        SpawnObj.SpawnIndex = Idx
        SpawnObj.SpawnCount = Idx
        SpawnObj:OnSpawnGroup(
            function(GroupObj)
                table.insert(SpawnedTable, GroupObj)
                if Heading and GroupObj:IsAir() then
                    local WPCoord = GroupObj:GetCoordinate():Translate(UTILS.NMToMeters(50), GroupObj:GetHeading())
                    local Speed = GroupObj:GetSpeedMax() * 0.8
                    if Speed > 1000 then
                        Speed = 1000
                    end
                    if Altitude then
                        WPCoord.y = UTILS.FeetToMeters(Altitude)
                    else
                        WPCoord.y = GroupObj:GetHeight()
                    end
                    GroupObj:RouteAirTo(WPCoord, 'BARO', nil, nil, Speed, nil)
                end
                -- SaveGroups support
                if STNE ~= nil and STNE.API ~= nil and STNE.API.InitGroupForSaveCache ~= nil then
                    --STNE.API.InitGroupForSave(GroupObj, ObjectName)
                    STNE.API.InitGroupForSaveCache(GroupObj, ObjectName, nil)
                end
            end
        )
        if Heading then
            SpawnObj:InitHeading(Heading)
        end
        if Altitude and ObjectGroup:IsAir() then
            local SpawnHeight = UTILS.FeetToMeters(Altitude)
            SpawnObj:SpawnFromVec2(Coord:GetVec2(), SpawnHeight, SpawnHeight)
        else
            SpawnObj:SpawnFromVec2(Coord:GetVec2())
        end
    end
    -- STATIC
    if ObjectStatic then
        local ObjectName = ObjectStatic:GetName()
        if Heading == nil then
            Heading = ObjectStatic:GetHeading()
        end
        local SpawnObj = SPAWNSTATIC:NewFromStatic(ObjectName)
        local Idx = SafeSpawnIndex(ObjectName)
        SpawnObj:SpawnFromCoordinate(Coord, Heading, ObjectName..'#'..Idx)
    end
    if Debug then BASE:E({FileVer,'CmdSpawn',ObjectGroup=ObjectGroup,ObjectStatic=ObjectStatic,SpawnedTable=#SpawnedTable}) end
end

--- Command: destroy
--- @param Coord table
--- @param CmdData table
local function CmdDestroy(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local Object = DataTable['GROUP'][1] or DataTable['UNIT'][1] or DataTable['STATIC'][1] or nil
    local TextCmd = DataTable['STRING'][1] or nil
    if Object then
        local ObjectTable = GetSimpleTable({DataTable['GROUP'], DataTable['UNIT'], DataTable['STATIC']})
        for _, Obj in pairs(ObjectTable) do
            if Obj ~= nil and Obj:IsAlive() then
                if Debug then BASE:E({FileVer,'CmdDestroy',Object=Obj:GetName(),Coordinate=CoordToString(Obj:GetCoordinate())}) end
                Obj:Destroy(false)
            end
        end
    end
    if TextCmd == 'last' then
        if #SpawnedTable >= 1 then
            local Obj = SpawnedTable[#SpawnedTable]
            if Debug then BASE:E({FileVer,'CmdDestroy',Object=Obj:GetName(),Coordinate=CoordToString(Obj:GetCoordinate())}) end
            Obj:Destroy(false)
            table.remove(SpawnedTable)
        end
    elseif TextCmd == 'all' then
        for _, Obj in pairs(SpawnedTable) do
            if Debug then BASE:E({FileVer,'CmdDestroy',Object=Obj:GetName(),Coordinate=CoordToString(Obj:GetCoordinate())}) end
            Obj:Destroy(false)
        end
        SpawnedTable = {}
    end
end

--- Command: flare
--- @param Coord table
--- @param CmdData table
local function CmdFlare(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local Object = DataTable['GROUP'][1] or DataTable['UNIT'][1] or DataTable['STATIC'][1] or nil
    local TextCmd = DataTable['STRING'][1] or nil
    local Color = FLARECOLOR.White
    if TextCmd then
        if TextCmd == 'yellow' then
            Color = FLARECOLOR.Yellow
        elseif TextCmd == 'green' then
            Color = FLARECOLOR.Green
        elseif TextCmd == 'red' then
            Color = FLARECOLOR.Red
        end
    end
    if Object then
        local ObjectTable = GetSimpleTable({DataTable['GROUP'], DataTable['UNIT'], DataTable['STATIC']})
        for _, Obj in pairs(ObjectTable) do
            if Obj ~= nil and Obj:IsAlive() then
                if Debug then BASE:E({FileVer,'CmdFlare',Color=Color,Object=Obj:GetName(),Coordinate=CoordToString(Obj:GetCoordinate())}) end
                Obj:GetCoordinate():Flare(Color, math.random(0,359))
            end
        end
    else
        Coord:Flare(Color, math.random(0,359))
        if Debug then BASE:E({FileVer,'CmdFlare',Color=Color,Coordinate=CoordToString(Coord)}) end
    end
end

--- Command: smoke
--- @param Coord table
--- @param CmdData table
local function CmdSmoke(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local Object = DataTable['GROUP'][1] or DataTable['UNIT'][1] or DataTable['STATIC'][1] or nil
    local TextCmd = DataTable['STRING'][1] or nil
    local Color = SMOKECOLOR.White
    if TextCmd then
        if TextCmd == 'green' then
            Color = SMOKECOLOR.Green
        elseif TextCmd == 'red' then
            Color = SMOKECOLOR.Red
        elseif TextCmd == 'orange' then
            Color = SMOKECOLOR.Orange
        elseif TextCmd == 'blue' then
            Color = SMOKECOLOR.Blue
        end
    end
    if Object then
        local ObjectTable = GetSimpleTable({DataTable['GROUP'], DataTable['UNIT'], DataTable['STATIC']})
        for _, Obj in pairs(ObjectTable) do
            if Obj ~= nil and Obj:IsAlive() then
                if Debug then BASE:E({FileVer,'CmdSmoke',Color=Color,Object=Obj:GetName(),Coordinate=CoordToString(Obj:GetCoordinate())}) end
                Obj:GetCoordinate():Smoke(Color)
            end
        end
    else
        Coord:Smoke(Color)
        if Debug then BASE:E({FileVer,'CmdSmoke',Color=Color,Coordinate=CoordToString(Coord)}) end
    end
end

--- Command: illumination
--- @param Coord table
--- @param CmdData table
local function CmdIllumination(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local Object = DataTable['GROUP'][1] or DataTable['UNIT'][1] or DataTable['STATIC'][1] or nil
    local Power = DataTable['NUMBER'][1] or 1000
    if Object then
        local ObjectTable = GetSimpleTable({DataTable['GROUP'], DataTable['UNIT'], DataTable['STATIC']})
        for _, Obj in pairs(ObjectTable) do
            if Obj ~= nil and Obj:IsAlive() then
                if Debug then BASE:E({FileVer,'CmdIllumination',Power=Power,Object=Obj:GetName(),Coordinate=CoordToString(Obj:GetCoordinate())}) end
                Obj:GetCoordinate():IlluminationBomb(Power)
            end
        end
    else
        Coord:IlluminationBomb(Power)
        if Debug then BASE:E({FileVer,'CmdIllumination',Power=Power,Coordinate=CoordToString(Coord)}) end
    end
end

--[[
--- Command: bombrunway
--- @param Coord table
--- @param CmdData table
local function CmdBombRunway(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local Object = DataTable['GROUP'][1] or nil
    local Target = DataTable['AIRBASE'][1] or nil
    local Altitude = DataTable['NUMBER'][1] or nil
    if Object and Target then
        local ObjectTable = GetSimpleTable({DataTable['GROUP']})
        for _, Obj in pairs(ObjectTable) do
            if Obj ~= nil and Obj:IsAlive() then
                if Debug then BASE:E({FileVer,'CmdBombRunway',Target=Target:GetName(),Object=Obj:GetName(),Coordinate=CoordToString(Obj:GetCoordinate())}) end
                local FltGrp = FLIGHTGROUP:New(Obj)
                local Mission = AUFTRAG:NewBOMBRUNWAY(Target, Altitude)
                Mission:SetMissionSpeed(UTILS.KmphToKnots(Obj:GetSpeedMax()*0.8))
                --Mission:SetMissionAltitude(Altitude)
                FltGrp:AddMission(Mission)
            end
        end
    end
end
]]

--- Command: mission
--- @param Coord table
--- @param CmdData table
local function CmdMission(Coord, CmdData)
    local DataTable = GetDataFromString(CmdData)
    local HasGroup = DataTable['GROUP'][1] or nil
    local HasUnit = DataTable['UNIT'][1] or nil
    local HasStatic = DataTable['STATIC'][1] or nil
    local HasAirbase = DataTable['AIRBASE'][1] or nil
    local HasNumber = DataTable['NUMBER'][1] or nil
    local HasString = DataTable['STRING'][1] or nil
    if HasString then
        local GroupTable = GetSimpleTable({DataTable['GROUP']})
        local UnitTable = GetSimpleTable({DataTable['UNIT']})
        local StaticTable = GetSimpleTable({DataTable['STATIC']})
        local AirbaseTable = GetSimpleTable({DataTable['AIRBASE']})
        local NumberTable = GetSimpleTable({DataTable['NUMBER']})
        local StringTable = GetSimpleTable({DataTable['STRING']})
        if HasString == 'bombrunway' then
        end
        --[[
        for _, Obj in pairs(ObjectTable) do
            if Obj ~= nil and Obj:IsAlive() then
                if Debug then BASE:E({FileVer,'CmdMission',Target=Target:GetName(),Object=Obj:GetName(),Coordinate=CoordToString(Obj:GetCoordinate())}) end
                local FltGrp = FLIGHTGROUP:New(Obj)
                local Mission = AUFTRAG:NewBOMBRUNWAY(Target, Altitude)
                Mission:SetMissionSpeed(UTILS.KmphToKnots(Obj:GetSpeedMax()*0.8))
                --Mission:SetMissionAltitude(Altitude)
                FltGrp:AddMission(Mission)
            end
        end
        ]]
    end
end

--- Process F10 marker command
--- @param Text string
--- @param Coord table
local function ProcessCommand(Text, Coord)
    local TextTable = UTILS.Split(Text, '\n')
    local _Command = TextTable[1] or nil
    local Action = TextTable[2] or nil
    local CmdData = TextTable[3] or nil
    if _Command == Command then
        if Debug then BASE:E({FileVer,Action=Action,CmdData=CmdData}) end
        if Action then
            if Action == 'explosion' then CmdExplosion(Coord, CmdData) end
            if Action == 'flag' then CmdFlag(Coord, CmdData) end
            if Action == 'spawn' then CmdSpawn(Coord, CmdData) end
            if Action == 'destroy' then CmdDestroy(Coord, CmdData) end
            if Action == 'flare' then CmdFlare(Coord, CmdData) end
            if Action == 'smoke' then CmdSmoke(Coord, CmdData) end
            if Action == 'illumination' then CmdIllumination(Coord, CmdData) end
            --if Action == 'bombrunway' then CmdBombRunway(Coord, CmdData) end
            if Action == 'mission' then CmdMission(Coord, CmdData) end
        end
    end
end

--- OnEventMarkRemoved
--- @param EventData table
function STNE.EventHandler.MissionTools:OnEventMarkRemoved(EventData)
    if EventData.text ~= nil and EventData.MarkCoordinate ~= nil and EventData.text:find(Command) then
        if Debug then BASE:E({FileVer,Command=Command,Coalition=EventData.IniCoalition or EventData.coalition,PlayerName=EventData.IniPlayerName}) end
        ProcessCommand(EventData.text, EventData.MarkCoordinate)
    end
end

-- EOF
env.info('FILE: '..FileVer..' END')