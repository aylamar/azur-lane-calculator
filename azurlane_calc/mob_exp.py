import configparser
from azurlane_calc.calc_level import calc_level

config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def mob_vang_exp(runsLeft, currentLevel, i):
    moraleBonus = config.get("Mob Vanguard Ship "+str(i+1), "hasMoraleBonus")
    mvp = config.get("Mob Vanguard Ship "+str(i+1), "mvp")
    useMobForBoss = config.get("Mob Fleet General", "useMobForBoss")
    exp = int(config.get("General", "baseEXP"))
    sRankNorm = config.get("General", "sRankNormal")
    battlesBeforeBoss = int(config.get("General", "battlesBeforeBoss"))
    expGained = exp

    if sRankNorm == "true":
        expGained *= 1.2
    if moraleBonus == "true":
        expGained *= 1.2
    if mvp == "true":
        expGained *= 2

    if useMobForBoss == "true":
        expGained = (battlesBeforeBoss + 1) * expGained
    else:
        expGained = battlesBeforeBoss * expGained
    expGained = int(expGained * runsLeft)
    estLevel = calc_level(currentLevel, expGained)

    return expGained, estLevel

def mob_main_exp(runsLeft, currentLevel, i, flagship):
    moraleBonus = config.get("Mob Main Ship "+str(i+1), "hasMoraleBonus")
    mvp = config.get("Mob Main Ship "+str(i+1), "mvp")
    useMobForBoss = config.get("Mob Fleet General", "useMobForBoss")
    exp = int(config.get("General", "baseEXP"))
    sRankNorm = config.get("General", "sRankNormal")
    battlesBeforeBoss = int(config.get("General", "battlesBeforeBoss"))
    expGained = exp

    if sRankNorm == "true":
        expGained *= 1.2
    if moraleBonus == "true":
        expGained *= 1.2
    if flagship == "true":
        expGained *= 1.5
    if mvp == "true":
        expGained *= 2

    if useMobForBoss == "true":
        expGained = (battlesBeforeBoss + 1) * expGained
    else:
        expGained = battlesBeforeBoss * expGained
    expGained = int(expGained * runsLeft)

    estLevel = calc_level(currentLevel, expGained)

    return expGained, estLevel