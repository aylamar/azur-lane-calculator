import configparser

config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')

def write_file():
    config.write(open('config.ini', 'w'))

def generate_config():
    config['General'] = {
    'level_entrance_cost': '10'
    }

    config['Mob_Fleet'] = {
        'mvp': 'Roon',
        'flagship': 'Unicorn',
        'fleet_oil_cost': '23',
        'battle_count': '5',
        'base_exp': '434',
        'use_mob_fleet_for_boss': 'true',
        'boss_exp': '615'
    }

    config['Mob_Fleet_Ships'] = {
        'vanguard_ship_one': 'Roon',
        'vanguard_ship_two': 'none',
        'vanguard_ship_three': 'none',
        'vanguard_ship_one_level': '82',
        'vanguard_ship_two_level': '1',
        'vanguard_ship_three_level': '1',
        'main_ship_one': 'Unicorn',
        'main_ship_two': 'none',
        'main_ship_three': 'none',
        'main_ship_one_level': '105',
        'main_ship_two_level': '1',
        'main_ship_three_level': '1'
    }

    #Boss Fleet
    config['Boss_Fleet'] = {
        'mvp': 'Sandy',
        'flagship': 'Washington',
        'fleet_oil_cost': '26',
        'boss_exp': '615'
    }

    config['Boss_Fleet_Ships'] = {
        'vanguard_ship_one': 'Sandy',
        'vanguard_ship_two': 'none',
        'vanguard_ship_three': 'none',
        'vanguard_ship_one_level': '115',
        'vanguard_ship_two_level': '1',
        'vanguard_ship_three_level': '1',
        'main_ship_one': 'Washington',
        'main_ship_two': 'none',
        'main_ship_three': 'none',
        'main_ship_one_level': '115',
        'main_ship_two_level': '1',
        'main_ship_three_level': '1'
    }

    write_file()
    exit()