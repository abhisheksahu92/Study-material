# Value equal to index value
# Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value.
#
# Example 1:
#
# Input:
# N = 5
# Arr[] = {15, 2, 45, 12, 7}
# Output: 2
# Explanation: Only Arr[2] = 2 exists here.
#
# Example 2:
#
# Input:
# N = 1
# Arr[] = {1}
# Output: 1
# Explanation: Here Arr[1] = 1 exists.

def valueEqualToIndex(arr):
    count = 0
    for x in range(len(arr)):
        if x+1 == arr[x]:
            count += 1
    return count

for value in [[15, 2, 45, 12, 7],[1]]:
    print(f'Input is {value}')
    print(valueEqualToIndex(value))