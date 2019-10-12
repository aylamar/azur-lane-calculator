import configparser
from azurlane_calc.ship import MainShip, VangShip
from azurlane_calc.boss_exp import boss_vang_exp, boss_main_exp

config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def generate_boss(runsLeft):
    bossVang = boss_vang(runsLeft)
    bossMain = boss_main(runsLeft)
    return bossVang, bossMain

def boss_vang(runsLeft):
    bossVang = []
    for i in range (3):
        name = config.get("Boss Vanguard Ship "+str(i+1), "name")
        mvp = config.get("Boss Vanguard Ship "+str(i+1), "mvp")
        level = config.get("Boss Vanguard Ship "+str(i+1), "level")
        morale = config.get("Boss Vanguard Ship "+str(i+1), "hasMoraleBonus")
        expGained, estLevel = boss_vang_exp(runsLeft, level, i)
        if name != "none":
            bossVang.append(VangShip(name,level,mvp,morale,expGained,estLevel))
        else:
            break

    return bossVang

def boss_main(runsLeft):
    bossMain = []
    for i in range (3):
        name = config.get("Boss Main Ship "+str(i+1), "name")
        mvp = config.get("Boss Main Ship "+str(i+1), "mvp")
        level = config.get("Boss Main Ship "+str(i+1), "level")
        morale = config.get("Boss Main Ship "+str(i+1), "hasMoraleBonus")
        flagship = config.get("Boss Main Ship "+str(i+1), "flagship")
        expGained, estLevel = boss_main_exp(runsLeft, level, i, flagship)
        if name != "none":
            bossMain.append(MainShip(name,level,mvp,morale,flagship,expGained,estLevel))
        else:
            break

    return bossMain