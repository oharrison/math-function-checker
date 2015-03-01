# Mathematics - Function checker

This script is designed to take as input a file in which the ordered pairs in a relation are stored. The script outputs formatted text representing the domain and range of the given relation. Additionally, it tells the user
if the given relation represents a function or not.

# Sample input file
|Domain Value | Range Value |
|-------------|-------------|
| 1 | 2 |
| 3 | 5 |
| 7 | 10|

Each line represents an ordered pair in a relation.

NOTE: Only the numbers are in the file. Each pair of numbers in on a separate line. The numbers in a pair are separated by a comma

# Sample output file
| Domain | Range |
| ---- | ----- |
| 1.0  |  2.0  |
| 3.0	 | 	5.0  |
| 7.0	 |	10.0 |


# Things I learned while building this
1. How to use argparse module
2. How to use csv module
