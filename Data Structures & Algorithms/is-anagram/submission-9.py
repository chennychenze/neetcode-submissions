class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        store = [0] * 26

        for i, j in zip(s, t):
            store[ord(i) - ord('a')] += 1
            store[ord(j) - ord('a')] -= 1

        for k in store:
            if k != 0:
                return False

        return True