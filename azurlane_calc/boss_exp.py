import configparser
from azurlane_calc.calc_level import calc_level

config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def boss_vang_exp(runsLeft, currentLevel, i):
    moraleBonus = config.get("Boss Vanguard Ship "+str(i+1), "hasMoraleBonus")
    mvp = config.get("Boss Vanguard Ship "+str(i+1), "mvp")
    exp = int(config.get("General", "baseEXP"))
    sRankNorm = config.get("General", "sRankNormal")
    expGained = exp

    if sRankNorm == "true":
        expGained *= 1.2
    if moraleBonus == "true":
        expGained *= 1.2
    if mvp == "true":
        expGained *= 2

    expGained = int(expGained)

    estLevel = calc_level(currentLevel, expGained)

    return expGained, estLevel

def boss_main_exp(runsLeft, currentLevel, i, flagship):
    moraleBonus = config.get("Boss Main Ship "+str(i+1), "hasMoraleBonus")
    mvp = config.get("Boss Main Ship "+str(i+1), "mvp")
    exp = int(config.get("General", "baseEXP"))
    sRankNorm = config.get("General", "sRankNormal")
    expGained = exp

    if sRankNorm == "true":
        expGained *= 1.2
    if moraleBonus == "true":
        expGained *= 1.2
    if flagship == "true":
        expGained *= 1.5
    if mvp == "true":
        expGained *= 2

    expGained = int(expGained)

    estLevel = calc_level(currentLevel, expGained)

    return expGained, estLevel