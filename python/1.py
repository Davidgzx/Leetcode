class Solution(object):
    # 1136ms
    def twoSum(self, nums, target):
        rlist=[]
        for i in range(len(nums)):
            if i not in rlist:
                number=target-nums[i]
                if (number in nums and nums.index(number)!=i):
                    rlist.append(i)
                    rlist.append(nums.index(number))
                    break
        return rlist

    # 1124ms
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         number=target-nums[i]
    #         if (number in nums and nums.index(number)!=i):
    #             return [i,nums.index(number)]

    # 32ms
    # def twoSum(self, nums, target):
    #     dict = {}
    #     for i in range(len(nums)):
    #         if nums[i] in dict:
    #             return[dict[nums[i]],i]
    #         else :
    #             dict[target-nums[i]]=i
            