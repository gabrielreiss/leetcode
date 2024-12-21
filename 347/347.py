class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = dict()
        
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        
        for num, freq in freq_dict.items():
            buckets[freq].append(num)
        
        result = []
        
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
