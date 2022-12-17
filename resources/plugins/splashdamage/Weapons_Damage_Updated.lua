
--assert(loadfile("C:\\Users\\spenc\\OneDrive\\Documents\\Eclipe_LDT\\dcs splash damage\\src\\mist.lua"))()
--[[
2 October 2020
FrozenDroid:
- Added error handling to all event handler and scheduled functions. Lua script errors can no longer bring the server down.
- Added some extra checks to which weapons to handle, make sure they actually have a warhead (how come S-8KOM's don't have a warhead field...?)

28 October 2020
FrozenDroid:
- Uncommented error logging, actually made it an error log which shows a message box on error.
- Fixed the too restrictive weapon filter (took out the HE warhead requirement)

21 December 2021
spencershepard (GRIMM):
 SPLASH DAMAGE 2.0:
 -Added blast wave effect to add timed and scaled secondary explosions on top of game objects
 -object geometry within blast wave changes damage intensity
 -damage boost for structures since they are hard to kill, even if very close to large explosions
 -increased some rocket values in explTable
 -missing weapons from explTable will display message to user and log to DCS.log so that we can add what's missing
 -damage model for ground units that will disable their weapons and ability to move with partial damage before they are killed
 -added options table to allow easy adjustments before release
 -general refactoring and restructure
--]]

----[[ ##### SCRIPT CONFIGURATION ##### ]]----

splash_damage_options = {
  ["static_damage_boost"] = 20, --apply extra damage to Unit.Category.STRUCTUREs with wave explosions
  ["oca_aircraft_damage_boost"] = 3000, --apply extra damage to parked Unit.Category.AIRPLANEs and Unit.Category.HELICOPTERs with wave explosions
  ["wave_explosions"] = true, --secondary explosions on top of game objects, radiating outward from the impact point and scaled based on size of object and distance from weapon impact point
  ["larger_explosions"] = true, --secondary explosions on top of weapon impact points, dictated by the values in the explTable
  ["damage_model"] = true, --allow blast wave to affect ground unit movement and weapons
  ["blast_search_radius"] = 200, --this is the max size of any blast wave radius, since we will only find objects within this zone
  ["cascade_damage_threshold"] = 0.1, --if the calculated blast damage doesn't exeed this value, there will be no secondary explosion damage on the unit.  If this value is too small, the appearance of explosions far outside of an expected radius looks incorrect.
  ["game_messages"] = true, --enable some messages on screen
  ["blast_stun"] = false, --not implemented
  ["unit_disabled_health"] = 30, --if health is below this value after our explosions, disable its movement
  ["unit_cant_fire_health"] = 50, --if health is below this value after our explosions, set ROE to HOLD to simulate damage weapon systems
  ["infantry_cant_fire_health"] = 90,  --if health is below this value after our explosions, set ROE to HOLD to simulate severe injury
  ["debug"] = false,  --enable debugging messages
  ["weapon_missing_message"] = true, --false disables messages alerting you to weapons missing from the explTable
}

local bdaMessagesEnable = 1
local clusterEffectsEnable = 1
local shipRadarDamageEnable = 1
refreshRate = 0.1
firebomb_splash_factor = 8
shell_max_flight_time = 20
cluster_max_flight_time = 20
cluster_munition_distribution_radius = 75
bda_message_time = 20

----[[ ##### End of SCRIPT CONFIGURATION ##### ]]----

explTable = {
  ["FAB_100"] = 45,
  ["FAB_250"] = 100,
  ["FAB_250M54TU"]= 100,
  ["FAB_500"] = 213,
  ["FAB_1500"]  = 675,
  ["BetAB_500"] = 98,
  ["BetAB_500ShP"]= 107,
  ["BKF_PTAB2_5KO"]= 10,
  ["BKF_AO2_5RT"]= 10,
  ["RBK_250_275_AO_1SCH"] = 100,
  ["RBK_250"] = 100,
  ["RBK_500AO"] = 200,
  ["RBK_500U"] = 200,
  ["RBK_500U_OAB_2_5RT"] = 200,
  ["KH-66_Grom"]  = 108,
  ["BDU_33"] = 201,                             -- BDU-33, smoke warhead (T-45, increased power for balance reasons)
  ["M_117"] = 201,
  ["Mk_81"] = 60,                               --
  ["Mk_82"] = 118,
  ["AN_M64"]  = 121,                            --
  ["Mk_83"] = 274,
  ["Mk_84"] = 582,                              --
  ["MK_82AIR"]  = 118,
  ["MK_82SNAKEYE"]= 118,                        --
  ["GBU_10"]  = 582,
  ["GBU_12"]  = 118,                            --
  ["GBU_16"]  = 274,
  ["KAB_1500Kr"]  = 675,                        --
  ["KAB_500Kr"] = 213,
  ["KAB_500"] = 213,                            --
  ["GBU_31"]  = 582,
  ["GBU_31_V_3B"] = 582,                        --
  ["GBU_31_V_2B"] = 582,
  ["GBU_31_V_4B"] = 582,                        --
  ["GBU_32_V_2B"] = 202,
  ["GBU_38"]  = 118,                            --
  ["AGM_62"]  = 400,
  ["GBU_24"]  = 582,                            --
  ["X_23"]  = 111,                              -- Kh-23 Grom anti-radar (AS-7 'Kerry')
  ["X_23L"] = 111,                              -- Kh-23L Grom laser (AS-7 'Kerry')
  ["X_28"]  = 160,                              -- Kh-28 anti-radar (AS-9 'Kyle')
  ["X_25ML"]  = 89,                             -- Kh-25ML laser (AS-10 'Karen')
  ["X_25MP"]  = 89,                             -- Kh-25MP anti-radar (AS-12 'Kegler')
  ["X_25MR"]  = 140,                            -- Kh-25MR TV (AS-12 'Kegler')
  ["X_58"]  = 140,                              -- Kh-58 anti-radar (AS-11 'Kilter')
  ["X_29L"] = 320,                              -- Kh-29L laser (AS-14 'Kedge')
  ["X_29T"] = 320,                              -- Kh-29T TV (AS-14 'Kedge')
  ["X_29TE"]  = 320,                            -- Kh_29TE export (AS-14 'Kedge')
  ["X_31P"]  = 87,                              -- Kh-31P (AS-17 Krypton)
  ["X_65"]  = 410,                              -- Kh-65 (AS-15B Kent)
  ["BK90_MJ1"] = 605,
  ["BK90_MJ2"] = 605,
  ["BK90_MJ1_MJ2"] = 605,
  ["Rb 04E"] = 300,
  ["Rb 15F"] = 200,
  ["Rb 15F (for A.I.)"] = 200,
  ["RB75"] = 57,
  ["RB75B"] = 57,
  ["RB75T"] = 136,
  ["AGM_45A"] = 68,
  ["AGM_65D"] = 57,
  ["AGM_65F"] = 136,
  ["AGM_65H"] = 57,
  ["AGM_65K"] = 136,
  ["AGM_84A"] = 221,
  ["AGM_84S"] = 221,
  ["AGM_84E"] = 221,
  ["AGM_88"] = 89,
  ["AGM_88C"] = 89,
  ["AGM_114K"] = 8,
  ["AGM_122"] = 15,
  ["AGM_123"] = 274,
  ["AGM_130"] = 582,
  ["AGM_119"] = 176,
  ["AGM_154A"]  = 10,                           -- AGM-154A - JSOW CEB (CBU-type) - 145 BLU-97/B Combined Effects Bomb (CEB) submunitions
  ["AGM_154C"]  = 305,                           -- AGM-154C - JSOW Unitary BROACH
  ["S-24A"] = 24,                                --
  ["S-24B"] = 123,                               --
  ["S-25OF"]  = 194,                             --
  ["S-25OFM"] = 150,                             --
  ["S-25O"] = 150,                               --
  ["S_25L"] = 190,                               --
  ["S-5M"]  = 5,                                 --
  ["C_5"]  = 5,                                  -- S-5
  ["C_8"]   = 8,                                 -- S-8
  ["C_8CM"] = 8,                                 -- S-8CM (с цветным дымом / with colored smoke )
  ["C_8OFP2"] = 8,                               -- S-8OFP2
  ["C_13"]  = 21,                                -- S-13
  ["C_24"]  = 123,                               -- S-24
  ["C_25"]  = 151,                               -- S-25
  ["HVAR"] = 13,
  ["Zuni_127"]  = 13,
  ["Zuni_127CM"]  = 13,
  ["ARAKM70BHE"]  = 14,
  ["BR_500"]  = 118,
  ["Rb 05A"]  = 217,
  ["HEBOMB"]  = 120,
  ["HEBOMBD"] = 120,
  ["MK-81SE"] = 60,
  ["HYDRA_70"] = 7,                              -- Hydra 70 2.75-inch/70mm rocket
  ["HYDRA_70_M151"] = 7,                         -- Hydra 70 2.75-inch/70mm rocket, M151 HEDP warhead
  ["HYDRA_70_M229"] = 7,                         -- Hydra 70 2.75-inch/70mm rocket, M229 HEDP warhead
  ["HYDRA_70_M274"] = 20,                        -- Hydra 70 2.75-inch/70mm rocket, M274 smoke warhead (T-45, increased power for balance reasons)
  ["HYDRA_70_M282"] = 7,                         -- Hydra 70 2.75-inch/70mm rocket, M282 MPP (penetrator) warhead
  ["HYDRA_70_MK5"] = 7,                          -- Hydra 70 2.75-inch/70mm rocket, Mk5 HEAT warhead
  ["FFAR Mk1 HE"] = 8,
  ["FFAR Mk5 HEAT"] = 8,
  ["SNEB68_EAP"] = 7,
  ["SNEB_TYPE253_H1"] = 7,
  ["SNEB_TYPE251_F1B"] = 7,
  ["MALUTKA"] = 4,                               -- AT-3 Sagger / 9M14 Malyutka
  ["KONKURS"] = 3,                               -- AT-5 Spandrel / 9M113 Konkurs
  ["AT_6"] = 6,                                  -- AT-6 Spiral / 9K114 Shturm
  ["Ataka_9M120"] = 8,                           -- AT-9 Spiral-2 / 9M120 Ataka
  ["Ataka_9M120F"] = 8 * firebomb_splash_factor, -- AT-9 Spiral-2 / 9M120F Ataka (thermobaric)
  ["P_9M117"] = 3,                               -- AT-10 Stabber / 9M117 Bastion
  ["SVIR"] = 5,                                  -- AT-11 Sniper / 9M119 Svir
  ["REFLEX"] = 5,                                -- AT-11 Sniper / 9M119M Refleks
  ["Vikhr_M"] = 12,                              -- AT-16 Scallion / 9K121 Vikhr
  ["HOT2"] = 15,
  ["HOT3"] = 15,
  ["TOW2"] = 15,
  ["TOW"] = 15,
  ["URAGAN_9M27F"] = 100,                        -- BM-27 Uragan / 9M27F (220mm HE)
  ["SMERCH_9M55F"] = 243,                        -- BM-30 Smerch / 9M55F (300mm HE)
  ["ALARM"] = 66,                                -- ALARM (Air-Launched Anti-Radiation Missile) - 146lbs (66kg) direct fragmentation with proximity/contact fuse
  ["Sea_Eagle"] = 230,
  ["YJ-83K"] = 165,                              -- Air-launched YJ-83 anti-ship missile
  ["250-3"] = 100,                               --("250 lb GP")
  ["British_GP_250LB_Bomb_Mk1"] = 100,           --("250 lb GP Mk.I")
  ["British_GP_250LB_Bomb_Mk4"] = 100,           --("250 lb GP Mk.IV")
  ["British_GP_250LB_Bomb_Mk5"] = 100,           --("250 lb GP Mk.V")
  ["British_GP_500LB_Bomb_Mk1"] = 213,           --("500 lb GP Mk.I")
  ["British_GP_500LB_Bomb_Mk4"] = 213,           --("500 lb GP Mk.IV")
  ["British_GP_500LB_Bomb_Mk4_Short"] = 213,     --("500 lb GP Short tail")
  ["British_GP_500LB_Bomb_Mk5"] = 213,           --("500 lb GP Mk.V")
  ["British_MC_250LB_Bomb_Mk1"] = 100,           --("250 lb MC Mk.I")
  ["British_MC_250LB_Bomb_Mk2"] = 100,           --("250 lb MC Mk.II")
  ["British_MC_500LB_Bomb_Mk1_Short"] = 213,     --("500 lb MC Short tail")
  ["British_MC_500LB_Bomb_Mk2"] = 213,           --("500 lb MC Mk.II")
  ["British_SAP_250LB_Bomb_Mk5"] = 100,          --("250 lb S.A.P.")
  ["British_SAP_500LB_Bomb_Mk5"] = 213,          --("500 lb S.A.P.")
  ["British_AP_25LBNo1_3INCHNo1"] = 4,           --("RP-3 25lb AP Mk.I")
  ["British_HE_60LBSAPNo2_3INCHNo1"] = 4,        --("RP-3 60lb SAP No2 Mk.I")
  ["British_HE_60LBFNo1_3INCHNo1"] = 4,          --("RP-3 60lb F No1 Mk.I")
  ["WGr21"] = 4,                                 --("Werfer-Granate 21 - 21 cm UnGd air-to-air rocket")
  ["3xM8_ROCKETS_IN_TUBES"] = 4,                 --("4.5 inch M8 UnGd Rocket")
  ["AN_M30A1"] = 45,                             --("AN-M30A1 - 100lb GP Bomb LD")
  ["AN-M57"] = 100,                              --("AN-M57 - 250lb GP Bomb LD")
  ["AN-M64"] = 213,                              --("AN-M64 - 500lb GP Bomb LD")
  ["AN-M65"] = 400,                              --("AN-M65 - 1000lb GP Bomb LD")
  ["AN-M66A2"] = 536,                            --("AN-M66A2 - 2000lb GP Bomb LD")
  ["AN_M57"] = 100,                              --("AN-M57 - 250lb GP Bomb LD")
  ["AN_M65"] = 400,                              --("AN-M65 - 1000lb GP Bomb LD")
  ["AN_M66"] = 536,                              --("AN-M66 - 2000lb GP Bomb LD")
  ["AN_M66A2"] = 536,                            --("AN-M66 - 2000lb GP Bomb LD")
  ["AN_M81"] = 110,                              --("AN-M81 - 260lb GP Bomb LD")
  ["AN_M88"] = 97,                               --("AN-M88 - 216lb GP Bomb LD")
  ["SC_50"] = 20,                                --("SC 50 - 50kg GP Bomb LD")
  ["ER_4_SC50"] = 20,                            --("4 x SC 50 - 50kg GP Bomb LD")
  ["SC_250_T1_L2"] = 100,                        --("SC 250 Type 1 L2 - 250kg GP Bomb LD")
  ["SC_501_SC250"] = 100,                        --("SC 250 Type 3 J - 250kg GP Bomb LD")
  ["Schloss500XIIC1_SC_250_T3_J"] = 100,         --("SC 250 Type 3 J - 250kg GP Bomb LD")
  ["SC_501_SC500"] = 213,                        --("SC 500 J - 500kg GP Bomb LD")
  ["SC_500_J"] = 213,                            --("SC 500 J - 500kg GP Bomb LD")
  ["SC_500_L2"] = 213,                           --("SC 500 L2 - 500kg GP Bomb LD")
  ["SD_250_Stg"] = 100,                          --("SD 250 Stg - 250kg GP Bomb LD")
  ["SD_500_A"] = 213,                            --("SD 500 A - 500kg GP Bomb LD")
--   ["AB_250_2_SD_2"] = 100,                       --("AB 250-2 - 144 x SD-2, 250kg CBU with HE submunitions")
--   ["AB_250_2_SD_10A"] = 100,                     --("AB 250-2 - 17 x SD-10A, 250kg CBU with 10kg Frag/HE submunitions")
--   ["AB_500_1_SD_10A"] = 213,                     --("AB 500-1 - 34 x SD-10A, 500kg CBU with 10kg Frag/HE submunitions")
--   ["CLUSTER_AB_250_2_SD_2"] = 100,               --("AB 250-2 - 144 x SD-2, 250kg CBU with HE submunitions")
--   ["CLUSTER_AB_250_2_SD_10A"] = 100,             --("AB 250-2 - 17 x SD-10A, 250kg CBU with 10kg Frag/HE submunitions")
--   ["CLUSTER_AB_500_1_SD_10A"] = 213,             --("AB 500-1 - 34 x SD-10A, 500kg CBU with 10kg Frag/HE submunitions")
  ["LTF_5B"] = 100,                              --("LTF 5b Aerial Torpedo")
  ["BL_755"] = 132,                              --("BL755 - 147 x parachute-retarded HEAT submunitions, 264kg")
  ["MK77mod0-WPN"] = 110 * firebomb_splash_factor, --("Mk 77 Mod 0 - 750 lb (340 kg) with 110 U.S. gallons (416 L; 92 imp gal) of petroleum oil.")
  ["MK77mod1-WPN"] = 75 * firebomb_splash_factor,  --("Mk 77 Mod 1 - 500 lb (230 kg) with 75 U.S. gallons (284 L; 62 imp gal) of petroleum oil.")
  ["BIN_200"] = 75 * firebomb_splash_factor,     --("BIN-200 - 200 kg Spanish liquid incendiary Napalm filled bomb.")
  --agm-65??
  ["BELOUGA"] = 10,                              -- BLG-66 Belouga AC - 305kg CBU, 151 x HEAT Bomblets
  ["BLG66_BELOUGA"] = 10,                        -- BLG-66 Belouga AC - 305kg CBU, 151 x HEAT Bomblets
  ["BAP_100"] = 100,
  ["ROCKEYE"] = 10,                             --("Mk-20 - 247 x Mk 118 Mod 1 bomblets, 222kg")
  ["CBU_87"] = 10,                               --CBU-87 - 202 x CEM Cluster Bomb
  ["CBU_103"] = 10,                              --CBU-103 - 202 x CEM, CBU with WCMD
  ["M_230_new"] = 30,                            --30mm M230 autocannon (AH-64)
  ["2A42"] = 30,                                 --30mm Shipunov 2A42 autocannon (Ka-50)
  ["GSh_23_UPK"] = 23,                           --23mm GSh-23 autocannon (Ka-50)
  ["GSh_30_2K"] = 30,                            --30mm GSh-30 autocannon (Mi-24P)
}

clusterWeaps = {
  ["BK90_MJ1"] = 72,                             -- BK-90 MJ1 (72 x MJ1 HE-FRAG Bomblets)
  ["BK90_MJ2"] = 24,                             -- BK-90 MJ2 (24 x MJ2 HEAT Bomblets)
  ["BK90_MJ1_MJ2"] = 48,                         -- BK-90 MJ1+2 (12x MJ2 HEAT / 36x MJ1 HE-FRAG Bomblets)
  ["BELOUGA"] = 151,                             -- BLG-66 Belouga AC - 305kg CBU, 151 x HEAT Bomblets
  ["BLG66_BELOUGA"] = 151,                       -- BLG-66 Belouga AC - 305kg CBU, 151 x HEAT Bomblets
  ["ROCKEYE"] = 247,                             -- ("Mk-20 - 247 x Mk 118 Mod 1 bomblets, 222kg")
  ["CBU_87"] = 202,                              -- CBU-87 - 202 x CEM Cluster Bomb
  ["CBU_103"] = 202,                             -- CBU-103 - 202 x CEM, CBU with WCMD
  ["AGM_154A"]  = 145,                           -- AGM-154A - JSOW CEB (CBU-type) - 145 BLU-97/B Combined Effects Bomb (CEB) submunitions
  ["BKF_PTAB2_5KO"]= 12,                         -- BKF - 12 x PTAB-2.5KO
  ["BKF_AO2_5RT"]= 12,                           -- BKF - 12 x AO-2.5RT
  ["RBK_250_275_AO_1SCH"] = 25,                  -- RBK-250-275 - 150 x AO-1SCh, 250kg CBU HE/Frag
  ["RBK_250"] = 25,                              -- RBK-250 - 42 x PTAB-2.5M, 250kg CBU Medium HEAT/AP
  ["RBK_500AO"] = 25,
  ["RBK_500U"] = 25,                             -- RBK-500U - 126 x OAB-2.5RT, 500kg CBU HE/Frag
  ["RBK_500U_OAB_2_5RT"] = 25,
}

antiRadiationMissile = {
  ["AGM_45A"] = 1,
  ["AGM_88"] = 1,
  ["AGM_88C"] = 1,
  ["AGM_122"] = 1,
  ["ALARM"] = 1,
  ["X_25MP"]  = 1,
  ["X_28"]  = 1,
  ["X_58"]  = 1,
}

ignoredWeaps = {
  ["AK_74"] = 1,                                  --5.45mm
  ["M4"] = 1,                                     --5.56mm
  ["7_62_MG"] = 1,                                --7.62mm
  ["7_62_PKT"] = 1,                               --7.62mm
  ["7_62_L94A1"] = 1,                             --7.62mm
  ["M_134"] = 1,                                  --7.62mm
  ["M240"] = 1,                                   --7.62mm
  ["PK-3"] = 1,                                   --PK-3 - 7.62mm GPMG
  ["MG34"] = 1,                                   --7.92mm
  ["Besa"] = 1,                                   --7.92mm
  ["Lee-Enfield SMLE No.4 Mk.1"] = 1,
  ["M1 Garand .30 cal"] = 1,
  ["Browning .30 cal"] = 1,
  ["12_7_MG"] = 1,                                --12.7mm
  ["M2_Browning"] = 1,                            --12.7mm
  ["BrowningM2"] = 1,                             --12.7mm
  ["KORD_12_7"] = 1,                             --12.7mm
  ["KPVT"] = 1,                                   --14.5mm
  ["coltMK12"] = 1,                               --20mm
  ["2A14_2"] = 1,                                 --23mm, ZU-23
  ["2A14_4"] = 1,                                 --23mm, ZSU-23
  ["NR-23"] = 1,                                  --23mm, NR-23
  ["GSH_23"] = 1,                                 --23mm
  ["M242_Bushmaster"] = 1,                        --25mm
  ["2A38"] = 1,                                   --30mm, 2S6 Tunguska
  ["2A72"] = 1,                                   --30mm, BMP-2
  ["DEFA 554"] = 1,                               --30mm
  ["NR-30"] = 1,                                  --30mm
  ["GSh_30_2"] = 1,                               --30mm
  ["GSh_30_6"] = 1,                               --30mm
  ["GSh-6-30K"] = 1,                              --30mm
  ["GAU_8"] = 1,                                  --30mm
  ["N-37"] = 1,                                   --37mm
  ["Flak M1 37mm"] = 1,                           --37mm
  ["Bofors 40mm gun"] = 1,                        --40mm
  ["S_68"] = 1,                                   --57mm
  ["AAA 01"] = 1,
--   weapons.shells.M1_37mm_HE-T
--   weapons.shells.M1_37mm_37AP-T
--   weapons.shells.M2_12_7_T
--   weapons.shells.KPVT_14_5_T
--   weapons.shells.OF_350
--   weapons.shells.Bofors_40mm_HE
--   weapons.shells.QF94_AA_HE
}

----[[ ##### HELPER/UTILITY FUNCTIONS ##### ]]----

local function tableHasKey(table,key)
    return table[key] ~= nil
end

local function debugMsg(str)
  if splash_damage_options.debug == true then
    trigger.action.outText(str , 5)
  end
end

local function gameMsg(str)
  if splash_damage_options.game_messages == true then
    trigger.action.outText(str , 5)
  end
end

local function getDistance(point1, point2)
  local x1 = point1.x
  local y1 = point1.y
  local z1 = point1.z
  local x2 = point2.x
  local y2 = point2.y
  local z2 = point2.z
  local dX = math.abs(x1-x2)
  local dZ = math.abs(z1-z2)
  local distance = math.sqrt(dX*dX + dZ*dZ)
  return distance
end

local function getDistance3D(point1, point2)
  local x1 = point1.x
  local y1 = point1.y
  local z1 = point1.z
  local x2 = point2.x
  local y2 = point2.y
  local z2 = point2.z
  local dX = math.abs(x1-x2)
  local dY = math.abs(y1-y2)
  local dZ = math.abs(z1-z2)
  local distance = math.sqrt(dX*dX + dZ*dZ + dY*dY)
  return distance
end

local function vec3Mag(speedVec)
  local mag = speedVec.x*speedVec.x + speedVec.y*speedVec.y+speedVec.z*speedVec.z
  mag = math.sqrt(mag)
  --trigger.action.outText("X = " .. speedVec.x ..", y = " .. speedVec.y .. ", z = "..speedVec.z, 10)
  --trigger.action.outText("Speed = " .. mag, 1)
  return mag
end

local function lookahead(speedVec)
  local speed = vec3Mag(speedVec)
  local dist = speed * refreshRate * 1.5
  return dist
end

----[[ ##### End of HELPER/UTILITY FUNCTIONS ##### ]]----


WpnHandler = {}
tracked_weapons = {}
tracked_shooters = {}
bda_damage = {}
bda_destroyed = {}
bda_wpn_disable = {}
bda_disable = {}

function track_wpns()
--  env.info("Weapon Track Start")
  for wpn_id_, wpnData in pairs(tracked_weapons) do
    if wpnData.wpn:isExist() then  -- just update speed, position and direction.
      wpnData.pos = wpnData.wpn:getPosition().p
      wpnData.dir = wpnData.wpn:getPosition().x
      wpnData.speed = wpnData.wpn:getVelocity()
      --wpnData.lastIP = land.getIP(wpnData.pos, wpnData.dir, 50)
    else -- wpn no longer exists, must be dead.
      if clusterWeaps[wpnData.name] then
        if wpnData.init then
          if explTable[wpnData.name] then
            env.info(wpnData.init.." opened a cluster "..wpnData.name.." at "..timer.getTime())
            tracked_shooters[wpnData.init] = { wpn = wpnData.name, init = wpnData.init, time = timer.getTime() }
          end
        end
      else
  --      trigger.action.outText("Weapon impacted, mass of weapon warhead is " .. wpnData.exMass, 2)
        local ip = land.getIP(wpnData.pos, wpnData.dir, lookahead(wpnData.speed))  -- terrain intersection point with weapon's nose.  Only search out 20 meters though.
        local impactPoint
        if not ip then -- use last calculated IP
          impactPoint = wpnData.pos
    --        trigger.action.outText("Impact Point:\nPos X: " .. impactPoint.x .. "\nPos Z: " .. impactPoint.z, 2)
        else -- use intersection point
          impactPoint = ip
    --        trigger.action.outText("Impact Point:\nPos X: " .. impactPoint.x .. "\nPos Z: " .. impactPoint.z, 2)
        end
        --env.info("Weapon is gone") -- Got to here --
        --trigger.action.outText("Weapon Type was: ".. wpnData.name, 20)

        --if wpnData.cat == Weapon.Category.ROCKET then
          blastWave(impactPoint, splash_damage_options.blast_search_radius, wpnData.ordnance, getWeaponExplosive(wpnData.name), wpnData.player)
          if splash_damage_options.larger_explosions == true then
            --env.info("triggered explosion size: "..getWeaponExplosive(wpnData.name))
            trigger.action.explosion(impactPoint, getWeaponExplosive(wpnData.name))
            --trigger.action.smoke(impactPoint, 0)
          end
          if wpnData.name == "MK77mod1-WPN" or wpnData.name == "BIN_200" then
              trigger.action.effectSmokeBig(impactPoint, 2, 0.5, wpnData.name)
          elseif wpnData.name == "MK77mod0-WPN" then
              trigger.action.effectSmokeBig(impactPoint, 3, 0.5, wpnData.name)
          end
        --end
      end
      tracked_weapons[wpn_id_] = nil -- remove from tracked weapons first.
    end
  end
--  env.info("Weapon Track End")
end

function onWpnEvent(event)
  if event.id == world.event.S_EVENT_SHOT then
    if event.weapon and string.find(event.weapon:getTypeName(), "weapons.shells.") == nil then
      local ordnance = event.weapon
      local weapon_desc = ordnance:getDesc()
      if explTable[ordnance:getTypeName()] then
        --trigger.action.outText(ordnance:getTypeName().." found.", 10)

        if (weapon_desc.category ~= 0) and event.initiator then
          if (weapon_desc.category == 1) then
            if (weapon_desc.MissileCategory ~= 1 and weapon_desc.MissileCategory ~= 2) then
              tracked_weapons[event.weapon.id_] = { wpn = ordnance, init = event.initiator:getName(), pos = ordnance:getPoint(), dir = ordnance:getPosition().x, name = ordnance:getTypeName(), speed = ordnance:getVelocity(), cat = ordnance:getCategory(), player=event.initiator:getPlayerName() }
            end
          else
            tracked_weapons[event.weapon.id_] = { wpn = ordnance, init = event.initiator:getName(), pos = ordnance:getPoint(), dir = ordnance:getPosition().x, name = ordnance:getTypeName(), speed = ordnance:getVelocity(), cat = ordnance:getCategory(), player=event.initiator:getPlayerName() }
          end
        end
      else
        env.info(ordnance:getTypeName().." missing from Splash Damage script")
        if splash_damage_options.weapon_missing_message == false then
          trigger.action.outText(ordnance:getTypeName().." missing from Splash Damage script", 10)
        end
      end
    end
  elseif event.id == world.event.S_EVENT_SHOOTING_START then
    -- An object has started shooting, evaluate the weapon and possibly store the shooter in array
    if event.weapon_name and ignoredWeaps[event.weapon_name] then
      -- Do nothing
    elseif event.weapon_name and event.initiator then
      local weapon = event.weapon_name
      if explTable[weapon] then
        env.info(event.initiator:getName().." started shooting with "..weapon)
        tracked_shooters[event.initiator:getName()] = { wpn = event.weapon_name, init = event.initiator:getName(), time = event.time, player=event.initiator:getPlayerName() }
      else
        env.info(weapon.." missing from Splash Damage script")
      end
    end
  elseif event.id == world.event.S_EVENT_SHOOTING_END then
    -- An object has stopped shooting, evaluate the weapon and possibly store the shooter in array
    if event.weapon_name and ignoredWeaps[event.weapon_name] then
      -- Do nothing
    elseif event.weapon_name and event.initiator then
      local weapon = event.weapon_name
      if explTable[weapon] then
        env.info(event.initiator:getName().." stopped shooting with "..weapon)
        tracked_shooters[event.initiator:getName()] = { wpn = event.weapon_name, init = event.initiator:getName(), time = event.time, player=event.initiator:getPlayerName() }
      else
        env.info(weapon.." missing from Splash Damage script")
      end
    end
  elseif event.id == world.event.S_EVENT_HIT then
    if event.weapon and event.target then
          local weapon = event.weapon:getTypeName()
          if shipRadarDamageEnable and event.target:getDesc().category == Unit.Category.SHIP and antiRadiationMissile[weapon] ~= nil then
            event.target:enableEmission(false)
            env.info("BDA: "..event.target:getTypeName().." radar destroyed")
            if event.initiator then
              if event.initiator:getPlayerName() ~= nil and bdaMessagesEnable then
                gameMsg("BDA: "..event.target:getTypeName().." radar destroyed")
              end
            end
          end
    end
    if event.weapon and ignoredWeaps[event.weapon] then
      -- Do nothing
    elseif event.target and event.initiator and tracked_shooters[event.initiator:getName()] ~= nil then
      local player = tracked_shooters[event.initiator:getName()].player
      local weapon = tracked_shooters[event.initiator:getName()].wpn
      local shoot_time = tracked_shooters[event.initiator:getName()].time
      local flight_time = shell_max_flight_time
      if clusterWeaps[weapon] then
        flight_time = cluster_max_flight_time
      end
      env.info("Hit with weapon "..weapon.." by "..event.initiator:getName().." at "..event.time.." shoot_time: "..shoot_time.." flight_time: "..flight_time)
      if event.time > (shoot_time + flight_time) then
        -- Max shell flight time exceeded, remove from shooter array if exists
        env.info("Removing "..event.initiator:getName().." from tracked shooters")
        tracked_shooters[event.initiator:getName()] = nil -- remove from tracked weapons
      else
        env.info(weapon.." hit a target")
        if event.target then
          local impactPoint = event.target:getPosition().p
          if explTable[weapon] then
            env.info(weapon.." hit "..event.target:getTypeName())
            --env.info('Impact point was at: X: ' .. impactPoint.x .. ' Y: ' .. impactPoint.y .. ' Z: ' .. impactPoint.z)
            if clusterEffectsEnable and clusterWeaps[weapon] then
              for i=1,clusterWeaps[weapon]
              do
                cluster_radius = math.random(0,cluster_munition_distribution_radius)
                cluster_angle = 2 * math.pi * (math.random())
                blastPoint = {
                  x = impactPoint.x + cluster_radius * math.cos(cluster_angle),
                  y = impactPoint.y,
                  z = impactPoint.z + cluster_radius * math.sin(cluster_angle)
                }
                --env.info('Generating cluster bomb explosion at: X: ' .. blastPoint.x .. ' Y: ' .. blastPoint.y .. ' Z: ' .. blastPoint.z)
                blastWave(blastPoint, splash_damage_options.blast_search_radius, weapon, getWeaponExplosive(weapon), player)
              end
            else
              blastWave(impactPoint, splash_damage_options.blast_search_radius, weapon, getWeaponExplosive(weapon), player)
            end
          end
        else
          env.info(weapon.." missing from Splash Damage script")
        end
      end
    end
  end
end

local function protectedCall(...)
  local status, retval = pcall(...)
  if not status then
    env.warning("Splash damage script error... gracefully caught! " .. retval, true)
  end
end


function WpnHandler:onEvent(event)
  protectedCall(onWpnEvent, event)
end



function explodeObject(table)
  local point = table[1]
  local distance = table[2]
  local power = table[3]
  trigger.action.explosion(point, power)
end

function getWeaponExplosive(name)
  if explTable[name] then
    return explTable[name]
  else
    return 0
  end
end


function modelUnitDamage(table)
  local units = table[1]
  local player = table[2]
  --debugMsg("units table: "..mist.utils.tableShow(units))
  for i, unit in ipairs(units)
  do
    --debugMsg("unit table: "..mist.utils.tableShow(unit))
    if unit:isExist() then  --if units are not already dead
      local health = (unit:getLife() / unit:getDesc().life) * 100

      if bda_damage[unit:getName()] ~= nil then
        local bda_time = bda_damage[unit:getName()].time
        local delay_time = bda_message_time
          if timer.getTime() > (bda_time + delay_time) then
            -- Message delay exceeded, remove from bda array if exists
            bda_damage[unit:getName()] = nil -- remove from bda array
        end
      end
      if bdaMessagesEnable and player ~= nil and bda_damage[unit:getName()] == nil and health < 100 then
        bda_damage[unit:getName()] = { unit = unit:getName(), time = timer.getTime() }
        gameMsg("BDA: "..unit:getTypeName().." damaged: "..100-health.."%")
      end

      --debugMsg(unit:getTypeName().." health %"..health)
      if unit:hasAttribute("Infantry") == true and health > 0 then  --if infantry
        if health <= splash_damage_options.infantry_cant_fire_health then
          ---disable unit's ability to fire---
          unit:getController():setOption(AI.Option.Ground.id.ROE , AI.Option.Ground.val.ROE.WEAPON_HOLD)
        end
      end
      if unit:getDesc().category == Unit.Category.GROUND_UNIT == true and unit:hasAttribute("Infantry") == false and health > 0 then  --if ground unit but not infantry
        if health <= splash_damage_options.unit_cant_fire_health then
          ---disable unit's ability to fire---
          unit:getController():setOption(AI.Option.Ground.id.ROE , AI.Option.Ground.val.ROE.WEAPON_HOLD)
          if bda_wpn_disable[unit:getName()] ~= nil then
            local bda_time = bda_wpn_disable[unit:getName()].time
            local delay_time = bda_message_time
            if timer.getTime() > (bda_time + delay_time) then
              -- Message delay exceeded, remove from bda array if exists
              bda_wpn_disable[unit:getName()] = nil -- remove from bda array
            end
          end
          if bdaMessagesEnable and player ~= nil and bda_wpn_disable[unit:getName()] == nil then
            bda_wpn_disable[unit:getName()] = { unit = unit:getName(), time = timer.getTime() }
            gameMsg("Critical hit: "..unit:getTypeName().." weapons disabled")
          end
        end
        if health <= splash_damage_options.unit_disabled_health and health > 0 then
          ---disable unit's ability to move---
          unit:getController():setTask({id = 'Hold', params = { }} )
          unit:getController():setOnOff(false)

          if bda_disable[unit:getName()] ~= nil then
            local bda_time = bda_disable[unit:getName()].time
            local delay_time = bda_message_time
            if timer.getTime() > (bda_time + delay_time) then
              -- Message delay exceeded, remove from bda array if exists
              bda_disable[unit:getName()] = nil -- remove from bda array
            end
          end
          if bdaMessagesEnable and player ~= nil and bda_disable[unit:getName()] == nil then
            bda_disable[unit:getName()] = { unit = unit:getName(), time = timer.getTime() }
            gameMsg("Critical hit: "..unit:getTypeName().." disabled")
          end

        end
      end

    else
      if unit:getName() ~= nil then
        if bda_destroyed[unit:getName()] ~= nil then
          local bda_time = bda_destroyed[unit:getName()].time
          local delay_time = bda_message_time
          if timer.getTime() > (bda_time + delay_time) then
            -- Message delay exceeded, remove from bda array if exists
            bda_destroyed[unit:getName()] = nil -- remove from bda array
          end
        end
        if bdaMessagesEnable and player ~= nil and bda_destroyed[unit:getName()] == nil then
          bda_destroyed[unit:getName()] = { unit = unit:getName(), time = timer.getTime() }
          gameMsg("BDA: "..unit:getTypeName().." critically damaged")
        end
      else
        if bdaMessagesEnable and player ~= nil then
          gameMsg("BDA: target destroyed")
        end
      end
      --debugMsg("unit no longer exists")
    end
  end
end


function blastWave(_point, _radius, weapon, power, player)
  local foundUnits = {}
  local volS = {
   id = world.VolumeType.SPHERE,
   params = {
     point = _point,
     radius = _radius
   }
  }

  local ifFound = function(foundObject, val)
    if foundObject:getDesc().category == Unit.Category.GROUND_UNIT and foundObject:getCategory() == Object.Category.UNIT then
      foundUnits[#foundUnits + 1] = foundObject
    end
    if foundObject:getDesc().category == Unit.Category.GROUND_UNIT then --if ground unit
      if splash_damage_options.blast_stun == true then
        --suppressUnit(foundObject, 2, weapon)
      end
    end
    if splash_damage_options.wave_explosions == true then
      local obj = foundObject
      local obj_location = obj:getPoint()
      local distance = getDistance(_point, obj_location)
      local timing = distance/500
      local scaled_power_factor = 0
      local intensity = 0
      local surface_area_default = 20
      local damage_for_surface = 0
      if obj:isExist() then

        if tableHasKey(obj:getDesc(), "box") then
          local length = (obj:getDesc().box.max.x + math.abs(obj:getDesc().box.min.x))
          local height = (obj:getDesc().box.max.y + math.abs(obj:getDesc().box.min.y))
          local depth = (obj:getDesc().box.max.z + math.abs(obj:getDesc().box.min.z))
          local _length = length
          local _depth = depth
          if depth > length then
            _length = depth
            _depth = length
          end
          local surface_distance = distance - _depth/2
          scaled_power_factor = 0.040 * power + 1 --this could be reduced into the calc on the next line
          intensity = (power * scaled_power_factor) / (4 * 3.14 * surface_distance * surface_distance )
          local surface_area = _length * height --Ideally we should roughly calculate the surface area facing the blast point, but we'll just find the largest side of the object for now
          damage_for_surface = intensity * surface_area
          env.info(weapon.." "..obj:getTypeName().." sa:"..surface_area.." distance:"..surface_distance.." dfs:"..damage_for_surface)
        else --debugMsg(obj:getTypeName().." object does not have box property")
          scaled_power_factor = 0.040 * power + 1 --this could be reduced into the calc on the next line
          intensity = (power * scaled_power_factor) / (4 * 3.14 * distance * distance )
          damage_for_surface = intensity * surface_area_default
          env.info(weapon.." "..obj:getTypeName().." distance:"..distance.." dfs:"..damage_for_surface)
        end

        --debugMsg(obj:getTypeName().." sa:"..surface_area.." distance:"..surface_distance.." dfs:"..damage_for_surface)
        if damage_for_surface > splash_damage_options.cascade_damage_threshold then
          local explosion_size = damage_for_surface
          if obj:getDesc().category == Unit.Category.STRUCTURE then
            explosion_size = intensity * splash_damage_options.static_damage_boost --apply an extra damage boost for static objects. should we factor in surface_area?
            --debugMsg("static obj :"..obj:getTypeName())
          end
          if (obj:getDesc().category == Unit.Category.AIRPLANE or obj:getDesc().category == Unit.Category.HELICOPTER) and obj:inAir() == false then
            explosion_size = intensity * splash_damage_options.oca_aircraft_damage_boost --apply an extra damage boost for aircraft to increase kill probability on OCA/Aircraft missions.
            --debugMsg("static obj :"..obj:getTypeName())
          end
          -- According to toutenglisse on DCS World forums (2022-06-11), ships do not have sensors attributes and therefore obj:hasSensors(Unit.SensorType.RADAR) cannot be used
          -- "I don't know why, but no Ship in DCS has ["sensors"] in its attributes (while obviously they have and can use them in game...). No way to use Ship with getDetectedTargets function (except for visual detection)."
          if shipRadarDamageEnable and obj:getDesc().category == Unit.Category.SHIP and antiRadiationMissile[weapon] ~= nil then
            obj:enableEmission(false)
            env.info("BDA: "..event.target:getTypeName().." radar destroyed")
            if player ~= nil and bdaMessagesEnable then
              gameMsg("BDA: "..obj:getTypeName().." radar destroyed")
            end
          end

          if explosion_size > power then explosion_size = power end --secondary explosions should not be larger than the explosion that created it
          local id = timer.scheduleFunction(explodeObject, {obj_location, distance, explosion_size}, timer.getTime() + timing)  --create the explosion on the object location

          if bda_damage[obj:getName()] ~= nil then
            local bda_time = bda_damage[obj:getName()].time
            local delay_time = bda_message_time
            if timer.getTime() > (bda_time + delay_time) then
                -- Message delay exceeded, remove from bda array if exists
                bda_damage[obj:getName()] = nil -- remove from bda array
            end
          end
          if bda_damage[obj:getName()] == nil then
            bda_damage[obj:getName()] = { unit = obj:getName(), time = timer.getTime() }
            if player ~= nil and bdaMessagesEnable then
              gameMsg("BDA: "..obj:getTypeName().." damaged: "..damage_for_surface)
            end
          end
        end
      end
    end
    return true
  end

  world.searchObjects(Object.Category.UNIT, volS, ifFound)
  world.searchObjects(Object.Category.STATIC, volS, ifFound)
  world.searchObjects(Object.Category.SCENERY, volS, ifFound)
  world.searchObjects(Object.Category.CARGO, volS, ifFound)
  --world.searchObjects(Object.Category.BASE, volS, ifFound)

  if splash_damage_options.damage_model == true then
    local id = timer.scheduleFunction(modelUnitDamage, {foundUnits, player}, timer.getTime() + 1.5) --allow some time for the game to adjust health levels before running our function
  end
end



function weaponDamage(bdaMessages, clusterEffects, shipRadarDamage)
  env.info(string.format("Weapons Damage Mod running. BDA messages enabled: %s, Cluster munition damage updates enabled: %s, Ship radar damage enabled: %s",tostring(bdaMessages),tostring(clusterEffects),tostring(shipRadarDamage)))
  bdaMessagesEnable = bdaMessages
  clusterEffectsEnable = clusterEffects
  shipRadarDamageEnable = shipRadarDamage

  timer.scheduleFunction(function()
      protectedCall(track_wpns)
      return timer.getTime() + refreshRate
    end,
    {},
    timer.getTime() + refreshRate
  )
  world.addEventHandler(WpnHandler)
end
