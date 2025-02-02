# Contains Duplicate
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

    def _containsDuplicate(self, nums: List[int]) -> bool:
        """Quick to write solution"""
        return len(set(nums)) != len(nums)
