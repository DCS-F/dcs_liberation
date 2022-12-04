--------------------------------------------------------------------------------------------------------------------------------------------------------------- VEAF root script library for DCS Workd
-- By zip (2018)
-- Modified by MetalStormGhost in 2022-12 because DCS World 2.8 crashes with the unmodified script
--
-- Features:
-- ---------
-- Contains all the constants and utility functions required by the other VEAF script libraries
--
-- Prerequisite:
-- ------------
-- * This script requires DCS 2.5.1 or higher and MIST 4.3.74 or higher.
--
-- Load the script:
-- ----------------
-- 1.) Download the script and save it anywhere on your hard drive.
-- 2.) Open your mission in the mission editor.
-- 3.) Add a new trigger:
--     * TYPE   "4 MISSION START"
--     * ACTION "DO SCRIPT FILE"
--     * OPEN --> Browse to the location of MIST and click OK.
--     * ACTION "DO SCRIPT FILE"
--     * OPEN --> Browse to the location where you saved the script and click OK.
--
-------------------------------------------------------------------------------------------------------------------------------------------------------------

ctld_groups = {}

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Global settings. Stores the root VEAF constants
-------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Identifier. All output in DCS.log will start with this.
ctld_groups.Id = "CTLD_groups"

--- Version.
ctld_groups.Version = "1.18.0"

--- Development version ?
ctld_groups.Development = true
ctld_groups.SecurityDisabled = true

-- trace level, specific to this module
--ctld_groups.LogLevel = "trace"
--ctld_groups.LogLevel = "debug"
--ctld_groups.ForcedLogLevel = "trace"

-- log level, limiting all the modules
ctld_groups.BaseLogLevel = 5 --trace

ctld_groups.DEFAULT_GROUND_SPEED_KPH = 30
-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Do not change anything below unless you know what you are doing!
-------------------------------------------------------------------------------------------------------------------------------------------------------------

ctld_groups.monitoredFlags = {}
ctld_groups.maxMonitoredFlag = 27000
ctld_groups.config = {}

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Utility methods
-------------------------------------------------------------------------------------------------------------------------------------------------------------

ctld_groups.EVENTMETA = {
    [world.event.S_EVENT_SHOT] = {
        Order = 1,
        Side = "I",
        Event = "OnEventShot",
        Text = "S_EVENT_SHOT"
    },
    [world.event.S_EVENT_HIT] = {
        Order = 1,
        Side = "T",
        Event = "OnEventHit",
        Text = "S_EVENT_HIT"
    },
    [world.event.S_EVENT_TAKEOFF] = {
        Order = 1,
        Side = "I",
        Event = "OnEventTakeoff",
        Text = "S_EVENT_TAKEOFF"
    },
    [world.event.S_EVENT_LAND] = {
        Order = 1,
        Side = "I",
        Event = "OnEventLand",
        Text = "S_EVENT_LAND"
    },
    [world.event.S_EVENT_CRASH] = {
        Order = -1,
        Side = "I",
        Event = "OnEventCrash",
        Text = "S_EVENT_CRASH"
    },
    [world.event.S_EVENT_EJECTION] = {
        Order = 1,
        Side = "I",
        Event = "OnEventEjection",
        Text = "S_EVENT_EJECTION"
    },
    [world.event.S_EVENT_REFUELING] = {
        Order = 1,
        Side = "I",
        Event = "OnEventRefueling",
        Text = "S_EVENT_REFUELING"
    },
    [world.event.S_EVENT_DEAD] = {
        Order = -1,
        Side = "I",
        Event = "OnEventDead",
        Text = "S_EVENT_DEAD"
    },
    [world.event.S_EVENT_PILOT_DEAD] = {
        Order = 1,
        Side = "I",
        Event = "OnEventPilotDead",
        Text = "S_EVENT_PILOT_DEAD"
    },
    [world.event.S_EVENT_BASE_CAPTURED] = {
        Order = 1,
        Side = "I",
        Event = "OnEventBaseCaptured",
        Text = "S_EVENT_BASE_CAPTURED"
    },
    [world.event.S_EVENT_MISSION_START] = {
        Order = 1,
        Side = "N",
        Event = "OnEventMissionStart",
        Text = "S_EVENT_MISSION_START"
    },
    [world.event.S_EVENT_MISSION_END] = {
        Order = 1,
        Side = "N",
        Event = "OnEventMissionEnd",
        Text = "S_EVENT_MISSION_END"
    },
    [world.event.S_EVENT_TOOK_CONTROL] = {
        Order = 1,
        Side = "N",
        Event = "OnEventTookControl",
        Text = "S_EVENT_TOOK_CONTROL"
    },
    [world.event.S_EVENT_REFUELING_STOP] = {
        Order = 1,
        Side = "I",
        Event = "OnEventRefuelingStop",
        Text = "S_EVENT_REFUELING_STOP"
    },
    [world.event.S_EVENT_BIRTH] = {
        Order = 1,
        Side = "I",
        Event = "OnEventBirth",
        Text = "S_EVENT_BIRTH"
    },
    [world.event.S_EVENT_HUMAN_FAILURE] = {
        Order = 1,
        Side = "I",
        Event = "OnEventHumanFailure",
        Text = "S_EVENT_HUMAN_FAILURE"
    },
    [world.event.S_EVENT_ENGINE_STARTUP] = {
        Order = 1,
        Side = "I",
        Event = "OnEventEngineStartup",
        Text = "S_EVENT_ENGINE_STARTUP"
    },
    [world.event.S_EVENT_ENGINE_SHUTDOWN] = {
        Order = 1,
        Side = "I",
        Event = "OnEventEngineShutdown",
        Text = "S_EVENT_ENGINE_SHUTDOWN"
    },
    [world.event.S_EVENT_PLAYER_ENTER_UNIT] = {
        Order = 1,
        Side = "I",
        Event = "OnEventPlayerEnterUnit",
        Text = "S_EVENT_PLAYER_ENTER_UNIT"
    },
    [world.event.S_EVENT_PLAYER_LEAVE_UNIT] = {
        Order = -1,
        Side = "I",
        Event = "OnEventPlayerLeaveUnit",
        Text = "S_EVENT_PLAYER_LEAVE_UNIT"
    },
    [world.event.S_EVENT_PLAYER_COMMENT] = {
        Order = 1,
        Side = "I",
        Event = "OnEventPlayerComment",
        Text = "S_EVENT_PLAYER_COMMENT"
    },
    [world.event.S_EVENT_SHOOTING_START] = {
        Order = 1,
        Side = "I",
        Event = "OnEventShootingStart",
        Text = "S_EVENT_SHOOTING_START"
    },
    [world.event.S_EVENT_SHOOTING_END] = {
        Order = 1,
        Side = "I",
        Event = "OnEventShootingEnd",
        Text = "S_EVENT_SHOOTING_END"
    },
    [world.event.S_EVENT_MARK_ADDED] = {
        Order = 1,
        Side = "I",
        Event = "OnEventMarkAdded",
        Text = "S_EVENT_MARK_ADDED"
    },
    [world.event.S_EVENT_MARK_CHANGE] = {
        Order = 1,
        Side = "I",
        Event = "OnEventMarkChange",
        Text = "S_EVENT_MARK_CHANGE"
    },
    [world.event.S_EVENT_MARK_REMOVED] = {
        Order = 1,
        Side = "I",
        Event = "OnEventMarkRemoved",
        Text = "S_EVENT_MARK_REMOVED"
    }
}

--[[ json.lua

Used from https://gist.github.com/tylerneylon/59f4bcf316be525b30ab with authorization

A compact pure-Lua JSON library.
The main functions are: json.stringify, json.parse.
## json.stringify:
This expects the following to be true of any tables being encoded:
 * They only have string or number keys. Number keys must be represented as
   strings in json; this is part of the json spec.
 * They are not recursive. Such a structure cannot be specified in json.
A Lua table is considered to be an array if and only if its set of keys is a
consecutive sequence of positive integers starting at 1. Arrays are encoded like
so: `[2, 3, false, "hi"]`. Any other type of Lua table is encoded as a json
object, encoded like so: `{"key1": 2, "key2": false}`.
Because the Lua nil value cannot be a key, and as a table value is considerd
equivalent to a missing key, there is no way to express the json "null" value in
a Lua table. The only way this will output "null" is if your entire input obj is
nil itself.
An empty Lua table, {}, could be considered either a json object or array -
it's an ambiguous edge case. We choose to treat this as an object as it is the
more general type.
To be clear, none of the above considerations is a limitation of this code.
Rather, it is what we get when we completely observe the json specification for
as arbitrary a Lua object as json is capable of expressing.
## json.parse:
This function parses json, with the exception that it does not pay attention to
\u-escaped unicode code points in strings.
It is difficult for Lua to return null as a value. In order to prevent the loss
of keys with a null value in a json string, this function uses the one-off
table value json.null (which is just an empty table) to indicate null values.
This way you can check if a value is null with the conditional
`val == json.null`.
If you have control over the data and are using Lua, I would recommend just
avoiding null values in your data to begin with.
--]]


ctld_groups.json = {}


-- Internal functions.

local function kind_of(obj)
  if type(obj) ~= 'table' then return type(obj) end
  local i = 1
  for _ in pairs(obj) do
    if obj[i] ~= nil then i = i + 1 else return 'table' end
  end
  if i == 1 then return 'table' else return 'array' end
end

local function escape_str(s)
  local in_char  = {'\\', '"', '/', '\b', '\f', '\n', '\r', '\t'}
  local out_char = {'\\', '"', '/',  'b',  'f',  'n',  'r',  't'}
  for i, c in ipairs(in_char) do
    s = s:gsub(c, '\\' .. out_char[i])
  end
  return s
end

-- Returns pos, did_find; there are two cases:
-- 1. Delimiter found: pos = pos after leading space + delim; did_find = true.
-- 2. Delimiter not found: pos = pos after leading space;     did_find = false.
-- This throws an error if err_if_missing is true and the delim is not found.
local function skip_delim(str, pos, delim, err_if_missing)
  pos = pos + #str:match('^%s*', pos)
  if str:sub(pos, pos) ~= delim then
    if err_if_missing then
      error('Expected ' .. delim .. ' near position ' .. pos)
    end
    return pos, false
  end
  return pos + 1, true
end

-- Expects the given pos to be the first character after the opening quote.
-- Returns val, pos; the returned pos is after the closing quote character.
local function parse_str_val(str, pos, val)
  val = val or ''
  local early_end_error = 'End of input found while parsing string.'
  if pos > #str then error(early_end_error) end
  local c = str:sub(pos, pos)
  if c == '"'  then return val, pos + 1 end
  if c ~= '\\' then return parse_str_val(str, pos + 1, val .. c) end
  -- We must have a \ character.
  local esc_map = {b = '\b', f = '\f', n = '\n', r = '\r', t = '\t'}
  local nextc = str:sub(pos + 1, pos + 1)
  if not nextc then error(early_end_error) end
  return parse_str_val(str, pos + 2, val .. (esc_map[nextc] or nextc))
end

-- Returns val, pos; the returned pos is after the number's final character.
local function parse_num_val(str, pos)
  local num_str = str:match('^-?%d+%.?%d*[eE]?[+-]?%d*', pos)
  local val = tonumber(num_str)
  if not val then error('Error parsing number at position ' .. pos .. '.') end
  return val, pos + #num_str
end


-- Public values and functions.

function ctld_groups.json.stringify(obj, as_key)
  local s = {}  -- We'll build the string as an array of strings to be concatenated.
  local kind = kind_of(obj)  -- This is 'array' if it's an array or type(obj) otherwise.
  if kind == 'array' then
    if as_key then error('Can\'t encode array as key.') end
    s[#s + 1] = '['
    for i, val in ipairs(obj) do
      if i > 1 then s[#s + 1] = ', ' end
      s[#s + 1] = ctld_groups.json.stringify(val)
    end
    s[#s + 1] = ']'
  elseif kind == 'table' then
    if as_key then error('Can\'t encode table as key.') end
    s[#s + 1] = '{'
    for k, v in pairs(obj) do
      if #s > 1 then s[#s + 1] = ', ' end
      s[#s + 1] = ctld_groups.json.stringify(k, true)
      s[#s + 1] = ':'
      s[#s + 1] = ctld_groups.json.stringify(v)
    end
    s[#s + 1] = '}'
  elseif kind == 'string' then
    return '"' .. escape_str(obj) .. '"'
  elseif kind == 'number' then
    if as_key then return '"' .. tostring(obj) .. '"' end
    return tostring(obj)
  elseif kind == 'boolean' then
    return tostring(obj)
  elseif kind == 'nil' then
    return 'null'
  else
    return '"Unjsonifiable type: ' .. kind .. '."'
    --error('Unjsonifiable type: ' .. kind .. '.')
  end
  return table.concat(s)
end

ctld_groups.json.null = {}  -- This is a one-off table to represent the null value.

function ctld_groups.json.parse(str, pos, end_delim)
  pos = pos or 1
  if pos > #str then error('Reached unexpected end of input.') end
  local pos = pos + #str:match('^%s*', pos)  -- Skip whitespace.
  local first = str:sub(pos, pos)
  if first == '{' then  -- Parse an object.
    local obj, key, delim_found = {}, true, true
    pos = pos + 1
    while true do
      key, pos = ctld_groups.json.parse(str, pos, '}')
      if key == nil then return obj, pos end
      if not delim_found then error('Comma missing between object items.') end
      pos = skip_delim(str, pos, ':', true)  -- true -> error if missing.
      obj[key], pos = ctld_groups.json.parse(str, pos)
      pos, delim_found = skip_delim(str, pos, ',')
    end
  elseif first == '[' then  -- Parse an array.
    local arr, val, delim_found = {}, true, true
    pos = pos + 1
    while true do
      val, pos = ctld_groups.json.parse(str, pos, ']')
      if val == nil then return arr, pos end
      if not delim_found then error('Comma missing between array items.') end
      arr[#arr + 1] = val
      pos, delim_found = skip_delim(str, pos, ',')
    end
  elseif first == '"' then  -- Parse a string.
    return parse_str_val(str, pos + 1)
  elseif first == '-' or first:match('%d') then  -- Parse a number.
    return parse_num_val(str, pos)
  elseif first == end_delim then  -- End of an object or array.
    return nil, pos + 1
  else  -- Parse true, false, or null.
    local literals = {['true'] = true, ['false'] = false, ['null'] = ctld_groups.json.null}
    for lit_str, lit_val in pairs(literals) do
      local lit_end = pos + #lit_str - 1
      if str:sub(pos, lit_end) == lit_str then return lit_val, lit_end + 1 end
    end
    local pos_info_str = 'position ' .. pos .. ': ' .. str:sub(pos, pos + 10)
    error('Invalid json syntax starting at ' .. pos_info_str)
  end
end

--- efficiently remove elements from a table
--- credit : Mitch McMabers (https://stackoverflow.com/questions/12394841/safely-remove-items-from-an-array-table-while-iterating)
function ctld_groups.arrayRemoveWhen(t, fnKeep)
    local pristine = true    
    local j, n = 1, #t;
    for i=1,n do
        if (fnKeep(t, i, j)) then
            if (i ~= j) then
                -- Keep i's value, move it to j's pos.
                t[j] = t[i];
                t[i] = nil;
            else
                -- Keep i's value, already at j's pos.
            end
            j = j + 1;
        else
            t[i] = nil;
            pristine = false
        end
    end
    return not pristine;
end

function ctld_groups.vecToString(vec)
    local result = ""
    if vec.x then
        result = result .. string.format(" x=%.1f", vec.x)
    end
    if vec.y then
        result = result .. string.format(" y=%.1f", vec.y)
    end
    if vec.z then
        result = result .. string.format(" z=%.1f", vec.z)
    end
    return result
end

function ctld_groups.discoverMetadata(o)
    local text = ""
    for key,value in pairs(getmetatable(o)) do
       text = text .. " - ".. key.."\n";
    end
	return text
end

function ctld_groups.serialize(name, value, level)
    -- mostly based on slMod serializer 
  
    local function _basicSerialize(s)
      if s == nil then
        return "\"\""
      else
        if ((type(s) == 'number') or (type(s) == 'boolean') or (type(s) == 'function') or (type(s) == 'table') or (type(s) == 'userdata') ) then
          return tostring(s)
        elseif type(s) == 'string' then
          return string.format('%q', s)
        end
      end	
    end
  
    -----Based on ED's serialize_simple2
    local basicSerialize = function(o)
        if type(o) == "number" then
            return tostring(o)
        elseif type(o) == "boolean" then
            return tostring(o)
        else -- assume it is a string
            return _basicSerialize(o)
        end
    end
  
    local serialize_to_t = function(name, value, level)
        ----Based on ED's serialize_simple2
  
        local var_str_tbl = {}
        if level == nil then
            level = ""
        end
        if level ~= "" then
            level = level .. "  "
        end
  
        table.insert(var_str_tbl, level .. name .. " = ")
  
        if type(value) == "number" or type(value) == "string" or type(value) == "boolean" then
            table.insert(var_str_tbl, basicSerialize(value) .. ",\n")
        elseif type(value) == "table" then
            table.insert(var_str_tbl, "{\n")
            local tkeys = {}
            -- populate the table that holds the keys
            for k in pairs(value) do table.insert(tkeys, k) end
            -- sort the keys
            table.sort(tkeys, _sortNumberOrCaseInsensitive)
            -- use the keys to retrieve the values in the sorted order
            for _, k in ipairs(tkeys) do  -- serialize its fields
              local v = value[k]
                local key
                if type(k) == "number" then
                    key = string.format("[%s]", k)
                else
                    key = string.format("[%q]", k)
                end
  
                table.insert(var_str_tbl, ctld_groups.serialize(key, v, level .. "  "))
            end
            if level == "" then
                table.insert(var_str_tbl, level .. "} -- end of " .. name .. "\n")
            else
                table.insert(var_str_tbl, level .. "}, -- end of " .. name .. "\n")
            end
        else
            ctld_groups.loggers.get(ctld_groups.Id):error("Cannot serialize a " .. type(value))
        end
        return var_str_tbl
    end
  
    local t_str = serialize_to_t(name, value, level)
  
    return table.concat(t_str)
end

function ctld_groups.ifnn(o, field)
    if o then
        if o[field] then
            if type(o[field]) == "function" then
                local sta, res = pcall(o[field],o)
                if sta then 
                    return res
                else
                    return nil
                end
            else
                return o[field]
            end
        end
    else
        return nil
    end
end

function ctld_groups.ifnns(o, fields)
    local result = nil
    if o then
        result = {}
        for _, field in pairs(fields) do
            if o[field] then
                if type(o[field]) == "function" then
                    local sta, res = pcall(o[field],o)
                    if sta then 
                        result[field] = res
                    else
                        result[field] = nil
                    end
                else
                    result[field] = o[field]
                end
            end
        end
    end
    return result
end

function ctld_groups.p(o, level, skip)
    if o and type(o) == "table" and (o.x and o.z and o.y and #o == 3) then
        return string.format("{x=%s, z=%s, y=%s}", ctld_groups.p(o.x), ctld_groups.p(o.z), ctld_groups.p(o.y))
    elseif o and type(o) == "table" and (o.x and o.y and #o == 2)  then
        return string.format("{x=%s, y=%s}", ctld_groups.p(o.x), ctld_groups.p(o.y))
    end
    local skip = skip
    if skip and type(skip)=="table" then
        for _, value in ipairs(skip) do
            skip[value]=true
        end
    end
    return ctld_groups._p(o, level, skip)
end

function ctld_groups._p(o, level, skip)
    local MAX_LEVEL = 20
    if level == nil then level = 0 end
    if level > MAX_LEVEL then 
        ctld_groups.loggers.get(ctld_groups.Id):error("max depth reached in ctld_groups.p : "..tostring(MAX_LEVEL))
        return ""
    end
    local text = ""
    if (type(o) == "table") then
        text = "\n"
        local keys = {}
        local values = {}
        for key, value in pairs(o) do
            local sKey = tostring(key)
            table.insert(keys, sKey)
            values[sKey] = value
        end
        table.sort(keys)
        for _, key in pairs(keys) do
            local value = values[key]
            for i=0, level do
                text = text .. " "
            end
            if not (skip and skip[key]) then
                text = text .. ".".. key.."="..ctld_groups.p(value, level+1, skip) .. "\n"
            else
                text = text .. ".".. key.."= [[SKIPPED]]\n"
            end
        end
    elseif (type(o) == "function") then
        text = "[function]"
    elseif (type(o) == "boolean") then
        if o == true then 
            text = "[true]"
        else
            text = "[false]"
        end
    else
        if o == nil then
            text = "[nil]"   
        else
            text = tostring(o)
        end
    end
    return text
end

function ctld_groups.length(T)
    local count = 0
    if T ~= nil then
        for _ in pairs(T) do count = count + 1 end
    end
    return count
end

--- Simple round
function ctld_groups.round(num, numDecimalPlaces)
  local mult = 10^(numDecimalPlaces or 0)
  return math.floor(num * mult + 0.5) / mult
end

--- shuffle a table elements around
function ctld_groups.shuffle(tbl)
    for i = #tbl, 2, -1 do
      local j = math.random(i)
      tbl[i], tbl[j] = tbl[j], tbl[i]
    end
    return tbl
end

--- Return the height of the land at the coordinate.
function ctld_groups.getLandHeight(vec3)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("getLandHeight: vec3  x=%.1f y=%.1f, z=%.1f", vec3.x, vec3.y, vec3.z))
    local vec2 = {x = vec3.x, y = vec3.z}
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("getLandHeight: vec2  x=%.1f z=%.1f", vec3.x, vec3.z))
    -- We add 1 m "safety margin" because data from getlandheight gives the surface and wind at or below the surface is zero!
    local height = math.floor(land.getHeight(vec2) + 1)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("getLandHeight: result  height=%.1f",height))
    return height
end

function ctld_groups.invertHeading(heading)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("invertHeading(%s)", ctld_groups.p(heading)))
    local result = heading - 180
    if result <= 0 then
        result = result + 360
    end
    return result
end

-- get a LL position based on a string 
-- can be UTM (U38TMP334456 or u37TMP4351)
-- can be LL with either : or - as a separator, and either DMS, DM decimal, or D decimal (N42:23:45E044-12.5 or N42.3345E044-12.5)
function ctld_groups.computeLLFromString(value)
    local function _computeLLValueFromString(value)
        local result = -1
        if value:find(":") or value:find("-") then
            -- convert in arc-seconds
            local values = ctld_groups.splitWithPattern(value, "[:-]+")
            local weights = {3600, 60, 1}
            for _, element in pairs(values) do
                ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("element=%s",ctld_groups.p(element)))
                local weight = table.remove(weights, 1)
                local elementInArcSec = tonumber(element)*weight
                result = result + elementInArcSec
            end
            result = result / 3600
        else
            -- decimals
            result = tonumber(value)
        end
        return result
    end
    
    local result = -1
    if value then
        local _value = value:lower()
        local _firstChar = _value:sub(1,1)
        if _firstChar == "u" then
            -- UTM coordinates
            local _zone, _digraph, _digits = _value:match("u(%d%d[a-z])([a-z][a-z])(%d+)")
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("_zone=%s",ctld_groups.p(_zone)))
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("_digraph=%s",ctld_groups.p(_digraph)))
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("_digits=%s",ctld_groups.p(_digits)))
            if _zone and _digraph and _digits then
                local _nDigits = #_digits
                local _northingString = _digits:sub(_nDigits/2+1)
                local _northing = tonumber(_northingString)
                ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("_northing=%s",ctld_groups.p(_northing)))
                if #_northingString == 1 then
                    _northing = _northing * 10000
                elseif #_northingString == 2 then
                    _northing = _northing * 1000
                elseif #_northingString == 3 then
                    _northing = _northing * 100
                elseif #_northingString == 4 then
                    _northing = _northing * 10
                end

                local _eastingString = _digits:sub(1, _nDigits/2)
                local _easting = tonumber(_eastingString)
                ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("_easting=%s",ctld_groups.p(_easting)))
                if #_eastingString == 1 then
                    _easting = _easting * 10000
                elseif #_eastingString == 2 then
                    _easting = _easting * 1000
                elseif #_eastingString == 3 then
                    _easting = _easting * 100
                elseif #_eastingString == 4 then
                    _easting = _easting * 10
                end

                local _utm= { UTMZone = _zone:upper(), MGRSDigraph = _digraph:upper(), Easting = _easting, Northing = _northing }  
                ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("_utm=%s",ctld_groups.p(_utm)))
                return coord.MGRStoLL(_utm)
            end
        elseif _firstChar == "n" or _firstChar == "s" or _firstChar == "e" or _firstChar == "w" then
            -- LL coordinates
            local _signLat, _digitsLat, _signLon, _digitsLon = _value:match([[([news])([%d:\.-]+)([news])([%d:\.-]+)]])
            local _multLat = 1
            if _signLat == "s" then 
                _multLat = -1
            end
            local _multLon = 1
            if _signLon == "w" then 
                _multLon = -1
            end
            local _lat = _multLat * _computeLLValueFromString(_digitsLat)
            local _lon = _multLon * _computeLLValueFromString(_digitsLon)
            return _lat, _lon
        end
    end
    -- unrecognized format
    return nil
end
 
function ctld_groups.silenceAtcOnAllAirbases()
    local bases = world.getAirbases()
    for _, base in pairs(bases) do
        if base:getDesc() then
            if base:getDesc().category == Airbase.Category.AIRDROME then
                ctld_groups.loggers.get(ctld_groups.Id):info("silencing ATC at base %s", ctld_groups.p(base:getDesc().displayName))
                base:setRadioSilentMode(true)
            end
        end
    end
end

--- Return a point at the same coordinates, but on the surface
function ctld_groups.placePointOnLand(vec3)
    -- convert a vec2 to a vec3
    if not vec3.z then
        vec3.z = vec3.y 
        vec3.y = 0
    end
    
    if not vec3.y then
        vec3.y = 0
    end
    
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("getLandHeight: vec3  x=%.1f y=%.1f, z=%.1f", vec3.x, vec3.y, vec3.z))
    local height = ctld_groups.getLandHeight(vec3)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("getLandHeight: result  height=%.1f",height))
    local result={x=vec3.x, y=height, z=vec3.z}
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("placePointOnLand: result  x=%.1f y=%.1f, z=%.1f", result.x, result.y, result.z))
    return result
end

--- Trim a string
function ctld_groups.trim(s)
    local a = s:match('^%s*()')
    local b = s:match('()%s*$', a)
    return s:sub(a,b-1)
end

--- Split string. C.f. http://stackoverflow.com/questions/1426954/split-string-in-lua
function ctld_groups.splitWithPattern(str, pat)
    local t = {}  -- NOTE: use {n = 0} in Lua-5.0
    local fpat = "(.-)" .. pat
    local last_end = 1
    local s, e, cap = str:find(fpat, 1)
    while s do
        if s ~= 1 or cap ~= "" then
            table.insert(t, cap)
        end
        last_end = e+1
        s, e, cap = str:find(fpat, last_end)
    end
    if last_end <= #str then
        cap = str:sub(last_end)
        table.insert(t, cap)
    end
    return t
end

function ctld_groups.split(str, sep)
    local result = {}
    local regex = ("([^%s]+)"):format(sep)
    for each in str:gmatch(regex) do
        table.insert(result, each)
    end
    return result
end

--- Break string around a separator
function ctld_groups.breakString(str, sep)
    local regex = ("^([^%s]+)%s(.*)$"):format(sep, sep)
    local a, b = str:match(regex)
    if not a then a = str end
    local result = {a, b}
    return result
end

--- Get the average center of a group position (average point of all units position)
function ctld_groups.getAveragePosition(group)
    if type(group) == "string" then 
        group = Group.getByName(group)
    end

    local count

	local totalPosition = {x = 0,y = 0,z = 0}
	if group then
		local units = Group.getUnits(group)
		for count = 1,#units do
			if units[count] then 
				totalPosition = mist.vec.add(totalPosition,Unit.getPosition(units[count]).p)
			end
		end
		if #units > 0 then
			return mist.vec.scalar_mult(totalPosition,1/#units)
		else
			return nil
		end
	else
		return nil
	end
end

function ctld_groups.emptyFunction()
end

--- Returns the wind direction (from) and strength.
function ctld_groups.getWind(point)

    -- Get wind velocity vector.
    local windvec3  = atmosphere.getWind(point)
    local direction = math.floor(math.deg(math.atan2(windvec3.z, windvec3.x)))
    
    if direction < 0 then
      direction = direction + 360
    end
    
    -- Convert TO direction to FROM direction. 
    if direction > 180 then
      direction = direction-180
    else
      direction = direction+180
    end
    
    -- Calc 2D strength.
    local strength=math.floor(math.sqrt((windvec3.x)^2+(windvec3.z)^2))
    
    -- Debug output.
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("Wind data: point x=%.1f y=%.1f, z=%.1f", point.x, point.y,point.z))
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("Wind data: wind  x=%.1f y=%.1f, z=%.1f", windvec3.x, windvec3.y,windvec3.z))
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("Wind data: |v| = %.1f", strength))
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("Wind data: ang = %.1f", direction))
    
    -- Return wind direction and strength (in m/s).
    return direction, strength, windvec3
  end

--- Find a suitable point for spawning a unit in a <dispersion>-sized circle around a spot
function ctld_groups.findPointInZone(spawnSpot, dispersion, isShip)
    local unitPosition
    local tryCounter = 1000
    local _dispersion = 0
    repeat -- Place the unit in a "dispersion" ft radius circle from the spawn spot
        unitPosition = mist.getRandPointInCircle(spawnSpot, _dispersion)
        local landType = land.getSurfaceType(unitPosition)
        tryCounter = tryCounter - 1
        _dispersion = _dispersion + dispersion
    until ((isShip and landType == land.SurfaceType.WATER) or (not(isShip) and (landType == land.SurfaceType.LAND or landType == land.SurfaceType.ROAD or landType == land.SurfaceType.RUNWAY))) or tryCounter == 0
    if tryCounter == 0 then
        return nil
    else
        return unitPosition
    end
end

--- TODO doc
function ctld_groups.generateVehiclesRoute(startPoint, destination, onRoad, speed, patrol)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("ctld_groups.generateVehiclesRoute(onRoad=[%s], speed=[%s], patrol=[%s])", tostring(onRoad or ""), tostring(speed or ""), tostring(patrol or "")))

    speed = speed or ctld_groups.DEFAULT_GROUND_SPEED_KPH
    onRoad = onRoad or false
    patrol = patrol or false
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("startPoint = {x = %d, y = %d, z = %d}", startPoint.x, startPoint.y, startPoint.z))
    local action = "Diamond"
    if onRoad then
        action = "On Road"
    end

    local endPoint = ctld_groupsNamedPoints.getPoint(destination)
    if not(endPoint) then
        -- check if these are coordinates
        local _lat, _lon = ctld_groups.computeLLFromString(destination)
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("_lat=%s",ctld_groups.p(_lat)))
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("_lon=%s",ctld_groups.p(_lon)))
        if _lat and _lon then 
            endPoint = coord.LLtoLO(_lat, _lon)
        end
    end
    if not(endPoint) then
        local msg = "A point named "..destination.." cannot be found, and these are not valid coordinates !"
        ctld_groups.loggers.get(ctld_groups.Id):warn(msg)
        trigger.action.outText(msg, 5)
        return
    end
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("endPoint=%s", ctld_groups.p(endPoint)))
        
    if onRoad then
        ctld_groups.loggers.get(ctld_groups.Id):trace("setting startPoint on a road")
        local road_x, road_z = land.getClosestPointOnRoads('roads',startPoint.x, startPoint.z)
        startPoint = ctld_groups.placePointOnLand({x = road_x, y = 0, z = road_z})
    else
        startPoint = ctld_groups.placePointOnLand({x = startPoint.x, y = 0, z = startPoint.z})
    end
    
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("startPoint = {x = %d, y = %d, z = %d}", startPoint.x, startPoint.y, startPoint.z))

    if onRoad then
        ctld_groups.loggers.get(ctld_groups.Id):trace("setting endPoint on a road")
        road_x, road_z =land.getClosestPointOnRoads('roads',endPoint.x, endPoint.z)
        endPoint = ctld_groups.placePointOnLand({x = road_x, y = 0, z = road_z})
    else
        endPoint = ctld_groups.placePointOnLand({x = endPoint.x, y = 0, z = endPoint.z})
    end
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("endPoint = {x = %d, y = %d, z = %d}", endPoint.x, endPoint.y, endPoint.z))
    
    local vehiclesRoute = {
        [1] = 
        {
            ["x"] = startPoint.x,
            ["y"] = startPoint.z,
            ["alt"] = startPoint.y,
            ["type"] = "Turning Point",
            ["ETA"] = 0,
            ["alt_type"] = "BARO",
            ["formation_template"] = "",
            ["name"] = "STA",
            ["ETA_locked"] = true,
            ["speed"] = speed / 3.6,
            ["action"] = action,
            ["task"] = 
            {
                ["id"] = "ComboTask",
                ["params"] = 
                {
                    ["tasks"] = 
                    {
                    }, -- end of ["tasks"]
                }, -- end of ["params"]
            }, -- end of ["task"]
            ["speed_locked"] = true,
        }, -- end of [1]
        [2] = 
        {
            ["x"] = endPoint.x,
            ["y"] = endPoint.z,
            ["alt"] = endPoint.y,
            ["type"] = "Turning Point",
            ["ETA"] = 0,
            ["alt_type"] = "BARO",
            ["formation_template"] = "",
            ["name"] = "END",
            ["ETA_locked"] = false,
            ["speed"] = speed / 3.6,
            ["action"] = action,
            ["speed_locked"] = true,
        }, -- end of [2]
    }

    if patrol then
        vehiclesRoute[3] = 
        {
            ["x"] = startPoint.x,
            ["y"] = startPoint.z,
            ["alt"] = startPoint.y,
            ["type"] = "Turning Point",
            ["ETA"] = 0,
            ["alt_type"] = "BARO",
            ["formation_template"] = "",
            ["name"] = "STA",
            ["ETA_locked"] = true,
            ["speed"] = speed / 3.6,
            ["action"] = action,
            ["task"] = 
            {
                ["id"] = "ComboTask",
                ["params"] = 
                {
                    ["tasks"] = 
                    {
                        [1] = 
                        {
                            ["enabled"] = true,
                            ["auto"] = false,
                            ["id"] = "GoToWaypoint",
                            ["number"] = 1,
                            ["params"] = 
                            {
                                ["fromWaypointIndex"] = 3,
                                ["nWaypointIndx"] = 1,
                            }, -- end of ["params"]
                        }, -- end of [1]
                    }, -- end of ["tasks"]
                }, -- end of ["params"]
            }, -- end of ["task"]
            ["speed_locked"] = true,
        }
    end
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("vehiclesRoute = %s", ctld_groups.p(vehiclesRoute)))

    return vehiclesRoute
end


--- Add a unit to the <group> on a suitable point in a <dispersion>-sized circle around a spot
function ctld_groups.addUnit(group, spawnSpot, dispersion, unitType, unitName, skill)
    local unitPosition = ctld_groups.findPointInZone(spawnSpot, dispersion, false)
    if unitPosition ~= nil then
        table.insert(
            group,
            {
                ["x"] = unitPosition.x,
                ["y"] = unitPosition.y,
                ["type"] = unitType,
                ["name"] = unitName,
                ["heading"] = 0,
                ["skill"] = skill
            }
        )
    else
        ctld_groups.loggers.get(ctld_groups.Id):info("cannot find a suitable position for unit "..unitType)
    end
end

--- Makes a group move to a waypoint set at a specific heading and at a distance covered at a specific speed in an hour
function ctld_groups.moveGroupAt(groupName, leadUnitName, heading, speed, timeInSeconds, endPosition, pMiddlePointDistance)
    ctld_groups.loggers.get(ctld_groups.Id):debug("ctld_groups.moveGroupAt(groupName=" .. groupName .. ", heading="..heading.. ", speed=".. speed..", timeInSeconds="..(timeInSeconds or 0))

    local unitGroup = Group.getByName(groupName)
    if unitGroup == nil then
        ctld_groups.loggers.get(ctld_groups.Id):error("ctld_groups.moveGroupAt: " .. groupName .. ' not found')
		return false
    end
    
    local leadUnit = unitGroup:getUnits()[1]
    if leadUnitName then
        leadUnit = Unit.getByName(leadUnitName)
    end
    if leadUnit == nil then
        ctld_groups.loggers.get(ctld_groups.Id):error("ctld_groups.moveGroupAt: " .. leadUnitName .. ' not found')
		return false
    end
    
    local headingRad = mist.utils.toRadian(heading)
    ctld_groups.loggers.get(ctld_groups.Id):trace("headingRad="..headingRad)
    local fromPosition = leadUnit:getPosition().p
    fromPosition = { x = fromPosition.x, y = fromPosition.z }
    ctld_groups.loggers.get(ctld_groups.Id):trace("fromPosition="..ctld_groups.vecToString(fromPosition))

    local mission = { 
		id = 'Mission', 
		params = { 
			["communication"] = true,
			["start_time"] = 0,
			route = { 
				points = { 
					-- first point
                    [1] = 
                    {
                        --["alt"] = 0,
                        ["type"] = "Turning Point",
                        --["formation_template"] = "Diamond",
                        --["alt_type"] = "BARO",
                        ["x"] = fromPosition.x,
                        ["y"] = fromPosition.z,
                        ["name"] = "Starting position",
                        ["action"] = "Turning Point",
                        ["speed"] = 9999, -- ahead flank
                        ["speed_locked"] = true,
                    }, -- end of [1]
				}, 
			} 
		} 
	}

    if pMiddlePointDistance then
        -- middle point (helps with having a more exact final bearing, specially with big hunks of steel like carriers)
        local middlePointDistance = 2000
        if pMiddlePointDistance then
            middlePointDistance = pMiddlePointDistance
        end

        local newWaypoint1 = {
            x = fromPosition.x + middlePointDistance * math.cos(headingRad),
            y = fromPosition.y + middlePointDistance * math.sin(headingRad),
        }
        fromPosition.x = newWaypoint1.x
        fromPosition.y = newWaypoint1.y
        ctld_groups.loggers.get(ctld_groups.Id):trace("newWaypoint1="..ctld_groups.vecToString(newWaypoint1))

        table.insert(mission.params.route.points, 
            {
                --["alt"] = 0,
                ["type"] = "Turning Point",
                --["formation_template"] = "Diamond",
                --["alt_type"] = "BARO",
                ["x"] = newWaypoint1.x,
                ["y"] = newWaypoint1.y,
                ["name"] = "Middle point",
                ["action"] = "Turning Point",
                ["speed"] = 9999, -- ahead flank
                ["speed_locked"] = true,
            }
        )
    end

    local length
    if timeInSeconds then 
        length = speed * timeInSeconds
    else
        length = speed * 3600 -- m travelled in 1 hour
    end
    ctld_groups.loggers.get(ctld_groups.Id):trace("length="..length .. " m")

    -- new route point
	local newWaypoint2 = {
		x = fromPosition.x + length * math.cos(headingRad),
		y = fromPosition.y + length * math.sin(headingRad),
	}
    ctld_groups.loggers.get(ctld_groups.Id):trace("newWaypoint2="..ctld_groups.vecToString(newWaypoint2))

    table.insert(mission.params.route.points, 
        {
            --["alt"] = 0,
            ["type"] = "Turning Point",
            --["formation_template"] = "Diamond",
            --["alt_type"] = "BARO",
            ["x"] = newWaypoint2.x,
            ["y"] = newWaypoint2.y,
            ["name"] = "",
            ["action"] = "Turning Point",
            ["speed"] = speed,
            ["speed_locked"] = true,
        }
    )

    if endPosition then
        table.insert(mission.params.route.points, 
            {
                --["alt"] = 0,
                ["type"] = "Turning Point",
                --["formation_template"] = "Diamond",
                --["alt_type"] = "BARO",
                ["x"] = endPosition.x,
                ["y"] = endPosition.z,
                ["name"] = "Back to starting position",
                ["action"] = "Turning Point",
                ["speed"] = 9999, -- ahead flank
                ["speed_locked"] = true,
            }
        )
    end

	-- replace whole mission
	unitGroup:getController():setTask(mission)
    
    return true
end

function ctld_groups.readyForCombat(group)
    if type(group) == 'string' then
        group = Group.getByName(group)
    end
    if group then
        local cont = group:getController()
        cont:setOnOff(true)
        cont:setOption(AI.Option.Ground.id.ALARM_STATE, AI.Option.Ground.val.ALARM_STATE.RED)	
        cont:setOption(AI.Option.Air.id.ROE, AI.Option.Air.val.ROE.WEAPON_FREE)
    end
end

-- Makes a group move to a specific waypoint at a specific speed
function ctld_groups.moveGroupTo(groupName, pos, speed, altitude)
    if not(altitude) then
        altitude = 0
    end
    ctld_groups.loggers.get(ctld_groups.Id):debug("ctld_groups.moveGroupTo(groupName=" .. groupName .. ", speed=".. speed .. ", altitude=".. altitude)
    ctld_groups.loggers.get(ctld_groups.Id):debug("pos="..ctld_groups.vecToString(pos))

	local unitGroup = Group.getByName(groupName)
    if unitGroup == nil then
        ctld_groups.loggers.get(ctld_groups.Id):error("ctld_groups.moveGroupTo: " .. groupName .. ' not found')
		return false
    end
    
    local route = {
        [1] =
        {
            ["alt"] = altitude,
            ["action"] = "Turning Point",
            ["alt_type"] = "BARO",
            ["speed"] = ctld_groups.round(speed, 2),
            ["type"] = "Turning Point",
            ["x"] = pos.x,
            ["y"] = pos.z,
            ["speed_locked"] = true,
        },
        [2] = 
        {
            ["alt"] = altitude,
            ["action"] = "Turning Point",
            ["alt_type"] = "BARO",
            ["speed"] = 0,
            ["type"] = "Turning Point",
            ["x"] = pos.x,
            ["y"] = pos.z,
            ["speed_locked"] = true,
        },
    }

    -- order group to new waypoint
	mist.goRoute(groupName, route)

    return true
end

function ctld_groups.getAvgGroupPos(groupName) -- stolen from Mist and corrected
	local group = groupName -- sometimes this parameter is actually a group
	if type(groupName) == 'string' and Group.getByName(groupName) and Group.getByName(groupName):isExist() == true then
		group = Group.getByName(groupName)
	end
	local units = {}
	for i = 1, group:getSize() do
		table.insert(units, group:getUnit(i):getName())
	end

	return mist.getAvgPos(units)
end

--- Computes the coordinates of a point offset from a route of a certain distance, at a certain distance from route start
--- e.g. we go from [startingPoint] to [destinationPoint], and at [distanceFromStartingPoint] we look at [offset] meters (left if <0, right else)
function ctld_groups.computeCoordinatesOffsetFromRoute(startingPoint, destinationPoint, distanceFromStartingPoint, offset)
    ctld_groups.loggers.get(ctld_groups.Id):trace("startingPoint="..ctld_groups.vecToString(startingPoint))
    ctld_groups.loggers.get(ctld_groups.Id):trace("destinationPoint="..ctld_groups.vecToString(destinationPoint))
    
    local vecAB = {x = destinationPoint.x +- startingPoint.x, y = destinationPoint.y - startingPoint.y, z = destinationPoint.z - startingPoint.z}
    ctld_groups.loggers.get(ctld_groups.Id):trace("vecAB="..ctld_groups.vecToString(vecAB))
    local alpha = math.atan2(vecAB.x, vecAB.z) -- atan2(y, x) 
    ctld_groups.loggers.get(ctld_groups.Id):trace("alpha="..alpha)
    local r = math.sqrt(distanceFromStartingPoint * distanceFromStartingPoint + offset * offset)
    ctld_groups.loggers.get(ctld_groups.Id):trace("r="..r)
    local beta = math.atan(offset / distanceFromStartingPoint)
    ctld_groups.loggers.get(ctld_groups.Id):trace("beta="..beta)
    local tho = alpha + beta
    ctld_groups.loggers.get(ctld_groups.Id):trace("tho="..tho)
    local offsetPoint = { z = r * math.cos(tho) + startingPoint.z, y = 0, x = r * math.sin(tho) + startingPoint.x}
    ctld_groups.loggers.get(ctld_groups.Id):trace("offsetPoint="..ctld_groups.vecToString(offsetPoint))
    local offsetPointOnLand = ctld_groups.placePointOnLand(offsetPoint)
    ctld_groups.loggers.get(ctld_groups.Id):trace("offsetPointOnLand="..ctld_groups.vecToString(offsetPointOnLand))

    return offsetPointOnLand, offsetPoint
end

function ctld_groups.getBearingAndRangeFromTo(fromPoint, toPoint)
    ctld_groups.loggers.get(ctld_groups.Id):trace("fromPoint="..ctld_groups.vecToString(fromPoint))
    ctld_groups.loggers.get(ctld_groups.Id):trace("toPoint="..ctld_groups.vecToString(toPoint))
    
    local vec = { z = toPoint.z - fromPoint.z, x = toPoint.x - fromPoint.x}
    local angle = mist.utils.round(mist.utils.toDegree(mist.utils.getDir(vec)), 0)
    local distance = mist.utils.get2DDist(toPoint, fromPoint)
    return angle, distance, mist.utils.round(distance / 1000, 0), mist.utils.round(mist.utils.metersToNM(distance), 0)
end

function ctld_groups.getGroupsOfCoalition(coa)
    local coalitions = { coalition.side.RED, coalition.side.BLUE, coalition.side.NEUTRAL}
    if coa then 
        coalitions = { coa } 
    end
    local allDcsGroups = {}
    for _, coa in pairs(coalitions) do
        local dcsGroups = coalition.getGroups(coa)
        for _, dcsGroup in pairs(dcsGroups) do
            table.insert(allDcsGroups, dcsGroup)
        end
    end
    return allDcsGroups
end

function ctld_groups.getStaticsOfCoalition(coa)
    local coalitions = { coalition.side.RED, coalition.side.BLUE, coalition.side.NEUTRAL}
    if coa then 
        coalitions = { coa } 
    end
    local allDcsStatics = {}
    for _, coa in pairs(coalitions) do
        local dcsStatics = coalition.getStaticObjects(coa)
        for _, dcsStatic in pairs(dcsStatics) do
            table.insert(allDcsStatics, dcsStatic)
        end
    end
    return allDcsStatics
end

function ctld_groups.getUnitsOfAllCoalitions(includeStatics)
    return ctld_groups.getUnitsOfCoalition(includeStatics)
end

function ctld_groups.getUnitsOfCoalition(includeStatics, coa)
    local allDcsUnits = {}
    local allDcsGroups = ctld_groups.getGroupsOfCoalition(coa)
    for _, group in pairs(allDcsGroups) do
        for _, unit in pairs(group:getUnits()) do
            table.insert(allDcsUnits, unit)
        end
    end
    if includeStatics then
        local allDcsStatics = ctld_groups.getStaticsOfCoalition(coa)
        for _, staticUnit in pairs(allDcsStatics) do
            table.insert(allDcsUnits, staticUnit)
        end
    end
    return allDcsUnits
end

function ctld_groups.findUnitsInCircle(center, radius, includeStatics)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("findUnitsInCircle(radius=%s)", tostring(radius)))
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("center=%s", ctld_groups.p(center)))


    local allDcsUnits = ctld_groups.getUnitsOfAllCoalitions(includeStatics)
    
    local result = {}
    for _, unit in pairs(allDcsUnits) do
        local pos = unit:getPosition().p
        if pos then -- you never know O.o
            local name = unit:getName()
            distanceFromCenter = ((pos.x - center.x)^2 + (pos.z - center.z)^2)^0.5
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("name=%s; distanceFromCenter=%s", tostring(name), ctld_groups.p(distanceFromCenter)))
            if distanceFromCenter <= radius then
                result[name] = unit
            end
        end
    end
    return result
end

--- modified version of mist.getGroupRoute that returns raw DCS group data
function ctld_groups.getGroupData(groupIdent)
    -- refactor to search by groupId and allow groupId and groupName as inputs
    local gpId = groupIdent
        if mist.DBs.MEgroupsByName[groupIdent] then
            gpId = mist.DBs.MEgroupsByName[groupIdent].groupId
        else
            ctld_groups.loggers.get(ctld_groups.Id):info(groupIdent..' not found in mist.DBs.MEgroupsByName')
        end

    for coa_name, coa_data in pairs(env.mission.coalition) do
        if (coa_name == 'red' or coa_name == 'blue') and type(coa_data) == 'table' then
            if coa_data.country then --there is a country table
                for cntry_id, cntry_data in pairs(coa_data.country) do
                    for obj_type_name, obj_type_data in pairs(cntry_data) do
                        if obj_type_name == "helicopter" or obj_type_name == "ship" or obj_type_name == "plane" or obj_type_name == "vehicle" then	-- only these types have points
                            if ((type(obj_type_data) == 'table') and obj_type_data.group and (type(obj_type_data.group) == 'table') and (#obj_type_data.group > 0)) then	--there's a group!
                                for group_num, group_data in pairs(obj_type_data.group) do
                                    if group_data and group_data.groupId == gpId	then -- this is the group we are looking for
                                        return group_data
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    
    ctld_groups.loggers.get(ctld_groups.Id):info(' no group data found for '..groupIdent)
    return nil
end

function ctld_groups.findInTable(data, key)
    local result = nil
    if data then
        result = data[key]
    end
    if result then 
        ctld_groups.loggers.get(ctld_groups.Id):trace(".findInTable found ".. key)
    end
    return result
end

function ctld_groups.getTankerData(tankerGroupName)
    ctld_groups.loggers.get(ctld_groups.Id):trace("getTankerData " .. tankerGroupName)
    local result = nil
    local tankerData = ctld_groups.getGroupData(tankerGroupName)
    if tankerData then
        result = {}
        -- find callsign
        local units = ctld_groups.findInTable(tankerData, "units")
        if units and units[1] then 
            local callsign = ctld_groups.findInTable(units[1], "callsign")
            if callsign then 
                local name = ctld_groups.findInTable(callsign, "name")
                if name then 
                    result.tankerCallsign = name
                end
            end
        end

        -- find frequency
        local communication = ctld_groups.findInTable(tankerData, "communication")
        if communication == true then
            local frequency = ctld_groups.findInTable(tankerData, "frequency")
            if frequency then 
                result.tankerFrequency = frequency
            end
        end
        local route = ctld_groups.findInTable(tankerData, "route")
        local points = ctld_groups.findInTable(route, "points")
        if points then
            ctld_groups.loggers.get(ctld_groups.Id):trace("found a " .. #points .. "-points route for tanker " .. tankerGroupName)
            for i, point in pairs(points) do
                ctld_groups.loggers.get(ctld_groups.Id):trace("found point #" .. i)
                local task = ctld_groups.findInTable(point, "task")
                if task then
                    local tasks = task.params.tasks
                    if (tasks) then
                        ctld_groups.loggers.get(ctld_groups.Id):trace("found " .. #tasks .. " tasks")
                        for j, task in pairs(tasks) do
                            ctld_groups.loggers.get(ctld_groups.Id):trace("found task #" .. j)
                            if task.params then
                                ctld_groups.loggers.get(ctld_groups.Id):trace("has .params")
                                if task.params.action then
                                    ctld_groups.loggers.get(ctld_groups.Id):trace("has .action")
                                    if task.params.action.params then
                                        ctld_groups.loggers.get(ctld_groups.Id):trace("has .params")
                                        if task.params.action.params.channel then
                                            ctld_groups.loggers.get(ctld_groups.Id):trace("has .channel")
                                            ctld_groups.loggers.get(ctld_groups.Id):info("Found a TACAN task for tanker " .. tankerGroupName)
                                            result.tankerTacanTask = task
                                            result.tankerTacanChannel = task.params.action.params.channel
                                            result.tankerTacanMode = task.params.action.params.modeChannel
                                            break
                                        end
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    return result
end

function ctld_groups.outTextForUnit(unitName, message, duration)
    local groupId = nil
    if unitName then
    local unit = Unit.getByName(unitName)
    if unit then 
        local group = unit:getGroup()
        if group then 
            groupId = group:getID()
        end
    end
    end
    if groupId then 
        trigger.action.outTextForGroup(groupId, message, duration)
    else
        trigger.action.outText(message, duration)
    end
end

--- Weather Report. Report pressure QFE/QNH, temperature, wind at certain location.
--- stolen from the weatherReport script and modified to fit our usage
function ctld_groups.weatherReport(vec3, alt, withLASTE)
     
    -- Get Temperature [K] and Pressure [Pa] at vec3.
    local T
    local Pqfe
    if not alt then
        alt = ctld_groups.getLandHeight(vec3)
    end

    -- At user specified altitude.
    T,Pqfe=atmosphere.getTemperatureAndPressure({x=vec3.x, y=alt, z=vec3.z})
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("T = %.1f, Pqfe = %.2f", T,Pqfe))
    
    -- Get pressure at sea level.
    local _,Pqnh=atmosphere.getTemperatureAndPressure({x=vec3.x, y=0, z=vec3.z})
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("Pqnh = %.2f", Pqnh))
    
    -- Convert pressure from Pascal to hecto Pascal.
    Pqfe=Pqfe/100
    Pqnh=Pqnh/100 
     
    -- Pressure unit conversion hPa --> mmHg or inHg
    local _Pqnh=string.format("%.2f mmHg (%.2f inHg)", Pqnh * weathermark.hPa2mmHg, Pqnh * weathermark.hPa2inHg)
    local _Pqfe=string.format("%.2f mmHg (%.2f inHg)", Pqfe * weathermark.hPa2mmHg, Pqfe * weathermark.hPa2inHg)
   
    -- Temperature unit conversion: Kelvin to Celsius or Fahrenheit.
    T=T-273.15
    local _T=string.format('%d°C (%d°F)', T, weathermark._CelsiusToFahrenheit(T))
  
    -- Get wind direction and speed.
    local Dir,Vel=weathermark._GetWind(vec3, alt)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("Dir = %.1f, Vel = %.1f", Dir,Vel))

    -- Get Beaufort wind scale.
    local Bn,Bd=weathermark._BeaufortScale(Vel)
    
    -- Formatted wind direction.
    local Ds = string.format('%03d°', Dir)
      
    -- Velocity in player units.
    local Vs=string.format('%.1f m/s (%.1f kn)', Vel, Vel * weathermark.mps2knots) 
    
    -- Altitude.
    local _Alt=string.format("%d m (%d ft)", alt, alt * weathermark.meter2feet)
      
    local text="" 
    text=text..string.format("Altitude %s ASL\n",_Alt)
    text=text..string.format("QFE %.2f hPa = %s\n", Pqfe,_Pqfe)
    text=text..string.format("QNH %.2f hPa = %s\n", Pqnh,_Pqnh)
    text=text..string.format("Temperature %s\n",_T)
    if Vel > 0 then
        text=text..string.format("Wind from %s at %s (%s)", Ds, Vs, Bd)
    else
        text=text.."No wind"
    end

    local function getLASTEat(vec3, alt)
        local T,_=atmosphere.getTemperatureAndPressure({x=vec3.x, y=alt, z=vec3.z})
        local Dir,Vel=weathermark._GetWind(vec3, alt)
        local laste = string.format("\nFL%02d W%03d/%02d T%d", alt * weathermark.meter2feet / 1000, Dir, Vel * weathermark.mps2knots, T-273.15)
        return laste
    end

    if withLASTE then
        text=text.."\n\nLASTE:"
        text=text..getLASTEat(vec3, math.floor(((alt * weathermark.meter2feet + 2000)/1000)*1000+500)/weathermark.meter2feet)
        text=text..getLASTEat(vec3, math.floor(((alt * weathermark.meter2feet + 8000)/1000)*1000+500)/weathermark.meter2feet)
        text=text..getLASTEat(vec3, math.floor(((alt * weathermark.meter2feet + 16000)/1000)*1000+500)/weathermark.meter2feet)
        --text=text..getLASTEat(vec3, _Alt + 7500)
    end

    return text
end

local function _initializeCountriesAndCoalitions()
    ctld_groups.countriesByCoalition={}
    ctld_groups.coalitionByCountry={}

    local function _sortByImportance(c1,c2)
        local importantCountries = { ['usa']=true, ['russia']=true}
        if c1 then
            return importantCountries[c1:lower()]
        end
        return string.lower(c1) < string.lower(c2)
    end

    for coalitionName, countries in pairs(mist.DBs.units) do
        coalitionName = coalitionName:lower()
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("coalitionName=%s", ctld_groups.p(coalitionName)))

        if not ctld_groups.countriesByCoalition[coalitionName] then 
            ctld_groups.countriesByCoalition[coalitionName]={} 
        end
        for countryName, _ in pairs(countries) do
            countryName = countryName:lower()
            table.insert(ctld_groups.countriesByCoalition[coalitionName], countryName)
            ctld_groups.coalitionByCountry[countryName]=coalitionName:lower()
        end

        table.sort(ctld_groups.countriesByCoalition[coalitionName], _sortByImportance)
    end

    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("ctld_groups.countriesByCoalition=%s", ctld_groups.p(ctld_groups.countriesByCoalition)))
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("ctld_groups.coalitionByCountry=%s", ctld_groups.p(ctld_groups.coalitionByCountry)))
end

function ctld_groups.getCountryId(countryName)
    ctld_groups.loggers.get(ctld_groups.Id):trace("ctld_groups.getCountryId(%s)", ctld_groups.p(countryName))
    local countryName = string.lower(countryName or "")
    for id, name in pairs(country.name) do
        if name:lower() == countryName then
            return id
        end
    end
    return 0
end

function ctld_groups.getCountryForCoalition(coalition)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("ctld_groups.getCountryForCoalition(coalition=%s)", tostring(coalition)))
    local coalition = coalition
    if not coalition then 
        coalition = 1 
    end

    local coalitionName = nil
    if type(coalition) == "number" then
        if coalition == 1 then 
            coalitionName = "red" 
        elseif coalition == 2 then 
            coalitionName = "blue" 
        else
            coalitionName = "neutral" 
        end
    else
        coalitionName = tostring(coalition)
    end

    if coalitionName then
        coalitionName = coalitionName:lower()
    else
        return nil
    end

    if not ctld_groups.countriesByCoalition then 
        _initializeCountriesAndCoalitions() 
    end
    
    return ctld_groups.countriesByCoalition[coalitionName][1]
end

function ctld_groups.getCoalitionForCountry(countryName, asNumber)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("ctld_groups.getCoalitionForCountry(countryName=%s, asNumber=%s)", tostring(countryName), tostring(asNumber)))

    if countryName then
        countryName = countryName:lower()
    else
        return nil
    end

    if not ctld_groups.coalitionByCountry then 
        _initializeCountriesAndCoalitions() 
    end
    
    local result = ctld_groups.coalitionByCountry[countryName]
    if asNumber then
        if result == 'neutral' then result = 0 end
        if result == 'red' then result = 1 end
        if result == 'blue' then result = 2 end
    end
    return result
end

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- mission restart at a certain hour of the day
-------------------------------------------------------------------------------------------------------------------------------------------------------------
function ctld_groups._endMission(delay1, message1, delay2, message2, delay3, message3)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("ctld_groups._endMission(delay1=%s, message1=%s, delay2=%s, message2=%s, delay3=%s, message3=%s)", ctld_groups.p(delay1), ctld_groups.p(message1), ctld_groups.p(delay2), ctld_groups.p(message2), ctld_groups.p(delay3), ctld_groups.p(message3)))

    if not delay1 then
        -- no more delay, let's end this !
        trigger.action.outText("Ending mission !",30)
        ctld_groups.loggers.get(ctld_groups.Id):info("ending mission")
        trigger.action.setUserFlag("666", 1)
    else 
        -- show the message
        trigger.action.outText(message1,30)
        -- schedule this function after "delay1" seconds
        ctld_groups.loggers.get(ctld_groups.Id):info(string.format("schedule ctld_groups._endMission after %d seconds", delay1))
        mist.scheduleFunction(ctld_groups._endMission, {delay2, message2, delay3, message3}, timer.getTime()+delay1)
    end
end

function ctld_groups._checkForEndMission(endTimeInSeconds, checkIntervalInSeconds, checkMessage, delay1, message1, delay2, message2, delay3, message3)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("ctld_groups._checkForEndMission(endTimeInSeconds=%s, checkIntervalInSeconds=%s, checkMessage=%s, delay1=%s, message1=%s, delay2=%s, message2=%s, delay3=%s, message3=%s)", ctld_groups.p(endTimeInSeconds), ctld_groups.p(checkIntervalInSeconds), ctld_groups.p(checkMessage), ctld_groups.p(delay1), ctld_groups.p(message1), ctld_groups.p(delay2), ctld_groups.p(message2), ctld_groups.p(delay3), ctld_groups.p(message3)))
    
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("timer.getAbsTime()=%d", timer.getAbsTime()))

    if timer.getAbsTime() >= endTimeInSeconds then
        ctld_groups.loggers.get(ctld_groups.Id):trace("calling ctld_groups._endMission")
        ctld_groups._endMission(delay1, message1, delay2, message2, delay3, message3)
    else
        -- output the message if specified
        if checkMessage then
            trigger.action.outText(checkMessage,30)
        end
        -- schedule this function after a delay
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("schedule ctld_groups._checkForEndMission after %d seconds", checkIntervalInSeconds))
        mist.scheduleFunction(ctld_groups._checkForEndMission, {endTimeInSeconds, checkIntervalInSeconds, checkMessage, delay1, message1, delay2, message2, delay3, message3}, timer.getTime()+checkIntervalInSeconds)
    end
end

function ctld_groups.endMissionAt(endTimeHour, endTimeMinute, checkIntervalInSeconds, checkMessage, delay1, message1, delay2, message2, delay3, message3)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("ctld_groups.endMissionAt(endTimeHour=%s, endTimeMinute=%s, checkIntervalInSeconds=%s, checkMessage=%s, delay1=%s, message1=%s, delay2=%s, message2=%s, delay3=%s, message3=%s)", ctld_groups.p(endTimeHour), ctld_groups.p(endTimeMinute), ctld_groups.p(checkIntervalInSeconds), ctld_groups.p(checkMessage), ctld_groups.p(delay1), ctld_groups.p(message1), ctld_groups.p(delay2), ctld_groups.p(message2), ctld_groups.p(delay3), ctld_groups.p(message3)))

    local endTimeInSeconds = endTimeHour * 3600 + endTimeMinute * 60
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("endTimeInSeconds=%d", endTimeInSeconds))
    ctld_groups._checkForEndMission(endTimeInSeconds, checkIntervalInSeconds, checkMessage, delay1, message1, delay2, message2, delay3, message3)    
end

function ctld_groups.randomlyChooseFrom(aTable, bias)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("randomlyChooseFrom(%d):%s",bias or 0, ctld_groups.p(aTable)))
    local index = math.floor(math.random(1, #aTable)) + (bias or 0)
    if index < 1 then index = 1 end
    if index > #aTable then index = #aTable end
    return aTable[index]
end

function ctld_groups.safeUnpack(package)
    if type(package) == 'table' then
        return unpack(package)
    else
        return package
    end
end

function ctld_groups.getRandomizableNumeric_random(val)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("getRandomizableNumeric_random(%s)", tostring(val)))
    local nVal = tonumber(val)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("nVal=%s", tostring(nVal)))
    if nVal == nil then 
        --[[
        local dashPos = nil
        for i = 1, #val do
            local c = val:sub(i,i)
            if c == '-' then 
                dashPos = i
                break
            end
        end
        if dashPos then 
            local lower = val:sub(1, dashPos-1)
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("lower=%s", tostring(lower)))
            if lower then 
                lower = tonumber(lower)
            end
            if lower == nil then lower = 0 end
            local upper = val:sub(dashPos+1)
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("upper=%s", tostring(upper)))
            if upper then 
                upper = tonumber(upper)
            end
            if upper == nil then upper = 5 end
            nVal = math.random(lower, upper)
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("random nVal=%s", tostring(nVal)))
        end
        --]]

        -- [[
        
        if val == "0-1" then nVal = math.random(1,2) end
        if val == "0-2" then nVal = math.random(1,2) end
        if val == "0-3" then nVal = math.random(1,3) end
        if val == "0-4" then nVal = math.random(1,4) end
        if val == "0-5" then nVal = math.random(1,5) end
        if val == "0-6" then nVal = math.random(1,6) end
        if val == "0-7" then nVal = math.random(1,7) end
        if val == "0-8" then nVal = math.random(1,8) end
        if val == "0-9" then nVal = math.random(1,9) end
    
        if val == "1-2" then nVal = math.random(1,2) end
        if val == "1-3" then nVal = math.random(1,3) end
        if val == "1-4" then nVal = math.random(1,4) end
        if val == "1-5" then nVal = math.random(1,5) end
        if val == "1-6" then nVal = math.random(1,6) end
        if val == "1-7" then nVal = math.random(1,7) end
        if val == "1-8" then nVal = math.random(1,8) end
        if val == "1-9" then nVal = math.random(1,9) end

        if val == "2-3" then nVal = math.random(2,3) end
        if val == "2-4" then nVal = math.random(2,4) end
        if val == "2-5" then nVal = math.random(2,5) end
        if val == "1-6" then nVal = math.random(1,6) end
        if val == "1-7" then nVal = math.random(1,7) end
        if val == "1-8" then nVal = math.random(1,8) end
        if val == "1-9" then nVal = math.random(1,9) end

        if val == "3-4" then nVal = math.random(3,4) end
        if val == "3-5" then nVal = math.random(3,5) end
        if val == "3-6" then nVal = math.random(3,6) end
        if val == "3-7" then nVal = math.random(3,7) end
        if val == "3-8" then nVal = math.random(3,8) end
        if val == "3-9" then nVal = math.random(3,9) end

        if val == "4-5" then nVal = math.random(4,5) end
        if val == "4-6" then nVal = math.random(4,6) end
        if val == "4-7" then nVal = math.random(4,7) end
        if val == "4-8" then nVal = math.random(4,8) end
        if val == "4-9" then nVal = math.random(4,9) end

        if val == "5-6" then nVal = math.random(5,6) end
        if val == "5-7" then nVal = math.random(5,7) end
        if val == "5-8" then nVal = math.random(5,8) end
        if val == "5-9" then nVal = math.random(5,9) end

        if val == "6-7" then nVal = math.random(6,7) end
        if val == "6-8" then nVal = math.random(6,8) end
        if val == "6-9" then nVal = math.random(6,9) end

        if val == "7-8" then nVal = math.random(7,8) end
        if val == "7-9" then nVal = math.random(7,9) end

        if val == "8-9" then nVal = math.random(8,9) end

        if val == "10-15" then nVal = math.random(10,15) end
        --]]

        --[[
        if val == "1-2" then nVal = 2 end
        if val == "1-3" then nVal = 3 end
        if val == "1-4" then nVal = 3 end
        if val == "1-5" then nVal = 3 end

        if val == "2-3" then nVal = 2 end
        if val == "2-4" then nVal = 3 end
        if val == "2-5" then nVal = 3 end

        if val == "3-4" then nVal = 3 end
        if val == "3-5" then nVal = 4 end

        if val == "4-5" then nVal = 4 end

        if val == "5-10" then nVal = 7 end
        
        if val == "10-15" then nVal = 12 end
        --]]

    --[[
        -- maybe it's a range ?
        local dashPos = val:find("-")
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("dashPos=%s", tostring(dashPos)))
        if dashPos then 
            local lower = val:sub(1, dashPos-1)
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("lower=%s", tostring(lower)))
            if lower then 
                lower = tonumber(lower)
            end
            if lower == nil then lower = 0 end
            local upper = val:sub(dashPos+1)
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("upper=%s", tostring(upper)))
            if upper then 
                upper = tonumber(upper)
            end
            if upper == nil then upper = 5 end
            nVal = math.random(lower, upper)
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("random nVal=%s", tostring(nVal)))
        end
        --]]
    end
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("nVal=%s", tostring(nVal)))
    return nVal
end

function ctld_groups.getRandomizableNumeric_norandom(val)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("getRandomizableNumeric_norandom(%s)", tostring(val)))
    local nVal = tonumber(val)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("nVal=%s", tostring(nVal)))
    if nVal == nil then 
        if val == "1-2" then nVal = 2 end
        if val == "1-3" then nVal = 3 end
        if val == "1-4" then nVal = 3 end
        if val == "1-5" then nVal = 3 end

        if val == "2-3" then nVal = 2 end
        if val == "2-4" then nVal = 3 end
        if val == "2-5" then nVal = 3 end

        if val == "3-4" then nVal = 3 end
        if val == "3-5" then nVal = 4 end

        if val == "4-5" then nVal = 4 end

        if val == "5-10" then nVal = 7 end
        
        if val == "10-15" then nVal = 12 end
    end
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("nVal=%s", tostring(nVal)))
    return nVal
end

function ctld_groups.getRandomizableNumeric(val)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("getRandomizableNumeric(%s)", tostring(val)))
    return ctld_groups.getRandomizableNumeric_random(val)
end

function ctld_groups.writeLineToTextFile(line, filename, filepath)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("writeLineToTextFile(%s, %s)", ctld_groups.p(line), ctld_groups.p(filename)))

    local l_lfs = lfs
    if not l_lfs and SERVER_CONFIG and SERVER_CONFIG.getModule then
        l_lfs = SERVER_CONFIG.getModule("lfs")
    end

    local l_io = io
    if not l_io and SERVER_CONFIG and SERVER_CONFIG.getModule then
        l_io = SERVER_CONFIG.getModule("io")
    end

    local l_os = os
    if not l_os and SERVER_CONFIG and SERVER_CONFIG.getModule then
        l_os = SERVER_CONFIG.getModule("os")
    end

    local filepath = filepath
    if not filepath and l_os then
        filepath = l_os.getenv("VEAF_EXPORT_DIR")
        if filepath then filepath = filepath .. "\\" end
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("filepath=%s", ctld_groups.p(filepath)))
    end
    if not filepath and l_os then
        filepath = l_os.getenv("TEMP")
        if filepath then filepath = filepath .. "\\" end
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("filepath=%s", ctld_groups.p(filepath)))
    end
    if not filepath and l_lfs then
        filepath = l_lfs.writedir()
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("filepath=%s", ctld_groups.p(filepath)))
    end

    if not filepath then
        return
    end

    local filename = filepath .. (filename or "default.log")

    local date = ""
    if l_os then
        date = l_os.date('%Y-%m-%d %H:%M:%S.000')
    end
    
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("filename=%s", ctld_groups.p(filename)))
    local file = l_io.open(filename, "a")
    if file then
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("file:write(%s)", ctld_groups.p(line)))
        file:write(string.format("[%s] %s\r\n", date, line))
        file:close()
    end
end

function ctld_groups.exportAsJson(data, name, jsonify, filename, export_path)
    local l_lfs = lfs
    if not l_lfs and SERVER_CONFIG and SERVER_CONFIG.getModule then
        l_lfs = SERVER_CONFIG.getModule("lfs")
    end

    local l_io = io
    if not l_io and SERVER_CONFIG and SERVER_CONFIG.getModule then
        l_io = SERVER_CONFIG.getModule("io")
    end

    local l_os = os
    if not l_os and SERVER_CONFIG and SERVER_CONFIG.getModule then
        l_os = SERVER_CONFIG.getModule("os")
    end

    local function writeln(file, text)
        file:write(text.."\r\n")
    end
    
    local export_path = export_path
    if not export_path and l_os then
        export_path = l_os.getenv("VEAF_EXPORT_DIR")
        if export_path then export_path = export_path .. "\\" end
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("export_path=%s", ctld_groups.p(export_path)))
    end
    if not export_path and l_os then
        export_path = l_os.getenv("TEMP")
        if export_path then export_path = export_path .. "\\" end
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("export_path=%s", ctld_groups.p(export_path)))
    end
    if not export_path and l_lfs then
        export_path = l_lfs.writedir()
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("export_path=%s", ctld_groups.p(export_path)))
    end
    
    if not export_path then
        return
    end
    
    local filename = filename or name .. ".json"
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("filename=%s", ctld_groups.p(filename)))
    
    ctld_groups.loggers.get(ctld_groups.Id):info("Dumping ".. name .." as json to "..filename .. " in "..export_path)

    local header =    '{\n'
    header = header .. '  "' .. name .. '": [\n'   

    local content = {}
    for key, value in pairs(data) do
        local line =  jsonify(key, value)
        table.insert(content, line)
    end
    local footer =    '\n'
    footer = footer .. ']\n'
    footer = footer .. '}\n'

    local file = l_io.open(export_path..filename, "w")
    writeln(file, header)
    writeln(file, table.concat(content, ",\n"))
    writeln(file, footer)
    file:close()
end

function ctld_groups.isUnitAlive(unit)
    return unit and unit:isExist() and unit:isActive()
end

function ctld_groups.getUnitLifeRelative(unit)
    if unit and ctld_groups.isUnitAlive(unit) then
        local life0=unit:getLife0()
        local lifeN=unit:getLife()
        return lifeN/life0
    else
        return 0
    end
end

function ctld_groups.setServerName(value)
    ctld_groups.config.SERVER_NAME = value
end

function ctld_groups.getPolygonFromUnits(unitNames)

    ctld_groups.loggers.get(ctld_groups.Id):debug(string.format("ctld_groups.getPolygonFromUnits()"))
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("unitNames = %s", ctld_groups.p(unitNames)))
    local polygon = {}
    for _, unitName in pairs(unitNames) do
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("unitName = %s", ctld_groups.p(unitName)))
        local unit = Unit.getByName(unitName)
        if not unit then
            local group = Group.getByName(unitName)
            if group then
                unit = group:getUnit(1)
            end
        end
        if unit then
            -- get position, place tracing marker and remove the unit
            local position = unit:getPosition().p
            unit:destroy()
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("position = %s", ctld_groups.p(position)))
            table.insert(polygon, mist.utils.deepCopy(position))
        end
    end
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("polygon = %s", ctld_groups.p(polygon)))
    return polygon
end

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Logging
-------------------------------------------------------------------------------------------------------------------------------------------------------------

ctld_groups.loggers = {}
ctld_groups.loggers.dict = {}

ctld_groups.Logger =
{
    -- technical name
    name = nil,
    -- logging level
    level = nil,
}
ctld_groups.Logger.__index = ctld_groups.Logger

ctld_groups.Logger.LEVEL = {
    ["error"]=1,
    ["warning"]=2,
    ["info"]=3,
    ["debug"]=4,
    ["trace"]=5,
}

function ctld_groups.Logger:new(name, level)
    local self = setmetatable({}, ctld_groups.Logger)
    self:setName(name)
    self:setLevel(level)
    return self
end

function ctld_groups.Logger:setName(value)
    self.name = value
    return self
end

function ctld_groups.Logger:getName()
    return self.name
end

function ctld_groups.Logger:setLevel(value, force)
    if ctld_groups.ForcedLogLevel then
        value = ctld_groups.ForcedLogLevel
    end
    local level = value
    if type(level) == "string" then
        level = ctld_groups.Logger.LEVEL[level:lower()]
    end
    if not level then 
        level = ctld_groups.Logger.LEVEL["info"]
    end
    if ctld_groups.BaseLogLevel < level and not force then
        level = ctld_groups.BaseLogLevel
    end
    self.level = level
    return self
end

function ctld_groups.Logger:getLevel()
    return self.level
end

function ctld_groups.Logger.splitText(text)
    local tbl = {}
    while text:len() > 4000 do
        local sub = text:sub(1, 4000)
        text = text:sub(4001)
        table.insert(tbl, sub)
    end
    table.insert(tbl, text)
    return tbl
end

function ctld_groups.Logger.formatText(text, ...)
    if not text then 
        return "" 
    end
    if type(text) ~= 'string' then
        text = ctld_groups.p(text)
    else
        if arg and arg.n and arg.n > 0 then
            local pArgs = {}
            for index,value in ipairs(arg) do
                pArgs[index] = ctld_groups.p(value)
            end
            text = text:format(unpack(pArgs))
        end            
    end
    local fName = nil
    local cLine = nil
    if debug then
        local dInfo = debug.getinfo(3)
        fName = dInfo.name
        cLine = dInfo.currentline
        -- local fsrc = dinfo.short_src
        --local fLine = dInfo.linedefined
    end
    if fName and cLine then
        return fName .. '|' .. cLine .. ': ' .. text
    elseif cLine then
        return cLine .. ': ' .. text
    else
        return ' ' .. text
    end
end

function ctld_groups.Logger:print(level, text)
    local texts = ctld_groups.Logger.splitText(text)
    local levelChar = 'E'
    local logFunction = env.error
    if level == ctld_groups.Logger.LEVEL["warning"] then
        levelChar = 'W'
        logFunction = env.warning
    elseif level == ctld_groups.Logger.LEVEL["info"] then
        levelChar = 'I'
        logFunction = env.info
    elseif level == ctld_groups.Logger.LEVEL["debug"] then
        levelChar = 'D'
        logFunction = env.info
    elseif level == ctld_groups.Logger.LEVEL["trace"] then
        levelChar = 'T'
        logFunction = env.info
    end
    for i = 1, #texts do
        if i == 1 then
            logFunction(self.name .. '|' .. levelChar .. '|' .. texts[i])
        else
            logFunction(texts[i])
        end
    end
end

function ctld_groups.Logger:error(text, ...)
    if self.level >= 1 then
        text = ctld_groups.Logger.formatText(text, unpack(arg))
        self:print(1, text)
    end
end

function ctld_groups.Logger:warn(text, ...)
    if self.level >= 2 then
        text = ctld_groups.Logger.formatText(text, unpack(arg))
        self:print(2, text)
    end
end

function ctld_groups.Logger:info(text, ...)
    if self.level >= 3 then
        text = ctld_groups.Logger.formatText(text, unpack(arg))
        self:print(3, text)
    end
end

function ctld_groups.Logger:debug(text, ...)
    if self.level >= 4 then
        text = ctld_groups.Logger.formatText(text, unpack(arg))
        self:print(4, text)
    end
end

function ctld_groups.Logger:trace(text, ...)
    if self.level >= 5 then
        text = ctld_groups.Logger.formatText(text, unpack(arg))
        self:print(5, text)
    end
end

function ctld_groups.Logger:marker(id, header, message, position, markersTable, radius, fillColor)
    if not id then
        id = 99999 
    end
    if self.level >= 5 then
        local correctedPos = {}
        correctedPos.x = position.x
        if not(position.z) then
            correctedPos.z = position.y
            correctedPos.y = position.alt
        else
            correctedPos.z = position.z
            correctedPos.y = position.y
        end
        if not (correctedPos.y) then
            correctedPos.y = 0
        end
        local message = message
        if header and id then
            message = header..id.." "..message
        end
        self:trace("creating trace marker #%s at point %s", id, ctld_groups.vecToString(correctedPos))
        if radius then
            trigger.action.circleToAll(-1, id, correctedPos, radius, fillColor, fillColor, 3, false)
        else
            trigger.action.markToAll(id, message, correctedPos, false) 
        end
        if markersTable then
            table.insert(markersTable, id)
            --self:trace("markersTable=%s", ctld_groups.p(markersTable))
        end
    end
    return id + 1
end

function ctld_groups.Logger:markerArrow(id, header, message, positionStart, positionEnd, markersTable, lineType, fillColor)
    if not id then
        id = 99999 
    end
    if self.level >= 5 then
        local points = { positionStart, positionEnd }
        for _, point in ipairs(points) do
            local correctedPos = {}
            correctedPos.x = point.x
            if not(point.z) then
                correctedPos.z = point.y
                correctedPos.y = point.alt
            else
                correctedPos.z = point.z
                correctedPos.y = point.y
            end
            if not (correctedPos.y) then
                correctedPos.y = 0
            end
            point.x = correctedPos.x
            point.y = correctedPos.y
            point.z = correctedPos.z
        end
        local positionStart = points[1]
        local positionEnd = points[2]

        local message = message
        if header and id then
            message = header..id.." "..message
        end
        
        self:trace("creating trace arrow #%s from point %s to point %s", id, ctld_groups.vecToString(positionStart), ctld_groups.vecToString(positionEnd))
        
        trigger.action.arrowToAll(-1, id, positionEnd, positionStart, fillColor, fillColor, lineType, false, message)
        if markersTable then
            table.insert(markersTable, id)
            --self:trace("markersTable=%s", ctld_groups.p(markersTable))
        end
    end
    return id + 1
end

function ctld_groups.Logger:markerQuad(id, header, message, points, markersTable, lineType, fillColor)
    if not id then
        id = 99999 
    end
    if self.level >= 5 then
        local points = points
        for _, point in ipairs(points) do
            local correctedPos = {}
            correctedPos.x = point.x
            if not(point.z) then
                correctedPos.z = point.y
                correctedPos.y = point.alt
            else
                correctedPos.z = point.z
                correctedPos.y = point.y
            end
            if not (correctedPos.y) then
                correctedPos.y = 0
            end
            point.x = correctedPos.x
            point.y = correctedPos.y
            point.z = correctedPos.z
        end

        local message = message
        if header and id then
            message = header..id.." "..message
        end
        
        self:trace("creating trace quad #%s", id)
        
        trigger.action.quadToAll(-1, id, points[1], points[2], points[3], points[4], fillColor, fillColor, lineType, false, message)
        if markersTable then
            table.insert(markersTable, id)
            --self:trace("markersTable=%s", ctld_groups.p(markersTable))
        end
    end
    return id + 1
end

function ctld_groups.Logger:cleanupMarkers(markersTable)
    local n=#markersTable
    for i=1,n do
        local markerId = markersTable[i]
        markersTable[i] = nil
        self:trace("deleting trace marker #%s at pos", markerId, i)
        trigger.action.removeMark(markerId)    
    end   
end

function ctld_groups.loggers.setBaseLevel(level) 
    ctld_groups.BaseLogLevel = level
    -- reset all loggers level if lower than the base level
    for name, logger in pairs(ctld_groups.loggers.dict) do
        logger:setLevel(logger:getLevel())
    end
end

function ctld_groups.loggers.new(loggerId, level) 
    if not loggerId or #loggerId == 0 then
        return nil
    end
    local result = ctld_groups.Logger:new(loggerId:upper(), level)
    ctld_groups.loggers.dict[loggerId:lower()] = result
    return result
end

function ctld_groups.loggers.get(loggerId) 
    local result = nil
    if loggerId and #loggerId > 0 then
        result = ctld_groups.loggers.dict[loggerId:lower()]
    end
    if not result then 
        result = ctld_groups.loggers.get("ctld_groups")
    end
    return result
end

if ctld_groups.Development then
    ctld_groups.loggers.setBaseLevel(ctld_groups.Logger.LEVEL["trace"])
end

ctld_groups.loggers.new(ctld_groups.Id, ctld_groups.LogLevel)

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Quick Reaction Alert - https://en.wikipedia.org/wiki/Quick_Reaction_Alert
-------------------------------------------------------------------------------------------------------------------------------------------------------------
CtldGroupsQRA =
{
    -- technical name (DCS zone name)
    name = nil,
    -- description for the briefing
    description = nil,
    -- aircraft groups forming the QRA
    groups = nil,
    -- coalition for the QRA
    coalition = nil,
    -- coalitions the QRA is defending against
    ennemyCoalitions = nil,
    -- message when the QRA is triggered
    messageStart = nil,
    -- message when the QRA is destroyed
    messageDestroyed = nil,
    -- message when the QRA is ready
    messageReady = nil,
    -- silent means no message is emitted
    silent = nil,
    -- radius of the defenders groups spawn
    radius = nil,
    -- react when helicopters enter the zone
    reactOnHelicopters = nil,

    timer = nil,
    state = nil,
    _enemyHumanUnits = nil
}
CtldGroupsQRA.__index = CtldGroupsQRA

CtldGroupsQRA.Id = "QRA"
--CtldGroupsQRA.LogLevel = "debug"

ctld_groups.loggers.new(CtldGroupsQRA.Id, CtldGroupsQRA.LogLevel)

CtldGroupsQRA.STATUS_READY = 1
CtldGroupsQRA.STATUS_ACTIVE = 2
CtldGroupsQRA.STATUS_DEAD = 3

CtldGroupsQRA.WATCHDOG_DELAY = 5

CtldGroupsQRA.DEFAULT_MESSAGE_START = "%s is deployed"
CtldGroupsQRA.DEFAULT_MESSAGE_DESTROYED = "%s has been destroyed"
CtldGroupsQRA.DEFAULT_MESSAGE_READY = "%s is ready"

function CtldGroupsQRA:new()
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA:new()"))
    local self = setmetatable({}, CtldGroupsQRA)
    self.name = nil
    self.description = nil
    self.groups = {}
    self.coalition = nil
    self.ennemyCoalitions = {}
    self.messageStart = CtldGroupsQRA.DEFAULT_MESSAGE_START
    self.messageDestroyed = CtldGroupsQRA.DEFAULT_MESSAGE_DESTROYED
    self.messageReady = CtldGroupsQRA.DEFAULT_MESSAGE_READY
    self.silent = false
    self.radius = 0
    self.reactOnHelicopters = false
    
    self._enemyHumanUnits = nil
    self.timer = 0
    self.state = nil
    return self
end

function CtldGroupsQRA:setName(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[]:setName(%s)", ctld_groups.p(value)))
    self.name = value
    return self
end

function CtldGroupsQRA:getName()
    return self.name
end

function CtldGroupsQRA:setDescription(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:setDescription(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    self.description = value
    return self
end

function CtldGroupsQRA:getDescription()
    return self.description or self.name
end

function CtldGroupsQRA:addGroup(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:addGroup(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    table.insert(self.groups, value)
    return self
end

function CtldGroupsQRA:getGroups()
    return self.groups
end

function CtldGroupsQRA:setCoalition(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:setCoalition(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    self.coalition = value
    return self
end

function CtldGroupsQRA:getCoalition()
    return self.coalition
end

function CtldGroupsQRA:addEnnemyCoalition(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:addEnnemyCoalition(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    self.ennemyCoalitions[value] = value
    return self
end

function CtldGroupsQRA:getEnnemyCoalitions()
    return self.ennemyCoalitions
end

function CtldGroupsQRA:setMessageStart(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:setMessageStart(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    self.messageStart = value
    return self
end

function CtldGroupsQRA:getMessageStart()
    return self.messageStart
end

function CtldGroupsQRA:setMessageDestroyed(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:setMessageDestroyed(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    self.messageDestroyed = value
    return self
end

function CtldGroupsQRA:getMessageDestroyed()
    return self.messageDestroyed
end

function CtldGroupsQRA:setMessageReady(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:setMessageReady(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    self.messageReady = value
    return self
end

function CtldGroupsQRA:getMessageReady()
    return self.messageReady
end

function CtldGroupsQRA:setSilent(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[]:setSilent(%s)", ctld_groups.p(value)))
    self.silent = value
    return self
end

function CtldGroupsQRA:isSilent()
    return self.silent
end

function CtldGroupsQRA:setReactOnHelicopters()
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace("CtldGroupsQRA[]:setReactOnHelicopters()")
    self.reactOnHelicopters = true
    return self
end

function CtldGroupsQRA:isReactOnHelicopters()
    return self.reactOnHelicopters
end

function CtldGroupsQRA:setRadius(value)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[]:setRadius(%s)", ctld_groups.p(value)))
    self.radius = value
    return self
end

function CtldGroupsQRA:getRadius()
    return self.radius
end




function CtldGroupsQRA:_getEnemyHumanUnits()
    --ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:_getEnemyHumanUnits() - computing", ctld_groups.p(self.name)))
    if not self._enemyHumanUnits then
        ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:_getEnemyHumanUnits() - computing", ctld_groups.p(self.name)))
        self._enemyHumanUnits = {}
        ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("self:getEnnemyCoalitions()[]=%s", ctld_groups.p(self:getEnnemyCoalitions())))
        for name, unit in pairs(mist.DBs.humansByName) do
            --ctld_groups.loggers.get(CtldGroupsQRA.Id):trace("unit=%s", unit)
            ctld_groups.loggers.get(CtldGroupsQRA.Id):trace("unit.unitName=%s", unit.unitName)
            ctld_groups.loggers.get(CtldGroupsQRA.Id):trace("unit.groupName=%s", unit.groupName)
            ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("unit.coalition=%s", ctld_groups.p(unit.coalition)))
            local coalitionId = 0
            if unit.coalition then
                if unit.coalition:lower() == "red" then
                    coalitionId = coalition.side.RED
                elseif unit.coalition:lower() == "blue" then
                    coalitionId = coalition.side.BLUE
                end
            end                    
            if self:getEnnemyCoalitions()[coalitionId] then
                if unit.category then
                    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace("unit.category=%s", unit.category)
                    if     (unit.category == "plane")
                        or (unit.category == "helicopter" and self:isReactOnHelicopters())
                    then
                        ctld_groups.loggers.get(CtldGroupsQRA.Id):trace("adding unit to enemy human units for QRA")
                        table.insert(self._enemyHumanUnits, unit.unitName)
                    end
                end
            end
        end
    end
    return self._enemyHumanUnits
end

function CtldGroupsQRA:check()
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:check()", ctld_groups.p(self.name)))
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("self.state=%s", ctld_groups._p(self.state)))

    local unitNames = self:_getEnemyHumanUnits()
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("unitNames=%s", ctld_groups.p(unitNames)))
    local unitsInZone = mist.getUnitsInZones(unitNames, {self:getName()})
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("unitsInZone=%s", ctld_groups._p(unitsInZone)))
    if (self.state == CtldGroupsQRA.STATUS_READY) and (unitsInZone and #unitsInZone > 0) then
        -- trigger the QRA
        self:deploy()
    elseif (self.state == CtldGroupsQRA.STATUS_DEAD) and (not unitsInZone or #unitsInZone == 0) then
        -- rearm the QRA
        self:rearm()
    elseif (self.state == CtldGroupsQRA.STATUS_ACTIVE) then
        local qraAlive = false
        for _, groupName in pairs(self:getGroups()) do
            if Group.getByName(groupName) then
                qraAlive = true
            end
        end
        if not qraAlive then
            -- signal QRA destroyed
            self:destroyed()
        end
    end

    mist.scheduleFunction(CtldGroupsQRA.check, {self}, timer.getTime() + CtldGroupsQRA.WATCHDOG_DELAY)    
end

function CtldGroupsQRA:deploy()
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:deploy()", ctld_groups.p(self.name)))
    if not self:isSilent() then
        local msg = string.format(self:getMessageStart(), self:getDescription())
        for coalition, _ in pairs(self:getEnnemyCoalitions()) do
            trigger.action.outTextForCoalition(coalition, msg, 15)
        end
    end
    for _, groupName in pairs(self:getGroups()) do
		local vars = {}
		vars.gpName = groupName
		vars.action = 'respawn'
		vars.radius = self:getRadius()
        vars.route = mist.getGroupRoute(groupName, 'task')
		mist.teleportToPoint(vars) -- respawn with radius
    end
    self.state = CtldGroupsQRA.STATUS_ACTIVE
end

function CtldGroupsQRA:destroyed()
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:destroyed()", ctld_groups.p(self.name)))
    if not self:isSilent() then
        local msg = string.format(self:getMessageDestroyed(), self:getDescription())
        for coalition, _ in pairs(self:getEnnemyCoalitions()) do
            trigger.action.outTextForCoalition(coalition, msg, 15)
        end
    end
    self.state = CtldGroupsQRA.STATUS_DEAD
end

function CtldGroupsQRA:rearm(silent)
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:rearm()", ctld_groups.p(self.name)))
    if not self:isSilent() and not silent then
        local msg = string.format(self:getMessageReady(), self:getDescription())
        for coalition, _ in pairs(self:getEnnemyCoalitions()) do
            trigger.action.outTextForCoalition(coalition, msg, 15) 
        end
    end
    for _, groupName in pairs(self:getGroups()) do
        local group = Group.getByName(groupName)
        if group then
            group:destroy()
        end
    end
    self.state = CtldGroupsQRA.STATUS_READY
end

function CtldGroupsQRA:start()
    ctld_groups.loggers.get(CtldGroupsQRA.Id):trace(string.format("CtldGroupsQRA[%s]:start()", ctld_groups.p(self.name)))
    self:rearm() -- TODO set true
    self:check()
end

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- unique identifers
-------------------------------------------------------------------------------------------------------------------------------------------------------------

ctld_groups.UNIQUE_ID = 10000 + math.random(50,500)

function ctld_groups.getUniqueIdentifier()
    ctld_groups.UNIQUE_ID = ctld_groups.UNIQUE_ID + 1
    return ctld_groups.UNIQUE_ID
end

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- lines and figures on the map
-------------------------------------------------------------------------------------------------------------------------------------------------------------

CtldGroupsDrawingOnMap =
{
    -- technical name (identifier)
    name = nil,
    -- coalition
    coalition = nil,
    -- points forming the drawing
    points = nil,
    -- color ({r, g, b, a})
    color = nil,
    -- fill color ({r, g, b, a})
    fillColor = nil,
    -- type of line (member of CtldGroupsDrawingOnMap.LINE_TYPE)
    lineType = nil,
    -- if true, the line is an arrow
    isArrow = nil,
    -- marker ids
    dcsMarkerIds = nil
}
CtldGroupsDrawingOnMap.__index = CtldGroupsDrawingOnMap

-- Type of line marking the zone
-- 0  No Line
-- 1  Solid
-- 2  Dashed
-- 3  Dotted
-- 4  Dot Dash
-- 5  Long Dash
-- 6  Two Dash
CtldGroupsDrawingOnMap.LINE_TYPE = {
    ["none"] = 0,
    ["solid"] = 1,
    ["dashed"] = 2,
    ["dotted"] = 3,
    ["dotdash"] = 4,
    ["longdash"] = 5,
    ["twodashes"] = 6
}

CtldGroupsDrawingOnMap.COLORS = {
    ["transparent"] = {0, 0, 0, 0},
    ["black"] = {0, 0, 0, 1},
    ["white"] = {1, 1, 1, 1},
    ["red"] = {1, 0, 0, 1},
    ["green"] = {0, 1, 0, 1},
    ["blue"] = {0, 0, 1, 1}
}

CtldGroupsDrawingOnMap.DEFAULT_COLOR = {170/255, 10/255, 0/255, 220/255}
CtldGroupsDrawingOnMap.DEFAULT_FILLCOLOR = {170/255, 10/255, 0/255, 170/255}

function CtldGroupsDrawingOnMap:new()
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap:new()"))
    local self = setmetatable({}, CtldGroupsDrawingOnMap)
    self.name = nil
    self.coalition = -1
    self.points = {}
    self.color = CtldGroupsDrawingOnMap.DEFAULT_COLOR
    self.fillColor = CtldGroupsDrawingOnMap.DEFAULT_FILLCOLOR
    self.lineType = CtldGroupsDrawingOnMap.LINE_TYPE.solid
    self.isArrow = false
    self.dcsMarkerIds = {}
    return self
end

function CtldGroupsDrawingOnMap:setName(value)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[]:setName(%s)", ctld_groups.p(value)))
    self.name = value
    return self
end

function CtldGroupsDrawingOnMap:getName()
    return self.name
end
 
function CtldGroupsDrawingOnMap:setCoalition(value)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:setCoalition(%s)", ctld_groups.p(self:getName()), ctld_groups.p(value)))
    self.coalition = value
    return self
end

function CtldGroupsDrawingOnMap:getCoalition()
    return self.coalition
end

function CtldGroupsDrawingOnMap:addPoint(value)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:addPoint(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    table.insert(self.points, 1, mist.utils.deepCopy(value))
    return self
end

function CtldGroupsDrawingOnMap:addPoints(value)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:addPoints(%s)", ctld_groups.p(self.name), ctld_groups.p(value)))
    if value and #value > 0 then
        for _, item in pairs(value) do
            self:addPoint(item)
        end
    end
    return self
end

function CtldGroupsDrawingOnMap:setPointsFromUnits(unitNames)
    ctld_groups.loggers.get(ctld_groups.Id):debug(string.format("CtldGroupsDrawingOnMap[%s]:setPointsFromUnits()", ctld_groups.p(self.name)))
    local polygon = ctld_groups.getPolygonFromUnits(unitNames)
    self:addPoints(polygon)
    return self
end

function CtldGroupsDrawingOnMap:setColor(value)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:setColor(%s)", ctld_groups.p(self:getName()), ctld_groups.p(value)))
    if value and type(value) == "string" then
        value = CtldGroupsDrawingOnMap.COLORS[value:lower()]
    end
    if value then
        self.color = mist.utils.deepCopy(value)
    end
    return self
end

function CtldGroupsDrawingOnMap:setFillColor(value)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:setFillColor(%s)", ctld_groups.p(self:getName()), ctld_groups.p(value)))
    if value and type(value) == "string" then
        value = CtldGroupsDrawingOnMap.COLORS[value:lower()]
    end
    if value then
        self.fillColor = mist.utils.deepCopy(value)
    end
    return self
end

function CtldGroupsDrawingOnMap:setLineType(value)
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:setLineType(%s)", ctld_groups.p(self:getName()), ctld_groups.p(value)))
    if value and type(value) == "string" then
        value = CtldGroupsDrawingOnMap.LINE_TYPE[value:lower()]
    end
    if value then
        self.lineType = value
    end
    return self
end

function CtldGroupsDrawingOnMap:setArrow()
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:setArrow()", ctld_groups.p(self:getName())))
    self.isArrow = true
    return self
end

function CtldGroupsDrawingOnMap:draw()
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:draw()", ctld_groups.p(self:getName())))

    -- start by erasing the drawing if it already is drawn
    self:erase()

    -- then draw it
    local lastPoint = nil
    local firstPoint = nil
    for _, point in pairs(self.points) do
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("drawing line [%s] - [%s]", ctld_groups.p(lastPoint), ctld_groups.p(point)))
        local id = ctld_groups.getUniqueIdentifier()
        if lastPoint then
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("id=[%s]", ctld_groups.p(id)))
            if self.isArrow then
                trigger.action.arrowToAll(self:getCoalition(), id, lastPoint, point, self.color, self.fillColor, self.lineType, true)
            else
                trigger.action.lineToAll(self:getCoalition(), id, lastPoint, point, self.color, self.lineType, true)
            end
        else
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("setting firstPoint to [%s]", ctld_groups.p(point)))
            trigger.action.markToCoalition(id, self.name, point, self.coalition, true, nil)
            firstPoint = point
        end
        table.insert(self.dcsMarkerIds, id)
        lastPoint = point
    end

    -- finish the polygon
    if firstPoint and lastPoint and #self.points > 2 and not self.isArrow then
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("finishing the polygon"))
        local id = ctld_groups.getUniqueIdentifier()
        ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("id=[%s]", ctld_groups.p(id)))
        if self.isArrow then
            trigger.action.arrowToAll(self:getCoalition(), id, lastPoint, firstPoint, self.color, self.fillColor, self.lineType, true)
        else
            trigger.action.lineToAll(self:getCoalition(), id, lastPoint, firstPoint, self.color, self.lineType, true)
        end
        table.insert(self.dcsMarkerIds, id)
    end
end

function CtldGroupsDrawingOnMap:erase()
    ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("CtldGroupsDrawingOnMap[%s]:erase()", ctld_groups.p(self:getName())))
    if self.dcsMarkerIds then
        for _, id in pairs(self.dcsMarkerIds) do
            ctld_groups.loggers.get(ctld_groups.Id):trace(string.format("removing mark id=[%s]", ctld_groups.p(id)))
            trigger.action.removeMark(id)
        end
    end
end

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- initialisation
-------------------------------------------------------------------------------------------------------------------------------------------------------------

-- initialize the random number generator to make it almost random
math.random(); math.random(); math.random()

--- Enable/Disable error boxes displayed on screen.
env.setErrorMessageBoxEnabled(false)

ctld_groups.loggers.get(ctld_groups.Id):info("Loading version %s", ctld_groups.Version)
ctld_groups.loggers.get(ctld_groups.Id):info("ctld_groups.Development=%s", ctld_groups.Development)
ctld_groups.loggers.get(ctld_groups.Id):info("ctld_groups.SecurityDisabled=%s", ctld_groups.SecurityDisabled)
--ctld_groups.loggers.get(ctld_groups.Id):info("ctld_groups.Debug=%s", ctld_groups.Debug)
--ctld_groups.loggers.get(ctld_groups.Id):info("ctld_groups.Trace=%s", ctld_groups.Trace)

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-- changes to CTLD 
-------------------------------------------------------------------------------------------------------------------------------------------------------------
if ctld then
    ctld_groups.loggers.get(ctld_groups.Id):info(string.format("Setting up CTLD"))

    -- change the init function so we can call it whenever we want
    ctld.skipInitialisation = true

    -- logging change
    ctld.p = ctld_groups.p
    ctld.Id = "CTLD"
    --ctld.LogLevel = "info"
    ctld.LogLevel = "debug"

    ctld.logger = ctld_groups.loggers.new(ctld.Id, ctld.LogLevel)

    ctld.logError = function(message)
        ctld_groups.loggers.get(ctld.Id):error(message)
    end

    ctld.logInfo = function(message)
        ctld_groups.loggers.get(ctld.Id):info(message)
    end    

    ctld.logDebug = function(message)
        ctld_groups.loggers.get(ctld.Id):debug(message)
    end    

    ctld.logTrace = function(message)
        ctld_groups.loggers.get(ctld.Id):trace(message)
    end    

    -- global configuration change
    ctld.cratesRequiredForFOB = 1

    --- replace the crate 3D model with an actual crate
    ctld.spawnableCratesModel_load = {
        ["category"] = "Cargos",
        ["shape_name"] = "bw_container_cargo",
        ["type"] = "container_cargo"
    }

    -- Simulated Sling load configuration
    ctld.minimumHoverHeight = 5.0 -- Lowest allowable height for crate hover
    ctld.maximumHoverHeight = 15.0 -- Highest allowable height for crate hover
    ctld.maxDistanceFromCrate = 8.0 -- Maximum distance from from crate for hover
    ctld.hoverTime = 10 -- Time to hold hover above a crate for loading in seconds

    -- ************** Maximum Units SETUP for UNITS ******************

    ctld.unitLoadLimits["UH-1H"] = 10
    ctld.unitLoadLimits["Mi-24P"] = 10
    ctld.unitLoadLimits["Mi-8MT"] = 20
    ctld.unitLoadLimits["UH-60L"] = 20
    ctld.unitLoadLimits["Yak-52"] = 1

    -- ************** Allowable actions for UNIT TYPES ******************

    ctld.unitActions["Yak-52"] = {crates=false, troops=true}
    ctld.unitActions["Mi-24P"] = {crates=true, troops=true}
    ctld.unitActions["Ka-50"] = {crates=true, troops=false}

    -- ************** INFANTRY GROUPS FOR PICKUP ******************

    table.insert(ctld.loadableGroups, {name = "2x - Standard Groups", inf = 12, mg = 4, at = 4 })
    table.insert(ctld.loadableGroups, {name = "3x - Mortar Squad", mortar = 18})
    
    ctld.autoInitializeAllHumanTransports = function()
        ctld_groups.loggers.get(ctld.Id):info("autoInitializeAllHumanTransports()")
        local TransportTypeNames = {"Mi-8MT", "UH-1H", "UH-60L", "Mi-24P", "Yak-52", "Ka-50", "SA342Mistral", "SA342L", "SA342M"}
        for name, unit in pairs(mist.DBs.humansByName) do
            ctld_groups.loggers.get(ctld.Id):trace(string.format("human player found name=%s, unitName=%s, groupName=%s", name, unit.unitName,unit.groupName))
            -- check if it's a transport helo
            for _, transportTypeName in pairs(TransportTypeNames) do
                if transportTypeName:lower() == unit.type:lower() then
                    table.insert(ctld.transportPilotNames, unit.unitName)
                    ctld_groups.loggers.get(ctld.Id):debug(string.format("Adding CTLD transport pilot %s of group %s", unit.unitName, unit.groupName))
                end
            end
        end
        ctld_groups.loggers.get(ctld.Id):trace("ctld.transportPilotNames=%s", ctld_groups.p(ctld.transportPilotNames))
    end

    ctld.autoInitializeAllLogistic = function()
        ctld_groups.loggers.get(ctld.Id):info("autoInitializeAllLogistic()")
        local CarrierTypeNames = {"Barracks 2", "Warehouse", "Garage small B", ".Command Center", ".Ammunition depot", "Hangar A", "Hangar B", "FARP CP Blindage", "FARP Fuel Depot", "FARP Ammo Dump Coating", "FARP Tent", "Invisible FARP", "SINGLE_HELIPAD", "FARP", "LHA_Tarawa", "Type_071", "Stennis", "VINSON", "Forrestal", "CVN_71", "CVN_72", "CVN_73", "CVN_75", "KUZNECOW", "CV_1143_5"}
        local ApcTypeNames = {"M 818", "AAV7", "M-113", "LAV-25", "M1126 Stryker ICV", "M-2 Bradley", "MCV-80", "M2A1_halftrack", "Marder", "TPZ", "Sd_Kfz_7", "Blitz_36-6700A", "Land_Rover_101_FC", "Land_Rover_109_S3", "Bedford_MWD", "Ural-375", "KrAZ6322", "KAMAZ Truck", "GAZ-66", "BTR-80", "BTR-82A", "BMP-1", "BMP-2", "BMP-3", "BMD-1", "BTR_D", "MTLB", "ZBD04A"}
        local units = mist.DBs.unitsByName -- local copy for faster execution
        for name, unit in pairs(units) do
            ctld_groups.loggers.get(ctld.Id):trace(string.format("name=%s, unit.type=%s", ctld_groups.p(name), ctld_groups.p(unit.type)))
            --ctld_groups.loggers.get(ctld.Id):trace(string.format("unit=%s", ctld_groups.p(unit)))
            --local unit = Unit.getByName(name)
            if unit then 
                for _, carrierTypeName in pairs(CarrierTypeNames) do
                    if carrierTypeName:lower() == unit.type:lower() then
                        table.insert(ctld.logisticUnits, unit.unitName)
                        ctld_groups.loggers.get(ctld.Id):debug(string.format("Adding CTLD logistic unit %s of group %s", unit.unitName, unit.groupName))
                    end
                end

                for _, apcTypeName in pairs(ApcTypeNames) do
                    if apcTypeName:lower() == unit.type:lower() then
                        table.insert(ctld.infantryUnits, unit.unitName)
                        ctld_groups.loggers.get(ctld.Id):debug(string.format("Adding CTLD infantry spawning unit %s of group %s", unit.unitName, unit.groupName))
                    end
                end
            end
        end
        ctld_groups.loggers.get(ctld.Id):trace("ctld.logisticUnits=%s", ctld_groups.p(ctld.logisticUnits))
        ctld_groups.loggers.get(ctld.Id):trace("ctld.infantryUnits=%s", ctld_groups.p(ctld.infantryUnits))
    end

    -- generate 20 pickup zone names in the form "pickzone #001"
    ctld_groups.loggers.get(ctld.Id):debug("generate 20 pickup zone names in the form 'CAPTURE-1'")
    ctld.pickupZones = {}
    table.insert(ctld.pickupZones, { "CAPTURE", "none", -1, "yes", 0 })
    for i = 1, 20 do
        table.insert(ctld.pickupZones, { string.format("CAPTURE-%d",i), "none", -1, "yes", 0 })
    end

    -- generate 20 logistic unit names in the form "logistic #001"
    ctld_groups.loggers.get(ctld.Id):debug("generate 20 logistic unit names in the form 'logistic #001'")
    ctld.logisticUnits = {}
    for i = 1, 20 do
        table.insert(ctld.logisticUnits, string.format("logistic #%03d",i))
    end
    
    -- Use only the automatic initialization
    ctld.transportPilotNames = {} 

    -- automatically add all the human-manned transport aircrafts to ctld.transportPilotNames
    ctld.autoInitializeAllHumanTransports()

    -- Use only the automatic initialization
    ctld.logisticUnits = {}

    -- automatically add all the carriers and FARPs to ctld.logisticUnits
    ctld.autoInitializeAllLogistic()

    ctld.initialize(true)

    ctld_groups.loggers.get(ctld.Id):info(string.format("Done setting up CTLD"))
end
