// [문제 링크]: https://www.acmicpc.net/problem/21612

# Input: Boiling temperature B
B = int(input().strip())
​
# Calculate atmospheric pressure P
P = 5 * B - 400
​
# Determine if below sea level, at sea level, or above sea level
if P > 100:
    sea_level_indicator = -1
elif P < 100:
    sea_level_indicator = 1
else:
    sea_level_indicator = 0
​
# Output the results
print(P)
print(sea_level_indicator)
​