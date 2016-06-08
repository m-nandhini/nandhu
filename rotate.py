def rotate(self, nums, k):
        length = len(nums)
        if k>=length:
            k = k-length
        for i in range(k):
            nums.insert(0,nums.pop())
