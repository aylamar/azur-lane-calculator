def runs():
    import configparser
    from azurlane_calc import runs

    # Read config file & define values
    config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
    config.read('config.ini')

    #Define variables from config file
    mobForBoss = config.get('Mob_Fleet', 'use_mobForBoss')
    levelCost = int(config.get('General', 'level_entrance_cost'))
    mobOilCost = int(config.get('Mob_Fleet', 'fleet_oil_cost'))
    battlesBeforeBoss = int(config.get('Mob_Fleet', 'battlesBeforeBoss'))
    bossOilCost = int(config.get('Boss_Fleet', 'fleet_oil_cost'))

    oil = int(input("How much oil do you currently have? "))

    #Math for calculating how many times map can be run
    if mobForBoss == 'true':
        runs_left = oil / (levelCost + (mobOilCost * (battlesBeforeBoss + 1)))
    else:
        runs_left = oil / (levelCost + (mobOilCost * battlesBeforeBoss) + bossOilCost)
    runs_left = int(runs_left)

    return runs_left, oil