local Cfg = {
--#################################################################################################
--
--  LuaLoader
--
--  Load LUA files dynamically.
--
--  Usage: (check drive:/folder)
--      MISSION EDITOR -> TRIGGERS -> MISSION START -> DO SCRIPT ->
--          assert(loadfile('C:/Folder/stne.LuaLoader.lua'))()
--
--#################################################################################################
--##  CONFIGURATION START  ##  DO NOT EDIT ABOVE THIS LINE  #######################################
--#################################################################################################
    Folder = 'C:/Folder',                       -- Folder
    Scripts = {                                 -- Lua scripts, check proper loading order
        'File1.lua',
        'File2.lua',
        'File3.lua',
    },
--#################################################################################################
--##  CONFIGURATION END  ##  DO NOT EDIT BELOW THIS LINE  #########################################
--#################################################################################################
}

-- File
local LuaFile = 'stne.LuaLoader.lua'
local Version = '210421'
local FileVer = LuaFile..'/'..Version
env.info('FILE: '..FileVer..' START')

-- Override configuration
if STNE_Config_LuaLoader then
    for key, value in pairs(STNE_Config_LuaLoader) do
        Cfg[key] = value
    end
end

-- Read config table
local Folder = Cfg.Folder
local Scripts = Cfg.Scripts

-- Check sanitizeModules
local Commands = 'Modules enabled in MissionScripting.lua:'
if os or io or lfs then
    if os then
        Commands = Commands .. ' OS'
    end
    if io then
        Commands = Commands .. ' IO'
    end
    if lfs then
        Commands = Commands .. ' LFS'
    end
else
    Commands = Commands .. ' none'
end
trigger.action.outText(Commands, 30)

-- Load lua scripts
trigger.action.outText('Load LUA files:', 30)
for i = 1, #Scripts, 1 do
    local LUA_File = loadfile(Folder .. '/' .. Scripts[i])
    if LUA_File then
        assert(LUA_File)()
        trigger.action.outText('-  ' .. i .. '/' .. #Scripts ..  '  GO  ' .. Scripts[i], 30)
    else
        trigger.action.outText('-  ' .. i .. '/' .. #Scripts ..  '  ERROR  ' .. Scripts[i], 30)
    end
end

-- EOF
env.info('FILE: '..FileVer..' END')