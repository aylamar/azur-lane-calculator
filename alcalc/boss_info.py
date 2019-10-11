from alcalc.runs_left import runs
from alcalc.ship_exp import calc_boss_exp
from alcalc.boss_exp import bossv_one_exp, bossv_two_exp, bossv_three_exp, bossm_one_exp, bossm_two_exp, bossm_three_exp
from alcalc.levels import find_level, find_total_exp

def bossv_one_info(runs_left):
    exp = calc_boss_exp(runs_left)
    exp, name, level = bossv_one_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def bossv_two_info(runs_left):
    exp = calc_boss_exp(runs_left)
    exp, name, level = bossv_two_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def bossv_three_info(runs_left):
    exp = calc_boss_exp(runs_left)
    exp, name, level = bossv_three_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def bossm_one_info(runs_left):
    exp = calc_boss_exp(runs_left)
    exp, name, level = bossm_one_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def bossm_two_info(runs_left):
    exp = calc_boss_exp(runs_left)
    exp, name, level = bossm_two_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def bossm_three_info(runs_left):
    exp = calc_boss_exp(runs_left)
    exp, name, level = bossm_three_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

