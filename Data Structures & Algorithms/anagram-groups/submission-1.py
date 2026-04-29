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