import configparser, os, sys

from prettytable import PrettyTable

from alcalc.generate_config import generate_config
from alcalc.runs_left import runs
from alcalc.mob_info import mobv_one_info, mobv_two_info, mobv_three_info, mobm_one_info, mobm_two_info, mobm_three_info
from alcalc.boss_info import bossv_one_info, bossv_two_info, bossv_three_info, bossm_one_info, bossm_two_info, bossm_three_info

#Create config file if one doesn't exist already
if not os.path.exists('config.ini'):
    generate_config()

# Read config file
config = configparser.ConfigParser(allow_no_value=True, comment_prefixes='#')
config.read('config.ini')

#Query the amount of runs_left
runs_left, oil = runs()
runs_left = int(runs_left)

#Generate all mob fleet values
mobv_one_name, mobv_one_exp, mobv_one_level, mobv_one_final_level = mobv_one_info(runs_left)
mobv_two_name, mobv_two_exp, mobv_two_level, mobv_two_final_level = mobv_two_info(runs_left)
mobv_three_name, mobv_three_exp, mobv_three_level, mobv_three_final_level = mobv_three_info(runs_left)
mobm_one_name, mobm_one_exp, mobm_one_level, mobm_one_final_level = mobm_one_info(runs_left)
mobm_two_name, mobm_two_exp, mobm_two_level, mobm_two_final_level = mobm_two_info(runs_left)
mobm_three_name, mobm_three_exp, mobm_three_level, mobm_three_final_level = mobm_three_info(runs_left)

#Mob Table
mob_table = PrettyTable()
mob_table.field_names = ["Ship Name", "EXP Gained", "Current Level", "Est. Level"]
if mobv_one_name != 'none':
    mob_table.add_row([mobv_one_name, mobv_one_exp, mobv_one_level, mobv_one_final_level])
if mobv_two_name != 'none':
    mob_table.add_row([mobv_two_name, mobv_two_exp, mobv_two_level, mobv_two_final_level])
if mobv_three_name != 'none':
    mob_table.add_row([mobv_three_name, mobv_three_exp, mobv_three_level, mobv_three_final_level])
if mobm_one_name != 'none':
    mob_table.add_row([mobm_one_name, mobm_one_exp, mobm_one_level, mobm_one_final_level])
if mobm_two_name != 'none':
    mob_table.add_row([mobm_two_name, mobm_two_exp, mobm_two_level, mobm_two_final_level])
if mobm_three_name != 'none':
    mob_table.add_row([mobm_three_name, mobm_three_exp, mobm_three_level, mobm_three_final_level])

print()
print("You can run the map a total of", runs_left, "times.")
print("Here is what your mob fleet will gain:")
print(mob_table)

mobv_total_exp = mobv_one_exp + mobv_two_exp + mobv_three_exp
mobm_total_exp = mobm_one_exp + mobm_two_exp + mobm_three_exp

print("Your mob fleet's vanguard will earn a total of", mobv_total_exp, "EXP.")
print("Your mob fleet's main fleet will earn a total of", mobm_total_exp, "EXP.")

#Initialize variable to check if the boss fleet is even used.
mob_for_boss = config.get('Mob_Fleet', 'use_mob_fleet_for_boss')

#Generate all boss fleet values
if (mob_for_boss != "true"):
    bossv_one_name, bossv_one_exp, bossv_one_level, bossv_one_final_level = bossv_one_info(runs_left)
    bossv_two_name, bossv_two_exp, bossv_two_level, bossv_two_final_level = bossv_two_info(runs_left)
    bossv_three_name, bossv_three_exp, bossv_three_level, bossv_three_final_level = bossv_three_info(runs_left)
    bossm_one_name, bossm_one_exp, bossm_one_level, bossm_one_final_level = bossm_one_info(runs_left)
    bossm_two_name, bossm_two_exp, bossm_two_level, bossm_two_final_level = bossm_two_info(runs_left)
    bossm_three_name, bossm_three_exp, bossm_three_level, bossm_three_final_level = bossm_three_info(runs_left)

#Boss Table
if (mob_for_boss != "true"):
    boss_table = PrettyTable()
    boss_table.field_names = ["Ship Name", "EXP Gained", "Current Level", "Est. Level"]
    if bossv_one_name != 'none':
        boss_table.add_row([bossv_one_name, bossv_one_exp, bossv_one_level, bossv_one_final_level])
    if bossv_two_name != 'none':
        boss_table.add_row([bossv_two_name, bossv_two_exp, bossv_two_level, bossv_two_final_level])
    if bossv_three_name != 'none':
        boss_table.add_row([bossv_three_name, bossv_three_exp, bossv_three_level, bossv_three_final_level])
    if bossm_one_name != 'none':
        boss_table.add_row([bossm_one_name, bossm_one_exp, bossm_one_level, bossm_one_final_level])
    if bossm_two_name != 'none':
        boss_table.add_row([bossm_two_name, bossm_two_exp, bossm_two_level, bossm_two_final_level])
    if bossm_three_name != 'none':
        boss_table.add_row([bossm_three_name, bossm_three_exp, bossm_three_level, bossm_three_final_level])

    print()
    print("Here is what your boss fleet will gain:")
    print(boss_table)

    bossv_total_exp = bossv_one_exp + bossv_two_exp + bossv_three_exp
    bossm_total_exp = bossm_one_exp + bossm_two_exp + bossm_three_exp

    print("Your boss fleet's vanguard will earn a total of", bossv_total_exp, "EXP.")
    print("Your boss fleet's main fleet will earn a total of", bossm_total_exp, "EXP.")

print()
input("Press Enter to exit the program...")