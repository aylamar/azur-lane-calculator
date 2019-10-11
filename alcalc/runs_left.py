def runs():
    import configparser
    
    # Read config file & define values
    config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
    config.read('config.ini')

    #Define variables from config file
    mob_fleet_for_boss = config.get('Mob_Fleet', 'use_mob_fleet_for_boss')
    level_cost = int(config.get('General', 'level_entrance_cost'))
    mob_fleet_oil_cost = int(config.get('Mob_Fleet', 'fleet_oil_cost'))
    battle_count = int(config.get('Mob_Fleet', 'battle_count'))
    boss_fleet_oil_Cost = int(config.get('Boss_Fleet', 'fleet_oil_cost'))

    oil = int(input("How much oil do you currently have? "))

    #Math for calculating how many times map can be run
    if mob_fleet_for_boss == 'true':
        runs_left = oil / (level_cost + (mob_fleet_oil_cost * (battle_count + 1)))
    else:
        runs_left = oil / (level_cost + (mob_fleet_oil_cost * battle_count) + boss_fleet_oil_Cost)
    runs_left = int(runs_left)

    return runs_left, oil