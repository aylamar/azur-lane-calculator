import configparser
from azurlane_calc.ship import MainShip, VangShip

config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def generate_mob():
    mobVang = mob_vang()
    mobMain = mob_main()

    return mobVang, mobMain

def mob_vang():
    mobVang = []
    for i in range (3):
        name = config.get("Mob Vanguard Ship "+str(i+1), "name")
        mvp = config.get("Mob Vanguard Ship "+str(i+1), "mvp")
        level = config.get("Mob Vanguard Ship "+str(i+1), "level")
        morale = config.get("Mob Vanguard Ship "+str(i+1), "hasMoraleBonus")
        if name != "none":
            mobVang.append(VangShip(name,mvp,level,morale))
        else:
            break

    return mobVang

def mob_main():
    mobMain = []
    for i in range (3):
        name = config.get("Mob Main Ship "+str(i+1), "name")
        mvp = config.get("Mob Main Ship "+str(i+1), "mvp")
        level = config.get("Mob Main Ship "+str(i+1), "level")
        morale = config.get("Mob Main Ship "+str(i+1), "hasMoraleBonus")
        flagship = config.get("Mob Main Ship "+str(i+1), "flagship")
        if name != "none":
            mobMain.append(MainShip(name,mvp,level,morale,flagship))
        else:
            break

    return mobMain