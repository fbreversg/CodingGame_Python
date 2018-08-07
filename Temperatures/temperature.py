import sys
import math

goal = 10000

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
   
    if abs(t) < abs(goal) or abs(t) == abs(goal) and goal < t: 
        goal = t
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
if goal==10000: 
    goal = 0
print(goal)