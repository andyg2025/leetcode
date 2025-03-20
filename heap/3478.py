import heapq

def findMaxSum(nums1, nums2, k):
            new_nums = [[value, index] for index, value in enumerate(nums1)]
            new_nums.sort()
            result = [0] * len(nums1)
            temp = []
            cur_sum = 0
            heap = []

            for val, i in new_nums:
                if not temp:
                    temp = [i]
                    continue
                if nums1[temp[0]] == val:
                    temp.append(i)
                    result[i] = cur_sum
                else:
                    for index in temp:
                        if len(heap) == k and heap[0] > nums2[index]:
                            continue
                        heapq.heappush(heap, nums2[index])
                        cur_sum += nums2[index]
                        if len(heap) > k:
                            cur_sum -= heapq.heappop(heap)

                    # for index in temp:
                    #     heapq.heappush(heap, nums2[index])
                    #     cur_sum+=nums2[index]
                    # while len(heap) > k:
                    #     cur_sum -= heapq.heappop(heap)
                    
                    result[i] = cur_sum
                    temp = [i]

            return result