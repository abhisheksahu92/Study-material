# Searching in an array where adjacent differ by at most k

# A step array is an array of integer where each element has a difference of at most k with its neighbor. Given a key x, we need to find the index value of x if multiple element exist return the first occurrence of the key.
#
# Examples:
#
# Input : arr[] = {4, 5, 6, 7, 6}
#            k = 1
#            x = 6
# Output : 2
# The first index of 6 is 2.
#
# Input : arr[] = {20, 40, 50, 70, 70, 60}
#           k = 20
#           x = 60
# Output : 5
# The index of 60 is 5

def diffatmost(li,k,x):
    for y in range(len(li)):
        if li[y] == x:
            if y == len(li) - 1:
                return y if abs(li[y-1]-li[y]) <= k else -1
            elif y == 0:
                return y if abs(li[y + 1] - li[y]) <= k else -1
            else:
                return y if abs(li[y + 1] - li[y]) <= k and abs(li[y-1]-li[y]) <= k else -1

for value in [[[4,5,6,7,6],1,6],[[20, 40, 50, 70, 70, 60],20,60]]:
    print(f'Input is {value}')
    print(diffatmost(*value))