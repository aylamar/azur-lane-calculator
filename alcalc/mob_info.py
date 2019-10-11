from alcalc.runs_left import runs
from alcalc.ship_exp import calc_mob_exp
from alcalc.mob_exp import mobv_one_exp, mobv_two_exp, mobv_three_exp, mobm_one_exp, mobm_two_exp, mobm_three_exp
from alcalc.levels import find_level, find_total_exp

def mobv_one_info(runs_left):
    exp = calc_mob_exp(runs_left)
    exp, name, level = mobv_one_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def mobv_two_info(runs_left):
    exp = calc_mob_exp(runs_left)
    exp, name, level = mobv_two_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def mobv_three_info(runs_left):
    exp = calc_mob_exp(runs_left)
    exp, name, level = mobv_three_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def mobm_one_info(runs_left):
    exp = calc_mob_exp(runs_left)
    exp, name, level = mobm_one_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def mobm_two_info(runs_left):
    exp = calc_mob_exp(runs_left)
    exp, name, level = mobm_two_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

def mobm_three_info(runs_left):
    exp = calc_mob_exp(runs_left)
    exp, name, level = mobm_three_exp(exp)

    final_exp = find_total_exp(level) + exp
    final_level = find_level(final_exp)

    return name, exp, level, final_level

