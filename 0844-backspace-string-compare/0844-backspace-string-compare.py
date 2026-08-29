class Solution:
    def backspaceCompare(self, s, t):

        def build(string):
            stack = []

            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)

            return stack

        return build(s) == build(t)