class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        myMap = defaultdict(list)

        def getAnagram(str):
            store = [0] * 26
            for c in str:
                store[ord(c) - ord('a')] += 1
            
            return tuple(store)

        for s in strs:
            anagram = getAnagram(s)
            myMap[anagram].append(s)

        return list(myMap.values())

        '''
        ✅ Time: O(n * k)

        n = len(strs), k = max length of a string

        Each string is processed in O(k) to count letters.

        ✅ Space: O(n * k)

        Up to n unique keys, each with strings of length up to k.

        store uses constant space O(26), but total space grows with input size.
        '''