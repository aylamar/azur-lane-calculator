import configparser
from azurlane_calc.ship import MainShip, VangShip

config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def generate_boss():
    bossVang = boss_vang()
    bossMain = boss_main()
    return bossVang, bossMain

def boss_vang():
    bossVang = []
    for i in range (3):
        name = config.get("Boss Vanguard Ship "+str(i+1), "name")
        mvp = config.get("Boss Vanguard Ship "+str(i+1), "mvp")
        level = config.get("Boss Vanguard Ship "+str(i+1), "level")
        morale = config.get("Boss Vanguard Ship "+str(i+1), "hasMoraleBonus")
        if name != "none":
            bossVang.append(VangShip(name,mvp,level,morale))
        else:
            break

    return bossVang

def boss_main():
    bossMain = []
    for i in range (3):
        name = config.get("Boss Main Ship "+str(i+1), "name")
        mvp = config.get("Boss Main Ship "+str(i+1), "mvp")
        level = config.get("Boss Main Ship "+str(i+1), "level")
        morale = config.get("Boss Main Ship "+str(i+1), "hasMoraleBonus")
        flagship = config.get("Boss Main Ship "+str(i+1), "flagship")
        if name != "none":
            bossMain.append(MainShip(name,mvp,level,morale,flagship))
        else:
            break

    return bossMain