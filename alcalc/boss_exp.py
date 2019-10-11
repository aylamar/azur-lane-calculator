import configparser

# Read config file & define values
config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def bossv_one_exp(exp):
    name = config.get('Boss_Fleet_Ships', 'vanguard_ship_one')
    level = int(config.get('Boss_Fleet_Ships', 'vanguard_ship_one_level'))
    mvp = config.get('Boss_Fleet', 'mvp')

    if name == "none":
        return (0, name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)

def bossv_two_exp(exp):
    name = config.get('Boss_Fleet_Ships', 'vanguard_ship_two')
    level = int(config.get('Boss_Fleet_Ships', 'vanguard_ship_two_level'))
    mvp = config.get('Boss_Fleet', 'mvp')

    if name == "none":
        return (0, name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)

def bossv_three_exp(exp):
    name = config.get('Boss_Fleet_Ships', 'vanguard_ship_three')
    level = int(config.get('Boss_Fleet_Ships', 'vanguard_ship_three_level'))
    mvp = config.get('Boss_Fleet', 'mvp')

    if name == "none":
        return (0, name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)

def bossm_one_exp(exp):
    name = config.get('Boss_Fleet_Ships', 'main_ship_one')
    level = int(config.get('Boss_Fleet_Ships', 'main_ship_one_level'))
    mvp = config.get('Boss_Fleet', 'mvp')
    flagship = config.get('Boss_Fleet', 'flagship')

    if name == "none":
        return (0, name, level)
    elif name == mvp and name == flagship:
        exp += (exp + (exp/2))
        return (int(exp), name, level)
    elif name == flagship:
        exp += (exp / 2)
        return (int(exp), name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)

def bossm_two_exp(exp):
    name = config.get('Boss_Fleet_Ships', 'main_ship_two')
    level = int(config.get('Boss_Fleet_Ships', 'main_ship_two_level'))
    mvp = config.get('Boss_Fleet', 'mvp')
    flagship = config.get('Boss_Fleet', 'flagship')

    if name == "none":
        return (0, name, level)
    elif name == mvp and name == flagship:
        exp += (exp + (exp/2))
        return (int(exp), name, level)
    elif name == flagship:
        exp += (exp / 2)
        return (int(exp), name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)

def bossm_three_exp(exp):
    name = config.get('Boss_Fleet_Ships', 'main_ship_three')
    level = int(config.get('Boss_Fleet_Ships', 'main_ship_three_level'))
    mvp = config.get('Boss_Fleet', 'mvp')
    flagship = config.get('Boss_Fleet', 'flagship')

    if name == "none":
        return (0, name, level)
    elif name == mvp and name == flagship:
        exp += (exp + (exp/2))
        return (int(exp), name, level)
    elif name == flagship:
        exp += (exp / 2)
        return (int(exp), name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)
