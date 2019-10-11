import configparser
    
# Read config file & define values
config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def calc_mob_exp(runs_left):

    #Define variables from config file
    mob_fleet_for_boss = config.get('Mob_Fleet', 'use_mob_fleet_for_boss')
    battle_count = int(config.get('Mob_Fleet', 'battle_count'))
    base_exp = int(config.get('Mob_Fleet', 'base_exp'))
    boss_exp = int(config.get('Mob_Fleet', 'boss_exp'))

    total_exp = 0

    if mob_fleet_for_boss == 'true':
        total_exp = runs_left * ((base_exp * battle_count) + boss_exp)
        return total_exp
    else:
        total_exp = runs_left * base_exp * (battle_count)
        return total_exp

def calc_boss_exp(runs_left):

    #Define variables from config file
    mob_fleet_for_boss = config.get('Mob_Fleet', 'use_mob_fleet_for_boss')
    boss_exp = int(config.get('Boss_Fleet', 'boss_exp'))

    total_exp = 0

    if mob_fleet_for_boss == 'true':
        total_exp = 0
        return total_exp
    else:
        total_exp = runs_left * boss_exp
        return total_exp
