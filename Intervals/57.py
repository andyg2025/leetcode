class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        [start, end] = self.bs(intervals, newInterval)

        print(start, end)
        if end<start:
            return intervals

        if start>0 and intervals[start-1][1] >= newInterval[0]:
            start-=1
            newInterval[0] = intervals[start][0]

        if end < len(intervals) and intervals[end][0] <= newInterval[1]:
            newInterval[1]=intervals[end][1]
            end+=1

        return intervals[:start] + [newInterval] + intervals[end:]

    def bs(self, intervals, newInterval):
        result=[]
        l,r=0,len(intervals)
        while l<r:
            mid = (l+r)//2
            if intervals[mid][0] >= newInterval[0]:
                r=mid
            else:
                l=mid+1
        result.append(l)

        l,r=0,len(intervals)
        while l<r:
            mid = (l+r)//2
            if intervals[mid][1] >= newInterval[1]:
                r=mid
            else:
                l=mid+1
        result.append(l)

        return result