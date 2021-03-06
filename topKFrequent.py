#
#    Given a non-empty array of integers, return the k most frequent elements.
#
#    For example,
#    Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
#    Note:
#    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#
class Solution(object):
    @staticmethod
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = {}
        for n in nums:
            if n not in res:
                res[n] = 0
            res[n] = res[n]+1
        return [elem[0] for pos, elem in enumerate(sorted([(key, res[key]) for key in res], key=lambda x: x[1], reverse=True)) if pos < k]
