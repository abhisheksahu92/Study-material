# Parenthesis Checker
# Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
# For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.
#
# Example 1:
#
# Input:
# {([])}
#
# Output:
# true
#
# Explanation:
# { ( [ ] ) }. Same colored brackets can form
# balaced pairs, with 0 number of
# unbalanced bracket.

def ispair(exp):
    for x in '{([':
        if x == '{':
            if exp.count(x) == exp.count('}'):
                pass
            else:
                return False
        if x == '[':
            if exp.count(x) == exp.count(']'):
                pass
            else:
                return False
        if x == '(':
            if exp.count(x) == exp.count(')'):
                pass
            else:
                return False
    return True


for value in ['{([])}','()','([]']:
    print(f'Input is {value}')
    print(ispair(value))
