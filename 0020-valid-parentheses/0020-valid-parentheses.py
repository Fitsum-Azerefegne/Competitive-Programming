class Solution:
    def isValid(self, s: str) -> bool:
        bracket_hash = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for bracket in s:
            if bracket in bracket_hash.keys():
                stack.append(bracket)
            else:
                if stack:
                    prev = stack.pop()
                    if bracket_hash[prev] != bracket:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False
       