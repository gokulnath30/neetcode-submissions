from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        freq_map = Counter(nums)
        
        # Step 2: Get the k most common elements
        most_common = freq_map.most_common(k)
        
        # Step 3: Extract just the elements (ignoring the frequencies)
        return [elem for elem, freq in most_common]


