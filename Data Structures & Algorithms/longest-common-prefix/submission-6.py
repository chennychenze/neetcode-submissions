class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        baseStr = strs[0]

        for i in range(len(baseStr)):
            for s in strs:
                if i == len(s) or baseStr[i] != s[i]:
                    return baseStr[:i]

        return strs[0]
        # time: O(m * n)  m is size of strs, n is size of the smallest s 
        # space: O(1)