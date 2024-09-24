class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        left = []
        right = []

        for start, end in intervals:
            if start > newInterval[1]:
                right.append([start, end])
            elif end < newInterval[0]:
                left.append([start, end])
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)

        return left + [[newStart, newEnd]] + right