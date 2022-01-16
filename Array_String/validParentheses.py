class Solution:
    def isValid(self, s):
        my_stack = []
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                my_stack.append(s[i])
            else :
                if len(my_stack) == 0:
                    return False
                else:
                    c = my_stack[len(my_stack)-1]
                    if (c == '[' and s[i] == ']' )or(c == '(' and s[i] == ')' )or(c == '{' and s[i] == '}' ):
                        my_stack.pop()
                    else: 
                        return False
        return len(my_stack) == 0

st = Solution()
print(st.isValid("()"))
