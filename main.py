import configparser, os, sys
from azurlane_calc.generate_config import generate_config
from azurlane_calc.mob_fleet import generate_mob
from azurlane_calc.boss_fleet import generate_boss
from azurlane_calc.runs_left import runs
from azurlane_calc.generate_table import generate_mob_table, generate_boss_table

#Create config file if one doesn't exist already
if not os.path.exists('config.ini'):
    generate_config()

#Calculate runsLeft
oil, runsLeft = runs()

#Generate fleet information
mobVang, mobMain = generate_mob(runsLeft)
bossVang, bossMain = generate_boss(runsLeft)

generate_mob_table(mobVang, mobMain)
generate_boss_table(bossVang, bossMain)