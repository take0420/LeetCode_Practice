# Solution 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        total = 0
        for num in nums:
            total += num # 現在の合計を更新する
            running_sum.append(total) # 更新した合計をリストに追加する

        return running_sum
