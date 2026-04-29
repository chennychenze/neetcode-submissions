class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        store = [0] * 26

        for char1, char2 in zip(s, t):
            store[ord(char1) - ord('a')] += 1
            store[ord(char2) - ord('a')] -= 1

        for s in store:
            if s != 0:
                return False

        return True

        # time: O(n)
        # space: O(26) = O(1)

        
        