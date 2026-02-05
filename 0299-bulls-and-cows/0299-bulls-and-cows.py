class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        secret = list(secret)
        guess = list(guess)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret[i] = None
                guess[i] = None

        for g in guess:
            if g is not None and g in secret:
                cows += 1
                secret[secret.index(g)] = None

        return f"{bulls}A{cows}B"
