class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        stack = []
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                if pairs[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0