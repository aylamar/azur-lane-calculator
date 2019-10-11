import configparser

# Read config file & define values
config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

def mobv_one_exp(exp):
    name = config.get('Mob_Fleet_Ships', 'vanguard_ship_one')
    level = int(config.get('Mob_Fleet_Ships', 'vanguard_ship_one_level'))
    mvp = config.get('Mob_Fleet', 'mvp')

    if name == "none":
        return (0, name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)

def mobv_two_exp(exp):
    name = config.get('Mob_Fleet_Ships', 'vanguard_ship_two')
    level = int(config.get('Mob_Fleet_Ships', 'vanguard_ship_two_level'))
    mvp = config.get('Mob_Fleet', 'mvp')

    if name == "none":
        return (0, name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)

def mobv_three_exp(exp):
    name = config.get('Mob_Fleet_Ships', 'vanguard_ship_three')
    level = int(config.get('Mob_Fleet_Ships', 'vanguard_ship_three_level'))
    mvp = config.get('Mob_Fleet', 'mvp')

    if name == "none":
        return (0, name, level)
    elif name == mvp:
        exp += exp
        return (int(exp), name, level)
    else:
        return (int(exp), name, level)

def mobm_one_exp(exp):
    name = config.get('Mob_Fleet_Ships', 'main_ship_one')
    level = int(config.get('Mob_Fleet_Ships', 'main_ship_one_level'))
    mvp = config.get('Mob_Fleet', 'mvp')
    flagship = config.get('Mob_Fleet', 'flagship')

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

def mobm_two_exp(exp):
    name = config.get('Mob_Fleet_Ships', 'main_ship_two')
    level = int(config.get('Mob_Fleet_Ships', 'main_ship_two_level'))
    mvp = config.get('Mob_Fleet', 'mvp')
    flagship = config.get('Mob_Fleet', 'flagship')

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

def mobm_three_exp(exp):
    name = config.get('Mob_Fleet_Ships', 'main_ship_three')
    level = int(config.get('Mob_Fleet_Ships', 'main_ship_three_level'))
    mvp = config.get('Mob_Fleet', 'mvp')
    flagship = config.get('Mob_Fleet', 'flagship')

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
