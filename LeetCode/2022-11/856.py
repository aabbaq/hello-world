class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for each in s:
            if each == '(':
                stack.append('(')
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                elif stack:
                    num =
                    while stack and stack[-1].isdigit():
                        num = stack.pop() * 2