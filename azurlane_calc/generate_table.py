import configparser
from prettytable import PrettyTable

# Read config file
config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

useMobForBoss = config.get("Mob Fleet General", "useMobForBoss")

def generate_mob_table(mobVang, mobMain):
    table = PrettyTable()
    table.field_names = ["Ship Name", "EXP Gained", "Current Level", "Est Level"]
    vangEXP = 0
    mainEXP = 0
    for i in range (len(mobVang)):
        table.add_row([mobVang[i].name, mobVang[i].expGained, mobVang[i].level, mobVang[i].estLevel])
        vangEXP += int(mobVang[i].expGained)

    for i in range (len(mobMain)):
        table.add_row([mobMain[i].name, mobMain[i].expGained, mobMain[i].level, mobMain[i].estLevel])
        mainEXP += mobMain[i].expGained
    
    print()
    print("Here is what your mob fleet will gain:")
    print(table)
    print("Your vanguard will gain a total of", vangEXP, "EXP.")
    print("Your main fleet will gain a total of", mainEXP, "EXP.")

def generate_boss_table(bossVang, bossMain):
    if useMobForBoss == "true":
        pass
    else:
        vangEXP = 0
        mainEXP = 0
        
        table = PrettyTable()
        table.field_names = ["Ship Name", "EXP Gained", "Current Level", "Est Level"]
        for i in range (len(bossVang)):
            table.add_row([bossVang[i].name, bossVang[i].expGained, bossVang[i].level, bossVang[i].estLevel])
            vangEXP += bossVang[i].expGained
        for i in range (len(bossMain)):
            table.add_row([bossMain[i].name, bossMain[i].expGained, bossMain[i].level, bossMain[i].estLevel])
            mainEXP += bossMain[i].expGained
        
        print()
        print("Here is what your mob fleet will gain:")
        print(table)
        print("Your vanguard will gain a total of", vangEXP, "EXP.")
        print("Your main fleet will gain a total of", mainEXP, "EXP.")

    input("Press Enter to exit the program..")
    exit()