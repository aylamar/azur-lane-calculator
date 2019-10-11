# Azur Lane Calculator
Lamar's Azur Lane EXP calculator for calculating how much EXP you'll get for farming a single map with a specified amount of oil.

## Requirements
- Python 3.7+
- PrettyTable
Pretty table can be installed with pip by using the following command: `pip install PrettyTable`

## Instructions
1. Clone or download the repo.
2. Navigate to the location you downloaded everything to with Command Prompt.
3. Run the command `python main.py` to launch the program and generate a config file.
4. Modify the variables in the config file.
5. Run `python main.py` again to run the program with your variables.

## Sample Output
```
You can run the map a total of 66 times.
Here is what your mob fleet will gain:
+-----------+------------+---------------+------------+
| Ship Name | EXP Gained | Current Level | Est. Level |
+-----------+------------+---------------+------------+
|    Roon   |   286440   |       82      |     95     |
|  Unicorn  |   214830   |      105      |    108     |
+-----------+------------+---------------+------------+
Your mob fleet's vanguard will earn a total of 286440 EXP.
Your mob fleet's main fleet will earn a total of 214830 EXP.

Here is what your boss fleet will gain:
+------------+------------+---------------+------------+
| Ship Name  | EXP Gained | Current Level | Est. Level |
+------------+------------+---------------+------------+
|   Sandy    |   81180    |      115      |    116     |
| Washington |   60885    |      115      |    116     |
+------------+------------+---------------+------------+
Your boss fleet's vanguard will earn a total of 81180 EXP.
Your boss fleet's main fleet will earn a total of 60885 EXP.
```
## Sample Config with Explanations
```
[General]
#Cost of entering level
level_entrance_cost = 10

[Mob_Fleet]
#Name of MVP and flagship, use the exact name listed in Mob_Fleet_Ships
mvp = Roon
flagship = Unicorn
fleet_oil_cost = 26
#Total battle count before fighting the boss
battle_count = 5
#Use the base EXP earned not including MVP or flagship, but including any happiness bonuses
#If fighting fleets with different exp payouts, use an average or the one fought the most
base_exp = 369
#true if use mob fleet to fight boss, otherwise false
use_mob_fleet_for_boss = false
#Use the base EXP earned not including MVP or flagship, but including any happiness bonuses
boss_exp = 513

[Mob_Fleet_Ships]
#Use underscores instead of spaces for multi word ship names
vanguard_ship_one = Roon
vanguard_ship_two = none
vanguard_ship_three = none
vanguard_ship_one_level = 82
vanguard_ship_two_level = 100
vanguard_ship_three_level = 100
main_ship_one = Unicorn
main_ship_two = none
main_ship_three = none
main_ship_one_level = 104
main_ship_two_level = 100
main_ship_three_level = 100

[Boss_Fleet]
mvp = Sandy
flagship = Washington
fleet_oil_cost = 39
boss_exp = 513

[Boss_Fleet_Ships]
vanguard_ship_one = Sandy
vanguard_ship_two = none
vanguard_ship_three = none
vanguard_ship_one_level = 115
vanguard_ship_two_level = 100
vanguard_ship_three_level = 100
main_ship_one = Washington
main_ship_two = none
main_ship_three = none
main_ship_one_level = 115
main_ship_two_level = 100
main_ship_three_level = 100
```
