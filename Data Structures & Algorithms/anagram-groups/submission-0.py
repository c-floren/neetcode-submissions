from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            str_map[sorted_s].append(s)
            
        return str_map.values()
