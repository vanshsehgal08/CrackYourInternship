class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            count=[0]*26 # a......z

            for c in s:
                count[ord(c) - ord("a")] += 1 # a is 0 and z is 25

            res[tuple(count)].append(s)
        
        return res.values()
        