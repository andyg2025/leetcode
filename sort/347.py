class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num]+=1

        sorted_map = sorted(map.items(), key=lambda x:-x[1])

        return [x[0] for x in sorted_map[:k]]
    