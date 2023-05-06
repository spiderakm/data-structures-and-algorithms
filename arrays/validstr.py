#Given a string S, composed of different combinations of '(' , ')', '{', '}', '[', ']'. The task is to verify the validity of the arrangement.
# link - https://practice.geeksforgeeks.org/problems/valid-expression1025/1?page=2&difficulty[]=1&category[]=Stack&sortBy=submissions

# Input:
# S = ()[]{}
# Output: 1
# Explanation: The arrangement is valid.

# bruteforce
def valid(s):
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) == 0


s = "()[]{}"
print(valid(s))


# optimise solution
def valid(s):
    stack = []
    brackets = {'(':')', '[':']', '{':'}'}
    for char in s:
        if char in brackets:
            stack.append(brackets[char])
        elif len(stack) > 0 and char == stack[-1]:
            stack.pop()
        else:
            return False
    return len(stack) == 0
    


s = "())({}"
print(valid(s))