import configparser
from azurlane_calc.ship import MainShip, VangShip
from azurlane_calc.mob_exp import mob_vang_exp, mob_main_exp

config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def generate_mob(runsLeft):
    mobVang = mob_vang(runsLeft)
    mobMain = mob_main(runsLeft)

    return mobVang, mobMain

def mob_vang(runsLeft):
    mobVang = []
    for i in range (3):
        name = config.get("Mob Vanguard Ship "+str(i+1), "name")
        mvp = config.get("Mob Vanguard Ship "+str(i+1), "mvp")
        level = config.get("Mob Vanguard Ship "+str(i+1), "level")
        morale = config.get("Mob Vanguard Ship "+str(i+1), "hasMoraleBonus")
        expGained, estLevel = mob_vang_exp(runsLeft, level, i)
        if name != "none":
            mobVang.append(VangShip(name,level,mvp,morale,expGained,estLevel))
        else:
            break

    return mobVang

def mob_main(runsLeft):
    mobMain = []
    for i in range (3):
        name = config.get("Mob Main Ship "+str(i+1), "name")
        mvp = config.get("Mob Main Ship "+str(i+1), "mvp")
        level = config.get("Mob Main Ship "+str(i+1), "level")
        morale = config.get("Mob Main Ship "+str(i+1), "hasMoraleBonus")
        flagship = config.get("Mob Main Ship "+str(i+1), "flagship")
        expGained, estLevel = mob_main_exp(runsLeft, level, i, flagship)
        if name != "none":
            mobMain.append(MainShip(name,level,mvp,morale,flagship,expGained,estLevel))
        else:
            break

    return mobMain