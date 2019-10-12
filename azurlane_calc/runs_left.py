def runs():
    import configparser

    # Read config file & define values
    config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
    config.read('config.ini')

    #Define variables from config file
    levelCost = int(config.get("General", "levelCost"))
    battlesBeforeBoss = int(config.get("General", "battlesBeforeBoss"))
    mobForBoss = config.get("Mob Fleet General", "useMobForBoss")
    mobCost = int(config.get("Mob Fleet General", "oilCost"))
    bossCost = int(config.get("Boss Fleet General", "oilCost"))

    oil = int(input("How much oil do you currently have? "))

    #Math for calculating how many times map can be run
    if mobForBoss == 'true':
        runsLeft = oil / (levelCost + (mobCost * (battlesBeforeBoss + 1)))
    else:
        runs_left = oil / (levelCost + (mobCost * battlesBeforeBoss) + bossCost)
    return oil, int(runsLeft)