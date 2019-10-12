# Azur Lane Calculator
Lamar's Azur Lane EXP calculator for calculating how much EXP you'll get for farming a single map with a specified amount of oil.

## Running on Windows
1. Download the latest release from the releases page.
2. Run `azur-lane-calculator.exe` and follow the instructions.

## Running from Source Requirements
- Python 3.7+
- PrettyTable
Pretty table can be installed with pip by using the following command: `pip install PrettyTable`

## Running From Source
1. Clone or download the repo.
2. Navigate to the location you downloaded everything to with Command Prompt.
3. Run the command `python main.py` to launch the program and generate a config file.
4. Modify the variables in the config file.
5. Run `python main.py` again to run the program with your variables.

## Sample Output
```
You can run the map a total of 66 times.
Here is what your mob fleet will gain:
You can run the map a total of 66 more times.

Here is what your mob fleet will gain:
+-----------+------------+---------------+-----------+ 
| Ship Name | EXP Gained | Current Level | Est Level | 
+-----------+------------+---------------+-----------+ 
|  Leander  |   162518   |      120      |    120    | 
|   Aurora  |   162518   |      115      |    116    | 
|    Hood   |   487555   |      120      |    120    | 
+-----------+------------+---------------+-----------+ 
Your vanguard will gain a total of 325036 EXP.
Your main fleet will gain a total of 487555 EXP.       

Here is what your boss fleet will gain:
+------------+------------+---------------+-----------+
| Ship Name  | EXP Gained | Current Level | Est Level |
+------------+------------+---------------+-----------+
|   Sandy    |   32472    |      115      |    116    |
|  Belfast   |   32472    |      120      |    120    |
| Washington |   97482    |      115      |    116    |
|   Akashi   |   32472    |      112      |    113    |
|  Shouhou   |   32472    |      110      |    111    |
+------------+------------+---------------+-----------+
Your vanguard will gain a total of 64944 EXP.
Your main fleet will gain a total of 162426 EXP.
```
