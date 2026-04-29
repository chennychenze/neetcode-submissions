class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        store = [0] * 26

        for (c1, c2) in zip(s, t):
            store[ord(c1) - ord('a')] += 1
            store[ord(c2) - ord('a')] -= 1
        
        for n in store:
            if n != 0:
                return False
        
        return True

        # time: O(n)
        # space: O(26) = O(1)

        
        