# Time:  O(nlogn)
# Space: O(n)

import heapq


# codeforces, https://codeforces.com/problemset/problem/1303/D
# heap, greedy
class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        if total < target:
            return -1

        result = 0
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        while heapq:
            if not target:
                break
            x = -heapq.heappop(max_heap)
            if x <= target:
                target -= x
                total -= x
            elif total-x >= target:
                total -= x
            else:
                heapq.heappush(max_heap, -x//2)
                heapq.heappush(max_heap, -x//2)
                result += 1
        return result


# Time:  O(nlogr)
# Space: O(logr)
# codeforces, https://codeforces.com/problemset/problem/1303/D
# bitmasks, greedy
class Solution2(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def floor_log2_x(x):
            return x.bit_length()-1

        if sum(nums) < target:
            return -1

        cnt = [0]*(floor_log2_x(max(nums))+1)
        for x in nums:
            cnt[floor_log2_x(x)] += 1
        result = i = 0
        while i < len(cnt):
            if target&(1<<i):
                if not cnt[i]:
                    j = next(j for j in xrange(i, len(cnt)) if cnt[j])
                    result += j-i
                    j = i
                    cnt[i] -= 1
                    continue
                cnt[i] -= 1
            if i+1 < len(cnt):
                cnt[i+1] += cnt[i]//2
            i += 1
        return result
