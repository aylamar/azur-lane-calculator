import configparser, os, sys
from azurlane_calc.mob_fleet import generate_mob
from azurlane_calc.boss_fleet import generate_boss

from prettytable import PrettyTable

#Create config file if one doesn't exist already
#if not os.path.exists('config.ini'):
#    generate_config()

# Read config file
config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

#Generate fleet information
mobVang, mobMain = generate_mob()
bossVang, bossMain = generate_boss()

print(mobVang[0].name)
print(bossVang[0].name)

print(len(bossMain))
