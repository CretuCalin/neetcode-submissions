class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        close_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        i = 0
        for i in range(len(s)):
            if s[i] in open_to_close:
                stack.append(s[i])
            if s[i] in close_to_open:
                if len(stack) == 0:
                    return False
                open_paran = stack.pop()
                if open_paran != close_to_open[s[i]]:
                    return False
        
        if len(stack) != 0:
            return False

        return True
