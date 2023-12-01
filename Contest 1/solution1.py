import sys

def doSomething(inval):
        stack = [] 
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in inval:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        if len(stack) == 0:
            return "YES" 
        else: 
            return "NO"

input = input()
output = doSomething(input)
print (output)
                                                                                                                            