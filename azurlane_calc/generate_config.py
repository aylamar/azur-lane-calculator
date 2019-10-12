import configparser

config = configparser.RawConfigParser(allow_no_value=True, comment_prefixes='#')
config.optionxform = str

def write_file():
    config.write(open('config.ini', 'w'))

def generate_config():
    config['General'] = {
    'levelCost': '10',
    'battlesBeforeBoss': '5',
    'baseEXP': '342',
    'sRankNormal': 'true',
    'bossEXP': '428',
    'sRankBoss': 'true'
    }

    config['Mob Fleet General'] = {
    'useMobForBoss': 'true',
    'oilCost': '23',
    }

    config['Mob Vanguard Ship 1'] = {
    'name': 'Roon',
    'level': '83',
    'mvp': 'true',
    'hasMoraleBonus': 'true',
    }

    config['Mob Vanguard Ship 2'] = {
    'name': 'none',
    'level': '0',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Mob Vanguard Ship 3'] = {
    'name': 'none',
    'level': '0',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Mob Main Ship 1'] = {
    'name': 'Unicorn',
    'level': '105',
    'mvp': 'false',
    'flagship': 'true',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Mob Main Ship 2'] = {
    'name': 'none',
    'level': '0',
    'mvp': 'false',
    'flagship': 'false',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Mob Main Ship 3'] = {
    'name': 'none',
    'level': '0',
    'mvp': 'false',
    'flagship': 'false',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Boss Fleet General'] = {
    'oilCost': '26',
    }

    config['Boss Vanguard Ship 1'] = {
    'name': 'Sandy',
    'level': '115',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Boss Vanguard Ship 2'] = {
    'name': 'none',
    'level': '0',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Boss Vanguard Ship 3'] = {
    'name': 'none',
    'level': '0',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Boss Main Ship 1'] = {
    'name': 'Washington',
    'level': '115',
    'flagship': 'true',
    'mvp': 'true',
    'hasMoraleBonus': 'true',
    }

    config['Boss Main Ship 2'] = {
    'name': 'none',
    'level': '0',
    'flagship': 'true',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    config['Boss Main Ship 3'] = {
    'name': 'none',
    'level': '0',
    'flagship': 'true',
    'mvp': 'false',
    'hasMoraleBonus': 'true',
    }

    write_file()
    print("Config file has been generated, please modify the values in the file then startup the program again.")
    input("Press Enter to exit the program..")
    exit()
